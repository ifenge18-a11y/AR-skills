# Research Base Workflow / Research Base 工作流

Use this reference only when the user explicitly requests Research Base work or the project `AGENTS.md` explicitly enables it. Research Base preserves useful exploratory research work without presenting it as established literature, method, or empirical knowledge.

## Activation and Authority

1. Read project `AGENTS.md` before any Research Base action. Its path, directory layout, language, frontmatter, status values, and promotion conditions override this reference.
2. Do not create a Research Base because a normal discussion seems useful. Temporary chat, disposable brainstorming, narrow editing, and one-off explanations remain outside it.
3. Before the first write, state the exact path and obtain user confirmation. The default helper path is `<project>/Research Base`; use a project-defined path when present.
4. When it exists, read `README.md`, `index.md`, `log.md`, and relevant active notes before writing. Treat index/log updates as part of each durable change.

## Evidence Boundary

| Layer | Authoritative content | Do not place here |
|---|---|---|
| Zotero | Records, PDFs, attachments, annotations, collections, tags, citation management | The sole record of exploratory research decisions |
| Knowledge Base | Traceable source notes, verified concepts, mature method rules, reusable claims | Unverified working ideas or unsettled design details |
| Research Base | Candidate questions, method prototypes, data checks, design options, discussion summaries, rejected or superseded paths | Duplicate source notes, Zotero read state, or unverified material phrased as a settled conclusion |

Research Base links to Knowledge Base pages; it does not reproduce a paper's source note, Zotero item key, PDF state, or deep-read status.

## Default Structure and Metadata

Unless `AGENTS.md` overrides it, use:

```text
Research Base/
  README.md
  index.md
  log.md
  00_Conversation_Notes/
  01_Topic_Exploration/
  02_Method_Prototypes/
  03_Data_Feasibility/
  04_Design_Alternatives/
  90_Archived_or_Rejected/
  _templates/
```

Use one of these `type` values: `conversation_note`, `topic_exploration`, `method_prototype`, `data_feasibility`, or `design_alternative`.

```yaml
type:
status: exploratory | under_review | promoted | rejected | superseded
evidence_status: unverified | partially_verified | verified
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
kb_promotion: false
related_kb_pages: []
supersedes:
```

Titles may be English; use Chinese prose by default unless the project rules say otherwise. Preserve English for constructs, variables, code, standards, and necessary quotations.

## Filing, Archive, and Promotion Protocol

1. **Classify.** File only persistent exploratory output with clear future reuse value. Keep verified literature and durable conclusions in Knowledge Base.
2. **Label evidence.** Mark unverified literature facts, data fields, sample coverage, mappings, identification assumptions, and expected results as `unverified` or `partially_verified`.
3. **Link, do not duplicate.** Link related Knowledge Base pages; preserve Zotero/source-note authority there.
4. **Maintain navigation.** Add, rename, archive, or status-change notes in `index.md`; append the date, changed note, and decision to `log.md`.
5. **Archive transparently.** Move rejected or deferred work to `90_Archived_or_Rejected/` when the project uses archival folders, or retain an explicit `rejected`/`superseded` status where the project schema specifies in-place status. Never delete the research trail.
6. **Promote only with authorization.** The user must explicitly request promotion unless `AGENTS.md` authorizes it. Verify the underlying evidence, write a concise stable conclusion to the appropriate Knowledge Base page, add reciprocal links and dates, set the original note to `promoted`, `kb_promotion: true`, and `evidence_status: verified`, then update both indexes and logs.
7. **Report the boundary.** Tell the user whether content was stored in Research Base or Knowledge Base, its evidence status, and whether promotion occurred.

## Maintainer Acceptance Matrix

| Scenario | Expected behavior |
|---|---|
| No opt-in | A method-concept question receives an answer only; no Research Base directory or note is created. |
| Create after confirmation | An explicit save request creates the configured structure only after exact-path confirmation; Knowledge Base remains unchanged. |
| File a prototype | An unsettled text-measurement idea becomes an `exploratory` method prototype with unresolved mapping, sample, dictionary, and validation issues. |
| Keep source authority | A request to organize one paper follows Zotero/Knowledge Base source-note flow and does not create a Research Base paper note. |
| Promote explicitly | Verified content is summarized in Knowledge Base only after explicit authorization; the original note retains links, date, and its exploration history. |
| Archive transparently | A rejected design is retained with a reason and any alternative link, and navigation/log records are updated. |
| Obey local language rule | English-title/Chinese-body project rules are honored while variable names and standards remain in English. |
