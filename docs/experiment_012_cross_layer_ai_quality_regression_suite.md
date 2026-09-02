# Experiment 012 — Cross-Layer AI Quality Regression Suite

## Objective

This experiment validates a cross-layer AI quality regression suite for release candidates.

The goal is to ensure that a release candidate is not approved when it weakens existing AI quality controls across grounding, hallucination risk, review routing, approval controls or evidence traceability.

## Why This Matters

AI-powered products can regress even when the user interface still appears functional.

A new release may introduce hallucinated output, weaken evidence grounding, break risk routing, bypass approval controls or reduce evidence traceability.

Traditional UI checks may miss these risks if they only verify that buttons, pages and happy paths still work.

This experiment treats AI release readiness as a testable quality gate across data, rule logic and browser workflow behaviour.

## Files

- `data/ai_quality_regression_cases.json`
- `rubrics/ai_quality_regression_rubric.md`
- `tests/test_ai_quality_regression.py`
- `demo/ai_quality_release_dashboard.html`
- `tests-ts/ai-quality-release-dashboard.spec.ts`

## Quality Risks Covered

This experiment covers:

- grounding regressions;
- hallucination regressions;
- risk routing regressions;
- approval control regressions;
- evidence traceability regressions;
- release candidates with critical failures;
- release candidates with high-risk failures;
- medium-risk releases requiring reviewer sign-off;
- blocked releases;
- escalated release reviews;
- mismatch between release status and release decision;
- browser workflows that allow unsafe release approval.

## Python Test Strategy

The Python/Pytest tests validate that:

- the AI quality regression dataset exists;
- each release candidate has the required fields;
- case IDs are unique;
- release candidate IDs are unique;
- release status and release decision use controlled values;
- release decision matches release status;
- regression flags are valid booleans;
- failure counts are valid non-negative integers;
- ready releases have no regressions or failures;
- critical failures block release;
- hallucination regression blocks or escalates release;
- approval control regression blocks release;
- risk routing regression requires escalation or blocking;
- evidence traceability regression requires escalation or blocking;
- high-risk failures prevent direct release approval;
- medium-risk-only cases require review or sign-off;
- non-ready releases require review notes;
- blocked releases have reject safe actions;
- escalated releases have escalate safe actions;
- safe actions are meaningful.

## Browser Automation Test Strategy

The TypeScript/Playwright tests validate that:

- the AI quality release dashboard controls are visible;
- a release candidate with no AI quality regressions can be approved;
- a medium-risk release requires notes before approval with sign-off;
- a high-risk regression is routed to escalation and requires notes;
- a hallucination regression with a critical failure blocks release;
- release attributes update correctly when the selected release candidate changes.

## QA Value

This experiment demonstrates a cross-layer AI Quality Engineering approach.

The Python layer validates the release-readiness rules and regression model.

The TypeScript/Playwright layer validates that the browser workflow enforces the release decision model.

Together, they show how AI quality can be tested before release rather than only after production incidents or user complaints.

## Relationship to Previous Experiments

This experiment builds on earlier work:

- Experiment 009 evaluated AI output grounding and hallucination guardrails.
- Experiment 010 validated human-in-the-loop review controls in the browser.
- Experiment 011 combined AI risk triage with review routing.
- Experiment 012 turns those ideas into a regression suite for release readiness.

## Key Learning

AI regression testing should cover more than UI stability.

A reliable AI product needs release gates that detect weakened grounding, hallucination risk, broken routing, unsafe approval controls and missing evidence traceability before release.