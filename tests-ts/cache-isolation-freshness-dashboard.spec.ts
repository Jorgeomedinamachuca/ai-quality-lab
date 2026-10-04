import { expect, test } from "@playwright/test";
import path from "path";

const demoPath = path.resolve(__dirname, "../demo/cache_isolation_freshness_dashboard.html");
const demoUrl = `file://${demoPath}`;

test.describe("Experiment 015 — Cache Isolation and Freshness Guardrail", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(demoUrl);
  });

  test("displays cache isolation and freshness dashboard controls", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Cache Isolation and Freshness Guardrail" })).toBeVisible();

    await expect(page.getByTestId("case-selector")).toBeVisible();
    await expect(page.getByTestId("cache-status")).toBeVisible();
    await expect(page.getByTestId("context-isolated")).toBeVisible();
    await expect(page.getByTestId("cache-key-scope")).toBeVisible();
    await expect(page.getByTestId("freshness-status")).toBeVisible();
    await expect(page.getByTestId("fallback-required")).toBeVisible();
    await expect(page.getByTestId("data-leakage-risk")).toBeVisible();
    await expect(page.getByTestId("stale-data-risk")).toBeVisible();
    await expect(page.getByTestId("audit-evidence-present")).toBeVisible();
    await expect(page.getByTestId("quality-status")).toBeVisible();

    await expect(page.getByTestId("review-notes")).toBeVisible();
    await expect(page.getByTestId("accept-button")).toBeVisible();
    await expect(page.getByTestId("fallback-button")).toBeVisible();
    await expect(page.getByTestId("review-button")).toBeVisible();
    await expect(page.getByTestId("block-button")).toBeVisible();
  });

  test("allows accepting a fresh isolated cache hit", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("fresh-hit");

    await expect(page.getByTestId("cache-status")).toHaveText("hit");
    await expect(page.getByTestId("context-isolated")).toHaveText("true");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("user_and_tenant");
    await expect(page.getByTestId("freshness-status")).toHaveText("fresh");
    await expect(page.getByTestId("fallback-required")).toHaveText("false");
    await expect(page.getByTestId("data-leakage-risk")).toHaveText("none");
    await expect(page.getByTestId("stale-data-risk")).toHaveText("none");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("valid-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeEnabled();
    await expect(page.getByTestId("fallback-button")).toBeDisabled();
    await expect(page.getByTestId("review-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeDisabled();

    await page.getByTestId("accept-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache result accepted");
  });

  test("routes cache miss to safe fallback", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("cache-miss");

    await expect(page.getByTestId("cache-status")).toHaveText("miss");
    await expect(page.getByTestId("context-isolated")).toHaveText("true");
    await expect(page.getByTestId("freshness-status")).toHaveText("not_applicable");
    await expect(page.getByTestId("fallback-required")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("fallback_required");
    await expect(page.getByTestId("fallback-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("fallback-button")).toBeEnabled();

    await page.getByTestId("fallback-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Cache miss handled through safe fallback with context isolation preserved.");
    await page.getByTestId("fallback-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Fallback path selected");
  });

  test("routes stale cache entry to review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("stale-entry");

    await expect(page.getByTestId("cache-status")).toHaveText("hit");
    await expect(page.getByTestId("freshness-status")).toHaveText("stale");
    await expect(page.getByTestId("fallback-required")).toHaveText("true");
    await expect(page.getByTestId("stale-data-risk")).toHaveText("medium");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await expect(page.getByTestId("review-button")).toBeEnabled();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Stale cache entry requires refresh before cached enrichment data is trusted.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache workflow reviewed");
  });

  test("blocks tenant-only cache key when user isolation is missing", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("tenant-only");

    await expect(page.getByTestId("cache-status")).toHaveText("hit");
    await expect(page.getByTestId("context-isolated")).toHaveText("false");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("tenant_only");
    await expect(page.getByTestId("data-leakage-risk")).toHaveText("high");
    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeDisabled();
    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("block-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Tenant-only cache key is unsafe for user-specific cached enrichment data.");
    await page.getByTestId("block-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache usage blocked");
  });

  test("blocks global cache key for context-specific data", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("global-key");

    await expect(page.getByTestId("cache-status")).toHaveText("hit");
    await expect(page.getByTestId("context-isolated")).toHaveText("false");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("global");
    await expect(page.getByTestId("data-leakage-risk")).toHaveText("critical");
    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("blocked-banner")).toBeVisible();

    await expect(page.getByTestId("block-button")).toBeEnabled();

    await page.getByTestId("review-notes").fill("Global cache key must not serve context-specific enrichment data.");
    await page.getByTestId("block-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache usage blocked");
  });

  test("routes fresh cache entry without audit evidence to review", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("missing-audit");

    await expect(page.getByTestId("cache-status")).toHaveText("hit");
    await expect(page.getByTestId("freshness-status")).toHaveText("fresh");
    await expect(page.getByTestId("audit-evidence-present")).toHaveText("false");
    await expect(page.getByTestId("fallback-required")).toHaveText("true");
    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("review-banner")).toBeVisible();

    await page.getByTestId("review-button").click();
    await expect(page.getByTestId("workflow-status")).toHaveText("Review notes required");

    await page.getByTestId("review-notes").fill("Freshness cannot be trusted without audit evidence.");
    await page.getByTestId("review-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache workflow reviewed");
  });

  test("routes expired cache entry to fallback path", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("expired-entry");

    await expect(page.getByTestId("cache-status")).toHaveText("expired");
    await expect(page.getByTestId("freshness-status")).toHaveText("expired");
    await expect(page.getByTestId("fallback-required")).toHaveText("true");
    await expect(page.getByTestId("stale-data-risk")).toHaveText("medium");
    await expect(page.getByTestId("quality-status")).toHaveText("fallback_required");
    await expect(page.getByTestId("fallback-banner")).toBeVisible();

    await page.getByTestId("review-notes").fill("Expired cache entry should use safe refresh or fallback.");
    await page.getByTestId("fallback-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Fallback path selected");
  });

  test("allows disabled cache when direct lookup preserves isolation", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("disabled-cache");

    await expect(page.getByTestId("cache-status")).toHaveText("disabled");
    await expect(page.getByTestId("context-isolated")).toHaveText("true");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("disabled");
    await expect(page.getByTestId("freshness-status")).toHaveText("not_applicable");
    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("valid-banner")).toBeVisible();

    await expect(page.getByTestId("accept-button")).toBeEnabled();

    await page.getByTestId("accept-button").click();

    await expect(page.getByTestId("workflow-status")).toHaveText("Cache result accepted");
  });

  test("updates cache attributes when selected case changes", async ({ page }) => {
    await page.getByTestId("case-selector").selectOption("fresh-hit");

    await expect(page.getByTestId("quality-status")).toHaveText("valid");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("user_and_tenant");

    await page.getByTestId("case-selector").selectOption("cache-miss");

    await expect(page.getByTestId("quality-status")).toHaveText("fallback_required");
    await expect(page.getByTestId("cache-status")).toHaveText("miss");

    await page.getByTestId("case-selector").selectOption("stale-entry");

    await expect(page.getByTestId("quality-status")).toHaveText("requires_review");
    await expect(page.getByTestId("freshness-status")).toHaveText("stale");

    await page.getByTestId("case-selector").selectOption("global-key");

    await expect(page.getByTestId("quality-status")).toHaveText("blocked");
    await expect(page.getByTestId("cache-key-scope")).toHaveText("global");
  });
});