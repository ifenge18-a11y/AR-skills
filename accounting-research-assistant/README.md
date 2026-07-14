# Accounting Research Assistant / 会计研究助手

## Version / 版本

Current version: `v1.1.0`

当前版本：`v1.1.0`

## Overview / 概览

`accounting-research-assistant` is a Codex skill for accounting, finance, and financial management research. It helps researchers move from broad research interests to research questions, literature positioning, theory, empirical design, data planning, reproducible coding plans, and manuscript writing.

`accounting-research-assistant` 是一个面向会计学、金融学和财务管理研究的 Codex Skill，用于帮助研究者从宽泛研究兴趣出发，逐步形成研究问题、文献定位、理论机制、实证设计、数据方案、可复现代码计划和论文写作文本。

It is especially suited for accounting papers, A-share empirical studies, audit research, disclosure research, financial reporting quality, corporate governance, ESG and sustainability disclosure, capital-market accounting research, manuscript revision, and research-plan development. Verified durable literature and synthesis work flows through the project Obsidian research-wiki by default; v1.1.0 adds an explicit Research Base path for exploratory material that is not yet ready for the Knowledge Base.

该 Skill 特别适合会计学术论文、A 股实证研究、审计研究、信息披露研究、财务报告质量研究、公司治理研究、ESG 与可持续披露、资本市场会计研究、论文修改和研究计划制定。已核验的长期文献与综合判断默认进入项目 Obsidian research-wiki；v1.1.0 增加仅在明确启用时使用的 Research Base，用于尚未进入 Knowledge Base 的探索性内容。

## What's New in v1.1.0 / 当前版本改动

- Added an opt-in Research Base workflow for candidate topics, conversation notes, method prototypes, data-feasibility checks, design alternatives, and transparent retained decision history.
- Separated the evidence boundary: Zotero remains the reference layer; research-wiki Knowledge Base holds source-traceable or verified knowledge; Research Base holds explicitly labelled exploratory work.
- Added mandatory read-before-write, exact-path confirmation, metadata, index/log, no-duplicate-source-note, archive, and promotion checks for Research Base.
- Restricted promotion to explicit user instruction or project `AGENTS.md` authorization; promoted notes retain their original reasoning and reciprocal Knowledge Base links.
- Added maintainer acceptance scenarios for non-opt-in behavior, prototypes, source authority, promotion, archiving, and local language rules.

中文说明：

- 增加显式启用的 Research Base 工作流，用于候选选题、讨论记录、方法原型、数据可行性、设计备选和可追溯的决策历史。
- 明确证据边界：Zotero 仍是引用层；research-wiki Knowledge Base 保存可追溯或已核验知识；Research Base 保存明确标记的探索性内容。
- 为 Research Base 增加读后写前检查、准确路径确认、元数据、index/log、禁止重复 source note、归档和升级检查。
- 仅在用户明确要求或项目 `AGENTS.md` 授权后升级内容；升级笔记保留原始推理与 Knowledge Base 的双向链接。
- 增加未启用、原型、来源权威、升级、归档及本地语言规则等维护者验收场景。

## What's New in v1.0.0 / 当前版本改动

- Made `accounting-research-assistant` the research-control layer and `$research-wiki` the default persistent Obsidian knowledge layer for durable literature, theory, design, variable, method, and claim work.
- Added a default preflight for project knowledge: read `index.md`, `log.md`, and relevant `sources/`, `themes/`, `concepts/`, `methods/`, and `claims/` pages before external literature search when a project wiki exists.
- Updated the literature workflow so AR-skill checks Obsidian first, searches external sources second, screens Zotero candidates with Boss judgment, and files useful source notes or synthesis back through `$research-wiki`.
- Added the AR-to-research-wiki handoff fields: `project`, `zotero_item_key`, `boss_category`, `deep_read_priority`, `boss_screening_reason`, `pdf_status`, `project_use`, and `need_fulltext_read`.
- Kept first-write safety: before writing to an Obsidian project for the first time, the assistant must state the exact project path and get user confirmation.

中文说明：

- 将 `accounting-research-assistant` 明确为研究总控层，将 `$research-wiki` 设为默认 Obsidian 知识沉淀层，用于有长期价值的文献、理论、设计、变量、方法和 claim 工作。
- 增加项目知识库预检：如果项目 wiki 已存在，外部检索前先读取 `index.md`、`log.md` 以及相关 `sources/`、`themes/`、`concepts/`、`methods/`、`claims/` 页面。
- 更新文献流程：AR-skill 先查 Obsidian，再检索外部来源；Boss 筛选 Zotero 候选文献后，通过 `$research-wiki` 回写 source note 或综合页面。
- 增加 AR 到 research-wiki 的固定交接字段：`project`、`zotero_item_key`、`boss_category`、`deep_read_priority`、`boss_screening_reason`、`pdf_status`、`project_use` 和 `need_fulltext_read`。
- 保留首次写入安全规则：首次写入某个 Obsidian 项目前，必须说明确切项目路径并获得用户确认。

## What's New in v0.1.8 / 历史版本改动

- Added a Zotero candidate-record import workflow for Literature Reviewer outputs.
- Added Boss abstract screening after Zotero import, with fixed categories: `core_literature`, `related_stream`, `theory_mechanism`, `method_data`, `china_context`, and `excluded_weakfit`.
- Added fixed Boss deep-read priorities: `high`, `medium`, `low`, and `exclude`.
- Added Zotero screening fields: `boss_category`, `deep_read_priority`, `boss_screening_reason`, and `pdf_status`.
- Clarified that PDF retrieval, paywalled full-text access, CAPTCHA, institutional login, and full-text attachments are handled manually or by later Zotero cleanup, not by Literature Reviewer.

中文说明：

- 增加 Literature Reviewer 候选题录导入 Zotero 的流程。
- 增加 Zotero 导入后的 Boss 摘要筛选，固定分类为：`core_literature`、`related_stream`、`theory_mechanism`、`method_data`、`china_context` 和 `excluded_weakfit`。
- 增加 Boss 固定精读优先级：`high`、`medium`、`low` 和 `exclude`。
- 增加 Zotero 筛选字段：`boss_category`、`deep_read_priority`、`boss_screening_reason` 和 `pdf_status`。
- 明确 PDF 获取、付费全文、验证码、机构登录和全文附件由人工或后续 Zotero 清理流程处理，不由 Literature Reviewer 自动完成。

## What's New in v0.1.4 / 历史版本改动

- Upgraded Boss-led mode into a stage-gated collaboration workflow with literature screening, theory mechanism, research design, and writing quality gates.
- Added explicit Boss gate decisions: `PROCEED`, `REFINE`, and `PIVOT`.
- Updated the Literature Reviewer source policy: English literature uses OpenAlex for preliminary screening and Google Scholar for verification; Chinese literature uses CNKI only; working papers are searched only when explicitly requested.
- Kept Theory Analyst as one subagent while adding three internal perspectives: mechanism supporter, identification skeptic, and institutional-context reviewer.
- Tightened Research Coder and Writer start conditions so coding and writing begin only after Boss review of the relevant upstream outputs.

中文说明：

- 将 Boss-led 模式升级为“阶段门禁 + 角色协作”流程，包含文献筛选、理论机制、研究设计和写作质量四类门禁。
- 增加 Boss 门禁结论：`PROCEED`、`REFINE` 和 `PIVOT`。
- 更新 Literature Reviewer 文献来源规则：英文文献使用 OpenAlex 初筛、Google Scholar 核验；中文文献仅使用 CNKI；工作论文仅在用户明确要求时检索。
- 保持 Theory Analyst 为单一 subAgent，同时加入机制支持者、识别怀疑者和制度背景审查者三种内部视角。
- 收紧 Research Coder 和 Writer 启动条件，确保代码规划和写作在 Boss 审查上游输出后进行。

## What's New in v0.1.3 / 历史版本改动

- Added staged Literature Reviewer evidence packets for topic screening and post-topic deep reading.
- Added screening-packet fields for paper, verification, research problem, setting, constructs, main finding, relevance to topic, project use, and deep-read priority.
- Added deep-read-packet fields for mechanism chain, competing explanations, boundary conditions, data and sample, variables, identification strategy, empirical tests, limitations, and project implications.
- Clarified how Boss, Theory Analyst, and Empirical Designer read different fields from the same Literature Reviewer information package.

中文说明：

- 增加 Literature Reviewer 分阶段文献信息包，用于选题筛选和选题确定后的核心文献精读。
- 增加筛选信息包字段：题录、核验状态、研究问题、设定、核心构念、主要发现、与选题关系、项目用途和精读优先级。
- 增加精读信息包字段：机制链条、竞争解释、边界条件、数据和样本、变量、识别策略、实证检验、局限和对本项目的启发。
- 明确 Boss、Theory Analyst 和 Empirical Designer 如何从同一套 Literature Reviewer 信息包中读取所需字段。

## What's New in v0.1.2 / 历史版本改动

- Added a project-topic Zotero archiving model for Literature Reviewer outputs.
- Defined the default Zotero collection structure for research projects, including `00_Inbox_ToReview`, `01_Core_Literature`, `04_Method_Data`, and `90_Excluded_WeakFit`.
- Added a standard tag vocabulary for verification status, literature role, discovery source, and follow-up actions.
- Expanded the Literature Reviewer import/archiving contract to include suggested collection, tags, and Zotero actions while keeping actual library operations in Zotero.

中文说明：

- 增加 Literature Reviewer 输出到 Zotero 的“项目-主题型”归档模型。
- 明确研究项目默认 Zotero collection 结构，包括 `00_Inbox_ToReview`、`01_Core_Literature`、`04_Method_Data` 和 `90_Excluded_WeakFit`。
- 增加核验状态、文献作用、发现来源和后续动作的标准 tag 体系。
- 扩展 Literature Reviewer 的导入/归档要求：输出建议 collection、tags 和 Zotero actions，但实际文献库操作仍由 Zotero 完成。

## What's New in v0.1.1 / 历史版本改动

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

The skill treats literature search as research discovery, verification, and durable Obsidian knowledge capture, not as citation-library management.

该 Skill 将文献检索视为研究发现、事实核验和 Obsidian 知识沉淀，而不是引用库管理。

For durable project work, AR-skill first checks the project research-wiki, then searches external sources, screens records, and files useful source notes or synthesis back through `$research-wiki`.

对于有长期项目价值的工作，AR-skill 先检查项目 research-wiki，再检索外部来源、筛选文献，并通过 `$research-wiki` 把有用的 source note 或综合判断写回 Obsidian。

Literature Reviewer uses staged evidence packets. During topic discussion, it uses screening granularity to record each paper's verification status, research problem, setting, constructs, main finding, relevance to the topic, project use, and deep-read priority. After the topic is settled, theory-core and empirical-core papers are upgraded to deep-read granularity for mechanisms, competing explanations, boundary conditions, data, variables, identification, tests, limitations, and project implications.

Literature Reviewer 使用分阶段信息包。选题讨论阶段采用筛选粒度，记录每篇文献的核验状态、研究问题、设定、核心构念、主要发现、与选题的关系、项目用途和精读优先级。选题确定后，对理论核心和实证核心文献升级为精读粒度，提取机制链条、竞争解释、边界条件、数据、变量、识别、检验、局限和对本项目的启发。

Recommended routes:

- OpenAlex for preliminary English literature discovery and metadata screening.
- Google Scholar for English record verification after OpenAlex screening, including visible publication metadata, citation signals, and recency checks.
- CNKI for Chinese literature, especially CSSCI and core accounting, finance, management, and economics journals; CNKI records do not require extra verification.
- Working papers, SSRN, NBER, publisher pages, institutional repositories, DOI pages, and journal pages only when the user explicitly asks for working-paper coverage or deeper verification.

推荐路线：

- OpenAlex：用于英文文献初筛和元数据发现。
- Google Scholar：用于 OpenAlex 初筛后的英文记录核验，包括可见发表信息、引用信号和时效性检查。
- CNKI：用于中文文献，尤其是 CSSCI 和会计、金融、管理、经济类核心期刊；CNKI 记录无需额外核验。
- 工作论文、SSRN、NBER、出版商页面、机构库、DOI 页面和期刊页面：仅在用户明确要求工作论文覆盖或深度核验时使用。

When access prompts, login requirements, CAPTCHA, or permission checks appear, the workflow should pause and ask the user to handle them manually.

遇到登录、验证码、权限确认或访问限制时，工作流应暂停，并由用户手动处理。

For durable literature work, use the project-topic candidate-import model: one root Zotero collection per research project, fixed child collections such as `00_Inbox_ToReview`, `01_Core_Literature`, `04_Method_Data`, and `90_Excluded_WeakFit`, plus tags for verification status, project role, source, Boss screening category, deep-read priority, and follow-up action. Literature Reviewer imports usable new candidate records through the Zotero plugin when they should enter the reference library; Boss then screens titles and abstracts to decide which papers need deep reading and which research-wiki pages should be updated.

对于有长期价值的文献工作，采用“项目-主题型候选题录导入”模型：每个研究项目一个 Zotero 根 collection，下面使用 `00_Inbox_ToReview`、`01_Core_Literature`、`04_Method_Data`、`90_Excluded_WeakFit` 等固定子目录，并用 tag 标记核验状态、文献作用、来源、Boss 筛选分类、精读优先级和后续动作。当新文献应进入引用库时，Literature Reviewer 通过 Zotero 插件导入可用候选题录；Boss 再根据标题和摘要筛选哪些文献需要精读，以及哪些 research-wiki 页面需要更新。

Boss screening uses fixed fields: `project`, `zotero_item_key`, `boss_category`, `deep_read_priority`, `boss_screening_reason`, `pdf_status`, `project_use`, and `need_fulltext_read`. High-priority records should be marked `need_pdf` and `need_fulltext_read` unless a PDF is already available. PDF retrieval, paid access, CAPTCHA, institutional login, duplicate cleanup, citation keys, exports, and full-text attachments remain manual or later Zotero follow-up work.

Boss 筛选使用固定字段：`project`、`zotero_item_key`、`boss_category`、`deep_read_priority`、`boss_screening_reason`、`pdf_status`、`project_use` 和 `need_fulltext_read`。高优先级文献应标记 `need_pdf` 和 `need_fulltext_read`，除非 PDF 已经可用。PDF 获取、付费访问、验证码、机构登录、重复项清理、citation key、导出和全文附件仍由人工或后续 Zotero 流程处理。

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

- Citation-file generation, BibTeX/RIS conversion, PDF downloading, paywalled full-text access, CAPTCHA handling, institutional-login handling, attachment management, and broad Zotero library cleanup.
- Bypassing paywalls, institutional access controls, CAPTCHA, or website anti-automation systems.
- Journal targeting, submission strategy, reviewer responses, appeal letters, seminar slides, and presentation production.
- Generic biomedical, laboratory, or Nature/CNS-style scientific-writing workflows.

不在本 Skill 范围内：

- 生成引用文件、BibTeX/RIS 转换、PDF 下载、付费全文访问、验证码处理、机构登录处理、附件管理和广义 Zotero 文献库清理。
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
