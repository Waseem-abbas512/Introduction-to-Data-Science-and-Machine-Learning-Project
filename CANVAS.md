# Agentic Data Science Canvas

**Project:** bakery-sales-forecast
**Team:** TBD
**Version:** 2026-11-16

> Owners: 👤 human decides · 🤖 agent drafts, human approves.
> Keep each block short. Details go in linked files; decisions go in `DECISIONS.md`.

---

## Problem

### 1. Decision 👤
For a one-off decision in a later, not-yet-specified season, the bakery’s operations manager chooses between continuing the current October-and-November offer and offering seasonal bread only in November. The target year and decision deadline remain open.

### 2. Questions 👤
Compare seasonal-bread turnover in October and November across the five historical selling seasons, including year-to-year variation, as descriptive evidence for the November-only alternative. The data does not observe the November-only counterfactual or establish the causal effect of removing October.

### 3. Audiences 👤
<!-- Who receives which result, in which form? At least: the decision-maker and the technical reader. -->

### 4. Success 👤
<!-- Metric(s), the baseline to beat, what is good enough to act on. Which errors are worse than others? -->

---

## Data and method

### 5. Data 🤖
The course bakery dataset records daily turnover by product group from 2013-07-01 through 2018-07-31. Seasonal bread is product group 6, recorded only from October through January (292 days total), spanning five selling seasons before the dataset ends. Winter 2022 is not covered. The data source does not state the currency. See the [dataset documentation](https://github.com/opencampus-sh/intro-to-data-science-and-ml/blob/main/data/bakery/README.md).

### 6. Known in advance 👤
Unknown. The operations manager needs to identify what information will be available by the actual decision deadline; do not use information observed after that point.

### 7. Data decisions 👤
<!-- Joins, missing values, encodings, exclusions, each with a reason. Link the entries in DECISIONS.md. -->

### 8. Checks 🤖
<!-- Checkpoints and the invariants that must hold at each (row counts, keys, date ranges, IDs, baseline). Link checks/. -->

---

## Evidence and action

### 9. Experiments 🤖
<!-- Experiment cards and their status; best result so far vs. baseline. Link experiments/LOG.md. -->

### 10. Findings 🤖
<!-- What we learned, how sure we are, and what the data cannot tell. -->

### 11. Recommendation 👤
<!-- What the decision-maker should do, under which conditions. Signed off by the team. -->

---

## Open questions
- Operations manager: specify the exact later season/year and calendar decision deadline.
- Operations manager: identify what sales, forecasts, inventory, costs, and other information will be available at that deadline.

## Decision log
See `DECISIONS.md`.
