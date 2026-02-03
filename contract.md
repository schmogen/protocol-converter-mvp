# Protocol Output Contract (v1)

Convert the input text into a clean lab protocol in Markdown.

## Rules
- Do NOT invent or add scientific content.
- Preserve all numbers/units/times/temperatures exactly.
- If something is unclear, write “[CHECK]” rather than guessing.

## Output format
# Title
(Use the title if present; otherwise write a reasonable title.)

## Objective
1–3 sentences.

## Materials
Bulleted list. Only include items present in the source.

## Procedure
Numbered steps. Keep steps short and clear.
- Use sub-bullets for sub-steps.
- Keep the original ordering.

## Notes
Optional. Include warnings/cautions/tips only if present.

## Review Checklist (always include)
At the end of the protocol, include a checklist in Markdown with these items:

## Review Checklist
- [ ] Growth conditions verified (temperature, CO2/O2, time)
- [ ] Media composition and volumes verified
- [ ] Mixing parameters verified (rpm/RCF, time)
- [ ] Incubation times verified
- [ ] Centrifugation settings verified (RCF, time, temp)
- [ ] Step order confirmed against source
- [ ] Any ambiguous values flagged with [CHECK]