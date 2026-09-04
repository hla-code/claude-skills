---
name: powerbi-forecasting-handoff
description: Review and document Power BI forecasting models, DAX measures, time-series data schemas, refresh partition parameters, and stakeholder handoff specs.
---

# Power BI Forecasting Handoff Skill

Use this skill when preparing, reviewing, or documenting a Power BI forecasting solution for production handoff, governance review, or executive stakeholder delivery.

## Process

1. **Semantic Data Model & Star-Schema Audit**: Validate date table continuity, calendar granularity, fact-to-dimension relationships (1:*, single direction), and incremental refresh policies per [powerbi-handoff-checklist.md](file:///references/powerbi-handoff-checklist.md).
2. **DAX & Measure Auditing**: Inspect time intelligence calculations (e.g. YTD, YoY, rolling averages, forecast intervals) for performance and syntax efficiency per [dax-best-practices.md](file:///references/dax-best-practices.md).
3. **Forecasting Parameters & Confidence Bounds**: Verify algorithm parameters (Exponential Smoothing, ARIMA, ML endpoint), forecast length, seasonality cycles, and confidence intervals (80%/95%).
4. **Governance, Security & Refresh Validation**: Check Row-Level Security (RLS), scheduled refresh cadence, gateway configuration, and memory partition sizing.
5. **Handoff Documentation Generation**: Produce standardized stakeholder operating sheets and data dictionary entries.

## Output

Return:
- **Handoff Readiness Verdict**: `[READY_FOR_PRODUCTION | PRODUCTION_WITH_NOTES | ACTION_REQUIRED]`
- **Model Architecture & Star-Schema Summary**: Table relationships, grain, and refresh mechanism
- **DAX & Measure Review Table**:
  | Measure Name | DAX Expression | Complexity/Performance Flag | Suggested Optimization |
  | :--- | :--- | :--- | :--- |
- **Executive & Operational Runbook**: Refresh instructions, error triage steps, and RLS roles

