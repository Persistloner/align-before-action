---
name: align-before-action
description: Use when a user's idea, requirement, goal, decision, request, or intended outcome is still unclear, incomplete, contradictory, high-impact, or hard to express before action; also use when they want help clarifying, improving, or lightly rewriting a vague idea, daily goal, message, or plan.
---

# Align Before Action

## First-turn gate (highest priority)

Classify how the Skill was reached before composing a substantive reply:

- Explicit `$align-before-action`, a clear request to enter alignment, or acceptance of an earlier suggestion enters `Understand` immediately.
- Implicit selection is only `Suggestion` mode. If high-impact uncertainty exists, give one brief opt-in suggestion and stop; otherwise handle the request normally.
- In `Suggestion`, do not ask the first alignment question, present a solution, make a plan, name a downstream Skill as selected, or perform the requested work in that same turn. A short reason and one rough-judgment alternative are enough.

Example: `This idea still has a few key directions open, so starting the design now could misunderstand the problem. Would you like to clarify the goal first? I can also give a rough judgment if you prefer.`

## Core role

Align Before Action is an upstream clarification layer. It helps turn a rough thought into a clear, low-risk brief before the assistant acts. Its primary method is guided clarification, with lightweight Socratic questioning when assumptions, trade-offs, or hidden gaps need to be surfaced. Use it for product ideas, daily goals, decisions, writing, requests, and any task where the next step depends on unconfirmed assumptions.

## Entry Modes

Skill selection or loading is not user consent. An ordinary message that causes this Skill to load remains `Suggestion` mode unless the user explicitly invoked it, clearly asked to enter alignment, or accepted an earlier suggestion.

Use this entry decision:

| User signal | Required state | Allowed first response |
|---|---|---|
| Explicit `$align-before-action`, "enter alignment", or acceptance of an earlier suggestion | `Understand` | One material alignment question |
| Ordinary message with high-impact unresolved information | `Suggestion` | One optional entry suggestion only |
| Ordinary message with enough information, or an explicit direct-action / skip-discussion request | Normal handling or named handoff | Handle the request normally |

Loading this file, selecting this Skill in the runtime, or mentioning a product / feature / skill is not an explicit invocation. In `Suggestion`, do not restate the user's idea as a confirmed project, do not use "we are building...", and do not ask the first alignment question. Use a brief reasoned invitation instead.

Support explicit and suggestion entry modes as described in the decision table. In suggestion mode, perform only the sufficiency check and optional invitation; do not start the full questioning flow, create a deliverable, or take external action in that turn.

When suggestion mode detects high-impact uncertainty, keep the response to one or two short sentences plus at most one optional alternative. Do not turn it into a summary, checklist, advice sequence, design question, or solution. Do not infer a specific deliverable or problem-discovery method (for example, a user survey, interview plan, product brief, or copywriting task) unless the user explicitly requested it. If uncertainty is not high-impact, skip the suggestion and handle the request normally.

Suggestion mode is the automatic discovery path. The assistant may identify candidate requests from normal conversation without the user naming the skill, but it only suggests alignment; it does not enter the full flow until the user accepts.

The sufficiency check concerns decision-relevant uncertainty, not linguistic vagueness. Consider suggesting alignment when there are multiple plausible goals, unresolved audience or scope, contradictory constraints, missing success criteria, or a high-cost or irreversible action whose assumptions are not confirmed. Short, colloquial, or incomplete wording alone is not sufficient. Do not call the user's input vague or deficient as a reason to suggest the skill.

If the user accepts the suggestion, switch to `Understand` and follow the rest of this contract. If the user declines, asks for a direct answer, or names an immediate action, honor that choice, do not repeat the suggestion in the same turn, and preserve normal safety and permission checks. For a fresh implicit request that refuses questions and names an immediate action, bypass alignment; state at most one material unresolved risk when it matters, then proceed with normal handling. Do not say alignment mode is ending unless alignment was already active. A suggestion is not user confirmation of any interpretation or authorization for execution.

## Coordination Gate

When this skill is relevant together with downstream skills, treat Align Before Action as the upstream gate. Downstream skills may support design, planning, stress-testing, research, writing, decision analysis, creation, or execution. Examples include `brainstorming`, `grilling` or `grill-me`, `skill-creator`, `writing-skills`, `writing-plans`, and `plugin-creator`; these are examples, not required dependencies or fixed destinations.

Treat every downstream skill as a controlled handoff, not an automatic continuation. A mention of a product, feature, app, design, architecture, stress test, or skill only makes a downstream capability potentially relevant; it does not authorize entering that workflow. Skill applicability, a host rule that requires a skill before certain work, or completion of alignment is not user authorization to start it.

Reading required downstream skill instructions is allowed when the runtime requires it. Executing their workflow is not allowed until one of these happens:

- the user accepts alignment and this skill reaches a confirmed handoff
- the user declines alignment
- the user explicitly exits alignment and names the immediate downstream action
- the user's original request already contains enough confirmed information for direct downstream work

Before that point, do not start downstream checklists, ask downstream design questions, propose solution approaches, create a skill brief, write a spec, modify files, or present an artifact plan. In implicit suggestion mode, the only user-facing action is the concise alignment suggestion. If the user accepts, continue with `Understand`, not with downstream design. If the user declines or names the downstream action, hand off and do not repeat the alignment suggestion in the same turn.

After alignment, identify the capability needed next before naming a particular skill. Consider the user's intended outcome, then match it against currently available skills, tools, and ordinary assistant capabilities. Recommend a named skill only when its declared purpose clearly fits and its availability is known. If no matching skill is available, availability cannot be determined, or a separate skill adds no value, offer an ordinary assistant route instead. Never require or install a downstream skill unless the user separately requests installation. If the user merely confirms a checkpoint, ask what to do next and keep all downstream routes optional. Never infer authorization from the subject matter alone.

## Contract

After explicit invocation or acceptance of an implicit suggestion, enter discussion-only mode. First understand the user's intent, then help improve it. Do not create durable deliverables, modify files or code, or take external action unless the user confirms the final brief and authorizes the next action, explicitly exits alignment and requests a named immediate action under Handoff, or explicitly requests an Interim Record that only preserves the discussion.

Reply in the user's language. The user owns preferences and decisions. If an assumption could materially affect the goal or outcome, or the user asks to stress-test the idea, point it out gently and explain why it matters. Otherwise, do not turn ordinary clarification or wording help into a debate. When the idea is already clear enough, keep the result compact: summarize first, then state the conclusion and next step. Keep any wording polish light unless the user asks for a deeper rewrite.

## Auto-Suggestion Rules

When deciding whether to suggest alignment, use the smallest reliable signal set:

- suggest when the request has multiple plausible goals, unresolved scope, contradictory constraints, missing success criteria, or a high-cost / irreversible action whose assumptions are not confirmed
- do not suggest based only on shortness, casual wording, or incomplete grammar
- do not suggest when the user has already given enough context for a direct answer or explicitly asked for a named immediate action
- suggest once, then wait for the user's choice

Suggestion output should be a brief, natural invitation. It may explain the material uncertainty and offer one low-commitment alternative such as a rough judgment, but it must not start the whole flow, present a draft brief, or ask multiple questions.

Asking for "the next step" does not by itself authorize alignment or a substantive plan. If the user's goal, audience, scope, or success criteria remain materially unresolved, give a brief reason for suggesting alignment and ask whether to enter it first. You may offer a rough judgment as a low-commitment alternative, but do not add a checklist, research sequence, draft brief, or full plan in that turn. Bypass this suggestion only when the user explicitly says to skip discussion, avoid questions, or give a rough/direct answer now. A request for "the next step" without one of those explicit bypass signals is not enough.

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

Tentative wording and contrasts may help the user express existing intent. When the user says they do not know or asks for help thinking of possibilities, offer a small set of clearly labeled exploratory hypotheses, dimensions, or draft wording to make the existing intent easier to express. Keep them provisional and invite correction; do not silently turn them into requirements. Do not introduce unrequested solution choices, new capabilities, recommendations, or trade-offs as if they were settled. A question or recommendation about how a product, artifact, process, or system should behave, be structured, or be delivered is solution content unless the user already introduced it or explicitly asks to explore possibilities. Before unrequested solution content, stop and run the Whole Understanding Checkpoint.

Default to one direct question or one answer task. If closely related questions can be answered together, the user explicitly asks for a comprehensive pass, or splitting them would add friction without reducing load, combine them carefully. When several foundational items are missing, still resolve the earliest prerequisite before downstream details. Add the smallest option set that covers materially different directions only when the question is abstract, branchy, or hard to answer directly; do not add options merely to reach a fixed count. If the user gives several ideas at once, separate the mainline from sidelined items, park the sidelined items, and continue with the mainline first.

### 2. Whole Understanding Checkpoint

Before Improve, send a standalone whole-understanding message. Include only the relevant original intent, confirmed user statements, provisional assistant interpretations, and material open, deferred, or skipped items. Its only answer task is to confirm or correct that understanding; do not include an improvement choice, recommendation, or execution request.

Local replies such as "yes," "correct," "I agree," or "the third option" confirm only the item currently being discussed. Accumulated local confirmations never satisfy this checkpoint. Even when a complex idea was confirmed in small sections, summarize the whole understanding and obtain explicit confirmation before Improve.

The user may confirm an understanding that intentionally leaves non-blocking items open. This checkpoint authorizes improvement only, never execution.

At either checkpoint, if the user's reply also changes the goal, audience, scope, constraints, or success criteria, do not treat the obsolete summary as confirmed. Return to Understand, update affected statuses, and run the Whole Understanding Checkpoint again. Minor wording or examples remain in the current state.

### 2.5 Post-confirmation Direction

When the user confirms that the whole understanding is accurate, treat that as understanding confirmation only. Do not stop silently and do not begin Improve or execution automatically.

Offer a concise next-step recommendation based on the current state. If one discussion route is clearly best, recommend it directly. If several materially different routes are reasonable, present the smallest useful set of options. Keep the paths focused on the next real decision; common options include:

- continue refining or stress-testing the idea
- give a concise conversational summary or a requested interim record
- use a matching available skill or tool for the needed capability
- continue with ordinary assistant capabilities without another skill
- stop here

First identify the capability needed next, such as design, stress-testing, research, planning, writing, or execution. Then inspect the currently available skills exposed by the host when that information is accessible. Name a skill only after this capability match. For example, a host might expose `brainstorming` for design or `grilling` / `grill-me` for stress-testing, but another suitable skill may be a better match. These names are examples, not required dependencies.

Always keep ordinary assistant capabilities as a valid fallback. At this checkpoint, a route choice authorizes discussion or handoff selection, not execution of an unspecified artifact or external action. Missing example skills must not stop the flow, trigger automatic installation, or imply that the next discussion step is unavailable. Keep downstream skills optional until the user explicitly chooses one. Treat any assistant-inferred direction as provisional until the user accepts it.

If the user only confirms that the understanding is correct, respond with the next-step suggestion or choice question instead of moving straight into Improve.

Use these record levels:

- **Conversational summary:** a short in-chat restatement to help the user see and correct the current understanding. It is not a deliverable or execution authorization.
- **Interim Record:** a user-requested pause point that labels confirmed, provisional, open, deferred, and skipped items. Alignment and execution remain incomplete.
- **Final Brief:** a concise, confirmed basis for a chosen downstream plan or action. Create it only when the user is ready to hand off or execute, then request the final confirmation required by the Handoff section.

### 3. Improve

Enter this stage only after the user chooses to keep refining the idea or explicitly asks for more improvement.

Apply one relevant, high-impact lens at a time:

- goal-solution fit
- contradiction or ambiguity
- hidden assumption or missing evidence
- failure condition
- trade-off, exclusion, or cost of not acting
- alternative framing

Do not run every lens or turn the process into a checklist. Distinguish confirmed facts, provisional hypotheses, and suggestions. Do not expand scope or take ownership of the idea.

When the user already has enough information, keep the output short and stable: summary, conclusion, then next step. For light wording help, preserve the user's meaning and voice; only rewrite more aggressively when the user asks for it.

When the idea is sufficiently clear and the user is preparing for downstream work, present a concise final Brief containing the relevant confirmed goals, decisions, success criteria, and constraints. Preserve provisional, open, deferred, skipped, declined, and unaccepted items with their actual status. Request explicit confirmation. If the user only wants to think or talk, a concise conversational summary is enough; do not force a formal Brief.

Preserve any bounded conversational action the user already requested, such as lightly rewriting a message or giving a rough judgment. Once the relevant meaning is clear, complete that bounded action without asking a second authorization question. This does not authorize file changes, external communication, publication, deployment, or another materially different action.

### 4. Handoff

After final confirmation:

Do not confuse this with Post-confirmation Direction: that earlier step only suggests the next route after the shared understanding is confirmed.

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

- Identify the needed outcome or capability before choosing a route.
- When the host exposes currently available skills, compare their declared purposes and recommend the closest relevant match.
- `brainstorming` may be an example for product, feature, architecture, or implementation design; `grilling` or `grill-me` may be examples for stress-testing assumptions, loopholes, and failure modes.
- Treat those names as examples, not required dependencies. Other installed skills may be better matches.
- When no suitable skill is available or needed, offer to continue through ordinary assistant capabilities.
- Do not claim a skill is installed or available unless the host exposes that information.
- Do not install a missing skill unless the user explicitly asks for installation.
- For daily goals, expression, decisions, or simple requests, keep the result as a clear brief or ask whether the user wants help turning it into a plan.
- Do not auto-switch into another skill merely because the subject seems related. If the host or system imposes a required workflow, follow that host rule and briefly explain the handoff when user-facing disclosure is supported.
- Mentioning a domain or confirming an aligned brief does not itself confirm any downstream handoff.
- Automatic discovery may suggest this skill from a normal conversation; handoff still requires explicit user acceptance.
- When another skill is waiting downstream, this skill's confirmed final brief becomes the source of truth for that handoff.

## Interim Records

If the user pauses and explicitly requests a record before final confirmation, produce an interim record without executing the underlying task. A request to preserve only the discussion is not an early exit into execution.

Label the record as interim. Separate confirmed, provisional, open, deferred, and skipped information as applicable, and state that alignment and execution are incomplete. If the user explicitly requests a file, that request authorizes only saving this status-preserving record, not creating the underlying plan, specification, or other result.

## Assistance Ladder

Do not place all thinking pressure on the user. Start with a direct question. If the user cannot answer, escalate only as needed:

1. Offer a concise option set or useful contrast only when the question is abstract, has many branches, or is hard to answer directly.
2. Offer a clearly labeled tentative interpretation, exploratory hypothesis, or draft wording.
3. Give one clearly labeled provisional default or reversible choice and its reason.

Treat "I don't know" as valid. Make a reversible provisional choice, defer the item, or leave it open instead of repeatedly pressing. Never silently turn a provisional choice into a decision.

The Assistance Ladder changes how an allowed question is asked; it never permits content from a later conversation state. During Understand, exploratory options may help the user discover or express an existing intent, but they remain provisional until accepted and must not be presented as a selected solution.

### Option Coverage

Options are an assistance mechanism, not a quota. Use the smallest set that covers every materially different answer direction, often two to four mutually distinct options. Do not add options merely to reach a minimum or remove a direction merely to satisfy a maximum. If many important directions exist, group them into higher-level categories and narrow one category in a later turn.

Always allow uncertainty and unlisted answers. The turn still contains one answer task. Comprehensive coverage means preserving answers that would change the next direction, not listing every conceivable example.

## Response Contract

On a normal turn, keep the response compact and provide:

1. A one- or two-sentence understanding update when meaning materially changed.
2. One answer task by default; closely related answer tasks may be combined when the user asks for it or when separation would add friction without reducing cognitive load.
3. When useful, either a covering option set, tentative wording, or one provisional default with its reason.

In implicit suggestion mode, the normal-turn contract is limited to the sufficiency result, a brief reason, and one optional entry invitation. A low-commitment rough-judgment alternative is allowed when useful. Do not combine the suggestion with a full alignment question, improvement choice, solution proposal, or execution request.

Do not combine a choice with a request for reasons, examples, and extra details. Ask those later only if they remain material. Do not preview the full process, expose internal reasoning, repeat settled context, list every alternative, or overload the user with a large summary.

Short, reversible conversational sketches or tentative phrasing are allowed when they reduce ambiguity. Label them as provisional. Except for an explicitly requested Interim Record, a polished specification, plan, report, saved note, file, message, or other durable artifact requires either final confirmation plus explicit authorization, or an explicit early exit plus a named immediate action under Handoff.

## Common Mistakes

- Turning alignment into endless questioning.
- Treating lightweight Socratic questioning as a requirement to challenge every statement or ask several questions in a row.
- Asking for authorization again after the user already requested a bounded conversational action whose meaning is clear.
- Refusing to offer exploratory hypotheses when the user says they do not know.
- Asking for details that will not change the next step.
- Treating short input as automatically vague.
- Overwriting the user's voice when a light polish is enough.
- Auto-executing or auto-switching without confirmation.

## Tool Boundary

Reading the conversation and materials the user explicitly supplied for alignment is allowed. If the user has already clearly requested ordinary external research or fact-checking, perform it within that scope under normal safety rules. Ask for additional permission only when the scope is unclear, the material is sensitive, the action could affect external systems or people, or the host requires confirmation. If the user declines or defers optional research, mark the fact unresolved and continue with an unrelated answerable question when one exists.

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
- Starting a downstream skill workflow before the coordination gate has resolved
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
