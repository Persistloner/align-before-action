# Align Before Action: Behavior Refinement Design

## Purpose

Refine the skill after real and fresh-context testing revealed inconsistent phase transitions. Preserve its lightweight, conversational experience while making stage completion, information status, and early exit behavior observable and testable.

## Evidence

Six independent conversations covered product ideas, an uncertain career decision, an urgent workplace task, a material scope change, an interim note, and non-product writing.

Stable behavior:

- replied in the user's language
- usually asked one answer task per turn
- reduced burden when the user was unsure
- rolled back after a material audience change
- kept an interim note distinct from a final deliverable
- generalized beyond product development

Observed failures:

- local confirmations sometimes replaced the whole-understanding checkpoint
- checkpoint timing varied from premature handoff to prolonged detailed questioning
- solution alternatives and recommendations appeared before original intent was confirmed
- assistant-authored inferences could become implicit product decisions
- urgency produced a hybrid artifact: a detailed plan presented as a final brief
- a fixed three-option limit could omit materially different answer paths

## Goals

1. Make every phase transition depend on an observable user message.
2. Keep understanding separate from improving the idea.
3. Prevent provisional assistant content from silently becoming confirmed.
4. Let users explicitly exit alignment without creating a hybrid discussion/execution state.
5. Cover the meaningful decision space without overloading one turn.

## Non-Goals

- adding a mandatory domain checklist
- forcing a minimum conversation length
- requiring every idea to resolve every open question
- changing manual invocation, language following, or normal safety rules
- expanding the skill into autonomous planning or execution

## State Model

### Understand

The assistant may clarify only the user's existing intent, meaning, context, desired outcome, constraints, and exclusions. It may offer tentative wording or contrasts to help the user express that intent.

The assistant must not introduce solution choices, new capabilities, recommendations, or trade-offs during this state, even as provisional suggestions. A question or recommendation about how a product, artifact, process, or system should behave, be structured, or be delivered is solution content unless the user already introduced it and the assistant is only resolving its meaning. Before any solution content, the assistant must first run the Whole Understanding Checkpoint. Assistance mechanisms may help express existing intent but cannot introduce content from Improve.

### Whole Understanding Checkpoint

This is a mandatory standalone assistant turn before Improve. It contains only the relevant parts of:

- the user's original intent
- confirmed user statements and decisions
- provisional assistant interpretations
- material open, deferred, or skipped items

Its only answer task is to confirm or correct the assistant's understanding. A user's local replies such as "yes," "correct," or "I choose the third option" confirm only the item currently discussed and never satisfy this checkpoint.

The user may confirm an understanding that intentionally leaves non-blocking items open. Completeness means accurate shared understanding, not exhaustive specification.

### Improve

Improve begins only after explicit confirmation of the Whole Understanding Checkpoint. The assistant may then introduce one high-impact suggestion, alternative, assumption, failure condition, or trade-off at a time.

When improvement is complete, the assistant presents the concise final brief and asks for explicit confirmation. The final brief must preserve the status of open, deferred, skipped, or declined items.

### Handoff

After final confirmation:

- confirmation plus a named next action authorizes that action
- confirmation without a named action produces only a handoff question

Before final confirmation, a user may explicitly stop alignment and request a named action. Natural language that clearly combines "stop discussing/asking" with "do this now" counts as an explicit exit; the user need not name the skill. The assistant states the most material unresolved risk once, says it is leaving alignment mode, and hands off to the requested action. It must not disguise a deliverable as a brief or require another confirmation unless safety or platform policy independently requires one.

## Information Status

Every material item has both a source and a status:

- user-stated fact or decision: confirmed only when the user explicitly states or accepts it
- assistant interpretation: provisional until confirmed
- assistant recommendation: suggestion until accepted
- unresolved item: open, deferred, or skipped as directed by the user

Summaries and interim notes must preserve these statuses. Repetition, plausibility, or continued discussion never upgrades an item automatically.

## Option Coverage

Options are an assistance mechanism, not a quota.

Use the smallest set that covers all materially different answer directions. Usually present three to five mutually distinct options. Do not delete a direction merely to satisfy a numeric limit. If more than five important directions exist, group them into higher-level categories and narrow them in a later turn. Always allow the user to answer with uncertainty or an unlisted alternative.

The turn still contains one answer task. Comprehensive coverage means covering choices that would change the next direction, not enumerating every conceivable example.

## Interim Notes

If the user pauses and explicitly requests a record before final confirmation, produce an interim record rather than a final brief. Separate confirmed, provisional, open, deferred, and skipped information. State that alignment and execution are incomplete.

## Response Shape

Normal turns remain lightweight:

1. Give a brief understanding update only when meaning changed.
2. Present one answer task.
3. Add options, tentative wording, or one recommendation only when it reduces user effort.

Checkpoint turns are exceptions only in that they may contain the concise whole understanding or final brief. They still ask for one response: confirm or correct.

## Verification

Add behavioral cases before editing the skill, then re-run the same scenarios after the change:

1. repeated local confirmations do not unlock Improve
2. an assistant-authored product capability remains provisional
3. the first solution-alternative question triggers a prior Whole Understanding Checkpoint
4. urgent "stop asking and give me the plan" exits cleanly instead of creating a hybrid brief
5. four materially distinct options are retained when reducing to three would lose information
6. more than five directions are grouped and narrowed across turns
7. scope changes still roll back correctly
8. interim records still preserve statuses
9. plain final confirmation still produces only the handoff question
10. final confirmation plus a named action still hands off immediately

Run at least five fresh-context repetitions for wording-sensitive transition rules. Keep the existing static validation and official skill validation green.

## Acceptance Criteria

- no test conversation enters Improve without a standalone Whole Understanding Checkpoint and explicit confirmation
- no assistant-authored item appears as confirmed without user acceptance
- phase timing is consistent across product and non-product conversations
- option sets cover materially different directions without a fixed three-option cap
- urgency produces either continued alignment or an explicit exit, never a plan disguised as a brief
- the installed skill and public package remain identical after validation
