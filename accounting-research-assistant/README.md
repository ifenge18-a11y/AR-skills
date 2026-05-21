# Accounting Research Assistant / 会计研究助手

## Version / 版本

Current version: `v0.1.1`

当前版本：`v0.1.1`

## Overview / 概览

`accounting-research-assistant` is a Codex skill for accounting, finance, and financial management research. It helps researchers move from broad research interests to research questions, literature positioning, theory, empirical design, data planning, reproducible coding plans, and manuscript writing.

`accounting-research-assistant` 是一个面向会计学、金融学和财务管理研究的 Codex Skill，用于帮助研究者从宽泛研究兴趣出发，逐步形成研究问题、文献定位、理论机制、实证设计、数据方案、可复现代码计划和论文写作文本。

It is especially suited for accounting papers, A-share empirical studies, audit research, disclosure research, financial reporting quality, corporate governance, ESG and sustainability disclosure, capital-market accounting research, manuscript revision, and research-plan development.

该 Skill 特别适合会计学术论文、A 股实证研究、审计研究、信息披露研究、财务报告质量研究、公司治理研究、ESG 与可持续披露、资本市场会计研究、论文修改和研究计划制定。

## What's New in v0.1.1 / 当前版本改动

- Added a single integrated research-assistant skill for accounting, finance, and financial management research.
- Built structured workflows for topic development, literature mapping, theory and hypotheses, empirical design, data planning, code planning, and manuscript writing.
- Added Boss-led multi-agent support for complex research planning, with roles for literature review, theory, empirical design, coding plans, writing, and final critical review.
- Strengthened the Literature Reviewer workflow for bilingual literature discovery and verification.
- Added clearer guidance for using OpenAlex, Google Scholar, CNKI, publisher pages, SSRN, NBER, institutional repositories, DOI pages, and CNKI detail pages as complementary literature routes.
- Added more explicit verification labels: `verified`, `partially verified`, and `unverified`.
- Clarified the boundary between research interpretation and reference-library management: Zotero handles citation files, imports, exports, PDFs, and collections.
- Clarified access and ethics boundaries: the skill does not bypass paywalls, institutional access controls, CAPTCHA, or website anti-automation systems.

中文说明：

- 新增一个整合式会计、金融和财务管理研究辅助 Skill。
- 建立选题、文献定位、理论与假设、实证设计、数据规划、代码规划和论文写作的结构化工作流。
- 增加 Boss-led 多 Agent 研究团队模式，用于复杂研究计划，覆盖文献综述、理论分析、实证设计、代码方案、写作整合和最终批判审查。
- 强化 Literature Reviewer 的中英文文献发现和核验流程。
- 明确 OpenAlex、Google Scholar、CNKI、出版商页面、SSRN、NBER、机构库、DOI 页面和 CNKI 详情页之间的互补检索路线。
- 增加更清晰的文献真实性标签：`verified`、`partially verified`、`unverified`。
- 明确研究解释和引用库管理的边界：Zotero 负责题录、导入导出、PDF 和 collection 管理。
- 明确访问和研究伦理边界：该 Skill 不绕过付费墙、机构权限、验证码或网站反自动化机制。

## Core Capabilities / 核心功能

- Topic development: refine broad ideas into feasible and testable research questions.
- Literature mapping: organize Chinese and English literature, identify theoretical tensions, position a project, and record verification status.
- Theory and hypotheses: develop mechanisms, competing explanations, boundary conditions, and observable predictions.
- Empirical design: plan samples, variables, models, fixed effects, clustering, robustness tests, mechanism tests, heterogeneity tests, and validity threats.
- Data and variables: define data sources, merge keys, sample filters, variable construction, scaling, lagging, winsorization, and reproducibility checks.
- Code planning: design Stata-first empirical workflows, with Python used when better suited for text analysis, parsing, automation, or machine learning.
- Manuscript writing: draft or revise abstracts, introductions, theory sections, hypotheses, research-design prose, results narratives, and contribution framing.

中文功能概括：

- 选题发展：将宽泛兴趣转化为可执行、可检验的研究问题。
- 文献定位：整理中英文文献，识别理论张力、研究缺口和贡献边界，并记录核验状态。
- 理论与假设：构建机制、竞争解释、边界条件和可观察预测。
- 实证设计：规划样本、变量、模型、固定效应、聚类标准误、稳健性、机制和异质性检验。
- 数据与变量：明确数据来源、合并键、样本筛选、变量定义、缩放、滞后、缩尾和可复现检查。
- 代码规划：以 Stata 实证流程为主，必要时使用 Python 处理文本分析、文件解析、自动化或机器学习任务。
- 论文写作：辅助撰写或修改摘要、引言、理论部分、假设、研究设计、结果叙述和贡献表述。

## Literature Workflow / 文献工作流

The skill treats literature search as research discovery and verification, not as citation-library management.

该 Skill 将文献检索视为研究发现和事实核验，而不是引用库管理。

Recommended routes:

- OpenAlex for preliminary English literature discovery and metadata screening.
- Google Scholar for recent papers, working papers, citation trails, and recency checks.
- CNKI for Chinese literature, especially CSSCI and core accounting, finance, management, and economics journals.
- Publisher pages, SSRN, NBER, institutional repositories, DOI pages, journal pages, and CNKI detail pages for verification.

推荐路线：

- OpenAlex：用于英文文献初筛和元数据发现。
- Google Scholar：用于最新英文文献、working paper、引用链和时效性检查。
- CNKI：用于中文文献，尤其是 CSSCI 和会计、金融、管理、经济类核心期刊。
- 出版商页面、SSRN、NBER、机构库、DOI 页面、期刊页面和 CNKI 详情页：用于文献信息核验。

When access prompts, login requirements, CAPTCHA, or permission checks appear, the workflow should pause and ask the user to handle them manually.

遇到登录、验证码、权限确认或访问限制时，工作流应暂停，并由用户手动处理。

## Boss-Led Multi-Agent Mode / Boss-Led 多 Agent 模式

When explicitly requested, the skill can use a Boss-led team structure:

- Boss: plans the work, coordinates roles, challenges weak logic, and synthesizes final output.
- Literature Reviewer: maps and verifies Chinese and English literature.
- Theory Analyst: develops mechanisms, hypotheses, and competing explanations.
- Empirical Designer: plans the empirical strategy and validity checks.
- Research Coder: converts the design into a reproducible Stata/Python workflow.
- Writer: integrates the research plan into manuscript-ready prose.

在用户明确要求时，该 Skill 可以使用 Boss-led 团队结构：

- Boss：制定计划、协调角色、审查逻辑漏洞并整合最终输出。
- Literature Reviewer：整理和核验中英文文献。
- Theory Analyst：构建机制、假设和竞争解释。
- Empirical Designer：规划实证策略和有效性检查。
- Research Coder：将研究设计转化为可复现 Stata/Python 工作流。
- Writer：将研究方案整合为论文式文本。

## Boundaries / 功能边界

Out of scope:

- Citation-file generation, BibTeX/RIS conversion, PDF-library management, and Zotero collection operations.
- Bypassing paywalls, institutional access controls, CAPTCHA, or website anti-automation systems.
- Journal targeting, submission strategy, reviewer responses, appeal letters, seminar slides, and presentation production.
- Generic biomedical, laboratory, or Nature/CNS-style scientific-writing workflows.

不在本 Skill 范围内：

- 生成引用文件、BibTeX/RIS 转换、PDF 文献库管理和 Zotero collection 操作。
- 绕过付费墙、机构权限、验证码或网站反自动化机制。
- 期刊投稿策略、审稿回复、申诉信、研讨会 PPT 或展示材料制作。
- 生物医学、实验室研究或 Nature/CNS 风格的泛科研写作流程。

## Typical Use / 典型用法

```text
Use $accounting-research-assistant to turn my accounting research question into a rigorous literature, theory, identification, data, code, and writing plan.
```

Example requests:

- Refine "digital transformation and accounting information quality" into a feasible accounting research topic.
- Search and organize English and Chinese literature on management tone and audit fees.
- Design an A-share empirical study with main tests, robustness tests, mechanism tests, and heterogeneity tests.
- Rewrite a paper introduction or research design section with stronger contribution framing.

示例请求：

- 帮我把“数字化转型与会计信息质量”发展成一个可行的会计研究选题。
- 帮我检索管理层语调与审计费用相关的中英文文献，并整理成文献矩阵。
- 帮我设计一个 A 股上市公司实证研究，包括主检验、稳健性检验、机制检验和异质性检验。
- 帮我修改论文引言或研究设计部分，使贡献表述更清晰。

## Research Standards / 研究标准

The skill should:

- Separate correlation, mechanism evidence, and causal identification.
- State assumptions, uncertainty, and missing verification items.
- Avoid inventing papers, journal placements, sample sizes, data fields, variable definitions, empirical findings, or manuscript facts.
- Flag weak identification, p-hacking, HARKing, sample-selection problems, and unavailable data.

该 Skill 应当：

- 区分相关性、机制证据和因果识别。
- 明确假设、不确定性和待核验事项。
- 避免虚构文献、期刊归属、样本量、数据库字段、变量定义、实证结果或论文事实。
- 提醒弱识别、p-hacking、HARKing、样本选择问题和不可获得数据等风险。
