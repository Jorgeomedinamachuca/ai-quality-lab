# Experiment 001 — Chatbot UI Smoke Test

## Purpose

This experiment validates the basic UI contract of an AI-style chatbot interface using Playwright and Pytest.

The aim is not to test a real LLM yet. Instead, this experiment establishes a controlled demo environment where chatbot interaction patterns can be automated, observed and extended safely.

## Quality Question

How can a Quality Engineer validate the minimum expected behaviour of an AI-style chatbot interface before testing deeper LLM response quality?

## Scope

This experiment covers:

- page loading;
- prompt input visibility;
- send button visibility;
- response panel visibility;
- prompt submission;
- deterministic response rendering;
- empty prompt validation.

## Out of Scope

This experiment does not yet cover:

- real LLM integration;
- semantic accuracy;
- hallucination detection;
- prompt injection;
- model safety;
- response scoring.

Those areas will be addressed in later experiments.

## Test Design

The demo chatbot uses deterministic JavaScript logic. This makes the test repeatable and suitable for CI.

The Playwright tests validate that:

1. The chatbot interface loads successfully.
2. The user can enter and submit a prompt.
3. A controlled response is rendered.
4. Empty prompts trigger a visible validation message.

## Tools

- Python
- Pytest
- Playwright
- HTML/CSS/JavaScript demo page
- GitHub Actions

## QA Value

This experiment demonstrates how UI-level quality gates can be created for AI-powered interfaces before introducing probabilistic LLM behaviour.

It also creates a foundation for future tests involving:

- LLM response quality evaluation;
- hallucination detection;
- prompt injection testing;
- data leakage checks;
- risk-based AI quality gates.

## Evidence

The test suite can be executed locally or through GitHub Actions.

Expected command:

\`\`\`bash
pytest
\`\`\`

Expected outcome:

\`\`\`text
All demo chatbot UI tests pass.
\`\`\`
