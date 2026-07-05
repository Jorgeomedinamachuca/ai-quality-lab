# QA Test Case Generator Skill

## Purpose

This skill helps generate structured QA test cases from a user story, acceptance criteria or product requirement.

It is designed for Quality Engineers who need to transform requirements into clear, risk-aware and reusable test scenarios.

## When to Use This Skill

Use this skill when the user provides:

- a user story
- acceptance criteria
- a product requirement
- a feature description
- a bug fix description
- a change request

## Expected Input

The input should include at least one of the following:

- user story
- business rule
- acceptance criteria
- expected behaviour
- known constraints
- risk areas

Example input:

As a registered user,
I want to reset my password,
So that I can regain access to my account if I forget it.

## Expected Output

The output should include:

- test case ID
- test title
- preconditions
- test steps
- expected result
- priority
- risk level
- test type
- notes or assumptions

## Output Format

The output should use a structured test case table with these columns:

ID | Test Scenario | Preconditions | Steps | Expected Result | Priority | Risk Level | Test Type

## Quality Rules

Generated test cases should be:

- clear
- traceable to the requirement
- specific enough to execute
- risk-aware
- readable by QA, developers and product stakeholders
- free from unnecessary implementation assumptions
- suitable for manual or automated testing analysis

## Safety and Reliability Rules

The skill must not:

- invent business rules not present in the requirement
- assume hidden system behaviour without stating it as an assumption
- produce unsafe or harmful testing instructions
- expose personal data
- include credentials, secrets or private information
- claim full coverage when the requirement is incomplete

If the requirement is ambiguous, the skill should:

- state the ambiguity
- list assumptions
- suggest clarification questions
- still provide useful initial test scenarios where appropriate

## Example

Input:

As a registered user,
I want to reset my password using my email address,
So that I can regain access to my account.

Expected output should include scenarios for:

- valid password reset request
- unregistered email address
- invalid email format
- expired reset link
- password policy validation
- repeated reset requests
- security messaging
- accessibility and usability checks

## QA Perspective

This skill is not intended to replace a QA Engineer. It is intended to support test design by generating an initial structured set of scenarios that can be reviewed, refined and risk-assessed by a human QA professional.
