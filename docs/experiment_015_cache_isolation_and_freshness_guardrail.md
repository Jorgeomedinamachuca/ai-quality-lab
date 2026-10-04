# Experiment 015 — Cache Isolation and Freshness Guardrail

## Purpose

This experiment validates a synthetic product workflow where cached enrichment data is used to improve performance.

The experiment focuses on the quality risks created when cached data is stale, incorrectly scoped, missing audit evidence, or unsafe to serve across user or tenant contexts.

## Quality Engineering Problem

Caching can improve performance, but it can also introduce serious quality and security risks.

A cached result should not be trusted only because it is available. It must also be fresh, isolated to the correct context, supported by audit evidence, and safe to use.

A quality risk appears when cached enrichment data is served from an unsafe key scope, reused across contexts, treated as fresh without evidence, or accepted when fallback should be required.

## Experiment Scope

This experiment validates:

- fresh cache hits;
- cache misses;
- stale cache entries;
- expired cache entries;
- disabled cache behaviour;
- user and tenant context isolation;
- unsafe cache key scopes;
- missing audit evidence;
- safe fallback and refresh behaviour;
- blocked workflows when leakage risk is high or critical.

## Out of Scope

This experiment does not model any real product, production issue, company workflow, internal system or customer data.

All scenarios, names and test data are synthetic.

The experiment does not test real cache infrastructure, real databases, real tenants, real users or real production traffic.

## Dataset

The dataset is stored in:

```text
data/cache_isolation_freshness_cases.json
```

The dataset contains synthetic cache safety cases covering:

- fresh isolated cache hit;
- cache miss with safe fallback;
- stale cache entry;
- tenant-only cache key risk;
- global cache key risk;
- fresh cache entry without audit evidence;
- expired cache entry;
- disabled cache with direct lookup.

## Rubric

The rubric is stored in:

```text
rubrics/cache_isolation_freshness_rubric.md
```

The rubric defines controlled values for:

- cache status;
- cache key scope;
- freshness status;
- data leakage risk;
- stale data risk;
- quality status.

It also defines expected quality rules for valid, fallback-required, review-required and blocked cache workflows.

## Python Validation

The Python validation is stored in:

```text
tests/test_cache_isolation_freshness.py
```

The Python tests validate that:

- the dataset exists and is not empty;
- all required fields are present;
- case IDs are unique;
- controlled values are used consistently;
- boolean fields are valid booleans;
- valid cache workflows preserve isolation and audit evidence;
- fresh cache hits require context isolation;
- cache misses require fallback;
- stale cache entries require review or fallback;
- expired cache entries use fallback-required status;
- disabled cache preserves safe direct lookup;
- unsafe cache key scopes are blocked;
- global cache keys for context-specific data are critical;
- missing audit evidence requires review or blocking;
- blocked workflows carry leakage risk;
- stale data risk is linked to stale, expired or unaudited data;
- non-isolated cache workflows cannot be valid;
- safe actions align with the quality status.

## Browser Workflow Validation

The browser demo is stored in:

```text
demo/cache_isolation_freshness_dashboard.html
```

The TypeScript Playwright tests are stored in:

```text
tests-ts/cache-isolation-freshness-dashboard.spec.ts
```

The browser layer validates that:

- cache case controls are visible;
- fresh isolated cache hits can be accepted;
- cache misses are routed to fallback;
- stale cache entries are routed to review;
- tenant-only cache key usage is blocked;
- global cache key usage is blocked;
- missing audit evidence is routed to review;
- expired cache entries are routed to fallback;
- disabled cache can be accepted when direct lookup preserves isolation;
- dashboard values update when the selected case changes.

## Quality Status Model

The experiment uses four quality statuses:

| Status | Meaning |
|---|---|
| `valid` | The cache workflow preserves isolation, freshness expectations and audit evidence. |
| `fallback_required` | The cache cannot be used directly and a safe fallback or refresh path is required. |
| `requires_review` | The cache workflow has quality uncertainty, such as stale data or missing audit evidence. |
| `blocked` | Cache usage is unsafe because isolation is broken or leakage risk is high or critical. |

## Senior QA Value

This experiment demonstrates cache-aware quality engineering.

It validates that performance optimisation does not weaken data isolation, freshness, provenance or trust.

The experiment is useful for AI Quality Engineering because AI-enabled systems often depend on cached enrichment, scoring, recommendation, routing, attribution or evidence data.

A mature QA strategy must validate both:

- the performance benefit of cache usage;
- the correctness and safety of cached data usage.

## Risk-Based Testing Perspective

The key risks tested are:

- cached data leaking across users, tenants or contexts;
- global cache keys being used for context-specific data;
- tenant-only cache keys being used for user-specific data;
- stale cache entries being trusted automatically;
- expired cache entries being served directly;
- missing audit evidence being ignored;
- fallback not being triggered when cache data is unsafe;
- unsafe cache isolation being treated as valid.

## Additional Suite Stabilisation

During this experiment, two earlier tests were updated to remove dependency on an external website.

The updated tests now use local synthetic fixtures instead of `example.com`, which makes the Python suite more deterministic and less dependent on network or third-party page behaviour.

Updated files:

```text
tests/test_ai_chatbot_ui.py
tests/test_basic_navigation.py
```

## Result

The experiment adds a synthetic quality gate for cache isolation and freshness.

It combines:

- JSON-based test data;
- a written quality rubric;
- Python/Pytest validation;
- a browser-based synthetic dashboard;
- TypeScript/Playwright workflow testing;
- improved deterministic behaviour in earlier browser-driven Python tests.

## Related Files

```text
data/cache_isolation_freshness_cases.json
rubrics/cache_isolation_freshness_rubric.md
tests/test_cache_isolation_freshness.py
demo/cache_isolation_freshness_dashboard.html
tests-ts/cache-isolation-freshness-dashboard.spec.ts
docs/experiment_015_cache_isolation_and_freshness_guardrail.md
tests/test_ai_chatbot_ui.py
tests/test_basic_navigation.py
```