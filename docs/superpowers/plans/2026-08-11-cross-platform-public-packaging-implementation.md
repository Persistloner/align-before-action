# Cross-Platform Public Packaging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Present `align-before-action` as a public, cross-platform skill pack with one shared behavior contract and clear host-specific packaging notes.

**Architecture:** Keep the Codex skill package as the canonical implementation. Add a small portability layer in docs that explains the shared contract once, then maps that contract to Codex, Claude Code, and WorkBuddy without pretending their packaging is identical.

**Tech Stack:** Markdown, YAML, existing Codex skill package, repository docs.

## Global Constraints

- Preserve the current Codex install path under `skills/align-before-action`.
- Do not claim unsupported automatic installation or discovery behavior for non-Codex hosts.
- Keep the existing behavioral cases and validation script passing.
- Keep the shared alignment contract consistent across all host notes.

---

### Task 1: Add cross-platform harness docs

**Files:**
- Create: `docs/harnesses/README.md`
- Create: `docs/harnesses/codex.md`
- Create: `docs/harnesses/claude-code.md`
- Create: `docs/harnesses/workbuddy.md`

**Interfaces:**
- Consumes: the existing alignment contract in `skills/align-before-action/SKILL.md`
- Produces: host-facing installation notes and a compatibility overview

- [ ] **Step 1: Write the portability docs**

Create a top-level harness guide that explains:
- the shared behavior contract
- how Codex uses the current skill package
- how Claude Code and WorkBuddy should consume the same core contract through their native skill loaders or equivalent instruction mechanisms
- that trigger syntax and auto-discovery may differ by host

Write one short host note per platform with the same common structure: what stays the same, what changes, and how the host should load the shared contract.

- [ ] **Step 2: Check for unsupported promises**

Read the new docs and remove any line that implies identical install mechanics across hosts.

Expected result: the docs promise identical intent and near-identical behavior, not identical packaging.

### Task 2: Update public README files

**Files:**
- Modify: `README.md`
- Modify: `README.zh-CN.md`

**Interfaces:**
- Consumes: `docs/harnesses/README.md`
- Produces: a public-facing explanation of cross-platform support and where to find host-specific notes

- [ ] **Step 1: Add a cross-platform support section**

Add a compact section near the top of both READMEs that says:
- this repo defines one shared alignment contract
- Codex is the packaged native path
- Claude Code and WorkBuddy are supported through host-specific porting notes
- host-specific invocation may differ, but the behavior contract stays the same

- [ ] **Step 2: Link to the harness docs**

Point readers to the new `docs/harnesses/README.md` so they can see the platform split without reading the whole repository.

### Task 3: Validate the release surface

**Files:**
- Modify: none
- Test: `scripts/validate.py`

**Interfaces:**
- Consumes: the updated release files and docs
- Produces: a validated repository state ready for public release

- [ ] **Step 1: Run validation**

Run:
`C:\Users\1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts\validate.py`

Expected result: `OK: validated 7 release files and 39 behavioral cases`

- [ ] **Step 2: Review the diff**

Confirm only the intended documentation files changed and the Codex package remains intact.

