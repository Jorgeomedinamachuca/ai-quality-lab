from urllib.parse import quote

from playwright.sync_api import Page, expect

from pages.chatbot_page import ChatbotPage


def test_chatbot_page_loads(page: Page):
    html = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>AI Chatbot Test Fixture</title>
      </head>
      <body>
        <h1>AI Chatbot Test Fixture</h1>
        <p>This local fixture validates the chatbot page object without using an external website.</p>
      </body>
    </html>
    """

    chatbot = ChatbotPage(page)
    chatbot.open(f"data:text/html,{quote(html)}")

    expect(page.get_by_role("heading", name="AI Chatbot Test Fixture")).to_be_visible()