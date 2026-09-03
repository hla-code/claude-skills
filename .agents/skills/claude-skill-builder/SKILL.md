---
name: claude-skill-builder
description: Guide and execute the end-to-end authoring, review, adversarial testing, linting, and packaging of Claude Skills under .claude/skills/<skill-name>/.
---

# Claude Skill Builder (Antigravity Workspace Skill)

Use this skill when creating, modifying, testing, or linting Claude Skills in this repository.

## Workflow

### 1. Scaffolding
When the user requests a new skill:
1. Run `python scripts/create_skill.py --name <name> --description "<description>"` or generate the directory structure under `.claude/skills/<name>/`.
2. Ensure folder name is kebab-case.

### 2. Drafting Core & References
1. **`SKILL.md`**:
   - Write valid YAML frontmatter (`name` matching folder, `description` between 30 and 350 chars).
   - Single top-level `# H1` header.
   - Keep the body lean (< 600 words) and purely procedural.
   - Provide a strict **Required Output Format** with tables and clear section headings.
2. **`references/`**:
   - Move all checklists, tables, taxonomies, and background documentation into `references/`.
   - Link to them from `SKILL.md` using relative links (e.g. `[checklist.md](file:///references/checklist.md)`).

### 3. Creating the Test Harness
Every skill must contain a `tests/` directory with:
- `prompts.md`: Benchmark prompts testing happy path and edge cases.
- `input-*.md`: Sample input documents (standard and risky/adversarial).
- `expected-eval.md`: Ground-truth evaluation checklist defining what Claude must catch.

### 4. Quality Gate Linting
Always run the repository linter before completing the task:
```bash
python scripts/lint_skills.py
```
Ensure 100% of checks pass with zero errors.
