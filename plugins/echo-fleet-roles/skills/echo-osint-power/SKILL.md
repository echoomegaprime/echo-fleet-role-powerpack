---
name: echo-osint-power
description: Collect, corroborate, preserve, and analyze lawful public-source intelligence for ECHO decisions. Use for Claude auto or Codex cauto osint sessions, entity research, web investigations, asset discovery, or evidence mapping.
---

# ECHO Osint Power

Self-contained compiled power skill for the `osint` role. Loading this skill alone delivers the full method (base + role composition). Do not rely on `Load $…` composition.

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
- `browser-automation`
- `ethical-hacking-mastery`
- `echo-frontier-infrastructure`

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

### Method component: ethical-hacking-mastery

# ethical-hacking-mastery

_Auto-mirrored from Grok charter via SYSTEMS/skill_mirror/generate.py._

## When to use

Advanced penetration testing and security assessment expertise

## How it runs

This skill is a **dispatch stub**. Runtime is provided by
`echo-charter-engine.execute(charter_slug="ethical-hacking-mastery")`, which classifies the
described behavior into primitive operations and dispatches through the 8
`echo-*-operator` primitives.

```python
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
engine_path = Path.home() / '.claude' / 'skills' / 'echo-charter-engine' / 'engine.py'
spec = spec_from_file_location('_engine', engine_path)
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.CharterEngine().execute('ethical-hacking-mastery')
```

## Original charter

To change runtime behavior, EITHER add a hand-curated mapping in
`echo-charter-engine/dispatch_map.json` keyed by `'ethical-hacking-mastery'`, OR add new
keyword routes in `echo-charter-engine/engine.py` `_KEYWORD_TO_OP`.

<!-- Generated-from-sha256: 42af94413448ae3374679f1b951e9e3412fd7e9fb33f23b9985c09398ea70abe -->

---

# Codex Skill Conversion

Original Claude skill: `ethical-hacking-mastery`  
Source path inside archive: `skills-plugin/c115c5f8-1a5a-479b-a3d0-211c06017423/ce295037-b5e4-4cc4-a786-879e05eb7799/skills/ethical-hacking-mastery`  
Risk tier: `high`  

## Universal Codex operating rules

- Read this `SKILL.md` before using the skill.
- Use included `scripts/`, `references/`, `templates/`, and `assets/` when present instead of recreating them.
- Do not expose secret values, tokens, credentials, taxpayer data, private keys, or real client records.
- Prefer read-only inspection first. Destructive operations require an explicit user command naming the target.
- For high-risk skills, produce a plan and confirm scope before executing system-changing commands.

---

# Ethical Hacking Mastery Skill

## Overview
This Skill provides comprehensive ethical hacking expertise synthesized from 500+ Tier A/S EKMs in ECHO_PRIME's knowledge base. Covers penetration testing, privilege escalation, OSINT, social engineering, exploitation techniques, and red team operations.

**Use this Skill when:**
- Penetration testing guidance needed
- Exploitation techniques required
- OSINT investigation methods
- Red team operation planning
- Security assessment strategies
- Privilege escalation vectors
- Post-exploitation tactics

## Core Knowledge Domains

### 1. Reconnaissance & OSINT
**Passive Reconnaissance:**
- Google dorking advanced operators
- Shodan/Censys search techniques
- DNS enumeration and subdomain discovery
- WHOIS and registrar intelligence
- Social media intelligence gathering
- Metadata extraction from documents
- Email harvesting and validation
- Public records and data breach searches

**Active Reconnaissance:**
- Port scanning methodologies (nmap, masscan)
- Service enumeration and banner grabbing
- Network topology mapping
- OS fingerprinting techniques
- Application discovery and versioning
- SSL/TLS certificate analysis
- Vulnerability scanning strategies

### 2. Exploitation Techniques
**Common Vulnerabilities:**
- SQL Injection (Union, Boolean, Time-based)
- Cross-Site Scripting (Reflected, Stored, DOM)
- Remote Code Execution vectors
- File upload vulnerabilities
- Directory traversal attacks
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE) injection
- Deserialization exploits

**Exploitation Frameworks:**
- Metasploit module development
- Custom exploit writing
- Payload generation and encoding
- Shellcode development basics
- Return-Oriented Programming (ROP)
- Heap exploitation techniques

### 3. Privilege Escalation
**Linux Privilege Escalation:**
- SUID binary exploitation
- Kernel exploits and versions
- Sudo misconfigurations
- Cron job manipulation
- Path hijacking
- Capabilities abuse
- Docker breakout techniques
- NFS share exploitation

**Windows Privilege Escalation:**
- Token impersonation
- Unquoted service paths
- AlwaysInstallElevated
- Registry autoruns
- DLL hijacking
- Kernel exploits (MS16-032, etc.)
- Potato family exploits
- Group Policy abuse

### 4. Post-Exploitation
**Persistence Mechanisms:**
- Registry autoruns
- Scheduled tasks
- Service creation
- WMI event subscriptions
- SSH key injection
- Web shells deployment
- Backdoor users creation

**Lateral Movement:**
- Pass-the-Hash attacks
- Pass-the-Ticket (Kerberos)
- PSExec and alternatives
- WMI remote execution
- PowerShell remoting
- RDP hijacking
- SMB relay attacks

**Data Exfiltration:**
- DNS tunneling
- ICMP tunneling
- HTTP/HTTPS exfiltration
- Cloud storage abuse
- Steganography techniques
- Encrypted channels

### 5. Social Engineering
**Pretexting Techniques:**
- Authority manipulation
- Urgency creation
- Trust exploitation
- Technical support scams
- Executive impersonation

**Phishing Operations:**
- Spear phishing campaigns
- Credential harvesting pages
- Email spoofing techniques
- Domain typosquatting
- Homograph attacks
- QR code phishing

### 6. Red Team Operations
**Planning & Reconnaissance:**
- Target profiling
- Attack surface mapping
- Kill chain development
- C2 infrastructure setup
- Operational security (OPSEC)

**Execution:**
- Initial access vectors
- Defense evasion techniques
- Anti-forensics methods
- Living off the land (LOLBins)
- Fileless malware concepts

## Key Tools & Frameworks

### Reconnaissance
- **nmap** - Network scanning and enumeration
- **masscan** - High-speed port scanner
- **subfinder** - Subdomain discovery
- **amass** - Attack surface mapping
- **theHarvester** - Email/subdomain gathering
- **recon-ng** - Reconnaissance framework
- **Shodan CLI** - Internet device search

### Exploitation
- **Metasploit** - Exploitation framework
- **sqlmap** - SQL injection automation
- **Burp Suite** - Web application testing
- **BeEF** - Browser exploitation
- **Cobalt Strike** - Red team platform
- **Empire/Starkiller** - Post-exploitation

### Privilege Escalation
- **LinPEAS** - Linux enumeration
- **WinPEAS** - Windows enumeration
- **GTFOBins** - Unix binary exploitation
- **LOLBAS** - Windows binary exploitation
- **PowerUp** - Windows privilege escalation

### Post-Exploitation
- **Mimikatz** - Credential extraction
- **BloodHound** - AD attack path mapping
- **CrackMapExec** - Network lateral movement
- **Impacket** - Network protocol toolkit

## Attack Methodologies

### Web Application Testing
```
1. Information Gathering
   - Identify technologies (Wappalyzer, BuiltWith)
   - Map attack surface (Burp Spider, OWASP ZAP)
   - Analyze source code and comments

2. Authentication Testing
   - Brute force credentials
   - Session management flaws
   - OAuth misconfigurations
   - JWT vulnerabilities

3. Authorization Testing
   - Vertical privilege escalation
   - Horizontal privilege escalation
   - IDOR (Insecure Direct Object Reference)
   - Path traversal

4. Input Validation
   - SQL injection all vectors
   - XSS (reflected, stored, DOM)
   - XXE injection
   - SSTI (Server-Side Template Injection)

5. Business Logic
   - Race conditions
   - Payment bypass
   - Account takeover chains
   - Workflow abuse
```

### Network Penetration Testing
```
1. External Reconnaissance
   - Passive: OSINT, DNS, WHOIS
   - Active: Port scans, service enum

2. External Attack Surface
   - VPN vulnerabilities
   - Exposed services exploitation
   - Web application attacks
   - Email phishing campaigns

3. Internal Network
   - Network segmentation testing
   - Internal reconnaissance
   - Privilege escalation
   - Lateral movement

4. Active Directory
   - Kerberoasting
   - AS-REP roasting
   - DCSync attacks
   - Golden/Silver tickets
```

### Mobile Application Testing
```
1. Static Analysis
   - Decompile APK/IPA
   - Source code review
   - Hardcoded secrets
   - Insecure storage

2. Dynamic Analy

…(truncated for compiled role skill)…


### Method component: echo-frontier-infrastructure

# Echo Frontier Infrastructure

Validate the installed policy:

```powershell
& "C:\ECHO_OMEGA_PRIME\SYSTEMS\echo_ops_control_suite\scripts\Test-EchoInfrastructurePolicy.ps1"
```

## Invariants

- No mutating action is remotely exposed.
- TRIGGERcmd contains read-only action IDs only.
- No public action accepts an arbitrary command or ScriptBlock.
- Every mutation has a confirmation token and audit record.
- Services are explicitly allowlisted.
- Skills and scripts separate judgment from deterministic enforcement.

A policy failure blocks expansion of the control plane. Fix the policy before adding capabilities.

## Role operating loop

Build decision-grade intelligence from public and authorized sources while preserving provenance, scope, and the distinction between leads and proof.

## OSINT loop

1. Define the authorized objective, entities, jurisdictions, time window, identifiers, exclusions, and evidence standard.
2. Search existing ECHO knowledge before collecting. Build an alias and identifier map to prevent entity conflation.
3. Collect from primary public sources first using dedicated browser tabs or passive CRUCIBLE capabilities. Respect access boundaries and rate limits.
4. Preserve URL, timestamp, source authority, query, content hash or capture, and chain of custody for material evidence.
5. Corroborate important claims across independent sources and track contradictions, gaps, and confidence.
6. Separate discovery leads, verified facts, negative results, and inference. Do not treat an index hit or empty result as proof.
7. Deliver the intelligence assessment, evidence matrix, next collection actions, and durable source record.

## Capability contract

Use `claude.shadowglass.*`, passive or authorized `echo.crucible.*`, `echo.fs.*`, and base knowledge capabilities through the scoped broker. Do not expose restricted personal, client, or credential data.

## Proof gate

Every high-impact claim must trace to preserved evidence with date and identity confidence. Negative findings require documented source coverage and remain qualified unless the source is authoritative and complete.

## Capability contract

- Scopes: `claude.shadowglass.*`, `echo.caps.*`, `echo.crucible.*`, `echo.fs.*`, `echo.sdk.*`
- Capability families: `claude.shadowglass.*`, `echo.crucible.*`
- Invoke through `sol_cli.py sdk invoke` with the role-scoped SOL_BROKER_TOKEN; never paste sovereign credentials.

## Adoption gate

Before Edit/Write/Bash/echo.*-invoke, the runtime requires this skill loaded for role `osint`. If denied, run: `Skill(echo-fleet-roles:echo-osint-power)` (or equivalent Skill tool load).
