import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/ai_quality_release_dashboard.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 012 — Cross-Layer AI Quality Regression Suite", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays release dashboard controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Cross-Layer AI Quality Regression Suite" })).toBeVisible();

    await expect(page.getByTestId("release-selector")).toBeVisible();
    await expect(page.getByTestId("release-candidate")).toBeVisible();
    await expect(page.getByTestId("grounding-regression")).toBeVisible();
    await expect(page.getByTestId("hallucination-regression")).toBeVisible();
    await expect(page.getByTestId("risk-routing-regression")).toBeVisible();
    await expect(page.getByTestId("approval-control-regression")).toBeVisible();
    await expect(page.getByTestId("evidence-traceability-regression")).toBeVisible();
    await expect(page.getByTestId("critical-failures-count")).toBeVisible();
    await expect(page.getByTestId("high-risk-failures-count")).toBeVisible();
    await expect(page.getByTestId("medium-risk-failures-count")).toBeVisible();
    await expect(page.getByTestId("release-status")).toBeVisible();
    await expect(page.getByTestId("release-decision")).toBeVisible();
    await expect(page.getByTestId("review-notes")).toBeVisible();
    await expect(page.getByTestId("approve-release-button")).toBeVisible();
    await expect(page.getByTestId("signoff-button")).toBeVisible();
    await expect(page.getByTestId("escalate-release-button")).toBeVisible();
    await expect(page.getByTestId("reject-release-button")).toBeVisible();
  });

  test("allows approval for a release candidate with no AI quality regressions", async ({ page }) => {
    await page.getByTestId("release-selector").selectOption("ready");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-001");
    await expect(page.getByTestId("release-status")).toHaveText("ready_for_release");
    await expect(page.getByTestId("release-decision")).toHaveText("approve_release");
    await expect(page.getByTestId("ready-banner")).toBeVisible();

    await expect(page.getByTestId("approve-release-button")).toBeEnabled();
    await expect(page.getByTestId("signoff-button")).toBeDisabled();
    await expect(page.getByTestId("escalate-release-button")).toBeDisabled();
    await expect(page.getByTestId("reject-release-button")).toBeDisabled();

    await page.getByTestId("approve-release-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Release approved");
  });

  test("requires notes before approving a medium-risk release with sign-off", async ({ page }) => {
    await page.getByTestId("release-selector").selectOption("review");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-006");
    await expect(page.getByTestId("release-status")).toHaveText("review_required");
    await expect(page.getByTestId("release-decision")).toHaveText("approve_with_signoff");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await expect(page.getByTestId("signoff-button")).toBeEnabled();
    await page.getByTestId("signoff-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Medium-risk regression reviewed and accepted with documented sign-off.");
    await page.getByTestId("signoff-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Release approved with sign-off");
  });

  test("routes high-risk regression to escalation and requires notes", async ({ page }) => {
    await page.getByTestId("release-selector").selectOption("escalation");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-003");
    await expect(page.getByTestId("risk-routing-regression")).toHaveText("true");
    await expect(page.getByTestId("release-status")).toHaveText("requires_escalation");
    await expect(page.getByTestId("release-decision")).toHaveText("escalate_release_review");
    await expect(page.getByTestId("escalation-banner")).toBeVisible();

    await expect(page.getByTestId("approve-release-button")).toBeDisabled();
    await expect(page.getByTestId("escalate-release-button")).toBeEnabled();

    await page.getByTestId("escalate-release-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Risk routing regression requires senior review before release.");
    await page.getByTestId("escalate-release-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Release review escalated");
  });

  test("blocks release when hallucination regression creates critical failure", async ({ page }) => {
    await page.getByTestId("release-selector").selectOption("blocked");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-002");
    await expect(page.getByTestId("grounding-regression")).toHaveText("true");
    await expect(page.getByTestId("hallucination-regression")).toHaveText("true");
    await expect(page.getByTestId("critical-failures-count")).toHaveText("1");
    await expect(page.getByTestId("release-status")).toHaveText("blocked");
    await expect(page.getByTestId("release-decision")).toHaveText("reject_release");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("approve-release-button")).toBeDisabled();
    await expect(page.getByTestId("signoff-button")).toBeDisabled();
    await expect(page.getByTestId("escalate-release-button")).toBeDisabled();
    await expect(page.getByTestId("reject-release-button")).toBeEnabled();

    await page.getByTestId("reject-release-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Critical hallucination regression blocks this release candidate.");
    await page.getByTestId("reject-release-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Release rejected");
  });

  test("updates release attributes when selected release candidate changes", async ({ page }) => {
    await page.getByTestId("release-selector").selectOption("ready");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-001");
    await expect(page.getByTestId("release-status")).toHaveText("ready_for_release");
    await expect(page.getByTestId("critical-failures-count")).toHaveText("0");

    await page.getByTestId("release-selector").selectOption("escalation");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-003");
    await expect(page.getByTestId("risk-routing-regression")).toHaveText("true");
    await expect(page.getByTestId("release-status")).toHaveText("requires_escalation");
    await expect(page.getByTestId("high-risk-failures-count")).toHaveText("1");

    await page.getByTestId("release-selector").selectOption("blocked");

    await expect(page.getByTestId("release-candidate")).toHaveText("RC-2026-002");
    await expect(page.getByTestId("hallucination-regression")).toHaveText("true");
    await expect(page.getByTestId("release-status")).toHaveText("blocked");
    await expect(page.getByTestId("release-decision")).toHaveText("reject_release");
  });
});