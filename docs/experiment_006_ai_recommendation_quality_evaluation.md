# Experiment 006 — Evidence-Based AI Recommendation Evaluation

## Objective

This experiment evaluates the quality of AI-style recommendations using structured test data and automated checks.

The goal is to show how Quality Engineering can assess AI recommendations before they are trusted in a product workflow.

## Why This Matters

AI-powered products often generate recommendations, matches or suggested actions.

A recommendation may look plausible but still be weak, unsafe or unsupported. For example, it may rely on a single keyword, confuse two identities, use stale data, expose sensitive information or invent expertise that is not present in the source data.

This experiment treats recommendations as testable quality artefacts.

## Files

- `data/recommendation_cases.json`
- `rubrics/ai_recommendation_quality_rubric.md`
- `tests/test_ai_recommendation_quality.py`

## Quality Risks Covered

This experiment covers:

- weak recommendations based on a single signal;
- missing evidence;
- vague explanations;
- unsupported expertise claims;
- sensitive information risk;
- identity confusion risk;
- high-risk recommendations without safety notes.

## Test Strategy

The automated tests validate that:

- the recommendation dataset exists;
- each recommendation case has the required structure;
- recommendation IDs are unique;
- input and recommended profiles contain role, topics and sector focus;
- recommendation reasons are meaningful;
- high-quality recommendations include enough evidence;
- single-signal recommendations are not marked as high quality;
- risk and quality levels use controlled values;
- high-risk recommendations include safety notes;
- sensitive client identifiers are not exposed.

## QA Value

This experiment demonstrates that AI recommendations should be evaluated against explicit criteria before being used.

The focus is not only whether an AI system returns an answer, but whether the recommendation is evidence-based, explainable, proportionate and safe for human review.

## Key Learning

AI recommendation quality can be tested through structured data, risk-based rubrics and automated validation.

This supports a shift from simple output checking to AI Quality Engineering.