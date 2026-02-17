import logging
import os
import tempfile
import shutil
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import existing pipeline functions
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from run_batch import (
    extract_text_from_pdf,
    clean_text,
    convert_to_protocol_markdown,
    finalize_protocol_md,
    generate_flags_md,
    append_flags_summary
)

load_dotenv()

app = FastAPI()

@app.get("/health")
def health():
    logger.info("Health check pinged")
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

# CORS: allow Next.js frontend in dev and production
# Set EXTRA_CORS_ORIGINS env var for additional origins (comma-separated)
_origins = [
    "http://localhost:3000",
    "https://protocolfoundry.io",
    "https://www.protocolfoundry.io",
]
_extra = os.getenv("EXTRA_CORS_ORIGINS", "")
if _extra:
    _origins.extend([o.strip() for o in _extra.split(",") if o.strip()])

app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20MB


def markdown_to_docx_pypandoc(md_content: str, output_path: Path) -> bool:
    """Convert markdown to docx using pypandoc. Returns True on success."""
    try:
        import pypandoc
        pypandoc.convert_text(
            md_content,
            'docx',
            format='md',
            outputfile=str(output_path)
        )
        return True
    except (ImportError, RuntimeError, OSError):
        return False


def markdown_to_docx_fallback(md_content: str, output_path: Path):
    """Fallback markdown to docx conversion using python-docx."""
    from docx import Document
    from docx.shared import Pt
    
    doc = Document()
    lines = md_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Skip empty lines
        if not line.strip():
            i += 1
            continue
        
        # Handle headings
        if line.startswith('# '):
            doc.add_heading(line[2:], level=1)
        elif line.startswith('## '):
            doc.add_heading(line[3:], level=2)
        elif line.startswith('### '):
            doc.add_heading(line[4:], level=3)
        elif line.startswith('#### '):
            doc.add_heading(line[5:], level=4)
        
        # Handle bullet lists
        elif line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            doc.add_paragraph(text, style='List Bullet')
        
        # Handle numbered lists
        elif len(line) > 2 and line[0].isdigit() and line[1:3] in ['. ', ') ']:
            text = line.split('. ', 1)[-1].split(') ', 1)[-1]
            doc.add_paragraph(text, style='List Number')
        
        # Regular paragraph
        else:
            doc.add_paragraph(line)
        
        i += 1
    
    doc.save(str(output_path))


@app.post("/convert")
async def convert_pdf(file: UploadFile = File(...)):
    """
    Convert uploaded PDF to protocol DOCX.
    """
    # Validate file type
    if not file.filename or not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    # Read file content
    file_content = await file.read()
    
    # Validate file size
    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File size exceeds 20MB limit")

    file_size_mb = len(file_content) / (1024 * 1024)
    logger.info(f"[{datetime.now()}] Conversion started: {file.filename} ({file_size_mb:.2f} MB)")

    # Create temporary directory
    temp_dir = Path(tempfile.mkdtemp())
    
    try:
        # Save uploaded PDF
        pdf_path = temp_dir / "input.pdf"
        with open(pdf_path, 'wb') as f:
            f.write(file_content)
        
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise HTTPException(status_code=500, detail="OPENAI_API_KEY not configured")
        
        client = OpenAI(api_key=api_key)
        
        # Load contract
        contract_path = Path(__file__).parent.parent.parent / "contract.md"
        if not contract_path.exists():
            raise HTTPException(status_code=500, detail="contract.md not found in repository root")
        
        with open(contract_path, 'r', encoding='utf-8') as f:
            contract = f.read()
        
        # Run pipeline
        try:
            raw_text = extract_text_from_pdf(pdf_path)
            cleaned_text = clean_text(raw_text)
            protocol_md = convert_to_protocol_markdown(client, contract, cleaned_text)
            protocol_md = finalize_protocol_md(protocol_md)
            flags_md = generate_flags_md(client, cleaned_text, protocol_md)
            final_md = append_flags_summary(protocol_md, flags_md)
        except Exception as e:
            logger.error(f"[{datetime.now()}] Pipeline failed: {file.filename} - {e}")
            raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")
        
        # Convert to DOCX
        docx_path = temp_dir / "output.docx"
        
        # Try pypandoc first
        if not markdown_to_docx_pypandoc(final_md, docx_path):
            # Fallback to python-docx
            try:
                markdown_to_docx_fallback(final_md, docx_path)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"DOCX conversion failed: {str(e)}")
        
        logger.info(f"[{datetime.now()}] Conversion completed: {file.filename}")

        # Return file
        return FileResponse(
            path=str(docx_path),
            filename="protocol.docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    
    except HTTPException:
        # Clean up temp directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise
    
    except Exception as e:
        logger.error(f"[{datetime.now()}] Unexpected error: {file.filename} - {e}")
        # Clean up temp directory
        shutil.rmtree(temp_dir, ignore_errors=True)
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")