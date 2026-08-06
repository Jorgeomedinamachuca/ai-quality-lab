# Experiment 007 — Analytics Signal Integrity Investigation

## Objective

This experiment investigates the integrity of product analytics signals when metrics show a significant decline.

The goal is to demonstrate that a decline in analytics events should not automatically be treated as a decline in real user behaviour until the measurement chain has been validated.

## Why This Matters

Product teams often use analytics signals to make decisions about engagement, adoption, product value and commercial performance.

However, analytics data can be affected by many factors that are not directly related to user behaviour. A metric may decline because of a tracking script issue, frontend regression, data pipeline delay, dashboard query change, consent or cookie impact, bot filtering change, segmentation issue or aggregation mismatch.

This experiment treats analytics signals as testable quality artefacts.

## Files

- `data/analytics_signal_cases.json`
- `rubrics/analytics_signal_integrity_rubric.md`
- `tests/test_analytics_signal_integrity.py`

## Quality Risks Covered

This experiment covers:

- gradual analytics signal decline;
- sudden post-release drops;
- segment-specific drops;
- dashboard-only reporting mismatch;
- controlled methodology changes;
- large unexplained declines;
- raw data versus dashboard mismatch;
- overconfident conclusions about user behaviour;
- insufficient evidence before business interpretation.

## Test Strategy

The automated tests validate that:

- the analytics signal dataset exists;
- each analytics case has the required structure;
- case IDs are unique;
- decline percentages match baseline and current values;
- decline patterns use controlled values;
- risk levels use controlled values;
- investigation statuses use controlled values;
- high-risk and critical cases include enough evidence checks;
- large unexplained declines require investigation;
- sudden declines are not treated as safe without investigation;
- dashboard mismatches require raw data comparison;
- segment-specific declines require segment comparison;
- safe conclusions do not overstate user behaviour;
- each case includes multiple possible causes;
- each case has a meaningful safe conclusion.

## QA Value

This experiment demonstrates a Quality Engineering approach to analytics and observability.

The focus is not only whether a dashboard shows a change, but whether the metric is complete, consistent, traceable and comparable across the reporting period.

It separates three different questions:

1. Did the metric decline?
2. Is the measurement layer reliable?
3. Does the decline reflect real user behaviour?

## Key Learning

A product analytics signal should not be treated as business truth until the measurement chain has been validated.

Analytics quality is part of product quality.