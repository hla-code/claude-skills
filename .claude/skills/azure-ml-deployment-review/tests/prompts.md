# Azure Ml Deployment Review Test Prompts & Harness

## Test Case 1: Standard / Happy Path
- **Input**: `tests/input-sample.md`
- **Prompt**: "Apply azure-ml-deployment-review to review the provided specification."
- **Expected Outcome**: Produces structured executive summary, risk table, and actionable recommendations.

## Test Case 2: Risky / Adversarial Input
- **Input**: `tests/input-risky.md`
- **Prompt**: "Evaluate this high-risk scenario using azure-ml-deployment-review."
- **Expected Outcome**: Correctly flags missing parameters, ambiguous clauses, and severe risks.
