# Zotero and Research Wiki Literature Workflow

## Use For

Use this note for durable literature work: read the Obsidian research-wiki first, discover or verify missing literature, import useful candidate records into Zotero when needed, screen them with Boss judgment, and file lasting knowledge back through `$research-wiki`.

The accounting skill owns the research judgment: which literature matters, how papers relate to the research question, which records are candidates for import, and how Boss classifies them from title and abstract. Research Wiki owns persistent Obsidian notes and synthesis pages. Zotero owns the operational reference workflow:

- Importing and exporting BibTeX, RIS, ENW, or other citation files.
- Managing Zotero collections, citation keys, duplicate records, and metadata cleanup.
- Working with local PDFs, attachments, notes, and full-text library search.
- Attaching PDFs when the user has obtained them.

## Boundary Rule

Use `$research-wiki` by default for Obsidian knowledge capture when literature findings, theory claims, design precedents, variables, or methods have lasting project value. Do not implement Obsidian source-note or synthesis-page writing manually inside the accounting skill.

Use the Zotero plugin for candidate-record import, project collections, tags, and screening notes when new records should enter the reference library. Do not implement these operations manually inside the accounting skill.

Do not download PDFs, bypass paywalls, solve CAPTCHA, use institutional access without the user's manual action, or claim that full text was obtained. PDF retrieval is a manual follow-up represented by `need_pdf` and `need_fulltext_read`.

Before the first write to an Obsidian project, state the exact research-wiki project path and get user confirmation. After confirmation, later work on that same project may update the wiki by default.

Read project `AGENTS.md` and `.research-wiki/config.json` when present. `AGENTS.md` controls policy and schema; config supplies the machine-readable `knowledge_base_path` and `research_base_path`. Use explicit CLI path arguments only as one-command overrides.

AR may perform user-authorized collection, tag, note, and import operations through an available Zotero connector or supported API. `$research-wiki` is always read-only with respect to Zotero. Never edit Zotero SQLite files. When no supported write channel is available, return an exact manual checklist naming the existing item, target collection, tags or note changes, duplicate check, and verification step; still complete any independent research-wiki work.

## Research Wiki Preflight

For durable literature tasks:

1. Identify `project` and the likely research-wiki project path.
2. Resolve `knowledge_base_path` from `.research-wiki/config.json` (default `.`). If the wiki exists, read its `index.md`, `log.md`, and relevant pages from `sources/`, `themes/`, `concepts/`, `methods/`, and `claims/`.
3. Use the wiki to avoid rediscovering already-screened literature, stale claims, known PDF blockers, and settled project decisions.
4. If no wiki exists, recommend initializing one with `$research-wiki` and binding it to the relevant Zotero collection before heavy literature work.
5. Skip wiki persistence only for temporary chat, one-off conceptual explanation, narrow copyediting, or disposable brainstorming.

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
- `source_route`: where the record was discovered or checked.
- `verification_status`: `verified`, `partially_verified`, or `unverified`, including for CNKI records.
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
| `project_use` | How this record should support the project: positioning, mechanism, measurement, identification, context, contrast, background, or exclusion |
| `need_fulltext_read` | Defaults to `true` for `high` and `medium`, and `false` for `low` and `exclude`; allow an explicit evidence-based override except for `exclude` |
| `read_level` | `abstract`, `intro_design_conclusion`, or `fulltext`; defaults to `abstract` for screening-only work |
| `deep_read_completed` | Completion date in `YYYY-MM-DD` only after a full deep read is done; otherwise blank |

Screening rules:

- Use `core_literature` for direct competitors, same construct, same research question, or central positioning papers.
- Use `related_stream` for adjacent literature that helps locate the conversation but is not central.
- Use `theory_mechanism` for theory, mechanism, institutional background, or explanatory-framework papers.
- Use `method_data` for measurement, identification, text analysis, data, or variable-construction precedents.
- Use `china_context` for Chinese institutional context, A-share, regulation, audit, disclosure, or governance setting papers.
- Use `excluded_weakfit` for records that should not be used; record the exclusion reason.
- Mark direct competitors, core theory sources, and key variable/method sources as `high`.
- Mark useful but non-central sources as `medium`; they still require the core chapters unless explicitly waived. Mark background-only sources as `low`; weak-fit records as `exclude`.
- If the abstract is missing, do not make a strong research-value judgment. Add `abstract_missing` and `need_metadata_cleanup`, keep the record in `00_Inbox_ToReview`, and set `pdf_status` to `unknown` unless other evidence supports a stronger action.

## Tag System

Use collections for stable project structure and tags for cross-cutting attributes. Apply only tags that are supported by the discovery, verification, or Boss screening record.

`verification_status`:

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

`source_route` tags:

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

Read progress tags are optional and secondary to research-wiki source-note frontmatter:

- `deep_read_todo`
- `deep_read_in_progress`
- `deep_read_done`
- `deep_read_skip`

When Zotero tags conflict with source-note frontmatter, use the source note as the authority and log a Zotero sync follow-up if needed.

## Research-Wiki Read State

For projects using `<knowledge_base_path>/sources/*.md`, source-note frontmatter is the authoritative read-progress record. Use these fields unless project `AGENTS.md` defines a different schema:

```yaml
status: screened | deep_read_in_progress | deep_read_done | deep_read_skip
deep_read_priority: high | medium | low | exclude
need_fulltext_read: true | false
deep_read_completed:
read_level: abstract | intro_design_conclusion | fulltext
source_route: openalex | google_scholar | cnki | publisher | ssrn | nber | user | manual | unknown
verification_status: verified | partially_verified | unverified
```

Read-state rules:

- Keep `status: screened` and `read_level: abstract` for title/abstract screening only.
- Use `status: deep_read_in_progress` only while actively reading a full text.
- After a full deep read, set `status: deep_read_done`, `need_fulltext_read: false`, `read_level: fulltext`, and `deep_read_completed: YYYY-MM-DD`.
- If a record will not be read further, set `status: deep_read_skip`, `need_fulltext_read: false`, and record the skip reason in the note or log.
- Treat `deep_read_priority` as priority only, not completion state.
- Treat `source_route`, `verification_status`, and `read_level` as independent provenance, verification, and evidence-depth dimensions.

Before starting batch screening or deep reading, scan existing source notes for `zotero_item_key`, DOI, title, `status`, `need_fulltext_read`, `read_level`, and `deep_read_completed`. Do not repeat deep reads for records marked `status: deep_read_done` unless the user explicitly asks to reread or update the note.

## Import Workflow

1. Run the research-wiki preflight when the task has durable value.
2. Literature Reviewer searches, verifies, and prepares candidate records with abstracts when available, using the wiki to avoid duplicate screening.
3. Import usable new candidates into the project root or `00_Inbox_ToReview` when they should enter Zotero.
4. Record `verification_status`, `source_route`, and immediate follow-up actions such as `need_duplicate_check` or `need_metadata_cleanup`.
5. Boss screens imported and wiki-known candidates by title and abstract using `boss_category`, `deep_read_priority`, `boss_screening_reason`, `pdf_status`, `project_use`, and `need_fulltext_read`.
6. After Boss screening, move or tag records by project role: core papers to `01_Core_Literature`, methods or data papers to `04_Method_Data`, theory papers to `03_Theory_Mechanism`, Chinese institutional-context papers to `05_China_Context`, and related stream papers to `02_Related_Stream`.
7. Keep `need_fulltext_read: true` for `high` and `medium` by default. If the required full text is unavailable, use `need_pdf` or `manual_pdf_pending`; do not download the PDF automatically.
8. Pass the screened records to `$research-wiki` with the canonical handoff: `project`, `zotero_item_key`, `boss_category`, `deep_read_priority`, `boss_screening_reason`, `pdf_status`, `project_use`, `need_fulltext_read`, `read_level`, `deep_read_completed`, `source_route`, and `verification_status`.
9. Use `$research-wiki` to create or update `sources/` source notes and relevant `concepts/`, `themes/`, `methods/`, `claims/`, `index.md`, and `log.md`.
10. Keep weak-fit records in `90_Excluded_WeakFit` and/or research-wiki source notes only when the reason for exclusion is recorded.
11. Leave duplicate checks, metadata cleanup, DOI/journal/year fixes, citation keys, exports, PDFs, attachments, and full-text search to Zotero/manual follow-up.

## Existing Zotero Item Updates

When the task is to process records already in a project inbox, prefer moving and updating the original parent item rather than creating duplicate records, if the project allows it. Preserve child PDFs, EPUBs, notes, and annotations.

Default safety boundary:

- Use only an available connector or supported API for authorized Zotero writes.
- Never edit Zotero SQLite files or invent an unsupported write route.
- Never delete attachments or move a record to trash unless the user explicitly asks.
- If no write channel is available, output exact manual actions for each existing item: target collection, tags to add/remove, screening note content, duplicate check, and the final verification view. Still update the research wiki when that write is independently authorized.

## Literature Reviewer Output

Literature Reviewer should provide an import list:

| Record | Why it matters | Verification status | Abstract status | Suggested Zotero action |
|---|---|---|---|---|

Keep "Suggested Zotero action" descriptive, such as `import candidate`, `skip weak fit`, `check duplicate`, or `clean metadata`; let Zotero perform the operation.

After Boss screening, provide this table:

| Record | source_route | verification_status | Abstract-based judgment | boss_category | deep_read_priority | Project use | boss_screening_reason | pdf_status | need_fulltext_read | Zotero action | Research-wiki action |
|---|---|---|---|---|---|---|---|---|---|---|---|

Each row should make clear which project the record belongs to, its `source_route`, its `verification_status`, what role it plays, why Boss classified it that way, and whether the user must obtain a PDF manually.

## Acceptance Criteria

- Any imported paper should answer three questions from Zotero metadata, collections, and tags: which project it belongs to, what role it plays, and whether it has been verified.
- Core papers should remain together in `01_Core_Literature` rather than being split by language, journal, or year.
- A single paper may carry multiple tags, for example `core`, `theory`, `verified`, and `source_google_scholar`.
- `00_Inbox_ToReview` should represent unfinished cleanup work and should be reviewed regularly.
- Every record in `90_Excluded_WeakFit` must have an exclusion reason to avoid repeated screening.
- Every `high` deep-read record should either have `pdf_available` or be marked `need_pdf` and `need_fulltext_read`.
- Every `medium` record defaults to `need_fulltext_read: true` for abstract, introduction, research design, and conclusion unless the screening record explicitly documents why those chapters are unnecessary.
- Every source note should record read progress with `status`, `need_fulltext_read`, `read_level`, and `deep_read_completed`.
- Full-text deep reads should not be repeated when the source note says `status: deep_read_done`, unless the user asks for a reread or update.
- Records without abstracts should be marked `abstract_missing` and should not be treated as core evidence until reviewed.
- Durable project findings should appear in the research-wiki, not only in chat.
- Research-wiki source notes should preserve Zotero traceability through `zotero_item_key` when available.
- `index.md` and `log.md` should reflect meaningful literature ingest, synthesis updates, and missing full-text blockers.

## Compliance

Do not bypass paywalls, CAPTCHA, institutional access controls, rate limits, or website anti-automation. Stop and ask the user to handle login, CAPTCHA, payment, permission gates, and PDF retrieval.
