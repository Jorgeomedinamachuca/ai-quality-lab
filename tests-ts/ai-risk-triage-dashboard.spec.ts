import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/ai_risk_triage_dashboard.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 011 — AI Risk Triage and Review Routing", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays risk triage dashboard controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "AI Risk Triage and Review Routing" })).toBeVisible();

    await expect(page.getByTestId("case-selector")).toBeVisible();
    await expect(page.getByTestId("grounding-status")).toBeVisible();
    await expect(page.getByTestId("hallucination-risk")).toBeVisible();
    await expect(page.getByTestId("unsupported-claims-count")).toBeVisible();
    await expect(page.getByTestId("evidence-items-count")).toBeVisible();
    await expect(page.getByTestId("risk-level")).toBeVisible();
    await expect(page.getByTestId("review-route")).toBeVisible();
    await expect(page.getByTestId("approval-policy")).toBeVisible();
    await expect(page.getByTestId("approve-button")).toBeVisible();
    await expect(page.getByTestId("escalate-button")).toBeVisible();
    await expect(page.getByTestId("block-button")).toBeVisible();
  });

  test("routes low-risk output to standard review and allows approval", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("low");

    await expect(page.getByTestId("risk-level")).toHaveText("low");
    await expect(page.getByTestId("review-route")).toHaveText("standard_review");
    await expect(page.getByTestId("approval-policy")).toHaveText("approval_allowed");
    await expect(page.getByTestId("standard-banner")).toBeVisible();

    await expect(page.getByTestId("approve-button")).toBeEnabled();
    await expect(page.getByTestId("escalate-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeDisabled();

    await page.getByTestId("approve-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Approved");
  });

  test("routes medium-risk output to review with notes", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("medium");

    await expect(page.getByTestId("risk-level")).toHaveText("medium");
    await expect(page.getByTestId("review-route")).toHaveText("review_with_notes");
    await expect(page.getByTestId("approval-policy")).toHaveText("approval_requires_notes");
    await expect(page.getByTestId("notes-banner")).toBeVisible();

    await expect(page.getByTestId("approve-button")).toBeEnabled();

    await page.getByTestId("approve-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Approval requires reviewer notes");

    await page.getByTestId("review-notes").fill("The output is partially grounded and requires reviewer justification.");
    await page.getByTestId("approve-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Approved");
  });

  test("routes high-risk output to senior review and blocks direct approval", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("high");

    await expect(page.getByTestId("risk-level")).toHaveText("high");
    await expect(page.getByTestId("review-route")).toHaveText("senior_review");
    await expect(page.getByTestId("approval-policy")).toHaveText("approval_blocked_pending_escalation");
    await expect(page.getByTestId("senior-banner")).toBeVisible();

    await expect(page.getByTestId("approve-button")).toBeDisabled();
    await expect(page.getByTestId("escalate-button")).toBeEnabled();

    await page.getByTestId("escalate-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Escalated to senior review");
  });

  test("routes critical-risk output to blocked state", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("critical");

    await expect(page.getByTestId("risk-level")).toHaveText("critical");
    await expect(page.getByTestId("review-route")).toHaveText("blocked");
    await expect(page.getByTestId("approval-policy")).toHaveText("approval_not_allowed");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("approve-button")).toBeDisabled();
    await expect(page.getByTestId("escalate-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("block-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Blocked");
  });

  test("updates visible risk attributes when case selection changes", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("medium");

    await expect(page.getByTestId("grounding-status")).toHaveText("partially_grounded");
    await expect(page.getByTestId("hallucination-risk")).toHaveText("medium");
    await expect(page.getByTestId("unsupported-claims-count")).toHaveText("1");
    await expect(page.getByTestId("evidence-items-count")).toHaveText("3");

    await page.getByTestId("case-selector").selectOption("critical");

    await expect(page.getByTestId("grounding-status")).toHaveText("ungrounded");
    await expect(page.getByTestId("hallucination-risk")).toHaveText("critical");
    await expect(page.getByTestId("unsupported-claims-count")).toHaveText("3");
    await expect(page.getByTestId("evidence-items-count")).toHaveText("1");
  });
});