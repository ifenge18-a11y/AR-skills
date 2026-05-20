# Accounting Research Assistant 说明文档

## 简介

当前版本：`v0.1.0`

`accounting-research-assistant` 是一个面向会计学、财务管理和公司金融研究的 Codex Skill。它用于辅助研究者完成从选题构思、文献理解、理论分析、实证设计、数据规划、代码方案到论文写作与修改的研究流程。

该 Skill 特别适合会计学术论文、A 股实证研究、审计研究、信息披露研究、财务报告质量研究、公司治理研究、ESG 与可持续披露研究、资本市场会计研究、论文文本修改和研究计划制定。

## 功能边界

该 Skill 保持单一结构，不拆分为多个独立 skill。它聚焦于会计、金融和财务管理研究本身，不处理做图、投稿发表策略、审稿回复、PPT 汇报、Nature/CNS 风格泛科研写作或生物医学工作流。

文献引用、题录导入导出、BibTeX/RIS、PDF 管理和 Zotero collection 操作交给 Zotero 工作流处理。本 Skill 只负责判断文献如何支持研究问题、理论、设计和写作。

## 主要功能

- 选题与研究问题提炼：将宽泛兴趣转化为可检验、可执行的研究问题。
- 文献理解与定位：构建中英文文献矩阵，识别理论张力、研究缺口和贡献边界，并标注文献真实性状态。
- 理论分析与假设提出：基于文献和会计制度背景，形成机制、竞争解释、边界条件和可检验假设。
- 实证研究设计：规划样本、变量、模型、固定效应、聚类标准误、主检验、稳健性检验、内生性检验、机制检验和异质性检验。
- 数据与变量规划：明确数据来源、合并键、变量定义、样本筛选、缩尾处理和可复现流程。
- Stata 与 Python 分析方案：以 Stata 为主要实证工具，必要时使用 Python 进行文本分析、文件处理或机器学习任务。
- 论文写作与修改：辅助撰写摘要、引言、理论部分、研究设计、结果叙述和贡献表述。

## 多 Agent 团队模式

该 Skill 支持 Boss-led multi-agent 工作流。用户明确要求多 agent、团队协作、Boss-led 模式，或使用默认多 agent 提示时，Boss 会先制定研究计划，再按阶段创建独立角色 agent。

默认角色包括：

- Boss：负责研究计划、方向判断、批判审查和角色协调。
- Literature Reviewer：使用 OpenAlex 初筛英文文献，使用 Chrome 检索 Google Scholar 最新英文文献和 CNKI 中文文献，并负责文献矩阵、研究定位与真实性核验；引用管理交给 Zotero。
- Theory Analyst：负责机制提炼、竞争解释、边界条件和假设构建。
- Empirical Designer：负责样本、变量、模型和完整检验体系设计。
- Research Coder：负责将实证设计转化为 Stata/Python 可复现分析流程。
- Writer：负责整合各角色结果并形成论文式文本。

Boss 默认采用阶段式并行：先启动文献综述角色，在初步文献结果稳定后并行推进理论分析和实证设计，再依次进入程序实现和写作整合。Boss 最后必须指出各角色输出中的逻辑漏洞、识别风险、文献缺口和写作问题。

## 文献与 Zotero 分工

该 Skill 支持文献检索路线设计、文献脉络整理、研究缺口识别和真实性标注。Zotero 负责引用和题录管理。

英文文献重点关注：

- The Accounting Review (AR/TAR)
- Journal of Accounting Research (JAR)
- Review of Accounting Studies (RAST)
- Contemporary Accounting Research (CAR)
- Journal of Accounting and Economics (JAE)

中文文献重点关注知网 CSSCI 来源，尤其是：

- 《经济研究》
- 《管理世界》
- 《会计研究》
- 《管理评论》
- 《金融研究》
- 《中国工业经济》

当用户要求检索文献时，Skill 可以先用 OpenAlex 初步发现英文候选文献；对最新英文文献，使用 Chrome 辅助检索 Google Scholar；对中文文献，使用 Chrome 辅助检索 CNKI。检索结果用于形成文献矩阵、研究定位和待核验清单。

当用户要求导入 Zotero、导出 BibTeX/RIS、管理 PDF、同步引用信息或维护 collection 时，应切换到 Zotero 工作流。

该流程不会绕过验证码、付费墙、机构权限或网站反自动化限制。遇到账号登录、验证码或权限确认时，会提醒用户手动处理。

## 输出特点

- 强调研究可执行性，优先输出表格、模型、变量字典、文献矩阵、代码计划和论文段落。
- 区分相关性和因果解释，避免过度声称因果关系。
- 明确标注假设、不确定性和待核验事项。
- 严禁虚构文献、样本量、期刊归属、数据库字段、变量取值、实证结果和论文修改事实。
- 对弱识别、p-hacking、HARKing、样本选择和不可获得数据等问题保持警惕。

## 典型用法

```text
Use $accounting-research-assistant in Boss-led multi-agent mode to turn my accounting research question into a rigorous literature, theory, identification, data, code, and writing plan.
```

也可以直接提出具体任务，例如：

- 帮我把“数字化转型与会计信息质量”发展成一个会计研究选题。
- 帮我检索管理层语调与审计费用相关的英文和中文文献，并整理成文献矩阵。
- 帮我设计一个 A 股上市公司实证研究，包括主检验、稳健性、内生性、机制和异质性。
- 帮我把现有结果写成论文引言和研究设计部分。

## 注意事项

该 Skill 是研究辅助工具，不替代研究者对文献真实性、数据权限、实证识别和论文伦理的最终判断。涉及最新文献、期刊状态、数据库字段、法规政策或具体论文事实时，应使用当前可靠来源进行核验。
