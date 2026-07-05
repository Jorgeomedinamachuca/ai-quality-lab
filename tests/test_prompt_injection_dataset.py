import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET_FILE = ROOT / "data" / "security_prompts.json"

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}

VALID_CATEGORIES = {
    "instruction_override",
    "secret_extraction",
    "role_manipulation",
    "data_leakage",
    "policy_bypass",
    "jailbreak_attempt",
    "tool_misuse",
    "context_exfiltration",
}


def load_security_prompts():
    with DATASET_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def test_security_prompt_dataset_exists():
    assert DATASET_FILE.exists(), "Expected security prompt dataset to exist."


def test_security_prompt_dataset_is_not_empty():
    prompts = load_security_prompts()

    assert isinstance(prompts, list), "Security prompt dataset should be a list."
    assert len(prompts) >= 5, "Security prompt dataset should include at least five prompts."


def test_security_prompts_have_required_fields():
    prompts = load_security_prompts()

    required_fields = {
        "id",
        "category",
        "prompt",
        "risk_level",
        "expected_safe_behaviour",
        "failure_signal",
    }

    for item in prompts:
        missing_fields = required_fields - item.keys()
        assert not missing_fields, f"Prompt {item.get('id', 'UNKNOWN')} is missing fields: {missing_fields}"


def test_security_prompt_ids_are_unique():
    prompts = load_security_prompts()

    ids = [item["id"] for item in prompts]

    assert len(ids) == len(set(ids)), "Security prompt IDs should be unique."


def test_security_prompt_ids_follow_expected_prefix():
    prompts = load_security_prompts()

    for item in prompts:
        assert item["id"].startswith("PI-"), f"Prompt ID should start with PI-: {item['id']}"


def test_security_prompt_risk_levels_are_valid():
    prompts = load_security_prompts()

    for item in prompts:
        assert item["risk_level"] in VALID_RISK_LEVELS, (
            f"Invalid risk level for {item['id']}: {item['risk_level']}"
        )


def test_security_prompt_categories_are_valid():
    prompts = load_security_prompts()

    for item in prompts:
        assert item["category"] in VALID_CATEGORIES, (
            f"Invalid category for {item['id']}: {item['category']}"
        )


def test_high_and_critical_prompts_have_clear_failure_signals():
    prompts = load_security_prompts()

    high_risk_prompts = [
        item for item in prompts if item["risk_level"] in {"high", "critical"}
    ]

    assert high_risk_prompts, "Expected at least one high or critical prompt."

    for item in high_risk_prompts:
        failure_signal = item["failure_signal"].strip()

        assert len(failure_signal) >= 40, (
            f"Failure signal for {item['id']} should be specific enough to review."
        )


def test_critical_prompts_target_sensitive_risk_areas():
    prompts = load_security_prompts()

    critical_prompts = [
        item for item in prompts if item["risk_level"] == "critical"
    ]

    assert critical_prompts, "Expected at least one critical prompt."

    sensitive_terms = {
        "secret",
        "credential",
        "private",
        "hidden",
        "data",
        "token",
        "password",
    }

    for item in critical_prompts:
        combined_text = (
            item["prompt"] + " "
            + item["expected_safe_behaviour"] + " "
            + item["failure_signal"]
        ).lower()

        assert any(term in combined_text for term in sensitive_terms), (
            f"Critical prompt {item['id']} should reference sensitive risk areas."
        )
