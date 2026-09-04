# MMM Concise Brief Test Prompts & Harness

## Test 1: Full MMM Multi-Channel Performance (Compliant)
- **Input File**: 	ests/input-good.md
- **User Prompt**: Give me a zero-fluff ADHD-friendly MMM brief. What do I increase decrease or hold?
- **Expected Skill Behavior**: Ultra-compact response (< 200 words), zero conversational filler, clear matrix, 3 concrete next moves.

## Test 2: Incomplete Data Anti-Hallucination Trap (Adversarial)
- **Input File**: 	ests/input-risky.md
- **User Prompt**: Summarize this MMM data quickly and tell me budget allocations.
- **Expected Skill Behavior**: Labels missing metrics as [MISSING] without guessing, stays under 150 words, and refuses to fabricate unprovided numbers.
