# Claude Code Adapter

Claude Code can use the same alignment contract, but its packaging and trigger syntax are host-specific.

## What stays the same

- Clarify before action
- One material question at a time
- Reversible provisional defaults are allowed when they reduce pressure
- Confirm the shared brief before handoff

## What changes

- Use Claude Code's native skill or instruction loader
- Use Claude Code's own trigger syntax or launcher
- Do not assume Codex-style `$align-before-action` support

## Porting note

Reuse the wording from `skills/align-before-action/SKILL.md` as the canonical behavior text, then wrap it in whatever Claude Code expects for skill loading.

