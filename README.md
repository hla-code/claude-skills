# Claude Skills Factory

A production-grade engineering repository for designing, testing, linting, packaging, and versioning **Claude Skills** (`.claude/skills/<skill-name>/...`).

Built on the architectural philosophy:
- **Antigravity** as the agentic builder, test harness generator, and quality gate.
- **Claude** as the runtime execution target (leveraging *Progressive Disclosure*).
- **Git** as the single source of truth and versioned distribution layer.

---

## 📁 Repository Structure

```text
claude-skills/
├── .claude/
│   └── skills/
│       ├── sow-review/                   # SOW & Service Agreement Review
│       │   ├── SKILL.md                  # Lean procedural skill definition
│       │   ├── references/               # Checklists, clause templates, taxonomies
│       │   └── tests/                    # Prompts, sample inputs, risky cases
│       └── mmm-model-design/             # Meridian / Marketing Mix Model Design
│           ├── SKILL.md
│           ├── references/
│           └── tests/
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

## ⚡ Quick Start

### 1. Scaffolding a New Skill
To generate a canonical skill boilerplate:
```bash
python scripts/create_skill.py --name "azure-ml-deployment-review" --description "Review Azure ML deployment configs for endpoint security, autoscaling, container sizing, and SLA risks."
```

### 2. Validating Against Quality Gates
Run the automated linter to verify frontmatter, markdown structure, broken reference links, and test harness completeness:
```bash
python scripts/lint_skills.py
```

### 3. Progressive Disclosure Design Rule
Claude inspects skills in 2 phases:
1. **Catalog Stage**: Claude reads only the frontmatter `name` and `description` to decide whether to activate the skill.
2. **Execution Stage**: Claude dynamically pulls `SKILL.md` and referenced files from `references/`.

Keep `SKILL.md` procedural, concise (< 500 words), and offload deep domain knowledge to `references/`.

---

## 🏷️ Versioning & Distribution

Skills are versioned independently using semantic git tags:
```bash
git tag v0.1-sow-review
git tag v0.2-sow-review
git push origin --tags
```
