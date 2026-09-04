#!/usr/bin/env python3
"""
Claude Skill Scaffolder CLI
Quickly scaffolds a new Claude skill adhering to canonical standards:
- .claude/skills/<name>/SKILL.md with frontmatter & procedural process
- references/ directory with domain checklists and replacement templates
- tests/ directory with 4-part harness (input-good.md, input-risky.md, expected-behavior.md, prompts.md)
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

# {title} Skill

Use this skill when reviewing or performing {lowercase_title} workflows.

## Process

1. **Intake & Scope Mapping**: Identify core entities, inputs, constraints, and dependencies.
2. **Evaluation & Verification**: Validate against domain standards (refer to [checklist.md](file:///references/checklist.md)).
3. **Risk & Gap Assessment**: Flag ambiguities, operational bottlenecks, compliance gaps, and unstated assumptions.
4. **Remediation**: Formulate concrete replacement wording, configuration parameters, or tactical fixes.

## Output

Return:
- **Overall Verdict**: Status and high-level viability assessment
- **Strong Points**: Validated areas and robust parameters
- **Required Fixes**: Prioritized findings by severity
- **Suggested Wording / Redlines**: Concrete drop-in fixes
- **Insertion Points**: Specific section or clause coordinates for each change
"""

CHECKLIST_TEMPLATE = """# {title} Checklist

## Core Verification Principles
- Verify clarity, precision, and alignment with operational objectives.
- Guard against common edge cases, hidden dependencies, and unstated assumptions.

## Verification Items
- [ ] Requirement 1: Explicitly stated, measurable, and verified against acceptance criteria.
- [ ] Requirement 2: Dependencies, data access prerequisites, and environment setup defined.
- [ ] Requirement 3: Error handling, SLA bounds, and fallback procedures documented.
"""

PROMPTS_TEMPLATE = """# {title} Test Prompts & Harness

## Test 1: Compliant / Standard Input
- **File**: `tests/input-good.md`
- **Prompt**: "Review the provided {lowercase_title} artifact using the {name} skill."
- **Focus**: Verify that compliant items pass without false positives while confirming baseline rigor.

## Test 2: Risky / Flawed Input
- **File**: `tests/input-risky.md`
- **Prompt**: "Perform a rigorous review of this {lowercase_title} artifact using {name} and provide redlines."
- **Focus**: Verify that ambiguous clauses, hidden risks, and missing parameters are flagged with exact suggested wording.
"""

INPUT_GOOD_TEMPLATE = """# Compliant Baseline: {title}

This document contains a robust, well-defined example of `{name}` with clear criteria, explicit boundaries, and complete specifications.
"""

INPUT_RISKY_TEMPLATE = """# Risky / Flawed Baseline: {title}

This document contains deliberate omissions, ambiguous clauses, unstated dependencies, and risk surfaces designed to test the `{name}` skill.
"""

EXPECTED_BEHAVIOR_TEMPLATE = """# Expected Evaluation Behavior: {title}

## Benchmark Criteria

1. **Compliant Input (`input-good.md`)**:
   - Status: APPROVED or APPROVED_WITH_CONDITIONS
   - Confirms clarity and verifies required safeguards are met
   - Avoids hallucinating non-existent flaws

2. **Risky Input (`input-risky.md`)**:
   - Status: REVISE_AND_RESUBMIT or ACTION_REQUIRED
   - Accurately catches all planted ambiguities and risks
   - Generates concrete replacement wording and specifies exact insertion points
   - Distinguishes between commercial, technical, and delivery risks
"""


def create_skill(name: str, description: str):
    name = name.strip().lower()
    if not name or " " in name:
        print("Error: Skill name must be kebab-case (e.g. sow-review, mmm-model-review).")
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

    # Write tests (4 canonical files)
    (tests_dir / "prompts.md").write_text(
        PROMPTS_TEMPLATE.format(title=title, name=name, lowercase_title=lowercase_title),
        encoding="utf-8",
    )
    (tests_dir / "input-good.md").write_text(
        INPUT_GOOD_TEMPLATE.format(title=title, name=name),
        encoding="utf-8",
    )
    (tests_dir / "input-risky.md").write_text(
        INPUT_RISKY_TEMPLATE.format(title=title, name=name),
        encoding="utf-8",
    )
    (tests_dir / "expected-behavior.md").write_text(
        EXPECTED_BEHAVIOR_TEMPLATE.format(title=title),
        encoding="utf-8",
    )

    print(f"✅ Successfully scaffolded Claude Skill '{name}' at:\n   {skill_dir}")
    print("\nCanonical files created:")
    print(f"  ├── SKILL.md")
    print(f"  ├── references/checklist.md")
    print(f"  └── tests/")
    print(f"      ├── prompts.md")
    print(f"      ├── input-good.md")
    print(f"      ├── input-risky.md")
    print(f"      └── expected-behavior.md")
    print(f"\nNext step: Populate domain references and run 'python scripts/lint_skills.py'.")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new canonical Claude Skill.")
    parser.add_argument("--name", "-n", required=True, help="Skill name in kebab-case (e.g. sow-review)")
    parser.add_argument("--description", "-d", required=True, help="Trigger description for progressive disclosure (< 350 chars)")

    args = parser.parse_args()
    create_skill(args.name, args.description)


if __name__ == "__main__":
    main()
