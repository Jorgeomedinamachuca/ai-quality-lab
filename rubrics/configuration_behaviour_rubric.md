# Experiment 016 — Configuration-Driven Behaviour Rubric

## Purpose

This rubric defines quality expectations for synthetic, configuration-driven product workflows.

The objective is to validate that configuration changes preserve expected behaviour, environment isolation, feature flag consistency, audit traceability and secure fallback handling.

## Core Quality Principle

A configuration should only be accepted when its behaviour is predictable, authorised, traceable and isolated to the intended environment.

Missing, invalid or unverified configurations must not silently enable unsafe functionality.

## Key Quality Criteria

A reliable configuration-driven workflow should:

- preserve environment isolation;
- apply feature flags consistently;
- detect configuration drift;
- maintain configuration provenance and audit evidence;
- use safe defaults for missing or invalid configurations;
- prevent unverified feature activation;
- block unsafe cross-environment configuration behaviour;
- assign appropriate security risks;
- align quality decisions with the configuration state.

## Controlled Values

### Environment

- `test`
- `staging`
- `production`

### Configuration Status

- `valid`
- `missing`
- `invalid`
- `drift_detected`
- `unverified`

### Feature Flag Status

- `enabled`
- `disabled`

### Security Risk

- `none`
- `low`
- `medium`
- `high`
- `critical`

### Quality Status

- `valid`
- `fallback_required`
- `requires_review`
- `blocked`

## Expected Quality Rules

### Valid Configuration

A configuration may be classified as `valid` when:

- the configuration status is `valid`;
- environment isolation is preserved;
- audit evidence is present;
- no unresolved configuration drift exists;
- security risk is `none`;
- feature flag behaviour is consistent with the approved configuration.

### Missing Configuration

When a required configuration is missing:

- the affected feature should be disabled;
- a safe default should be applied;
- audit evidence should be preserved;
- the quality status should be `fallback_required`.

### Invalid Configuration

An invalid configuration must not be accepted automatically.

If the affected feature is disabled using a verified safe default, the workflow may be classified as `fallback_required`.

If an invalid configuration causes unsafe behaviour, the workflow must be blocked.

### Configuration Drift

Configuration drift occurs when the active configuration differs from its approved baseline.

When drift remains unresolved:

- `configuration_drift` must be `true`;
- the configuration must not be classified as `valid`;
- review or blocking is required according to the risk;
- the discrepancy should be documented.

After successful remediation, the configuration may return to `valid` when its baseline and audit evidence are verified.

### Environment Isolation

Configurations must remain isolated to their intended environment.

If `environment_isolated` is `false`:

- the workflow must be `blocked`;
- the security risk must be `high` or `critical`;
- the configuration must not be accepted as safe.

### Feature Flag Safety

Feature flags should reflect the intended configuration state.

An enabled feature must not be approved when:

- its configuration is unverified;
- required audit evidence is missing;
- environment isolation has failed;
- unresolved critical configuration drift exists.

A disabled feature may be accepted when disabling it is intentional, authorised and supported by evidence.

### Safe Default Behaviour

Safe defaults must protect the system when configurations are missing or invalid.

When `safe_default_applied` is `true`:

- the affected feature should be `disabled`;
- the workflow must preserve environment isolation;
- the fallback should be auditable;
- the configuration must not be classified as fully valid until the original configuration issue is resolved.

### Audit Evidence

Configuration decisions should preserve sufficient evidence to establish:

- the intended configuration state;
- the authorised environment;
- the expected feature flag behaviour;
- whether configuration drift was detected;
- whether safe fallback was applied;
- the resulting quality decision.

Missing audit evidence must prevent approval of an unverified feature activation.

## Quality Decision Matrix

| Condition | Expected Quality Status |
|---|---|
| Verified, isolated configuration with no risk | `valid` |
| Intentionally disabled feature with verified configuration | `valid` |
| Missing configuration with safe default | `fallback_required` |
| Invalid configuration with verified fail-safe behaviour | `fallback_required` |
| Unresolved configuration drift requiring investigation | `requires_review` |
| Cross-environment configuration contamination | `blocked` |
| Unverified feature activation without audit evidence | `blocked` |
| Corrected and verified configuration drift | `valid` |

## Blocking Rules

A configuration must be blocked when:

- environment isolation has failed;
- unverified configuration enables functionality without audit evidence;
- an invalid configuration produces unsafe behaviour;
- critical security risk remains unresolved;
- unsafe configuration behaviour is incorrectly treated as valid.

## Safe Action Expectations

Each synthetic scenario must contain a meaningful `safe_action`.

Safe actions should describe an appropriate QA response, such as:

- accept a verified configuration;
- apply a safe default;
- investigate configuration drift;
- restore an approved baseline;
- block an unsafe activation;
- verify configuration provenance before approval.

## Python Quality Gate Expectations

Python/Pytest validation should check:

- dataset structure and required fields;
- unique scenario identifiers;
- controlled values;
- boolean field integrity;
- relationships between configuration and quality status;
- environment isolation;
- feature flag safety;
- configuration drift handling;
- audit evidence requirements;
- safe default behaviour;
- meaningful safe actions.

## Browser Workflow Expectations

TypeScript/Playwright validation should check:

- configuration scenario selection;
- visible configuration attributes;
- correct quality status display;
- enabled and disabled workflow actions;
- review notes where required;
- blocking of unsafe configurations;
- safe fallback routing;
- updates when a different scenario is selected.

## Risk-Based Testing Perspective

The main quality risks are:

- configuration drift;
- unexpected feature activation;
- missing configuration evidence;
- unsafe defaults;
- cross-environment configuration contamination;
- inconsistencies between feature flag state and configuration status;
- insufficient review controls;
- incorrect approval of unsafe configurations.

## Scope and Limitations

This experiment uses entirely synthetic scenarios.

It does not test a real configuration service, feature flag provider, production infrastructure, deployment pipeline or access-control system.

The initial quality gates validate a controlled dataset and simulated browser workflow decisions. They do not measure live configuration propagation or prove infrastructure-level isolation.

## Key Principle

Configuration-driven systems remain trustworthy when configuration changes are traceable, environment boundaries are preserved, and unsafe states are detected before approval.