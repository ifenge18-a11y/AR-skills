# Zotero Literature Workflow

## Use For

Use this reference when the user asks to search Google Scholar or CNKI, download literature, import records into Zotero, export BibTeX/RIS, sync citation keys, or inspect PDFs and full text.

## Compliance Rules

- Default to a semi-automated, permission-respecting workflow.
- Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation.
- Stop and ask the user to take over when a login, CAPTCHA, payment, or access gate appears.
- Download PDFs only when the user has access rights and explicitly asks for download/import.
- Before writing to Zotero, confirm the exact records and target collection unless the user already gave explicit import instructions.
- Mark literature records as verified, partially verified, or unverified.

## Tool Routing

- Use Browser or Chrome for web search and page interaction. Prefer Chrome when the user's existing login, cookies, or institutional access are needed.
- Use the Zotero plugin for local Zotero status, search, import, export, citation-key sync, and full-text reads from existing library items.
- Use Google Scholar and CNKI as discovery surfaces, not as sources to scrape aggressively.

## Google Scholar Workflow

1. Search by construct, setting, journal, author, and date terms.
2. Prefer opening publisher, SSRN, NBER, institutional repository, or journal pages for verification.
3. Export citation metadata through BibTeX/RIS when available.
4. Download a PDF only from an accessible publisher, repository, or author-hosted source that the user is allowed to access.
5. Import confirmed BibTeX/RIS records into Zotero.
6. Record source URL, access date, verification status, and unresolved metadata gaps.

## CNKI Workflow

1. Use Chrome when CNKI access depends on the user's login or institution.
2. Search by Chinese keywords, author names, journal names, CSSCI filters, and publication years.
3. Prioritize CSSCI economics and management journals, especially Economic Research Journal, Management World, Accounting Research, Management Review, Journal of Financial Research, and China Industrial Economics.
4. Export CNKI citation records when available.
5. Download PDFs only when the user has access rights.
6. Import confirmed records or RIS/BibTeX files into Zotero, then verify title, authors, journal, year, volume, issue, pages, DOI, and URL.

## Zotero Import Workflow

1. Check Zotero readiness with the Zotero helper before operating the library.
2. Search the local library before importing to avoid duplicates.
3. Confirm target collection and record list before `import-bibtex` or `import-ris`, unless the user explicitly requested import.
4. After import, report title, creators, year, Zotero item key, and BibTeX key when available.
5. Keep a note of records that need manual metadata cleanup.
