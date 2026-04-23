---
skill_id: git-protocol-v2
name: "Atomic Traceability Protocol"
description: "Ensures version control integrity through verified atomic commits and spec-linked history."
version: "2.0.0"
---

# Git & Version Control Protocol

## 1. Commit Standards (Conventional Traceability)
Every commit must follow the pattern: `<type>(<scope>): <subject>`
- **Types**: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`.
- **Scope**: The specific module or feature folder (e.g., `ui`, `auth`, `api`).
- **Body**: Must answer "Why was this necessary?". Reference the specific line in `mission.md` if it fulfills a core objective.
- **Footer**: MUST include `Refs: #[plan_id]` to link the commit to the active implementation plan in `specs/features/`.

## 2. The "Green Gate" Workflow
Never commit "broken" code. Before every commit, the agent must:
1.  **Lint**: Ensure no syntax errors or technical debt was introduced.
2.  **Verify**: Run the `playwright_testing` skill or relevant test suites.
3.  **Snapshot**: Use `/context-snapshot` (from `superpowers.md`) to summarize the delta.

## 3. Branching Strategy
- **Development**: All work happens on feature branches: `feat/[feature-id]-[short-desc]`.
- **Main/Prod**: Stable code only. Merges to `main` require a successful `/verify-implementation` of the entire app.
- **Cleanup**: Delete feature branches immediately after a successful merge to keep the workspace lightweight.

## 4. Orchestration Commands
- **/safe-commit**: Triggers a 3-step sequence: `Lint` -> `Test` -> `Commit`. If any step fails, the commit is aborted, and a `fix` plan is suggested.
- **/sync-milestone**: Commits all current changes, updates `ROADMAP.md` status, and pushes to the remote repository.
- **/atomic-revert**: Analyzes the last commit and performs a clean revert while also updating the relevant `.md` plans to "In Progress" or "Blocked" state.

## 5. Constraints
- **No Mega-Commits**: If a change exceeds 200 lines of code, split it into atomic logical blocks, unless very notable exceptions, where the agent must inform and ask before commiting.
- **Spec Sync**: A commit that changes logic MUST be accompanied by a corresponding update in the `specs/` directory to prevent "Context Drift".
