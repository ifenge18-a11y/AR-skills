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

## Project-Topic Archiving Model

Default to a project-topic archive when literature discovered by the Literature Reviewer is imported into Zotero. Create one root collection per research project, for example `Project - 管理层语调与审计费用`.

Under each project root, use these stable child collections:

- `00_Inbox_ToReview`: newly imported records that still need metadata cleanup, duplicate checks, PDF attachment, or verification.
- `01_Core_Literature`: papers that must be read closely and directly support the project's positioning.
- `02_Related_Stream`: related research streams that inform the project but are not central.
- `03_Theory_Mechanism`: theory, mechanism, institutional background, and explanatory-framework literature.
- `04_Method_Data`: identification strategies, variable construction, text analysis, database, or method references.
- `05_China_Context`: Chinese institutional context, A-share, audit, regulation, disclosure, or other China-setting literature.
- `90_Excluded_WeakFit`: discovered records that are not used; keep the exclusion reason in a note or handoff field.

Do not use language, journal name, or publication year as primary collections. Treat those as tags, search filters, saved searches, or metadata fields so core literature is not split across archival folders.

## Tag System

Use collections for stable project structure and tags for cross-cutting attributes. Apply only tags that are supported by the discovery and verification record.

Verification status:

- `verified`
- `partially_verified`
- `unverified`

Project role:

- `core`
- `background`
- `method`
- `theory`
- `china_context`
- `replication_candidate`
- `excluded`

Discovery or verification source:

- `source_openalex`
- `source_google_scholar`
- `source_cnki`
- `source_publisher`
- `source_ssrn`
- `source_nber`

Follow-up action:

- `need_metadata_cleanup`
- `need_duplicate_check`
- `need_pdf`
- `need_fulltext_read`
- `need_citation_check`

## Import Workflow

1. Literature Reviewer searches and screens literature only for research value, verification status, and project use.
2. When records are imported into Zotero, place all new records in `00_Inbox_ToReview` first.
3. Tag each record with verification status, project role, source, and any follow-up action.
4. Zotero handles duplicate checks, metadata cleanup, DOI/journal/year fixes, citation keys, PDFs, attachments, notes, and full-text search.
5. After cleanup, move records to the relevant project collection: core papers to `01_Core_Literature`, methods or data papers to `04_Method_Data`, theory papers to `03_Theory_Mechanism`, and Chinese institutional-context papers to `05_China_Context`.
6. Keep weak-fit records in `90_Excluded_WeakFit` only when the reason for exclusion is recorded.

## Literature Reviewer Handoff

The accounting skill may provide a handoff list:

| Record | Why it matters | Verification status | Suggested Zotero action |
|---|---|---|---|

Keep "Suggested Zotero action" descriptive, such as `import if verified`, `check duplicate`, `attach accessible PDF`, or `clean metadata`; let Zotero perform the action.

For project-topic archiving, the handoff may also include suggested collection and tag fields:

| Record | Why it matters | Verification status | Suggested collection | Suggested tags | Suggested Zotero action |
|---|---|---|---|---|---|

Each handoff row should make clear which project the record belongs to, what role it plays in the project, and whether its bibliographic facts have been verified.

## Acceptance Criteria

- Any imported paper should answer three questions from Zotero metadata, collections, and tags: which project it belongs to, what role it plays, and whether it has been verified.
- Core papers should remain together in `01_Core_Literature` rather than being split by language, journal, or year.
- A single paper may carry multiple tags, for example `core`, `theory`, `verified`, and `source_google_scholar`.
- `00_Inbox_ToReview` should represent unfinished cleanup work and should be reviewed regularly.
- Every record in `90_Excluded_WeakFit` must have an exclusion reason to avoid repeated screening.

## Compliance

Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation. Stop and ask the user to handle login, CAPTCHA, payment, or permission gates.
