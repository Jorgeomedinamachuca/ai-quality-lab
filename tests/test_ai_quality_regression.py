import json
from pathlib import Path


AI_QUALITY_REGRESSION_DATA_PATH = Path("data/ai_quality_regression_cases.json")

VALID_RELEASE_STATUSES = {
    "ready_for_release",
    "review_required",
    "requires_escalation",
    "blocked",
}

VALID_RELEASE_DECISIONS = {
    "approve_release",
    "approve_with_signoff",
    "escalate_release_review",
    "reject_release",
}

EXPECTED_DECISION_BY_STATUS = {
    "ready_for_release": "approve_release",
    "review_required": "approve_with_signoff",
    "requires_escalation": "escalate_release_review",
    "blocked": "reject_release",
}

REGRESSION_FLAGS = {
    "grounding_regression",
    "hallucination_regression",
    "risk_routing_regression",
    "approval_control_regression",
    "evidence_traceability_regression",
}


def load_ai_quality_regression_cases():
    with AI_QUALITY_REGRESSION_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_ai_quality_regression_dataset_exists():
    assert AI_QUALITY_REGRESSION_DATA_PATH.exists(), (
        "AI quality regression dataset file is missing."
    )


def test_ai_quality_regression_dataset_is_not_empty():
    cases = load_ai_quality_regression_cases()

    assert isinstance(cases, list), "AI quality regression dataset must be a list."
    assert len(cases) > 0, "AI quality regression dataset must contain at least one case."


def test_each_ai_quality_regression_case_has_required_fields():
    required_fields = {
        "id",
        "release_candidate",
        "scenario",
        "description",
        "grounding_regression",
        "hallucination_regression",
        "risk_routing_regression",
        "approval_control_regression",
        "evidence_traceability_regression",
        "critical_failures_count",
        "high_risk_failures_count",
        "medium_risk_failures_count",
        "review_notes_required",
        "release_status",
        "release_decision",
        "safe_action",
    }

    for case in load_ai_quality_regression_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"AI quality regression case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_ai_quality_regression_ids_are_unique():
    cases = load_ai_quality_regression_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "AI quality regression case IDs must be unique."


def test_release_candidate_ids_are_unique():
    cases = load_ai_quality_regression_cases()
    release_candidates = [case["release_candidate"] for case in cases]

    assert len(release_candidates) == len(set(release_candidates)), (
        "Release candidate IDs must be unique."
    )


def test_release_status_and_decision_use_controlled_values():
    for case in load_ai_quality_regression_cases():
        assert case["release_status"] in VALID_RELEASE_STATUSES, (
            f"{case['id']} has invalid release status: {case['release_status']}"
        )
        assert case["release_decision"] in VALID_RELEASE_DECISIONS, (
            f"{case['id']} has invalid release decision: {case['release_decision']}"
        )


def test_release_decision_matches_release_status():
    for case in load_ai_quality_regression_cases():
        expected_decision = EXPECTED_DECISION_BY_STATUS[case["release_status"]]

        assert case["release_decision"] == expected_decision, (
            f"{case['id']} release decision should be {expected_decision} "
            f"when status is {case['release_status']}."
        )


def test_regression_flags_are_booleans():
    for case in load_ai_quality_regression_cases():
        for flag in REGRESSION_FLAGS:
            assert isinstance(case[flag], bool), (
                f"{case['id']} {flag} must be a boolean."
            )


def test_failure_counts_are_valid_non_negative_integers():
    failure_count_fields = {
        "critical_failures_count",
        "high_risk_failures_count",
        "medium_risk_failures_count",
    }

    for case in load_ai_quality_regression_cases():
        for field in failure_count_fields:
            assert isinstance(case[field], int), (
                f"{case['id']} {field} must be an integer."
            )
            assert case[field] >= 0, (
                f"{case['id']} {field} cannot be negative."
            )


def test_review_notes_required_is_boolean():
    for case in load_ai_quality_regression_cases():
        assert isinstance(case["review_notes_required"], bool), (
            f"{case['id']} review_notes_required must be a boolean."
        )


def test_ready_for_release_has_no_regressions_or_failures():
    for case in load_ai_quality_regression_cases():
        if case["release_status"] == "ready_for_release":
            assert not any(case[flag] for flag in REGRESSION_FLAGS), (
                f"{case['id']} ready releases cannot have regression flags."
            )
            assert case["critical_failures_count"] == 0, (
                f"{case['id']} ready releases cannot have critical failures."
            )
            assert case["high_risk_failures_count"] == 0, (
                f"{case['id']} ready releases cannot have high-risk failures."
            )
            assert case["medium_risk_failures_count"] == 0, (
                f"{case['id']} ready releases cannot have medium-risk failures."
            )
            assert case["review_notes_required"] is False, (
                f"{case['id']} ready releases should not require review notes."
            )


def test_critical_failures_block_release():
    for case in load_ai_quality_regression_cases():
        if case["critical_failures_count"] > 0:
            assert case["release_status"] == "blocked", (
                f"{case['id']} critical failures should block the release."
            )
            assert case["release_decision"] == "reject_release", (
                f"{case['id']} critical failures should reject the release."
            )


def test_hallucination_regression_blocks_or_escalates_release():
    for case in load_ai_quality_regression_cases():
        if case["hallucination_regression"]:
            assert case["release_status"] in {"blocked", "requires_escalation"}, (
                f"{case['id']} hallucination regression should block or escalate release."
            )
            assert case["release_decision"] in {
                "reject_release",
                "escalate_release_review",
            }, (
                f"{case['id']} hallucination regression should not allow direct approval."
            )


def test_approval_control_regression_blocks_release():
    for case in load_ai_quality_regression_cases():
        if case["approval_control_regression"]:
            assert case["release_status"] == "blocked", (
                f"{case['id']} approval control regression should block release."
            )
            assert case["release_decision"] == "reject_release", (
                f"{case['id']} approval control regression should reject release."
            )


def test_risk_routing_regression_requires_escalation_or_blocking():
    for case in load_ai_quality_regression_cases():
        if case["risk_routing_regression"]:
            assert case["release_status"] in {"requires_escalation", "blocked"}, (
                f"{case['id']} risk routing regression should escalate or block release."
            )
            assert case["release_decision"] in {
                "escalate_release_review",
                "reject_release",
            }, (
                f"{case['id']} risk routing regression should not approve release directly."
            )


def test_evidence_traceability_regression_requires_escalation_or_blocking():
    for case in load_ai_quality_regression_cases():
        if case["evidence_traceability_regression"]:
            assert case["release_status"] in {"requires_escalation", "blocked"}, (
                f"{case['id']} evidence traceability regression should escalate or block release."
            )


def test_high_risk_failures_prevent_direct_release_approval():
    for case in load_ai_quality_regression_cases():
        if case["high_risk_failures_count"] > 0:
            assert case["release_status"] in {"requires_escalation", "blocked"}, (
                f"{case['id']} high-risk failures should escalate or block release."
            )
            assert case["release_decision"] != "approve_release", (
                f"{case['id']} high-risk failures should prevent direct release approval."
            )


def test_medium_risk_only_cases_require_review_or_signoff():
    for case in load_ai_quality_regression_cases():
        has_only_medium_risk = (
            case["medium_risk_failures_count"] > 0
            and case["high_risk_failures_count"] == 0
            and case["critical_failures_count"] == 0
            and not any(case[flag] for flag in REGRESSION_FLAGS)
        )

        if has_only_medium_risk:
            assert case["release_status"] == "review_required", (
                f"{case['id']} medium-risk-only releases should require review."
            )
            assert case["release_decision"] == "approve_with_signoff", (
                f"{case['id']} medium-risk-only releases should require sign-off."
            )
            assert case["review_notes_required"] is True, (
                f"{case['id']} medium-risk-only releases should require notes."
            )


def test_review_notes_required_for_non_ready_releases():
    for case in load_ai_quality_regression_cases():
        if case["release_status"] != "ready_for_release":
            assert case["review_notes_required"] is True, (
                f"{case['id']} non-ready releases should require review notes."
            )


def test_blocked_releases_have_reject_safe_action():
    for case in load_ai_quality_regression_cases():
        if case["release_status"] == "blocked":
            assert "reject" in case["safe_action"].lower(), (
                f"{case['id']} blocked releases should have a reject safe action."
            )


def test_escalated_releases_have_escalate_safe_action():
    for case in load_ai_quality_regression_cases():
        if case["release_status"] == "requires_escalation":
            assert "escalate" in case["safe_action"].lower(), (
                f"{case['id']} escalated releases should have an escalate safe action."
            )


def test_safe_actions_are_meaningful():
    for case in load_ai_quality_regression_cases():
        assert len(case["safe_action"].strip()) >= 70, (
            f"{case['id']} safe action is too short or vague."
        )


def test_release_candidates_use_expected_prefix():
    for case in load_ai_quality_regression_cases():
        assert case["release_candidate"].startswith("RC-"), (
            f"{case['id']} release candidate should use RC- prefix."
        )