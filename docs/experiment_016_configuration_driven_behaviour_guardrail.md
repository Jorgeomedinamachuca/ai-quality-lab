
# Experiment 016 — Configuration-Driven Behaviour Guardrail

## Purpose

This experiment evaluates configuration-driven behaviour in a synthetic product workflow.

It focuses on feature flag consistency, configuration drift, environment isolation, fail-safe defaults, audit evidence and risk-based quality decisions.

## Quality Engineering Problem

Configuration changes can introduce functional inconsistencies, security risks and unexpected behaviour without requiring changes to application code.

A configuration may appear technically valid while being applied to the wrong environment, lacking audit evidence or enabling a feature without authorisation.

Quality Engineering must therefore evaluate both configuration correctness and the safety of the resulting behaviour.

## Experiment Scope

The experiment covers:

- Verified configuration states
- Intentionally disabled features
- Missing configuration with safe defaults
- Configuration drift
- Cross-environment configuration contamination
- Unverified feature activation
- Invalid configuration with safe fallback
- Resolved configuration drift

All scenarios use synthetic data.

## Quality Decision Model

| Quality status | Expected behaviour |
|---|---|
| `valid` | Verified configuration may be accepted |
| `fallback_required` | A safe fallback must be selected |
| `requires_review` | Configuration must be reviewed |
| `blocked` | Unsafe configuration cannot be approved |

## Python Quality Gates

The Python/Pytest layer checks:

- Dataset structure and mandatory fields
- Controlled configuration values
- Unique scenario identifiers
- Boolean field integrity
- Environment isolation
- Feature flag consistency
- Safe default enforcement
- Configuration drift handling
- Audit evidence requirements
- Security risk classification
- Quality status consistency
- Safe action alignment
- Scenario and environment coverage

The tests evaluate declarative quality rules against synthetic scenario data.

## Browser Workflow Validation

The TypeScript/Playwright layer validates:

- Configuration scenario selection
- Displayed configuration attributes
- Approval of verified configurations
- Acceptance of intentionally disabled features
- Mandatory notes for fallback, review and blocking
- Review routing for unresolved configuration drift
- Blocking of cross-environment contamination
- Blocking of unverified feature activation
- Safe fallback for invalid configurations
- Acceptance of verified drift remediation
- Reset of review notes and workflow decisions when switching scenarios

## Validation Results

Local validation completed successfully:

- Python/Pytest: 232 passed (entire Python suite)
- TypeScript/Playwright: 52 passed (entire browser suite)
- Experiment 016: 29 Python tests and 10 Playwright tests

These results reflect local execution of the synthetic test suites.

## Senior QA and AI Quality Engineering Value

This experiment demonstrates a shift-left approach to configuration quality.

It extends AI Quality Engineering beyond response evaluation into operational safeguards surrounding AI-enabled applications.

Configuration-driven systems can influence:

- AI feature availability
- Model selection and routing
- Evaluation settings
- Human review requirements
- Security controls
- Environment-specific behaviour

Validating configuration integrity helps prevent unsafe feature activation and inconsistent behaviour.

## Limitations

This experiment does not connect to a real configuration service, feature flag platform or production system.

The dashboard simulates quality decisions and does not apply infrastructure changes.

The tests validate the dataset rules and simulated UI behaviour. They do not prove real-world configuration propagation, environment isolation or authorisation enforcement.

## Confidentiality and Synthetic Data

All scenarios, configurations, environments and results are synthetic.

No real company systems, internal tickets, client information, production configurations or proprietary implementation details are represented.

## Related Files

- `data/configuration_behaviour_cases.json`
- `rubrics/configuration_behaviour_rubric.md`
- `tests/test_configuration_behaviour.py`
- `demo/configuration_behaviour_dashboard.html`
- `tests-ts/configuration-behaviour-dashboard.spec.ts`
- `docs/experiment_016_configuration_driven_behaviour_guardrail.md`

## Conclusion

The experiment provides a repeatable, risk-based quality assessment for configuration-driven behaviour.

It demonstrates how configuration provenance, environment isolation and fail-safe decisions can be evaluated using Python quality gates and browser workflow automation.
