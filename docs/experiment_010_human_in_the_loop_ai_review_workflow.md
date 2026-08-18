# Experiment 010 — Human-in-the-Loop AI Review Workflow

## Objective

This experiment validates a browser-based human review workflow for AI-generated outputs.

The goal is to ensure that AI outputs are not approved automatically when they are weakly grounded, high risk or require human judgement.

## Why This Matters

AI-powered products often generate recommendations, summaries, suggested actions or professional profile insights.

Even when AI output sounds plausible, it may still require human review before it is used in a product or business workflow.

This experiment tests a simple human-in-the-loop review interface where reviewers can approve, reject or request changes to an AI-generated output.

## Files

- `demo/ai_review_workflow.html`
- `tests-ts/ai-review-workflow.spec.ts`
- `playwright.config.ts`
- `tsconfig.json`
- `package.json`

## Quality Risks Covered

This experiment covers:

- approving AI output without evidence review;
- approving weakly grounded AI output;
- approving high hallucination-risk output;
- rejecting output without review notes;
- requesting changes without review notes;
- missing visibility of the evidence panel;
- missing visibility of review controls;
- lack of clear workflow status after reviewer action.

## Test Strategy

The Playwright TypeScript tests validate that:

- the AI output, evidence and review controls are visible;
- fully grounded low-risk AI output can be approved;
- weakly grounded AI output blocks approval;
- high hallucination-risk output blocks approval;
- rejection requires review notes;
- requesting changes requires review notes.

## QA Value

This experiment demonstrates browser automation for an AI assurance workflow.

It complements the Python-based AI quality gates by testing the product layer where human reviewers interact with AI-generated content.

The experiment separates two testing layers:

- Python/Pytest for AI quality gates, datasets, rubrics and evidence validation;
- TypeScript/Playwright for browser automation and human review workflow testing.

## Key Learning

AI quality is not only about the model output.

A robust AI product also needs workflow controls that prevent unsafe or weakly grounded outputs from being approved without appropriate human review.