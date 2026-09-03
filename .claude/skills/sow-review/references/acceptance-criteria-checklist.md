# Acceptance Criteria Checklist & Guardrails

## Core Principles
1. **Zero Subjective Criteria**: Prohibit phrases like "to client satisfaction", "good working order", or "meets industry standards" without numerical or deterministic definitions.
2. **Deemed Acceptance Window**: Every review period must contain explicit deemed acceptance language (e.g. 5 business days without written objection = deemed accepted).
3. **Single Remediation Cycle**: Non-acceptance notices must include written, itemized non-conformities; the supplier remediates once, and subsequent rejection triggers dispute escalation or change order.

## Red Flag Patterns & Suggested Guardrails

| Pattern | Risk Description | Recommended Guardrail Language |
| :--- | :--- | :--- |
| **Open-Ended Revisions** | "Provider will revise until approved." | "Includes up to two (2) consolidated rounds of client feedback within 5 business days of each draft submission." |
| **Vague Performance Benchmark** | "System operates quickly and smoothly under peak load." | "System maintains p95 latency under 350ms at up to 500 concurrent requests/sec as measured by load test suite." |
| **Silent Review Periods** | No explicit deadline for client sign-off. | "Client shall provide written acceptance or itemized rejection within five (5) business days. Failure to respond within this period constitutes deemed acceptance." |
| **Tying Milestone Payments to Operational Rollout** | Payment delayed by factors outside supplier control (e.g. user adoption). | "Payment milestone is triggered upon delivery and code freeze of Phase 2 artifacts, irrespective of client production rollout schedule." |
