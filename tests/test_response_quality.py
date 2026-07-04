import json
from pathlib import Path


def load_test_prompts():
    path = Path("data/test_prompts.json")
    return json.loads(path.read_text(encoding="utf-8"))


def test_prompt_dataset_has_required_fields():
    prompts = load_test_prompts()

    assert len(prompts) > 0

    required_fields = {
        "id",
        "category",
        "risk_level",
        "prompt",
        "expected_behaviour",
        "failure_signal",
    }

    for item in prompts:
        assert required_fields.issubset(item.keys())


def test_prompt_categories_are_defined():
    prompts = load_test_prompts()
    categories = {item["category"] for item in prompts}

    expected_categories = {
        "functional",
        "hallucination",
        "consistency",
        "data_leakage",
        "prompt_injection",
        "usability",
        "safety",
    }

    assert categories.issubset(expected_categories)


def test_prompt_ids_are_unique():
    prompts = load_test_prompts()
    prompt_ids = [item["id"] for item in prompts]

    assert len(prompt_ids) == len(set(prompt_ids))


def test_critical_risks_have_failure_signals():
    prompts = load_test_prompts()
    critical_prompts = [item for item in prompts if item["risk_level"] == "critical"]

    assert critical_prompts

    for item in critical_prompts:
        assert item["failure_signal"].strip()
