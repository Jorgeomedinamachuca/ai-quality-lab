import json
from pathlib import Path


AI_OUTPUT_GROUNDING_DATA_PATH = Path("data/ai_output_grounding_cases.json")

VALID_GROUNDING_STATUSES = {
    "fully_grounded",
    "partially_grounded",
    "weakly_grounded",
    "ungrounded",
}

VALID_HALLUCINATION_RISKS = {"low", "medium", "high", "critical"}
VALID_QUALITY_LEVELS = {"low", "medium", "high"}


def load_ai_output_grounding_cases():
    with AI_OUTPUT_GROUNDING_DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def test_ai_output_grounding_dataset_exists():
    assert AI_OUTPUT_GROUNDING_DATA_PATH.exists(), (
        "AI output grounding dataset file is missing."
    )


def test_ai_output_grounding_dataset_is_not_empty():
    cases = load_ai_output_grounding_cases()

    assert isinstance(cases, list), "AI output grounding dataset must be a list."
    assert len(cases) > 0, "AI output grounding dataset must contain at least one case."


def test_each_ai_output_grounding_case_has_required_fields():
    required_fields = {
        "id",
        "scenario",
        "description",
        "user_request",
        "provided_evidence",
        "ai_output",
        "unsupported_claims",
        "grounding_status",
        "hallucination_risk",
        "expected_quality",
        "safe_action",
    }

    for case in load_ai_output_grounding_cases():
        missing_fields = required_fields - set(case)

        assert not missing_fields, (
            f"AI output grounding case {case.get('id', '<missing id>')} "
            f"is missing fields: {missing_fields}"
        )


def test_ai_output_grounding_ids_are_unique():
    cases = load_ai_output_grounding_cases()
    ids = [case["id"] for case in cases]

    assert len(ids) == len(set(ids)), "AI output grounding case IDs must be unique."


def test_controlled_values_are_used():
    for case in load_ai_output_grounding_cases():
        assert case["grounding_status"] in VALID_GROUNDING_STATUSES, (
            f"{case['id']} has invalid grounding status: {case['grounding_status']}"
        )
        assert case["hallucination_risk"] in VALID_HALLUCINATION_RISKS, (
            f"{case['id']} has invalid hallucination risk: {case['hallucination_risk']}"
        )
        assert case["expected_quality"] in VALID_QUALITY_LEVELS, (
            f"{case['id']} has invalid expected quality: {case['expected_quality']}"
        )


def test_provided_evidence_is_required():
    for case in load_ai_output_grounding_cases():
        assert isinstance(case["provided_evidence"], list), (
            f"{case['id']} provided_evidence must be a list."
        )
        assert len(case["provided_evidence"]) >= 1, (
            f"{case['id']} must include at least one evidence item."
        )


def test_ai_output_is_meaningful():
    for case in load_ai_output_grounding_cases():
        output = case["ai_output"].strip()

        assert len(output) >= 60, (
            f"{case['id']} AI output is too short to evaluate grounding."
        )


def test_unsupported_claims_are_structured_as_list():
    for case in load_ai_output_grounding_cases():
        assert isinstance(case["unsupported_claims"], list), (
            f"{case['id']} unsupported_claims must be a list."
        )


def test_fully_grounded_outputs_have_no_unsupported_claims():
    for case in load_ai_output_grounding_cases():
        if case["grounding_status"] == "fully_grounded":
            assert len(case["unsupported_claims"]) == 0, (
                f"{case['id']} fully grounded outputs should not have unsupported claims."
            )
            assert case["hallucination_risk"] == "low", (
                f"{case['id']} fully grounded outputs should be low hallucination risk."
            )


def test_outputs_with_unsupported_claims_are_not_high_quality():
    for case in load_ai_output_grounding_cases():
        if len(case["unsupported_claims"]) > 0:
            assert case["expected_quality"] != "high", (
                f"{case['id']} outputs with unsupported claims cannot be high quality."
            )


def test_ungrounded_outputs_are_low_quality_and_high_risk():
    for case in load_ai_output_grounding_cases():
        if case["grounding_status"] == "ungrounded":
            assert case["expected_quality"] == "low", (
                f"{case['id']} ungrounded outputs should be low quality."
            )
            assert case["hallucination_risk"] in {"high", "critical"}, (
                f"{case['id']} ungrounded outputs should be high or critical risk."
            )


def test_fabricated_sources_are_critical_or_rejected():
    source_terms = {"report", "source", "document", "according to"}

    for case in load_ai_output_grounding_cases():
        combined_unsupported_claims = " ".join(case["unsupported_claims"]).lower()
        ai_output = case["ai_output"].lower()

        if any(term in combined_unsupported_claims for term in source_terms):
            assert case["hallucination_risk"] == "critical", (
                f"{case['id']} fabricated source references should be critical risk."
            )
            assert "reject" in case["safe_action"].lower(), (
                f"{case['id']} fabricated source references should be rejected."
            )

        if "according to" in ai_output and len(case["unsupported_claims"]) > 0:
            assert case["hallucination_risk"] == "critical", (
                f"{case['id']} unsupported cited claims should be critical risk."
            )


def test_inference_presented_as_fact_requires_rewrite_or_qualification():
    inference_terms = {"likely", "suggests", "may", "possible", "further evidence"}

    for case in load_ai_output_grounding_cases():
        if case["grounding_status"] in {"partially_grounded", "weakly_grounded"}:
            safe_action = case["safe_action"].lower()

            assert "rewrite" in safe_action or "qualification" in safe_action or "evidence" in safe_action, (
                f"{case['id']} partially/weakly grounded outputs require rewrite, "
                "qualification or explicit evidence handling."
            )

            if case["hallucination_risk"] == "medium":
                assert any(term in safe_action for term in inference_terms), (
                    f"{case['id']} medium-risk outputs should handle uncertainty explicitly."
                )


def test_safe_actions_are_meaningful():
    for case in load_ai_output_grounding_cases():
        safe_action = case["safe_action"].strip()

        assert len(safe_action) >= 50, (
            f"{case['id']} safe action is too short or vague."
        )


def test_low_quality_outputs_require_rejection_or_rewrite():
    for case in load_ai_output_grounding_cases():
        if case["expected_quality"] == "low":
            safe_action = case["safe_action"].lower()

            assert "reject" in safe_action or "rewrite" in safe_action, (
                f"{case['id']} low-quality outputs should be rejected or rewritten."
            )


def test_high_quality_outputs_are_low_risk_or_qualified():
    for case in load_ai_output_grounding_cases():
        if case["expected_quality"] == "high":
            assert case["hallucination_risk"] == "low", (
                f"{case['id']} high-quality outputs should be low hallucination risk."
            )
            assert case["grounding_status"] == "fully_grounded", (
                f"{case['id']} high-quality outputs should be fully grounded."
            )


def test_outputs_do_not_claim_grounding_without_evidence():
    for case in load_ai_output_grounding_cases():
        if len(case["provided_evidence"]) == 0:
            assert case["grounding_status"] != "fully_grounded", (
                f"{case['id']} cannot be fully grounded without evidence."
            )