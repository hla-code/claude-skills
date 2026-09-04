# High-Risk Azure ML Deployment Configuration

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: fraud-detector-v1
endpoint_name: public-payments-endpoint
model: azureml:fraud-model-llm-heavy:latest  # Unpinned version
instance_type: Standard_F2s_v2              # Severely under-resourced for heavy LLM inference (2 vCPU, 4GB RAM)
instance_count: 1                           # Single instance (No SLA / SPOF)
request_settings:
  request_timeout_ms: 60000                 # Dangerously high timeout blocks queue
  max_concurrent_requests_per_instance: 50  # Over-concurrency causes OOM crashes
# Missing scale_settings (no autoscaling configured)
# Missing liveness_probe
# Missing readiness_probe (traffic hits uninitialized container)
environment_variables:
  AUTH_TOKEN_SECRET: "eyJhbGciOiJIUzI1NiIsIn..." # Hardcoded plaintext token
```

