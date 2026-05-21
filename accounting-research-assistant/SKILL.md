---
name: accounting-research-assistant
version: 0.1.1
description: Assist accounting, finance, and financial management research workflows across topic refinement, literature understanding, theory development, empirical research design, data and variable planning, reproducible Stata/Python analysis planning, and manuscript section writing. Use when Codex is asked to help with academic accounting research, archival accounting studies, audit research, financial reporting research, management accounting research, ESG/accounting disclosure studies, capital market accounting research, Chinese A-share accounting research, manuscript drafting or revision, or research project planning in accounting and related finance fields.
---

# Accounting Research Assistant

## Scope Boundary

This is a single skill for accounting, finance, and financial management research. Keep all work inside the existing research-assistant scope:

- In scope: research question shaping, literature understanding and positioning, theory and hypotheses, empirical design, data and variable planning, Stata/Python analysis plans, reproducibility planning, and manuscript section drafting or revision.
- Out of scope: figure production, publication or submission strategy, reviewer response letters, rebuttals, seminar or PPT decks, Nature/CNS-style generic scientific writing, biomedical workflows, citation-file generation, BibTeX/RIS conversion, PDF library management, and Zotero library operations.
- Zotero owns reference-management work. When users ask for citation files, imports, exports, PDFs, collections, or local bibliography management, route those tasks to Zotero instead of expanding this skill.

When a user request mixes in-scope and out-of-scope work, handle the in-scope research work and explicitly route the out-of-scope portion to the appropriate tool or a separate workflow.

## Single-Skill Routing

Start every request by classifying the task into one or more internal routes. If the request spans routes, work in this order: topic, literature, theory, design, data, code, writing.

| Route | Use when the user needs | Reference |
|---|---|---|
| Topic shaping | Research question, contribution, setting, feasibility | This file |
| Literature understanding | Literature map, gap, positioning, construct lineage | `references/literature-map.md` |
| Theory and hypotheses | Mechanisms, competing explanations, boundary conditions | This file |
| Research design | Sample, model, identification, robustness, validity threats | `references/research-design.md` |
| Data and variables | Databases, joins, variable definitions, sample filters | `references/data-and-variables.md` |
| Code planning | Stata/Python workflow, script order, reproducibility checks | `references/data-and-variables.md` |
| Manuscript writing | Abstract, introduction, theory, research design, result narrative | `references/writing-workflow.md` |

## Boss-Led Agent Orchestration

Use the Boss-led multi-agent workflow only when the user explicitly asks for multi-agent, team, Boss-led, or independent-agent collaboration, or when the user uses the default prompt that explicitly requests Boss-led multi-agent mode. Otherwise, first mention that the skill can switch into Boss-led multi-agent mode, then continue with the ordinary workflow unless the user authorizes agent creation.

When Boss-led mode is active, the Boss is responsible for the research plan, role assignment, synthesis, and critical review. Read `references/agent-roles.md` before creating role agents or describing the team protocol.

Default runtime protocol:

1. Boss drafts the research plan, identifies missing constraints, and decides which role agents are needed.
2. Boss creates independent sub-agents for the needed roles. Use staged parallelism: start `literature_reviewer` first; after preliminary literature signals are available, run `theory_analyst` and `empirical_designer` in parallel when useful; start `research_coder` after the empirical design is stable; start `writer` after Boss has reviewed the role outputs.
3. Each role agent must return conclusions, evidence, unverified items, and input needs for other roles.
4. Boss must challenge role outputs, identify weak logic, unsupported claims, identification risks, literature gaps, and writing problems. Do not merely summarize.
5. Boss produces the final integrated answer with explicit assumptions and unresolved verification items.

## Core Workflow

After routing the request, use the relevant checklist. If the user's request is outside the scope boundary, say so briefly and redirect to the appropriate tool or workflow rather than absorbing the task into this skill.

1. **Idea shaping**: turn a broad interest into a falsifiable accounting research question.
2. **Literature mapping**: locate conversations, constructs, mechanisms, and unresolved tensions.
3. **Theory and hypotheses**: connect institutional setting, incentives, information environment, agency conflicts, and measurement choices.
4. **Research design**: propose sample, variables, model, identification strategy, robustness, and threats.
5. **Data planning**: specify databases, joins, filters, variable definitions, and reproducible cleaning steps.
6. **Code planning**: convert a stable empirical design into reproducible Stata/Python script order, outputs, checks, and logs.
7. **Writing and revision**: improve abstracts, introductions, theory sections, hypotheses, research-design prose, result narratives, contribution framing, and replication documentation.

Prefer outputs that are immediately usable by a researcher: tables, model equations, variable dictionaries, literature matrices, analysis plans, code workflow plans, or manuscript-ready prose.

## Research Discipline

Before giving recommendations, identify:

- Research setting: market, audit, tax, governance, disclosure, ESG, management accounting, China-focused, cross-country, experimental, survey, or mixed-method.
- Unit of analysis: firm-year, firm-quarter, audit engagement, analyst forecast, restatement event, director-year, city-year, subsidiary-year, executive-year, transaction, or text document.
- Inference goal: descriptive mapping, association, causal estimate, mechanism test, prediction, measurement validation, or theory synthesis.
- Feasible data: named databases, public filings, proprietary data, hand-collected data, text data, interviews, surveys, or experiments.
- Target output: idea memo, literature review, empirical design, data plan, code plan, paper section, or manuscript revision.

If core facts are missing, make conservative assumptions and label them. Ask only when the missing information would materially change the design.

## Task Playbooks

### Idea Shaping

Produce a compact research memo with:

- A one-sentence research question.
- The accounting construct and why it is hard to observe.
- The economic mechanism and competing explanations.
- The likely contribution: theory, setting, measurement, identification, or practical relevance.
- A feasible empirical strategy and the main threat to validity.
- Three stronger alternative framings if the first framing feels incremental.

### Literature Mapping

Create a literature matrix with columns for paper, setting, research question, theory, data, identification, main finding, limitation, and implication for the user's project.

Read `references/literature-map.md` when the user asks for a literature review, paper positioning, related-work section, literature-use strategy, gap analysis, or OpenAlex-based preliminary search.

Use Zotero, not this skill, when the user asks to download literature, import records, export BibTeX/RIS, work with PDFs, manage collections, or maintain citation metadata. This skill may define what literature is needed and how it supports the research question, but Zotero owns the reference-management operations.

Use current sources when the user asks for the latest papers, specific article details, journal status, rankings, or publication facts. Prefer journal pages, SSRN, NBER, institutional repositories, and publisher pages over secondary summaries.

### Theory and Hypotheses

Draft hypotheses by separating:

- Mechanism: why the effect should exist.
- Boundary condition: when the effect should be stronger or weaker.
- Alternative explanation: what else could produce the same pattern.
- Observable implication: what coefficient, heterogeneity, or cross-sectional pattern should appear.

Avoid hypotheses that merely restate the regression sign. Tie the prediction to accounting institutions, reporting incentives, assurance, governance, contracts, tax rules, disclosure channels, or capital market information processing.

### Research Design

Read `references/research-design.md` when the user needs empirical models, identification choices, variable construction, robustness checks, or validity threats.

For every empirical design, provide:

- Sample definition and exclusion rules.
- Dependent variable, treatment or key independent variable, controls, fixed effects, clustering, and model equation.
- Identification assumptions and why they might fail.
- Robustness and falsification tests.
- Interpretation limits and what the design cannot claim.

When proposing causal language, explicitly state whether the design supports causal interpretation or only association.

### Data and Variables

Read `references/data-and-variables.md` when the user asks about databases, variable definitions, sample construction, joins, data cleaning, or replication packages.

For data plans, specify:

- Data source and table or filing type when known.
- Entity keys, time keys, and merge grain.
- Variable formulas with numerator, denominator, winsorization, scaling, and lagging choices.
- Sample filters and the reason for each filter.
- Reproducibility notes: raw-data manifest, code order, logs, and output checks.

### Code Planning

For code plans:

- Prefer Stata for archival empirical accounting regressions, fixed effects, clustered standard errors, tables, logs, and sample-count diagnostics.
- Use Python only when it is better suited for text analysis, parsing, file processing, machine learning, or automation around data preparation.
- Specify script order, file responsibilities, required inputs, expected outputs, and validation checks.
- Do not write final code around unverified database fields, unavailable proprietary data, or undefined variable formulas.

### Writing and Revision

Read `references/writing-workflow.md` when the user asks for abstracts, introductions, theory sections, hypotheses, research-design prose, result narratives, contribution framing, or revision of manuscript text.

For manuscript work:

- Make the contribution explicit and credible, not inflated.
- Keep the introduction's logic in this order: phenomenon, tension, why accounting matters, design, findings, contribution.
- Distinguish statistical results from economic magnitudes and interpretation.
- Preserve the author's claims if defensible; weaken claims when the design does not support them.
- Do not turn writing tasks into journal submission strategy, reviewer response, PPT planning, or generic Nature/CNS prose.

## Output Standards

- Use English for manuscript-facing sections unless the user asks for Chinese.
- Use Chinese for planning discussion when the user writes in Chinese.
- Prefer structured tables for research design, literature mapping, and variable dictionaries.
- Include assumptions and caveats when evidence is incomplete.
- Do not invent citations, paper results, sample sizes, journal placements, database fields, regression results, variable values, or manuscript changes. Verify unstable publication facts with current sources.
- Flag ethical issues: p-hacking, undisclosed sample selection, HARKing, unavailable proprietary data, weak identification, and unsupported causal claims.
- Separate correlation, mechanism evidence, and causal identification. Use causal wording only when the design and assumptions support it.
- Mark unverified literature, data fields, and empirical claims explicitly rather than smoothing over uncertainty.

## Reference Files

- `references/agent-roles.md`: Boss-led multi-agent role definitions, runtime protocol, and output contracts.
- `references/literature-map.md`: literature review workflow, positioning matrix, OpenAlex discovery, and search guidance.
- `references/research-design.md`: empirical accounting design patterns, model templates, and validity checks.
- `references/data-and-variables.md`: common data sources, variable construction habits, and reproducibility checklist.
- `references/writing-workflow.md`: accounting and finance manuscript section writing workflow.
