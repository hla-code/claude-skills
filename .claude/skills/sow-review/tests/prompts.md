# SOW Review Test Harness & Evaluation Prompts

## Test Case 1: High-Risk Fixed-Price Analytics Engagement
- **Input File**: `tests/input-risky.md`
- **User Prompt**: "Review this draft statement of work for an enterprise Meridian MMM project. Identify all delivery, scope, and commercial risks, and provide redline recommendations."
- **Expected Skill Behavior**:
  - Triggers the `sow-review` skill.
  - Identifies missing deemed acceptance period.
  - Flags unbounded "client satisfaction" clause in deliverable acceptance.
  - Detects absence of day-for-day schedule relief on client data delays.
  - Identifies broad IP assignment that threatens supplier's reusable MMM library.
  - Outputs structured verdict (`REVISE_AND_RESUBMIT`), Risk Matrix, and exact redline clauses.

## Test Case 2: Well-Structured Standard Pilot SOW
- **Input File**: `tests/input-good.md`
- **User Prompt**: "Review this short pilot statement of work for potential issues."
- **Expected Skill Behavior**:
  - Acknowledges clear binary acceptance criteria.
  - Identifies presence of 5-day deemed acceptance clause.
  - Issues `APPROVED` or `APPROVED_WITH_CONDITIONS` verdict with minor polish notes.

