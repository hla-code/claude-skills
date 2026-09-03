---
name: sow-review
description: Review statements of work (SOWs), service agreements, and technical scopes for acceptance criteria, delivery risk, pricing assumptions, IP terms, and customer obligations.
---

# SOW Review

Use this skill when analyzing a statement of work, delivery proposal, service agreement, technical annex, or pilot project scope.

## Review Workflow

1. **Extraction & Baseline**: Identify the parties, workstreams, milestones, deliverables, timelines, pricing model, and customer obligations.
2. **Acceptance Criteria Verification**: Verify that every deliverable has an unambiguous, measurable acceptance event and sign-off window (refer to [acceptance-criteria-checklist.md](file:///references/acceptance-criteria-checklist.md)).
3. **Risk Identification**: Cross-reference against [risk-taxonomy.md](file:///references/risk-taxonomy.md) to flag:
   - Hidden dependencies, data access blockers, and client delays
   - Out-of-scope creep masquerading as standard delivery
   - Ambiguous IP, background licensing, or knowledge handover terms
   - Uncapped warranty or open-ended operational support commitments
4. **Remediation & Redlining**: Generate exact replacement wording using [replacement-clauses.md](file:///references/replacement-clauses.md) with specific insertion points.

## Required Output Format

Always structure the review as follows:

### 1. Executive Summary & Verdict
- **Status**: `[APPROVED | APPROVED_WITH_CONDITIONS | REVISE_AND_RESUBMIT]`
- **Verdict Summary**: 2–3 sentences summarizing the commercial and delivery viability.
- **Top 3 Risks**: Key blockers requiring executive alignment.

### 2. Risk Matrix
| Category | Identified Issue | Severity (High/Med/Low) | Impact | Recommended Fix |
| :--- | :--- | :--- | :--- | :--- |
| Scope & Deliverables | ... | ... | ... | ... |
| Acceptance & Sign-off | ... | ... | ... | ... |
| Client Dependencies | ... | ... | ... | ... |
| Commercial & IP | ... | ... | ... | ... |

### 3. Concrete Redline & Suggested Wording
For each flagged issue:
- **Location**: Section / Clause number
- **Identified Flaw**: Concise explanation of the loophole or ambiguity
- **Suggested Replacement**: Fenced markdown block with exact drafting language
- **Rationale**: Commercial or legal justification
