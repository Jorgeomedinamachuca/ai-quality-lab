# Cache Isolation and Freshness Rubric

## Purpose

This rubric defines quality expectations for workflows that use cached enrichment data to improve performance.

The goal is to validate that cached data remains isolated by context, remains fresh enough to be trusted, and falls back safely when cache data is missing, stale, expired, disabled or unsafe.

## Core Quality Principle

Cached data should never be trusted only because it is available.

A reliable cache strategy must preserve context isolation, freshness expectations, audit evidence and safe fallback behaviour.

## Key Quality Criteria

A reliable cache workflow should:

- preserve user and tenant context isolation;
- avoid global cache keys for context-specific data;
- avoid tenant-only cache keys when user-specific data is involved;
- distinguish fresh, stale, expired and unavailable cache states;
- require fallback when cache data is missing, stale, expired or unsafe;
- block cache usage where cross-context leakage is possible;
- preserve audit evidence for cached enrichment data;
- classify stale data and leakage risk separately;
- align quality status with cache safety.

## Controlled Values

### Cache Status

- `hit`
- `miss`
- `expired`
- `disabled`

### Cache Key Scope

- `user_and_tenant`
- `tenant_only`
- `global`
- `disabled`

### Freshness Status

- `fresh`
- `stale`
- `expired`
- `not_applicable`

### Data Leakage Risk

- `none`
- `low`
- `high`
- `critical`

### Stale Data Risk

- `none`
- `medium`

### Quality Status

- `valid`
- `fallback_required`
- `requires_review`
- `blocked`

## Expected Quality Rules

The expected quality model is:

- valid workflows preserve context isolation and do not carry leakage or stale data risk;
- fallback-required workflows use a safe alternative when cache data is missing, expired or intentionally disabled;
- review-required workflows have quality uncertainty, such as stale data or missing audit evidence;
- blocked workflows have unsafe cache isolation or critical leakage risk.

## Context Isolation Rules

Cached enrichment data should be isolated by the appropriate context.

For user-specific or tenant-specific data, the safest scope is:

```text
user_and_tenant
```

The workflow should block when context-specific data is served from:

```text
tenant_only
global
```

unless the data is explicitly non-sensitive, non-user-specific and safe for that scope.

## Freshness Rules

Fresh cache data may be used only when audit evidence is present and context isolation is preserved.

Stale or expired cache data should not be trusted automatically.

A stale cache entry should require review or refresh.

An expired cache entry should use a safe fallback or refresh path.

## Fallback Rules

Fallback is required when:

- the cache misses;
- the cache entry is stale;
- the cache entry is expired;
- cache use is disabled;
- audit evidence is missing;
- cache key scope is unsafe.

Fallback should preserve context isolation and avoid serving unsafe cached data.

## Blocking Rules

The workflow should be blocked when:

- context isolation is false and data leakage risk is high or critical;
- a global cache key is used for context-specific data;
- a tenant-only cache key may expose user-specific data;
- cached data could leak across users, tenants or contexts;
- the quality decision treats unsafe cache isolation as valid.

## Audit Evidence Rules

Cached enrichment data should include enough audit evidence to understand:

- where the cached data came from;
- when it was generated;
- which context it belongs to;
- whether it remains fresh;
- whether fallback or refresh was required.

Freshness should not be trusted when audit evidence is missing.

## QA Value

This rubric supports AI Quality Engineering for systems where cached enrichment, scoring, recommendation, routing or attribution data may influence user-facing decisions.

It helps teams ask:

- is the cache key scoped safely?
- is the cached data fresh enough?
- is the data isolated by user and tenant context?
- is fallback used when cache data is missing or unsafe?
- is stale data reviewed instead of trusted automatically?
- is leakage risk blocked rather than accepted?
- is there enough audit evidence to trust the cached result?

## Key Principle

Caching improves performance only when it does not weaken isolation, freshness, provenance or trust.