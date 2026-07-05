# Publishing Workflow Quality Rubric

This rubric defines quality criteria for evaluating SaaS-style content publishing workflows.

## Evaluation Areas

| Area | Quality Question | Strong Signal |
|---|---|---|
| Workflow integrity | Does the content move through valid states only? | Draft, review and published states are controlled and testable. |
| Validation | Are required fields enforced? | Missing title or body prevents progress. |
| Role-based access | Are restricted actions protected? | Authors cannot publish, editors can publish after review. |
| Safe rendering | Is user-provided content displayed safely? | Script-like input is rendered as text, not executable code. |
| Regression value | Would the tests catch common workflow failures? | Tests cover positive, negative and security-oriented scenarios. |
| Evidence | Can the behaviour be verified automatically? | Playwright tests run in CI and produce repeatable results. |

## QA Interpretation

A publishing workflow is not only a UI journey. It is a business-critical path.

Quality risks include:

- invalid content being published
- users bypassing review
- incorrect role permissions
- missing validation
- unsafe rendering of user-provided content
- regression defects in state transitions

A strong test suite should protect the workflow, the user, the business process and the security boundary.
