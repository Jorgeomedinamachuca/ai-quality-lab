# Experiment 009 — AI Output Grounding and Hallucination Guardrail

## Objective

This experiment evaluates whether AI-generated outputs are grounded in the evidence provided.

The goal is to detect unsupported claims, fabricated sources, overconfident conclusions and hallucination risk before AI outputs are trusted in product workflows.

## Why This Matters

AI-powered systems often generate summaries, recommendations, explanations and suggested actions.

These outputs may sound fluent and plausible while still introducing claims that are not supported by the available evidence.

A system may invent expertise, cite sources that were not provided, present assumptions as facts, omit uncertainty or make a recommendation stronger than the evidence allows.

This experiment treats AI-generated output as a testable quality artefact.

## Files

- `data/ai_output_grounding_cases.json`
- `rubrics/ai_output_grounding_rubric.md`
- `tests/test_ai_output_grounding.py`

## Quality Risks Covered

This experiment covers:

- unsupported expertise claims;
- fabricated source references;
- inference presented as fact;
- missing limitations;
- overconfident conclusions;
- weakly grounded outputs;
- ungrounded outputs;
- hallucination risk;
- safe uncertainty handling.

## Test Strategy

The automated tests validate that:

- the AI output grounding dataset exists;
- each grounding case has the required structure;
- case IDs are unique;
- controlled values are used for grounding status, hallucination risk and expected quality;
- provided evidence is present and structured;
- AI outputs are meaningful enough to evaluate;
- unsupported claims are structured as a list;
- fully grounded outputs do not contain unsupported claims;
- outputs with unsupported claims are not marked as high quality;
- ungrounded outputs are low quality and high or critical risk;
- fabricated source references are treated as critical risk;
- partially or weakly grounded outputs require rewrite, qualification or explicit evidence handling;
- safe actions are meaningful;
- low-quality outputs require rejection or rewrite;
- high-quality outputs are fully grounded and low risk;
- outputs cannot be fully grounded without evidence.

## QA Value

This experiment demonstrates a Quality Engineering approach to LLM output evaluation.

The focus is not only whether an AI system produces a fluent answer, but whether each claim can be traced back to the evidence available to the system.

It separates three different questions:

1. Is the output fluent?
2. Is the output supported by evidence?
3. Is the output safe to use in a product or business workflow?

## Relationship to Previous Experiments

This experiment extends the AI Quality Engineering logic developed in earlier experiments:

- Experiment 006 evaluates whether AI recommendations are evidence-based and safe.
- Experiment 007 evaluates whether analytics signals are reliable before business conclusions are drawn.
- Experiment 008 evaluates whether profile data has provenance and identity safety before it is used.
- Experiment 009 evaluates whether AI-generated output remains grounded in the evidence and avoids hallucination.

## Key Learning

AI output should not be trusted only because it sounds plausible.

A grounded AI output should be supported by evidence, acknowledge uncertainty and avoid unsupported claims, fabricated sources or overconfident conclusions.