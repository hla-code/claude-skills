# Meridian Priors & Calibration Guide

## Prior Distributions
- **oi_prior**: Prefer LogNormal(mean, sd) parameterized via experimental lift or historical conversion rates. Avoid broad Uniform or unbounded Normal priors.
- **lpha_prior (Adstock Decay)**: Use Beta(alpha, beta) with mean = 0.3 for short-decay digital and mean = 0.7 for long-decay awareness broadcast.
- **ec_50_prior (Half-Saturation)**: Calibrate to the 50th–70th percentile of historical weekly channel spend per geo.
- **slope_prior (Hill Saturation Slope)**: Gamma(shape=3.0, scale=0.5) for stable S-curve dynamics without step-function artifacts.
