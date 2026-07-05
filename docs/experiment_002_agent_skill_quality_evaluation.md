# Experiment 002 — Agent Skill Quality Evaluation

## Purpose

This experiment explores how a Quality Engineer can evaluate reusable AI agent skills, including Claude-style skills, as testable quality artefacts.

The aim is to assess whether a skill is clear, safe, reusable and suitable for structured AI-assisted QA workflows.

## Quality Question

How can a Quality Engineer evaluate whether an AI agent skill is clear, safe, reusable and testable?

## Scope

This experiment covers:

- skill folder structure
- presence of SKILL.md
- clear purpose definition
- expected input definition
- expected output definition
- safety and reliability boundaries
- example input and output files
- automated structural validation using Pytest

## Out of Scope

This experiment does not yet cover:

- executing the skill inside Claude
- comparing outputs across different LLMs
- measuring semantic quality of generated test cases
- testing against real product requirements
- adversarial prompt injection against the skill

Those areas can be added in later experiments.

## Test Design

The experiment treats the agent skill as a quality artefact.

The automated tests check that the skill includes:

1. a SKILL.md file
2. expected instruction sections
3. an examples folder
4. sample input
5. expected output
6. safety and reliability rules

## Tools

- Python
- Pytest
- Markdown
- GitHub Actions
- Claude-style skill structure

## QA Value

This experiment demonstrates that AI agent skills can be reviewed, versioned and tested like other software quality artefacts.

It also shows how a QA professional can apply structured evaluation to AI-assisted workflows before using them in production or delivery contexts.

## Evidence

The test suite can be executed locally or through GitHub Actions.

Expected command:

pytest

Expected outcome:

All agent skill structure tests pass.

## Related Files

- skills/qa-test-case-generator/SKILL.md
- skills/qa-test-case-generator/examples/sample_user_story.md
- skills/qa-test-case-generator/examples/expected_test_cases.md
- rubrics/agent_skill_quality_rubric.md
- tests/test_agent_skill_structure.py
