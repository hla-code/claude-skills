# Production Azure ML Deployment YAML (Compliant Baseline)

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: fraud-detector-prod
endpoint_name: payments-scoring-endpoint
model: azureml:fraud-model-xgboost:4
instance_type: Standard_DS4_v2
instance_count: 3
scale_settings:
  type: target_utilization
  min_instances: 2
  max_instances: 8
  target_utilization_percentage: 70
request_settings:
  request_timeout_ms: 1500
  max_concurrent_requests_per_instance: 4
liveness_probe:
  period: 10
  initial_delay: 30
  timeout: 2
  success_threshold: 1
  failure_threshold: 3
  path: /live
readiness_probe:
  period: 5
  initial_delay: 20
  timeout: 2
  success_threshold: 1
  failure_threshold: 3
  path: /ready
environment_variables:
  WORKERS_PER_CORE: "2"
  MODEL_CACHE_DIR: "/mnt/models"
```

