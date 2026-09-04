# Expected Evaluation Behavior: MMM Model Review

## Benchmark Criteria

1. **Compliant Input (input-good.md)**:
   - Status: VALIDATED
   - Confirms MCMC convergence (R-hat < 1.05, ESS > 800)
   - Validates baseline vs media contribution split (72% / 28%)
   - Confirms adstock half-lives align with channel characteristics

2. **Risky Input (input-risky.md)**:
   - Status: REVISE_AND_RE-ESTIMATE
   - Flags MCMC non-convergence (R-hat = 1.18)
   - Detects severe autocorrelation (DW = 0.82) indicating missing baseline trend/seasonality
   - Catches unrealistic 14-week half-life on Brand Search and .50 ROAS
   - Flags negative TV beta (-.40) and unrealistic 65% marketing contribution share
   - Recommends Bayesian priors, geo-level estimation, and non-negative constraints
