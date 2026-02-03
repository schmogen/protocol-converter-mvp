# AI Task – Build Local MVP Wrapper

## Objective
Wrap the existing converter into a local web MVP:
- Backend endpoint: POST /convert (multipart form upload: file)
- Response: converted .docx file download

## Requirements
- Do not rewrite conversion logic
- Reuse existing scripts/functions (likely convert_protocol.py)
- Add a small FastAPI app to call the converter
- Add a minimal frontend page (static HTML) with upload + convert button
- Show status states and errors
- Add file validation: PDF only, max 20MB
- Provide commands to run locally on Windows Git Bash

## Output Format (MANDATORY)
- Show final file tree
- For every new/modified file: provide FULL file contents
- Provide exact commands to install deps and run
