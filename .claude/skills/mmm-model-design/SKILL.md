---
name: mmm-model-design
description: Design, review, and calibrate Marketing Mix Modeling (MMM) architectures using Google Meridian or Bayesian MMM frameworks, including channel hierarchy, prior selection, adstock, and saturation.
---

# Marketing Mix Model (MMM) Design

Use this skill when designing, scoping, or evaluating a Bayesian Marketing Mix Model (such as Google Meridian or lightweight Bayesian MMMs).

## Modeling Workflow

1. **Data Audit & Frequency Alignment**: Assess channel granularity (weekly vs daily, geo vs national), spend variability, and control variables per [data-quality-checklist.md](file:///references/data-quality-checklist.md).
2. **Prior Calibration**: Define informative Bayesian priors for ROI/mROAS and adstock decay rates based on experimental lift studies or industry benchmarks using [meridian-prior-guidelines.md](file:///references/meridian-prior-guidelines.md).
3. **Model Specification & Transformation**:
   - Set Hill saturation parameters (half-saturation, slope).
   - Configure geometric or Weibull adstock decay windows.
   - Specify organic controls, macro indicators (seasonality, CPI, trend), and baseline sales.
4. **Validation & Diagnostics Strategy**: Define R-hat convergence thresholds, out-of-sample holdout validation, and posterior predictive checks.

## Required Output Format

Always structure the MMM specification as follows:

### 1. Model Architecture Overview
- **Framework Target**: Google Meridian / Bayesian MMM
- **Aggregation Level**: [Geo-level | National] at [Weekly | Daily] resolution
- **Dependent Variable**: [Revenue | Conversions | Units]

### 2. Channel & Prior Specification Matrix
| Channel | Adstock Decay Type | Half-Life Range | Prior Distribution | Prior Mean / CI | Source/Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... | ... |

### 3. Controls, Seasonality & Exogenous Drivers
- List organic baseline factors, holiday indicators, and econometric controls.

### 4. Convergence & Evaluation Criteria
- Convergence targets (R-hat < 1.05, ESS > 400), out-of-sample MAPE threshold, and validation experiment calibration strategy.
