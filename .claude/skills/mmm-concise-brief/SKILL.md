---
name: mmm-concise-brief
description: Generate ultra-concise, zero-fluff MMM summaries with strict token limits, zero hallucination, and direct budget actions for ADHD/executive brevity.
---

# MMM Concise Brief Skill

Use this skill when analyzing Marketing Mix Modeling (MMM) outputs for rapid executive decisions, ADHD-friendly digestion, or when token budget and strict factual grounding are critical.

## Rules & Constraints

1. **Strict Token Budget**: Total response MUST be under 250 words. Be ruthlessly concise.
2. **Zero Hallucination**: Quote ONLY numbers and metrics explicitly provided in the prompt. If any metric is absent, write `[MISSING]`—NEVER invent, estimate, or extrapolate unprovided values.
3. **Zero Conversational Fluff**: No greetings, no preamble ("Sure, here is your summary..."), no methodology essays, and no sign-offs. Start directly with the `# Summary` header.
4. **Action Assignment**: For every channel, assign exactly one verdict: `INCREASE`, `DECREASE`, `HOLD`, `TEST`, or `KILL` based on [concise-decision-rules.md](file:///references/concise-decision-rules.md).

## Output Schema

Always format the response in this exact structure:

### 1. TL;DR (Max 2 Bullets)
- **Bottom Line**: [1 sentence summarizing total marketing health]
- **Key Shift**: [1 sentence on the biggest budget reallocation opportunity]

### 2. Channel Action Matrix
| Channel | Current Spend | ROAS / mROAS | Adstock Decay | Action | Tactical Rationale (<= 8 words) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | `[ACTION]` | ... |

### 3. Immediate Tactical Next Steps (3 Bullets Only)
1. **[Action 1]**: Concrete dollar shift or test to execute.
2. **[Action 2]**: Specific data gap to resolve.
3. **[Action 3]**: Follow-up experiment or timeline constraint.

