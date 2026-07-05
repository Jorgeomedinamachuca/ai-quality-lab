import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
USER_STORIES_FILE = ROOT / "data" / "user_stories.json"

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}


def load_user_stories():
    with USER_STORIES_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def test_user_stories_dataset_exists():
    assert USER_STORIES_FILE.exists(), "Expected user_stories.json dataset to exist."


def test_user_stories_dataset_is_not_empty():
    stories = load_user_stories()

    assert isinstance(stories, list), "User stories dataset should be a list."
    assert len(stories) >= 3, "Expected at least three user stories."


def test_user_stories_have_required_fields():
    stories = load_user_stories()

    required_fields = {
        "id",
        "title",
        "persona",
        "goal",
        "benefit",
        "description",
        "acceptance_criteria",
        "business_rules",
        "edge_cases",
        "negative_scenarios",
        "security_considerations",
        "testability_notes",
        "risk_level",
    }

    for story in stories:
        missing_fields = required_fields - story.keys()
        assert not missing_fields, (
            f"User story {story.get('id', 'UNKNOWN')} is missing fields: {missing_fields}"
        )


def test_user_story_ids_are_unique_and_follow_prefix():
    stories = load_user_stories()

    ids = [story["id"] for story in stories]

    assert len(ids) == len(set(ids)), "User story IDs should be unique."

    for story_id in ids:
        assert story_id.startswith("US-"), f"User story ID should start with US-: {story_id}"


def test_user_stories_define_persona_goal_and_benefit():
    stories = load_user_stories()

    for story in stories:
        assert story["persona"].strip(), f"{story['id']} should define a persona."
        assert story["goal"].strip(), f"{story['id']} should define a goal."
        assert story["benefit"].strip(), f"{story['id']} should define a benefit."


def test_acceptance_criteria_are_defined_and_testable():
    stories = load_user_stories()

    for story in stories:
        criteria = story["acceptance_criteria"]

        assert isinstance(criteria, list), f"{story['id']} acceptance criteria should be a list."
        assert len(criteria) >= 3, f"{story['id']} should include at least three acceptance criteria."

        combined_criteria = " ".join(criteria).lower()

        assert "given" in combined_criteria, f"{story['id']} should include Given-style context."
        assert "when" in combined_criteria, f"{story['id']} should include When-style action."
        assert "then" in combined_criteria, f"{story['id']} should include Then-style outcome."


def test_business_rules_negative_scenarios_and_edge_cases_are_present():
    stories = load_user_stories()

    for story in stories:
        assert len(story["business_rules"]) >= 2, (
            f"{story['id']} should include at least two business rules."
        )
        assert len(story["negative_scenarios"]) >= 2, (
            f"{story['id']} should include at least two negative scenarios."
        )
        assert len(story["edge_cases"]) >= 2, (
            f"{story['id']} should include at least two edge cases."
        )


def test_risk_levels_are_valid():
    stories = load_user_stories()

    for story in stories:
        assert story["risk_level"] in VALID_RISK_LEVELS, (
            f"Invalid risk level for {story['id']}: {story['risk_level']}"
        )


def test_high_and_critical_stories_include_security_considerations():
    stories = load_user_stories()

    high_risk_stories = [
        story for story in stories if story["risk_level"] in {"high", "critical"}
    ]

    assert high_risk_stories, "Expected at least one high or critical risk story."

    for story in high_risk_stories:
        assert len(story["security_considerations"]) >= 2, (
            f"{story['id']} should include security considerations."
        )


def test_user_stories_include_testability_notes():
    stories = load_user_stories()

    for story in stories:
        notes = story["testability_notes"]

        assert isinstance(notes, list), f"{story['id']} testability notes should be a list."
        assert len(notes) >= 2, f"{story['id']} should include at least two testability notes."


def test_critical_user_stories_reference_access_or_security_risk():
    stories = load_user_stories()

    critical_stories = [
        story for story in stories if story["risk_level"] == "critical"
    ]

    assert critical_stories, "Expected at least one critical user story."

    sensitive_terms = {
        "role",
        "access",
        "permission",
        "security",
        "safe",
        "script",
        "unauthorised",
        "ownership",
    }

    for story in critical_stories:
        combined_text = " ".join(
            story["business_rules"]
            + story["negative_scenarios"]
            + story["security_considerations"]
            + story["testability_notes"]
        ).lower()

        assert any(term in combined_text for term in sensitive_terms), (
            f"{story['id']} should reference access, permission or security risk."
        )
