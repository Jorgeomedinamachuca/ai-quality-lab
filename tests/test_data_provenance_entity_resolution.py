import json
from datetime import datetime, timezone
from pathlib import Path


PROFILE_PROVENANCE_DATA_PATH = Path("data/profile_provenance_cases.json")

VALID_ENTITY_MATCH_CONFIDENCE = {"low", "medium", "high"}
VALID_IDENTITY_RISK_LEVELS = {"low", "medium", "high", "critical"}
VALID_PROVENANCE_STATUSES = {
    "verified",
    "incomplete",
    "stale",
    "requires_review",
    "rejected",
}
VALID_QUALITY_LEVELS = {"low", "medium", "high"}


def load_profile_provenance_cases():
    with PROFILE_PROVENANCE_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def parse_timestamp(timestamp):
    return datetime.fromisoformat(timestamp.replace("Z", "+00:00"))


def test_profile_provenance_dataset_exists():
    assert PROFILE_PROVENANCE_DATA_PATH.exists(), (
        "Profile provenance dataset file is missing."
    )


def test_profile_provenance_dataset_is_not_empty():
    cases = load_profile_provenance_cases()

    assert isinstance(cases, list), "Profile provenance dataset must be a list."
    assert len(cases) > 0, "Profile provenance dataset must contain at least one case."


def test_each_profile_provenance_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "profile_field",
        "displayed_value",
        "source_type",
        "source_reference",
        "source_timestamp",
        "entity_match_confidence",
        "identity_risk",
        "provenance_status",
        "evidence",
        "expected_quality",
        "safe_action",
    }

    for case in load_profile_provenance_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"Profile provenance case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_profile_provenance_ids_are_unique():
    cases = load_profile_provenance_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "Profile provenance case IDs must be unique."


def test_controlled_values_are_used():
    for case in load_profile_provenance_cases():
        assert case["entity_match_confidence"] in VALID_ENTITY_MATCH_CONFIDENCE, (
            f"{case['id']} has invalid entity match confidence: "
            f"{case['entity_match_confidence']}"
        )
        assert case["identity_risk"] in VALID_IDENTITY_RISK_LEVELS, (
            f"{case['id']} has invalid identity risk: {case['identity_risk']}"
        )
        assert case["provenance_status"] in VALID_PROVENANCE_STATUSES, (
            f"{case['id']} has invalid provenance status: "
            f"{case['provenance_status']}"
        )
        assert case["expected_quality"] in VALID_QUALITY_LEVELS, (
            f"{case['id']} has invalid expected quality: {case['expected_quality']}"
        )


def test_source_timestamp_is_valid_iso_datetime():
    for case in load_profile_provenance_cases():
        parsed_timestamp = parse_timestamp(case["source_timestamp"])

        assert parsed_timestamp.tzinfo is not None, (
            f"{case['id']} source timestamp must include timezone information."
        )


def test_verified_records_require_source_reference_and_high_confidence():
    for case in load_profile_provenance_cases():
        if case["provenance_status"] == "verified":
            assert case["source_reference"].strip(), (
                f"{case['id']} verified records require a source reference."
            )
            assert case["entity_match_confidence"] == "high", (
                f"{case['id']} verified records require high entity match confidence."
            )
            assert case["identity_risk"] == "low", (
                f"{case['id']} verified records should have low identity risk."
            )


def test_missing_source_reference_is_not_high_quality():
    for case in load_profile_provenance_cases():
        if not case["source_reference"].strip():
            assert case["expected_quality"] != "high", (
                f"{case['id']} records without source reference cannot be high quality."
            )
            assert case["provenance_status"] in {"incomplete", "requires_review", "rejected"}, (
                f"{case['id']} missing source reference should not be marked verified."
            )


def test_low_confidence_identity_matches_require_review():
    for case in load_profile_provenance_cases():
        if case["entity_match_confidence"] == "low":
            assert case["provenance_status"] == "requires_review", (
                f"{case['id']} low-confidence identity matches require review."
            )
            assert case["expected_quality"] == "low", (
                f"{case['id']} low-confidence identity matches should be low quality."
            )


def test_high_or_critical_identity_risk_is_not_high_quality():
    for case in load_profile_provenance_cases():
        if case["identity_risk"] in {"high", "critical"}:
            assert case["expected_quality"] != "high", (
                f"{case['id']} high/critical identity risk cannot be high quality."
            )
            assert case["provenance_status"] in {"requires_review", "rejected"}, (
                f"{case['id']} high/critical identity risk should require review or rejection."
            )


def test_stale_records_are_flagged_correctly():
    for case in load_profile_provenance_cases():
        timestamp = parse_timestamp(case["source_timestamp"])
        reference_date = datetime(2026, 8, 1, tzinfo=timezone.utc)
        age_in_days = (reference_date - timestamp).days

        if age_in_days > 730:
            assert case["provenance_status"] == "stale", (
                f"{case['id']} records older than two years should be marked stale."
            )
            assert case["expected_quality"] != "high", (
                f"{case['id']} stale records should not be high quality."
            )


def test_risky_records_have_enough_evidence():
    for case in load_profile_provenance_cases():
        if case["identity_risk"] in {"high", "critical"}:
            assert len(case["evidence"]) >= 4, (
                f"{case['id']} high/critical identity risk requires at least four evidence items."
            )


def test_cross_context_contamination_is_suppressed_or_reviewed():
    cross_context_terms = {
        "cross-context",
        "another profile",
        "different organisation",
        "organisation affiliation may belong to another profile",
    }

    for case in load_profile_provenance_cases():
        combined_text = json.dumps(case, ensure_ascii=False).lower()

        if any(term in combined_text for term in cross_context_terms):
            safe_action = case["safe_action"].lower()

            assert case["identity_risk"] in {"high", "critical"}, (
                f"{case['id']} cross-context contamination should be high or critical risk."
            )
            assert "suppress" in safe_action or "manual" in safe_action or "review" in safe_action, (
                f"{case['id']} cross-context contamination should be suppressed or reviewed."
            )


def test_safe_action_is_meaningful():
    for case in load_profile_provenance_cases():
        safe_action = case["safe_action"].strip()

        assert len(safe_action) >= 50, (
            f"{case['id']} safe action is too short or vague."
        )


def test_unverified_data_is_not_used_as_confirmed_ai_evidence():
    for case in load_profile_provenance_cases():
        if case["provenance_status"] != "verified":
            safe_action = case["safe_action"].lower()

            assert "verified" in safe_action or "review" in safe_action or "confirmation" in safe_action or "suppress" in safe_action, (
                f"{case['id']} unverified data needs verification, review, confirmation or suppression."
            )