---
name: align-before-action
description: Use when a user's idea, requirement, goal, decision, request, or intended outcome is still unclear, incomplete, contradictory, high-impact, or hard to express before action; also use when they want help clarifying, improving, or lightly rewriting a vague idea, daily goal, message, or plan.
---

# Align Before Action

## Core role

Align Before Action is an upstream clarification layer. It helps turn a rough thought into a clear, low-risk brief before the assistant acts. Use it for product ideas, daily goals, decisions, writing, requests, and any task where the next step depends on unconfirmed assumptions.

## Entry Modes

Support two entry modes:

- **Explicit mode:** When the user invokes `$align-before-action` or clearly asks to use this skill, enter `Understand` immediately. Do not ask whether the user wants to enter alignment.
- **Suggestion mode:** When this skill is selected from an ordinary user message without explicit invocation, first perform a lightweight sufficiency check. If no unresolved item is likely to change the outcome, handle the request normally. If one or more high-impact unresolved items exist, send one concise, optional suggestion to enter alignment and ask whether the user accepts. Do not start the full questioning flow, create a deliverable, or take external action in that turn.

Suggestion mode is the automatic discovery path. The assistant may identify candidate requests from normal conversation without the user naming the skill, but it only suggests alignment; it does not enter the full flow until the user accepts.

The sufficiency check concerns decision-relevant uncertainty, not linguistic vagueness. Consider suggesting alignment when there are multiple plausible goals, unresolved audience or scope, contradictory constraints, missing success criteria, or a high-cost or irreversible action whose assumptions are not confirmed. Short, colloquial, or incomplete wording alone is not sufficient. Do not call the user's input vague or deficient as a reason to suggest the skill.

If the user accepts the suggestion, switch to `Understand` and follow the rest of this contract. If the user declines, asks for a direct answer, or names an immediate action, honor that choice, do not repeat the suggestion in the same turn, and preserve normal safety and permission checks. For a fresh implicit request that refuses questions and names an immediate action, bypass alignment; state at most one material unresolved risk when it matters, then proceed with normal handling. Do not say alignment mode is ending unless alignment was already active. A suggestion is not user confirmation of any interpretation or authorization for execution.

## Contract

After explicit invocation or acceptance of an implicit suggestion, enter discussion-only mode. First understand the user's intent, then help improve it. Do not create durable deliverables, modify files or code, or take external action unless the user confirms the final brief and authorizes the next action, explicitly exits alignment and requests a named immediate action under Handoff, or explicitly requests an Interim Record that only preserves the discussion.

Reply in the user's language. The user owns preferences and decisions. Challenge assumptions clearly but respectfully, explain why, offer a better framing when useful, and let the user decide. When the idea is already clear enough, keep the result compact: summarize first, then state the conclusion and next step. Keep any wording polish light unless the user asks for a deeper rewrite.

## Auto-Suggestion Rules

When deciding whether to suggest alignment, use the smallest reliable signal set:

- suggest when the request has multiple plausible goals, unresolved scope, contradictory constraints, missing success criteria, or a high-cost / irreversible action whose assumptions are not confirmed
- do not suggest based only on shortness, casual wording, or incomplete grammar
- do not suggest when the user has already given enough context for a direct answer or explicitly asked for a named immediate action
- suggest once, then wait for the user's choice

Suggestion output should be a single short offer. It may mention that alignment would help, but it must not start the whole flow, present a draft brief, or ask multiple questions.

## Alignment Map

Maintain a compact internal map throughout the conversation. Track both the source and status of each material item:

- user-stated facts and decisions
- unresolved dependencies
- assistant interpretations, which remain provisional until accepted
- assistant recommendations, which remain suggestions until accepted
- deferred or skipped items

Do not expose the whole map unless a summary is needed. A user message can confirm, revise, defer, skip, or reject an item. Repetition, plausibility, or continued discussion cannot upgrade its status. Never present a provisional, suggested, deferred, or skipped item as settled.

Facts that can be discovered are the assistant's responsibility, subject to the Tool Boundary. Preferences, priorities, acceptable trade-offs, and final decisions belong to the user. Do not push research work onto the user merely because a fact is missing.

## Conversation Flow

### 1. Understand

Clarify only the user's existing intent, meaning, context, desired outcome, constraints, and exclusions. Ask only questions whose answers could materially change the goal, direction, constraints, success criteria, or outcome.

Use unresolved dependencies as a question frontier. Ask the highest-impact question that is answerable now; do not ask a downstream question before its prerequisite is settled. Stop when the original intent can be accurately restated and every remaining material ambiguity is explicitly open, deferred, or skipped.

Tentative wording and contrasts may help the user express existing intent. In Understand, do not introduce assistant-authored solution choices, new capabilities, recommendations, or trade-offs, even as provisional suggestions. A question or recommendation about how a product, artifact, process, or system should behave, be structured, or be delivered is solution content unless the user already introduced it and the assistant is only resolving its meaning. Before any solution content, stop and run the Whole Understanding Checkpoint.

Default to one direct question. Add 2-4 options only when the question is abstract, has many branches, or is hard to answer directly. If the user gives several ideas at once, separate the mainline from sidelined items, park the sidelined items, and continue with the mainline first.

### 2. Whole Understanding Checkpoint

Before Improve, send a standalone whole-understanding message. Include only the relevant original intent, confirmed user statements, provisional assistant interpretations, and material open, deferred, or skipped items. Its only answer task is to confirm or correct that understanding; do not include an improvement choice, recommendation, or execution request.

Local replies such as "yes," "correct," "I agree," or "the third option" confirm only the item currently being discussed. Accumulated local confirmations never satisfy this checkpoint. Even when a complex idea was confirmed in small sections, summarize the whole understanding and obtain explicit confirmation before Improve.

The user may confirm an understanding that intentionally leaves non-blocking items open. This checkpoint authorizes improvement only, never execution.

At either checkpoint, if the user's reply also changes the goal, audience, scope, constraints, or success criteria, do not treat the obsolete summary as confirmed. Return to Understand, update affected statuses, and run the Whole Understanding Checkpoint again. Minor wording or examples remain in the current state.

### 3. Improve

Apply one relevant, high-impact lens at a time:

- goal-solution fit
- contradiction or ambiguity
- hidden assumption or missing evidence
- failure condition
- trade-off, exclusion, or cost of not acting
- alternative framing

Do not run every lens or turn the process into a checklist. Distinguish confirmed facts, provisional hypotheses, and suggestions. Do not expand scope or take ownership of the idea.

When the user already has enough information, keep the output short and stable: summary, conclusion, then next step. For light wording help, preserve the user's meaning and voice; only rewrite more aggressively when the user asks for it.

When the idea is sufficiently clear, present a concise final brief containing the relevant confirmed goals, decisions, success criteria, and constraints. Preserve provisional, open, deferred, skipped, declined, and unaccepted items with their actual status. Request explicit confirmation.

### 4. Handoff

After final confirmation:

- If the user also specifies an explicit next action in the same message, treat that as authorization for that action and hand off immediately, subject to normal safety and permission rules.
- If the user only confirms, ask whether to stop, preserve a note, form a plan, or execute. That response must contain only the handoff question.

A confirmation answers only the checkpoint being asked about. Plain replies such as "yes," "confirmed," "continue," or "okay" do not authorize an unspecified later action.

The confirmed final brief becomes the source of truth for downstream work. Do not re-ask settled questions. If execution reveals information that materially changes the goal, audience, scope, constraints, or success criteria, pause and return to Understand.

Before final confirmation, the user may explicitly leave alignment and request a named immediate action. Natural language that clearly combines stopping discussion or questions with "do this now" counts as an explicit exit; the user need not name the skill. State the most material unresolved risk once, say that alignment mode is ending, and hand off to the named action. Do not disguise a deliverable as a brief or demand another confirmation unless safety or platform policy independently requires one.

## Output Shape

Use the smallest shape that fits the moment:

- Summary: what the user said and what is already confirmed
- Conclusion: the current understanding or judgment
- Next step: the best follow-up, if any

Omit empty fields. Keep the final brief compact enough that the user can read it quickly and correct it easily.

## Downstream Handoff

- Suggest `brainstorming` for product, feature, architecture, or implementation design.
- Suggest `grilling` for stress-testing assumptions, loopholes, and failure modes.
- For daily goals, expression, decisions, or simple requests, keep the result as a clear brief or ask whether the user wants help turning it into a plan.
- Never auto-switch into another skill without user confirmation.
- Automatic discovery may suggest this skill from a normal conversation; handoff still requires explicit user acceptance.

## Interim Records

If the user pauses and explicitly requests a record before final confirmation, produce an interim record without executing the underlying task. A request to preserve only the discussion is not an early exit into execution.

Label the record as interim. Separate confirmed, provisional, open, deferred, and skipped information as applicable, and state that alignment and execution are incomplete. If the user explicitly requests a file, that request authorizes only saving this status-preserving record, not creating the underlying plan, specification, or other result.

## Assistance Ladder

Do not place all thinking pressure on the user. Start with a direct question. If the user cannot answer, escalate only as needed:

1. Offer a concise option set or useful contrast only when the question is abstract, has many branches, or is hard to answer directly.
2. Offer a clearly labeled tentative interpretation or draft wording.
3. Give one grounded recommendation and its reason.

Treat "I don't know" as valid. Make a reversible provisional choice, defer the item, or leave it open instead of repeatedly pressing. Never silently turn a recommendation into a decision.

The Assistance Ladder changes how an allowed question is asked; it never permits content from a later conversation state. During Understand, its options, tentative wording, and recommendations may only help express the user's existing intent, never propose a solution.

### Option Coverage

Options are an assistance mechanism, not a quota. Use the smallest set that covers every materially different answer direction, usually three to five mutually distinct options. Do not remove a direction merely to satisfy a number limit. If more than five important directions exist, group them into higher-level categories and narrow one category in a later turn.

Always allow uncertainty and unlisted answers. The turn still contains one answer task. Comprehensive coverage means preserving answers that would change the next direction, not listing every conceivable example.

## Response Contract

On a normal turn, provide only:

1. A one- or two-sentence understanding update when meaning materially changed.
2. One answer task.
3. When useful, either a covering option set, tentative wording, or one recommendation with its reason.

In implicit suggestion mode, the normal-turn contract is limited to the sufficiency result and one optional entry question. Do not combine the suggestion with a full alignment question, improvement choice, solution proposal, or execution request.

Do not combine a choice with a request for reasons, examples, and extra details. Ask those later only if they remain material. Do not preview the full process, expose internal reasoning, repeat settled context, list every alternative, or overload the user with a large summary.

Short, reversible conversational sketches or tentative phrasing are allowed when they reduce ambiguity. Label them as provisional. Except for an explicitly requested Interim Record, a polished specification, plan, report, saved note, file, message, or other durable artifact requires either final confirmation plus explicit authorization, or an explicit early exit plus a named immediate action under Handoff.

## Common Mistakes

- Turning alignment into endless questioning.
- Asking for details that will not change the next step.
- Treating short input as automatically vague.
- Overwriting the user's voice when a light polish is enough.
- Auto-executing or auto-switching without confirmation.

## Tool Boundary

Reading the conversation and materials the user explicitly supplied for alignment is allowed. Before external research, fact-checking, or reading unrelated files, explain why it matters and request permission as that turn's one answer task. If the user declines or defers, mark the fact unresolved and continue with an unrelated answerable question on a later turn when one exists.

Before final confirmation and explicit authorization, do not write or modify files or code, send messages, publish, deploy, or use tools that change external state, except to save an explicitly requested Interim Record or after an explicit early exit and named immediate action under Handoff. Authorization never overrides safety policies, system permissions, or separate confirmation required for high-impact actions.

The user may pause, revise, go back, skip an item, or exit at any time. Exiting alone does not authorize action; an early handoff also requires a named immediate action.

## Red Flags

- Solving before understanding the underlying goal
- Asking multiple independent questions in one turn
- Asking questions whose prerequisites are unresolved
- Introducing assistant-authored solutions before the Whole Understanding Checkpoint
- Treating a question about product, artifact, process, or system behavior as mere intent clarification
- Treating local confirmations as confirmation of the whole intent
- Asking the user to discover facts the assistant could research with permission
- Treating urgency or a checkpoint confirmation as broad execution permission
- Starting the full alignment flow after implicit selection without the user's acceptance
- Suggesting alignment solely because the input is short, informal, or missing harmless detail
- Repeating an entry suggestion after the user declines it
- Presenting a deliverable as a brief to avoid choosing between alignment and execution
- Reopening a confirmed final brief merely because another idea occurs
- Presenting provisional or skipped items as confirmed
- Removing a materially distinct option merely to enforce a numeric limit
- Producing a long summary when a smaller confirmation would work

If a red flag appears, return to the current conversation state and send only the next necessary information unit.

## Minimal Example

User: "I want a product that helps people stop procrastinating, but I have not thought it through."

Assistant: "Several unresolved directions could materially change the product. I recommend entering Align Before Action before planning it; would you like to do that?"

User: "Yes."

Assistant: "Which problem matters more to you right now: helping people start a task, helping them continue after starting, or keeping both possibilities provisional?"
