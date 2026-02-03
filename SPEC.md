# Protocol Converter MVP (Local)

## Goal
User uploads a PDF and gets a converted DOCX back immediately (download).

## MVP Flow
1. User opens a local web page
2. User selects a PDF
3. User clicks Convert
4. The system returns a DOCX for download
5. Errors are shown clearly

## Constraints
- Input: PDF only
- Output: DOCX
- Max file size: 20MB
- No auth for MVP
- Conversion logic must be reused as-is (no rewrite)

## Acceptance Criteria
- One command starts the backend
- User can convert via browser UI end-to-end locally
- Clear error handling
