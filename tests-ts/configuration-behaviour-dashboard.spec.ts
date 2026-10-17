
import { expect, test } from "@playwright/test";
import path from "path";
import { pathToFileURL } from "url";

const demoPath = path.resolve(
  __dirname,
  "../demo/configuration_behaviour_dashboard.html"
);

const demoUrl = pathToFileURL(demoPath).href;

test.describe(
  "Experiment 016 — Configuration-Driven Behaviour Guardrail",
  () => {
    test.beforeEach(async ({ page }) => {
      await page.goto(demoUrl);
    });

    test("displays configuration dashboard controls", async ({ page }) => {
      await expect(
        page.getByRole("heading", {
          name: "Configuration-Driven Behaviour Guardrail",
        })
      ).toBeVisible();

      await expect(page.getByTestId("case-selector")).toBeVisible();
      await expect(page.getByTestId("environment")).toBeVisible();
      await expect(page.getByTestId("configuration-status")).toBeVisible();
      await expect(page.getByTestId("feature-flag-status")).toBeVisible();
      await expect(page.getByTestId("environment-isolated")).toBeVisible();
      await expect(page.getByTestId("audit-evidence-present")).toBeVisible();
      await expect(page.getByTestId("quality-status")).toBeVisible();
      await expect(page.getByTestId("review-notes")).toBeVisible();
      await expect(page.getByTestId("accept-button")).toBeVisible();
      await expect(page.getByTestId("fallback-button")).toBeVisible();
      await expect(page.getByTestId("review-button")).toBeVisible();
      await expect(page.getByTestId("block-button")).toBeVisible();

      await expect(page.getByTestId("case-selector").locator("option")).toHaveCount(8);
    });

    test("accepts verified configuration", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-001");

      await expect(page.getByTestId("environment")).toHaveText("test");
      await expect(page.getByTestId("configuration-status")).toHaveText("valid");
      await expect(page.getByTestId("feature-flag-status")).toHaveText("enabled");
      await expect(page.getByTestId("environment-isolated")).toHaveText("true");
      await expect(page.getByTestId("audit-evidence-present")).toHaveText("true");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");
      await expect(page.getByTestId("valid-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeEnabled();
      await expect(page.getByTestId("fallback-button")).toBeDisabled();
      await expect(page.getByTestId("review-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeDisabled();

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration accepted"
      );
    });

    test("accepts intentionally disabled feature", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-002");

      await expect(page.getByTestId("configuration-status")).toHaveText("valid");
      await expect(page.getByTestId("feature-flag-status")).toHaveText("disabled");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");
      await expect(page.getByTestId("accept-button")).toBeEnabled();

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration accepted"
      );
    });

    test("requires notes before selecting safe fallback", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-003");

      await expect(page.getByTestId("configuration-status")).toHaveText("missing");
      await expect(page.getByTestId("feature-flag-status")).toHaveText("disabled");
      await expect(page.getByTestId("safe-default-applied")).toHaveText("true");
      await expect(page.getByTestId("quality-status")).toHaveText("fallback_required");
      await expect(page.getByTestId("fallback-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("fallback-button")).toBeEnabled();

      await page.getByTestId("fallback-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Review notes required"
      );

      await page.getByTestId("review-notes").fill(
        "Missing configuration detected. The affected feature remains disabled."
      );

      await page.getByTestId("fallback-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Safe fallback selected"
      );
    });

    test("routes configuration drift to review", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-004");

      await expect(page.getByTestId("configuration-status")).toHaveText(
        "drift_detected"
      );
      await expect(page.getByTestId("configuration-drift")).toHaveText("true");
      await expect(page.getByTestId("security-risk")).toHaveText("medium");
      await expect(page.getByTestId("quality-status")).toHaveText(
        "requires_review"
      );
      await expect(page.getByTestId("review-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("review-button")).toBeEnabled();

      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Review notes required"
      );

      await page.getByTestId("review-notes").fill(
        "Configuration drift requires comparison with the approved baseline."
      );

      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration marked for review"
      );
    });

    test("blocks cross-environment configuration contamination", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-005");

      await expect(page.getByTestId("environment")).toHaveText("production");
      await expect(page.getByTestId("environment-isolated")).toHaveText("false");
      await expect(page.getByTestId("configuration-drift")).toHaveText("true");
      await expect(page.getByTestId("security-risk")).toHaveText("critical");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");
      await expect(page.getByTestId("blocked-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeEnabled();

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Review notes required"
      );

      await page.getByTestId("review-notes").fill(
        "Environment isolation failed. Configuration approval is prohibited."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration blocked"
      );
    });

    test("blocks unverified feature activation", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-006");

      await expect(page.getByTestId("configuration-status")).toHaveText(
        "unverified"
      );
      await expect(page.getByTestId("feature-flag-status")).toHaveText("enabled");
      await expect(page.getByTestId("audit-evidence-present")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("high");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");

      await expect(page.getByTestId("accept-button")).toBeDisabled();

      await page.getByTestId("review-notes").fill(
        "Unverified activation has insufficient audit evidence."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration blocked"
      );
    });

    test("routes invalid configuration to safe fallback", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-007");

      await expect(page.getByTestId("configuration-status")).toHaveText("invalid");
      await expect(page.getByTestId("feature-flag-status")).toHaveText("disabled");
      await expect(page.getByTestId("safe-default-applied")).toHaveText("true");
      await expect(page.getByTestId("quality-status")).toHaveText(
        "fallback_required"
      );

      await expect(page.getByTestId("fallback-button")).toBeEnabled();

      await page.getByTestId("review-notes").fill(
        "Invalid configuration safely disabled the feature."
      );

      await page.getByTestId("fallback-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Safe fallback selected"
      );
    });

    test("accepts resolved configuration drift", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-008");

      await expect(page.getByTestId("environment")).toHaveText("production");
      await expect(page.getByTestId("configuration-status")).toHaveText("valid");
      await expect(page.getByTestId("configuration-drift")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("none");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");

      await expect(page.getByTestId("accept-button")).toBeEnabled();

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration accepted"
      );
    });

    test("resets review notes and decisions when switching scenarios", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("CDB-004");

      await page.getByTestId("review-notes").fill(
        "Review the configuration difference."
      );
      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Configuration marked for review"
      );

      await page.getByTestId("case-selector").selectOption("CDB-005");

      await expect(page.getByTestId("review-notes")).toHaveValue("");
      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Pending assessment"
      );
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");

      await expect(page.getByTestId("review-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeEnabled();
      await expect(page.getByTestId("review-banner")).toBeHidden();
      await expect(page.getByTestId("blocked-banner")).toBeVisible();
    });
  }
);
