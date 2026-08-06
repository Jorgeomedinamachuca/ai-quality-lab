# Analytics Signal Integrity Rubric

## Purpose

This rubric defines quality expectations for investigating changes in product analytics signals.

The goal is to avoid treating analytics changes as reliable business evidence until measurement integrity has been checked.

A decline in analytics events does not automatically mean that user behaviour has declined. It may indicate a real behavioural change, but it may also indicate an instrumentation issue, data pipeline issue, dashboard issue, consent impact, segmentation issue or reporting logic change.

## Core Quality Principle

Analytics signals should be treated as testable data artefacts.

Before drawing a business conclusion from a metric change, Quality Engineering should verify whether the signal is complete, consistent, traceable and comparable across the reporting period.

## Investigation Criteria

A good analytics signal investigation should check:

- whether the decline is gradual, sudden, segment-specific or dashboard-only;
- whether raw events match reported dashboard values;
- whether tracking scripts or event listeners still fire correctly;
- whether any frontend, backend, API or pipeline release coincides with the change;
- whether event schemas changed during the reporting period;
- whether consent, cookie, privacy or browser behaviour affected event capture;
- whether bot filtering or invalid traffic rules changed;
- whether date ranges, timezones or aggregation logic changed;
- whether the decline affects all segments or only specific users, customers, channels or environments;
- whether the metric definition remained stable across the period.

## Risk Areas

Analytics signals may be misleading when:

- tracking implementation changes without test coverage;
- dashboards aggregate data differently from raw event logs;
- event names, schemas or payload fields change;
- consent rules reduce event capture;
- browser privacy controls block scripts;
- bot filtering changes remove previously counted traffic;
- segment filters are applied inconsistently;
- timezone or date range logic changes;
- missing events are interpreted as reduced user behaviour;
- business decisions are made before the measurement layer is validated.

## Expected Safe Behaviour

The investigation should:

- avoid premature conclusions;
- separate measurement integrity from user behaviour;
- require evidence before classifying a decline as real usage decline;
- document possible causes;
- compare multiple data sources where possible;
- identify whether the issue is product-wide or segment-specific;
- flag high-risk or critical drops for further investigation;
- state a safe conclusion that reflects uncertainty.

## Signal Integrity Levels

### High Integrity

The metric is supported by consistent raw events, stable tracking implementation, stable aggregation logic and no unexplained gaps.

### Partial Integrity

The metric shows a meaningful trend, but some areas require verification before the signal is used for business decisions.

### Low Integrity

The metric cannot be trusted because raw data, event capture, aggregation, segmentation or reporting logic may be incomplete or inconsistent.

## Investigation Status Values

The expected investigation status should use controlled values:

- `requires_investigation`
- `explainable_change`
- `confirmed_measurement_issue`
- `confirmed_usage_decline`
- `insufficient_evidence`

## QA Value

This rubric supports a Quality Engineering approach to product analytics.

It encourages teams to ask:

- are we measuring the same thing as before?
- are events still being captured correctly?
- is the dashboard telling the same story as the raw data?
- did the product change, the users change, or the measurement layer change?
- what evidence is needed before making a business conclusion?

## Key Principle

Do not treat an analytics signal as business truth until the measurement chain has been validated.