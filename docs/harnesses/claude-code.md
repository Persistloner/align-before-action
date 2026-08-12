# Claude Code Adapter

Claude Code can use the same alignment contract, but its packaging and trigger syntax are host-specific.

## What stays the same

- Clarify before action
- One material question at a time by default, with related questions combined when that reduces user effort
- Reversible provisional defaults are allowed when they reduce pressure
- Confirm the shared brief before handoff
- Route by the capability needed next. If installed skills cannot be enumerated, use ordinary assistant capabilities instead of claiming a named skill is available.

## What changes

- Use Claude Code's native skill or instruction loader
- Use Claude Code's own trigger syntax or launcher
- Do not assume Codex-style `$align-before-action` support

## Porting note

Reuse the wording from `skills/align-before-action/SKILL.md` as the canonical behavior text, then wrap it in whatever Claude Code expects for skill loading.
