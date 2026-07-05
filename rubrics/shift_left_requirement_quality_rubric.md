# Shift-Left Requirement Quality Rubric

This rubric evaluates whether a user story is ready for development, testing and automation.

## Purpose

The purpose of this rubric is to help Quality Engineers identify ambiguity, missing acceptance criteria, security gaps and testability risks before implementation starts.

## Evaluation Areas

| Area | Quality Question | Strong Signal |
|---|---|---|
| Story clarity | Is the story understandable? | Persona, goal and benefit are clearly defined. |
| Acceptance criteria | Is expected behaviour testable? | Criteria use clear Given/When/Then or equivalent structure. |
| Business rules | Are product constraints explicit? | Rules are specific and linked to expected behaviour. |
| Negative scenarios | Are failure paths considered? | Invalid or blocked actions are documented. |
| Edge cases | Are boundary conditions considered? | Whitespace, repeated actions, unusual input and state changes are considered. |
| Security considerations | Are access control and data risks considered? | Permissions, ownership and safe handling are documented. |
| Testability | Can QA validate the story? | Observable outputs, statuses or messages are defined. |
| Risk classification | Is the risk level appropriate? | High-risk stories include security and workflow controls. |

## Shift-Left Quality Gate

A user story should not be considered ready if it lacks:

- clear persona, goal and benefit
- acceptance criteria
- business rules
- negative scenarios
- testability notes
- security considerations for high-risk or critical stories

## QA Interpretation

Shift-left QA means identifying quality risks before implementation.

A strong requirement should help teams answer:

- What behaviour is expected?
- What should be prevented?
- What could go wrong?
- Who is allowed to perform the action?
- What evidence can prove that the feature works?
- What should be automated later?

From a Quality Engineering perspective, requirements are testable artefacts.
