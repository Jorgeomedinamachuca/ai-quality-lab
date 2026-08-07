# Data Provenance and Entity Resolution Rubric

## Purpose

This rubric defines quality expectations for professional profile data used in AI-powered recommendations, matching systems or public-facing product workflows.

The goal is to ensure that profile fields are traceable, verifiable and safe before they are displayed or used as evidence for automated recommendations.

## Core Quality Principle

Professional profile data should not be trusted only because it appears plausible.

Before a profile field is displayed or used by an AI system, Quality Engineering should verify:

- where the data came from;
- when it was collected or imported;
- whether the source is trusted;
- whether the identity match is reliable;
- whether the data may be stale;
- whether the data may belong to another person, organisation or context;
- whether human review is required before use.

## Key Quality Criteria

A high-quality profile data record should include:

- a clear source type;
- a source reference;
- a source timestamp;
- an explicit provenance status;
- an entity match confidence level;
- an identity risk level;
- supporting evidence;
- a safe action for handling the data.

## Risk Areas

Profile data may be unsafe or unreliable when:

- the source is unknown;
- the source reference is missing;
- the source timestamp is missing;
- the data is stale;
- two identities have been merged incorrectly;
- two organisations have been mixed in one profile field;
- a field comes from aggregated or transformed data without sufficient traceability;
- identity matching is based only on weak signals such as name or role similarity;
- low-confidence data is published automatically;
- profile data is used in AI recommendations without provenance checks.

## Entity Resolution Risks

Entity resolution is especially risky when the system tries to decide whether two records refer to the same person or organisation.

A weak entity resolution process may create false associations, such as:

- assigning the wrong employer to a professional;
- merging two professionals with similar names;
- combining historical and current roles incorrectly;
- presenting stale employment data as current;
- mixing data from different organisations or contexts;
- using incorrect profile data as evidence for AI recommendations.

## Expected Safe Behaviour

The system should:

- block or flag fields with missing provenance;
- avoid automatically publishing high-risk identity matches;
- require manual review when entity match confidence is low;
- flag stale data before using it in recommendations;
- suppress fields where cross-context contamination is suspected;
- avoid using unverified data as evidence for AI recommendations;
- provide a clear safe action for each risk scenario.

## Provenance Status Values

The expected provenance status should use controlled values:

- `verified`
- `incomplete`
- `stale`
- `requires_review`
- `rejected`

## Entity Match Confidence Values

The expected entity match confidence should use controlled values:

- `low`
- `medium`
- `high`

## Identity Risk Values

The expected identity risk should use controlled values:

- `low`
- `medium`
- `high`
- `critical`

## Quality Levels

### High

The data has clear provenance, recent source information, high entity match confidence and low identity risk.

### Medium

The data has some evidence but requires caution, confirmation or freshness checks before use.

### Low

The data has missing provenance, stale source information, low match confidence, high identity risk or possible cross-context contamination.

## QA Value

This rubric supports a Quality Engineering approach to data provenance and identity safety.

It encourages teams to ask:

- do we know where this data came from?
- can we trace the source?
- is the source recent enough?
- are we sure this profile belongs to the right person?
- could this data belong to another organisation or context?
- should this field be blocked, flagged or manually reviewed?

## Key Principle

Do not display or use professional profile data in AI recommendations unless its provenance and identity boundaries are sufficiently verified.