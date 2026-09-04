# Google Meridian Model Specification Template

`python
import meridian
from meridian.model import spec
from meridian.data import load

# 1. Define Input Data
input_data = load.load_data(
    kpi= revenue,
    media_spend=[search_spend, social_spend, tv_spend],
    media_impressions=[search_impr, social_impr, tv_grps],
    controls=[cpi, holiday_flag, price_index],
    population=dma_population,
    geo=dma_code,
    time=week_start_date
)

# 2. Prior Distributions
roi_priors = {
    search: spec.LogNormal(mean=1.5, sd=0.3),
    social: spec.LogNormal(mean=0.8, sd=0.4),
    tv: spec.LogNormal(mean=0.5, sd=0.5),
}

# 3. Model Spec
model_spec = spec.ModelSpec(
    prior=spec.PriorDistribution(roi_priors=roi_priors),
    knots=12,  # Quarterly baseline spline knots
    geo_effects=spec.GeoEffects.RANDOM,
    adstock_decay_type=spec.AdstockDecayType.GEOMETRIC
)
`
