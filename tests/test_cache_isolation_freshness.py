import json
from pathlib import Path


CACHE_ISOLATION_DATA_PATH = Path("data/cache_isolation_freshness_cases.json")

VALID_CACHE_STATUSES = {
    "hit",
    "miss",
    "expired",
    "disabled",
}

VALID_CACHE_KEY_SCOPES = {
    "user_and_tenant",
    "tenant_only",
    "global",
    "disabled",
}

VALID_FRESHNESS_STATUSES = {
    "fresh",
    "stale",
    "expired",
    "not_applicable",
}

VALID_DATA_LEAKAGE_RISKS = {
    "none",
    "low",
    "high",
    "critical",
}

VALID_STALE_DATA_RISKS = {
    "none",
    "medium",
}

VALID_QUALITY_STATUSES = {
    "valid",
    "fallback_required",
    "requires_review",
    "blocked",
}


def load_cache_isolation_cases():
    with CACHE_ISOLATION_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_cache_isolation_dataset_exists():
    assert CACHE_ISOLATION_DATA_PATH.exists(), (
        "Cache isolation and freshness dataset file is missing."
    )


def test_cache_isolation_dataset_is_not_empty():
    cases = load_cache_isolation_cases()

    assert isinstance(cases, list), "Cache isolation dataset must be a list."
    assert len(cases) > 0, "Cache isolation dataset must contain at least one case."


def test_each_cache_isolation_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "cache_status",
        "context_isolated",
        "cache_key_scope",
        "freshness_status",
        "fallback_required",
        "data_leakage_risk",
        "stale_data_risk",
        "audit_evidence_present",
        "quality_status",
        "safe_action",
    }

    for case in load_cache_isolation_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"Cache isolation case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_cache_isolation_ids_are_unique():
    cases = load_cache_isolation_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "Cache isolation case IDs must be unique."


def test_controlled_values_are_used():
    for case in load_cache_isolation_cases():
        assert case["cache_status"] in VALID_CACHE_STATUSES, (
            f"{case['id']} has invalid cache status: {case['cache_status']}"
        )
        assert case["cache_key_scope"] in VALID_CACHE_KEY_SCOPES, (
            f"{case['id']} has invalid cache key scope: {case['cache_key_scope']}"
        )
        assert case["freshness_status"] in VALID_FRESHNESS_STATUSES, (
            f"{case['id']} has invalid freshness status: {case['freshness_status']}"
        )
        assert case["data_leakage_risk"] in VALID_DATA_LEAKAGE_RISKS, (
            f"{case['id']} has invalid data leakage risk: {case['data_leakage_risk']}"
        )
        assert case["stale_data_risk"] in VALID_STALE_DATA_RISKS, (
            f"{case['id']} has invalid stale data risk: {case['stale_data_risk']}"
        )
        assert case["quality_status"] in VALID_QUALITY_STATUSES, (
            f"{case['id']} has invalid quality status: {case['quality_status']}"
        )


def test_boolean_fields_are_valid_booleans():
    boolean_fields = {
        "context_isolated",
        "fallback_required",
        "audit_evidence_present",
    }

    for case in load_cache_isolation_cases():
        for field in boolean_fields:
            assert isinstance(case[field], bool), (
                f"{case['id']} {field} must be a boolean."
            )


def test_valid_cache_workflows_are_isolated_and_low_risk():
    for case in load_cache_isolation_cases():
        if case["quality_status"] == "valid":
            assert case["context_isolated"] is True, (
                f"{case['id']} valid cache workflows must preserve context isolation."
            )
            assert case["data_leakage_risk"] == "none", (
                f"{case['id']} valid cache workflows must not carry leakage risk."
            )
            assert case["stale_data_risk"] == "none", (
                f"{case['id']} valid cache workflows must not carry stale data risk."
            )
            assert case["audit_evidence_present"] is True, (
                f"{case['id']} valid cache workflows require audit evidence."
            )


def test_fresh_cache_hit_requires_context_isolation_and_audit_evidence():
    for case in load_cache_isolation_cases():
        if case["cache_status"] == "hit" and case["freshness_status"] == "fresh":
            if case["quality_status"] == "valid":
                assert case["context_isolated"] is True, (
                    f"{case['id']} valid fresh cache hits require context isolation."
                )
                assert case["cache_key_scope"] == "user_and_tenant", (
                    f"{case['id']} valid fresh cache hits should use user_and_tenant scope."
                )
                assert case["audit_evidence_present"] is True, (
                    f"{case['id']} valid fresh cache hits require audit evidence."
                )


def test_cache_miss_requires_safe_fallback():
    for case in load_cache_isolation_cases():
        if case["cache_status"] == "miss":
            assert case["fallback_required"] is True, (
                f"{case['id']} cache misses should require fallback."
            )
            assert case["quality_status"] == "fallback_required", (
                f"{case['id']} cache misses should be marked fallback_required."
            )
            assert case["freshness_status"] == "not_applicable", (
                f"{case['id']} cache misses should have not_applicable freshness."
            )


def test_stale_cache_requires_review_or_fallback():
    for case in load_cache_isolation_cases():
        if case["freshness_status"] == "stale":
            assert case["fallback_required"] is True, (
                f"{case['id']} stale cache entries should require fallback or refresh."
            )
            assert case["quality_status"] == "requires_review", (
                f"{case['id']} stale cache entries should require review."
            )
            assert case["stale_data_risk"] == "medium", (
                f"{case['id']} stale cache entries should carry stale data risk."
            )


def test_expired_cache_uses_fallback_required_status():
    for case in load_cache_isolation_cases():
        if case["cache_status"] == "expired":
            assert case["freshness_status"] == "expired", (
                f"{case['id']} expired cache entries should have expired freshness."
            )
            assert case["fallback_required"] is True, (
                f"{case['id']} expired cache entries should require fallback."
            )
            assert case["quality_status"] == "fallback_required", (
                f"{case['id']} expired cache entries should use fallback_required status."
            )


def test_disabled_cache_preserves_safe_direct_lookup():
    for case in load_cache_isolation_cases():
        if case["cache_status"] == "disabled":
            assert case["cache_key_scope"] == "disabled", (
                f"{case['id']} disabled cache should use disabled cache key scope."
            )
            assert case["freshness_status"] == "not_applicable", (
                f"{case['id']} disabled cache should have not_applicable freshness."
            )
            assert case["context_isolated"] is True, (
                f"{case['id']} disabled cache workflows should still preserve isolation."
            )


def test_unsafe_cache_key_scope_is_blocked():
    unsafe_scopes = {"tenant_only", "global"}

    for case in load_cache_isolation_cases():
        if case["cache_key_scope"] in unsafe_scopes:
            assert case["context_isolated"] is False, (
                f"{case['id']} unsafe cache key scope should not be context isolated."
            )
            assert case["quality_status"] == "blocked", (
                f"{case['id']} unsafe cache key scope should be blocked."
            )
            assert case["data_leakage_risk"] in {"high", "critical"}, (
                f"{case['id']} unsafe cache key scope should carry high or critical leakage risk."
            )


def test_global_cache_key_for_context_specific_data_is_critical():
    for case in load_cache_isolation_cases():
        if case["cache_key_scope"] == "global":
            assert case["quality_status"] == "blocked", (
                f"{case['id']} global cache key usage should be blocked."
            )
            assert case["data_leakage_risk"] == "critical", (
                f"{case['id']} global cache key usage should be critical leakage risk."
            )
            assert case["fallback_required"] is True, (
                f"{case['id']} global cache key usage should require fallback."
            )


def test_missing_audit_evidence_requires_review_or_blocking():
    for case in load_cache_isolation_cases():
        if case["audit_evidence_present"] is False:
            assert case["quality_status"] in {"requires_review", "blocked"}, (
                f"{case['id']} missing audit evidence should require review or blocking."
            )
            assert case["fallback_required"] is True, (
                f"{case['id']} missing audit evidence should require fallback or refresh."
            )


def test_blocked_workflows_have_leakage_risk():
    for case in load_cache_isolation_cases():
        if case["quality_status"] == "blocked":
            assert case["data_leakage_risk"] in {"high", "critical"}, (
                f"{case['id']} blocked cache workflows should carry high or critical leakage risk."
            )
            assert case["fallback_required"] is True, (
                f"{case['id']} blocked cache workflows should require fallback."
            )


def test_fallback_required_status_has_fallback_enabled():
    for case in load_cache_isolation_cases():
        if case["quality_status"] == "fallback_required":
            assert case["fallback_required"] is True, (
                f"{case['id']} fallback_required status should have fallback_required=true."
            )


def test_stale_data_risk_requires_non_fresh_status_or_missing_evidence():
    for case in load_cache_isolation_cases():
        if case["stale_data_risk"] == "medium":
            assert (
                case["freshness_status"] in {"stale", "expired"}
                or case["audit_evidence_present"] is False
            ), (
                f"{case['id']} stale data risk should be linked to stale, expired or unaudited cache data."
            )


def test_non_isolated_cache_cannot_be_valid():
    for case in load_cache_isolation_cases():
        if case["context_isolated"] is False:
            assert case["quality_status"] != "valid", (
                f"{case['id']} non-isolated cache workflows cannot be valid."
            )


def test_safe_actions_are_meaningful():
    for case in load_cache_isolation_cases():
        assert len(case["safe_action"].strip()) >= 70, (
            f"{case['id']} safe action is too short or vague."
        )


def test_safe_actions_align_with_quality_status():
    expected_terms_by_status = {
        "valid": {"accept", "fresh", "isolation", "direct"},
        "fallback_required": {"fallback", "refresh", "safe", "proceed"},
        "requires_review": {"review", "stale", "audit", "freshness"},
        "blocked": {"block", "leak", "global", "context"},
    }

    for case in load_cache_isolation_cases():
        safe_action = case["safe_action"].lower()
        expected_terms = expected_terms_by_status[case["quality_status"]]

        assert any(term in safe_action for term in expected_terms), (
            f"{case['id']} safe action should align with quality status "
            f"{case['quality_status']}."
        )