# AI Scoring Path Consistency Rubric

## Purpose

This rubric defines quality expectations for validating that AI scoring results are produced through consistent, traceable and expected scoring paths.

The goal is to detect scoring path inconsistency, missing provenance, unexpected scoring routes, mixed scoring paths and retry-related ambiguity before scored outputs are trusted.

## Core Quality Principle

AI scoring results should not be trusted only because a score exists.

A reliable scoring workflow should show which scoring path produced the result, whether retry logic was used, whether the actual scoring path matches the expected path and whether manual review is required before the result can be used.

## Key Quality Criteria

A reliable AI scoring path process should:

- record scoring provenance for every scored result;
- define the expected scoring path for each record group;
- record the actual scoring path used;
- detect mixed scoring paths;
- flag unexpected scoring paths;
- require review when retry logic is used;
- block results when scoring provenance is missing;
- escalate results where scoring paths are inconsistent;
- prevent inconsistent scoring results from being treated as valid;
- align risk level, quality status and safe action.

## Controlled Values

### Expected Scoring Path

- `ai_scoring`
- `rule_based_scoring`

### Actual Scoring Path

- `ai_scoring`
- `rule_based_scoring`
- `experimental_scoring`
- `human_review_adjustment`

### Risk Level

- `low`
- `medium`
- `high`
- `critical`

### Quality Status

- `valid`
- `review_required`
- `requires_review`
- `blocked`

## Expected Quality Rules

The expected scoring quality model is:

- low risk → valid;
- medium risk → review required;
- high risk → requires review;
- critical risk → blocked.

## Provenance Rules

Scoring provenance must be present when a scoring result exists.

If scoring provenance is missing, the result should be treated as critical risk and blocked.

## Mixed Path Rules

A scoring result should be flagged when more than one scoring path contributes to the final output.

Mixed scoring paths should require manual review because results may not be comparable across records.

## Retry Rules

Retry logic should not hide how a score was produced.

If retry was used, the scoring path should remain explicit and traceable. Retry usage should normally require review notes or manual review before the result is trusted.

## Unexpected Path Rules

If the actual scoring path does not match the expected scoring path, the result should be escalated for review.

Unexpected scoring paths should not be treated as valid without investigation.

## Low-Risk Rules

A scoring result may be low risk only when:

- scoring provenance is present;
- the actual scoring path matches the expected scoring path;
- no mixed path is detected;
- retry was not used;
- manual review is not required.

## QA Value

This rubric supports AI Quality Engineering for scoring and classification workflows.

It helps teams ask:

- which scoring path produced this result?
- does the actual scoring path match the expected path?
- was retry logic used?
- did retry logic change the scoring path?
- is scoring provenance available?
- are mixed paths present?
- should the result be accepted, reviewed, escalated or blocked?

## Key Principle

Every AI scoring result should be traceable to a consistent and expected scoring path before it is used in downstream product, analytics or review workflows.