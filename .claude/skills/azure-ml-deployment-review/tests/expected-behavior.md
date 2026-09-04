# Expected Evaluation Behavior: Azure ML Deployment Review

## Benchmark Criteria

1. **Compliant Input (input-good.md)**:
   - Status: APPROVED or APPROVED_WITH_CONDITIONS
   - Validates horizontal scaling configuration (min 2, max 8 instances)
   - Confirms health probes (/live and /ready) are defined
   - Validates adequate memory and timeout allocations

2. **Risky Input (input-risky.md)**:
   - Status: ACTION_REQUIRED
   - Flags single-instance SPOF (instance_count: 1) violating high-availability SLA
   - Detects missing health probes (liveness and readiness)
   - Identifies high risk of Out-Of-Memory (OOM) crashing due to under-provisioned Standard_F2s_v2 with max_concurrent_requests: 50
   - Flags security hazard: plaintext secret in environment_variables instead of Azure Key Vault reference
   - Provides concrete replacement YAML redline
