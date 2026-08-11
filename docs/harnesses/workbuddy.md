# WorkBuddy Adapter

WorkBuddy can use the same alignment contract, but the repository should treat its packaging as host-specific.

## What stays the same

- The idea of aligning before action
- The one-question-at-a-time interaction style
- The final confirmation gate before execution

## What changes

- WorkBuddy's loader or launcher
- WorkBuddy's trigger phrase or command
- WorkBuddy-specific metadata, if any

## Porting note

Use the core skill text as the behavior source of truth, then wrap it in WorkBuddy's native loading mechanism.

