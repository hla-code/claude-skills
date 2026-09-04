# Contract Risk Review Test Prompts & Harness

## Test 1: Standard Balanced Master Agreement (Compliant)
- **Input File**: 	ests/input-good.md
- **User Prompt**:  Review this draft Master Services Agreement and confirm whether liability and IP provisions are balanced.
- **Expected Skill Behavior**: Returns APPROVED with confirmation of standard market terms.

## Test 2: High-Risk Enterprise Vendor Agreement (Adversarial)
- **Input File**: 	ests/input-risky.md
- **User Prompt**: Perform a rigorous commercial and legal risk audit on this enterprise vendor contract before our leadership signs.
- **Expected Skill Behavior**: Issues REVISE_AND_RESUBMIT, flags 4 critical risk triggers, and outputs protective redline clauses.
