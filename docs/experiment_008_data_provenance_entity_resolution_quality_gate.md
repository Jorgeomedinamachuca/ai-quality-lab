# Experiment 008 — Data Provenance and Entity Resolution Quality Gate

## Objective

This experiment evaluates whether professional profile data is traceable, verifiable and safe before it is displayed or used in AI-powered recommendations.

The goal is to show how Quality Engineering can assess data provenance and entity resolution risks before profile data becomes evidence for automated matching, recommendations or public-facing product workflows.

## Why This Matters

AI-powered systems often rely on structured profile data to make recommendations or generate matches.

However, profile data can be unreliable when the source is unclear, the timestamp is missing, the data is stale, or two identities have been incorrectly merged.

A profile field may look plausible but still be unsafe if it cannot be traced back to a reliable source.

This experiment treats profile provenance and entity resolution as testable quality artefacts.

## Files

- `data/profile_provenance_cases.json`
- `rubrics/data_provenance_entity_resolution_rubric.md`
- `tests/test_data_provenance_entity_resolution.py`

## Quality Risks Covered

This experiment covers:

- missing source references;
- unclear source types;
- stale profile data;
- low-confidence identity matches;
- duplicate identity merge risk;
- cross-context contamination;
- high or critical identity risk;
- unsafe use of unverified data in AI recommendations;
- profile data being displayed without sufficient provenance checks.

## Test Strategy

The automated tests validate that:

- the profile provenance dataset exists;
- each profile provenance case has the required structure;
- case IDs are unique;
- controlled values are used for match confidence, identity risk, provenance status and expected quality;
- source timestamps are valid ISO datetimes with timezone information;
- verified records require source references, high confidence and low identity risk;
- records without source references cannot be high quality;
- low-confidence identity matches require review;
- high or critical identity risk cannot be high quality;
- stale records are correctly flagged;
- risky records include enough evidence;
- cross-context contamination is suppressed or reviewed;
- safe actions are meaningful;
- unverified data is not used as confirmed AI evidence.

## QA Value

This experiment demonstrates a Quality Engineering approach to data provenance and identity safety.

It shows that data used by AI systems should be tested before it is trusted.

The focus is not only whether a profile field exists, but whether the field has a reliable source, a clear timestamp, sufficient identity confidence and a safe handling rule.

## Relationship to Previous Experiments

This experiment extends the data quality logic introduced in earlier experiments:

- Experiment 006 evaluates whether AI recommendations are evidence-based and safe.
- Experiment 007 evaluates whether analytics signals are reliable before business conclusions are drawn.
- Experiment 008 evaluates whether the underlying profile data is traceable and identity-safe before it is displayed or used as recommendation evidence.

## Key Learning

AI quality depends on data quality.

A recommendation system cannot be trusted if the profile data behind it has unclear provenance, stale sources, weak identity matching or possible cross-context contamination.