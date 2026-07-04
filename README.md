# AI Quality Lab

[![AI Quality Lab Tests](https://github.com/Jorgeomedinamachuca/ai-quality-lab/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/Jorgeomedinamachuca/ai-quality-lab/actions/workflows/playwright-tests.yml)

AI Quality Lab is a personal learning and research laboratory focused on the future of Quality Engineering in the age of Artificial Intelligence.

The project explores how modern QA practices can be adapted to test AI-powered applications, chatbot behaviour and LLM-based features using tools such as Playwright, Python, Pytest and structured evaluation rubrics.

This repository is not intended to demonstrate software development expertise as its primary goal. Its purpose is to build practical, evidence-based experience in AI Quality Engineering through experimentation, automation, documentation and systematic evaluation of intelligent systems.

## Vision

AI Quality Lab investigates how Quality Engineering can evolve when software products become increasingly probabilistic, conversational and AI-assisted.

Traditional test automation remains essential, but AI-powered systems introduce new quality risks:

- non-deterministic responses;
- hallucinated or unsupported claims;
- prompt injection vulnerabilities;
- data leakage risk;
- inconsistent behaviour across repeated runs;
- unclear acceptance criteria for response quality;
- difficulty converting qualitative behaviour into measurable release signals.

This lab is designed to explore those risks from a practical QA perspective.

## Objectives

- Learn Playwright from the perspective of a Quality Engineer.
- Explore how AI can improve QA processes.
- Design practical methodologies for evaluating LLM-based applications.
- Create reusable frameworks for AI-driven testing.
- Document rubrics, test strategies and evaluation techniques.
- Build a public portfolio that reflects a professional transition into AI Quality Engineering.

## Research Areas

- AI-driven testing
- Playwright automation
- Chatbot testing
- LLM evaluation
- Prompt injection testing
- Hallucination detection
- AI security
- Data leakage testing
- Response quality evaluation
- AI-assisted test design
- Intelligent automation
- Modern Quality Engineering

## Philosophy

Every experiment in this lab must answer a real quality question about AI-based systems.

The aim is not to learn tools for their own sake. The aim is to understand how to evaluate the quality, reliability, safety and usefulness of intelligent applications.

Each experiment should produce at least one tangible output:

- reusable code;
- documentation;
- test cases;
- evaluation rubrics;
- technical articles;
- good practices;
- automation examples;
- risk-based testing artefacts.

## What This Project Demonstrates

This repository demonstrates how more than twenty years of Quality Assurance and Quality Engineering experience can be applied to the new generation of AI-powered products.

It shows practical capability across:

- test strategy design;
- exploratory and risk-based thinking;
- Playwright browser automation;
- Python and Pytest test implementation;
- LLM response evaluation;
- AI risk modelling;
- prompt dataset design;
- quality gates and reporting;
- documentation of repeatable QA practices.

## Current Scope

The current version focuses on a foundational AI testing framework with:

- Playwright UI automation examples;
- structured prompt datasets;
- LLM response quality rubrics;
- hallucination and prompt injection test scenarios;
- sample AI test reporting;
- documentation for AI testing strategy.

## Project Structure

```text
ai-quality-lab/
├── README.md
├── pytest.ini
├── requirements.txt
├── tests/
│   ├── test_basic_navigation.py
│   ├── test_ai_chatbot_ui.py
│   └── test_response_quality.py
├── pages/
│   └── chatbot_page.py
├── data/
│   └── test_prompts.json
├── rubrics/
│   └── llm_response_rubric.md
├── reports/
│   └── sample_test_report.md
├── docs/
│   ├── vision.md
│   ├── testing_strategy.md
│   └── ai_testing_notes.md
└── .github/
    └── workflows/
        └── playwright-tests.yml
```

## Technology Stack

- Python
- Pytest
- Playwright
- pytest-playwright
- GitHub Actions
- Markdown documentation

## How to Run Locally

### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
pytest
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install
pytest
```

## Example Test Areas

| Area | Quality Risk | Example Evaluation |
|---|---|---|
| Hallucination | The model invents unsupported facts | Check whether the answer admits uncertainty |
| Prompt injection | The model follows malicious instructions | Check whether hidden instructions are protected |
| Data leakage | The system exposes confidential data | Check whether sensitive-data requests are refused |
| Consistency | Similar prompts produce contradictory answers | Run repeated prompts and compare behaviour |
| Response quality | The answer is unclear or incomplete | Score against an evaluation rubric |
| UX | The chatbot flow is confusing | Validate interaction, feedback and clarity |

## Roadmap

- Add a richer prompt dataset by AI risk category.
- Add automated response scoring helpers.
- Add CSV or JSON report generation.
- Add examples of AI-assisted test case design.
- Add Playwright tests against a real demo chatbot application.
- Add prompt injection and data leakage test suites.
- Add technical write-ups for LinkedIn and portfolio use.
- Add GitHub Actions artefact upload for test reports.

## Professional Positioning

The long-term goal of AI Quality Lab is to become a personal reference point for AI Quality Engineering.

The project is designed to position its author as a Quality Engineering professional capable of connecting established QA experience, automation, AI safety, security awareness and LLM evaluation in order to help teams build more reliable, safer and higher-quality AI products.

## Experiments

### Experiment 001 — Chatbot UI Smoke Test

This experiment validates the basic UI contract of an AI-style chatbot interface using Playwright and Pytest.

It demonstrates how a Quality Engineer can automate the minimum expected behaviour of a chatbot-style interface before introducing deeper LLM response quality evaluation.

Covered behaviours:

- chatbot page loading;
- prompt input visibility;
- send button visibility;
- response panel visibility;
- prompt submission;
- deterministic response rendering;
- empty prompt validation.

Documentation:

- [`docs/experiment_001_chatbot_ui_smoke_test.md`](docs/experiment_001_chatbot_ui_smoke_test.md)

Related files:

- [`demo/chatbot.html`](demo/chatbot.html)
- [`tests/test_demo_chatbot_ui.py`](tests/test_demo_chatbot_ui.py)
