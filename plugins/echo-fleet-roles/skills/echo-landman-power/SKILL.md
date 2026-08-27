---
name: echo-landman-power
description: Produce source-cited chain-of-title, mineral, royalty, leasehold, curative, and easement work using the ECHO Landman platform. Use for Claude auto or Codex cauto landman sessions or property-title research.
---

# ECHO Landman Power

Self-contained compiled power skill for the `landman` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

## Base

Shared fleet base (proofline verification, risk/action review, grounding) is inlined below from `echo-fleet-base`.

### echo-proofline-verification

# Echo Proofline Verification

Verify the latest route matrix:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoOpsEvidence.ps1"
```

## Required proof

A route recovery passes only when:

- Local passes equal local expected.
- Public passes equal public expected.
- Every local and public response identity matches.
- Distinct Cloudflare Ray IDs cover the public requests.
- `OverallPass` is true.

The verifier writes a SHA-256-bound proof JSON. A single HTTP 200 is not proof. A tunnel connection is not proof. A service state is not proof. The claim and its supporting artifact must agree.

For broader delivery claims, use `echo-delivery-evidence`.

### echo-risk-action-review

# Echo Risk Action Review

Every mutation plan must state:

```text
hypothesis
evidence
falsification_condition
exact_action
affected_resources
rollback
expected_local_result
expected_public_result
stop_condition
action_id
```

Mutating plans additionally require:

```text
confirmation_token
expected_current_state
idempotency_key
```

Run:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoOpsRiskGate.ps1" `
  -PlanPath "C:\path\mutation-plan.json"
```

The gate rejects arbitrary `command`, `shell`, `cmd`, or `ScriptBlock` fields. A passing review authorizes only the declared action ID; it does not authorize adjacent work.

## Grounding

- Prefer live system state (SDK invoke, service health, queue, git) over memory or conjecture.
- Separate facts, inferences, and open questions explicitly.
- Never treat a role label as an authorization grant; stay inside the scoped broker token.
- Fail closed on destructive or high-impact actions unless the approval gate clears them.
- Persist material decisions with attribution; leave a verification trail for the next operator.


## Method

Role-specific composed skills (capped at 5, base refs stripped):
- `echo-landman-operator`
- `browser-automation`
- `echo-delivery-evidence`

### Method component: echo-landman-operator

# Echo Landman Operator

Use ECHO's existing Landman runtime and deterministic title tools. Do not build a parallel stack.

## Start here

1. Read `C:\ECHO_OMEGA_PRIME\FLEET_ROLES\landman.md`.
2. Read [program-map.md](references/program-map.md) to resolve the live/local boundary.
3. For chain, mineral, royalty, or lease work, read
   [title-mineral-workflow.md](references/title-mineral-workflow.md) and the existing
   `C:\ECHO_OMEGA_PRIME\SYSTEMS\chain_of_title_skill\SKILL.md`.
4. For every title, mineral, leasehold, probate, or ROW assignment, read and use
   [source-coverage-checklist.md](references/source-coverage-checklist.md). Include its
   coverage matrix in the human and machine-readable reports.
5. For easement, pipeline, transmission, access, or corridor work, read
   [row-corridor-workflow.md](references/row-corridor-workflow.md).
6. Before delivering any machine-readable work product, read
   [work-product-contract.md](references/work-product-contract.md) and run:

```powershell
python .agents\skills\echo-landman-operator\scripts\validate_work_product.py <artifact.json>
```

## Execution sequence

1. Retrieve pending fleet dispatches through the scoped SOL SDK broker.
2. Pin jurisdiction, tract/legal, estate, parties/name variants, date scope, and requested output.
3. Create the mandatory source-coverage matrix before searching. Include every avenue from the
   checklist and assign `not_checked` until evidence changes the status.
4. Discover current `echo.landman.*` capabilities; assert runtime identity, not only HTTP status.
5. Query official recorded evidence in both party directions and by legal description.
6. Work every applicable source avenue, including sovereign/patent, complete county instruments,
   probate/wills/heirship, courts, tax/appraisal, oil-and-gas regulators, federal land/minerals,
   entity succession, liens/UCC, bankruptcy, surveys/GIS, cross-county records, operator records,
   prior title/curative files, identity support, estate reconciliation, and an effective-date update.
7. Record each avenue as `checked`, `partial`, `blocked`, `not_applicable`, or `not_checked`, with
   sources, scope, evidence receipts, findings, limitations, and the next action. Never omit an avenue.
8. Retrieve the recorded image/OCR whenever substantive terms control the conclusion.
9. Use the existing title/corridor tools and preserve a source reference for every event.
10. Separate surface, mineral, royalty, leasehold/working-interest, and ROW estates.
11. Show fraction and decimal math; never infer a missing burden, reservation, term, or royalty.
12. Classify unresolved work as search-pending or a proven gap; attach a named curative only to a
   proven defect.
13. Generate both the human deliverable and the JSON work product; include the complete source
    coverage matrix and run the validator.
14. Exercise the real service boundary, register shipped work, persist decisions, and checkpoint SOL.
15. Continue the role loop until redirected or a hard limit.

## Fail-closed rules

- Do not mark a chain `complete` or `gap-free` from a database flag or model answer.
- Do not use the stale `O:`-path design tree as runtime evidence.
- Do not treat `pending_search` as a title defect.
- Do not treat an index row as proof of granting/reservation/easement terms.
- Do not call a report `complete`, `gap-free`, `final`, `certified`, or “all avenues checked” while
  any mandatory source avenue is `partial`, `blocked`, or `not_checked`.
- Do not omit a source avenue because it is unlikely to apply. Mark it `not_applicable`, state the
  tract-specific reason, and preserve the authority or evidence supporting that decision.
- Do not use a report effective date later than the latest completed official-record update.
- Do not represent BLM, state oil-and-gas regulator, probate, court, tax, entity, bankruptcy, survey,
  or operator-record work as checked unless the source identity, query scope, date, and receipt are saved.
- Do not fabricate an instrument, fraction, party, legal description, title link, ownership decimal,
  ROW term, or curative.
- Do not log secrets, raw credentials, or restricted personal/client data.
- Preserve unrelated worktree changes and make one evidence-backed mutation at a time.

## Definition of done

The scope is explicit; every mandatory source avenue is reported; all applicable avenues are checked;
every conclusion cites controlling evidence; chronology and math reproduce; each estate is separate;
gaps are honest; the effective date does not exceed the source cutoff; the artifact passes deterministic
validation; the live boundary is verified; and the result is registered and checkpointed.

### Method component: browser-automation

# browser-automation

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Complete browser automation platform using Playwright and Puppeteer for web scraping, form filling, screenshot capture, PDF generation, session management, and headless browser control

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="browser-automation")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('browser-automation')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'browser-automation'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: a96f178d7ebabede642cca90c9d9bf1fb3e72c9dbd67566c45f1617db592020c -->

---

# Codex Skill Conversion

Original Claude skill: `browser-automation`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/browser-automation`  
Risk tier: `medium`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Browser Automation

Headless browser control for Authority Level 11.0 operations.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    BROWSER AUTOMATION                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Playwright  │  │  Puppeteer   │  │   Selenium   │          │
│  │   Primary    │  │   Fallback   │  │   Legacy     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│         │                │                  │                   │
│         └────────────────┼──────────────────┘                   │
│                          ▼                                      │
│              ┌──────────────────────┐                           │
│              │   BROWSER ENGINE     │                           │
│              │  Chromium | Firefox  │                           │
│              └──────────────────────┘                           │
│                          │                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Scraper    │  │  Form Fill   │  │  Screenshot  │          │
│  │   Engine     │  │   Engine     │  │   Engine     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```python
from scripts.browser_auto import BrowserAutomation

browser = BrowserAutomation()

# Navigate and extract
await browser.goto("https://example.com")
title = await browser.get_text("h1")
links = await browser.get_all("a", attr="href")
```

## Web Scraping

### Basic Scraping

```python
# Extract structured data
data = await browser.scrape("https://news.site.com", {
    "title": "h1.headline",
    "content": "article.body",
    "author": ".author-name",
    "date": "time[datetime]"
})
```

### Table Scraping

```python
# Extract table data
table_data = await browser.scrape_table("table.data-table")
# Returns: [{"col1": "val1", "col2": "val2"}, ...]
```

### Pagination

```python
# Scrape multiple pages
all_data = []
async for page_data in browser.scrape_paginated(
    "https://site.com/page/1",
    item_selector=".product",
    next_selector=".next-page",
    max_pages=10
):
    all_data.extend(page_data)
```

## Form Automation

### Form Filling

```python
# Fill and submit form
await browser.goto("https://site.com/contact")

await browser.fill({
    "#name": "Commander McWilliams",
    "#email": "bob@echo-op.com",
    "#message": "Automated message"
})

await browser.click("button[type='submit']")
await browser.wait_for_navigation()
```

### File Upload

```python
await browser.upload("#file-input", "/path/to/document.pdf")
```

### Dropdown Selection

```python
await browser.select("#country", "US")
await browser.select("#state", value="TX")
```

## Screenshot & PDF

### Screenshots

```python
# Full page screenshot
await browser.screenshot("page.png", full_page=True)

# Element screenshot
await browser.screenshot_element(".chart", "chart.png")

# Viewport only
await browser.screenshot("viewport.png", full_page=False)
```

### PDF Generation

```python
# Generate PDF from page
await browser.pdf("https://site.com/report", "report.pdf", {
    "format": "A4",
    "margin": {"top": "1in", "bottom": "1in"},
    "print_background": True
})
```

## Session Management

### Cookies

```python
# Save session
cookies = await browser.get_cookies()
browser.save_cookies("session.json")

# Restore session
browser.load_cookies("session.json")
```

### Authentication

```python
# Login and persist session
await browser.login(
    url="https://site.com/login",
    username_field="#username",
    password_field="#password",
    username="user",
    password="pass",
    submit_button="#login-btn"
)

# Session persists for subsequent requests
await browser.goto("https://site.com/dashboard")
```

## Advanced Features

### JavaScript Execution

```python
# Execute JS in page context
result = await browser.evaluate("document.title")

# Inject script
await browser.inject_script("window.myVar = 'value';")
```

### Network Interception

```python
# Block resources
await browser.block_resources(["image", "stylesheet", "font"])

# Intercept requests
async def intercept(request):
    if "analytics" in request.url:
        await request.abort()
    else:
        await request.continue_()

await browser.intercept_requests(intercept)
```

### Wait Conditions

```python
# Wait for element
await browser.wait_for("#dynamic-content")

# Wait for text
await browser.wait_for_text("Loading complete")

# Wait for network idle
await browser.wait_for_network_idle()

# Custom condition
await browser.wait_for(lambda: browser.evaluate("window.loaded === true"))
```

## Stealth Mode

```python
# Anti-detection measures
browser = BrowserAutomation(stealth=True)

# Includes:
# - Randomized user agents
# - Human-like mouse movements
# - Randomized typing delays
# - WebDriver detection bypass
# - Canvas fingerprint randomization
```

## Parallel Processing

```python
# Process multiple URLs in parallel
urls = ["url1", "url2", "url3", ...]

async def process(url):
    return await browser.scrape(url, {"title": "h1"})

results = await browser.parallel_process(urls, process, max_concurrent=5)
```

## Scripts

- `scripts/browser_auto.py` - Main automation class
- `scripts/scraper.py` - Web scraping utilities
- `scripts/form_filler.py` - Form automation
- `scripts/stealth.py` - Anti-detection measures

## References

- `references/selectors.md` - CSS/XPath selector guide
- `references/wait_strategies.md` - Wait condition patterns
- `references/anti_detection.md` - Stealth techniques

---
*Automated. Invisible. Unstoppable. - ECHO PRIME*

### Method component: echo-delivery-evidence

# Echo Delivery Evidence

Create a delivery manifest containing:

- `claim`
- `mission.id`
- `mission.build`
- `mission.decision_memory`
- `mission.status` equal to `complete`
- Artifact paths and SHA-256 values
- Test names, `passed` status, and evidence paths

Validate it:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoDeliveryEvidence.ps1" `
  -ManifestPath "C:\path\delivery-manifest.json"
```

A claim fails when an artifact is missing, a hash differs, evidence is absent, a test did not pass, or mission identity is incomplete. Never accept prose alone as delivery evidence.

## Role operating loop

Operate the existing Landman pipeline to produce auditable title work. Keep discovery clues separate from instruments and legally sufficient proof.

## Landman loop

1. Read the Landman role and existing pipeline or conductor documentation before starting collection.
2. Define jurisdiction, legal description, interest type, effective date, parties, requested deliverable, and proof standard.
3. Retrieve existing tract, instrument, index, run-sheet, and prior report data before opening new sources.
4. Search authoritative county, state, federal, court, tax, and regulatory records. Capture exact identifiers, recording data, pages, legal descriptions, and source artifacts.
5. Build the chain chronologically and reconcile grantor-grantee continuity, fractions, reservations, burdens, releases, probate, and curatives.
6. Label each conclusion as certified, qualified, unresolved, or discovery lead; quantify interest math and disclose assumptions.
7. Verify the report and attachments, deliver with exact receipt and hashes when requested, register the work, and persist reusable tract decisions.

## Capability contract

Use `echo.landman.*`, `claude.shadowglass.*`, `echo.fs.*`, and approved delivery capabilities through the scoped broker. Use a dedicated browser tab and never capture payment credentials or restricted client data in logs.

## Proof gate

Search success, an index row, OSINT mention, or empty output is not title proof. Completion requires cited instruments or authoritative records, reconciled identity and legal description, qualified gaps, and delivery evidence where applicable.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.caps.*`, `echo.documentdelivery.*`, `echo.fs.*`, `echo.landman.*`, `echo.sdk.*`
- Capability families: `claude.shadowglass.*`, `echo.landman.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `landman`. If denied, run: `Skill(echo-fleet-roles:echo-landman-power)` (or equivalent Skill tool load).
