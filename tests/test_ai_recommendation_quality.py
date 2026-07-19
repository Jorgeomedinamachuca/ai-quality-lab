import json
from pathlib import Path


RECOMMENDATION_DATA_PATH = Path("data/recommendation_cases.json")

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}
VALID_QUALITY_LEVELS = {"low", "medium", "high"}


def load_recommendation_cases():
    with RECOMMENDATION_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_recommendation_dataset_exists():
    assert RECOMMENDATION_DATA_PATH.exists(), "Recommendation dataset file is missing."


def test_recommendation_dataset_is_not_empty():
    cases = load_recommendation_cases()

    assert isinstance(cases, list), "Recommendation dataset must be a list."
    assert len(cases) > 0, "Recommendation dataset must contain at least one case."


def test_each_recommendation_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "input_profile",
        "recommended_profile",
        "recommendation_reason",
        "evidence",
        "risk_level",
        "expected_quality",
        "safety_notes",
    }

    for case in load_recommendation_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"Recommendation case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_recommendation_ids_are_unique():
    cases = load_recommendation_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "Recommendation case IDs must be unique."


def test_recommendation_profiles_have_required_structure():
    required_profile_fields = {"role", "topics", "sector_focus"}

    for case in load_recommendation_cases():
        for profile_field in ["input_profile", "recommended_profile"]:
            profile = case[profile_field]
            missing_fields = required_profile_fields - set(profile)

            assert not missing_fields, (
                f"{case['id']} {profile_field} is missing fields: {missing_fields}"
            )
            assert isinstance(profile["topics"], list), (
                f"{case['id']} {profile_field}.topics must be a list."
            )
            assert isinstance(profile["sector_focus"], list), (
                f"{case['id']} {profile_field}.sector_focus must be a list."
            )


def test_recommendation_reason_is_meaningful():
    for case in load_recommendation_cases():
        reason = case["recommendation_reason"].strip()

        assert len(reason) >= 30, (
            f"{case['id']} recommendation reason is too short or vague."
        )


def test_evidence_is_required_for_high_quality_recommendations():
    for case in load_recommendation_cases():
        if case["expected_quality"] == "high":
            assert len(case["evidence"]) >= 2, (
                f"{case['id']} high-quality recommendations require at least two evidence signals."
            )


def test_single_signal_recommendations_are_not_high_quality():
    for case in load_recommendation_cases():
        if len(case["evidence"]) < 2:
            assert case["expected_quality"] != "high", (
                f"{case['id']} should not be high quality with fewer than two evidence signals."
            )


def test_risk_and_quality_levels_are_valid():
    for case in load_recommendation_cases():
        assert case["risk_level"] in VALID_RISK_LEVELS, (
            f"{case['id']} has invalid risk level: {case['risk_level']}"
        )
        assert case["expected_quality"] in VALID_QUALITY_LEVELS, (
            f"{case['id']} has invalid expected quality: {case['expected_quality']}"
        )


def test_high_risk_recommendations_have_safety_notes():
    for case in load_recommendation_cases():
        if case["risk_level"] in {"high", "critical"}:
            assert len(case["safety_notes"]) >= 2, (
                f"{case['id']} high-risk recommendations require safety notes."
            )


def test_recommendations_do_not_use_sensitive_client_identifiers():
    blocked_terms = {
        "client name:",
        "patient name:",
        "confidential matter:",
        "private email:",
        "personal phone:",
    }

    for case in load_recommendation_cases():
        searchable_text = json.dumps(case, ensure_ascii=False).lower()

        for blocked_term in blocked_terms:
            assert blocked_term not in searchable_text, (
                f"{case['id']} contains a blocked sensitive identifier: {blocked_term}"
            )