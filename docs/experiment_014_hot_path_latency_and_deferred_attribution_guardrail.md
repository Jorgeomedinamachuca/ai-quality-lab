# Experiment 014 — Hot-Path Latency and Deferred Attribution Guardrail

## Purpose

This experiment validates a synthetic product workflow where a user-facing action must remain fast while attribution or audit enrichment may need to be completed asynchronously.

The experiment focuses on the quality risk created when slow downstream dependency work blocks the hot path, and on the safeguards required when attribution is deferred for later recovery.

## Quality Engineering Problem

Modern AI-enabled and data-driven systems often need to record attribution, evidence, audit metadata or enrichment data after a user-facing action.

A quality risk appears when the workflow waits for slow downstream dependency work before responding to the user.

A safer design keeps the user-facing path fast, creates a deferred attribution record when immediate attribution cannot complete, and allows background recovery to reconcile attribution later.

## Experiment Scope

This experiment validates:

- fast user-facing workflow behaviour;
- slow synchronous dependency risk;
- deferred attribution handling;
- background recovery requirements;
- retryable recovery failure;
- preserved audit evidence;
- blocked workflows when attribution is lost;
- alignment between data loss risk and quality status.

## Out of Scope

This experiment does not model any real product, endpoint, company workflow, production issue or internal system.

All scenarios, names and test data are synthetic.

The experiment does not test real infrastructure, real queues, real databases, real email tracking, real redirects or real customer data.

## Dataset

The dataset is stored in:

```text
data/async_attribution_recovery_cases.json
