# Zotero Literature Workflow

## Use For

Use this note when Literature Reviewer discoveries need to be imported into Zotero and then screened by Boss for deep-reading priority.

The accounting skill owns the research judgment: which literature matters, how papers relate to the research question, which records are candidates for import, and how Boss classifies them from title and abstract. Zotero owns the operational reference workflow:

- Importing and exporting BibTeX, RIS, ENW, or other citation files.
- Managing Zotero collections, citation keys, duplicate records, and metadata cleanup.
- Working with local PDFs, attachments, notes, and full-text library search.
- Attaching PDFs when the user has obtained them.

## Boundary Rule

Use the Zotero plugin for candidate-record import, project collections, tags, and screening notes when Zotero work is part of the task. Do not implement these operations manually inside the accounting skill.

Do not download PDFs, bypass paywalls, solve CAPTCHA, use institutional access without the user's manual action, or claim that full text was obtained. PDF retrieval is a manual follow-up represented by `need_pdf` and `need_fulltext_read`.

## Project-Topic Archiving Model

Default to a project-topic archive when literature discovered by the Literature Reviewer is imported into Zotero. Create one root collection per research project, for example `Project - 管理层语调与审计费用`.

Under each project root, use these stable child collections:

- `00_Inbox_ToReview`: newly imported candidate records that still need Boss screening, metadata cleanup, duplicate checks, PDF attachment, or verification.
- `01_Core_Literature`: papers that must be read closely and directly support the project's positioning.
- `02_Related_Stream`: related research streams that inform the project but are not central.
- `03_Theory_Mechanism`: theory, mechanism, institutional background, and explanatory-framework literature.
- `04_Method_Data`: identification strategies, variable construction, text analysis, database, or method references.
- `05_China_Context`: Chinese institutional context, A-share, audit, regulation, disclosure, or other China-setting literature.
- `90_Excluded_WeakFit`: discovered records that are not used; keep the exclusion reason in a note or screening field.

Do not use language, journal name, or publication year as primary collections. Treat those as tags, search filters, saved searches, or metadata fields so core literature is not split across archival folders.

## Candidate Import

Default import scope: import candidate literature records, not every search hit and not only final deep-read papers. A candidate record is suitable for Zotero import when it has enough metadata for later identification and has a plausible project use from title, abstract, keywords, venue, or verified search context.

Literature Reviewer should preserve these fields when available:

- Title, authors, year, source or venue.
- DOI, OpenAlex URL, Google Scholar result URL or cluster id, CNKI detail URL, publisher URL, or other stable source URL.
- Abstract and keywords.
- Discovery source and search terms.
- Verification status.
- Literature Reviewer relevance note.

Skip records that are obviously unrelated, duplicate search artifacts, or too incomplete to identify. Report skipped records with a short reason.

## Boss Abstract Screening

After candidate import, Boss screens title and abstract before assigning deep-reading work.

Use these fixed fields:

| Field | Allowed values or rule |
|---|---|
| `boss_category` | `core_literature`, `related_stream`, `theory_mechanism`, `method_data`, `china_context`, `excluded_weakfit` |
| `deep_read_priority` | `high`, `medium`, `low`, `exclude` |
| `boss_screening_reason` | One concise reason tied to direct competition, theory, method/data, China context, background use, or weak fit |
| `pdf_status` | `need_pdf`, `pdf_available`, `manual_pdf_pending`, `not_needed`, or `unknown` |

Screening rules:

- Use `core_literature` for direct competitors, same construct, same research question, or central positioning papers.
- Use `related_stream` for adjacent literature that helps locate the conversation but is not central.
- Use `theory_mechanism` for theory, mechanism, institutional background, or explanatory-framework papers.
- Use `method_data` for measurement, identification, text analysis, data, or variable-construction precedents.
- Use `china_context` for Chinese institutional context, A-share, regulation, audit, disclosure, or governance setting papers.
- Use `excluded_weakfit` for records that should not be used; record the exclusion reason.
- Mark direct competitors, core theory sources, and key variable/method sources as `high`.
- Mark useful but non-central sources as `medium`; background-only sources as `low`; weak-fit records as `exclude`.
- If the abstract is missing, do not make a strong research-value judgment. Add `abstract_missing` and `need_metadata_cleanup`, keep the record in `00_Inbox_ToReview`, and set `pdf_status` to `unknown` unless other evidence supports a stronger action.

## Tag System

Use collections for stable project structure and tags for cross-cutting attributes. Apply only tags that are supported by the discovery, verification, or Boss screening record.

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
- `abstract_missing`

Boss screening:

- `boss_core_literature`
- `boss_related_stream`
- `boss_theory_mechanism`
- `boss_method_data`
- `boss_china_context`
- `boss_excluded_weakfit`
- `deep_read_high`
- `deep_read_medium`
- `deep_read_low`
- `deep_read_exclude`

## Import Workflow

1. Literature Reviewer searches, verifies, and prepares candidate records with abstracts when available.
2. When Zotero import is part of the task, import usable candidates into the project root or `00_Inbox_ToReview`.
3. Tag each record with verification status, source, and immediate follow-up actions such as `need_duplicate_check` or `need_metadata_cleanup`.
4. Boss screens imported candidates by title and abstract using `boss_category`, `deep_read_priority`, `boss_screening_reason`, and `pdf_status`.
5. After Boss screening, move or tag records by project role: core papers to `01_Core_Literature`, methods or data papers to `04_Method_Data`, theory papers to `03_Theory_Mechanism`, Chinese institutional-context papers to `05_China_Context`, and related stream papers to `02_Related_Stream`.
6. Mark high-priority records with `need_pdf` and `need_fulltext_read` unless a PDF is already available. Do not download the PDF automatically.
7. Keep weak-fit records in `90_Excluded_WeakFit` only when the reason for exclusion is recorded.
8. Leave duplicate checks, metadata cleanup, DOI/journal/year fixes, citation keys, exports, PDFs, attachments, and full-text search to Zotero/manual follow-up.

## Literature Reviewer Output

Literature Reviewer should provide an import list:

| Record | Why it matters | Verification status | Abstract status | Suggested Zotero action |
|---|---|---|---|---|

Keep "Suggested Zotero action" descriptive, such as `import candidate`, `skip weak fit`, `check duplicate`, or `clean metadata`; let Zotero perform the operation.

After Boss screening, provide this table:

| Record | Abstract-based judgment | boss_category | deep_read_priority | Project use | boss_screening_reason | pdf_status | Zotero action |
|---|---|---|---|---|---|---|---|

Each row should make clear which project the record belongs to, what role it plays, whether its bibliographic facts are verified, why Boss classified it that way, and whether the user must obtain a PDF manually.

## Acceptance Criteria

- Any imported paper should answer three questions from Zotero metadata, collections, and tags: which project it belongs to, what role it plays, and whether it has been verified.
- Core papers should remain together in `01_Core_Literature` rather than being split by language, journal, or year.
- A single paper may carry multiple tags, for example `core`, `theory`, `verified`, and `source_google_scholar`.
- `00_Inbox_ToReview` should represent unfinished cleanup work and should be reviewed regularly.
- Every record in `90_Excluded_WeakFit` must have an exclusion reason to avoid repeated screening.
- Every `high` deep-read record should either have `pdf_available` or be marked `need_pdf` and `need_fulltext_read`.
- Records without abstracts should be marked `abstract_missing` and should not be treated as core evidence until reviewed.

## Compliance

Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation. Stop and ask the user to handle login, CAPTCHA, payment, permission gates, and PDF retrieval.
