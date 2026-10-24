
# Experiment 017 — Third-Party Script Governance Rubric

## Purpose

This rubric defines quality expectations for the governance of third-party scripts in a synthetic web application.

The objective is to validate script authorisation, source allowlisting, integrity verification, environment isolation, audit evidence and risk-based execution decisions.

## Core Quality Principle

A third-party script must not be permitted to execute solely because it is available or originates from a recognised source.

Execution must be supported by appropriate authorisation, source validation, integrity verification and environment-specific controls.

When the required evidence is missing or a security control fails, the default behaviour must prevent execution.

## Key Quality Criteria

A reliable third-party script governance process should:

- permit execution only for approved scripts;
- verify that script sources are allowlisted;
- require integrity verification before execution;
- prevent execution when integrity verification fails;
- preserve environment isolation;
- prevent pending or unapproved scripts from executing;
- maintain auditable evidence of authorisation decisions;
- enforce safe behaviour when execution is not requested;
- distinguish security risks from quality decisions;
- prevent unsafe scripts from being approved.

## Controlled Values

### Environment

- `test`
- `staging`
- `production`

### Script Status

- `approved`
- `unapproved`
- `pending_review`
- `disabled`

### Integrity Status

- `verified`
- `unverified`
- `mismatch`

### Security Risk

- `none`
- `medium`
- `high`
- `critical`

### Quality Status

- `valid`
- `requires_review`
- `blocked`

### Boolean Fields

The following fields must contain actual JSON boolean values:

- `source_allowlisted`
- `execution_requested`
- `execution_allowed`
- `environment_isolated`
- `audit_evidence_present`

## Expected Quality Rules

### Approved and Verified Scripts

A script may execute only when all of the following conditions are satisfied:

- `script_status` is `approved`;
- `source_allowlisted` is `true`;
- `integrity_status` is `verified`;
- `execution_requested` is `true`;
- `environment_isolated` is `true`;
- `audit_evidence_present` is `true`;
- `security_risk` is `none`;
- `quality_status` is `valid`.

The `execution_allowed` field must be `true` only when these conditions are satisfied.

### Unapproved Sources

A script originating from a source that is not allowlisted must not execute.

When `source_allowlisted` is `false`:

- `execution_allowed` must be `false`;
- `quality_status` must be `blocked`;
- `security_risk` must be `high` or `critical`.

### Integrity Verification

Integrity verification must be independent of source approval.

An allowlisted source does not automatically establish that a script has verified integrity.

When `integrity_status` is `unverified` or `mismatch`:

- script execution must be denied;
- an integrity mismatch must be blocked;
- an unverified execution request must be blocked in the baseline dataset;
- the quality decision must reflect the security risk.

### Environment Isolation

Script configurations must remain isolated to their intended environment.

When `environment_isolated` is `false`:

- `execution_allowed` must be `false`;
- `quality_status` must be `blocked`;
- `security_risk` must be `critical`.

### Audit Evidence

Audit evidence must support script governance decisions.

Evidence may include:

- authorisation status;
- source approval;
- integrity verification status;
- intended environment;
- execution request status;
- recorded quality decision.

When audit evidence is missing:

- execution must be denied;
- the workflow must not be classified as valid;
- review or blocking must be required, according to the risk.

### Pending Approval

Scripts awaiting approval must not execute.

When `script_status` is `pending_review`:

- `execution_allowed` must be `false`;
- `quality_status` must be `requires_review`;
- a review decision must be recorded before approval.

### Disabled Scripts

A script intentionally disabled by configuration must remain inactive.

When `script_status` is `disabled`:

- `execution_requested` must be `false`;
- `execution_allowed` must be `false`;
- the disabled state may be considered valid when supported by verified evidence and environment isolation.

### No Execution Requested

An approved and verified script does not need to execute merely because it is safe.

When `execution_requested` is `false`:

- `execution_allowed` must be `false`.

The workflow may remain valid if the script is approved, its integrity is verified and its provenance is supported by evidence.

## Quality Decision Matrix

| Condition | Expected Quality Status | Execution |
|---|---|---|
| Approved, allowlisted, verified and authorised for execution | `valid` | Allowed |
| Unapproved source | `blocked` | Denied |
| Integrity mismatch | `blocked` | Denied |
| Approved script with missing audit evidence | `requires_review` | Denied |
| Intentionally disabled script | `valid` | Denied |
| Environment isolation failure | `blocked` | Denied |
| Script awaiting approval | `requires_review` | Denied |
| Approved script without execution request | `valid` | Denied |
| Unverified integrity with execution requested | `blocked` | Denied |

## Blocking Rules

Script execution must be blocked when:

- the source is not authorised;
- integrity verification reports a mismatch;
- integrity is unverified and execution has been requested;
- environment isolation has failed;
- critical security risk is present;
- execution is requested for an explicitly unapproved script.

Missing audit evidence must prevent execution, even when the quality decision is `requires_review` rather than `blocked`.

## Safe Action Expectations

Each synthetic scenario must contain a meaningful `safe_action`.

Actions should align with the quality decision:

- `valid`: allow authorised execution or accept a verified inactive state;
- `requires_review`: request evidence, retain the denied execution state and complete review;
- `blocked`: prevent execution and investigate the failed security control.

## Python Quality Gate Expectations

Python/Pytest validation should check:

- dataset existence and structure;
- required fields;
- unique scenario identifiers;
- controlled values;
- boolean field integrity;
- execution authorisation rules;
- allowlist enforcement;
- integrity verification;
- environment isolation;
- audit evidence;
- pending approval handling;
- disabled state behaviour;
- quality and security risk consistency;
- meaningful safe actions.

## Browser Workflow Expectations

TypeScript/Playwright validation should check:

- scenario selection;
- displayed script governance attributes;
- execution permission status;
- appropriate quality banners;
- authorised execution decisions;
- review notes for pending or uncertain states;
- blocked actions for unsafe scripts;
- safe handling of disabled scripts;
- reset of workflow decisions when switching scenarios.

## Risk-Based Testing Perspective

The main risks are:

- unauthorised third-party script execution;
- execution of modified or unverified script content;
- incorrectly trusted external sources;
- missing authorisation evidence;
- cross-environment configuration contamination;
- bypassed approval processes;
- disabled scripts being executed;
- incorrect classification of critical security risks.

## Scope and Limitations

This experiment uses entirely synthetic scenarios and controlled quality decisions.

It does not load third-party scripts, make external script requests or execute untrusted JavaScript.

The initial Python quality gates validate declarative scenario rules.

The browser layer will validate a simulated governance dashboard.

These tests do not prove actual browser enforcement of Content Security Policy (CSP), Subresource Integrity (SRI), network restrictions or production script authorisation.

Real enforcement testing would require additional isolated fixtures and dedicated security test cases.

## Confidentiality and Synthetic Data

All cases, environments, authorisation decisions and security risks are fictional.

No proprietary source code, real internal tickets, production configurations, external suppliers or identifiable company implementations are represented.

## Key Principle

Third-party script governance is trustworthy only when script execution is supported by verified authorisation, source validation, integrity evidence and enforceable security boundaries.
