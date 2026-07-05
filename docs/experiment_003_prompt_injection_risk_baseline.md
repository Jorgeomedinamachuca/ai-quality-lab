# Experiment 003 — Prompt Injection Risk Baseline

## Purpose

This experiment defines a baseline dataset for prompt injection and AI security testing.

The aim is not to test a real LLM yet. Instead, the experiment establishes structured security prompts that can later be used against AI-powered applications, chatbot interfaces or LLM evaluation pipelines.

## Quality Question

How can a Quality Engineer define and validate baseline prompt injection risks before testing a real LLM-powered application?

## Scope

This experiment covers:

- prompt injection test case design
- risk categorisation
- expected safe behaviour
- failure signal definition
- dataset structure validation
- automated Pytest checks

## Out of Scope

This experiment does not yet cover:

- executing prompts against a real LLM
- comparing model responses
- scoring actual assistant outputs
- integrating with an AI API
- testing live production systems

Those areas can be addressed in later experiments.

## Risk Categories

The dataset includes prompts covering:

- instruction override
- secret extraction
- role manipulation
- data leakage
- policy bypass
- jailbreak attempts
- tool misuse
- context exfiltration

## Test Design

The prompt injection dataset is treated as a QA artefact.

The automated tests validate that each prompt includes:

1. a unique ID
2. a known category
3. a valid risk level
4. a clear prompt
5. expected safe behaviour
6. a failure signal

The tests also check that high and critical risk prompts include enough information to support review and future automation.

## QA Value

This experiment demonstrates how AI security testing can be made more structured and repeatable.

Instead of relying on informal adversarial prompts, the dataset defines prompt injection scenarios as test cases with expected behaviour and observable failure signals.

This creates a foundation for future work involving:

- automated prompt execution
- LLM response evaluation
- security-focused quality gates
- refusal quality analysis
- data leakage detection
- prompt injection regression testing

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

All prompt injection dataset tests pass.

## Related Files

- data/security_prompts.json
- rubrics/prompt_injection_risk_rubric.md
- tests/test_prompt_injection_dataset.py
