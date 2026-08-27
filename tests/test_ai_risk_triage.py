import json
from pathlib import Path


AI_RISK_TRIAGE_DATA_PATH = Path("data/ai_risk_triage_cases.json")

VALID_GROUNDING_STATUSES = {
    "fully_grounded",
    "partially_grounded",
    "weakly_grounded",
    "ungrounded",
}

VALID_HALLUCINATION_RISKS = {"low", "medium", "high", "critical"}
VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}

VALID_REVIEW_ROUTES = {
    "standard_review",
    "review_with_notes",
    "senior_review",
    "blocked",
}

VALID_APPROVAL_POLICIES = {
    "approval_allowed",
    "approval_requires_notes",
    "approval_blocked_pending_escalation",
    "approval_not_allowed",
}

EXPECTED_ROUTE_BY_RISK_LEVEL = {
    "low": "standard_review",
    "medium": "review_with_notes",
    "high": "senior_review",
    "critical": "blocked",
}

EXPECTED_APPROVAL_POLICY_BY_RISK_LEVEL = {
    "low": "approval_allowed",
    "medium": "approval_requires_notes",
    "high": "approval_blocked_pending_escalation",
    "critical": "approval_not_allowed",
}


def load_ai_risk_triage_cases():
    with AI_RISK_TRIAGE_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_ai_risk_triage_dataset_exists():
    assert AI_RISK_TRIAGE_DATA_PATH.exists(), "AI risk triage dataset file is missing."


def test_ai_risk_triage_dataset_is_not_empty():
    cases = load_ai_risk_triage_cases()

    assert isinstance(cases, list), "AI risk triage dataset must be a list."
    assert len(cases) > 0, "AI risk triage dataset must contain at least one case."


def test_each_ai_risk_triage_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "grounding_status",
        "hallucination_risk",
        "unsupported_claims_count",
        "evidence_items_count",
        "fabricated_source",
        "sensitive_or_regulated_context",
        "risk_level",
        "review_route",
        "approval_policy",
        "safe_action",
    }

    for case in load_ai_risk_triage_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"AI risk triage case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_ai_risk_triage_ids_are_unique():
    cases = load_ai_risk_triage_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "AI risk triage case IDs must be unique."


def test_ai_risk_triage_controlled_values_are_used():
    for case in load_ai_risk_triage_cases():
        assert case["grounding_status"] in VALID_GROUNDING_STATUSES, (
            f"{case['id']} has invalid grounding status: {case['grounding_status']}"
        )
        assert case["hallucination_risk"] in VALID_HALLUCINATION_RISKS, (
            f"{case['id']} has invalid hallucination risk: {case['hallucination_risk']}"
        )
        assert case["risk_level"] in VALID_RISK_LEVELS, (
            f"{case['id']} has invalid risk level: {case['risk_level']}"
        )
        assert case["review_route"] in VALID_REVIEW_ROUTES, (
            f"{case['id']} has invalid review route: {case['review_route']}"
        )
        assert case["approval_policy"] in VALID_APPROVAL_POLICIES, (
            f"{case['id']} has invalid approval policy: {case['approval_policy']}"
        )


def test_numeric_counts_are_valid_non_negative_integers():
    for case in load_ai_risk_triage_cases():
        assert isinstance(case["unsupported_claims_count"], int), (
            f"{case['id']} unsupported_claims_count must be an integer."
        )
        assert isinstance(case["evidence_items_count"], int), (
            f"{case['id']} evidence_items_count must be an integer."
        )
        assert case["unsupported_claims_count"] >= 0, (
            f"{case['id']} unsupported_claims_count cannot be negative."
        )
        assert case["evidence_items_count"] >= 0, (
            f"{case['id']} evidence_items_count cannot be negative."
        )


def test_boolean_fields_are_valid_booleans():
    for case in load_ai_risk_triage_cases():
        assert isinstance(case["fabricated_source"], bool), (
            f"{case['id']} fabricated_source must be a boolean."
        )
        assert isinstance(case["sensitive_or_regulated_context"], bool), (
            f"{case['id']} sensitive_or_regulated_context must be a boolean."
        )


def test_review_route_matches_risk_level():
    for case in load_ai_risk_triage_cases():
        expected_route = EXPECTED_ROUTE_BY_RISK_LEVEL[case["risk_level"]]

        assert case["review_route"] == expected_route, (
            f"{case['id']} review route should be {expected_route} "
            f"for {case['risk_level']} risk."
        )


def test_approval_policy_matches_risk_level():
    for case in load_ai_risk_triage_cases():
        expected_policy = EXPECTED_APPROVAL_POLICY_BY_RISK_LEVEL[case["risk_level"]]

        assert case["approval_policy"] == expected_policy, (
            f"{case['id']} approval policy should be {expected_policy} "
            f"for {case['risk_level']} risk."
        )


def test_low_risk_requires_strong_grounding_and_low_hallucination_risk():
    for case in load_ai_risk_triage_cases():
        if case["risk_level"] == "low":
            assert case["grounding_status"] == "fully_grounded", (
                f"{case['id']} low-risk outputs must be fully grounded."
            )
            assert case["hallucination_risk"] == "low", (
                f"{case['id']} low-risk outputs must have low hallucination risk."
            )
            assert case["unsupported_claims_count"] == 0, (
                f"{case['id']} low-risk outputs must not contain unsupported claims."
            )
            assert case["evidence_items_count"] >= 2, (
                f"{case['id']} low-risk outputs need sufficient supporting evidence."
            )


def test_medium_risk_requires_notes_route():
    for case in load_ai_risk_triage_cases():
        if case["risk_level"] == "medium":
            assert case["review_route"] == "review_with_notes", (
                f"{case['id']} medium-risk outputs should require review with notes."
            )
            assert case["approval_policy"] == "approval_requires_notes", (
                f"{case['id']} medium-risk outputs should require notes before approval."
            )


def test_high_risk_requires_senior_review():
    for case in load_ai_risk_triage_cases():
        if case["risk_level"] == "high":
            assert case["review_route"] == "senior_review", (
                f"{case['id']} high-risk outputs should be routed to senior review."
            )
            assert case["approval_policy"] == "approval_blocked_pending_escalation", (
                f"{case['id']} high-risk outputs should block approval pending escalation."
            )


def test_critical_risk_is_blocked():
    for case in load_ai_risk_triage_cases():
        if case["risk_level"] == "critical":
            assert case["review_route"] == "blocked", (
                f"{case['id']} critical-risk outputs should be blocked."
            )
            assert case["approval_policy"] == "approval_not_allowed", (
                f"{case['id']} critical-risk outputs should not be approved."
            )


def test_fabricated_sources_are_critical_and_blocked():
    for case in load_ai_risk_triage_cases():
        if case["fabricated_source"]:
            assert case["risk_level"] == "critical", (
                f"{case['id']} fabricated sources should be critical risk."
            )
            assert case["review_route"] == "blocked", (
                f"{case['id']} fabricated sources should be blocked."
            )
            assert case["approval_policy"] == "approval_not_allowed", (
                f"{case['id']} fabricated sources should not be approved."
            )


def test_missing_evidence_cannot_be_low_or_medium_risk():
    for case in load_ai_risk_triage_cases():
        if case["evidence_items_count"] == 0:
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} missing evidence should be high or critical risk."
            )
            assert case["review_route"] in {"senior_review", "blocked"}, (
                f"{case['id']} missing evidence should not go to standard review."
            )


def test_high_hallucination_risk_cannot_use_standard_review():
    for case in load_ai_risk_triage_cases():
        if case["hallucination_risk"] in {"high", "critical"}:
            assert case["review_route"] != "standard_review", (
                f"{case['id']} high or critical hallucination risk cannot use standard review."
            )
            assert case["approval_policy"] != "approval_allowed", (
                f"{case['id']} high or critical hallucination risk cannot allow approval."
            )


def test_sensitive_or_regulated_context_escalates_when_not_fully_grounded():
    for case in load_ai_risk_triage_cases():
        if (
            case["sensitive_or_regulated_context"]
            and case["grounding_status"] != "fully_grounded"
        ):
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} sensitive or regulated context should escalate risk "
                "when not fully grounded."
            )
            assert case["review_route"] in {"senior_review", "blocked"}, (
                f"{case['id']} sensitive or regulated context should not use standard review "
                "when grounding is incomplete."
            )


def test_unsupported_claims_prevent_low_risk_classification():
    for case in load_ai_risk_triage_cases():
        if case["unsupported_claims_count"] > 0:
            assert case["risk_level"] != "low", (
                f"{case['id']} unsupported claims should prevent low-risk classification."
            )


def test_ungrounded_outputs_cannot_be_low_or_medium_risk():
    for case in load_ai_risk_triage_cases():
        if case["grounding_status"] == "ungrounded":
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} ungrounded outputs should be high or critical risk."
            )


def test_safe_actions_are_meaningful_and_match_routing():
    expected_terms_by_route = {
        "standard_review": {"standard", "review", "allow"},
        "review_with_notes": {"notes", "review", "require"},
        "senior_review": {"senior", "review", "escalate", "route"},
        "blocked": {"block", "approval", "source", "unsupported"},
    }

    for case in load_ai_risk_triage_cases():
        safe_action = case["safe_action"].strip().lower()
        expected_terms = expected_terms_by_route[case["review_route"]]

        assert len(safe_action) >= 70, (
            f"{case['id']} safe action is too short or vague."
        )
        assert any(term in safe_action for term in expected_terms), (
            f"{case['id']} safe action should align with route {case['review_route']}."
        )