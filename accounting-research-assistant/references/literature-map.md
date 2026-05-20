# Literature Mapping

## Use For

Use this reference for literature reviews, related-work sections, gap identification, literature-use strategy, and paper positioning.

This file supports intellectual literature work: mapping conversations, constructs, theory, evidence, limitations, and contribution boundaries. It does not manage references. Use Zotero for BibTeX/RIS, PDF handling, imports, exports, citation keys, and local library collections.

## Intake Check

Before mapping literature, identify:

- Research construct and likely synonyms.
- Research setting: accounting, finance, financial management, audit, disclosure, governance, tax, ESG, capital markets, China A-share, or adjacent management/economics.
- Unit of analysis or evidence base when known.
- User's purpose: topic screening, positioning, related-work section, theory support, design precedent, or citation verification.
- Language scope: English, Chinese, or both.

If the request is mainly reference-library work, route it to Zotero and keep this file focused on research meaning.

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

Use this order for literature discovery:

1. OpenAlex preliminary search: use OpenAlex to identify candidate English works, authors, venues, years, DOI metadata, citation links, and related concepts. Treat OpenAlex as a discovery and metadata source, not final proof of publication facts.
2. Google Scholar latest-English check: use Chrome to search Google Scholar for newly published or online-first English papers, working papers, and citation trails that may not be fully reflected in OpenAlex. If Google Scholar asks for login, CAPTCHA, or unusual traffic confirmation, stop and ask the user to complete it manually.
3. CNKI Chinese search: use Chrome to search CNKI for Chinese CSSCI literature. If CNKI asks for account login, institutional access, CAPTCHA, or download permission, stop and ask the user to complete it manually.
4. Source verification: verify important records through publisher pages, SSRN, NBER, institutional repositories, journal pages, or CNKI detail pages before treating them as confirmed citations.

For OpenAlex, search by title keywords, construct synonyms, author names, venue names, publication years, and DOI when available. Record the OpenAlex work URL or DOI when available.

Priority English accounting journals:

- The Accounting Review (AR/TAR)
- Journal of Accounting Research (JAR)
- Review of Accounting Studies (RAST)
- Contemporary Accounting Research (CAR)
- Journal of Accounting and Economics (JAE)

Priority Chinese sources: CNKI CSSCI journals, especially economics and management journals such as Economic Research Journal, Management World, Accounting Research, Management Review, Journal of Financial Research, and China Industrial Economics.

Do not invent citations, findings, authors, publication years, journal placements, issue details, sample sizes, or DOIs. If a record cannot be verified from a reliable source, label it as unverified or partially verified instead of citing it as fact.

## Verification Labels

Use exactly one label for each record:

- `verified`: key facts are checked against a publisher page, journal page, DOI record, SSRN/NBER/institutional repository, CNKI detail page, or another reliable source.
- `partially verified`: title/authors/year or venue are supported, but important details such as findings, sample, identification, DOI, or final publication status are not fully checked.
- `unverified`: discovered through search or memory but not confirmed from a reliable source.

Never use unverified records as decisive support for a contribution, theory claim, or design precedent. They can be listed as candidates for follow-up.

## Literature Matrix

Use this table structure:

| Paper | Source route | Verification | Setting | Question | Theory | Data | Identification | Main finding | Limitation | Use in project |
|---|---|---|---|---|---|---|---|---|---|---|

Keep the "Use in project" column explicit: background, contrast, mechanism support, measurement precedent, design precedent, or contribution boundary.

Use "Source route" to show where the record came from, such as OpenAlex, Google Scholar, CNKI, publisher page, SSRN, NBER, or institutional repository. Use "Verification" to mark verified, partially verified, or unverified.

For "Use in project", choose precise roles such as background, contrast, mechanism support, measurement precedent, identification precedent, institutional setting, contribution boundary, or unresolved competing evidence.

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
- Zotero handoff note only when the user needs reference-management operations.

## QA Checklist

- No invented papers, findings, sample sizes, journal placements, issue data, or DOIs.
- Chinese and English literature are not treated as interchangeable when institutional settings differ.
- A paper's finding is not generalized beyond its setting, data, and identification.
- Literature gaps are framed as theory, setting, measurement, boundary, or design gaps, not just absence claims.
- Citation formatting and library management are left to Zotero.
