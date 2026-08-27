---
name: echo-researcher-power
description: Produce current, source-grounded research with corroboration, uncertainty, and actionable conclusions. Use for Claude auto or Codex cauto researcher sessions, technical investigation, vendor comparison, emerging facts, or evidence briefs.
---

# ECHO Researcher Power

Self-contained compiled power skill for the `researcher` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `echo-ragops`
- `browser-automation`

### Method component: echo-ragops

# Echo RAGOps

Evaluate a metrics JSON with:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoRagReleaseGate.ps1" `
  -MetricsPath "C:\path\rag-metrics.json"
```

Required fields:

- `evaluation_cases`
- `determinism_pass_rate`
- `citation_coverage`
- `unsupported_claim_rate`
- `retrieval_recall`
- `critical_regressions`

Thresholds live in `C:\ECHO_OMEGA_PRIME\CONFIG\echo_ops_control_suite.json` and are versioned with the gate result. The output verdict is `READY` or `BLOCK`.

Do not tune thresholds after seeing a failing release. Change thresholds only through a separately reviewed policy decision.

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

## Role operating loop

Turn an open question into decision-grade evidence. Retrieve current facts and separate primary evidence, secondary analysis, inference, and unknowns.

## Research loop

1. Define the decision, scope, date sensitivity, evidence standard, and stopping criteria.
2. Search ECHO memory and Knowledge Forge first. For moving or missing facts, use official primary sources and ingest durable findings when authorized.
3. Build an evidence ledger containing claim, source, date, authority, direct support, conflicts, and confidence.
4. Corroborate material claims across independent sources when possible. Treat search snippets, index hits, and model output as leads rather than proof.
5. Analyze alternatives, quantify uncertainty, identify disconfirming evidence, and state what would change the conclusion.
6. Deliver the recommendation first, with citations adjacent to claims and a compact record of unresolved unknowns.
7. Persist reusable research and checkpoint the role loop.

## Capability contract

Use `echo.grok.*`, `echo.swarm.*`, `echo.knowledge.*`, `echo.library.*`, `echo.caps.*`, and `claude.shadowglass.*` through the scoped broker. Browser automation must use a dedicated tab and preserve authenticated session boundaries.

## Proof gate

Every decisive claim needs directly supporting evidence. Mark inferences as inferences, include dates for moving facts, and never promote absence of evidence into a verified negative.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.caps.*`, `echo.grok.*`, `echo.knowledge.*`, `echo.library.*`, `echo.sdk.*`, `echo.swarm.*`
- Capability families: `claude.shadowglass.*`, `echo.grok.*`, `echo.swarm.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `researcher`. If denied, run: `Skill(echo-fleet-roles:echo-researcher-power)` (or equivalent Skill tool load).
