# Research Design

## Use For

Use this reference for empirical model planning, identification strategy, robustness checks, and threats to validity in accounting research.

Keep the design inside accounting, finance, and financial management research. This reference does not cover figure production, publication strategy, reviewer responses, or slide preparation.

## Intake Check

Before proposing a design, identify:

- Research question and key construct.
- Setting and institutional background.
- Unit of analysis: firm-year, firm-quarter, audit engagement, event, executive-year, director-year, analyst forecast, text document, or another stated grain.
- Inference goal: association, causal estimate, mechanism test, measurement validation, prediction, or descriptive mapping.
- Candidate data sources and whether they are available to the user.
- Treatment or key independent variable, outcome, timing, and plausible control group.

If the design depends on unavailable data, unverified database fields, or undefined timing, state the gap before giving model details.

## Baseline Archival Model

For firm-year or firm-quarter panels:

```text
Y_{i,t} = beta_0 + beta_1 X_{i,t} + Controls_{i,t} + FirmFE + YearFE + epsilon_{i,t}
```

Choose fixed effects based on the variation needed to identify beta_1:

- Firm fixed effects absorb time-invariant firm traits.
- Year or quarter fixed effects absorb common shocks.
- Industry-year fixed effects absorb sector-specific time shocks.
- Province-year or country-year fixed effects absorb location-level policy and macro shocks.
- Auditor-year, partner-year, or office-year fixed effects can matter in audit settings.

Cluster standard errors at the treatment assignment or shock level when possible. If treatment varies by firm over time, firm clustering is often a minimum; if policy varies by region-year or industry-year, cluster accordingly or use multi-way clustering.

## Identification Patterns

### Difference-in-Differences

Use when a treatment begins at different times or affects treated and control groups differently.

Checklist:

- Define treated group, control group, event date, and post period.
- Plot event-study coefficients and pre-trends.
- Explain why treated and control units would have followed parallel trends absent treatment.
- Check confounding contemporaneous shocks.
- Consider staggered-DID estimators when treatment timing varies and effects may be heterogeneous.
- Avoid DID if treatment timing, treatment assignment, or comparison units cannot be stated clearly.

### Event Study

Use for market reactions, disclosure events, enforcement announcements, restatements, or audit opinions.

Checklist:

- Define event date precisely.
- Choose event window and estimation window.
- Handle confounding events.
- Report abnormal returns or abnormal volume and economic magnitude.
- Avoid interpreting market reaction as long-run real effect.

### Instrumental Variables

Use only when exclusion restriction is plausible and explainable.

Checklist:

- Relevance: why the instrument predicts the endogenous variable.
- Exclusion: why the instrument affects outcome only through the endogenous variable.
- Monotonicity and local average treatment interpretation when relevant.
- Weak-instrument diagnostics.
- Do not propose an instrument only because it is correlated with the endogenous variable.

### Regression Discontinuity

Use when treatment changes at a known threshold.

Checklist:

- Show density or manipulation tests.
- Show covariate continuity.
- Use local windows and bandwidth sensitivity.
- Interpret estimates as local to the threshold.

### Matching or Reweighting

Use matching, entropy balancing, inverse-probability weighting, or coarsened exact matching to improve observable comparability, not as a substitute for an identification strategy.

Checklist:

- Define covariates measured before treatment.
- Report balance before and after adjustment.
- Explain remaining unobservable selection concerns.
- Avoid matching on post-treatment variables.

## Accounting-Specific Endogeneity Threats

- Omitted governance, culture, information environment, or enforcement intensity.
- Reverse causality between performance, reporting choices, and market outcomes.
- Selection into disclosure, audit quality, ownership, or voluntary assurance.
- Measurement error in constructs such as earnings quality, disclosure tone, readability, or ESG performance.
- Mechanical correlation when variables share components, such as accruals and earnings.
- Simultaneous regulatory changes in policy settings.

## Robustness and Falsification

Include tests matched to the main threat:

- Alternative dependent variable and key variable definitions.
- Alternative fixed effects and clustering.
- Placebo outcomes that should not respond.
- Placebo treatment dates or pseudo-treated groups.
- Entropy balancing, matching, or reweighting when observables differ.
- Excluding crisis years, regulated industries, state-owned firms, financial firms, or influential observations when justified.
- Heterogeneity tests tied to theory, not just data mining.

## Output Contract

For every empirical design, return:

- Research design summary: setting, unit, sample period if known, and inference goal.
- Variable table: dependent variable, key variable, controls, fixed effects, clustering, timing, and source.
- Model equation with clear subscripts and timing.
- Identification argument and why it may fail.
- Test architecture: main test, robustness, falsification, mechanism, and heterogeneity tests.
- Interpretation boundary: association, causal estimate, mechanism evidence, or prediction.
- Missing information and verification needs.

## Reporting Standards

Always separate:

- Statistical significance.
- Economic magnitude.
- Identification assumption.
- Interpretation boundary.

Use causal wording only when the design and assumptions support it.

## QA Checklist

- The unit of analysis matches the model, fixed effects, clustering, and data grain.
- Treatment timing is measured before the outcome.
- Controls are not mechanically part of the dependent variable unless justified.
- Fixed effects do not absorb the identifying variation.
- Clustering follows the treatment or shock level when possible.
- Robustness tests answer concrete threats rather than padding the design.
- Causal claims are downgraded when parallel trends, exclusion, continuity, or other core assumptions are weak.
