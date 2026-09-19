# Async Attribution Recovery Rubric

## Purpose

This rubric defines quality expectations for workflows where a user-facing action must remain fast while attribution or audit enrichment may be completed asynchronously.

The goal is to validate that slow downstream dependency work does not block the user-facing path, and that attribution can still be recovered safely through deferred processing.

## Core Quality Principle

A user-facing workflow should not wait unnecessarily for slow downstream attribution enrichment.

If attribution cannot be completed immediately, the system should preserve enough audit evidence to recover it later without losing traceability.

## Key Quality Criteria

A reliable deferred attribution workflow should:

- keep the user-facing response fast;
- avoid blocking the hot path on slow downstream dependencies;
- create a deferred attribution record when immediate attribution cannot complete;
- preserve audit evidence for recovery;
- keep failed recovery attempts retryable;
- mark lost attribution as critical risk;
- block workflows where attribution is deferred without recovery evidence;
- distinguish completed, deferred, recovered, failed and lost attribution states;
- align data loss risk, quality status and safe action.

## Controlled Values

### User-Facing Response

- `fast`
- `slow`

### Downstream Dependency Status

- `available`
- `temporarily_unavailable`
- `slow`
- `failed`

### Attribution Status

- `completed`
- `deferred`
- `recovered`
- `recovery_failed`
- `lost`

### Data Loss Risk

- `none`
- `low`
- `medium`
- `high`
- `critical`

### Quality Status

- `valid`
- `recovery_pending`
- `requires_review`
- `blocked`

## Expected Quality Rules

The expected quality model is:

- valid workflows have fast user-facing response and complete or recovered attribution;
- recovery-pending workflows are allowed only when deferred records and audit evidence are present;
- workflows that block the user-facing path on slow dependency work require review;
- workflows with failed recovery require review while remaining retryable;
- workflows with lost attribution or missing recovery evidence are blocked.

## Hot-Path Rules

The hot path should remain fast.

Slow downstream dependency work should not be performed synchronously where it delays the user-facing response.

## Deferred Attribution Rules

Deferred attribution is acceptable only when:

- a deferred record is created;
- audit evidence is present;
- background recovery is required;
- the failure remains retryable;
- data loss risk is not critical.

## Background Recovery Rules

Recovered attribution should be treated as valid where audit evidence remains present and the deferred record allowed attribution to be reconciled.

Failed recovery attempts should remain retryable unless attribution is confirmed lost.

## Blocking Rules

The workflow should be blocked when:

- attribution is lost;
- no deferred record exists after dependency failure;
- audit evidence is missing for deferred attribution;
- data loss risk is critical;
- recovery is impossible or untraceable.

## QA Value

This rubric supports AI Quality Engineering for product workflows where attribution, audit or evidence enrichment may not complete synchronously.

It helps teams ask:

- did the user-facing path remain fast?
- was slow dependency work deferred?
- was enough evidence preserved for recovery?
- can failed recovery be retried?
- was attribution eventually completed or recovered?
- was data loss prevented?
- should the workflow be accepted, reviewed, retried or blocked?

## Key Principle

A workflow can be fast and still trustworthy only if deferred attribution is traceable, recoverable and supported by audit evidence.