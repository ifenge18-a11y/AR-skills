# Data and Variables

## Use For

Use this reference for database planning, variable definitions, sample construction, merge logic, and replication package preparation.

Keep this reference focused on data availability, variable construction, merge discipline, Stata/Python analysis planning, and reproducibility. Do not turn it into figure production, submission packaging, reviewer response support, or citation-library management.

## Intake Check

Before giving a data or variable plan, identify:

- Research setting and country or market.
- Unit of analysis and time frequency.
- Candidate data sources the user can access.
- Dependent variable, treatment or key independent variable, and core controls.
- Timing convention: fiscal year, calendar year, announcement date, event date, or reporting date.
- Software expectation: Stata by default for empirical accounting analysis; Python only for text, parsing, automation, or machine-learning tasks that Stata does not handle well.

If a database field, table name, or access right is uncertain, label it as unverified instead of presenting it as a fact.

## Common Data Sources

Potential sources depend on institutional setting:

- US firms: Compustat, CRSP, Audit Analytics, I/B/E/S, ExecuComp, BoardEx, SEC EDGAR, WRDS datasets.
- Audit: Audit Analytics, PCAOB inspection reports, audit reports, audit fee disclosures, partner-level data where available.
- China: CSMAR, WIND, RESSET, CNINFO filings, CNRDS, stock exchange inquiry letters, CSRC enforcement actions.
- International: Orbis, Worldscope, Datastream, Refinitiv, S&P Capital IQ, country-level governance or enforcement datasets.
- Text: annual reports, 10-K/10-Q filings, audit reports, conference calls, ESG reports, exchange comment letters, news.
- ESG and sustainability: Refinitiv ESG, MSCI, Sustainalytics, CSMAR ESG, Bloomberg ESG, company reports.

Verify exact table names and field availability before writing final code or variable definitions.

## Sample Construction

Record every filter:

| Step | Filter | Rationale | Observations removed | Observations remaining |
|---|---|---|---:|---:|

Typical filters:

- Remove financial firms or utilities when accounting ratios are structurally different.
- Require nonmissing dependent variable, key independent variable, and controls.
- Require sufficient data history for lagged variables or rolling measures.
- Winsorize continuous variables, usually at 1% and 99%, unless the field has a stronger convention.
- Align fiscal year, calendar year, announcement date, and market data windows carefully.
- Preserve the sample funnel even when observation counts are unknown; mark counts as `TBD` until data are run.

## Variable Dictionary

Use this table structure:

| Variable | Role | Definition | Timing | Source | Expected sign | Notes |
|---|---|---|---|---|---|---|

Specify:

- Numerator and denominator.
- Scaling and transformations.
- Lagging convention.
- Treatment coding.
- Missing value handling.
- Winsorization or trimming.
- Whether each variable is measured before, during, or after the outcome period.

## Merge Discipline

Before merging, define:

- Entity key: gvkey, permno, cik, stock code, auditor id, director id, executive id, city code, or country code.
- Time key: fiscal year, fiscal quarter, calendar date, event date, report date, or announcement date.
- Grain: one row per firm-year, firm-quarter, event, audit engagement, executive-year, director-year, or document.

After merging, check:

- Duplicate keys.
- Unmatched observations by source and year.
- Sudden sample loss.
- Impossible values, such as negative assets where not meaningful.
- Look-ahead bias from variables measured after the outcome.
- Many-to-many merges unless they are intentionally justified and audited.

## Code Planning

For Stata-centered workflows, specify:

- Ordered script names and responsibilities, such as import, clean, merge, construct variables, sample filters, descriptives, main regressions, robustness, and export tables.
- Required input files and expected output datasets for each step.
- Log files and sample-count checks after major filters and merges.
- Regression commands at the level of design, including fixed effects and clustered standard errors, without inventing unavailable variable names.

Use Python when needed for:

- Text extraction, document parsing, web or filing metadata processing, machine learning, and large-file preprocessing.
- Pre-Stata feature construction that produces an auditable dataset.

Do not use Python as a substitute for clear empirical design. Do not write code around unverified database fields or undefined formulas.

## Replication Package Checklist

For a clean replication package:

- Separate raw, intermediate, and final outputs.
- Keep a data manifest describing each input file and access restrictions.
- Use numbered scripts in execution order.
- Save logs and sample-count tables.
- Export final variable dictionary.
- Include code that recreates all tables and figures from the analysis dataset.
- Document proprietary data limitations and provide instructions for rebuilding when licenses allow.

## Output Contract

For data, variable, or code-planning tasks, return:

- Data source map with verified and unverified sources separated.
- Merge plan: keys, time alignment, grain, expected loss points, and duplicate checks.
- Variable dictionary with formulas, timing, scaling, source, and notes.
- Sample construction funnel with observation counts as `TBD` when not yet run.
- Script order and output artifacts.
- Reproducibility checks and unresolved data-access questions.

## QA Checklist

- No invented database fields, table names, sample sizes, or descriptive statistics.
- Variable timing avoids look-ahead bias.
- Merge keys match the unit of analysis.
- Winsorization, lagging, scaling, and missing-value rules are explicit.
- Proprietary or restricted data are identified as access-dependent.
- Stata/Python responsibilities are separated clearly.
