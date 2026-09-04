# Claude Skills Factory

A production-grade engineering repository for designing, testing, linting, packaging, and versioning **Claude Skills** (`.claude/skills/<skill-name>/...`).

### Core Architectural Philosophy
- **Antigravity** as the agentic builder, test harness generator, and quality gate.
- **Claude** as the runtime execution engine (leveraging *Progressive Disclosure*).
- **Git** as the single source of truth and versioned distribution layer.

---

## 📁 Repository Structure

```text
claude-skills/
├── .claude/
│   └── skills/
│       ├── sow-review/                   # SOW & Scope Clarity Review
│       │   ├── SKILL.md                  # Lean procedural skill definition
│       │   ├── references/               # Checklists, clause templates, taxonomies
│       │   └── tests/                    # input-good.md, input-risky.md, expected-behavior.md, prompts.md
│       ├── contract-risk-review/         # Commercial & MSA Liability Risk Audit
│       ├── mmm-model-review/             # Post-Estimation Marketing Mix Model Audit
│       ├── meridian-mmm-build/           # Google Meridian Model Scaffolding & Priors
│       ├── mmm-model-design/             # Bayesian MMM Architecture & Prior Planning
│       ├── azure-ml-deployment-review/   # Azure ML Online Endpoints & Security
│       └── powerbi-forecasting-handoff/  # Power BI Forecasting Model & Governance Handoff
├── docs/
│   ├── skill-authoring-guide.md          # Progressive disclosure & authoring standards
│   └── antigravity-agentic-workflow.md   # Parallel multi-agent workflow pattern
├── scripts/
│   ├── lint_skills.py                    # Automated quality gate linter
│   └── create_skill.py                   # Canonical skill scaffolding CLI
├── CHANGELOG.md
└── README.md
```

---

## 🎯 Narrow, Repeatable Skills Catalog

| Skill Name | Scope / Trigger | Key References | Test Harness Status |
| :--- | :--- | :--- | :--- |
| **`sow-review`** | Scope clarity, acceptance events, IP terms, client dependencies, redlines | [Checklist](file:///.claude/skills/sow-review/references/acceptance-criteria-checklist.md), [Taxonomy](file:///.claude/skills/sow-review/references/risk-taxonomy.md), [Clauses](file:///.claude/skills/sow-review/references/replacement-clauses.md) | ✅ Passed (4/4 files) |
| **`contract-risk-review`** | Commercial liability caps, indemnities, SLA penalties, termination terms | [Checklist](file:///.claude/skills/contract-risk-review/references/contract-risk-checklist.md), [Protective Clauses](file:///.claude/skills/contract-risk-review/references/standard-protective-clauses.md) | ✅ Passed (4/4 files) |
| **`mmm-model-review`** | MMM decomposition audit, adstock decay half-lives, saturation, autocorrelation | [Checklist](file:///.claude/skills/mmm-model-review/references/mmm-audit-checklist.md), [Benchmarks](file:///.claude/skills/mmm-model-review/references/adstock-decay-benchmarks.md) | ✅ Passed (4/4 files) |
| **`meridian-mmm-build`** | Google Meridian Python pipelines, GeoLift priors, MCMC convergence | [Spec Template](file:///.claude/skills/meridian-mmm-build/references/meridian-spec-template.md), [Priors Guide](file:///.claude/skills/meridian-mmm-build/references/meridian-priors-guide.md) | ✅ Passed (4/4 files) |
| **`mmm-model-design`** | Bayesian MMM architecture design, prior planning, control variable selection | [Checklist](file:///.claude/skills/mmm-model-design/references/data-quality-checklist.md), [Priors Guide](file:///.claude/skills/mmm-model-design/references/meridian-prior-guidelines.md) | ✅ Passed (4/4 files) |
| **`azure-ml-deployment-review`** | Managed online endpoints, autoscaling rules, private links, container sizing | [Checklist](file:///.claude/skills/azure-ml-deployment-review/references/security-and-networking-checklist.md) | ✅ Passed (4/4 files) |
| **`powerbi-forecasting-handoff`** | Star-schema data models, DAX time-intelligence, incremental refresh, RLS | [Checklist](file:///.claude/skills/powerbi-forecasting-handoff/references/powerbi-handoff-checklist.md), [DAX Best Practices](file:///.claude/skills/powerbi-forecasting-handoff/references/dax-best-practices.md) | ✅ Passed (4/4 files) |

---

## ⚡ Developer Commands

### 1. Scaffolding a New Skill
Generate the canonical 4-part test harness and directory structure:
```bash
python scripts/create_skill.py --name "custom-skill-name" --description "Action-oriented description (< 350 chars) used for runtime progressive disclosure routing."
```

### 2. Validating Against Quality Gates
Run the automated linter to verify frontmatter, markdown structure, word count limits, reference links, and test harness completeness:
```bash
python scripts/lint_skills.py
```

### 3. Progressive Disclosure Design Rules
Claude inspects skills in 2 phases:
1. **Catalog Scan Stage**: Claude evaluates the frontmatter `name` and `description` across `.claude/skills/` to decide whether to activate the skill.
2. **Execution Stage**: Claude dynamically pulls `SKILL.md` and referenced files from `references/`.

Keep `SKILL.md` procedural, concise (< 500 words), and offload deep domain knowledge to `references/`.

---

## 🏷️ Versioning & Distribution

Skills are versioned independently using semantic git tags:
```bash
git tag v0.1-sow-review
git tag v0.1-contract-risk-review
git tag v0.1-meridian-mmm-build
git push origin --tags
```

