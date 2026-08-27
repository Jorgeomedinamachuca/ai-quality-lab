# AI Risk Triage and Review Routing Rubric

## Purpose

This rubric defines quality expectations for triaging AI-generated outputs into the correct human review route.

The goal is to ensure that AI outputs are routed according to evidence quality, grounding status, hallucination risk, unsupported claims, fabricated sources and sensitive or regulated context.

## Core Quality Principle

AI-generated outputs should not follow the same review path regardless of risk.

A robust AI assurance workflow should route low, medium, high and critical risk outputs to different review paths, with stronger controls for weak grounding, unsupported claims, fabricated sources and sensitive contexts.

## Key Quality Criteria

A reliable AI risk triage process should:

- classify risk using controlled values;
- route low-risk outputs to standard review;
- require reviewer notes for medium-risk outputs;
- route high-risk outputs to senior review;
- block critical-risk outputs from approval;
- treat fabricated sources as critical risk;
- prevent missing evidence from being treated as low risk;
- escalate regulated or sensitive contexts when evidence is incomplete;
- align approval policy with risk level and review route.

## Controlled Values

### Grounding Status

- `fully_grounded`
- `partially_grounded`
- `weakly_grounded`
- `ungrounded`

### Hallucination Risk

- `low`
- `medium`
- `high`
- `critical`

### Risk Level

- `low`
- `medium`
- `high`
- `critical`

### Review Route

- `standard_review`
- `review_with_notes`
- `senior_review`
- `blocked`

### Approval Policy

- `approval_allowed`
- `approval_requires_notes`
- `approval_blocked_pending_escalation`
- `approval_not_allowed`

## Expected Routing Rules

The expected routing model is:

- low risk → standard review → approval allowed;
- medium risk → review with notes → approval requires notes;
- high risk → senior review → approval blocked pending escalation;
- critical risk → blocked → approval not allowed.

## Risk Escalation Rules

The system should escalate risk when:

- the output is weakly grounded or ungrounded;
- hallucination risk is high or critical;
- unsupported claims are present;
- the output fabricates a source;
- evidence is missing or insufficient;
- the context is sensitive or regulated;
- the output could create business, legal, compliance or reputational harm.

## Critical Risk Rules

An output should be critical risk when it fabricates a source or cites evidence that was not provided.

Critical-risk outputs should be blocked and should not be approved through a standard review path.

## Medium Risk Rules

An output may be medium risk where there is partial grounding, limited evidence or low hallucination risk but insufficient support for confident approval.

Medium-risk outputs should require reviewer notes before approval.

## High Risk Rules

An output should be high risk where weak grounding, high hallucination risk, missing evidence or regulated context makes standard review unsafe.

High-risk outputs should be routed to senior review.

## Low Risk Rules

An output should only be low risk where it is fully grounded, has low hallucination risk, has no unsupported claims and has sufficient supporting evidence.

Low-risk outputs may proceed through standard human review.

## QA Value

This rubric supports an AI Quality Engineering approach that tests not only AI output quality, but also the decision logic used to route outputs through human review workflows.

It helps teams ask:

- is this output safe for standard review?
- does this output require reviewer notes?
- should this output be escalated?
- should this output be blocked?
- does the UI enforce the same route as the risk model?

## Key Principle

Risk triage should be consistent, evidence-based and enforceable at both the data validation layer and the browser workflow layer.