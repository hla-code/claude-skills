# Expected Evaluation Behavior: Meridian MMM Build

## Benchmark Criteria

1. **Compliant Input (input-good.md)**:
   - Generates clean, production-ready Python code importing meridian.
   - Properly integrates Meta GeoLift experimental prior (LogNormal with mean centered at 1.85 and sd bounded to the test CI).
   - Configures Geo random effects and spline knots for macro baseline trend.
   - Sets up MCMC sampling parameters with 4 chains and convergence checks.

2. **Risky Input (input-risky.md)**:
   - Rejects unviable 20-week dataset (insufficient sample size for MMM).
   - Rejects Uniform(0, 1000) and fixed 0.99 decay as statistically unsound.
   - Flags 25 micro-campaigns as severe multicollinearity and recommends aggregating into 4–5 macro channel groups.
