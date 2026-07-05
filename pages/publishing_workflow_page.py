from pathlib import Path


class PublishingWorkflowPage:
    def __init__(self, page):
        self.page = page
        self.demo_path = Path(__file__).resolve().parents[1] / "demo" / "publishing_workflow.html"

    def open(self):
        self.page.goto(self.demo_path.as_uri())

    def select_role(self, role):
        self.page.get_by_test_id("role-select").select_option(role)

    def fill_title(self, title):
        self.page.get_by_test_id("title-input").fill(title)

    def fill_body(self, body):
        self.page.get_by_test_id("body-input").fill(body)

    def save_draft(self):
        self.page.get_by_test_id("save-draft-button").click()

    def submit_for_review(self):
        self.page.get_by_test_id("submit-review-button").click()

    def publish(self):
        self.page.get_by_test_id("publish-button").click()

    def publish_button(self):
        return self.page.get_by_test_id("publish-button")

    def validation_message(self):
        return self.page.get_by_test_id("validation-message").inner_text()

    def workflow_status(self):
        return self.page.get_by_test_id("workflow-status").inner_text()

    def preview_title(self):
        return self.page.get_by_test_id("preview-title").inner_text()

    def preview_body(self):
        return self.page.get_by_test_id("preview-body").inner_text()

    def preview_body_html(self):
        return self.page.get_by_test_id("preview-body").inner_html()
