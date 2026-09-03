#!/usr/bin/env python3
"""
Claude Skill Scaffolder CLI
Quickly scaffolds a new Claude skill adhering to canonical standards:
- .claude/skills/<name>/SKILL.md with frontmatter
- references/ directory
- tests/ directory with prompts.md and test cases
"""

import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / ".claude" / "skills"

SKILL_TEMPLATE = """---
name: {name}
description: {description}
---

# {title}

Use this skill when analyzing or performing {lowercase_title} workflows.

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
"""

CHECKLIST_TEMPLATE = """# {title} Checklist

## Core Evaluation Principles
- Verify clarity, precision, and alignment with project objectives.
- Guard against common edge cases and undocumented assumptions.

## Verification Items
- [ ] Requirement 1: Explicitly stated and measurable.
- [ ] Requirement 2: Dependencies and access prerequisites defined.
- [ ] Requirement 3: Fallback and error handling documented.
"""

PROMPTS_TEMPLATE = """# {title} Test Prompts & Harness

## Test Case 1: Standard / Happy Path
- **Input**: `tests/input-sample.md`
- **Prompt**: "Apply {name} to review the provided specification."
- **Expected Outcome**: Produces structured executive summary, risk table, and actionable recommendations.

## Test Case 2: Risky / Adversarial Input
- **Input**: `tests/input-risky.md`
- **Prompt**: "Evaluate this high-risk scenario using {name}."
- **Expected Outcome**: Correctly flags missing parameters, ambiguous clauses, and severe risks.
"""

INPUT_SAMPLE_TEMPLATE = """# Sample Input for {title}

Use this document to test standard execution of `{name}`.
"""

INPUT_RISKY_TEMPLATE = """# High-Risk / Edge Case Input for {title}

Use this document to verify that `{name}` catches subtle errors and omissions.
"""


def create_skill(name: str, description: str):
    name = name.strip().lower()
    if not name or " " in name:
        print("Error: Skill name must be kebab-case (e.g. mmm-review, sow-review).")
        sys.exit(1)

    skill_dir = SKILLS_DIR / name
    if skill_dir.exists():
        print(f"Error: Skill '{name}' already exists at {skill_dir}")
        sys.exit(1)

    ref_dir = skill_dir / "references"
    tests_dir = skill_dir / "tests"

    ref_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    title = " ".join(word.capitalize() for word in name.split("-"))
    lowercase_title = " ".join(name.split("-"))

    # Write SKILL.md
    (skill_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(
            name=name,
            description=description,
            title=title,
            lowercase_title=lowercase_title,
        ),
        encoding="utf-8",
    )

    # Write references
    (ref_dir / "checklist.md").write_text(
        CHECKLIST_TEMPLATE.format(title=title),
        encoding="utf-8",
    )

    # Write tests
    (tests_dir / "prompts.md").write_text(
        PROMPTS_TEMPLATE.format(title=title, name=name),
        encoding="utf-8",
    )
    (tests_dir / "input-sample.md").write_text(
        INPUT_SAMPLE_TEMPLATE.format(title=title, name=name),
        encoding="utf-8",
    )
    (tests_dir / "input-risky.md").write_text(
        INPUT_RISKY_TEMPLATE.format(title=title, name=name),
        encoding="utf-8",
    )

    print(f"✅ Successfully scaffolded Claude Skill '{name}' at:\n   {skill_dir}")
    print("\nFiles created:")
    print(f"  ├── SKILL.md")
    print(f"  ├── references/checklist.md")
    print(f"  └── tests/")
    print(f"      ├── prompts.md")
    print(f"      ├── input-sample.md")
    print(f"      └── input-risky.md")
    print(f"\nNext step: Run 'python scripts/lint_skills.py' to validate.")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new canonical Claude Skill.")
    parser.add_argument("--name", "-n", required=True, help="Skill name in kebab-case (e.g. sow-review)")
    parser.add_argument("--description", "-d", required=True, help="Trigger description for progressive disclosure (< 300 chars)")

    args = parser.parse_args()
    create_skill(args.name, args.description)


if __name__ == "__main__":
    main()
