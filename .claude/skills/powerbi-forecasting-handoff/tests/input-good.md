# Power BI Forecasting Model Spec (Compliant Baseline)

- **Architecture**: Star schema with DimDate (marked as Date Table, 2020-2027), DimProduct, DimRegion, and FactSales.
- **Relationships**: 1-to-many, single direction from dimensions to FactSales.
- **Measures**:
  - Actual Sales = SUM(FactSales[Amount])
  - Forecast Sales 30D = CALCULATE([Actual Sales], DATEADD(DimDate[Date], -30, DAY)) * [Growth Factor]
  - Forecast Upper 80% = [Forecast Sales 30D] + (1.28 * [Forecast StdError])
- **Refresh**: Incremental refresh (Store 3 years, refresh last 7 days) connected to Snowflake via DirectQuery/Import hybrid partition.
- **Security**: Dynamic RLS configured via USERPRINCIPALNAME() mapped to DimRegion[SecurityGroup].
