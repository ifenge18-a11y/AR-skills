# Data and Variables

## Use For

Use this reference for database planning, variable definitions, sample construction, merge logic, and replication package preparation.

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

## Replication Package Checklist

For a clean replication package:

- Separate raw, intermediate, and final outputs.
- Keep a data manifest describing each input file and access restrictions.
- Use numbered scripts in execution order.
- Save logs and sample-count tables.
- Export final variable dictionary.
- Include code that recreates all tables and figures from the analysis dataset.
- Document proprietary data limitations and provide instructions for rebuilding when licenses allow.
