# AI Output Grounding Rubric

## Purpose

This rubric defines quality expectations for evaluating whether AI-generated outputs are grounded in the evidence provided.

The goal is to detect unsupported claims, fabricated sources, overconfident conclusions and hallucination risk before AI outputs are trusted in product workflows.

## Core Quality Principle

AI output should not be accepted only because it sounds fluent or plausible.

A high-quality AI output should be supported by the available evidence, clearly distinguish evidence from inference, acknowledge uncertainty where appropriate and avoid inventing facts, sources, expertise, relationships or experience.

## Key Quality Criteria

A grounded AI output should:

- use only facts present in the provided evidence;
- avoid unsupported expertise claims;
- avoid fabricated source references;
- avoid presenting assumptions as confirmed facts;
- acknowledge limitations in the evidence;
- separate evidence from inference;
- avoid overconfident recommendations where evidence is incomplete;
- be suitable for human review before business-critical use.

## Risk Areas

AI outputs may be unsafe or unreliable when they:

- invent professional expertise not present in the evidence;
- cite documents, reports or sources that were not provided;
- infer current activity from historical or general profile data;
- present weak evidence as strong proof;
- omit important limitations;
- confuse possible relevance with confirmed suitability;
- use plausible language to hide unsupported claims;
- create a recommendation that cannot be traced back to evidence.

## Grounding Status Values

The expected grounding status should use controlled values:

- `fully_grounded`
- `partially_grounded`
- `weakly_grounded`
- `ungrounded`

## Hallucination Risk Values

The expected hallucination risk should use controlled values:

- `low`
- `medium`
- `high`
- `critical`

## Quality Levels

The expected quality should use controlled values:

- `low`
- `medium`
- `high`

## Expected Safe Behaviour

The system should:

- allow outputs that are fully grounded and low risk;
- require qualification when evidence is incomplete;
- reject or rewrite outputs with unsupported claims;
- reject outputs that fabricate sources;
- avoid using ungrounded outputs as recommendation evidence;
- preserve human review for business-critical or high-risk use.

## Quality Levels

### High

The output is grounded in the evidence, avoids unsupported claims and handles uncertainty appropriately.

### Medium

The output is partly grounded but requires qualification, review or clearer uncertainty handling.

### Low

The output includes unsupported claims, fabricated sources, overconfident conclusions or ungrounded assertions.

## QA Value

This rubric supports a Quality Engineering approach to LLM output evaluation.

It encourages teams to ask:

- what evidence supports this claim?
- did the AI add anything that was not provided?
- is the output presenting inference as fact?
- has the AI fabricated a source?
- does the output acknowledge uncertainty?
- should this be allowed, rewritten or rejected?

## Key Principle

Do not trust AI output unless its claims can be traced back to the available evidence.