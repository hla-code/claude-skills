---
name: contract-risk-review
description: Review commercial contracts and vendor master service agreements for indemnification exposure, liability caps, termination clauses, and SLA penalties.
---

# Contract Risk Review Skill

Use this skill when auditing a Master Services Agreement (MSA), vendor contract, enterprise SaaS agreement, or commercial subcontract.

## Process

1. **Extraction & Baseline**: Identify contract structure, governing law, term, payment schedules, and critical milestone commitments.
2. **Liability & Indemnity Audit**: Inspect limitation of liability caps, super-caps, uncapped indemnity carveouts, and gross negligence definitions using [contract-risk-checklist.md](file:///references/contract-risk-checklist.md).
3. **Operational & IP Protection**: Verify background IP retention, work-product assignment limits, audit rights, and data confidentiality terms.
4. **Exit & Remedy Mechanics**: Check termination for convenience, cure periods, transition assistance obligations, and SLA penalty reciprocity.
5. **Redline Generation**: Formulate protective replacement wording using [standard-protective-clauses.md](file:///references/standard-protective-clauses.md) with exact clause references.

## Output

Return:
- **Overall Verdict**: `[APPROVED | APPROVED_WITH_CONDITIONS | REVISE_AND_RESUBMIT]`
- **Executive Summary**: 2–3 sentences on overall legal and commercial exposure.
- **Risk Classification Matrix**:
  | Category | Clause Ref | Severity (High/Med/Low) | Legal/Commercial Risk | Recommended Redline |
  | :--- | :--- | :--- | :--- | :--- |
- **Concrete Clause-by-Clause Redlines**: Fenced text blocks showing deleted and inserted language with precise clause numbers.

