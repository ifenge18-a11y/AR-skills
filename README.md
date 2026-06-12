# AR Skills

## Overview

**English:** This repository provides Codex skills for academic research workflows. Its main maintained skill, `accounting-research-assistant`, supports accounting, finance, and financial management research from topic development through literature mapping, theory, empirical design, data planning, reproducible coding plans, and manuscript-ready writing.

**中文：** 本仓库提供面向学术研究流程的 Codex Skills。当前主要维护的 Skill 是 `accounting-research-assistant`，用于支持会计学、金融学和财务管理研究，从选题发展、文献定位、理论机制、实证设计、数据规划、可复现代码方案到论文写作。

## Main Skill

- Skill name: `accounting-research-assistant`
- Version: `v1.0.0`
- Primary audience: accounting, finance, financial management, audit, disclosure, governance, ESG, capital markets, and China A-share empirical researchers.

## Accounting Research Assistant v1.0.0

Version `v1.0.0` makes `accounting-research-assistant` the research-control layer and `$research-wiki` the default Obsidian knowledge-capture layer. For durable literature, theory, research-design, variable, method, and claim work, AR-skill should first consult the project research-wiki, then search or verify external sources, then write useful findings back to Obsidian through `$research-wiki`.

`v1.0.0` 将 `accounting-research-assistant` 明确为研究总控层，并将 `$research-wiki` 设为默认 Obsidian 知识沉淀层。对于有长期价值的文献、理论、研究设计、变量、方法和 claim 工作，AR-skill 应先读取项目 research-wiki，再检索或核验外部来源，最后通过 `$research-wiki` 把有用结论写回 Obsidian。

Key updates:

- Default research-wiki preflight before durable literature work: read `index.md`, `log.md`, and relevant source/synthesis pages when a project wiki exists.
- Default persistence after Boss screening or synthesis: update source notes and relevant `concepts/`, `themes/`, `methods/`, and `claims/` pages through `$research-wiki`.
- Fixed AR-to-research-wiki handoff fields: `project`, `zotero_item_key`, `boss_category`, `deep_read_priority`, `boss_screening_reason`, `pdf_status`, `project_use`, and `need_fulltext_read`.
- Zotero remains the reference-management layer; research-wiki remains the Obsidian knowledge layer; AR-skill remains responsible for research judgment.
- First writes to an Obsidian project still require explicit project-path confirmation.

主要更新：

- 有长期价值的文献工作默认先做 research-wiki 预检：如果项目 wiki 已存在，先读取 `index.md`、`log.md` 和相关 source/synthesis 页面。
- Boss 筛选或综合判断后，默认通过 `$research-wiki` 更新 source notes 以及相关 `concepts/`、`themes/`、`methods/`、`claims/` 页面。
- 固定 AR 到 research-wiki 的交接字段：`project`、`zotero_item_key`、`boss_category`、`deep_read_priority`、`boss_screening_reason`、`pdf_status`、`project_use` 和 `need_fulltext_read`。
- Zotero 仍是引用管理层；research-wiki 仍是 Obsidian 知识库层；AR-skill 仍负责研究判断。
- 首次写入某个 Obsidian 项目前，仍需明确项目路径并获得确认。

## What It Helps With

- Topic development: refine broad interests into testable and feasible research questions.
- Literature understanding: build Chinese and English literature matrices, identify theoretical tensions, position a project, and mark verification status.
- Obsidian knowledge capture: use `$research-wiki` by default to persist durable source notes, literature synthesis, methods, concepts, and claims.
- Theory and hypotheses: develop mechanisms, competing explanations, boundary conditions, and testable predictions.
- Empirical design: plan samples, variables, models, fixed effects, clustering, robustness tests, mechanism tests, heterogeneity tests, and validity threats.
- Data and variables: define data sources, merge keys, sample filters, variable construction, winsorization, scaling, lagging, and reproducibility checks.
- Code planning: organize Stata-first empirical workflows, with Python used when text analysis, parsing, automation, or machine learning makes it more appropriate.
- Manuscript writing: draft or revise abstracts, introductions, theory sections, hypotheses, research design prose, results narratives, and contribution framing.

## Literature Workflow

The skill supports research-oriented literature discovery, verification, and project knowledge capture. For durable project work, it should check the project Obsidian research-wiki before external search and file useful results back through `$research-wiki`.

It can help plan and synthesize searches across:

- Project Obsidian research-wiki for prior source notes, theme pages, method pages, claim pages, known blockers, and settled screening decisions.
- OpenAlex for preliminary English literature discovery and metadata screening.
- Google Scholar for English record verification after OpenAlex screening.
- CNKI for Chinese literature, especially CSSCI and core accounting, finance, management, and economics journals.
- Working papers, SSRN, NBER, publisher pages, institutional repositories, DOI pages, and journal pages only when explicitly requested or needed for deeper verification.

The skill does not invent citation facts. Literature records should be marked as `verified`, `partially verified`, `unverified`, or `CNKI record` depending on the evidence available.

## Boundaries

This is a research-assistance skill, not a reference-library manager or publication-service workflow.

Out of scope:

- BibTeX/RIS creation, citation-file conversion, PDF library management, duplicate cleanup, citation-key maintenance, and broad Zotero library cleanup.
- Bypassing paywalls, institutional access controls, CAPTCHA, or website anti-automation systems.
- Journal targeting, submission strategy, reviewer responses, appeal letters, seminar slides, and presentation production.
- Generic biomedical, laboratory, or Nature/CNS-style scientific writing workflows.

When citation files, PDF retrieval, exports, duplicate cleanup, or broad Zotero maintenance are needed, those tasks should be handled by a Zotero-focused or manual workflow instead.

## Boss-Led Research Team Mode

The skill can support a Boss-led multi-agent workflow when explicitly requested. In that mode, the Boss coordinates specialized research roles:

- Literature Reviewer: maps and verifies Chinese and English literature.
- Theory Analyst: develops mechanisms, hypotheses, and competing explanations.
- Empirical Designer: plans the empirical strategy and validity checks.
- Research Coder: turns the design into a reproducible Stata/Python workflow.
- Writer: integrates the research plan into manuscript-ready prose.

This mode is intended for complex research planning, not for simple single-step questions.

## Influences From Other Skills

This skill borrows practical workflow ideas from related research-support skills, while keeping the implementation focused on accounting research:

- Google Scholar search skills: structured search planning, recent-paper checks, citation-trail awareness, and recording useful search-result fields.
- CNKI search skills: Chinese literature search routines, CSSCI/core-journal attention, CNKI detail-page verification, and manual handling of login or access prompts.
- Zotero-oriented workflows: clear separation between research interpretation and reference-library management.
- Multi-agent research workflows: role separation between literature review, theory, empirical design, coding plans, writing, and final critical review.

## Typical Use

```text
Use $accounting-research-assistant to turn my accounting research question into a rigorous literature, theory, identification, data, code, and writing plan.
```

Example requests:

- Refine "digital transformation and accounting information quality" into a feasible accounting research topic.
- Search and organize English and Chinese literature on management tone and audit fees.
- Design an A-share empirical study with main tests, robustness tests, mechanism tests, and heterogeneity tests.
- Rewrite a paper introduction or research design section with stronger contribution framing.

## Research Standards

The skill is designed to be conservative about evidence. It should:

- Separate correlation, mechanism evidence, and causal identification.
- State assumptions, uncertainty, and missing verification items.
- Avoid unsupported claims about papers, journals, datasets, sample sizes, variables, or empirical results.
- Flag weak identification, p-hacking, HARKing, sample-selection problems, and unavailable data.

Researchers remain responsible for final judgments about literature accuracy, data permissions, empirical identification, and research ethics.
