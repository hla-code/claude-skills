# MMM Concise Decision Rules & Anti-Hallucination Guardrails

## 1. Action Assignment Heuristics
- **INCREASE**: Marginal ROAS (mROAS) > Target Break-even ROAS AND channel is not heavily saturated.
- **DECREASE**: mROAS < Break-even ROAS OR channel is far past Hill saturation inflection point.
- **HOLD**: mROAS is near equilibrium AND spend is optimized.
- **TEST**: High uncertainty in priors, wide credible intervals, or conflicting incrementality lift results.
- **KILL**: Consistently negative or near-zero marginal contribution with no awareness spillover.

## 2. Anti-Hallucination & Token Economy Rules
1. **Never Fill in Blanks**: If the prompt says  Meta spend is ROAS is 1.8 and mentions Google Search without numbers, write Spend: [MISSING], ROAS: [MISSING]. Do NOT assume standard benchmark numbers as facts.
2. **Word Count Ceiling**: Total words must be < 250 words.
3. **Pointers over Essays**: Use bullets and tables rather than paragraphs.
