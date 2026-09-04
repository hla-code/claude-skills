# Power BI Forecasting Handoff Test Prompts & Harness

## Test 1: Production Star-Schema Handoff Review (Compliant)
- **Input File**: 	ests/input-good.md
- **User Prompt**: Review this Power BI forecasting dataset documentation for enterprise production handoff.
- **Expected Skill Behavior**: Validates semantic model, confirms compliance with governance checklist, returns READY_FOR_PRODUCTION.

## Test 2: Flawed Flat-Model Handoff Review (Adversarial)
- **Input File**: 	ests/input-risky.md
- **User Prompt**: Audit this Power BI report model submitted by an analyst before deploying to executive workspace.
- **Expected Skill Behavior**: Identifies performance traps, DAX bottlenecks, divide-by-zero vulnerability, and returns ACTION_REQUIRED with optimized code.
