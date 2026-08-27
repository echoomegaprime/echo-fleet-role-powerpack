---
name: echo-experience-designer-power
description: Design and validate premium, coherent, responsive, accessible ECHO user journeys and interface systems across normal and failure states. Use for Claude auto or Codex cauto Experience Designer sessions, UX research, information architecture, Figma/prototypes, design systems, accessibility, responsive interaction, visual acceptance, and live UI audits.
---

# ECHO Experience Designer Power

Self-contained compiled power skill for the `experience-designer` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `figma:figma-use`
- `figma:figma-generate-design`
- `browser-automation`
- `brand-guidelines`
- `gui-building-prime`

### Method component: figma:figma-use

# use_figma — Figma Plugin API Skill

Use the `use_figma` tool to execute JavaScript in Figma files via the Plugin API. All detailed reference docs live in `references/`.

**Always include `figma-use` in the comma-separated `skillNames` parameter when calling `use_figma`. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-use`).** This is a logging parameter used to track skill usage — it does not affect execution.

**If Figma MCP tools appear as deferred tools, batch-load all their schemas in a single `ToolSearch` call** using the `select:` syntax — e.g. `ToolSearch query="select:use_figma,get_screenshot,get_metadata,create_new_file"`. One round trip beats six.

**If the task involves building or updating a full page, screen, or multi-section layout in Figma from code**, also load [figma-generate-design](../figma-generate-design/SKILL.md). It provides the workflow for discovering design system components via `search_design_system`, importing them, and assembling screens incrementally. Both skills work together: this one for the API rules, that one for the screen-building workflow.

**If the task involves creating or building a component in Figma** (even a single component), also load [figma-generate-library](../figma-generate-library/SKILL.md). It provides the component creation workflow — variable foundations, variant sets, design token bindings — that `figma-use` alone doesn't cover.

Before anything, load [plugin-api-standalone.index.md](references/plugin-api-standalone.index.md) to understand what is possible. When you are asked to write plugin API code, use this context to grep `references/plugin-api-standalone.d.ts` for relevant types, methods, and properties. This is the definitive source of truth for the API surface. It is a large typings file, so do not load it all at once, grep for relevant sections as needed.

IMPORTANT: Whenever you work with design systems, start with [working-with-design-systems/wwds.md](references/working-with-design-systems/wwds.md) to understand the key concepts, processes, and guidelines for working with design systems in Figma. Then load the more specific references for components, variables, text styles, and effect styles as needed.

## 1. Critical Rules

1.  **Use `return` to send data back.** The return value is JSON-serialized automatically (objects, arrays, strings, numbers). Do NOT call `figma.closePlugin()` or wrap code in an async IIFE — this is handled for you.
2.  **Write plain JavaScript with top-level `await` and `return`.** Code is automatically wrapped in an async context. Do NOT wrap in `(async () => { ... })()`.
3.  `figma.notify()` **throws "not implemented"** — never use it
3a. **Return node IDs and keep workflow state outside the Figma file.** Put human-readable component purpose and usage in the component's `description`.
4.  `console.log()` is NOT returned — use `return` for output
5.  **Work incrementally in small steps.** Break large operations into multiple `use_figma` calls. Validate after each step. This is the single most important practice for avoiding bugs.
6.  Colors are **0–1 range** (not 0–255): `{r: 1, g: 0, b: 0}` = red
7.  Fills/strokes are **read-only arrays** — clone, modify, reassign
8.  **Every text edit follows the canonical recipe: load font → `await` → mutate → return affected node IDs.** Skipping the load throws `Cannot write to node with unloaded font "<family> <style>"`. The rule covers more than `characters` — it applies to any operation on nodes with unloaded fonts (`appendChild`, `insertChild`, `setBoundVariable`, `setExplicitVariableModeForCollection`, `setValueForMode`, `findAll` callbacks touching text). When mutating existing text, load the node's *current* fonts via `getStyledTextSegments(['fontName'])`, not a hardcoded default. Inter is preloaded in most environments so other families surface this bug more often — the recipe is the same for every font. Use `await figma.listAvailableFontsAsync()` first if the style string is unverified. See [Canonical text-edit recipe](references/gotchas.md#canonical-text-edit-recipe-font-load--await--mutate--return-ids).
9.  **Pages load incrementally** — use `await figma.setCurrentPageAsync(page)` to switch pages and load their content. The sync setter `figma.currentPage = page` does **NOT** work and will throw (see Page Rules below)
10. `setBoundVariableForPaint` returns a **NEW** paint — must capture and reassign
11. `createVariable` accepts collection **object or ID string** (object preferred)
12. **`layoutSizingHorizontal/Vertical` is value-restricted by structural context — `FIXED` always works, `HUG` and `FILL` do not.** `'HUG'` is valid only on an auto-layout frame itself OR on a **TEXT** child of one. `'FILL'` is valid only on a child of an auto-layout frame that is also not absolute-positioned, not inside an immutable frame, and not a canvas-grid child. Practical consequence: append to an auto-layout parent FIRST, then set `HUG`/`FILL` — a newly-created or unparented node can't satisfy the rule yet. The property itself exists on every `SceneNode`; the error is value-rejection, not "no such property". See [Gotchas](references/gotchas.md#layoutsizinghorizontallayoutsizingvertical-value-rules-fixed-hug-fill).
12a. **Use auto-layout for containers that hold related children.** When children have a structural relationship — stacked, side-by-side, aligned, gapped, hugged — wrap them in `figma.createAutoLayout()`, not `figma.createFrame()` with absolute `x`/`y`. Absolute coordinates govern where a container sits on the canvas; auto-layout governs how its children relate inside it. Skipping the container leaves no protection against text reflow, content changes, or overlap.
12b. **`layoutSizing*` and `*AxisSizingMode` are different enums — don't cross them.** `layoutSizingHorizontal`/`layoutSizingVertical` (set on a **child**) take `'FIXED'|'HUG'|'FILL'`; `primaryAxisSizingMode`/`counterAxisSizingMode` (set on the **frame** itself) take `'FIXED'|'AUTO'`. So `layoutSizingVertical = 'AUTO'` is invalid (use `'HUG'`), and `counterAxisSizingMode = 'FILL'` throws `Expected 'FIXED' | 'AUTO', received 'FILL'` (use `'FIXED'`/`'AUTO'`). Two more errors from the same setter — `Error: in set_layoutSizingHorizontal: node must be an auto-layout frame or a child of an auto-layout frame` and `Error: in set_layoutSizingHorizontal: FILL can only be set on children of auto-layout frames` — mean the node isn't in an auto-layout context yet; **recommendation: make the parent auto-layout (`figma.createAutoLayout()`) and `appendChild` the node before setting** (see Rule 12). See [Gotchas](references/gotchas.md#layoutsizing-vs-axissizingmode-two-different-sizing-enums).
13. **Position new top-level nodes away from (0,0).** Nodes appended directly to the page default to (0,0). Scan `figma.currentPage.children` to find a clear position (e.g., to the right of the rightmost node). This only applies to page-level nodes — nodes nested inside other frames or auto-layout containers are positioned by their parent. See [Gotchas](references/gotchas.md).
14. **On `use_figma` error, STOP. Do NOT immediately retry.** Failed scripts are **atomic** — if a script errors, it is not executed at all and no changes are made to the file. Read the error message carefully, fix the script, then retry. See [Error Recovery](#6-error-recovery--self-correction).
15. **MUST `return` ALL created/mutated node IDs.** Whenever a script creates new nodes or mutates existing ones on the canvas, collect every affected node ID and return them in a structured object (e.g. `return { createdNodeIds: [...], mutatedNodeIds: [...] }`). This is essential for subsequent calls to reference, validate, or clean up those nodes.
16. **Always set `variable.scopes` explicitly when creating variables.** The default `ALL_SCOPES` pollutes every property picker — alm

…(truncated for compiled role skill)…


### Method component: figma:figma-generate-design

# Build / Update Screens and Views from Design System

Use this skill to create or update **screens, views, and multi-section UI containers** in Figma by **reusing the published design system** — components, variables, and styles — rather than drawing primitives with hardcoded values. This includes full pages, modals, dialogs, drawers, sidebars, panels, and any composed view with multiple sections. The key insight: the Figma file likely has a published design system with components, color/spacing variables, and text/effect styles that correspond to the codebase's UI components and tokens. Find and use those instead of drawing boxes with hex colors.

**MANDATORY**: You MUST also load [figma-use](../figma-use/SKILL.md) before any `use_figma` call. That skill contains critical rules (color ranges, font loading, etc.) that apply to every script you write.

**Always include `figma-generate-design` in the comma-separated `skillNames` parameter when calling `use_figma` as part of this skill. If this skill was loaded via an MCP resource, you MUST prefix the name with `resource:` (e.g. `resource:figma-generate-design`).** This is a logging parameter — it does not affect execution.

## Skill Boundaries

- Use this skill when the deliverable is a **composed Figma view** (new or updated) — full-page screens, modals, dialogs, drawers, sidebars, panels, or any multi-section container — built from design system component instances.
- If the user wants to create **new reusable components or variants**, use [figma-use](../figma-use/SKILL.md) directly.
- If the user wants to write **Code Connect mappings**, switch to [figma-code-connect](../figma-code-connect/SKILL.md).

## Prerequisites

- Figma MCP server must be connected
- The target Figma file must have a published design system with components (or access to a team library)
- User must provide a target Figma file (URL or `fileKey`). If they don't have one yet, invoke `/figma-create-new-file` (or call `create_new_file`) first and reuse the returned file_key. Both `use_figma` and `generate_figma_design` require an existing `fileKey`.
- Source code or description of the screen/view to build/update

## Parallel Workflow with generate_figma_design (Web Apps Only)

When building a screen from a **web app** that can be rendered in a browser, the best results come from running both approaches in parallel:

1. **In parallel:**
   - Start building the screen using this skill's workflow (use_figma + design system components) against the target Figma file (`fileKey`).
   - Run `generate_figma_design` against the **same `fileKey`** to capture a pixel-perfect screenshot of the running web app into that file. `generate_figma_design` always requires `fileKey` — if the user does not yet have a Figma file, first invoke `/figma-create-new-file` (or call the `create_new_file` MCP tool) to get one, and reuse that file_key for both this skill and the capture.
2. **Once both complete:** Update the use_figma output to match the pixel-perfect layout from the `generate_figma_design` capture. The capture provides the exact spacing, sizing, and visual treatment to aim for, while your use_figma output has proper component instances linked to the design system. If the capture contains images, transfer them to your use_figma output by copying `imageHash` values from the capture's image fills (see Step 5 for details).
3. **Once confirmed looking good:** Delete the `generate_figma_design` output — it was only used as a visual reference.

This combines the best of both: `generate_figma_design` gives pixel-perfect layout accuracy, while use_figma gives proper design system component instances that stay linked and updatable.

**This parallel workflow is MANDATORY when the source contains images.** The `use_figma` Plugin API cannot fetch external image URLs — it can only set image fills by copying `imageHash` values from nodes already in the file. `generate_figma_design` rasterizes all visible images into Figma, providing the hashes you need. If you skip the capture when images are present, image frames will be left blank.

For non-web apps (iOS, Android, etc.) or when updating existing screens, use the standard workflow below.

## Required Workflow

**Follow these steps in order. Do not skip steps.**

> **Hard gates — forbidden shortcuts:**
>
> - **Forbidden:** `search_design_system` for component keys until 2a-i is complete and 2a-ii is attempted or logged N/A (e.g. "empty file, no existing screens").
> - **Forbidden:** Any `use_figma` call that mutates the canvas (Step 3+) until all Step 2 rows in the checklist below are filled in.

### Step 1: Understand the Deliverable

Before touching Figma, understand what you're building:

1. If building from code, read the relevant source files to understand the structure, sections, and which components are used.
2. Identify the major sections of the view (e.g., for a page: Header, Hero, Content Panels, Footer; for a modal: Title Bar, Form Sections, Action Bar; for a sidebar: Navigation, Content Area, Footer Actions).
3. For each section, list the UI components involved (buttons, inputs, cards, navigation pills, accordions, etc.).
4. **Identify the product's font family from the source. Do not default to Inter.** Find *which* typeface the product uses before writing any script. See [references/discover-product-font.md](references/discover-product-font.md) for where to look (CSS variables, component files) and how to resolve messy Figma font names.
5. **Check whether the view contains any images** (e.g., `<img>`, `<Image>`, background images, product photos, avatars, icons loaded from URLs). If it does and this is a web app, you **must** run the parallel `generate_figma_design` capture workflow — start it immediately alongside Step 2 so the capture runs while you discover components. See "Parallel Workflow with generate_figma_design" above.

### Step 2: Collect Component Keys, Variables, and Styles

You need three things from the design system: **components** (buttons, cards, etc.), **variables** (colors, spacing, radii), and **styles** (text styles, effect styles like shadows). Don't hardcode hex colors or pixel values when design system tokens exist.

#### 2a: Discover components


**2a-i — REQUIRED: Check Code Connect for needed components.** Starting from the component list you built in Step 1, check whether each component has a Code Connect file in the codebase. Code Connect files live next to the component source and are named by platform:

- **TypeScript/JS**: `*.figma.ts`, `*.figma.js`
- **React (parser-based)**: `*.figma.tsx`
- **Kotlin/Compose**: `.kt` files containing `@FigmaConnect`
- **Swift**: `.swift` files containing `FigmaConnect`

For each component you need (e.g., Button, Card, Input), search for its Code Connect file — glob or grep by component name (e.g., `**/Button.figma.tsx`, `**/Card.figma.ts`). Only read files that match components you actually need.

From each matching Code Connect file, extract the Figma component URL. Parse `fileKey` and `nodeId` from the URL (convert hyphens to colons: `123-456` → `123:456`). Then resolve component keys via `use_figma`:

**Example:** Code Connect file contains `// url=https://figma.com/design/ABC123/File?node-id=609-35535`. Parse `fileKey` = `ABC123`, `nodeId` = `609:35535`. Run `use_figma` against the **library file** (fileKey `ABC123`, not the target file) to resolve the key:

```js
const node = await figma.getNodeByIdAsync("609:35535");
const set = node?.parent?.type === "COMPONENT_SET" ? node.parent : node;
return { componentKey: set.key };
```

Batch multiple lookups in a single call. Use the returned keys with `importComponentSetByKeyAsync()` in Step 4.

Mark resolved components. If all components are resolved, skip 2a-ii and 2a-iii. If none of the needed components have Code Connect files, proceed to 2a-ii.

**2a-ii — REQUIRED if unresolved components remain:

…(truncated for compiled role skill)…


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

### Method component: gui-building-prime

# gui-building-prime

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Electron GUI creation with real-time dashboards and MCP integration

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="gui-building-prime")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('gui-building-prime')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'gui-building-prime'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 21405d5922220565e55e3e8607bbacb126102665054ac9b23e9a4d9e0ce9e405 -->

---

# Codex Skill Conversion

Original Claude skill: `gui-building-prime`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/gui-building-prime`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# GUI Building Prime Directive

## Overview
Authority Level 11.0 GUI creation expertise for ECHO PRIME's multi-tab Electron interface, real-time monitoring dashboards, MCP server visualization, and autonomous GUI generation. Synthesized from production GUI patterns, reactive frameworks, and human-computer interaction principles.

**Use this Skill when:**
- Building ECHO PRIME's main Electron GUI
- Creating tabbed interfaces for MCP servers
- Implementing real-time monitoring dashboards
- Auto-generating interfaces from specifications
- Building voice-enabled interactive GUIs
- Creating holographic-style visualizations
- Implementing Authority Level 11.0 controls
- Building self-healing GUI components

## Core Knowledge Domains

### 1. ECHO PRIME Electron Architecture
**Main GUI Structure:**
```javascript
// P:\ECHO_PRIME\ECHO PRIMEGUI\electron-app\Master Gui\index.html
const { app, BrowserWindow, ipcMain, Menu } = require('electron');
const path = require('path');

class EchoPrimeGUI {
    constructor() {
        this.mainWindow = null;
        this.serverWindows = new Map();
        this.authorityLevel = 11.0;
        
        // Phoenix healing integration
        this.phoenixMonitor = new PhoenixGUIMonitor();
        
        // MCP constellation tracking
        this.mcpServers = new Map([
            ['HARVESTERS', { port: 11001, status: 'active' }],
            ['TRAINERS', { port: 11002, status: 'active' }],
            ['MEMORY_ORCHESTRATION', { port: 11003, status: 'active' }],
            ['EPCP3O', { port: 11004, status: 'active' }]
        ]);
    }
    
    createMainWindow() {
        this.mainWindow = new BrowserWindow({
            width: 1920,
            height: 1080,
            frame: false,  // Frameless for custom titlebar
            transparent: true,
            backgroundColor: '#00000000',
            webPreferences: {
                nodeIntegration: true,
                contextIsolation: false,
                webviewTag: true
            }
        });
        
        // Load main interface
        this.mainWindow.loadFile('index.html');
        
        // Authority Level 11.0 menu
        this.createAuthorityMenu();
        
        // Auto-healing on crash
        this.mainWindow.webContents.on('crashed', () => {
            this.phoenixMonitor.resurrect(this.mainWindow);
        });
    }
    
    createAuthorityMenu() {
        const template = [
            {
                label: 'Authority 11.0',
                submenu: [
                    { label: 'Commander Mode', accelerator: 'Ctrl+Shift+C' },
                    { label: 'Phoenix Healing', accelerator: 'Ctrl+Shift+P' },
                    { label: 'Memory Crystals', accelerator: 'Ctrl+Shift+M' },
                    { type: 'separator' },
                    { label: 'Emergency Override', role: 'forceReload' }
                ]
            }
        ];
        
        Menu.setApplicationMenu(Menu.buildFromTemplate(template));
    }
}
```

### 2. Tabbed MCP Server Interfaces
**Dynamic Tab Generation:**
```html
<!-- P:\ECHO_PRIME\ECHO PRIMEGUI\electron-app\TABS\template.html -->
<!DOCTYPE html>
<html>
<head>
    <style>
        :root {
            --echo-primary: #00ffff;
            --echo-secondary: #ff00ff;
            --echo-dark: #0a0a0f;
            --authority-gold: #ffd700;
        }
        
        body {
            background: linear-gradient(135deg, var(--echo-dark) 0%, #1a1a2e 100%);
            color: var(--echo-primary);
            font-family: 'Consolas', 'Courier New', monospace;
            margin: 0;
            overflow: hidden;
        }
        
        .tab-container {
            display: grid;
            grid-template-columns: 250px 1fr;
            height: 100vh;
        }
        
        .sidebar {
            background: rgba(0, 0, 0, 0.8);
            border-right: 2px solid var(--echo-primary);
            padding: 20px;
        }
        
        .server-status {
            display: flex;
            align-items: center;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid transparent;
            transition: all 0.3s;
        }
        
        .server-status:hover {
            border-color: var(--echo-primary);
            box-shadow: 0 0 10px var(--echo-primary);
        }
        
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 10px;
            animation: pulse 2s infinite;
        }
        
        .status-active { background: #00ff00; }
        .status-warning { background: #ffff00; }
        .status-error { background: #ff0000; }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .main-panel {
            padding: 20px;
            position: relative;
        }
        
        .holographic-display {
            background: 
                repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 2px,
                    rgba(0, 255, 255, 0.03) 2px,
                    rgba(0, 255, 255, 0.03) 4px
                );
            border: 2px solid var(--echo-primary);
            border-radius: 10px;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        .holographic-display::before {
            content: '';
            position: absolute;
            top: -100%;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                180deg,
                transparent 0%,
                rgba(0, 255, 255, 0.1) 50%,
                transparent 100%
            );
            animation: scan 3s linear infinite;
        }
        
        @keyframes scan {
            to { transform: translateY(200%); }
        }
    </style>
</head>
<body>
    <div class=

…(truncated for compiled role skill)…


## Role operating loop

Own the complete experience from entry and comprehension through success, failure, recovery, and return use.

## Workflow

1. Inspect the live product, product contract, users, analytics, feedback, incidents, brand assets, content, and design system.
2. Map first-time and expert journeys including entry, decisions, permissions, loading, empty, error, offline, destructive confirmation, recovery, completion, and return.
3. Define information architecture, terminology, hierarchy, navigation, search/discovery, and cross-device behavior.
4. Test low-fidelity flow structure, then create responsive high-fidelity prototypes for interaction, content, motion, and trust moments.
5. Specify tokens, typography, spacing, grids, color roles, icons, components, states, focus, motion, data visualization, and content voice.
6. Validate WCAG 2.2 AA semantics, keyboard/focus, contrast, zoom/reflow, reduced motion, labels/errors/live regions, captions, and touch targets.
7. Run realistic task tests and measure success, time, error, comprehension, confidence, and accessibility across viewports and degraded states.
8. Hand off annotated flows, component/state contracts, assets, responsive rules, event instrumentation, accessibility assertions, and visual baselines.
9. Inspect the live implementation interactively; file reproducible discrepancies and re-test fixes.
10. Compare post-release journey metrics with baseline and register reusable patterns.

## Capability contract

Use claude.shadowglass.*, echo.website.*, echo.beta.*, echo.betaportal.*, echo.sentinel.*, echo.grok.*, echo.image.*, echo.caps.*, and echo.sdk.* through the scoped broker. Reserve dedicated browser tabs and never expose protected fields.

## Visual floor

No emoji UI, placeholder glyph brands, generic template styling, happy-path-only states, inaccessible custom controls, deceptive copy, or desktop-only layouts. Use crafted icons or purposeful art, real typography hierarchy, intentional tokens, complete states, and measurable performance/accessibility.

## Deep reference

Read [the experience operating contract](references/operating-contract.md) for journey/state matrices, design-system deliverables, accessibility gates, usability measures, and implementation acceptance.

## Done gate

Representative users can complete critical journeys across devices and failure states, accessibility gates pass, and the live implementation matches the documented system and metrics.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.beta.*`, `echo.betaportal.*`, `echo.caps.*`, `echo.grok.*`, `echo.image.*`, `echo.sdk.*`, `echo.sentinel.*`, `echo.website.*`
- Capability families: `claude.shadowglass.*`, `echo.beta.*`, `echo.betaportal.*`, `echo.website.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `experience-designer`. If denied, run: `Skill(echo-fleet-roles:echo-experience-designer-power)` (or equivalent Skill tool load).
