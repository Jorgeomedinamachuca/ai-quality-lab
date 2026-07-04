import pytest

pytest.importorskip("pytest_playwright")

from playwright.sync_api import Page, expect
from pages.chatbot_page import ChatbotPage


def test_chatbot_page_loads(page: Page):
    # Replace this URL with your own demo chatbot or test environment.
    chatbot = ChatbotPage(page)
    chatbot.open("https://example.com")

    # Example placeholder assertion.
    expect(page.get_by_role("heading")).to_be_visible()
