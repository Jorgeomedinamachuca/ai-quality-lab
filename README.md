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
| 012 | Cross-Layer AI Quality Regression Suite | Validates AI release candidates across Python quality gates and TypeScript Playwright browser workflow controls. | Pytest, JSON, Playwright, TypeScript, AI Regression Testing |
| 013 | AI Scoring Path Consistency Guardrail | Validates scoring path provenance, consistency and review controls across Python rules and TypeScript browser automation. | Pytest, JSON, Playwright, TypeScript, AI Scoring QA |
| 014 | Hot-Path Latency and Deferred Attribution Guardrail | Validates fast user-facing workflow behaviour, deferred attribution recovery, retryable failures and blocked states when attribution evidence is missing. | Pytest, JSON, Playwright, TypeScript, Async Workflow QA |
| 015 | Cache Isolation and Freshness Guardrail | Validates cache key isolation, freshness, stale data risk, fallback behaviour, audit evidence and blocked states for unsafe cached enrichment data. | Pytest, JSON, Playwright, TypeScript, Cache QA |
| 016 | Configuration-Driven Behaviour Guardrail | Validates feature flag consistency, configuration drift, environment isolation, fail-safe defaults and configuration quality decisions. | Pytest, JSON, Playwright, TypeScript, Configuration QA |

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
## Experiment 012 — Cross-Layer AI Quality Regression Suite

This experiment validates a cross-layer AI quality regression suite for release candidates.

It combines Python/Pytest release-readiness validation with TypeScript/Playwright browser automation for release workflow enforcement.

It covers:

- grounding regressions;
- hallucination regressions;
- risk routing regressions;
- approval control regressions;
- evidence traceability regressions;
- critical failure blocking;
- high-risk release escalation;
- medium-risk sign-off requirements;
- release status validation;
- release decision validation;
- browser-level release approval controls.

Related files:

- [`data/ai_quality_regression_cases.json`](data/ai_quality_regression_cases.json)
- [`rubrics/ai_quality_regression_rubric.md`](rubrics/ai_quality_regression_rubric.md)
- [`tests/test_ai_quality_regression.py`](tests/test_ai_quality_regression.py)
- [`demo/ai_quality_release_dashboard.html`](demo/ai_quality_release_dashboard.html)
- [`tests-ts/ai-quality-release-dashboard.spec.ts`](tests-ts/ai-quality-release-dashboard.spec.ts)
- [`docs/experiment_012_cross_layer_ai_quality_regression_suite.md`](docs/experiment_012_cross_layer_ai_quality_regression_suite.md)

## Experiment 013 — AI Scoring Path Consistency Guardrail

This experiment validates whether AI scoring results are produced through consistent, traceable and expected scoring paths.

It combines Python/Pytest scoring path validation with TypeScript/Playwright browser automation for review workflow enforcement.

It covers:

- scoring provenance;
- expected scoring path validation;
- actual scoring path validation;
- mixed scoring path detection;
- unexpected scoring path detection;
- retry-related ambiguity;
- manual review routing;
- blocked scoring results;
- browser-level scoring acceptance controls.

Related files:

- [`data/ai_scoring_path_cases.json`](data/ai_scoring_path_cases.json)
- [`rubrics/ai_scoring_path_consistency_rubric.md`](rubrics/ai_scoring_path_consistency_rubric.md)
- [`tests/test_ai_scoring_path_consistency.py`](tests/test_ai_scoring_path_consistency.py)
- [`demo/ai_scoring_path_dashboard.html`](demo/ai_scoring_path_dashboard.html)
- [`tests-ts/ai-scoring-path-dashboard.spec.ts`](tests-ts/ai-scoring-path-dashboard.spec.ts)
- [`docs/experiment_013_ai_scoring_path_consistency_guardrail.md`](docs/experiment_013_ai_scoring_path_consistency_guardrail.md)

## Experiment 014 — Hot-Path Latency and Deferred Attribution Guardrail

Experiment 014 validates a synthetic deferred attribution recovery workflow.

The experiment checks that a user-facing action can remain fast while attribution or audit enrichment is completed asynchronously. It focuses on hot-path latency risk, deferred attribution records, background recovery, retryable recovery failure, preserved audit evidence and blocked workflows when attribution is lost.

This experiment adds another reliability layer to the AI Quality Lab by testing not only whether a workflow produces the right status, but whether the system preserves traceability when work is moved away from the user-facing path.

### Quality focus

- Hot-path latency guardrails
- Deferred attribution recovery
- Background recovery logic
- Retryable failure handling
- Audit evidence preservation
- Data loss risk classification
- Review and blocked workflow routing

### Related files

```text
data/async_attribution_recovery_cases.json
rubrics/async_attribution_recovery_rubric.md
tests/test_async_attribution_recovery.py
demo/async_attribution_recovery_dashboard.html
tests-ts/async-attribution-recovery-dashboard.spec.ts
docs/experiment_014_hot_path_latency_and_deferred_attribution_guardrail.md
```

## Experiment 015 — Cache Isolation and Freshness Guardrail

Experiment 015 validates a synthetic cache isolation and freshness workflow.

The experiment checks that cached enrichment data remains isolated by context, fresh enough to trust, supported by audit evidence and routed safely when fallback, review or blocking is required.

This experiment adds a cache-aware reliability layer to the AI Quality Lab by testing whether performance optimisation preserves data isolation, freshness, provenance and trust.

### Quality focus

- Cache key isolation
- User and tenant context separation
- Freshness validation
- Stale and expired cache handling
- Safe fallback and refresh paths
- Audit evidence preservation
- Data leakage risk classification
- Review and blocked workflow routing

### Additional suite stabilisation

During this experiment, two earlier tests were updated to remove dependency on an external website.

The updated tests now use local synthetic fixtures instead of `example.com`, making the Python suite more deterministic and less dependent on network or third-party page behaviour.

### Related files

```text
data/cache_isolation_freshness_cases.json
rubrics/cache_isolation_freshness_rubric.md
tests/test_cache_isolation_freshness.py
demo/cache_isolation_freshness_dashboard.html
tests-ts/cache-isolation-freshness-dashboard.spec.ts
docs/experiment_015_cache_isolation_and_freshness_guardrail.md
tests/test_ai_chatbot_ui.py
tests/test_basic_navigation.py
```

## Experiment 016 — Configuration-Driven Behaviour Guardrail

Experiment 016 evaluates synthetic configuration-driven behaviour using risk-based quality gates.

The experiment validates configuration consistency, feature flag safety, environment isolation, configuration drift, fail-safe defaults and audit evidence.

It combines declarative Python/Pytest validation with a TypeScript/Playwright browser workflow that simulates accepting, reviewing, blocking or applying safe fallback to configuration scenarios.

### Quality focus

- Configuration drift detection
- Feature flag consistency
- Environment isolation
- Fail-safe defaults
- Configuration provenance
- Audit evidence
- Risk-based quality decisions
- Browser workflow guardrails

### Related files

- `data/configuration_behaviour_cases.json`
- `rubrics/configuration_behaviour_rubric.md`
- `tests/test_configuration_behaviour.py`
- `demo/configuration_behaviour_dashboard.html`
- `tests-ts/configuration-behaviour-dashboard.spec.ts`
- `docs/experiment_016_configuration_driven_behaviour_guardrail.md`

### Validation

- 29 Python/Pytest tests for Experiment 016
- 10 TypeScript/Playwright tests for Experiment 016
- 232 Python/Pytest tests passing across the lab
- 52 TypeScript/Playwright tests passing locally



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
