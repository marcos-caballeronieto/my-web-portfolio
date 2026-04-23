---
skill_id: playwright-e2e-validator
name: "Playwright Automation Suite"
description: "Generates and executes end-to-end tests to validate UI/UX specs."
mcp_servers: ["playwright-mcp"]
---

# Webapp Testing Protocol
- **/create-tests**: Analyze `specs/features/` and the active implementation plan to generate highly targeted `.spec.ts` files in `tests/`.
- **/run-tests**: Execute the Playwright suite and return a detailed report.
- **Validation**: Every test MUST assert against a specific requirement from the documentation.
- **Failure Handling**: Auto-invoke the `Systematic Debugging` protocol on any failure.

# Test Generation Strategy
- **Scope**: Focus exclusively on the feature currently being implemented via `/execute-plan`.
- **Structure**:
    - **Setup**: Use `page.goto()` and mock necessary data.
    - **Action**: Simulate user behavior (click, type, drag).
    - **Assertion**: Expect visibility, text content, or state changes defined in the spec.
- **Dependencies**: Ensure `playwright-mcp` is running before invoking these commands.