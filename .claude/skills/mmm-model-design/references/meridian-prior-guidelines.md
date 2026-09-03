# Meridian Prior Selection Guidelines

## 1. ROI / mROAS Priors
- **Informative Priors (Recommended)**: Use Log-Normal or Truncated Normal distributions centered on verified incrementality lift test results (e.g. Geo-experiments, Conversion Lift tests).
- **Default Prior Scaling**: If historical lift data is unavailable, use weakly informative Log-Normal priors centered on historical spend share with broad standard deviation to avoid bias.
- **Prohibited**: Uniform/flat unbounded priors that allow negative media coefficients or implausibly high ROAS (> 50x).

## 2. Adstock & Decay Parameters
| Channel Archetype | Recommended Decay Mode | Expected Half-Life Range |
| :--- | :--- | :--- |
| **Paid Search / Performance Lower Funnel** | Geometric | 0.5 – 2.0 weeks |
| **Paid Social / Dynamic Display** | Geometric or Weibull | 1.0 – 3.0 weeks |
| **Linear TV / Connected TV (CTV)** | Geometric or Weibull | 4.0 – 12.0 weeks |
| **Print / Out-of-Home (OOH)** | Geometric | 2.0 – 6.0 weeks |

## 3. Hill Saturation Parameters
- **Slope ($S$)**: Constrain between 0.5 and 3.0 to prevent step-function saturation.
- **Half-Saturation ($K$)**: Center near the channel median non-zero spend with Log-Normal prior.
