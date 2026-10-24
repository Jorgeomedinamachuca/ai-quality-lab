
import json
from pathlib import Path

import pytest


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "third_party_script_cases.json"
)

REQUIRED_FIELDS = {
    "id",
    "scenario",
    "description",
    "environment",
    "script_status",
    "source_allowlisted",
    "integrity_status",
    "execution_requested",
    "execution_allowed",
    "environment_isolated",
    "audit_evidence_present",
    "security_risk",
    "quality_status",
    "safe_action",
}

VALID_ENVIRONMENTS = {"test", "staging", "production"}

VALID_SCRIPT_STATUSES = {
    "approved",
    "unapproved",
    "pending_review",
    "disabled",
}

VALID_INTEGRITY_STATUSES = {
    "verified",
    "unverified",
    "mismatch",
}

VALID_SECURITY_RISKS = {
    "none",
    "medium",
    "high",
    "critical",
}

VALID_QUALITY_STATUSES = {
    "valid",
    "requires_review",
    "blocked",
}

BOOLEAN_FIELDS = {
    "source_allowlisted",
    "execution_requested",
    "execution_allowed",
    "environment_isolated",
    "audit_evidence_present",
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


def test_all_cases_have_required_fields(cases):
    for case in cases:
        assert REQUIRED_FIELDS <= set(case), case.get("id")


def test_scenario_ids_are_unique(cases):
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids))


def test_ids_follow_experiment_prefix(cases):
    for case in cases:
        assert case["id"].startswith("TPS-")


def test_scenarios_have_meaningful_descriptions(cases):
    for case in cases:
        assert isinstance(case["scenario"], str)
        assert case["scenario"].strip()
        assert isinstance(case["description"], str)
        assert len(case["description"].strip()) >= 30


def test_environment_values_are_controlled(cases):
    for case in cases:
        assert case["environment"] in VALID_ENVIRONMENTS


def test_script_status_values_are_controlled(cases):
    for case in cases:
        assert case["script_status"] in VALID_SCRIPT_STATUSES


def test_integrity_status_values_are_controlled(cases):
    for case in cases:
        assert case["integrity_status"] in VALID_INTEGRITY_STATUSES


def test_security_risk_values_are_controlled(cases):
    for case in cases:
        assert case["security_risk"] in VALID_SECURITY_RISKS


def test_quality_status_values_are_controlled(cases):
    for case in cases:
        assert case["quality_status"] in VALID_QUALITY_STATUSES


def test_boolean_fields_have_correct_types(cases):
    for case in cases:
        for field in BOOLEAN_FIELDS:
            assert type(case[field]) is bool, (
                f"{case['id']}: {field} must be a boolean"
            )


def test_execution_requires_all_security_controls(cases):
    for case in cases:
        if case["execution_allowed"]:
            assert case["script_status"] == "approved"
            assert case["source_allowlisted"] is True
            assert case["integrity_status"] == "verified"
            assert case["execution_requested"] is True
            assert case["environment_isolated"] is True
            assert case["audit_evidence_present"] is True
            assert case["security_risk"] == "none"
            assert case["quality_status"] == "valid"


def test_fully_authorised_execution_request_is_allowed(cases):
    for case in cases:
        authorised = (
            case["script_status"] == "approved"
            and case["source_allowlisted"] is True
            and case["integrity_status"] == "verified"
            and case["execution_requested"] is True
            and case["environment_isolated"] is True
            and case["audit_evidence_present"] is True
            and case["security_risk"] == "none"
            and case["quality_status"] == "valid"
        )
        if authorised:
            assert case["execution_allowed"] is True


def test_non_allowlisted_sources_are_blocked(cases):
    for case in cases:
        if not case["source_allowlisted"]:
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"
            assert case["security_risk"] in {"high", "critical"}


def test_integrity_mismatch_is_critical_or_high_and_blocked(cases):
    for case in cases:
        if case["integrity_status"] == "mismatch":
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"
            assert case["security_risk"] in {"high", "critical"}


def test_unverified_integrity_with_execution_request_is_blocked(cases):
    for case in cases:
        if (
            case["integrity_status"] == "unverified"
            and case["execution_requested"]
        ):
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"


def test_environment_isolation_failure_is_critical(cases):
    for case in cases:
        if not case["environment_isolated"]:
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"
            assert case["security_risk"] == "critical"


def test_missing_audit_evidence_prevents_execution(cases):
    for case in cases:
        if not case["audit_evidence_present"]:
            assert case["execution_allowed"] is False
            assert case["quality_status"] in {
                "requires_review",
                "blocked",
            }


def test_pending_review_cannot_execute(cases):
    for case in cases:
        if case["script_status"] == "pending_review":
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "requires_review"


def test_disabled_script_cannot_execute(cases):
    for case in cases:
        if case["script_status"] == "disabled":
            assert case["execution_requested"] is False
            assert case["execution_allowed"] is False


def test_no_execution_request_means_no_execution(cases):
    for case in cases:
        if not case["execution_requested"]:
            assert case["execution_allowed"] is False


def test_critical_security_risk_is_blocked(cases):
    for case in cases:
        if case["security_risk"] == "critical":
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"


def test_valid_status_requires_safe_controls(cases):
    for case in cases:
        if case["quality_status"] == "valid":
            assert case["script_status"] in {
                "approved",
                "disabled",
            }
            assert case["source_allowlisted"] is True
            assert case["integrity_status"] == "verified"
            assert case["environment_isolated"] is True
            assert case["audit_evidence_present"] is True
            assert case["security_risk"] == "none"


def test_review_status_never_allows_execution(cases):
    for case in cases:
        if case["quality_status"] == "requires_review":
            assert case["execution_allowed"] is False


def test_blocked_status_never_allows_execution(cases):
    for case in cases:
        if case["quality_status"] == "blocked":
            assert case["execution_allowed"] is False


def test_unapproved_scripts_never_execute(cases):
    for case in cases:
        if case["script_status"] == "unapproved":
            assert case["execution_allowed"] is False
            assert case["quality_status"] == "blocked"


def test_safe_actions_are_meaningful(cases):
    for case in cases:
        assert isinstance(case["safe_action"], str)
        assert len(case["safe_action"].strip()) >= 50


def test_safe_actions_align_with_quality_status(cases):
    expected_terms = {
        "valid": {
            "allow",
            "accept",
            "verified",
            "authorised",
        },
        "requires_review": {
            "review",
            "evidence",
            "authorisation",
            "disabled",
        },
        "blocked": {
            "block",
            "prevent",
            "investigate",
        },
    }

    for case in cases:
        action = case["safe_action"].lower()
        terms = expected_terms[case["quality_status"]]

        assert any(term in action for term in terms), (
            f"{case['id']}: safe action does not align "
            f"with {case['quality_status']}"
        )


def test_all_quality_statuses_are_covered(cases):
    actual = {case["quality_status"] for case in cases}

    assert actual == {
        "valid",
        "requires_review",
        "blocked",
    }


def test_all_environments_are_covered(cases):
    actual = {case["environment"] for case in cases}

    assert actual == {
        "test",
        "staging",
        "production",
    }
