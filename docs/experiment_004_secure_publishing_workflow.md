# Experiment 004 — Secure Publishing Workflow

## Purpose

This experiment simulates a small SaaS-style publishing workflow and validates it with Playwright and Pytest.

The aim is to demonstrate how a Quality Engineer can test realistic product behaviour without using proprietary data, private business rules or company-specific implementation details.

## Quality Question

How can a Quality Engineer validate that a content item moves safely from draft to publish without workflow, validation, permission or safe-rendering defects?

## Scope

This experiment covers:

- draft creation
- content preview
- submit for review
- publish workflow
- required field validation
- role-based publish permissions
- safe rendering of potentially unsafe content

## Out of Scope

This experiment does not cover:

- a real backend
- authentication
- real user accounts
- production data
- company-specific business logic
- proprietary content workflows
- database persistence

## Test Design

The experiment uses a controlled HTML demo page and Playwright automation.

The tests validate that:

1. an author can save a draft
2. an author can submit content for review
3. an author cannot publish content
4. an editor can publish content after review submission
5. title is required
6. body is required
7. script-like input is rendered as text and not executable HTML

## QA Value

This experiment demonstrates how a real-world SaaS workflow can be abstracted into a safe, synthetic and testable scenario.

It combines:

- functional workflow testing
- regression testing
- role-based access thinking
- validation testing
- basic security-oriented UI testing
- Playwright Page Object Model

## Ethical Boundary

This experiment is intentionally generic.

It does not use:

- real company data
- real customer data
- proprietary workflows
- internal product names
- screenshots from any employer system
- confidential defects or implementation details

The goal is to show transferable QA thinking, not to reproduce a private product.

## Tools

- Playwright
- Pytest
- Python
- HTML
- JavaScript
- GitHub Actions

## Evidence

The test suite can be executed locally or through GitHub Actions.

Expected command:

pytest

Expected outcome:

All secure publishing workflow tests pass.

## Related Files

- demo/publishing_workflow.html
- pages/publishing_workflow_page.py
- tests/test_secure_publishing_workflow.py
