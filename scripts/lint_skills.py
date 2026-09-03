#!/usr/bin/env python3
"""
Claude Skill Quality Gate Linter
Validates Claude skills for frontmatter correctness, progressive disclosure design,
reference link integrity, test harness completeness, and token compactness.
"""

import sys
import re
from pathlib import Path
import yaml

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT_DIR / ".claude" / "skills"


def check_skill(skill_dir: Path) -> list[str]:
    errors = []
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"Missing required SKILL.md file in {skill_dir}"]

    content = skill_md.read_text(encoding="utf-8")

    # 1. Frontmatter validation
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not frontmatter_match:
        errors.append("Invalid or missing YAML frontmatter enclosed in '---'")
        return errors

    fm_raw, body = frontmatter_match.groups()
    try:
        fm = yaml.safe_load(fm_raw)
    except yaml.YAMLError as e:
        errors.append(f"YAML parsing error in frontmatter: {e}")
        return errors

    if not isinstance(fm, dict):
        errors.append("Frontmatter must be a valid key-value mapping")
        return errors

    name = fm.get("name")
    if not name:
        errors.append("Missing required 'name' in frontmatter")
    elif name != skill_name:
        errors.append(f"Skill name in frontmatter ('{name}') does not match directory name ('{skill_name}')")
    elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
        errors.append(f"Skill name '{name}' must be kebab-case (e.g. sow-review)")

    desc = fm.get("description")
    if not desc:
        errors.append("Missing required 'description' in frontmatter")
    else:
        desc_clean = desc.strip()
        if len(desc_clean) < 30:
            errors.append(f"Description is too short ({len(desc_clean)} chars). Minimum 30 characters recommended for accurate Claude activation.")
        if len(desc_clean) > 350:
            errors.append(f"Description is too long ({len(desc_clean)} chars). Claude frontmatter descriptions should stay under 350 characters for progressive disclosure efficiency.")

    # 2. Markdown Structure checks
    h1_matches = re.findall(r"^#\s+(.+)$", body, re.MULTILINE)
    if len(h1_matches) == 0:
        errors.append("Missing top-level H1 header ('# Skill Title') in SKILL.md body")
    elif len(h1_matches) > 1:
        errors.append(f"Multiple H1 headers found ({len(h1_matches)}). Use a single H1 and H2/H3 for subsections.")

    word_count = len(body.split())
    if word_count > 800:
        errors.append(f"SKILL.md body is {word_count} words (exceeds recommended 800-word limit). Move domain knowledge into references/ folder to keep SKILL.md lean.")

    # 3. Check reference links
    ref_links = re.findall(r"\[.*?\]\((?:file:///)?references/([^\)]+)\)", body)
    references_dir = skill_dir / "references"
    for ref_file in ref_links:
        clean_ref = ref_file.split("#")[0]
        target_path = references_dir / clean_ref
        if not target_path.exists():
            errors.append(f"Broken reference link: references/{clean_ref} does not exist")

    # 4. Check Test Harness
    tests_dir = skill_dir / "tests"
    if not tests_dir.exists() or not tests_dir.is_dir():
        errors.append("Missing 'tests/' directory. Every skill must have a test harness.")
    else:
        prompts_file = tests_dir / "prompts.md"
        if not prompts_file.exists():
            errors.append("Missing 'tests/prompts.md'. Add representative test prompts and expected evaluation criteria.")
        
        test_files = list(tests_dir.glob("*.md"))
        if len(test_files) < 2:
            errors.append("Test harness should contain at least 2 files (e.g. prompts.md + input sample or expected eval).")

    return errors


def main():
    print("=" * 60)
    print(" Claude Skills Quality Gate Linter")
    print("=" * 60)

    if not SKILLS_DIR.exists():
        print(f"Error: Skills directory not found at {SKILLS_DIR}")
        sys.exit(1)

    skill_folders = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    if not skill_folders:
        print("No skills found in .claude/skills/")
        sys.exit(0)

    total_errors = 0
    passed = 0

    for skill_dir in sorted(skill_folders):
        errors = check_skill(skill_dir)
        if errors:
            print(f"\n❌ [FAIL] {skill_dir.name}")
            for err in errors:
                print(f"   - {err}")
            total_errors += len(errors)
        else:
            print(f"✅ [PASS] {skill_dir.name}")
            passed += 1

    print("\n" + "-" * 60)
    print(f"Summary: {passed}/{len(skill_folders)} skills passed. Total issues: {total_errors}")
    print("-" * 60)

    if total_errors > 0:
        sys.exit(1)
    else:
        print("All Claude skills passed quality gate validation! 🎉\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
