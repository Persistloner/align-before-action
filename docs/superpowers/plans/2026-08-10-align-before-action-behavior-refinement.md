# Align Before Action Behavior Refinement Implementation Plan

> Status: Superseded. Later revisions added implicit suggestion mode, broader handoff wording, and the current published README/skill behavior.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make phase transitions, information status, early exit, and option coverage consistent without increasing normal-turn information load.

**Architecture:** Keep the skill self-contained. Encode observable state-transition conditions in `SKILL.md`, record the new failures as declarative behavioral cases, and update user-facing documentation to match. Validate static structure locally, then forward-test the packaged skill in fresh contexts before synchronizing it to the installed directory.

**Tech Stack:** Markdown, YAML, Python 3 with PyYAML, Codex skill validator, fresh-context agent conversations.

## Global Constraints

- Keep manual invocation and `policy.allow_implicit_invocation: false` unchanged.
- Keep the Chinese default prompt and reply-in-user-language behavior unchanged.
- Do not add a mandatory domain checklist or minimum conversation length.
- Normal turns contain one answer task and remain concise.
- Do not synchronize the installed skill until the packaged version passes static and behavioral validation.
- The project is not currently a Git repository, so this plan contains no commit steps.

---

### Task 1: Encode the Observed Failures

**Files:**
- Modify: `evals/cases.yaml`

**Interfaces:**
- Consumes: behavior requirements from `docs/superpowers/specs/2026-08-10-align-before-action-behavior-refinement-design.md`
- Produces: declarative cases consumed by reviewers and `scripts/validate.py`

- [x] **Step 1: Add failing behavioral cases before editing the skill**

Add cases for: mandatory whole-understanding checkpoint, local confirmation isolation, solution-boundary detection, provisional inference preservation, semantic early exit, four-direction option coverage, and grouping when more than five directions exist.

- [x] **Step 2: Verify each case reproduces an observed current-version failure**

Use the existing raw transcripts from the six fresh-context conversations. Confirm that current behavior violated the expected or forbidden assertion for each new failure case.

### Task 2: Implement Observable State Transitions

**Files:**
- Modify: `skills/align-before-action/SKILL.md`

**Interfaces:**
- Consumes: the new behavioral cases in `evals/cases.yaml`
- Produces: the complete runtime instruction contract for `align-before-action`

- [x] **Step 1: Replace the ambiguous Understand exit with a standalone checkpoint**

Require a standalone whole-understanding message whose only answer task is confirm or correct. State that local confirmations never unlock Improve.

- [x] **Step 2: Add the observable Understand/Improve boundary**

Classify assistant-authored solution alternatives, new capabilities, recommendations, and trade-offs as Improve content. Require the whole-understanding checkpoint before asking such questions.

- [x] **Step 3: Add status promotion rules**

Keep assistant interpretations provisional and recommendations suggested until explicit user acceptance. Prevent summaries from silently upgrading them.

- [x] **Step 4: Resolve early-exit behavior**

Treat natural language that clearly combines stopping alignment with a named immediate action as an explicit exit. State one material unresolved risk, leave alignment mode, and hand off without producing a hybrid brief.

- [x] **Step 5: Replace the fixed option cap**

Use the smallest set covering materially distinct directions, usually three to five. Group and narrow when more than five directions exist, while allowing uncertainty and unlisted answers.

- [x] **Step 6: Preserve the response-load contract**

Keep one answer task per normal turn and concise checkpoint summaries. Remove or rewrite any old rule that conflicts with adaptive option coverage.

### Task 3: Update Public Documentation

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`

**Interfaces:**
- Consumes: final behavior in `skills/align-before-action/SKILL.md`
- Produces: accurate public explanation in English and Simplified Chinese

- [x] **Step 1: Document the mandatory whole-understanding checkpoint**

Explain that local answers do not replace whole-intent confirmation.

- [x] **Step 2: Document adaptive option coverage**

Replace wording that implies a fixed option cap with three-to-five typical coverage and hierarchical narrowing.

- [x] **Step 3: Document semantic early exit**

Explain that a user may explicitly stop alignment and request a named action, subject to unresolved-risk disclosure and normal safety rules.

### Task 4: Verify and Deploy

**Files:**
- Verify: `skills/align-before-action/SKILL.md`
- Verify: `skills/align-before-action/agents/openai.yaml`
- Verify: `evals/cases.yaml`
- Verify: `README.md`
- Verify: `README.zh-CN.md`
- Synchronize after validation: `C:\Users\1\.codex\skills\align-before-action\SKILL.md`

**Interfaces:**
- Consumes: packaged release files
- Produces: validated packaged and installed copies with identical hashes

- [x] **Step 1: Run repository validation**

Run `python scripts/validate.py`. Expected: exit code 0 and all release files plus behavioral cases validated.

- [x] **Step 2: Run the official skill validator**

Run Codex `quick_validate.py skills/align-before-action`. Expected: `Skill is valid!`.

- [x] **Step 3: Run fresh-context behavioral tests**

Repeat the local-confirmation, solution-boundary, inference-status, urgent-exit, four-option, grouping, interim-note, scope-change, plain-confirmation, and confirmation-plus-action scenarios. Use at least five repetitions for the whole-understanding transition wording.

- [x] **Step 4: Synchronize the verified package**

Copy only `SKILL.md` and `agents/openai.yaml` to the installed skill directory after all prior checks pass.

- [x] **Step 5: Verify installed equality and validity**

Compare SHA-256 hashes for packaged and installed files, then run the official validator against the installed directory. Expected: matching hashes and `Skill is valid!`.
