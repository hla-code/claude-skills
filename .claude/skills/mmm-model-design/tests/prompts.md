# MMM Model Design Test Harness & Prompts

## Test Case 1: Prior & Architecture Review for Meridian Model
- **Input File**: `tests/input-risky-spec.md`
- **User Prompt**: "Review this proposed Google Meridian model specification. Flag statistical risks, prior misconfigurations, and data gaps."
- **Expected Skill Behavior**:
  - Catches the insufficient 36-week history for annual seasonality.
  - Flags flat/uninformative priors on TV and Digital spend.
  - Identifies multicollinearity between Google Brand and Non-Brand search.
  - Generates recommended prior distributions with Log-Normal formulations and half-life constraints.
