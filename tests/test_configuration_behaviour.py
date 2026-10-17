
import json
from pathlib import Path

import pytest


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "configuration_behaviour_cases.json"
)

VALID_ENVIRONMENTS = {"test", "staging", "production"}

VALID_CONFIGURATION_STATUSES = {
    "valid",
    "missing",
    "invalid",
    "drift_detected",
    "unverified",
}

VALID_FEATURE_FLAGS = {"enabled", "disabled"}

VALID_SECURITY_RISKS = {
    "none", "low", "medium", "high", "critical"
}

VALID_QUALITY_STATUSES = {
    "valid",
    "fallback_required",
    "requires_review",
    "blocked",
}

REQUIRED_FIELDS = {
    "id",
    "scenario",
    "description",
    "environment",
    "configuration_status",
    "feature_flag_status",
    "environment_isolated",
    "safe_default_applied",
    "audit_evidence_present",
    "configuration_drift",
    "security_risk",
    "quality_status",
    "safe_action",
}


@pytest.fixture(scope="module")
def cases():
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_dataset_exists():
    assert DATA_PATH.is_file()


def test_dataset_is_non_empty(cases):
    assert isinstance(cases, list)
    assert len(cases) > 0


def test_all_required_fields_exist(cases):
    for case in cases:
        assert REQUIRED_FIELDS <= set(case), case.get("id")


def test_case_ids_are_unique(cases):
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))


def test_case_ids_follow_experiment_prefix(cases):
    for case in cases:
        assert case["id"].startswith("CDB-")


def test_scenarios_and_descriptions_are_present(cases):
    for case in cases:
        assert isinstance(case["scenario"], str)
        assert case["scenario"].strip()
        assert isinstance(case["description"], str)
        assert case["description"].strip()


def test_environment_values_are_controlled(cases):
    for case in cases:
        assert case["environment"] in VALID_ENVIRONMENTS


def test_configuration_status_values_are_controlled(cases):
    for case in cases:
        assert (
            case["configuration_status"]
            in VALID_CONFIGURATION_STATUSES
        )


def test_feature_flag_values_are_controlled(cases):
    for case in cases:
        assert case["feature_flag_status"] in VALID_FEATURE_FLAGS


def test_security_risk_values_are_controlled(cases):
    for case in cases:
        assert case["security_risk"] in VALID_SECURITY_RISKS


def test_quality_status_values_are_controlled(cases):
    for case in cases:
        assert case["quality_status"] in VALID_QUALITY_STATUSES


def test_boolean_fields_have_correct_types(cases):
    fields = (
        "environment_isolated",
        "safe_default_applied",
        "audit_evidence_present",
        "configuration_drift",
    )

    for case in cases:
        for field in fields:
            assert type(case[field]) is bool, (
                f"{case['id']}: {field} must be boolean"
            )


def test_valid_cases_require_verified_configuration(cases):
    for case in cases:
        if case["quality_status"] == "valid":
            assert case["configuration_status"] == "valid"
            assert case["environment_isolated"] is True
            assert case["audit_evidence_present"] is True
            assert case["configuration_drift"] is False
            assert case["security_risk"] == "none"


def test_valid_cases_do_not_use_safe_default(cases):
    for case in cases:
        if case["quality_status"] == "valid":
            assert case["safe_default_applied"] is False


def test_missing_configuration_uses_safe_fallback(cases):
    for case in cases:
        if case["configuration_status"] == "missing":
            assert case["feature_flag_status"] == "disabled"
            assert case["safe_default_applied"] is True
            assert case["audit_evidence_present"] is True
            assert case["quality_status"] == "fallback_required"


def test_invalid_configuration_is_not_accepted(cases):
    for case in cases:
        if case["configuration_status"] == "invalid":
            assert case["quality_status"] != "valid"


def test_safe_defaults_disable_affected_features(cases):
    for case in cases:
        if case["safe_default_applied"]:
            assert case["feature_flag_status"] == "disabled"
            assert case["environment_isolated"] is True
            assert case["audit_evidence_present"] is True


def test_fallback_status_requires_safe_default(cases):
    for case in cases:
        if case["quality_status"] == "fallback_required":
            assert case["safe_default_applied"] is True
            assert case["feature_flag_status"] == "disabled"


def test_unresolved_drift_requires_review_or_block(cases):
    for case in cases:
        if case["configuration_drift"]:
            assert case["quality_status"] in {
                "requires_review", "blocked"
            }


def test_detected_drift_has_correct_flag(cases):
    for case in cases:
        if case["configuration_status"] == "drift_detected":
            assert case["configuration_drift"] is True
            assert case["quality_status"] == "requires_review"


def test_environment_isolation_failure_blocks(cases):
    for case in cases:
        if not case["environment_isolated"]:
            assert case["quality_status"] == "blocked"
            assert case["security_risk"] in {"high", "critical"}


def test_unverified_activation_without_evidence_blocks(cases):
    for case in cases:
        if (
            case["configuration_status"] == "unverified"
            and case["feature_flag_status"] == "enabled"
            and not case["audit_evidence_present"]
        ):
            assert case["quality_status"] == "blocked"
            assert case["security_risk"] in {"high", "critical"}


def test_critical_risk_is_blocked(cases):
    for case in cases:
        if case["security_risk"] == "critical":
            assert case["quality_status"] == "blocked"


def test_blocked_cases_cannot_be_accepted(cases):
    for case in cases:
        if case["quality_status"] == "blocked":
            assert case["quality_status"] != "valid"
            assert case["security_risk"] in {"high", "critical"}


def test_enabled_features_are_not_accepted_without_evidence(cases):
    for case in cases:
        if (
            case["feature_flag_status"] == "enabled"
            and not case["audit_evidence_present"]
        ):
            assert case["quality_status"] == "blocked"


def test_safe_actions_are_meaningful(cases):
    for case in cases:
        assert isinstance(case["safe_action"], str)
        assert len(case["safe_action"].strip()) >= 50


def test_safe_actions_align_with_quality_decisions(cases):
    expected_words = {
        "valid": ("accept", "verified"),
        "fallback_required": ("safe", "fallback", "default", "fail-safe"),
        "requires_review": ("review", "investigate"),
        "blocked": ("block", "restore"),
    }

    for case in cases:
        action = case["safe_action"].lower()

        assert any(
            word in action
            for word in expected_words[case["quality_status"]]
        ), f"{case['id']}: safe action does not match quality status"


def test_expected_scenarios_are_covered(cases):
    statuses = {case["quality_status"] for case in cases}

    assert statuses == {
        "valid",
        "fallback_required",
        "requires_review",
        "blocked",
    }


def test_environment_coverage(cases):
    environments = {case["environment"] for case in cases}

    assert environments == {
        "test",
        "staging",
        "production",
    }
