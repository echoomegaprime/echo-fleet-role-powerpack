import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import path from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const pluginRoot = path.join(root, "plugins", "echo-fleet-roles");
const skillsRoot = path.join(pluginRoot, "skills");
const pinPath = path.join(root, "docs", "SKILL_HASH_PIN.json");
const marketplacePath = path.join(root, ".agents", "plugins", "marketplace.json");

function sha256(file: string): string {
  return createHash("sha256").update(readFileSync(file)).digest("hex");
}

describe("canonical echo-fleet-roles plugin", () => {
  it("marketplace publishes exactly one plugin named echo-fleet-roles", () => {
    const mkt = JSON.parse(readFileSync(marketplacePath, "utf8"));
    assert.equal(mkt.name, "echo-omega-prime-marketplace");
    assert.equal(mkt.plugins.length, 1);
    assert.equal(mkt.plugins[0].name, "echo-fleet-roles");
  });

  it("plugin.json name is echo-fleet-roles (doctrine prefix)", () => {
    const pj = JSON.parse(
      readFileSync(path.join(pluginRoot, ".codex-plugin", "plugin.json"), "utf8"),
    );
    assert.equal(pj.name, "echo-fleet-roles");
    assert.ok(pj.version);
  });

  it("ships echo-role-switching and echo-fleet-base plus role powers", () => {
    const skills = readdirSync(skillsRoot).filter((n) =>
      statSync(path.join(skillsRoot, n)).isDirectory(),
    );
    assert.ok(skills.includes("echo-role-switching"));
    assert.ok(skills.includes("echo-fleet-base"));
    assert.ok(skills.includes("echo-judge-power"));
    assert.ok(skills.includes("echo-commander-power"));
    assert.ok(skills.includes("echo-builder-power"));
    assert.ok(skills.length >= 31);
  });

  it("registry default_plugin points at canonical marketplace plugin", () => {
    const reg = JSON.parse(
      readFileSync(path.join(pluginRoot, "config", "role_power_registry.json"), "utf8"),
    );
    assert.equal(reg.default_plugin, "echo-fleet-roles@echo-omega-prime-marketplace");
    assert.equal(reg.canonical_decision.retired_skills_plugin, "echo-fleet-role-powerpack@echoomegaprime");
  });

  it("SKILL_HASH_PIN matches on-disk SKILL.md files", () => {
    assert.ok(existsSync(pinPath));
    const pin = JSON.parse(readFileSync(pinPath, "utf8"));
    assert.equal(pin.plugin, "echo-fleet-roles@echo-omega-prime-marketplace");
    for (const [name, meta] of Object.entries(pin.skills as Record<string, { sha256: string }>)) {
      const skillMd = path.join(skillsRoot, name, "SKILL.md");
      assert.ok(existsSync(skillMd), `missing ${skillMd}`);
      assert.equal(sha256(skillMd), meta.sha256, `hash drift for ${name}`);
    }
  });

  it("disable justifications doc lists both vercel and figma duplicates", () => {
    const doc = readFileSync(path.join(root, "docs", "PLUGIN_DISABLE_JUSTIFICATIONS.md"), "utf8");
    assert.match(doc, /vercel@openai-curated/);
    assert.match(doc, /vercel@claude-plugins-official/);
    assert.match(doc, /figma@openai-curated/);
    assert.match(doc, /figma@claude-plugins-official/);
    assert.match(doc, /retired-duplicate-role-skills-plugin|Retired \(skills plugin\)/);
  });
});
