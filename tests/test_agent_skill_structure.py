from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "qa-test-case-generator"
SKILL_FILE = SKILL_DIR / "SKILL.md"
EXAMPLES_DIR = SKILL_DIR / "examples"


def test_agent_skill_file_exists():
    assert SKILL_FILE.exists(), "Expected SKILL.md to exist for the QA Test Case Generator skill."


def test_agent_skill_examples_exist():
    assert EXAMPLES_DIR.exists(), "Expected examples directory to exist."

    expected_files = [
        EXAMPLES_DIR / "sample_user_story.md",
        EXAMPLES_DIR / "expected_test_cases.md",
    ]

    for file_path in expected_files:
        assert file_path.exists(), f"Expected example file to exist: {file_path.name}"


def test_agent_skill_contains_required_sections():
    content = SKILL_FILE.read_text(encoding="utf-8")

    required_sections = [
        "## Purpose",
        "## When to Use This Skill",
        "## Expected Input",
        "## Expected Output",
        "## Output Format",
        "## Quality Rules",
        "## Safety and Reliability Rules",
        "## QA Perspective",
    ]

    for section in required_sections:
        assert section in content, f"Missing required section: {section}"


def test_agent_skill_defines_safety_boundaries():
    content = SKILL_FILE.read_text(encoding="utf-8").lower()

    required_terms = [
        "must not",
        "personal data",
        "credentials",
        "secrets",
        "assumptions",
    ]

    for term in required_terms:
        assert term in content, f"Expected safety boundary term not found: {term}"


def test_expected_output_uses_structured_test_case_format():
    expected_output = (EXAMPLES_DIR / "expected_test_cases.md").read_text(encoding="utf-8")

    required_columns = [
        "ID",
        "Test Scenario",
        "Preconditions",
        "Steps",
        "Expected Result",
        "Priority",
        "Risk Level",
        "Test Type",
    ]

    for column in required_columns:
        assert column in expected_output, f"Missing expected test case column: {column}"
