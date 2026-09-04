# Flawed Meridian Build Request (Adversarial)

- **Dataset**: National aggregate data only, 20 weeks total.
- **Priors Requested**:
  - Set all ROI priors to Uniform(0, 1000) (completely uninformative).
  - Set adstock decay to fixed 0.99 for all channels.
  - Disable baseline knots (flat constant baseline).
- **Channels**: 25 separate micro-campaigns with zero impressions data.
