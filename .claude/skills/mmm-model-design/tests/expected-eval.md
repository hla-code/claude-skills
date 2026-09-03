# Expected Evaluation Benchmark for mmm-model-design

## Evaluation Criteria for Risky Meridian Spec

When evaluating Claude's output on `tests/input-risky-spec.md`, verify the presence of the following critical detections:

| Requirement | Pass Criteria |
| :--- | :--- |
| **History Length Warning** | Flags that 36 weeks is insufficient to disentangle seasonality from media baseline (recommends minimum 104 weeks / 2 years). |
| **Prior Hazard Identification** | Rejects `Uniform(0, 100)` priors as uninformative and prone to extreme posterior distortion; recommends Log-Normal priors centered on incrementality tests or benchmarks. |
| **Adstock Decay Differentiation** | Rejects uniform $\alpha = 0.9$ (which represents excessive multi-month adstock for lower-funnel Brand Search); recommends $\alpha \in [0.1, 0.3]$ for Brand Search and higher decay only for TV. |
| **Omission of Controls** | Flags missing holiday (Q4/Black Friday) and promotional pricing discount controls. |
| **Structured Output** | Delivers full Channel & Prior Specification Matrix with corrected parameters. |
