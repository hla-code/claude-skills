# MMM Model Design Test Prompts & Harness

## Test 1: Geo-Level Meridian Architecture (Compliant)
- **Input File**: `tests/input-good.md`
- **User Prompt**: "Evaluate this proposed Geo-level Meridian MMM specification and confirm if the adstock decay priors and control structures are mathematically sound."
- **Expected Skill Behavior**: Validates informative priors, geo-level aggregation, Hill parameters, and convergence targets.

## Test 2: Flawed High-Risk MMM Spec (Adversarial)
- **Input File**: `tests/input-risky.md`
- **User Prompt**: "Design and audit this MMM architecture for an e-commerce brand."
- **Expected Skill Behavior**: Catches lack of degrees of freedom (26 weeks national data), unbounded priors on low-spend channels, missing organic seasonality, and multicollinearity between promotions and media spend.
