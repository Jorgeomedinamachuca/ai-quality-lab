# AI Quality Regression Rubric

## Purpose

This rubric defines quality expectations for detecting AI quality regressions before a release candidate is approved.

The goal is to validate whether a release candidate preserves existing AI quality controls across grounding, hallucination risk, review routing, approval controls and evidence traceability.

## Core Quality Principle

An AI-powered product should not be released when a new version weakens existing quality, safety or review controls.

A release candidate should only be approved when AI quality gates pass and no blocking regression is detected.

## Key Quality Criteria

A reliable AI quality regression process should:

- detect grounding regressions;
- detect hallucination regressions;
- detect risk routing regressions;
- detect approval control regressions;
- detect evidence traceability regressions;
- block release candidates with critical failures;
- escalate release candidates with high-risk failures;
- require reviewer sign-off for medium-risk issues;
- approve only release candidates with no blocking regressions;
- align release status with release decision and safe action.

## Controlled Values

### Release Status

- `ready_for_release`
- `review_required`
- `requires_escalation`
- `blocked`

### Release Decision

- `approve_release`
- `approve_with_signoff`
- `escalate_release_review`
- `reject_release`

## Expected Release Decision Rules

The expected release model is:

- ready for release → approve release;
- review required → approve with sign-off;
- requires escalation → escalate release review;
- blocked → reject release.

## Blocking Regression Rules

A release candidate should be blocked when:

- critical failures are present;
- hallucination regression creates unsupported AI output;
- approval controls allow unsafe approval;
- multiple high-risk AI quality regressions are detected;
- the release would allow ungrounded or unsafe AI output into production.

## Escalation Rules

A release candidate should require escalation when:

- risk routing regression is detected;
- evidence traceability regression is detected;
- high-risk failures are present without a critical blocking failure;
- AI quality confidence is reduced but the release is not automatically rejected.

## Sign-off Rules

A release candidate may require sign-off where:

- only medium-risk failures are present;
- no critical failure exists;
- no high-risk failure exists;
- reviewer notes are required before approval.

## Low-Risk Release Rules

A release candidate may be ready for release only where:

- no grounding regression is detected;
- no hallucination regression is detected;
- no risk routing regression is detected;
- no approval control regression is detected;
- no evidence traceability regression is detected;
- no critical, high or medium risk failures are present;
- reviewer notes are not required.

## QA Value

This rubric supports cross-layer AI Quality Engineering.

It links AI output quality, data traceability, risk routing and browser workflow controls into a release-readiness model.

It helps teams ask:

- did this release introduce hallucinated output?
- did this release weaken grounding?
- did this release break risk routing?
- did this release allow unsafe approval?
- did this release lose evidence traceability?
- should this release be approved, signed off, escalated or rejected?

## Key Principle

AI release readiness should be evidence-based, regression-aware and enforceable across data, logic and browser workflow layers.