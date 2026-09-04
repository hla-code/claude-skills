---
name: meridian-mmm-build
description: Scaffold, configure, and validate Google Meridian Bayesian Marketing Mix Models, channel priors, spend data preprocessing, and MCMC convergence diagnostics.
---

# Meridian MMM Build Skill

Use this skill when scaffolding, authoring Python model specifications, configuring priors, or validating data pipelines for Google Meridian Bayesian Marketing Mix Models.

## Process

1. **Input Data Schema & Tensor Preparation**: Validate required input tensors (`time`, `geo`, `kpi`, `media_spend`, `media_impressions`, `controls`, `population`) per [meridian-spec-template.md](file:///references/meridian-spec-template.md).
2. **Prior Distribution Definition**: Configure informative `PriorDistribution` objects for channel ROI (`roi_prior`), adstock decay (`alpha_prior`), and Hill saturation (`ec_50_prior` / `slope_prior`) using [meridian-priors-guide.md](file:///references/meridian-priors-guide.md).
3. **Model Configuration & Calibration**: Set `knots` for baseline trend, geo random effects (`geo_effects`), and media spend calibration matrices (e.g. from GeoLift / incrementality tests).
4. **MCMC Sampling & Diagnostics Execution**: Define `sample_posterior()` parameters (`n_chains`, `n_adapt`, `n_burnin`, `n_keep`), target acceptance rate, and convergence thresholds (R-hat < 1.05).
5. **Output Generation**: Produce complete, runnable Python code using the official `meridian` SDK.

## Output

Return:
- **Build Summary**: Model structure, dimension tensors, and calibration strategy
- **Executable Python Script**: Complete `meridian.model.ModelSpec` configuration and MCMC runner
- **Prior Verification Table**: Prior distributions, parameter bounds, and empirical justifications
- **Execution Checklist**: Pre-flight data validation commands and expected convergence metrics

