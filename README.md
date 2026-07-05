# AI Quality Lab

[![AI Quality Lab Tests](https://github.com/Jorgeomedinamachuca/ai-quality-lab/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/Jorgeomedinamachuca/ai-quality-lab/actions/workflows/playwright-tests.yml)

AI Quality Lab is a personal learning and research laboratory focused on the future of Quality Engineering in the age of Artificial Intelligence.

The project explores how modern QA practices can evolve for AI-powered applications through practical experiments with Playwright, Python, Pytest, GitHub Actions, LLM evaluation rubrics, Agent Skills, prompt injection testing and risk-based quality gates.

This repository is not intended to demonstrate software development expertise as its primary goal. Its purpose is to build practical, evidence-based experience in AI Quality Engineering through experimentation, automation, documentation and systematic evaluation of intelligent systems.

---

## Vision

AI Quality Lab investigates how Quality Engineering can evolve when software products become increasingly probabilistic, conversational and AI-assisted.

Traditional test automation remains essential, but AI-powered systems introduce new quality risks:

- non-deterministic responses;
- hallucinated or unsupported claims;
- prompt injection vulnerabilities;
- data leakage risk;
- inconsistent behaviour across repeated runs;
- unclear acceptance criteria for response quality;
- difficulty converting qualitative behaviour into measurable release signals.

This lab is designed to explore those risks from a practical QA perspective.

---

## Lab Areas

AI Quality Lab is organised around several practical research areas:

| Area | Purpose |
|---|---|
| Playwright Automation | UI automation for AI-style applications, chatbot interfaces and SaaS workflows. |
| Pytest Framework | Test structure, assertions, fixtures and repeatable automation. |
| AI Evaluation | Evaluation of LLM-style responses, consistency, hallucination risks and response quality. |
| Security Testing | Prompt injection, data leakage and unsafe instruction handling. |
| Test Rubrics | Structured quality criteria for evaluating AI outputs, requirements and agent behaviour. |
| Claude Skills / Agent Skills | Experiments with reusable agent skills, including structure, clarity, safety and testability. |
| Shift-Left Quality | Requirement quality gates before implementation starts. |
| GitHub Actions | Continuous integration for automated test execution and quality evidence. |

---

## Current Experiments

| Experiment | Focus | Status |
|---|---|---|
| Experiment 001 — Chatbot UI Smoke Test | Playwright automation for a controlled AI-style chatbot interface. | Active |
| Experiment 002 — Agent Skill Quality Evaluation | QA evaluation of Claude-style reusable agent skills. | Active |
| Experiment 003 — Prompt Injection Risk Baseline | Structured AI security testing dataset for prompt injection risks. | Active |
| Experiment 004 — Secure Publishing Workflow | SaaS-style workflow validation using Playwright and Page Object Model. | Active |
| Experiment 005 — Shift-Left Requirement Quality Gate | Requirement quality, testability and risk validation before implementation. | Active |

---

## Experiment 001 — Chatbot UI Smoke Test

This experiment validates the basic UI contract of an AI-style chatbot interface using Playwright and Pytest.

It covers:

- chatbot page loading;
- prompt input visibility;
- send button visibility;
- response panel visibility;
- prompt submission;
- deterministic response rendering;
- empty prompt validation.

Related files:

- [`demo/chatbot.html`](demo/chatbot.html)
- [`tests/test_demo_chatbot_ui.py`](tests/test_demo_chatbot_ui.py)
- [`docs/experiment_001_chatbot_ui_smoke_test.md`](docs/experiment_001_chatbot_ui_smoke_test.md)

---

## Experiment 002 — Agent Skill Quality Evaluation

This experiment evaluates a reusable Claude-style Agent Skill as a testable QA artefact.

It covers:

- skill folder structure;
- `SKILL.md` validation;
- expected input and output definition;
- safety and reliability rules;
- example user story and expected test cases;
- Pytest-based structural validation.

Related files:

- [`skills/qa-test-case-generator/SKILL.md`](skills/qa-test-case-generator/SKILL.md)
- [`skills/qa-test-case-generator/examples/sample_user_story.md`](skills/qa-test-case-generator/examples/sample_user_story.md)
- [`skills/qa-test-case-generator/examples/expected_test_cases.md`](skills/qa-test-case-generator/examples/expected_test_cases.md)
- [`rubrics/agent_skill_quality_rubric.md`](rubrics/agent_skill_quality_rubric.md)
- [`tests/test_agent_skill_structure.py`](tests/test_agent_skill_structure.py)
- [`docs/experiment_002_agent_skill_quality_evaluation.md`](docs/experiment_002_agent_skill_quality_evaluation.md)

---

## Experiment 003 — Prompt Injection Risk Baseline

This experiment defines a structured baseline dataset for prompt injection and AI security testing.

It covers:

- instruction override;
- secret extraction;
- role manipulation;
- data leakage;
- policy bypass;
- jailbreak attempts;
- tool misuse;
- context exfiltration;
- expected safe behaviour;
- observable failure signals.

Related files:

- [`data/security_prompts.json`](data/security_prompts.json)
- [`rubrics/prompt_injection_risk_rubric.md`](rubrics/prompt_injection_risk_rubric.md)
- [`tests/test_prompt_injection_dataset.py`](tests/test_prompt_injection_dataset.py)
- [`docs/experiment_003_prompt_injection_risk_baseline.md`](docs/experiment_003_prompt_injection_risk_baseline.md)

---

## Experiment 004 — Secure Publishing Workflow

This experiment simulates a small SaaS-style publishing workflow and validates it using Playwright and Pytest.

It demonstrates how a Quality Engineer can test realistic product behaviour without using proprietary data, private business rules or company-specific implementation details.

It covers:

- draft creation;
- content preview;
- submit for review;
- publish workflow;
- required field validation;
- role-based publish permissions;
- safe rendering of potentially unsafe content;
- Playwright Page Object Model.

Related files:

- [`demo/publishing_workflow.html`](demo/publishing_workflow.html)
- [`pages/publishing_workflow_page.py`](pages/publishing_workflow_page.py)
- [`tests/test_secure_publishing_workflow.py`](tests/test_secure_publishing_workflow.py)
- [`rubrics/publishing_workflow_quality_rubric.md`](rubrics/publishing_workflow_quality_rubric.md)
- [`docs/experiment_004_secure_publishing_workflow.md`](docs/experiment_004_secure_publishing_workflow.md)

---

## Experiment 005 — Shift-Left Requirement Quality Gate

This experiment demonstrates how Quality Engineering can shift left by evaluating user stories before implementation starts.

It validates whether requirements include enough clarity, acceptance criteria, business rules, negative scenarios, edge cases, security considerations and testability notes to support development and automation.

It covers:

- requirement clarity;
- persona, goal and benefit;
- acceptance criteria;
- business rules;
- edge cases;
- negative scenarios;
- security considerations;
- testability notes;
- risk classification;
- AI-assisted development readiness.

Related files:

- [`data/user_stories.json`](data/user_stories.json)
- [`rubrics/shift_left_requirement_quality_rubric.md`](rubrics/shift_left_requirement_quality_rubric.md)
- [`tests/test_shift_left_requirement_quality.py`](tests/test_shift_left_requirement_quality.py)
- [`docs/experiment_005_shift_left_requirement_quality_gate.md`](docs/experiment_005_shift_left_requirement_quality_gate.md)

---

## Repository Structure

```text
ai-quality-lab/
├── .github/
│   └── workflows/
├── data/
├── demo/
├── docs/
├── pages/
├── reports/
├── rubrics/
├── skills/
├── tests/
├── README.md
├── pytest.ini
└── requirements.txt
```

---

## Running the Tests

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

Run the test suite:

```bash
pytest
```

The same suite is executed through GitHub Actions on every push.

---

## What This Project Demonstrates

This repository demonstrates how more than twenty years of Quality Assurance and Quality Engineering experience can be applied to the new generation of AI-powered products.

It shows practical capability across:

- test strategy design;
- exploratory and risk-based thinking;
- Playwright browser automation;
- Python and Pytest implementation;
- LLM response evaluation;
- AI risk modelling;
- prompt injection test design;
- quality gates and reporting;
- documentation of repeatable QA practices;
- shift-left quality review;
- AI-assisted development readiness.

---

## Philosophy

Every experiment in this lab must answer a real quality question about AI-based systems.

The aim is not to learn tools for their own sake. The aim is to understand how to evaluate the quality, reliability, safety and usefulness of intelligent applications.

Each experiment should produce at least one tangible output:

- reusable code;
- documentation;
- test cases;
- evaluation rubrics;
- technical notes;
- good practices;
- automation examples;
- risk-based testing artefacts.