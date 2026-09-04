# Power BI Handoff & Governance Checklist

## 1. Data Modeling & Relationships
- [ ] Dedicated contiguous Date Dimension table marked as official Date Table.
- [ ] Pure Star-Schema structure (no bi-directional cross-filtering or snowflake loops).
- [ ] Fact tables have numeric surrogate keys; unnecessary high-cardinality text columns removed.
- [ ] Incremental refresh configured for fact tables with > 5M rows.

## 2. DAX Measure Standards
- [ ] Explicit measures used everywhere (zero implicit default summaries).
- [ ] Variables (VAR / RETURN) used for repeated filter expressions and sub-calculations.
- [ ] DIVIDE() used instead of / to eliminate division-by-zero errors.
- [ ] Time intelligence functions (DATESYTD, SAMEPERIODLASTYEAR, DATEADD) reference the Date Dimension column, not fact dates.

## 3. Governance & Operations
- [ ] RLS roles tested in Power BI Service with test users.
- [ ] Scheduled refresh window avoids upstream ETL processing overlap.
- [ ] Report documentation sheet included with metric definitions and refresh contact.
