from urllib.parse import quote

from playwright.sync_api import Page, expect


def test_basic_navigation(page: Page):
    html = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>AI Quality Lab Navigation Fixture</title>
      </head>
      <body>
        <h1>AI Quality Lab Navigation Fixture</h1>
        <p>This local fixture avoids dependency on external websites.</p>
      </body>
    </html>
    """

    page.goto(f"data:text/html,{quote(html)}")

    expect(page).to_have_title("AI Quality Lab Navigation Fixture")
    expect(
        page.get_by_role("heading", name="AI Quality Lab Navigation Fixture")
    ).to_be_visible()