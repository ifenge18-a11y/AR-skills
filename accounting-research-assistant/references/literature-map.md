# Literature Mapping

## Use For

Use this reference for literature reviews, related-work sections, gap identification, literature-use strategy, and paper positioning.

This file supports intellectual literature work: mapping conversations, constructs, theory, evidence, limitations, and contribution boundaries. Use Zotero for operational reference work. When Zotero archiving is part of the task, this skill may prepare candidate records and use the Zotero plugin for import, project collections, tags, and Boss screening notes; PDF handling, exports, citation keys, duplicate cleanup, and broad local library maintenance remain Zotero/manual follow-up.

For durable project work, use the project Obsidian research-wiki as the first and last stop: read existing wiki knowledge before search, then write useful literature findings and synthesis back through `$research-wiki`.

## Intake Check

Before mapping literature, identify:

- Research construct and likely synonyms.
- Research setting: accounting, finance, financial management, audit, disclosure, governance, tax, ESG, capital markets, China A-share, or adjacent management/economics.
- Unit of analysis or evidence base when known.
- User's purpose: topic screening, positioning, related-work section, theory support, design precedent, or citation verification.
- Language scope: English, Chinese, or both.
- Project wiki status: existing research-wiki path, candidate project path, or no wiki yet.

If the request is mainly reference-library work, route it to Zotero. If it is durable research knowledge work, route persistence through `$research-wiki` and keep this file focused on research meaning, candidate selection, and Boss screening rationale.

## Search Strategy

Start from the user's construct and setting, then expand through synonyms:

- Financial reporting: disclosure quality, accruals, conservatism, comparability, readability, restatements, internal control, earnings management.
- Audit: audit quality, auditor independence, audit fees, key audit matters, audit effort, going concern, partner effects, PCAOB inspections.
- Capital markets: information asymmetry, analyst forecasts, crash risk, liquidity, cost of capital, market reaction, price discovery.
- Governance and incentives: boards, ownership, executive compensation, institutional investors, debt covenants, political connections.
- Tax: tax avoidance, book-tax differences, tax enforcement, tax risk, tax disclosure.
- ESG and disclosure: sustainability reporting, assurance, greenwashing, climate risk, social responsibility, mandatory disclosure.
- China setting: A-share firms, CSRC regulation, exchanges, state ownership, local government, tunneling, connected transactions, enforcement actions.

Prefer seed papers from top accounting journals and adjacent finance/economics journals, then snowball forward and backward.

## Search Route

Use this order for literature discovery and persistence:

1. Research-wiki preflight: if a project wiki exists, read `index.md`, `log.md`, and relevant `sources/`, `themes/`, `concepts/`, `methods/`, and `claims/` pages before external search. If no wiki exists and the task has durable value, recommend creating one and binding it to a Zotero collection.
2. OpenAlex preliminary search: use OpenAlex to identify candidate English works, authors, venues, years, DOI metadata, citation links, and related concepts. Treat OpenAlex as a discovery and metadata source, not final proof of publication facts.
3. Google Scholar English verification: use Chrome to search Google Scholar to verify English records that came from OpenAlex or are otherwise used as core evidence. Record visible metadata and citation signals. If Google Scholar asks for login, CAPTCHA, or unusual traffic confirmation, stop and ask the user to complete it manually.
4. CNKI Chinese search: use Chrome to search CNKI for Chinese CSSCI literature. Record `source_route: cnki`; no second discovery source is required, but still assign the same three-value `verification_status` based on what the visible CNKI record supports. If CNKI asks for account login, institutional access, CAPTCHA, or download permission, stop and ask the user to complete it manually.
5. Working-paper search: skip by default. Search SSRN, NBER, unpublished papers, or latest working-paper evidence only when the user explicitly asks for working papers or deeper working-paper coverage.
6. Research-wiki filing: after Boss screening or synthesis, pass project-use decisions to `$research-wiki` so useful sources and cross-paper claims are stored in Obsidian rather than left only in chat.

For OpenAlex, search by title keywords, construct synonyms, author names, venue names, publication years, and DOI when available. Record the OpenAlex work URL or DOI when available.

Priority English accounting journals:

- The Accounting Review (AR/TAR)
- Journal of Accounting Research (JAR)
- Review of Accounting Studies (RAST)
- Contemporary Accounting Research (CAR)
- Journal of Accounting and Economics (JAE)

Priority Chinese sources: CNKI CSSCI journals, especially economics and management journals such as Economic Research Journal, Management World, Accounting Research, Management Review, Journal of Financial Research, and China Industrial Economics.

Do not invent citations, findings, authors, publication years, journal placements, issue details, sample sizes, or DOIs. If a record's key facts or substantive claims cannot be checked, set `verification_status` to `unverified` or `partially_verified` instead of citing it as fact. `source_route: cnki` identifies provenance; it is not a verification label.

## Chrome Search Procedures

Use Chrome searches as auditable discovery and verification steps, not as PDF-acquisition or citation-export operations. Do not download paywalled papers, bypass access controls, solve CAPTCHA programmatically, or manage BibTeX/RIS/PDF files inside this skill.

For Google Scholar:

- Build searches from the research construct, synonyms, author names, journal names, exact phrases, and year ranges. Use focused searches before broad searches when the topic is mature.
- Extract and record the title, authors, source or venue-year line, citation count, open full-text link when visible, result URL, and Google Scholar `data-cid` or equivalent cluster identifier when available.
- Use Google Scholar mainly to verify English records found through OpenAlex, confirm visible publication/citation metadata, and check recency or citation-count signals beyond OpenAlex.
- Do not follow records to publisher pages, SSRN, NBER, institutional repositories, DOI pages, or journal pages unless the user explicitly asks for deeper verification or working-paper coverage.
- If Google Scholar shows CAPTCHA, unusual-traffic warnings, login requirements, or access prompts, stop and ask the user to complete the browser step manually before continuing.

For CNKI:

- Use ordinary keyword search for broad discovery and advanced search when author, title, journal, year range, source category, CSSCI, 北大核心, or other filters matter.
- Prioritize CSSCI, 北大核心, and accounting, finance, management, and economics journals; give special attention to the priority Chinese journals listed above.
- Extract and record the title, authors, source or journal, publication date, citation count, download count, result URL, and detail-page URL when available.
- Treat CNKI search results as `source_route: cnki`. Do not require a second discovery route beyond recording the visible CNKI fields.
- If CNKI asks for account login, institutional access, CAPTCHA, or download permission, stop and ask the user to handle the browser step manually. Do not attempt to bypass permissions or automate downloads.

## Provenance and Verification

Keep these dimensions separate for every record:

- `source_route`: `openalex`, `google_scholar`, `cnki`, `publisher`, `ssrn`, `nber`, `user`, `manual`, or `unknown`.
- `verification_status: verified`: the facts used are supported by the recorded route.
- `verification_status: partially_verified`: bibliographic facts are supported, but important findings, sample, identification, DOI, or publication status remain unchecked.
- `verification_status: unverified`: the record or claim has not been confirmed from an inspectable source.

CNKI needs no second source by default: a visible CNKI record may support `verified` bibliographic facts, while substantive claims remain `partially_verified` until the necessary evidence is read. Never use an unverified record as decisive support for a contribution, theory claim, or design precedent.

## Staged Evidence Packets

Use staged evidence packets instead of treating every paper at the same level of detail. The default unit is a per-paper record that can be read by the Boss, Theory Analyst, and Empirical Designer.

### Screening Packet

Use screening granularity while the topic is still being discussed. The purpose is broad, low-cost triage: decide whether a record matters, how credible it is, which constructs it touches, and whether it deserves deep reading.

Use this table structure:

| Paper | source_route | verification_status | Research problem | Setting | Constructs | Main finding | Relevance to topic | Use in project | deep_read_role | deep_read_priority |
|---|---|---|---|---|---|---|---|---|---|---|

Field rules:

- `Paper`: title, authors, year, and source or venue when known.
- `source_route`: use the fixed provenance values above.
- `verification_status`: use only `verified`, `partially_verified`, or `unverified` for every route.
- `Research problem`: the paper's actual research question, not a generic topic label.
- `Setting`: institutional setting, sample context, country or market, industry, and unit of analysis when known.
- `Constructs`: core constructs, concepts, variables, or mechanisms touched by the paper.
- `Main finding`: the main result, tied to setting and evidence; do not generalize beyond what is verified.
- `Relevance to topic`: why this paper matters or does not matter for the user's current topic.
- `Use in project`: choose precise roles such as background, contrast, mechanism support, measurement precedent, identification precedent, institutional setting, contribution boundary, unresolved competing evidence, or weak fit.
- `deep_read_role`: `theory_core`, `empirical_core`, `theory_and_empirical_core`, `background_only`, or `no_deep_read`.
- `deep_read_priority`: only `high`, `medium`, `low`, or `exclude`. This is scheduling priority, not literature role or completion state.

### Deep-Read Packet

After the topic is settled, upgrade records whose `deep_read_role` is `theory_core`, `empirical_core`, or `theory_and_empirical_core` to deep-read granularity. Do not deep-read every background paper.

Use this extended structure for upgraded records:

| Paper | Mechanism chain | Competing explanations | Boundary conditions | Data and sample | Variables | Identification strategy | Empirical tests | Limitations | Implications for our project |
|---|---|---|---|---|---|---|---|---|---|

Deep-read fields must stay project-facing:

- `Mechanism chain`: how constructs connect into a causal or interpretive logic.
- `Competing explanations`: alternative mechanisms that could produce similar findings.
- `Boundary conditions`: where the theory or evidence should be stronger, weaker, or not travel.
- `Data and sample`: data sources, sample period, unit of analysis, and important filters when verified.
- `Variables`: key dependent variables, independent variables, moderators, mediators, or measurement choices.
- `Identification strategy`: research design, fixed effects, instruments, DiD/event design, matching, discontinuity, or other identification logic when present.
- `Empirical tests`: main tests, mechanism tests, heterogeneity tests, robustness tests, or falsification tests that may inform the user's design.
- `Limitations`: theoretical, measurement, setting, sample, identification, or external-validity limits.
- `Implications for our project`: what to borrow, avoid, challenge, extend, or verify before using.

### Role Consumption

- Boss reads the screening packet first: `verification_status`, `setting`, `constructs`, `main finding`, `relevance to topic`, `use in project`, `deep_read_role`, and `deep_read_priority` to judge topic value, core constructs, contribution boundary, and reading priorities.
- Theory Analyst reads screening `constructs` first, then deep-read `mechanism chain`, `competing explanations`, `boundary conditions`, and `limitations` to build mechanisms, hypotheses, and observable predictions.
- Empirical Designer reads screening `constructs` and `setting` first, then deep-read `data and sample`, `variables`, `identification strategy`, `empirical tests`, and `limitations` to design sample, variables, model, validity checks, mechanism tests, and robustness tests.

## Gap Assessment

A convincing gap should be more than "few papers study X." Test the gap against these standards:

- **Theoretical tension**: existing theories imply competing predictions.
- **Institutional change**: a rule, enforcement change, technology, or market structure creates new variation.
- **Measurement advance**: new data observe a construct previously measured noisily.
- **Boundary condition**: prior results may not travel across ownership, enforcement, information environment, or contracting settings.
- **Design improvement**: new identification addresses a known endogeneity concern.

## Positioning Language

Strong positioning usually follows this pattern:

1. "Prior work shows..."
2. "However, this evidence leaves open..."
3. "This matters in accounting because..."
4. "Our setting/design/data allow..."
5. "The study contributes by..."

Avoid overclaiming novelty if the contribution is mainly setting extension, improved measurement, or a sharper mechanism test.

## Output Contract

For literature-mapping tasks, return:

- Search route and scope used.
- Literature matrix with verification labels.
- Theoretical conversations and unresolved tensions.
- Contribution boundary: what the user's project can and cannot claim relative to prior work.
- Missing verification list for papers, findings, data facts, or publication status.
- Research-wiki update summary for durable project work, including pages created or changed when writes are performed.
- Zotero candidate-import and Boss-screening note when new records should enter the project Zotero collection.

## QA Checklist

- No invented papers, findings, sample sizes, journal placements, issue data, or DOIs.
- Chinese and English literature are not treated as interchangeable when institutional settings differ.
- A paper's finding is not generalized beyond its setting, data, and identification.
- Literature gaps are framed as theory, setting, measurement, boundary, or design gaps, not just absence claims.
- Durable findings have been checked against the project research-wiki and filed back through `$research-wiki` when they add lasting project value.
- Citation formatting, exports, PDF retrieval, attachment handling, and broad library maintenance are left to Zotero/manual follow-up.
