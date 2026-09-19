import json
from pathlib import Path


ASYNC_ATTRIBUTION_DATA_PATH = Path("data/async_attribution_recovery_cases.json")

VALID_USER_FACING_RESPONSES = {"fast", "slow"}

VALID_DOWNSTREAM_DEPENDENCY_STATUSES = {
    "available",
    "temporarily_unavailable",
    "slow",
    "failed",
}

VALID_ATTRIBUTION_STATUSES = {
    "completed",
    "deferred",
    "recovered",
    "recovery_failed",
    "lost",
}

VALID_DATA_LOSS_RISKS = {
    "none",
    "low",
    "medium",
    "high",
    "critical",
}

VALID_QUALITY_STATUSES = {
    "valid",
    "recovery_pending",
    "requires_review",
    "blocked",
}


def load_async_attribution_cases():
    with ASYNC_ATTRIBUTION_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_async_attribution_dataset_exists():
    assert ASYNC_ATTRIBUTION_DATA_PATH.exists(), (
        "Async attribution recovery dataset file is missing."
    )


def test_async_attribution_dataset_is_not_empty():
    cases = load_async_attribution_cases()

    assert isinstance(cases, list), "Async attribution dataset must be a list."
    assert len(cases) > 0, "Async attribution dataset must contain at least one case."


def test_each_async_attribution_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "user_facing_response",
        "downstream_dependency_status",
        "attribution_status",
        "deferred_record_created",
        "background_recovery_required",
        "retryable_failure",
        "audit_evidence_present",
        "data_loss_risk",
        "quality_status",
        "safe_action",
    }

    for case in load_async_attribution_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"Async attribution case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_async_attribution_ids_are_unique():
    cases = load_async_attribution_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "Async attribution case IDs must be unique."


def test_controlled_values_are_used():
    for case in load_async_attribution_cases():
        assert case["user_facing_response"] in VALID_USER_FACING_RESPONSES, (
            f"{case['id']} has invalid user-facing response: "
            f"{case['user_facing_response']}"
        )
        assert case["downstream_dependency_status"] in VALID_DOWNSTREAM_DEPENDENCY_STATUSES, (
            f"{case['id']} has invalid downstream dependency status: "
            f"{case['downstream_dependency_status']}"
        )
        assert case["attribution_status"] in VALID_ATTRIBUTION_STATUSES, (
            f"{case['id']} has invalid attribution status: {case['attribution_status']}"
        )
        assert case["data_loss_risk"] in VALID_DATA_LOSS_RISKS, (
            f"{case['id']} has invalid data loss risk: {case['data_loss_risk']}"
        )
        assert case["quality_status"] in VALID_QUALITY_STATUSES, (
            f"{case['id']} has invalid quality status: {case['quality_status']}"
        )


def test_boolean_fields_are_valid_booleans():
    boolean_fields = {
        "deferred_record_created",
        "background_recovery_required",
        "retryable_failure",
        "audit_evidence_present",
    }

    for case in load_async_attribution_cases():
        for field in boolean_fields:
            assert isinstance(case[field], bool), (
                f"{case['id']} {field} must be a boolean."
            )


def test_valid_workflows_have_fast_response_and_completed_or_recovered_attribution():
    for case in load_async_attribution_cases():
        if case["quality_status"] == "valid":
            assert case["user_facing_response"] == "fast", (
                f"{case['id']} valid workflows should keep the user-facing response fast."
            )
            assert case["attribution_status"] in {"completed", "recovered"}, (
                f"{case['id']} valid workflows need completed or recovered attribution."
            )
            assert case["audit_evidence_present"] is True, (
                f"{case['id']} valid workflows require audit evidence."
            )
            assert case["data_loss_risk"] == "none", (
                f"{case['id']} valid workflows should have no data loss risk."
            )


def test_deferred_attribution_requires_deferred_record_and_audit_evidence():
    for case in load_async_attribution_cases():
        if case["attribution_status"] == "deferred":
            assert case["deferred_record_created"] is True, (
                f"{case['id']} deferred attribution requires a deferred record."
            )
            assert case["background_recovery_required"] is True, (
                f"{case['id']} deferred attribution requires background recovery."
            )


def test_recovery_pending_requires_fast_response_and_retryable_failure():
    for case in load_async_attribution_cases():
        if case["quality_status"] == "recovery_pending":
            assert case["user_facing_response"] == "fast", (
                f"{case['id']} recovery-pending workflows should keep the user-facing response fast."
            )
            assert case["deferred_record_created"] is True, (
                f"{case['id']} recovery-pending workflows require deferred records."
            )
            assert case["background_recovery_required"] is True, (
                f"{case['id']} recovery-pending workflows require background recovery."
            )
            assert case["retryable_failure"] is True, (
                f"{case['id']} recovery-pending workflows should remain retryable."
            )
            assert case["audit_evidence_present"] is True, (
                f"{case['id']} recovery-pending workflows require audit evidence."
            )
            assert case["data_loss_risk"] in {"low", "medium"}, (
                f"{case['id']} recovery-pending workflows should not have high or critical data loss risk."
            )


def test_slow_user_facing_response_requires_review():
    for case in load_async_attribution_cases():
        if case["user_facing_response"] == "slow":
            assert case["quality_status"] == "requires_review", (
                f"{case['id']} slow user-facing workflows should require review."
            )
            assert case["data_loss_risk"] in {"medium", "high"}, (
                f"{case['id']} slow workflows should carry medium or high quality risk."
            )


def test_missing_audit_evidence_blocks_deferred_or_lost_attribution():
    for case in load_async_attribution_cases():
        if (
            case["audit_evidence_present"] is False
            and case["attribution_status"] in {"deferred", "lost"}
        ):
            assert case["quality_status"] == "blocked", (
                f"{case['id']} missing audit evidence should block deferred or lost attribution."
            )
            assert case["data_loss_risk"] in {"high", "critical"}, (
                f"{case['id']} missing audit evidence should carry high or critical data loss risk."
            )


def test_lost_attribution_is_blocked_and_critical():
    for case in load_async_attribution_cases():
        if case["attribution_status"] == "lost":
            assert case["quality_status"] == "blocked", (
                f"{case['id']} lost attribution should be blocked."
            )
            assert case["data_loss_risk"] == "critical", (
                f"{case['id']} lost attribution should be critical data loss risk."
            )
            assert case["audit_evidence_present"] is False, (
                f"{case['id']} lost attribution should not claim audit evidence."
            )


def test_recovered_attribution_has_audit_evidence_and_no_data_loss():
    for case in load_async_attribution_cases():
        if case["attribution_status"] == "recovered":
            assert case["deferred_record_created"] is True, (
                f"{case['id']} recovered attribution should have come from a deferred record."
            )
            assert case["audit_evidence_present"] is True, (
                f"{case['id']} recovered attribution requires audit evidence."
            )
            assert case["data_loss_risk"] == "none", (
                f"{case['id']} recovered attribution should have no data loss risk."
            )
            assert case["quality_status"] == "valid", (
                f"{case['id']} recovered attribution should be valid."
            )


def test_failed_recovery_requires_review_and_retryability():
    for case in load_async_attribution_cases():
        if case["attribution_status"] == "recovery_failed":
            assert case["quality_status"] == "requires_review", (
                f"{case['id']} failed recovery should require review."
            )
            assert case["retryable_failure"] is True, (
                f"{case['id']} failed recovery should remain retryable."
            )
            assert case["deferred_record_created"] is True, (
                f"{case['id']} failed recovery should preserve a deferred record."
            )
            assert case["audit_evidence_present"] is True, (
                f"{case['id']} failed recovery should preserve audit evidence."
            )


def test_failed_downstream_dependency_must_preserve_recovery_evidence_or_block():
    for case in load_async_attribution_cases():
        if case["downstream_dependency_status"] == "failed":
            if (
                case["deferred_record_created"] is False
                or case["audit_evidence_present"] is False
            ):
                assert case["quality_status"] == "blocked", (
                    f"{case['id']} failed dependency without recovery evidence should block."
                )
                assert case["data_loss_risk"] == "critical", (
                    f"{case['id']} failed dependency without recovery evidence should be critical."
                )


def test_blocked_workflows_have_high_or_critical_data_loss_risk():
    for case in load_async_attribution_cases():
        if case["quality_status"] == "blocked":
            assert case["data_loss_risk"] in {"high", "critical"}, (
                f"{case['id']} blocked workflows should have high or critical data loss risk."
            )


def test_fast_response_does_not_make_lost_attribution_valid():
    for case in load_async_attribution_cases():
        if (
            case["user_facing_response"] == "fast"
            and case["attribution_status"] == "lost"
        ):
            assert case["quality_status"] == "blocked", (
                f"{case['id']} fast response cannot compensate for lost attribution."
            )


def test_background_recovery_required_has_deferred_record():
    for case in load_async_attribution_cases():
        if case["background_recovery_required"]:
            assert case["deferred_record_created"] is True, (
                f"{case['id']} background recovery requires a deferred record."
            )


def test_safe_actions_are_meaningful():
    for case in load_async_attribution_cases():
        assert len(case["safe_action"].strip()) >= 70, (
            f"{case['id']} safe action is too short or vague."
        )


def test_safe_actions_align_with_quality_status():
    expected_terms_by_status = {
        "valid": {"accept", "completed", "recovered", "evidence"},
        "recovery_pending": {"proceed", "deferred", "recovery", "preserving"},
        "requires_review": {"review", "escalate", "retryable", "dependency"},
        "blocked": {"block", "lost", "audit", "evidence"},
    }

    for case in load_async_attribution_cases():
        safe_action = case["safe_action"].lower()
        expected_terms = expected_terms_by_status[case["quality_status"]]

        assert any(term in safe_action for term in expected_terms), (
            f"{case['id']} safe action should align with quality status "
            f"{case['quality_status']}."
        )
        