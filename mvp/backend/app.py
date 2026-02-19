import logging
import os
import re
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


def _add_markdown_table_to_doc(doc, table_lines: list) -> None:
    """Create a python-docx Table from markdown table lines."""
    rows = []
    for line in table_lines:
        line = line.strip()
        if not line.startswith('|'):
            continue
        # Skip separator row — inner content is only dashes, colons, spaces
        inner = line.strip('|')
        if re.match(r'^[\s\-|:]+$', inner):
            continue
        cells = [c.strip() for c in line.split('|')[1:-1]]
        rows.append(cells)

    if not rows:
        return

    num_cols = max(len(row) for row in rows)
    tbl = doc.add_table(rows=len(rows), cols=num_cols)
    tbl.style = 'Table Grid'

    for r_idx, row_data in enumerate(rows):
        row = tbl.rows[r_idx]
        for c_idx in range(num_cols):
            cell_text = row_data[c_idx] if c_idx < len(row_data) else ''
            cell = row.cells[c_idx]
            cell.text = cell_text
            if r_idx == 0:
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True


def markdown_to_docx(md_content: str, output_path: Path):
    """Convert markdown to docx using python-docx."""
    from docx import Document

    doc = Document()
    lines = md_content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Detect markdown table
        if line.strip().startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            _add_markdown_table_to_doc(doc, table_lines)
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
        
        try:
            markdown_to_docx(final_md, docx_path)
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