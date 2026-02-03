# Protocol Converter MVP (Local)

## Goal
User uploads a PDF and downloads a converted DOCX.

## MVP Flow
1. User opens a local web page
2. User selects a PDF
3. User clicks Convert
4. System returns a DOCX download
5. Errors are shown clearly

## Constraints
- PDF only, max 20MB
- Output: DOCX
- Local-first MVP
- Do NOT rewrite existing pipeline logic; wrap/reuse it

## Acceptance Criteria
- One command starts backend
- Conversion works end-to-end via browser locally

