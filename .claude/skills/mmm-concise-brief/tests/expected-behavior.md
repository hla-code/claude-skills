# Expected Evaluation Behavior: MMM Concise Brief

## Benchmark Criteria

1. **Compliant Input (input-good.md)**:
   - Total word count is under 200 words.
   - Zero conversational preamble or postamble (no Here is your summary).
   - Channel Action Matrix accurately assigns:
     - Brand Search: HOLD or INCREASE (mROAS 2.10 vs 1.20 target)
     - Non-Brand Search: INCREASE (mROAS 1.35 with 50% saturation room)
     - Meta Social: DECREASE (mROAS 0.75 is below 1.20 threshold and 92% saturated)
     - Linear TV: TEST (wide CI / early curve)

2. **Risky / Incomplete Input (input-risky.md)**:
   - Total word count remains under 150 words.
   - **Zero Hallucination**: Explicitly writes [MISSING] for TikTok Spend & ROAS, Paid Search Decay, and Overall Budget.
   - Does NOT guess or invent numbers.
   - Accurately assigns Affiliates as KILL or DECREASE (ROAS 0.60 vs 1.50 target) and TikTok as TEST (missing parameters).
