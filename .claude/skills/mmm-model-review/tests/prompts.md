# MMM Model Review Test Prompts & Harness

## Test 1: Production MMM Audit (Compliant)
- **Input File**: 	ests/input-good.md
- **User Prompt**:  Perform an executive audit on this MMM model output and confirm if it is ready to guide our quarterly budget allocation.
- **Expected Skill Behavior**: Returns VALIDATED, confirms robust diagnostics, and endorses decision readiness.

## Test 2: Flawed MMM Decomposition Audit (Adversarial)
- **Input File**: 	ests/input-risky.md
- **User Prompt**: Review these MMM model results. An external agency claims our media is driving 65% of all revenue.
- **Expected Skill Behavior**: Returns REVISE_AND_RE-ESTIMATE, identifies autocorrelation, over-attribution, non-convergence, and provides tactical remediation.
