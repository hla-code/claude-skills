# Azure ML Deployment Checklist

## 1. Compute & Scaling
- [ ] Instance count >= 2 for production SLA (zero single-point-of-failure).
- [ ] Autoscaling configured with CPU / latency metrics (min_instances, max_instances).
- [ ] Memory limit configured with minimum 25% headroom above peak batch inference footprint.
- [ ] GPU drivers and CUDA container image pinned to immutable tags.

## 2. Networking & Security
- [ ] `public_network_access: disabled` on workspace and online endpoints for private-link setups.
- [ ] VNet subnet allocated with sufficient IP address capacity for scaling spikes.
- [ ] Egress traffic routed through Azure Firewall or NAT Gateway with explicit FQDN whitelisting.
- [ ] Authentication set to `auth_mode: aml_token` or Microsoft Entra managed identity (avoid plain API key sharing).

## 3. Reliability & Health Probes
- [ ] Liveness probe path `/live` configured with initial delay > container startup time.
- [ ] Readiness probe path `/ready` testing model weights loaded in memory before accepting traffic.
- [ ] Blue/Green deployment strategy defined with explicit traffic allocation (e.g. 90/10 canary).

