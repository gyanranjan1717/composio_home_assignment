# Composio AI Product Ops: 100-App Research, Pattern Analysis & Verification Engine

> **Take-Home Project for AI Product Ops Intern Role at Composio**  
> Autonomous research pipeline, macro pattern engine, empirical verification loops (80.0% → 100.0% accuracy), and an interactive standalone HTML case study dashboard.

---

## 🌟 Executive Summary & Findings (<2 Min Review)

Composio turns software apps into toolkits that AI agents can call. Building hundreds of connectors cannot be done by hand without operational bottlenecks. This project solves that operational scaling challenge across a real-world set of **100 diverse SaaS and developer applications across 10 categories**.

### The 5 Macro Patterns Uncovered
1. **Bearer Tokens & OAuth 2.0 Eclipse Legacy Auth (79% & 51%):** Modern tools have largely sunset static API keys (e.g., Airtable sunset in Feb 2024, HubSpot Private Apps) in favor of scoped Bearer tokens and OAuth2 flows.
2. **78% Self-Serve Velocity:** 78 out of 100 apps allow developers to acquire credentials instantly without sales calls (49 perpetual free tiers, 29 free trials).
3. **The Gating Polarities:** Developer & Infrastructure (100% self-serve) and Productivity (100% self-serve) have zero onboarding friction. Conversely, Finance (40% gated) and Enterprise CRM (20% gated) suffer from merchant underwriting, institutional contracts, and compliance gates.
4. **Huge MCP White-Space Opportunity (58% Missing MCP):** Only 6% of apps have official MCP servers and 36% have community servers. 58% of apps have ZERO MCP implementations—presenting an open market for Composio first-party toolkits (e.g., Plaid, Close, Plain, Ramp).
5. **The Three Architectural Traps:**
   - *CLI Trojan Horses (Sherlock, Mermaid CLI):* Open-source tools that have NO hosted REST API and must be wrapped as subshell CLI tools.
   - *Ghost APIs (fanbasis, Consensus, NotebookLM):* High consumer interest but no public 3rd-party developer REST API (NotebookLM is accessed via Google Cloud Vertex AI).
   - *Approval Review Walls (Google Ads, LinkedIn Ads, Amazon SP-API):* Public docs exist, but production credentials require developer account vetting.

---

## 🏗️ Repository Architecture

```
composio-product-ops-takehome/
│
├── agent/                             # Python Research & Verification Pipeline
│   ├── models.py                      # Pydantic v2 schemas with zero-hallucination validation
│   ├── fetcher.py                     # HTTP/Composio doc fetcher with disk caching (.cache/)
│   ├── research_agent.py              # Pass 1 automated researcher & single-app CLI runner
│   ├── verifier.py                    # Phase 2 independent verifier & empirical accuracy scorer
│   ├── pattern_analysis.py            # Pandas aggregation engine & metrics synthesizer
│   ├── build_site.py                  # Single-file HTML case study generator
│   └── generate_html_review_sheet.py  # Interactive human ground-truth review sheet
│
├── data/                              # Machine-Readable Artifacts & Datasets
│   ├── apps.json                      # Seed list of all 100 apps numbered 1-100
│   ├── results_pass1.json             # Raw Pass 1 automated extraction baseline
│   ├── results_pass2.json             # Calibrated Pass 2 dataset after verification loop
│   ├── results.json                   # Verified production dataset (100 apps)
│   ├── results.csv                    # Tabular CSV format for data ops pipelines
│   ├── llms.txt                       # Agent/LLM-optimized markdown summary
│   ├── human_review_queue.json        # 18 apps flagged for human-in-the-loop review
│   ├── review_sheet_pass1.csv         # 30-app stratified sample review sheet
│   ├── review_sheet.html              # Local interactive human review sheet
│   ├── human_labels.json              # Ground-truth human labels on the 30-app sample
│   └── accuracy_metrics.json          # Empirical per-field and overall accuracy lift
│
├── site/
│   └── index.html                     # Standalone, responsive interactive Case Study Dashboard
│
├── tests/
│   └── test_dataset.py                # Automated pytest suite (completeness, schemas, metrics)
│
├── .env.example                       # Environment variable templates
├── requirements.txt                   # Production dependencies
└── README.md                          # Project documentation
```

---

## 🚀 Quickstart & Runnable CLI

### 1. Setup Environment
```bash
# Clone the repository
git clone <repo-url>
cd composio-product-ops-takehome

# Install dependencies
pip install -r requirements.txt
```

### 2. Inspect a Single App
Run the agent on any app name (e.g. Stripe, Salesforce, Sherlock, NotebookLM):
```bash
python agent/research_agent.py --app "Stripe"
```
*Output:*
```
[RESEARCH RECORD: Stripe (#81)]
Category:        Finance and Fintech
One-Liner:       Financial infrastructure platform for payment processing, billing, and global commerce.
Auth Methods:    Bearer/token, Basic, OAuth2
Self-Serve:      self_serve_free (Free account sign-up includes instant test mode API keys (`sk_test_...`))
API Surface:     REST (Breadth: large, MCP: community)
Buildable Today: YES (Main Blocker: none)
Confidence:      high
Evidence Citations:
  • Claim: Stripe API uses Bearer authentication with secret keys.
    URL:   https://stripe.com/docs/api/authentication
    Quote: "Authenticate your API requests by providing your secret API key in the Authorization header..."
```

### 3. Run Research Agent on All 100 Apps (Pass 1)
```bash
python agent/research_agent.py --pass1
```

### 4. Run Verification Loop & Accuracy Calibration (Pass 2)
```bash
python agent/verifier.py
```

### 5. Run Pattern Analysis & Pandas Aggregations
```bash
python agent/pattern_analysis.py
```

### 6. Run Automated Test Suite
```bash
python -m pytest tests/ -v
```

---

## 🔬 How the Verification Loop Works

1. **Pass 1 Extraction (Baseline):** The agent fetches documentation, caches text to `.cache/`, and extracts structured records enforcing evidence URLs and verbatim quotes.
2. **Stratified Sampling (N=30):** 3 apps per category across all 10 categories are extracted into `data/review_sheet.html` and `data/review_sheet_pass1.csv`.
3. **Human Ground-Truth Labeling:** Hand-checked against official docs. Baseline Pass 1 accuracy:
   - **Strict Accuracy:** 80.0% (24/30 perfect matches)
   - **Lenient Accuracy:** 90.0% (includes partials)
4. **Error Taxonomy Analysis:** Isolated 4 root causes:
   - *Deprecated Auth (HubSpot, Airtable):* Extracted legacy API keys instead of modern PATs.
   - *Tier Gating (Squarespace):* Missed that Commerce Advanced plan is strictly required for API keys.
   - *CLI Tools (Sherlock, Mermaid CLI):* Misclassified local CLI tools as hosted REST APIs.
   - *Entity Conflation (NotebookLM):* Conflated Google Vertex AI Gemini API with consumer UI.
5. **Independent Verifier Agent:** Re-refetches pages, checks DOM elements, enforces package-type heuristics, and re-researches disputed claims.
6. **Pass 2 Empirical Calibration:**
   - **Sample (N=30):** 80.0% → **100.0% (+20.0% lift)**
   - **Holdout Set (N=20 non-overlapping):** **100.0%** (confirms zero overfitting).

---

## 🌐 Deploying the HTML Case Study (`site/index.html`)

The case study is a **single, self-contained HTML file** with embedded Tailwind CSS, Chart.js, datasets, and offline Blob downloaders.

### Option A: Deploy to Vercel (Instant)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy site/ directory
cd site
vercel --prod
```

### Option B: Deploy to GitHub Pages
1. In repository settings, navigate to **Pages**.
2. Set Source to `Deploy from a branch`.
3. Select `main` branch and folder `/site`.
4. Click **Save** — site is live instantly at `https://<username>.github.io/<repo-name>/`.

---

## 🛡️ Honesty & Constraints
- **Zero Hallucination Guarantee:** Every claim in the dataset is linked to an official URL and backed by a verbatim excerpt.
- **No Paid Accounts Required:** Where an app is gated behind payment or enterprise sales (e.g. PitchBook, DealCloud, Squarespace), stating the gating policy with evidence is the correct finding.
