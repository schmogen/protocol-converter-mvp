# AI Task – Build Local MVP Wrapper

## Objective
Create a local web MVP wrapper around the existing pipeline.

## Requirements
- Do NOT rewrite the LLM logic or extraction logic
- Reuse functions from run_batch.py where possible:
  - extract_text_from_pdf, clean_text
  - convert_to_protocol_markdown, finalize_protocol_md
  - generate_flags_md, append_flags_summary
- Add FastAPI backend: POST /convert (multipart upload: file)
- Validate: PDF only, <= 20MB
- Use repo-root contract.md as contract
- Return a .docx download (Markdown -> DOCX)
  - Prefer pypandoc (pandoc may be missing)
  - Provide fallback using python-docx if pandoc not available
- Add minimal frontend page with file picker + Convert + status + download
- Provide exact Windows Git Bash commands to run locally

## Output Format (MANDATORY)
- Final file tree
- FULL contents for every new/modified file
- Exact commands to install and run

