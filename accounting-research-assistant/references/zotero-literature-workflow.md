# Zotero Handoff

## Use For

Use this note only to route reference-management work out of `accounting-research-assistant`.

The accounting skill may identify which literature matters, how papers relate to the research question, and which records still need verification. Zotero owns the operational reference workflow:

- Importing and exporting BibTeX, RIS, ENW, or other citation files.
- Managing Zotero collections, citation keys, duplicate records, and metadata cleanup.
- Working with local PDFs, attachments, notes, and full-text library search.
- Downloading or attaching PDFs when the user has access rights.

## Boundary Rule

When the user asks for Zotero operations, switch to the Zotero workflow or plugin. Do not implement those operations inside the accounting research skill.

The accounting skill may provide a handoff list:

| Record | Why it matters | Verification status | Suggested Zotero action |
|---|---|---|---|

Keep "Suggested Zotero action" descriptive, such as `import if verified`, `check duplicate`, `attach accessible PDF`, or `clean metadata`; let Zotero perform the action.

## Compliance

Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation. Stop and ask the user to handle login, CAPTCHA, payment, or permission gates.
