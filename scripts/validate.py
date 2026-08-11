from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "align-before-action"
REQUIRED = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "NOTICE.md",
    ROOT / "evals" / "cases.yaml",
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "agents" / "openai.yaml",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        fail(f"missing required files: {', '.join(missing)}")

    texts = {path: read_utf8(path) for path in REQUIRED}
    skill_text = texts[SKILL_DIR / "SKILL.md"]
    match = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter = yaml.safe_load(match.group(1))
    if frontmatter.get("name") != "align-before-action":
        fail("frontmatter name must be align-before-action")
    description = frontmatter.get("description", "")
    if not isinstance(description, str) or not description.startswith("Use when"):
        fail("frontmatter description must state the trigger conditions")

    config = yaml.safe_load(texts[SKILL_DIR / "agents" / "openai.yaml"])
    interface = config.get("interface", {})
    if interface.get("display_name") != "Align Before Action":
        fail("display_name must be English: Align Before Action")
    if "$align-before-action" not in interface.get("default_prompt", ""):
        fail("default_prompt must explicitly invoke $align-before-action")
    if config.get("policy", {}).get("allow_implicit_invocation") is not True:
        fail("allow_implicit_invocation must be true for suggestion mode")

    evals = yaml.safe_load(texts[ROOT / "evals" / "cases.yaml"])
    cases = evals.get("cases", [])
    if len(cases) < 10:
        fail("evals/cases.yaml must contain at least 10 behavioral cases")
    ids = [case.get("id") for case in cases]
    if any(not case_id for case_id in ids) or len(ids) != len(set(ids)):
        fail("behavioral case ids must be present and unique")
    for case in cases:
        if not case.get("expected") or not case.get("forbidden"):
            fail(f"case {case.get('id')} needs expected and forbidden assertions")

    combined = "\n".join(texts.values())
    placeholders = re.findall(r"\b(?:TODO|TBD|FIXME)\b", combined, re.IGNORECASE)
    if placeholders:
        fail("release files contain unfinished placeholders")

    print(f"OK: validated {len(REQUIRED)} release files and {len(cases)} behavioral cases")


if __name__ == "__main__":
    main()
