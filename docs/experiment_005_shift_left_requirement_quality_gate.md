# Experiment 005 — Shift-Left Requirement Quality Gate

## Purpose

This experiment demonstrates how Quality Engineering can shift left by evaluating user stories before implementation starts.

The aim is to identify ambiguity, missing acceptance criteria, weak testability, missing negative scenarios and security gaps early in the delivery lifecycle.

## Quality Question

How can a Quality Engineer identify ambiguity, missing acceptance criteria and testability risks before implementation starts?

## Scope

This experiment covers:

- user story structure
- persona, goal and benefit
- acceptance criteria
- business rules
- edge cases
- negative scenarios
- security considerations
- testability notes
- risk classification
- automated validation using Pytest

## Out of Scope

This experiment does not cover:

- implementation of the user stories
- UI automation
- API automation
- live product validation
- proprietary business rules
- real company requirements

## Test Design

The user story dataset is treated as a QA artefact.

The automated tests validate that each story includes:

1. a unique ID
2. title and description
3. persona, goal and benefit
4. acceptance criteria
5. business rules
6. negative scenarios
7. edge cases
8. security considerations
9. testability notes
10. valid risk level

High and critical risk stories must include security considerations.

## QA Value

This experiment demonstrates that QA can add value before code exists.

It helps prevent defects caused by:

- unclear requirements
- missing acceptance criteria
- untested edge cases
- weak role or permission rules
- missing negative scenarios
- poor observability
- lack of testability

## Shift-Left Interpretation

Shift-left testing is not only about automating earlier.

It is also about asking better quality questions earlier:

- Is this requirement testable?
- What could go wrong?
- What should be prevented?
- What evidence will prove that it works?
- What risks should be discussed before development starts?
- What should an AI coding agent or developer not assume?

## Connection to AI-Assisted Development

This experiment is also relevant to AI coding agents.

Before asking an AI tool or developer to implement a feature, the requirement should be clear, risk-assessed and testable.

A weak requirement can lead to weak implementation, even with a strong coding tool.

## Tools

- Python
- Pytest
- JSON
- Markdown
- GitHub Actions

## Evidence

The test suite can be executed locally or through GitHub Actions.

Expected command:

pytest

Expected outcome:

All shift-left requirement quality tests pass.

## Related Files

- data/user_stories.json
- rubrics/shift_left_requirement_quality_rubric.md
- tests/test_shift_left_requirement_quality.py
