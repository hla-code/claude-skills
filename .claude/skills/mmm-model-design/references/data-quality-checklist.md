# MMM Data Quality & Pre-Modeling Checklist

## 1. Time Series Dimensions & Granularity
- **Minimum Duration**: At least 104 weeks (2 full years) of historical weekly data to decouple seasonal cycles from media spend effects.
- **Geo Aggregation**: Prefer Designated Market Area (DMA) or state-level data over national totals whenever media execution varies by region.

## 2. Spend Variance & Multicollinearity
- **Zero Variance Check**: Exclude channels with constant weekly spend (e.g. static sponsorships) as they collapse into baseline intercept.
- **Variance Inflation Factor (VIF)**: Keep channel-to-channel VIF < 5.0. If two digital channels co-vary heavily, consolidate or apply custom joint priors.
- **Zero Spend Ratio**: Channels with > 70% zero-spend weeks must be modeled with caution or combined.

## 3. Organic & Exogenous Controls
- Ensure baseline model incorporates:
  - Price elasticity / discounting index
  - Competitor spend or macro index (e.g. Consumer Sentiment)
  - Organic website traffic / search trends (careful: avoid endogeneity with paid search)
  - Calendar anomalies (Black Friday, Cyber Monday, Easter shifts)
