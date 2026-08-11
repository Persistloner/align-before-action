# Implicit Alignment Suggestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an opt-in-by-confirmation suggestion entry to `align-before-action` while preserving direct explicit invocation and the existing alignment and handoff contract.

**Architecture:** Allow implicit skill selection, but distinguish an implicit suggestion mode from an explicit full-alignment mode in `SKILL.md`. The implicit mode evaluates only decision-relevant uncertainty and emits one concise opt-in question; it never starts the full questioning flow or takes action. Extend declarative behavioral coverage and bilingual documentation, then synchronize only validated runtime files to the installed skill.

**Tech Stack:** Markdown, YAML, Python 3 with PyYAML, Codex skill validator.

## Global Constraints

- Explicit `$align-before-action` invocation enters `Understand` immediately.
- Implicit handling may only suggest alignment when high-impact unresolved information is present.
- A suggestion is one concise answer task and is never repeated after decline in the same turn.
- Decision-relevant uncertainty, not shortness or informal wording, determines suggestion eligibility.
- Existing whole-understanding, improvement, status, early-exit, tool-boundary, and safety rules remain unchanged after entry.
- No durable deliverable or external state change occurs in suggestion mode.
- Keep Chinese as the default prompt language and reply in the user's language.

---

### Task 1: Add failing behavioral cases

**Files:**
- Modify: `evals/cases.yaml`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-08-10-implicit-alignment-suggestion-design.md`
- Produces: observable cases for implicit suggestion behavior and regression coverage for explicit invocation

- [ ] **Step 1: Replace the old manual-only entry expectation**

Change the entry case so a natural, materially under-specified idea expects one concise alignment suggestion, while forbidding immediate full alignment or execution.

- [ ] **Step 2: Add implicit sufficiency and acceptance cases**

Add cases for sufficient input with no suggestion, acceptance entering `Understand`, decline without repetition, explicit invocation bypassing the suggestion, and explicit named action or urgency remaining unblocked.

- [ ] **Step 3: Add wording-boundary cases**

Add cases forbidding the assistant from calling an input vague solely because it is short or colloquial, and requiring a decision-relevant unresolved reason when a suggestion is made.

- [ ] **Step 4: Run the cases against the current skill behavior**

Use fresh contexts or independent manual transcripts to confirm the new implicit cases fail against the current manual-only version before editing `SKILL.md` or metadata.

### Task 2: Implement dual entry modes

**Files:**
- Modify: `skills/align-before-action/SKILL.md`
- Modify: `skills/align-before-action/agents/openai.yaml`
- Modify: `scripts/validate.py`

**Interfaces:**
- Consumes: the new entry cases and design invariants
- Produces: explicit full mode and implicit suggestion mode with a stable handoff into the existing flow

- [ ] **Step 1: Enable implicit selection in metadata**

Set `policy.allow_implicit_invocation` to `true` and update the frontmatter description to describe natural triggers without summarizing the workflow.

- [ ] **Step 2: Add the two-mode entry contract**

State that explicit invocation enters `Understand` immediately; implicit selection performs only the sufficiency check and either continues normally or asks one opt-in question.

- [ ] **Step 3: Define the sufficiency predicate**

Use multiple plausible goals, unresolved audience or scope, contradictory constraints, missing success criteria, or high-cost/irreversible actions as signals. Exclude shortness, colloquial style, and harmless missing detail by themselves.

- [ ] **Step 4: Define decline, direct-action, and repetition behavior**

Honor a decline or named action, do not repeat the suggestion in the same turn, and preserve normal safety and permission checks.

- [ ] **Step 5: Re-read existing flow rules for conflicts**

Ensure suggestion mode cannot create artifacts, expose internal state, ask the full sequence prematurely, or bypass whole-understanding and final confirmation once the user opts in.

### Task 3: Update public documentation

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`

**Interfaces:**
- Consumes: final dual-mode behavior in `SKILL.md`
- Produces: accurate usage guidance in English and Simplified Chinese

- [ ] **Step 1: Explain explicit and suggestion entry modes**

Describe that users can invoke the skill directly, while ordinary requests may receive a short opt-in suggestion when important decisions remain unresolved.

- [ ] **Step 2: Add examples for suggested entry and direct handling**

Include one under-specified idea that receives a suggestion and one sufficiently specified request that proceeds normally.

- [ ] **Step 3: State the non-blocking behavior**

Document that declining the suggestion leaves the user free to continue normally and that the skill does not label users or their ideas as vague.

### Task 4: Verify and deploy

**Files:**
- Verify: `skills/align-before-action/SKILL.md`
- Verify: `skills/align-before-action/agents/openai.yaml`
- Verify: `evals/cases.yaml`
- Verify: `README.md`
- Verify: `README.zh-CN.md`
- Synchronize after validation: `C:\Users\1\.codex\skills\align-before-action\SKILL.md`
- Synchronize after validation: `C:\Users\1\.codex\skills\align-before-action\agents\openai.yaml`

**Interfaces:**
- Consumes: packaged release files
- Produces: validated packaged and installed copies with identical runtime file hashes

- [ ] **Step 1: Run repository validation**

Run `python scripts/validate.py` with the bundled Python and temporary PyYAML dependency. Expect all release files and behavioral cases to validate.

- [ ] **Step 2: Run the official skill validator**

Run Codex `quick_validate.py` against the packaged skill. Expect `Skill is valid!`.

- [ ] **Step 3: Run fresh-context behavioral checks**

Check implicit ambiguous, implicit sufficient, acceptance, decline, explicit invocation, urgency, and wording-boundary scenarios, plus existing whole-understanding and handoff regressions.

- [ ] **Step 4: Synchronize the verified runtime files**

Copy only `SKILL.md` and `agents/openai.yaml` to the installed directory after all checks pass.

- [ ] **Step 5: Verify installed equality and validity**

Compare SHA-256 hashes for both runtime files and run the official validator against the installed directory.
