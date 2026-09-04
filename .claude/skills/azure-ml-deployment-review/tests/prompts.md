# Azure ML Deployment Review Test Prompts & Harness

## Test 1: Production Managed Online Deployment (Compliant)
- **Input File**: `tests/input-good.md`
- **User Prompt**: "Review this production Azure ML managed deployment specification for our payment scoring service."
- **Expected Skill Behavior**: Validates autoscaling rules, probes, and resource sizing. Returns `APPROVED` status.

## Test 2: High-Risk Unscaled Endpoint (Flawed)
- **Input File**: `tests/input-risky.md`
- **User Prompt**: "Perform an architectural risk audit on this Azure ML deployment YAML before we deploy to production."
- **Expected Skill Behavior**: Identifies single instance SPOF, missing liveness/readiness probes, extreme concurrency risk, and hardcoded secret. Returns `ACTION_REQUIRED` with drop-in YAML redlines.

