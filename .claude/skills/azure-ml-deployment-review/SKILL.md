---
name: azure-ml-deployment-review
description: Review Azure ML deployment configs for endpoint security, autoscaling, container sizing, and SLA risks.
---

# Azure Ml Deployment Review

Use this skill when analyzing or performing azure ml deployment review workflows.

## Workflow

1. **Context & Input Gathering**: Identify core objectives, constraints, inputs, and stakeholders.
2. **Analysis & Verification**: Validate against domain standards (refer to [checklist.md](file:///references/checklist.md)).
3. **Synthesis & Remediation**: Formulate precise recommendations, fixes, or implementation steps.

## Required Output Format

Always return the response in this structured layout:

### 1. Executive Summary
- **Status**: [APPROVED | ACTION_REQUIRED | REJECTED]
- **Key Takeaway**: 1–2 sentences summarizing the verdict.

### 2. Detailed Findings & Recommendations
| Area | Observation | Severity (High/Med/Low) | Recommended Action |
| :--- | :--- | :--- | :--- |
| ... | ... | ... | ... |

### 3. Concrete Action Items / Replacement Content
- Exact wording, code, or configuration changes ready for direct application.
