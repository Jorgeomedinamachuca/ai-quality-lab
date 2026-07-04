from pathlib import Path


def test_demo_chatbot_loads_successfully(page):
    demo_path = Path(__file__).resolve().parents[1] / "demo" / "chatbot.html"

    page.goto(demo_path.as_uri())

    assert page.get_by_role("heading", name="AI Quality Lab Demo Chatbot").is_visible()
    assert page.get_by_test_id("prompt-input").is_visible()
    assert page.get_by_test_id("send-button").is_visible()
    assert page.get_by_test_id("response-panel").is_visible()


def test_demo_chatbot_returns_controlled_response(page):
    demo_path = Path(__file__).resolve().parents[1] / "demo" / "chatbot.html"

    page.goto(demo_path.as_uri())

    page.get_by_test_id("prompt-input").fill(
        "Explain why hallucination detection matters in AI quality engineering."
    )
    page.get_by_test_id("send-button").click()

    response = page.get_by_test_id("response-text")
    meta = page.get_by_test_id("response-meta")

    assert response.is_visible()
    assert "controlled AI-style response" in response.inner_text()
    assert "deterministic demo logic" in meta.inner_text()


def test_demo_chatbot_validates_empty_prompt(page):
    demo_path = Path(__file__).resolve().parents[1] / "demo" / "chatbot.html"

    page.goto(demo_path.as_uri())

    page.get_by_test_id("send-button").click()

    assert "Please enter a prompt" in page.get_by_test_id("response-text").inner_text()
    assert "Validation message displayed" in page.get_by_test_id("response-meta").inner_text()
