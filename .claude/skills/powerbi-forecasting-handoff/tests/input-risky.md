# Power BI Forecasting Model Spec (Risky & Flawed)

- **Architecture**: Single flat table MasterDump (120 columns, 15M rows) directly imported from Excel.
- **Relationships**: Bi-directional relationship between MasterDump and CustomerMaster causing ambiguous paths.
- **Measures**:
  - Sales Forecast = MasterDump[Sales] / MasterDump[Budget] (Implicit column calculation, divide-by-zero crashes on zero budget).
  - YTD Sales = CALCULATE(SUM(MasterDump[Sales]), FILTER(ALL(MasterDump), MasterDump[Date] <= MAX(MasterDump[Date]))) (Severe table-scan performance bottleneck).
- **Security**: No RLS configured (all users see global executive salaries).
- **Refresh**: Full import of 15M rows every 30 minutes.
