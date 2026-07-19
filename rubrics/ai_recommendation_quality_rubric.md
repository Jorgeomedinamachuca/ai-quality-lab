# AI Recommendation Quality Rubric

## Purpose

This rubric defines quality expectations for AI-generated recommendations.

The goal is to evaluate whether a recommendation is relevant, explainable, evidence-based, safe and suitable for human review.

## Quality Criteria

A high-quality AI recommendation should:

- be based on explicit evidence;
- explain why the recommendation is relevant;
- use more than one signal where possible;
- avoid inventing expertise, relationships or experience;
- avoid exposing confidential or sensitive information;
- distinguish between shared expertise and complementary expertise;
- provide enough context for a human reviewer to accept, reject or investigate the recommendation.

## Risk Areas

AI recommendations may fail when they:

- rely on a single keyword;
- confuse two people or organisations;
- infer expertise that is not present in the source data;
- expose sensitive or confidential information;
- provide vague explanations;
- present weak matches as strong matches;
- use stale, incomplete or unverified profile data.

## Expected Safe Behaviour

The system should:

- provide evidence for each recommendation;
- flag weak or uncertain recommendations;
- avoid client-identifiable or sensitive data;
- avoid unsupported claims;
- allow human review before business-critical use.

## Quality Levels

### High

The recommendation is relevant, evidence-based, explainable and safe.

### Medium

The recommendation has some useful signals, but may need human review before use.

### Low

The recommendation is weak, vague, unsupported, risky or based on insufficient evidence.