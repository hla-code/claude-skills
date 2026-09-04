# Estimated MMM Decomposition & Diagnostics (Flawed Audit Case)

- **Model Context**: National OLS / Bayesian MMM with only 40 weekly data points.
- **Convergence**: Max R-hat = 1.18 (MCMC failed to converge on channel betas).
- **Diagnostics**: Durbin-Watson = 0.82 (severe positive autocorrelation in residuals, unmodeled trend).
- **Decomposition**:
  - Baseline Revenue: 35% (dangerously low baseline for an established 10-year-old consumer brand).
  - Total Media Contribution: 65% (massive over-attribution to advertising).
- **Channel Estimates**:
  1. Brand Search: ROAS = .50, Half-life = 14.0 weeks (statistically impossible decay for brand search intent).
  2. Linear TV: ROAS = -.40 (negative beta left unconstrained).
  3. Meta Social: ROAS = .15, Hill slope = 0.1 (degenerate flat saturation curve).
