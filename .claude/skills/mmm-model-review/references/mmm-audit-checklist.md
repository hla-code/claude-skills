# Marketing Mix Model Audit Checklist

## 1. Data Integrity & Granularity
- [ ] Minimum 104 weeks (2 years) for national models; minimum 52 weeks for geo-level models with >= 30 DMAs.
- [ ] Media spend and exposure (impressions/clicks) variance verified (no long zero-variance stretches).
- [ ] Major promotional discounts, seasonality, and macro factors included as controls.

## 2. Parameter Plausibility
- [ ] Direct response channels (Search, Performance Social) have short half-lives (0.5 to 2.5 weeks).
- [ ] Brand awareness channels (TV, Video, Out-of-Home) have moderate half-lives (3 to 8 weeks).
- [ ] Channel contribution shares sum to reasonable total marketing contribution (typically 15% - 40% for established brands).
- [ ] Baseline sales explain 60% - 85% of volume and demonstrate stable organic trend.

## 3. Convergence & Fit Diagnostics
- [ ] Gelman-Rubin R-hat < 1.05 for all media coefficient parameters.
- [ ] Bulk & Tail Effective Sample Size (ESS) > 400.
- [ ] Out-of-sample MAPE < 10% on test holdout period.
- [ ] Durbin-Watson statistic between 1.7 and 2.3 (no severe autocorrelation in residuals).
