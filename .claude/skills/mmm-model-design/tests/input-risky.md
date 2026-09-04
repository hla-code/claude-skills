# Proposed Meridian MMM Model Specification

**Client**: D2C Ecommerce Apparel  
**Time Horizon**: 36 Weeks (May 2025 – January 2026)  
**Target Variable**: Total Weekly Sales ($)  
**Channels**:
1. Google Brand Search (Spend & Clicks)
2. Google Non-Brand Search (Spend & Clicks)
3. Facebook/Instagram Performance Ads (Spend & Impressions)
4. National Linear TV (Spend & GRPs)

**Proposed Prior Configuration**:
- Flat Uniform priors `Uniform(0, 100)` for all channel ROI parameters.
- Geometric adstock parameter $\alpha = 0.9$ fixed across all channels including Brand Search.
- No exogenous holiday or promotional controls included.
