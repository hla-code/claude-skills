---
name: azure-ml-deployment-review
description: Review Azure ML managed online endpoints, compute sizing, autoscaling rules, private networking, egress security, and SLA readiness.
---

# Azure ML Deployment Review Skill

Use this skill when reviewing Azure Machine Learning (Azure ML) managed online endpoints, deployment YAML templates, inference container resource allocations, and production serving architectures.

## Process

1. **Endpoint & Infrastructure Inspection**: Verify compute SKU suitability, instance count, auto-scaling thresholds, and multi-zone redundancy.
2. **Network & Identity Security**: Check VNet integration, private endpoint configuration, egress lockdown, TLS termination, and Azure Managed Identity usage (refer to [security-and-networking-checklist.md](file:///references/security-and-networking-checklist.md)).
3. **Reliability & Probe Auditing**: Inspect liveness/readiness probes, container timeouts, retry policies, and blue/green traffic splitting.
4. **Cost & Sizing Verification**: Flag over-provisioned GPU/CPU allocations or under-provisioned memory limits that risk Out-Of-Memory (OOM) failures.
5. **Remediation**: Provide drop-in Azure CLI / ARM / Bicep / YAML snippets with exact parameter corrections.

## Output

Return:
- **Overall Verdict**: `[APPROVED | APPROVED_WITH_CONDITIONS | ACTION_REQUIRED]`
- **Deployment Health Summary**: 2–3 sentences on throughput, resilience, and security compliance.
- **Risk & Gap Matrix**: High / Medium / Low findings across compute, security, and scaling.
- **Suggested Configuration Fixes**: Drop-in YAML redlines with exact parameter paths.

