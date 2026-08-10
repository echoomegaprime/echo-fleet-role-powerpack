import { loadJson, saveJson, audit, createJob, completeJob } from "./lib/store.js";
import type { ToolDef } from "./lib/mcp-http.js";

export const FLEET_ROLES = [
  { id: "observer", power: ["read"], risk: "info" },
  { id: "operator", power: ["read", "service_control"], risk: "medium" },
  { id: "builder", power: ["read", "sdk_invoke", "qcoder"], risk: "medium" },
  { id: "security", power: ["read", "re_suite", "audit"], risk: "high" },
  { id: "sovereign", power: ["read", "write", "fleet_control", "canary"], risk: "high" },
  { id: "canary", power: ["canary_preview"], risk: "high" },
  { id: "innovator", power: ["propose", "apply_gated"], risk: "medium" },
  { id: "ops", power: ["prime_ops", "desktop"], risk: "high" },
] as const;

export type ActiveRole = {
  role_id: string;
  risk: string;
  activatedAt: string;
  activatedBy?: string;
};

export function powerpackRoles() {
  return {
    status: "live",
    roles: FLEET_ROLES.map((r) => ({
      id: r.id,
      power: r.power,
      risk: r.risk,
      contract: `powerpack.${r.id}.v1`,
    })),
    count: FLEET_ROLES.length,
  };
}

export function rolesActive(): ActiveRole | null {
  return loadJson<ActiveRole | null>("active-role.json", null);
}

export function powerpackStatus() {
  const active = rolesActive();
  return {
    status: "live",
    bundle: "echo-fleet-role-powerpack",
    version: "1.0.0",
    roles: FLEET_ROLES.length,
    active_role: active?.role_id ?? null,
    active,
    policy: { high_risk_requires_EXECUTE: true, no_raw_shell: true },
  };
}

export function powerpackActivate(roleId: string, confirm?: string, activatedBy?: string) {
  const role = FLEET_ROLES.find((r) => r.id === roleId);
  if (!role) {
    return {
      ok: false as const,
      error: "unknown_role",
      allowed: FLEET_ROLES.map((r) => r.id),
    };
  }
  const needsConfirm = role.risk === "high";
  if (needsConfirm && confirm !== "EXECUTE") {
    return {
      ok: false as const,
      error: "confirm_required",
      confirm_word: "EXECUTE",
      role: role.id,
      risk: role.risk,
    };
  }
  const job = createJob("roles_switch", "powerpack_activate", { roleId });
  const rec: ActiveRole = {
    role_id: role.id,
    risk: role.risk,
    activatedAt: new Date().toISOString(),
    activatedBy: activatedBy || "mcp",
  };
  const hist = loadJson<ActiveRole[]>("role-history.json", []);
  hist.unshift(rec);
  saveJson("role-history.json", hist.slice(0, 100));
  saveJson("active-role.json", rec);
  completeJob(job.id, rec);
  audit("powerpack.activate", { roleId: role.id, risk: role.risk, jobId: job.id });
  return {
    ok: true as const,
    active: rec,
    power: [...role.power],
    job_id: job.id,
    rollback: { action: "activate_observer", note: "Switch back to observer" },
  };
}

export const tools: ToolDef[] = [
  {
    name: "powerpack_roles",
    description: "List fleet roles and power contracts",
    inputSchema: { type: "object", properties: {} },
    handler: () => powerpackRoles(),
  },
  {
    name: "powerpack_status",
    description: "Active role and policy",
    inputSchema: { type: "object", properties: {} },
    handler: () => powerpackStatus(),
  },
  {
    name: "powerpack_activate",
    description: "Activate a fleet role (high risk requires confirm=EXECUTE)",
    inputSchema: {
      type: "object",
      properties: {
        role_id: { type: "string" },
        confirm: { type: "string" },
        activated_by: { type: "string" },
      },
      required: ["role_id"],
    },
    handler: (a) =>
      powerpackActivate(
        String(a.role_id ?? ""),
        a.confirm != null ? String(a.confirm) : undefined,
        a.activated_by != null ? String(a.activated_by) : undefined,
      ),
  },
];
