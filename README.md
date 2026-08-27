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
| 006 | Evidence-Based AI Recommendation Evaluation | Evaluates AI-style recommendations for evidence, explainability, risk and safety. | Pytest, JSON, AI QA, Risk-Based Testing |
| 007 | Analytics Signal Integrity Investigation | Investigates analytics signal declines before drawing conclusions about user behaviour. | Pytest, JSON, Analytics QA, Data Integrity |
| 008 | Data Provenance and Entity Resolution Quality Gate | Validates profile data provenance, source traceability and identity safety before AI use. | Pytest, JSON, Data Quality, Entity Resolution |
| 009 | AI Output Grounding and Hallucination Guardrail | Evaluates whether AI outputs are supported by evidence and avoid hallucinated claims. | Pytest, JSON, LLM Evaluation, Groundedness |
| 010 | Human-in-the-Loop AI Review Workflow | Validates browser-based review controls for approving, rejecting or requesting changes to AI-generated outputs. | Playwright, TypeScript, Browser Automation, AI Assurance |
| 011 | AI Risk Triage and Review Routing | Combines Python risk-rule validation with TypeScript Playwright browser workflow routing for AI-generated outputs. | Pytest, JSON, Playwright, TypeScript, AI Risk Triage |

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

## Experiment 006 — Evidence-Based AI Recommendation Evaluation

This experiment evaluates AI-style recommendations using structured test data, a quality rubric and automated Pytest checks.

It focuses on whether recommendations are evidence-based, explainable, safe and suitable for human review. It also checks for common AI recommendation risks such as weak single-signal matches, missing evidence, vague explanations, identity confusion and sensitive information exposure.

It covers:

- evidence-based recommendation quality;
- weak single-signal matches;
- missing evidence;
- vague explanations;
- identity confusion risk;
- sensitive information exposure;
- safety notes for high-risk recommendations;
- human review readiness.

Related files:

- [`data/recommendation_cases.json`](data/recommendation_cases.json)
- [`rubrics/ai_recommendation_quality_rubric.md`](rubrics/ai_recommendation_quality_rubric.md)
- [`tests/test_ai_recommendation_quality.py`](tests/test_ai_recommendation_quality.py)
- [`docs/experiment_006_ai_recommendation_quality_evaluation.md`](docs/experiment_006_ai_recommendation_quality_evaluation.md)

---
## Experiment 007 — Analytics Signal Integrity Investigation

This experiment investigates analytics signal declines before drawing conclusions about user behaviour.

It focuses on whether a metric decline reflects real behavioural change or whether it may be caused by measurement, tracking, dashboard, pipeline, segmentation, consent, bot filtering or reporting issues.

It covers:

- gradual analytics signal decline;
- sudden post-release drops;
- segment-specific drops;
- dashboard-only reporting mismatches;
- controlled methodology changes;
- large unexplained declines;
- raw data versus dashboard comparison;
- safe conclusions that avoid overstating user behaviour;
- investigation evidence before business interpretation.

Related files:

- [`data/analytics_signal_cases.json`](data/analytics_signal_cases.json)
- [`rubrics/analytics_signal_integrity_rubric.md`](rubrics/analytics_signal_integrity_rubric.md)
- [`tests/test_analytics_signal_integrity.py`](tests/test_analytics_signal_integrity.py)
- [`docs/experiment_007_analytics_signal_integrity_investigation.md`](docs/experiment_007_analytics_signal_integrity_investigation.md)

## Experiment 008 — Data Provenance and Entity Resolution Quality Gate

This experiment evaluates whether professional profile data is traceable, verifiable and safe before it is displayed or used in AI-powered recommendations.

It focuses on data provenance, source traceability, entity resolution, stale data, identity confusion and cross-context contamination risk.

It covers:

- missing source references;
- unclear source types;
- stale profile data;
- low-confidence identity matches;
- duplicate identity merge risk;
- cross-context contamination;
- high or critical identity risk;
- unsafe use of unverified data as AI recommendation evidence;
- safe handling rules for risky profile fields.

Related files:

- [`data/profile_provenance_cases.json`](data/profile_provenance_cases.json)
- [`rubrics/data_provenance_entity_resolution_rubric.md`](rubrics/data_provenance_entity_resolution_rubric.md)
- [`tests/test_data_provenance_entity_resolution.py`](tests/test_data_provenance_entity_resolution.py)
- [`docs/experiment_008_data_provenance_entity_resolution_quality_gate.md`](docs/experiment_008_data_provenance_entity_resolution_quality_gate.md)

## Experiment 009 — AI Output Grounding and Hallucination Guardrail

This experiment evaluates whether AI-generated outputs are grounded in the evidence provided.

It focuses on unsupported claims, fabricated sources, overconfident conclusions, inference presented as fact, missing limitations and hallucination risk.

It covers:

- unsupported expertise claims;
- fabricated source references;
- inference presented as fact;
- missing limitations;
- overconfident conclusions;
- weakly grounded outputs;
- ungrounded outputs;
- hallucination risk;
- safe uncertainty handling;
- rejection or rewrite rules for low-quality AI outputs.

Related files:

- [`data/ai_output_grounding_cases.json`](data/ai_output_grounding_cases.json)
- [`rubrics/ai_output_grounding_rubric.md`](rubrics/ai_output_grounding_rubric.md)
- [`tests/test_ai_output_grounding.py`](tests/test_ai_output_grounding.py)
- [`docs/experiment_009_ai_output_grounding_and_hallucination_guardrail.md`](docs/experiment_009_ai_output_grounding_and_hallucination_guardrail.md)

## Experiment 010 — Human-in-the-Loop AI Review Workflow

This experiment validates a browser-based human review workflow for AI-generated outputs.

It focuses on the product layer where reviewers interact with AI-generated content and decide whether to approve, reject or request changes.

It covers:

- visibility of AI output;
- visibility of supporting evidence;
- visibility of review controls;
- approval of fully grounded low-risk AI output;
- blocking approval for weakly grounded AI output;
- blocking approval for high hallucination-risk output;
- requiring review notes before rejection;
- requiring review notes before requesting changes;
- clear workflow status after reviewer action.

Related files:

- [`demo/ai_review_workflow.html`](demo/ai_review_workflow.html)
- [`tests-ts/ai-review-workflow.spec.ts`](tests-ts/ai-review-workflow.spec.ts)
- [`docs/experiment_010_human_in_the_loop_ai_review_workflow.md`](docs/experiment_010_human_in_the_loop_ai_review_workflow.md)

## Experiment 011 — AI Risk Triage and Review Routing

This experiment validates an AI risk triage model and a browser-based review routing workflow.

It combines Python/Pytest data validation with TypeScript/Playwright browser automation.

It covers:

- controlled AI risk levels;
- review route validation;
- approval policy validation;
- unsupported claims risk escalation;
- fabricated source blocking;
- missing evidence escalation;
- sensitive or regulated context escalation;
- low-risk standard review;
- medium-risk review with notes;
- high-risk senior review;
- critical-risk blocking;
- browser-level enforcement of the risk model.

Related files:

- [`data/ai_risk_triage_cases.json`](data/ai_risk_triage_cases.json)
- [`rubrics/ai_risk_triage_rubric.md`](rubrics/ai_risk_triage_rubric.md)
- [`tests/test_ai_risk_triage.py`](tests/test_ai_risk_triage.py)
- [`demo/ai_risk_triage_dashboard.html`](demo/ai_risk_triage_dashboard.html)
- [`tests-ts/ai-risk-triage-dashboard.spec.ts`](tests-ts/ai-risk-triage-dashboard.spec.ts)
- [`docs/experiment_011_ai_risk_triage_and_review_routing.md`](docs/experiment_011_ai_risk_triage_and_review_routing.md)

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
---

## Notice

Copyright © 2026 Jorge Medina Machuca. All rights reserved.

This repository is a personal portfolio and learning project. No permission is granted to copy, reuse, redistribute, commercially exploit or adapt its contents without explicit written permission.

See [NOTICE.md](NOTICE.md).
