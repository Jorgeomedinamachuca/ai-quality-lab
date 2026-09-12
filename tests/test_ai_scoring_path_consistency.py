import json
from pathlib import Path


AI_SCORING_PATH_DATA_PATH = Path("data/ai_scoring_path_cases.json")

VALID_EXPECTED_SCORING_PATHS = {
    "ai_scoring",
    "rule_based_scoring",
}

VALID_ACTUAL_SCORING_PATHS = {
    "ai_scoring",
    "rule_based_scoring",
    "experimental_scoring",
    "human_review_adjustment",
}

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}

VALID_QUALITY_STATUSES = {
    "valid",
    "review_required",
    "requires_review",
    "blocked",
}

EXPECTED_QUALITY_STATUS_BY_RISK_LEVEL = {
    "low": "valid",
    "medium": "review_required",
    "high": "requires_review",
    "critical": "blocked",
}


def load_ai_scoring_path_cases():
    with AI_SCORING_PATH_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_ai_scoring_path_dataset_exists():
    assert AI_SCORING_PATH_DATA_PATH.exists(), (
        "AI scoring path dataset file is missing."
    )


def test_ai_scoring_path_dataset_is_not_empty():
    cases = load_ai_scoring_path_cases()

    assert isinstance(cases, list), "AI scoring path dataset must be a list."
    assert len(cases) > 0, "AI scoring path dataset must contain at least one case."


def test_each_ai_scoring_path_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "record_group",
        "expected_scoring_path",
        "actual_scoring_paths",
        "scoring_provenance_present",
        "retry_used",
        "manual_review_required",
        "mixed_path_detected",
        "risk_level",
        "quality_status",
        "safe_action",
    }

    for case in load_ai_scoring_path_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"AI scoring path case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_ai_scoring_path_ids_are_unique():
    cases = load_ai_scoring_path_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "AI scoring path case IDs must be unique."


def test_controlled_values_are_used():
    for case in load_ai_scoring_path_cases():
        assert case["expected_scoring_path"] in VALID_EXPECTED_SCORING_PATHS, (
            f"{case['id']} has invalid expected scoring path: "
            f"{case['expected_scoring_path']}"
        )
        assert case["risk_level"] in VALID_RISK_LEVELS, (
            f"{case['id']} has invalid risk level: {case['risk_level']}"
        )
        assert case["quality_status"] in VALID_QUALITY_STATUSES, (
            f"{case['id']} has invalid quality status: {case['quality_status']}"
        )


def test_actual_scoring_paths_are_valid_list_values():
    for case in load_ai_scoring_path_cases():
        assert isinstance(case["actual_scoring_paths"], list), (
            f"{case['id']} actual_scoring_paths must be a list."
        )

        for scoring_path in case["actual_scoring_paths"]:
            assert scoring_path in VALID_ACTUAL_SCORING_PATHS, (
                f"{case['id']} has invalid actual scoring path: {scoring_path}"
            )


def test_boolean_fields_are_valid_booleans():
    boolean_fields = {
        "scoring_provenance_present",
        "retry_used",
        "manual_review_required",
        "mixed_path_detected",
    }

    for case in load_ai_scoring_path_cases():
        for field in boolean_fields:
            assert isinstance(case[field], bool), (
                f"{case['id']} {field} must be a boolean."
            )


def test_quality_status_matches_risk_level():
    for case in load_ai_scoring_path_cases():
        expected_status = EXPECTED_QUALITY_STATUS_BY_RISK_LEVEL[case["risk_level"]]

        assert case["quality_status"] == expected_status, (
            f"{case['id']} quality status should be {expected_status} "
            f"for {case['risk_level']} risk."
        )


def test_low_risk_requires_consistent_traceable_path():
    for case in load_ai_scoring_path_cases():
        if case["risk_level"] == "low":
            assert case["scoring_provenance_present"] is True, (
                f"{case['id']} low-risk scoring requires provenance."
            )
            assert case["actual_scoring_paths"] == [case["expected_scoring_path"]], (
                f"{case['id']} low-risk scoring must use only the expected path."
            )
            assert case["retry_used"] is False, (
                f"{case['id']} low-risk scoring should not involve retry ambiguity."
            )
            assert case["manual_review_required"] is False, (
                f"{case['id']} low-risk scoring should not require manual review."
            )
            assert case["mixed_path_detected"] is False, (
                f"{case['id']} low-risk scoring cannot have mixed path detection."
            )


def test_missing_provenance_is_critical_and_blocked():
    for case in load_ai_scoring_path_cases():
        if case["scoring_provenance_present"] is False:
            assert case["risk_level"] == "critical", (
                f"{case['id']} missing provenance should be critical risk."
            )
            assert case["quality_status"] == "blocked", (
                f"{case['id']} missing provenance should block scoring result."
            )
            assert case["manual_review_required"] is True, (
                f"{case['id']} missing provenance should require review."
            )


def test_mixed_paths_require_review_and_high_or_critical_risk():
    for case in load_ai_scoring_path_cases():
        if case["mixed_path_detected"]:
            assert len(case["actual_scoring_paths"]) > 1, (
                f"{case['id']} mixed path detection should include more than one path."
            )
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} mixed paths should be high or critical risk."
            )
            assert case["manual_review_required"] is True, (
                f"{case['id']} mixed paths should require manual review."
            )
            assert case["quality_status"] in {"requires_review", "blocked"}, (
                f"{case['id']} mixed paths should require review or be blocked."
            )


def test_retry_usage_requires_review_unless_low_risk_not_used():
    for case in load_ai_scoring_path_cases():
        if case["retry_used"]:
            assert case["manual_review_required"] is True, (
                f"{case['id']} retry usage should require manual review."
            )
            assert case["risk_level"] in {"medium", "high", "critical"}, (
                f"{case['id']} retry usage should not remain low risk."
            )


def test_unexpected_scoring_path_requires_review():
    for case in load_ai_scoring_path_cases():
        actual_paths = case["actual_scoring_paths"]

        if (
            case["scoring_provenance_present"]
            and len(actual_paths) == 1
            and actual_paths[0] != case["expected_scoring_path"]
        ):
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} unexpected scoring path should escalate risk."
            )
            assert case["manual_review_required"] is True, (
                f"{case['id']} unexpected scoring path should require review."
            )
            assert case["quality_status"] in {"requires_review", "blocked"}, (
                f"{case['id']} unexpected scoring path should not be valid."
            )


def test_empty_actual_paths_only_allowed_when_provenance_missing():
    for case in load_ai_scoring_path_cases():
        if len(case["actual_scoring_paths"]) == 0:
            assert case["scoring_provenance_present"] is False, (
                f"{case['id']} empty actual paths should only occur when provenance is missing."
            )
            assert case["quality_status"] == "blocked", (
                f"{case['id']} empty actual paths should block the result."
            )


def test_valid_results_have_no_review_or_mixed_path_flags():
    for case in load_ai_scoring_path_cases():
        if case["quality_status"] == "valid":
            assert case["manual_review_required"] is False, (
                f"{case['id']} valid results should not require manual review."
            )
            assert case["mixed_path_detected"] is False, (
                f"{case['id']} valid results should not have mixed paths."
            )
            assert case["scoring_provenance_present"] is True, (
                f"{case['id']} valid results require provenance."
            )


def test_blocked_results_are_not_usable_without_review():
    for case in load_ai_scoring_path_cases():
        if case["quality_status"] == "blocked":
            assert case["risk_level"] == "critical", (
                f"{case['id']} blocked results should be critical risk."
            )
            assert case["manual_review_required"] is True, (
                f"{case['id']} blocked results should require review."
            )


def test_actual_path_list_matches_mixed_path_flag():
    for case in load_ai_scoring_path_cases():
        if len(case["actual_scoring_paths"]) > 1:
            assert case["mixed_path_detected"] is True, (
                f"{case['id']} multiple actual scoring paths should set mixed_path_detected."
            )

        if case["mixed_path_detected"] is False and case["scoring_provenance_present"]:
            assert len(case["actual_scoring_paths"]) <= 1, (
                f"{case['id']} non-mixed scoring should not include multiple paths."
            )


def test_safe_actions_are_meaningful():
    for case in load_ai_scoring_path_cases():
        assert len(case["safe_action"].strip()) >= 70, (
            f"{case['id']} safe action is too short or vague."
        )


def test_safe_actions_align_with_quality_status():
    expected_terms_by_status = {
        "valid": {"accept", "provenance", "expected"},
        "review_required": {"review", "notes", "traceable"},
        "requires_review": {"review", "escalate", "manual"},
        "blocked": {"block", "provenance", "verified"},
    }

    for case in load_ai_scoring_path_cases():
        safe_action = case["safe_action"].lower()
        expected_terms = expected_terms_by_status[case["quality_status"]]

        assert any(term in safe_action for term in expected_terms), (
            f"{case['id']} safe action should align with quality status "
            f"{case['quality_status']}."
        )


def test_scoring_results_are_traceable_when_not_blocked():
    for case in load_ai_scoring_path_cases():
        if case["quality_status"] != "blocked":
            assert case["scoring_provenance_present"] is True, (
                f"{case['id']} non-blocked scoring results require provenance."
            )
            assert len(case["actual_scoring_paths"]) >= 1, (
                f"{case['id']} non-blocked scoring results need at least one actual path."
            )