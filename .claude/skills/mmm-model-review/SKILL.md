---
name: mmm-model-review
description: Audit and review Marketing Mix Models (MMMs) for adstock decay half-lives, Hill saturation parameters, baseline trend collinearity, and channel attribution validity.
---

# MMM Model Review Skill

Use this skill when auditing, peer-reviewing, or validating the statistical soundness and commercial credibility of an estimated Marketing Mix Model (MMM).

## Process

1. **Parameter & Decomposition Audit**: Inspect channel ROI, contribution shares, baseline percentages, and adstock half-lives against [adstock-decay-benchmarks.md](file:///references/adstock-decay-benchmarks.md).
2. **Statistical Diagnostics & Quality Check**: Review MCMC convergence (R-hat, Effective Sample Size), holdout MAPE, residuals autocorrelation (Durbin-Watson), and variance inflation factors per [mmm-audit-checklist.md](file:///references/mmm-audit-checklist.md).
3. **Plausibility & Anomaly Detection**: Flag channels with negative ROI, unbounded decay windows, unrealistically high saturation inflection points, or collinearity with price discounts.
4. **Experimental Calibration Check**: Compare model-estimated incremental ROAS against geo-lift or matched-market incrementality test results.
5. **Remediation & Recommendation**: Suggest specific prior adjustments, channel groupings, or model reformulations.

## Output

Return:
- **Overall Verdict**: `[VALIDATED | VALIDATED_WITH_RESERVATIONS | REVISE_AND_RE-ESTIMATE]`
- **Executive Audit Summary**: 2–3 sentences on model credibility and business decision readiness.
- **Channel Diagnostics Table**:
  | Channel | Modeled ROI | Adstock Half-Life | Saturation Status | Credibility Flag | Recommended Action |
  | :--- | :--- | :--- | :--- | :--- | :--- |
- **Identified Flaws & Remediation Actions**: Explicit adjustments to priors, control variables, or data transformations.

