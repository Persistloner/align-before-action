# Align Before Action: Public Release Plan

## Goal

Publish a reusable Codex skill that changes the interaction contract from immediate execution to explicit alignment: understand the user's intent, help improve it, confirm the shared brief, and act only after unambiguous authorization.

## Behavioral Changes

1. Preserve the current staged flow and manual invocation policy.
2. Track an internal alignment map so questions follow unresolved dependencies.
3. Separate discoverable facts from user-owned preferences and decisions.
4. Use an assistance ladder when the user cannot answer directly.
5. Improve one high-impact weakness at a time using a small set of review lenses.
6. Distinguish reversible conversational drafts from formal deliverables.
7. Treat `final confirmation + explicit next action` as authorization for that action; ask a handoff question only when no action was specified.
8. Keep each turn lightweight and reply in the user's language.

## Release Artifacts

- English skill metadata and instruction body
- Chinese default prompt plus English invocation example
- English and Simplified Chinese READMEs
- MIT license and third-party inspiration notice
- Behavioral evaluation cases
- Local static validator and GitHub Actions workflow

## Verification

1. Run the official `quick_validate.py` against the packaged skill.
2. Run the repository validator against metadata, encoding, frontmatter, policy, and evaluation cases.
3. Re-run baseline failure cases in fresh contexts, including five confirmation/action repetitions.
4. Run pressure cases for question dependency, assistance escalation, fact ownership, and improvement focus.
5. Synchronize the verified package to the installed skill directory and validate it again.
