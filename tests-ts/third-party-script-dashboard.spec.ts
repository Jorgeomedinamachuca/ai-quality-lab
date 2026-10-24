
import { expect, test } from "@playwright/test";
import path from "path";
import { pathToFileURL } from "url";

const demoPath = path.resolve(
  __dirname,
  "../demo/third_party_script_dashboard.html"
);

const demoUrl = pathToFileURL(demoPath).href;

test.describe(
  "Experiment 017 — Third-Party Script Governance Guardrail",
  () => {
    test.beforeEach(async ({ page }) => {
      await page.goto(demoUrl);
    });

    test("displays all script governance controls", async ({ page }) => {
      await expect(
        page.getByRole("heading", {
          name: "Third-Party Script Governance Guardrail",
        })
      ).toBeVisible();

      await expect(page.getByTestId("case-selector")).toBeVisible();

      const fields = [
        "environment",
        "script-status",
        "source-allowlisted",
        "integrity-status",
        "execution-requested",
        "execution-allowed",
        "environment-isolated",
        "audit-evidence-present",
        "security-risk",
        "quality-status",
        "review-notes",
        "workflow-status",
      ];

      for (const field of fields) {
        await expect(page.getByTestId(field)).toBeVisible();
      }

      await expect(
        page.getByTestId("case-selector").locator("option")
      ).toHaveCount(9);

      await expect(page.getByTestId("accept-button")).toBeVisible();
      await expect(page.getByTestId("review-button")).toBeVisible();
      await expect(page.getByTestId("block-button")).toBeVisible();
    });

    test("accepts approved script with verified integrity", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-001");

      await expect(page.getByTestId("script-status")).toHaveText("approved");
      await expect(page.getByTestId("source-allowlisted")).toHaveText("true");
      await expect(page.getByTestId("integrity-status")).toHaveText("verified");
      await expect(page.getByTestId("execution-requested")).toHaveText("true");
      await expect(page.getByTestId("execution-allowed")).toHaveText("true");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");
      await expect(page.getByTestId("valid-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeEnabled();
      await expect(page.getByTestId("review-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeDisabled();

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Governance decision accepted"
      );
    });

    test("blocks a script from an unapproved source", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-002");

      await expect(page.getByTestId("source-allowlisted")).toHaveText("false");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("high");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");
      await expect(page.getByTestId("blocked-banner")).toBeVisible();

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeEnabled();

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Review notes required"
      );

      await page.getByTestId("review-notes").fill(
        "The source is not allowlisted. Execution must remain denied."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script execution blocked"
      );
    });

    test("blocks integrity mismatch even for an approved source", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-003");

      await expect(page.getByTestId("script-status")).toHaveText("approved");
      await expect(page.getByTestId("source-allowlisted")).toHaveText("true");
      await expect(page.getByTestId("integrity-status")).toHaveText("mismatch");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("critical");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");

      await expect(page.getByTestId("accept-button")).toBeDisabled();

      await page.getByTestId("review-notes").fill(
        "Integrity evidence does not match the approved reference."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script execution blocked"
      );
    });

    test("requires review when audit evidence is missing", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-004");

      await expect(page.getByTestId("script-status")).toHaveText("approved");
      await expect(page.getByTestId("audit-evidence-present")).toHaveText("false");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
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
        "Authorisation evidence must be verified before approval."
      );

      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script marked for review"
      );
    });

    test("accepts an intentionally disabled script without execution", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-005");

      await expect(page.getByTestId("script-status")).toHaveText("disabled");
      await expect(page.getByTestId("execution-requested")).toHaveText("false");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");

      await expect(page.getByTestId("accept-button")).toBeEnabled();

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Governance decision accepted"
      );
    });

    test("blocks environment isolation failure", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-006");

      await expect(page.getByTestId("environment")).toHaveText("production");
      await expect(page.getByTestId("environment-isolated")).toHaveText("false");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("critical");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("block-button")).toBeEnabled();

      await page.getByTestId("review-notes").fill(
        "The script configuration violates environment isolation."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script execution blocked"
      );
    });

    test("keeps pending script approval in review state", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-007");

      await expect(page.getByTestId("script-status")).toHaveText(
        "pending_review"
      );
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("quality-status")).toHaveText(
        "requires_review"
      );

      await expect(page.getByTestId("accept-button")).toBeDisabled();
      await expect(page.getByTestId("review-button")).toBeEnabled();

      await page.getByTestId("review-notes").fill(
        "Formal script approval has not been completed."
      );

      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script marked for review"
      );
    });

    test("accepts verified script when execution was not requested", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-008");

      await expect(page.getByTestId("script-status")).toHaveText("approved");
      await expect(page.getByTestId("integrity-status")).toHaveText("verified");
      await expect(page.getByTestId("execution-requested")).toHaveText("false");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("quality-status")).toHaveText("valid");

      await page.getByTestId("accept-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Governance decision accepted"
      );
    });

    test("blocks execution when script integrity is unverified", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-009");

      await expect(page.getByTestId("source-allowlisted")).toHaveText("true");
      await expect(page.getByTestId("integrity-status")).toHaveText(
        "unverified"
      );
      await expect(page.getByTestId("execution-requested")).toHaveText("true");
      await expect(page.getByTestId("execution-allowed")).toHaveText("false");
      await expect(page.getByTestId("security-risk")).toHaveText("high");
      await expect(page.getByTestId("quality-status")).toHaveText("blocked");

      await expect(page.getByTestId("accept-button")).toBeDisabled();

      await page.getByTestId("review-notes").fill(
        "Source approval does not replace independent integrity verification."
      );

      await page.getByTestId("block-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script execution blocked"
      );
    });

    test("resets review notes and workflow actions when scenario changes", async ({ page }) => {
      await page.getByTestId("case-selector").selectOption("TPS-004");

      await page.getByTestId("review-notes").fill(
        "Missing authorisation evidence requires review."
      );

      await page.getByTestId("review-button").click();

      await expect(page.getByTestId("workflow-status")).toHaveText(
        "Script marked for review"
      );

      await page.getByTestId("case-selector").selectOption("TPS-003");

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
