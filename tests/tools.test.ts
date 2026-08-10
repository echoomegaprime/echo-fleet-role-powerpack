import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { powerpackActivate, powerpackRoles, powerpackStatus } from "../src/tools.ts";

describe("echo-fleet-role-powerpack", () => {
  it("lists roles", () => {
    assert.ok(powerpackRoles().count >= 6);
  });
  it("status live", () => {
    assert.equal(powerpackStatus().status, "live");
  });
  it("high risk requires EXECUTE", () => {
    const r = powerpackActivate("sovereign");
    assert.equal(r.ok, false);
  });
  it("activates with EXECUTE", () => {
    const r = powerpackActivate("sovereign", "EXECUTE", "test");
    assert.equal(r.ok, true);
    assert.equal(powerpackStatus().active_role, "sovereign");
  });
  it("observer without confirm", () => {
    const r = powerpackActivate("observer");
    assert.equal(r.ok, true);
  });
});
