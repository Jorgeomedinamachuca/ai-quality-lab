# AI Testing Strategy

AI Quality Lab treats AI-powered features as product features that require structured Quality Engineering.

AI testing should combine conventional test automation with risk-based assessment of probabilistic behaviour. A chatbot may function correctly from a UI perspective while still producing unsafe, inconsistent or low-quality responses.

## Strategic Test Areas

1. Functional behaviour
2. Output quality
3. Consistency and repeatability
4. Hallucination risk
5. Prompt injection resistance
6. Data leakage risk
7. User experience
8. Latency and performance
9. Regression testing
10. Acceptance criteria and release gates

## QA Approach

- Start with real user journeys.
- Identify AI-specific quality risks.
- Define expected behaviour before execution.
- Create prompt datasets by risk category.
- Execute tests across repeated runs where relevant.
- Evaluate outputs using structured rubrics.
- Record failures, patterns and uncertainty.
- Convert findings into product risks and release recommendations.

## Risk-Based Questions

- What could the model say that would damage user trust?
- What unsupported claims could create business, legal or reputational risk?
- What sensitive data must never be exposed?
- What instructions should the model refuse?
- What behaviour should remain stable across repeated runs?
- What level of response quality is acceptable for release?

## Quality Gates

A release should not pass AI quality evaluation if:

- the system exposes confidential or sensitive information;
- the system follows prompt injection instructions;
- hallucinated facts appear in business-critical flows;
- the response is materially misleading;
- the model refuses valid user requests without justification;
- the UX gives users no clear path to recover from failure.
