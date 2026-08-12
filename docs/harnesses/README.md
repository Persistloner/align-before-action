# Harness Porting Notes

`align-before-action` has one shared behavior contract and host-specific packaging.

## Shared contract

- Clarify before action.
- Advance one material question at a time by default; combine closely related questions when that reduces user effort.
- Offer concise options or a reversible provisional default when that helps.
- Preserve clearly requested bounded conversational actions and allow exploratory hypotheses when the user does not know, while keeping both bounded and provisional.
- Confirm the final brief before handoff.
- Route by the capability needed next; use an available matching skill when exposed, otherwise continue with ordinary assistant capabilities.
- Treat example skills such as `brainstorming`, `grilling`, or `grill-me` as optional integrations, not dependencies.
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

If a host cannot enumerate installed skills, do not claim a downstream skill is available. Offer the equivalent ordinary assistant route and keep the conversation moving.
