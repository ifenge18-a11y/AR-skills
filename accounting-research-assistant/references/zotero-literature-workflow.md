# Zotero Literature Workflow

## Use For

Use this reference when the user asks to search OpenAlex, Google Scholar, or CNKI, download literature, import records into Zotero, export BibTeX/RIS, sync citation keys, or inspect PDFs and full text.

## Compliance Rules

- Default to a semi-automated, permission-respecting workflow.
- Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation.
- Stop and ask the user to take over when a login, CAPTCHA, payment, or access gate appears.
- Download PDFs only when the user has access rights and explicitly asks for download/import.
- Before writing to Zotero, confirm the exact records and target collection unless the user already gave explicit import instructions.
- Mark literature records as verified, partially verified, or unverified.

## Tool Routing

- Use OpenAlex for preliminary English literature discovery, metadata screening, DOI lookup, venue filtering, and citation trail expansion.
- Use Browser or Chrome for web search and page interaction. Prefer Chrome when the user's existing login, cookies, or institutional access are needed.
- Use the Zotero plugin for local Zotero status, search, import, export, citation-key sync, and full-text reads from existing library items.
- Use Google Scholar and CNKI as discovery surfaces, not as sources to scrape aggressively.

## OpenAlex Workflow

1. Use OpenAlex first for English literature discovery unless the user asks only for Chinese literature.
2. Search by construct keywords, synonyms, authors, title fragments, DOI, venue, and year range.
3. Filter candidates by accounting relevance, venue quality, publication year, DOI presence, and abstract/concept fit.
4. Use OpenAlex records to build the initial candidate list, then verify important facts through publisher pages, journal pages, SSRN, NBER, institutional repositories, or Google Scholar.
5. Record OpenAlex work URL, DOI, venue, publication year, and verification status when available.

## Google Scholar Workflow

1. Use Chrome to search Google Scholar for latest English literature, online-first papers, working papers, and citation trails.
2. Search by construct, setting, journal, author, and date terms.
3. Prefer opening publisher, SSRN, NBER, institutional repository, or journal pages for verification.
4. Export citation metadata through BibTeX/RIS when available.
5. Download a PDF only from an accessible publisher, repository, or author-hosted source that the user is allowed to access.
6. Import confirmed BibTeX/RIS records into Zotero.
7. Record source URL, access date, verification status, and unresolved metadata gaps.

## CNKI Workflow

1. Use Chrome for CNKI searches because CNKI often depends on the user's login, cookies, or institutional access.
2. Search by Chinese keywords, author names, journal names, CSSCI filters, and publication years.
3. Prioritize CSSCI economics and management journals, especially Economic Research Journal, Management World, Accounting Research, Management Review, Journal of Financial Research, and China Industrial Economics.
4. Export CNKI citation records when available.
5. Download PDFs only when the user has access rights.
6. Import confirmed records or RIS/BibTeX files into Zotero, then verify title, authors, journal, year, volume, issue, pages, DOI, and URL.

## Zotero Import Workflow

1. Check Zotero readiness with the Zotero helper before operating the library.
2. Search the local library before importing to avoid duplicates.
3. Use the research project name as the top-level Zotero collection name. If the project name is missing, derive a concise name from the research question and confirm it before import.
4. Under the project collection, maintain language subcollections:
   - `English`
   - `Chinese`
5. Create the project collection and missing language subcollections when they do not already exist.
6. When the literature stream is complex, create additional subcollections under `English` and `Chinese` by literature lineage, mechanism, construct, method, or institutional setting. Use concise names such as `Disclosure Quality`, `Audit Pricing`, `Digital Transformation`, `Governance Mechanisms`, or their Chinese equivalents.
7. Put each imported record into the most specific appropriate subcollection. If a paper fits multiple streams, place it in the primary stream and note secondary relevance in the literature matrix.
8. Confirm target collection structure and record list before `import-bibtex` or `import-ris`, unless the user explicitly requested import and collection creation.
9. After import, report title, creators, year, Zotero item key, BibTeX key when available, and final collection path.
10. Keep a note of records that need manual metadata cleanup.
