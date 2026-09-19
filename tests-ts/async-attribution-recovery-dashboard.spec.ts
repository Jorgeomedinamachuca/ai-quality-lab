import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/async_attribution_recovery_dashboard.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 014 — Hot-Path Latency and Deferred Attribution Guardrail", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays async attribution recovery dashboard controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Hot-Path Latency and Deferred Attribution Guardrail" })).toBeVisible();

    await expect(page.getByTestId("case-selector")).toBeVisible();
    await expect(page.getByTestId("user-facing-response")).toBeVisible();
    await expect(page.getByTestId("downstream-dependency-status")).toBeVisible();
    await expect(page.getByTestId("attribution-status")).toBeVisible();
    await expect(page.getByTestId("deferred-record-created")).toBeVisible();
    await expect(page.getByTestId("background-recovery-required")).toBeVisible();
    await expect(page.getByTestId("retryable-failure")).toBeVisible();
    await expect(page.getByTestId("audit-evidence-present")).toBeVisible();
    await expect(page.getByTestId("data-loss-risk")).toBeVisible();
    await expect(page.getByTestId("quality-status")).toBeVisible();
    await expect(page.getByTestId("review-notes")).toBeVisible();
    await expect(page.getByTestId("accept-button")).toBeVisible();
    await expect(page.getByTestId("recovery-button")).toBeVisible();
    await expect(page.getByTestId("review-button")).toBeVisible();
    await expect(page.getByTestId("block-button")).toBeVisible();
  });

  test("allows accepting immediate attribution with fast response", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("immediate");

    await expect(page.getByTestId("user-facing-response")).toHaveText("fast");
    await expect(page.getByTestId("downstream-dependency-status")).toHaveText("available");
    await expect(page.getByTestId("attribution-status")).toHaveText("completed");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("valid-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeEnabled();
    await expect(page.getByTestId("recovery-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeDisabled();

    await page.getByTestId("accept-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Workflow accepted");
  });

  test("requires notes for deferred attribution recovery", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("deferred");

    await expect(page.getByTestId("user-facing-response")).toHaveText("fast");
    await expect(page.getByTestId("downstream-dependency-status")).toHaveText("temporarily_unavailable");
    await expect(page.getByTestId("attribution-status")).toHaveText("deferred");
    await expect(page.getByTestId("deferred-record-created")).toHaveText("true");
    await expect(page.getByTestId("background-recovery-required")).toHaveText("true");
    await expect(page.getByTestId("retryable-failure")).toHaveText("true");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("recovery_pending");
    await expect(page.getByTestId("recovery-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("recovery-button")).toBeEnabled();

    await page.getByTestId("recovery-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Attribution was deferred with audit evidence and remains retryable.");
    await page.getByTestId("recovery-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Recovery pending");
  });

  test("routes slow synchronous dependency path to review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("slow");

    await expect(page.getByTestId("user-facing-response")).toHaveText("slow");
    await expect(page.getByTestId("downstream-dependency-status")).toHaveText("slow");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeEnabled();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("The user-facing workflow is blocked by synchronous dependency work.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Workflow reviewed");
  });

  test("accepts recovered attribution with preserved audit evidence", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("recovered");

    await expect(page.getByTestId("user-facing-response")).toHaveText("fast");
    await expect(page.getByTestId("attribution-status")).toHaveText("recovered");
    await expect(page.getByTestId("deferred-record-created")).toHaveText("true");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
    await expect(page.getByTestId("data-loss-risk")).toHaveText("none");
    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("valid-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeEnabled();

    await page.getByTestId("accept-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Workflow accepted");
  });

  test("routes failed retryable recovery to review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("failed-retryable");

    await expect(page.getByTestId("attribution-status")).toHaveText("recovery_failed");
    await expect(page.getByTestId("deferred-record-created")).toHaveText("true");
    await expect(page.getByTestId("retryable-failure")).toHaveText("true");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await expect(page.getByTestId("review-button")).toBeEnabled();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Recovery failed but remains retryable with audit evidence preserved.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Workflow reviewed");
  });

  test("blocks workflow when attribution is lost", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("lost");

    await expect(page.getByTestId("downstream-dependency-status")).toHaveText("failed");
    await expect(page.getByTestId("attribution-status")).toHaveText("lost");
    await expect(page.getByTestId("deferred-record-created")).toHaveText("false");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("false");
    await expect(page.getByTestId("data-loss-risk")).toHaveText("critical");
    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("block-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Attribution was lost and no recovery evidence was preserved.");
    await page.getByTestId("block-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Workflow blocked");
  });

  test("updates attribution attributes when selected case changes", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("immediate");

    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("attribution-status")).toHaveText("completed");

    await page.getByTestId("case-selector").selectOption("deferred");

    await expect(page.getByTestId("quality-status")).toHaveText("recovery_pending");
    await expect(page.getByTestId("attribution-status")).toHaveText("deferred");

    await page.getByTestId("case-selector").selectOption("failed-retryable");

    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("attribution-status")).toHaveText("recovery_failed");

    await page.getByTestId("case-selector").selectOption("lost");

    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("attribution-status")).toHaveText("lost");
  });
});
