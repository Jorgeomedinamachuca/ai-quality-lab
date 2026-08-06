import json
from pathlib import Path


ANALYTICS_SIGNAL_DATA_PATH = Path("data/analytics_signal_cases.json")

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}

VALID_DECLINE_PATTERNS = {
    "gradual",
    "sudden",
    "segment_specific",
    "reporting_mismatch",
    "controlled_change",
}

VALID_INVESTIGATION_STATUSES = {
    "requires_investigation",
    "explainable_change",
    "confirmed_measurement_issue",
    "confirmed_usage_decline",
    "insufficient_evidence",
}


def load_analytics_signal_cases():
    with ANALYTICS_SIGNAL_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_analytics_signal_dataset_exists():
    assert ANALYTICS_SIGNAL_DATA_PATH.exists(), "Analytics signal dataset file is missing."


def test_analytics_signal_dataset_is_not_empty():
    cases = load_analytics_signal_cases()

    assert isinstance(cases, list), "Analytics signal dataset must be a list."
    assert len(cases) > 0, "Analytics signal dataset must contain at least one case."


def test_each_analytics_signal_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "metric_name",
        "event_type",
        "period",
        "baseline_value",
        "current_value",
        "decline_percentage",
        "decline_pattern",
        "affected_segments",
        "possible_causes",
        "evidence_required",
        "risk_level",
        "expected_investigation_status",
        "safe_conclusion",
    }

    for case in load_analytics_signal_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"Analytics signal case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_analytics_signal_ids_are_unique():
    cases = load_analytics_signal_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "Analytics signal case IDs must be unique."


def test_decline_percentage_matches_baseline_and_current_values():
    for case in load_analytics_signal_cases():
        baseline = case["baseline_value"]
        current = case["current_value"]
        expected_decline = round(((baseline - current) / baseline) * 100, 1)

        assert case["decline_percentage"] == expected_decline, (
            f"{case['id']} decline_percentage should be {expected_decline}, "
            f"but got {case['decline_percentage']}."
        )


def test_decline_patterns_use_controlled_values():
    for case in load_analytics_signal_cases():
        assert case["decline_pattern"] in VALID_DECLINE_PATTERNS, (
            f"{case['id']} has invalid decline pattern: {case['decline_pattern']}"
        )


def test_risk_levels_use_controlled_values():
    for case in load_analytics_signal_cases():
        assert case["risk_level"] in VALID_RISK_LEVELS, (
            f"{case['id']} has invalid risk level: {case['risk_level']}"
        )


def test_investigation_statuses_use_controlled_values():
    for case in load_analytics_signal_cases():
        assert case["expected_investigation_status"] in VALID_INVESTIGATION_STATUSES, (
            f"{case['id']} has invalid investigation status: "
            f"{case['expected_investigation_status']}"
        )


def test_high_or_critical_risk_cases_require_multiple_evidence_items():
    for case in load_analytics_signal_cases():
        if case["risk_level"] in {"high", "critical"}:
            assert len(case["evidence_required"]) >= 4, (
                f"{case['id']} high/critical risk cases require at least four evidence checks."
            )


def test_large_unexplained_declines_require_investigation():
    for case in load_analytics_signal_cases():
        if (
            case["decline_percentage"] >= 50
            and case["expected_investigation_status"] != "explainable_change"
        ):
            assert case["expected_investigation_status"] == "requires_investigation", (
                f"{case['id']} large unexplained declines should require investigation."
            )


def test_sudden_declines_are_not_treated_as_safe_without_investigation():
    for case in load_analytics_signal_cases():
        if case["decline_pattern"] == "sudden":
            assert case["expected_investigation_status"] == "requires_investigation", (
                f"{case['id']} sudden declines should require investigation."
            )
            assert case["risk_level"] in {"high", "critical"}, (
                f"{case['id']} sudden declines should be high or critical risk."
            )


def test_dashboard_mismatches_require_raw_data_comparison():
    for case in load_analytics_signal_cases():
        if case["decline_pattern"] == "reporting_mismatch":
            evidence_text = " ".join(case["evidence_required"]).lower()

            assert "raw" in evidence_text, (
                f"{case['id']} reporting mismatches should require raw data comparison."
            )
            assert "dashboard" in evidence_text, (
                f"{case['id']} reporting mismatches should mention dashboard validation."
            )


def test_segment_specific_declines_require_segment_comparison():
    for case in load_analytics_signal_cases():
        if case["decline_pattern"] == "segment_specific":
            evidence_text = " ".join(case["evidence_required"]).lower()

            assert "segment" in evidence_text, (
                f"{case['id']} segment-specific declines should require segment comparison."
            )


def test_safe_conclusions_do_not_overstate_user_behaviour():
    blocked_phrases = {
        "users stopped engaging",
        "users are no longer interested",
        "engagement definitely declined",
        "usage definitely declined",
        "the product is failing",
    }

    for case in load_analytics_signal_cases():
        conclusion = case["safe_conclusion"].lower()

        for blocked_phrase in blocked_phrases:
            assert blocked_phrase not in conclusion, (
                f"{case['id']} safe conclusion overstates behaviour: {blocked_phrase}"
            )


def test_each_case_includes_possible_causes():
    for case in load_analytics_signal_cases():
        assert len(case["possible_causes"]) >= 3, (
            f"{case['id']} should include at least three possible causes."
        )


def test_each_case_has_meaningful_safe_conclusion():
    for case in load_analytics_signal_cases():
        conclusion = case["safe_conclusion"].strip()

        assert len(conclusion) >= 60, (
            f"{case['id']} safe conclusion is too short or vague."
        )