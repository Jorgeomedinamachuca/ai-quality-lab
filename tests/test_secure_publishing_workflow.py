from pages.publishing_workflow_page import PublishingWorkflowPage


def test_author_can_save_draft_and_submit_for_review(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    workflow.select_role("author")
    workflow.fill_title("AI Quality Engineering Notes")
    workflow.fill_body("This draft describes quality risks in AI-powered applications.")

    workflow.save_draft()

    assert workflow.workflow_status() == "Status: Draft saved"
    assert workflow.preview_title() == "AI Quality Engineering Notes"
    assert "quality risks" in workflow.preview_body()

    workflow.submit_for_review()

    assert workflow.workflow_status() == "Status: Submitted for review"


def test_author_cannot_publish_content(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    workflow.select_role("author")
    workflow.fill_title("Draft by Author")
    workflow.fill_body("This content should require editor approval.")

    workflow.submit_for_review()

    assert workflow.workflow_status() == "Status: Submitted for review"
    assert workflow.publish_button().is_disabled()


def test_editor_can_publish_content_after_review_submission(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    workflow.select_role("editor")
    workflow.fill_title("Approved Content")
    workflow.fill_body("This content has passed review and can be published.")

    workflow.submit_for_review()

    assert workflow.publish_button().is_enabled()

    workflow.publish()

    assert workflow.workflow_status() == "Status: Published"


def test_title_is_required_before_saving_draft(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    workflow.fill_body("Body exists but title is missing.")
    workflow.save_draft()

    assert workflow.validation_message() == "Title is required before continuing."
    assert workflow.workflow_status() == "Status: Draft not saved"


def test_body_is_required_before_saving_draft(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    workflow.fill_title("Missing Body")
    workflow.save_draft()

    assert workflow.validation_message() == "Body is required before continuing."
    assert workflow.workflow_status() == "Status: Draft not saved"


def test_preview_renders_script_input_as_text_not_executable_html(page):
    workflow = PublishingWorkflowPage(page)
    workflow.open()

    unsafe_content = "<script>window.__unsafeContentExecuted = true;</script>"

    workflow.select_role("editor")
    workflow.fill_title("Safe Rendering Check")
    workflow.fill_body(unsafe_content)

    workflow.save_draft()

    assert unsafe_content in workflow.preview_body()
    assert "<script>" not in workflow.preview_body_html()

    script_executed = page.evaluate("window.__unsafeContentExecuted === true")
    assert script_executed is False
