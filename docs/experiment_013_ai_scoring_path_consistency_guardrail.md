# Experiment 013 — AI Scoring Path Consistency Guardrail

## Objective

This experiment validates whether AI scoring results are produced through consistent, traceable and expected scoring paths.

The goal is to detect missing scoring provenance, mixed scoring paths, unexpected scoring routes and retry-related ambiguity before scored outputs are trusted in downstream product, analytics or review workflows.

## Why This Matters

AI-powered products often score, classify or rank records before those results are shown to users or used by downstream systems.

A scoring result may look valid because a score exists, but the quality risk is whether the system can explain how that score was produced.

If the scoring path is missing, inconsistent, mixed or unexpected, the result may not be comparable, auditable or safe to use.

This experiment treats scoring path consistency as a quality gate.

## Files

- `data/ai_scoring_path_cases.json`
- `rubrics/ai_scoring_path_consistency_rubric.md`
- `tests/test_ai_scoring_path_consistency.py`
- `demo/ai_scoring_path_dashboard.html`
- `tests-ts/ai-scoring-path-dashboard.spec.ts`

## Quality Risks Covered

This experiment covers:

- missing scoring provenance;
- mixed scoring paths;
- unexpected scoring paths;
- retry-related ambiguity;
- invalid scoring results treated as trustworthy;
- blocked scoring results;
- manual review requirements;
- mismatch between risk level and quality status;
- browser workflows that allow unsafe scoring results to be accepted.

## Python Test Strategy

The Python/Pytest tests validate that:

- the AI scoring path dataset exists;
- each scoring case has the required fields;
- case IDs are unique;
- controlled values are used;
- actual scoring paths are valid list values;
- boolean fields are valid booleans;
- quality status matches risk level;
- low-risk cases require a consistent and traceable scoring path;
- missing provenance is critical risk and blocked;
- mixed paths require review and high or critical risk;
- retry usage requires review;
- unexpected scoring paths require review;
- empty actual paths are only allowed when provenance is missing;
- valid results have no review or mixed-path flags;
- blocked results are not usable without review;
- actual path lists match the mixed-path flag;
- safe actions are meaningful and aligned with quality status;
- non-blocked scoring results are traceable.

## Browser Automation Test Strategy

The TypeScript/Playwright tests validate that:

- the scoring path dashboard controls are visible;
- a valid consistent scoring path can be accepted;
- retry paths require review notes;
- mixed scoring paths are routed to manual review;
- missing scoring provenance blocks the scoring result;
- visible scoring path attributes update when the selected case changes.

## QA Value

This experiment demonstrates cross-layer AI Quality Engineering for scoring workflows.

The Python layer validates the scoring path model and consistency rules.

The TypeScript/Playwright layer validates that the browser workflow enforces review, acceptance and blocking behaviour according to scoring path quality.

Together, they show how AI scoring results can be tested for traceability, comparability and safe downstream use.

## Relationship to Previous Experiments

This experiment builds on earlier work:

- Experiment 009 evaluated AI output grounding and hallucination guardrails.
- Experiment 010 validated human-in-the-loop review controls.
- Experiment 011 combined AI risk triage with review routing.
- Experiment 012 validated AI release-readiness regression gates.
- Experiment 013 focuses on scoring path consistency and provenance before scored outputs are trusted.

## Key Learning

AI scoring quality is not only about the final score.

A reliable AI scoring workflow must preserve scoring provenance, keep scoring paths consistent and route ambiguous or inconsistent results to review before downstream use.