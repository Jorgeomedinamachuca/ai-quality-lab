import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/ai_review_workflow.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 010 — Human-in-the-Loop AI Review Workflow", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays AI output, evidence and review controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Human-in-the-Loop AI Review Workflow" })).toBeVisible();

    await expect(page.getByTestId("ai-output")).toContainText("AI governance advisory work");
    await expect(page.getByTestId("evidence-list")).toContainText("data protection matters");
    await expect(page.getByTestId("grounding-status")).toBeVisible();
    await expect(page.getByTestId("hallucination-risk")).toBeVisible();
    await expect(page.getByTestId("review-notes")).toBeVisible();
    await expect(page.getByTestId("approve-button")).toBeVisible();
    await expect(page.getByTestId("reject-button")).toBeVisible();
    await expect(page.getByTestId("request-changes-button")).toBeVisible();
  });

  test("allows approval for fully grounded low-risk AI output", async ({ page }) => {
    await page.getByTestId("grounding-status").selectOption("fully_grounded");
    await page.getByTestId("hallucination-risk").selectOption("low");

    await expect(page.getByTestId("warning-banner")).not.toBeVisible();
    await expect(page.getByTestId("approve-button")).toBeEnabled();

    await page.getByTestId("approve-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Approved");
    await expect(page.getByTestId("success-banner")).toBeVisible();
  });

  test("blocks approval when AI output is weakly grounded", async ({ page }) => {
    await page.getByTestId("grounding-status").selectOption("weakly_grounded");
    await page.getByTestId("hallucination-risk").selectOption("low");

    await expect(page.getByTestId("warning-banner")).toBeVisible();
    await expect(page.getByTestId("approve-button")).toBeDisabled();
  });

  test("blocks approval when hallucination risk is high", async ({ page }) => {
    await page.getByTestId("grounding-status").selectOption("fully_grounded");
    await page.getByTestId("hallucination-risk").selectOption("high");

    await expect(page.getByTestId("warning-banner")).toBeVisible();
    await expect(page.getByTestId("approve-button")).toBeDisabled();
  });

  test("requires review notes before rejecting AI output", async ({ page }) => {
    await page.getByTestId("reject-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Rejection requires review notes");

    await page.getByTestId("review-notes").fill("The output contains unsupported claims and should not be approved.");
    await page.getByTestId("reject-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Rejected");
  });

  test("requires review notes before requesting changes", async ({ page }) => {
    await page.getByTestId("request-changes-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Change request requires review notes");

    await page.getByTestId("review-notes").fill("Please qualify the output and add clearer evidence references.");
    await page.getByTestId("request-changes-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Changes requested");
  });
});