from playwright.sync_api import Page

class ChatbotPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def submit_prompt(self, prompt: str):
        # Replace selectors with selectors from your real chatbot UI.
        self.page.get_by_placeholder("Ask something").fill(prompt)
        self.page.get_by_role("button", name="Send").click()

    def get_latest_response(self) -> str:
        # Replace selector with the real chatbot response locator.
        return self.page.locator(".chatbot-response").last.inner_text()
