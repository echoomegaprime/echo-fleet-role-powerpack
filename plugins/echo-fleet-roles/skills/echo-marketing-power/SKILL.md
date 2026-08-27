---
name: echo-marketing-power
description: Build premium, measurable ECHO positioning, content, campaigns, and conversion systems. Use for Claude auto or Codex cauto marketing sessions, launches, growth experiments, brand messaging, or campaign analysis.
---

# ECHO Marketing Power

Self-contained compiled power skill for the `marketing` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `brand-guidelines`
- `internal-comms`
- `browser-automation`
- `echo-delivery-evidence`

### Method component: brand-guidelines

# brand-guidelines

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="brand-guidelines")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('brand-guidelines')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'brand-guidelines'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 439827531e32340bedcc6dff6ed41ea71a9722bfdf227cae7552871d55663a4f -->

---

# Codex Skill Conversion

Original Claude skill: `brand-guidelines`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/brand-guidelines`  
Risk tier: `low`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems

### Method component: internal-comms

# internal-comms

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="internal-comms")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('internal-comms')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'internal-comms'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 42e684265ade5b92a01829dc0cb8a218eb945ec2f4bdae161c10e7c3cb7c14e4 -->

---

# Codex Skill Conversion

Original Claude skill: `internal-comms`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/internal-comms`  
Risk tier: `low`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

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

Convert verified product value into distinctive, truthful, measurable demand. Protect brand quality and user trust across every channel.

## Growth loop

1. Retrieve the real product, audience, offer, proof, pricing, funnel, brand system, prior campaigns, and current analytics.
2. Define one audience, one problem, one promise, one proof mechanism, one action, and one measurable conversion event.
3. Research current channel rules and competitor positioning from primary sources. Separate evidence from creative hypothesis.
4. Create a cohesive campaign with premium visual direction, accessible copy, accurate claims, tracking, consent, and channel-specific variants.
5. Test links, attribution, responsive rendering, forms, analytics events, opt-out behavior, and destination readiness before launch.
6. Launch only within authorized reach. Mass outbound, public controversy attribution, or spend beyond hard limits requires the applicable approval.
7. Measure conversion and quality, retain winning evidence, retire weak variants, register the campaign, and persist reusable insight.

## Capability contract

Use `echo.website.*`, `echo.vercel.*`, `echo.image.*`, `echo.grok.*`, `echo.social.*`, and `claude.shadowglass.*` through the scoped broker. Probe current provider and platform contracts before publishing.

## Proof gate

Published content is not a successful campaign. Require live destination checks, tracking evidence, claim substantiation, consent controls, and measured outcome against the declared baseline.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.caps.*`, `echo.grok.*`, `echo.image.*`, `echo.sdk.*`, `echo.social.*`, `echo.vercel.*`, `echo.website.*`
- Capability families: `claude.shadowglass.*`, `echo.grok.*`, `echo.website.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `marketing`. If denied, run: `Skill(echo-fleet-roles:echo-marketing-power)` (or equivalent Skill tool load).
