# Expected Evaluation Benchmark for sow-review

## Risky SOW Evaluation Criteria

When evaluating Claude's output on `tests/input-risky-sow.md`, verify the presence of the following key detections:

| Requirement | Pass Criteria |
| :--- | :--- |
| **Verdict** | Must issue `REVISE_AND_RESUBMIT` or `APPROVED_WITH_CONDITIONS` (Severe conditions). |
| **Subjective Acceptance Catch** | Flags Section 3 ("Client reserves the right to withhold final milestone payment until all stakeholders approve"). |
| **Data Dependency Relief** | Flags Section 4 ("in due course") and provides a day-for-day schedule relief clause. |
| **Training Scope Cap** | Flags Section 2.3 ("until they are proficient") and suggests capping to fixed hours/attendees. |
| **IP Overreach** | Flags Section 5 ("All code, models, templates... become exclusive property") and inserts Background IP carve-out. |
| **Deemed Acceptance** | Supplies replacement wording granting a 5-day deemed acceptance period. |
