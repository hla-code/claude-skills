# Claude Skill Authoring Guide

This guide establishes the engineering standards for authoring high-leverage **Claude Skills** (`.claude/skills/<skill-name>/...`).

---

## 1. The Progressive Disclosure Philosophy

Claude does not ingest your entire skills library into every prompt. Instead, it utilizes **Progressive Disclosure**:

```
[User Prompt]
      │
      ▼
[Phase 1: Catalog Scan]
Claude scans frontmatter 'name' and 'description' across all skills in .claude/skills/
      │
   Match? ──── No ───► Generic Claude execution
      │
     Yes
      ▼
[Phase 2: Procedural Load]
Claude dynamically reads .claude/skills/<skill-name>/SKILL.md
      │
      ▼
[Phase 3: Deep Retrieval]
Claude loads referenced documents in references/ only if required
```

### Implications for Authors:
1. **Description is the Routing Key**: Spend time refining the description. Include trigger conditions, domain terms, and operational keywords.
2. **Lean SKILL.md**: Keep the primary `SKILL.md` procedural, concise (< 500 words), and focused on the decision workflow and output schema.
3. **References as Domain Repositories**: Detailed checklists, clause libraries, regex patterns, and statistical lookup tables live inside `references/`.

---

## 2. Directory Layout Convention

Every skill in `.claude/skills/` must follow this structure:

```text
.claude/skills/<skill-name>/
├── SKILL.md                  # Main entry point (frontmatter + procedural guide)
├── references/               # Deep domain knowledge, checklists, templates
│   ├── checklist.md
│   └── domain-rules.md
├── scripts/                  # (Optional) Deterministic helper scripts (Python/Node)
└── tests/                    # Evaluation suite
    ├── prompts.md            # Benchmark prompts
    ├── input-sample.md       # Standard test document
    ├── input-risky.md        # Edge case / adversarial test document
    └── expected-eval.md      # Ground truth evaluation criteria
```

---

## 3. Writing Effective Frontmatter

```yaml
---
name: sow-review
description: Review statements of work (SOWs), service agreements, and technical scopes for acceptance criteria, delivery risk, pricing assumptions, IP terms, and customer obligations.
---
```

### Rules:
- **`name`**: Must be kebab-case and strictly match the folder name.
- **`description`**: Must be 30–350 characters. Start with active verbs ("Review...", "Design...", "Validate..."). Enumerate the primary entities and risk surfaces.

---

## 4. Output Contracts

Every skill must define an unambiguous **Required Output Format**. When Claude knows the exact markdown structure, table headers, and verdict enums to output, the quality and consistency of responses improve dramatically.
