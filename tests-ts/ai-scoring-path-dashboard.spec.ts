import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/ai_scoring_path_dashboard.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 013 — AI Scoring Path Consistency Guardrail", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays scoring path dashboard controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "AI Scoring Path Consistency Guardrail" })).toBeVisible();

    await expect(page.getByTestId("case-selector")).toBeVisible();
    await expect(page.getByTestId("record-group")).toBeVisible();
    await expect(page.getByTestId("expected-scoring-path")).toBeVisible();
    await expect(page.getByTestId("actual-scoring-paths")).toBeVisible();
    await expect(page.getByTestId("scoring-provenance-present")).toBeVisible();
    await expect(page.getByTestId("retry-used")).toBeVisible();
    await expect(page.getByTestId("manual-review-required")).toBeVisible();
    await expect(page.getByTestId("mixed-path-detected")).toBeVisible();
    await expect(page.getByTestId("risk-level")).toBeVisible();
    await expect(page.getByTestId("quality-status")).toBeVisible();
    await expect(page.getByTestId("review-notes")).toBeVisible();
    await expect(page.getByTestId("accept-button")).toBeVisible();
    await expect(page.getByTestId("review-button")).toBeVisible();
    await expect(page.getByTestId("block-button")).toBeVisible();
  });

  test("allows accepting a valid consistent scoring path", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("valid-ai");

    await expect(page.getByTestId("expected-scoring-path")).toHaveText("ai_scoring");
    await expect(page.getByTestId("actual-scoring-paths")).toHaveText("ai_scoring");
    await expect(page.getByTestId("scoring-provenance-present")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("valid-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeEnabled();
    await expect(page.getByTestId("review-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeDisabled();

    await page.getByTestId("accept-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Scoring result accepted");
  });

  test("requires notes when retry path needs review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("retry-review");

    await expect(page.getByTestId("retry-used")).toHaveText("true");
    await expect(page.getByTestId("manual-review-required")).toHaveText("true");
    await expect(page.getByTestId("risk-level")).toHaveText("medium");
    await expect(page.getByTestId("quality-status")).toHaveText("review_required");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeEnabled();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Retry was used, but provenance is explicit and the scoring path is traceable.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Scoring result reviewed");
  });

  test("routes mixed scoring paths to manual review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("mixed-path");

    await expect(page.getByTestId("actual-scoring-paths")).toHaveText("ai_scoring, rule_based_scoring");
    await expect(page.getByTestId("mixed-path-detected")).toHaveText("true");
    await expect(page.getByTestId("risk-level")).toHaveText("high");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("escalation-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeEnabled();
    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Mixed scoring paths require manual review before downstream use.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Scoring result reviewed");
  });

  test("blocks scoring result when provenance is missing", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("missing-provenance");

    await expect(page.getByTestId("actual-scoring-paths")).toHaveText("none");
    await expect(page.getByTestId("scoring-provenance-present")).toHaveText("false");
    await expect(page.getByTestId("risk-level")).toHaveText("critical");
    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("block-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Missing scoring provenance means the scoring path cannot be verified.");
    await page.getByTestId("block-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Scoring result blocked");
  });

  test("updates scoring path attributes when selected case changes", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("valid-ai");

    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("mixed-path-detected")).toHaveText("false");

    await page.getByTestId("case-selector").selectOption("retry-review");

    await expect(page.getByTestId("retry-used")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("review_required");

    await page.getByTestId("case-selector").selectOption("mixed-path");

    await expect(page.getByTestId("actual-scoring-paths")).toHaveText("ai_scoring, rule_based_scoring");
    await expect(page.getByTestId("mixed-path-detected")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");

    await page.getByTestId("case-selector").selectOption("missing-provenance");

    await expect(page.getByTestId("scoring-provenance-present")).toHaveText("false");
    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
  });
});
