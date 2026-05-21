# AR Skills

## Overview

**English:** This repository provides a Codex skill for accounting, finance, and financial management research. Its main skill, `accounting-research-assistant`, helps researchers turn broad ideas into rigorous research questions, literature maps, theory, empirical designs, data plans, reproducible coding plans, and manuscript-ready writing.

**中文：** 本仓库提供面向会计学、金融学和财务管理研究的 Codex Skill。核心 Skill `accounting-research-assistant` 用于帮助研究者从选题构思出发，逐步形成研究问题、文献图谱、理论机制、实证设计、数据方案、可复现代码计划和论文写作文本。

## Main Skill

- Skill name: `accounting-research-assistant`
- Version: `v0.1.2`
- Primary audience: accounting, finance, financial management, audit, disclosure, governance, ESG, capital markets, and China A-share empirical researchers.

## What It Helps With

- Topic development: refine broad interests into testable and feasible research questions.
- Literature understanding: build Chinese and English literature matrices, identify theoretical tensions, position a project, and mark verification status.
- Theory and hypotheses: develop mechanisms, competing explanations, boundary conditions, and testable predictions.
- Empirical design: plan samples, variables, models, fixed effects, clustering, robustness tests, mechanism tests, heterogeneity tests, and validity threats.
- Data and variables: define data sources, merge keys, sample filters, variable construction, winsorization, scaling, lagging, and reproducibility checks.
- Code planning: organize Stata-first empirical workflows, with Python used when text analysis, parsing, automation, or machine learning makes it more appropriate.
- Manuscript writing: draft or revise abstracts, introductions, theory sections, hypotheses, research design prose, results narratives, and contribution framing.

## Literature Workflow

The skill supports research-oriented literature discovery and verification. It can help plan and synthesize searches across:

- OpenAlex for preliminary English literature discovery and metadata screening.
- Google Scholar for recent English papers, working papers, citation trails, and recency checks.
- CNKI for Chinese literature, especially CSSCI and core accounting, finance, management, and economics journals.
- Publisher pages, SSRN, NBER, institutional repositories, journal pages, DOI pages, and CNKI detail pages for source verification.

The skill does not invent citation facts. Literature records should be marked as `verified`, `partially verified`, or `unverified` depending on the evidence available.

## Boundaries

This is a research-assistance skill, not a reference-library manager or publication-service workflow.

Out of scope:

- BibTeX/RIS creation, citation-file conversion, PDF library management, and Zotero collection operations.
- Bypassing paywalls, institutional access controls, CAPTCHA, or website anti-automation systems.
- Journal targeting, submission strategy, reviewer responses, appeal letters, seminar slides, and presentation production.
- Generic biomedical, laboratory, or Nature/CNS-style scientific writing workflows.

When citation files, PDFs, imports, exports, or Zotero collections are needed, those tasks should be handled by a Zotero-focused workflow instead.

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
