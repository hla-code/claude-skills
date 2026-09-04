# High-Quality Geo-Level Meridian MMM Specification (Compliant Baseline)

- **Model Framework**: Google Meridian (Bayesian Geo-level MMM)
- **Time Window**: 156 weeks (3 years), weekly cadence across top 50 Nielsen DMAs.
- **KPI**: Direct-to-Consumer Gross Revenue ().
- **Media Channels**:
  1. Search Brand: Geometric adstock, decay prior Beta(1, 4) (half-life ~1 week), LogNormal prior based on GeoLift calibration test (mROAS prior mean: 2.4, sd: 0.3).
  2. Search Non-Brand: Geometric adstock, decay prior Beta(2, 3) (half-life ~2-3 weeks), LogNormal prior (mROAS prior mean: 1.1, sd: 0.4).
  3. Paid Social Video: Weibull adstock (shape=2.0, scale=3.5), Hill saturation with half-saturation informed by historical spend percentiles.
  4. Linear TV: Geometric adstock (half-life 4-6 weeks), LogNormal prior based on matched-market test.
- **Controls**: Regional unemployment rate, consumer confidence index, base price index, national holiday dummies.
- **Diagnostics Target**: R-hat < 1.05 across all parameters, Effective Sample Size (ESS) > 600, Holdout MAPE < 7%.
