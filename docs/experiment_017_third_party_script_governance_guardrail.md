
# Experiment 017 — Third-Party Script Governance Guardrail

## Purpose

This experiment evaluates third-party script governance using entirely synthetic scenarios and risk-based quality controls.

It focuses on script authorisation, source allowlisting, integrity verification, environment isolation, audit evidence and safe execution decisions.

## Quality Engineering Problem

Third-party scripts can introduce software supply chain, privacy, security and operational risks.

A script must not be considered safe solely because its source is recognised or its execution has been requested.

Quality Engineering must validate the evidence supporting execution decisions, including authorisation, source approval, integrity and environmental boundaries.

## Experiment Scope

The experiment covers:

- Approved scripts with verified integrity
- Unapproved script sources
- Integrity verification mismatches
- Missing audit evidence
- Intentionally disabled scripts
- Environment isolation failures
- Pending script approval
- Approved scripts without execution requests
- Unverified script integrity

All scenarios and decisions are synthetic.

## Quality Decision Model

| Quality status | Expected behaviour |
|---|---|
| `valid` | Accept a verified governance decision; execution is permitted only when all required controls are satisfied |
| `requires_review` | Keep execution denied and require review |
| `blocked` | Prevent execution approval due to failed security controls |

## Python Quality Gates

The Python/Pytest layer validates:

- Dataset existence and structure
- Mandatory fields and unique scenario identifiers
- Controlled values and boolean integrity
- Script authorisation requirements
- Source allowlisting
- Integrity verification
- Environment isolation
- Audit evidence requirements
- Pending approval and disabled states
- Execution request consistency
- Security risk classification
- Quality decision consistency
- Meaningful safe actions
- Environment and quality status coverage

## Browser Workflow Validation

The TypeScript/Playwright layer validates:

- Nine selectable synthetic governance scenarios
- Visibility of script governance attributes
- Acceptance of authorised, verified decisions
- Blocking of unapproved sources
- Blocking of integrity mismatches
- Review routing for missing audit evidence
- Safe handling of intentionally disabled scripts
- Blocking of environment isolation failures
- Pending approval review controls
- Safe handling of scripts without execution requests
- Blocking of unverified integrity
- Reset of notes and decisions when switching scenarios

## Validation Results

Local validation completed successfully:

- Experiment 017 Python/Pytest: 31 passed
- Complete Python/Pytest suite: 263 passed
- Experiment 017 TypeScript/Playwright: 11 passed
- Complete TypeScript/Playwright suite: 63 passed

These results reflect local execution.

## Senior QA and AI Quality Engineering Value

This experiment extends the AI Quality Lab into software supply chain risk and third-party dependency governance.

It demonstrates risk-based validation of security-relevant decisions, including:

- Preventing unauthorised execution
- Separating source approval from integrity verification
- Preserving authorisation evidence
- Enforcing review and blocking decisions
- Maintaining environment-specific controls
- Applying fail-safe governance rules

Such safeguards are relevant to AI-enabled web applications that integrate third-party dependencies.

## Scope and Limitations

The experiment evaluates a controlled JSON dataset and a simulated browser governance dashboard.

It does not execute third-party scripts or independently enforce script blocking.

No external script requests, real supplier integrations, production configurations or customer data are used.

The tests do not establish real Content Security Policy (CSP), Subresource Integrity (SRI) or network-layer enforcement.

A future experiment could test actual browser enforcement using isolated, synthetic fixtures.

## Confidentiality and Synthetic Data

All scenarios, script attributes, environments and execution decisions are fictional.

No identifiable company tickets, proprietary implementations, internal workflows or production data are represented.

## Related Files

- `data/third_party_script_cases.json`
- `rubrics/third_party_script_governance_rubric.md`
- `tests/test_third_party_script_governance.py`
- `demo/third_party_script_dashboard.html`
- `tests-ts/third-party-script-dashboard.spec.ts`
- `docs/experiment_017_third_party_script_governance_guardrail.md`

## Conclusion

Experiment 017 provides a repeatable synthetic quality assessment for third-party script governance.

It combines declarative Python quality gates with browser workflow automation to evaluate script authorisation, integrity, evidence and risk-based approval decisions.
