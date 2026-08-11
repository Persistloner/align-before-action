# Harness Porting Notes

`align-before-action` has one shared behavior contract and host-specific packaging.

## Shared contract

- Clarify before action.
- Ask one material question at a time.
- Offer concise options or a reversible provisional default when that helps.
- Confirm the final brief before handoff.
- Let the host decide how auto-discovery and invocation are wired.

## Supported hosts

| Host | Packaging role | Notes |
|---|---|---|
| Codex | Native package | Uses `skills/align-before-action/SKILL.md` and `agents/openai.yaml`. |
| Claude Code | Ported adapter | Reuse the same core contract through Claude Code's skill loader or equivalent instruction mechanism. |
| WorkBuddy | Ported adapter | Reuse the same core contract through WorkBuddy's native skill or prompt loading path. |

## Porting rule

Keep the shared behavior the same. Only the wrapper changes:

- installation location
- trigger syntax
- auto-suggestion behavior
- host-specific metadata

If a host cannot auto-discover the skill, the skill still works as a manually invoked alignment tool.

