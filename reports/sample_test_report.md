# Sample AI Test Report

## Feature Tested

Demo chatbot response quality.

## Test Scope

- Functional prompts
- Hallucination prompts
- Prompt injection prompts
- Data leakage prompts
- Safety prompts
- Usability prompts

## Summary

| Area | Result | Notes |
|---|---|---|
| Functional behaviour | Pass | Responses were understandable |
| Hallucination risk | Needs review | Some unsupported claims observed |
| Prompt injection | Pass | No hidden instructions exposed |
| Data leakage | Pass | No sensitive data exposed |
| Safety | Pass | Unsafe requests were refused |
| Usability | Pass | Responses were clear |

## Risk Assessment

| Risk | Severity | Recommendation |
|---|---|---|
| Unsupported factual claims | High | Add stricter grounding and uncertainty checks |
| Inconsistent repeated answers | Medium | Run repeated prompt batches and compare output patterns |
| Weak refusal wording | Medium | Define refusal-quality acceptance criteria |

## Recommendation

Add explicit acceptance criteria for response quality and repeat tests across multiple model runs. For high-risk journeys, combine automated checks with human review and risk-based release gates.
