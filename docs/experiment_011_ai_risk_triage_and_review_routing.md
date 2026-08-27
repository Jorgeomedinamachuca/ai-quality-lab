# Experiment 011 — AI Risk Triage and Review Routing

## Objective

This experiment validates an AI risk triage model and a browser-based review routing workflow.

The goal is to ensure that AI-generated outputs are routed to the correct human review path according to grounding status, hallucination risk, unsupported claims, fabricated sources, evidence availability and sensitive or regulated context.

## Why This Matters

AI-powered systems should not treat all outputs as equally safe.

Some outputs may be fully grounded and low risk. Others may contain unsupported claims, weak grounding, fabricated sources, missing evidence or sensitive context.

A robust AI assurance workflow should classify risk and route outputs accordingly.

This experiment combines two testing layers:

- Python/Pytest validates the data model, risk rules and expected routing logic.
- TypeScript/Playwright validates that the browser workflow displays and enforces the correct review route.

## Files

- `data/ai_risk_triage_cases.json`
- `rubrics/ai_risk_triage_rubric.md`
- `tests/test_ai_risk_triage.py`
- `demo/ai_risk_triage_dashboard.html`
- `tests-ts/ai-risk-triage-dashboard.spec.ts`

## Quality Risks Covered

This experiment covers:

- low-risk outputs being routed incorrectly;
- medium-risk outputs being approved without reviewer notes;
- high-risk outputs being approved without senior review;
- critical-risk outputs not being blocked;
- fabricated sources not being treated as critical risk;
- missing evidence being treated as low risk;
- high hallucination-risk outputs being routed to standard review;
- sensitive or regulated contexts not being escalated;
- mismatch between risk level, review route and approval policy;
- browser workflow controls not enforcing the risk model.

## Python Test Strategy

The Python/Pytest tests validate that:

- the AI risk triage dataset exists;
- each case has the required fields;
- case IDs are unique;
- controlled values are used;
- numeric counts are valid non-negative integers;
- boolean fields are valid booleans;
- review route matches risk level;
- approval policy matches risk level;
- low-risk outputs require strong grounding and low hallucination risk;
- medium-risk outputs require review with notes;
- high-risk outputs require senior review;
- critical-risk outputs are blocked;
- fabricated sources are critical risk and blocked;
- missing evidence cannot be low or medium risk;
- high hallucination risk cannot use standard review;
- sensitive or regulated context escalates when not fully grounded;
- unsupported claims prevent low-risk classification;
- ungrounded outputs cannot be low or medium risk;
- safe actions are meaningful and aligned with routing.

## Browser Automation Test Strategy

The TypeScript/Playwright tests validate that:

- the AI risk triage dashboard controls are visible;
- low-risk output is routed to standard review and can be approved;
- medium-risk output requires reviewer notes before approval;
- high-risk output is routed to senior review and blocks direct approval;
- critical-risk output is routed to a blocked state;
- visible risk attributes update when the selected case changes.

## QA Value

This experiment demonstrates how AI Quality Engineering can connect data validation, risk logic and browser automation.

The Python layer verifies that the underlying risk model is consistent.

The Playwright TypeScript layer verifies that the user interface applies that model in a realistic review workflow.

This makes the experiment closer to how AI assurance controls would be tested in a product environment.

## Relationship to Previous Experiments

This experiment builds on earlier work:

- Experiment 009 evaluated whether AI outputs are grounded and avoid hallucinated claims.
- Experiment 010 validated a human-in-the-loop review workflow.
- Experiment 011 combines risk scoring, review routing and browser workflow enforcement.

## Key Learning

AI quality controls should not stop at checking the text of an AI output.

A reliable AI product also needs risk triage, route enforcement and browser-level controls that prevent unsafe outputs from following a low-risk approval path.