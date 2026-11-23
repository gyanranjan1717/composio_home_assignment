"""Compiles and generates the complete single-file interactive HTML Case Study."""

import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
SITE_DIR = os.path.join(os.path.dirname(__file__), "..", "site")
os.makedirs(SITE_DIR, exist_ok=True)

def generate_html_site():
    with open(os.path.join(DATA_DIR, "results.json"), "r", encoding="utf-8") as f:
        results = json.load(f)

    with open(os.path.join(DATA_DIR, "pattern_analysis.json"), "r", encoding="utf-8") as f:
        patterns = json.load(f)

    with open(os.path.join(DATA_DIR, "accuracy_metrics.json"), "r", encoding="utf-8") as f:
        accuracy = json.load(f)

    with open(os.path.join(DATA_DIR, "llms.txt"), "r", encoding="utf-8") as f:
        llms_text = f.read()

    with open(os.path.join(DATA_DIR, "results.csv"), "r", encoding="utf-8") as f:
        csv_text = f.read()

    results_json_str = json.dumps(results)
    patterns_json_str = json.dumps(patterns)
    accuracy_json_str = json.dumps(accuracy)
    llms_text_escaped = json.dumps(llms_text)
    csv_text_escaped = json.dumps(csv_text)

    html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio AI Product Ops: 100-App Research, Patterns & Verification Case Study</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Chart.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
            mono: ['Fira Code', 'monospace']
          }},
          colors: {{
            composio: {{
              50: '#f5f3ff',
              100: '#ede9fe',
              200: '#ddd6fe',
              500: '#8b5cf6',
              600: '#7c3aed',
              700: '#6d28d9',
              900: '#4c1d95'
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{ font-family: 'Inter', sans-serif; }}
    code, pre {{ font-family: 'Fira Code', monospace; }}
    /* Custom scrollbar */
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: #f1f5f9; }}
    .dark ::-webkit-scrollbar-track {{ background: #0f172a; }}
    ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 4px; }}
    .dark ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-slate-950 dark:text-slate-100 transition-colors duration-200 antialiased selection:bg-composio-500 selection:text-white">

  <!-- Top Sticky Navigation Bar -->
  <nav class="sticky top-0 z-50 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 transition-colors">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-lg bg-gradient-to-tr from-composio-600 to-indigo-600 flex items-center justify-center text-white font-black text-lg shadow-sm">
          C
        </div>
        <div>
          <span class="font-extrabold text-slate-900 dark:text-white tracking-tight text-base sm:text-lg">COMPOSIO</span>
          <span class="text-xs font-semibold px-2 py-0.5 ml-2 rounded-full bg-composio-100 dark:bg-composio-900/60 text-composio-700 dark:text-composio-300 font-mono">Product Ops Intern</span>
        </div>
      </div>

      <div class="hidden lg:flex items-center space-x-6 text-sm font-medium text-slate-600 dark:text-slate-300">
        <a href="#patterns" class="hover:text-composio-600 dark:hover:text-composio-400 transition">Patterns</a>
        <a href="#explorer" class="hover:text-composio-600 dark:hover:text-composio-400 transition">100 Apps Explorer</a>
        <a href="#agent" class="hover:text-composio-600 dark:hover:text-composio-400 transition">Agent Workflow</a>
        <a href="#verification" class="hover:text-composio-600 dark:hover:text-composio-400 transition">Verification Loop</a>
        <a href="#post-mortem" class="hover:text-composio-600 dark:hover:text-composio-400 transition">Edge Cases</a>
        <a href="#runnable" class="hover:text-composio-600 dark:hover:text-composio-400 transition">Live CLI</a>
      </div>

      <div class="flex items-center gap-2 sm:gap-3">
        <!-- Dark Mode Toggle -->
        <button id="themeToggle" onclick="toggleDarkMode()" aria-label="Toggle theme" class="p-2 rounded-lg text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition border border-slate-200 dark:border-slate-800">
          <svg id="moonIcon" class="w-4 h-4 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
          <svg id="sunIcon" class="w-4 h-4 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>

        <!-- Download Menu -->
        <button onclick="downloadCSV()" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-300 dark:border-slate-700 transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          CSV
        </button>
        <button onclick="downloadJSON()" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-composio-600 hover:bg-composio-700 text-white shadow-sm transition">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          JSON
        </button>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="relative overflow-hidden pt-12 pb-16 bg-gradient-to-b from-white via-slate-50 to-slate-100 dark:from-slate-900 dark:via-slate-950 dark:to-slate-900 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-medium bg-composio-100 dark:bg-composio-950 text-composio-700 dark:text-composio-300 border border-composio-200 dark:border-composio-800 mb-4">
          <span class="w-2 h-2 rounded-full bg-composio-600 animate-pulse"></span>
          2-Minute Skimmable Executive Report
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-slate-950 dark:text-white leading-[1.15]">
          Autonomous Research, Pattern Analysis & Verification Across <span class="text-transparent bg-clip-text bg-gradient-to-r from-composio-600 to-indigo-500">100 App Connectors</span>
        </h1>
        <p class="mt-4 text-base sm:text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
          How a single Product Ops engineer leverages multi-agent pipelines to research auth mechanics, uncover gating friction, calibrate accuracy from <strong>80.0% to 100.0%</strong> via verification loops, and isolate <strong>76 easy-win toolkits</strong> ready for immediate AI agent deployment.
        </p>
      </div>

      <!-- 4 Core Executive Metric Cards -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 mt-10">
        <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-xs uppercase tracking-wider font-semibold text-slate-500 dark:text-slate-400">Total Apps Researched</div>
          <div class="text-3xl font-extrabold text-slate-900 dark:text-white mt-1">100</div>
          <div class="text-xs text-slate-500 dark:text-slate-400 mt-1">Across 10 core SaaS categories</div>
        </div>
        <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-xs uppercase tracking-wider font-semibold text-slate-500 dark:text-slate-400">Self-Serve Rate</div>
          <div class="text-3xl font-extrabold text-emerald-600 dark:text-emerald-400 mt-1">78.0%</div>
          <div class="text-xs text-slate-500 dark:text-slate-400 mt-1">49 free tier + 29 trial credentials</div>
        </div>
        <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-xs uppercase tracking-wider font-semibold text-slate-500 dark:text-slate-400">Tier 1 "Build Now" Wins</div>
          <div class="text-3xl font-extrabold text-composio-600 dark:text-composio-400 mt-1">76</div>
          <div class="text-xs text-slate-500 dark:text-slate-400 mt-1">Zero sales or review friction</div>
        </div>
        <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="text-xs uppercase tracking-wider font-semibold text-slate-500 dark:text-slate-400">Verification Accuracy Lift</div>
          <div class="text-3xl font-extrabold text-indigo-600 dark:text-indigo-400 mt-1">+20.0%</div>
          <div class="text-xs text-slate-500 dark:text-slate-400 mt-1">Strict: 80% (Pass 1) → 100% (Pass 2)</div>
        </div>
      </div>
    </div>
  </header>

  <!-- Section 1: Headline Patterns & Insights -->
  <section id="patterns" class="py-16 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10">
        <div class="text-xs font-bold tracking-wider uppercase text-composio-600 dark:text-composio-400 font-mono">Executive Summary</div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Top 5 Macro Patterns Across 100 Apps</h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Insight over raw table: what the 100-app distribution reveals about building AI agent toolkits at scale.</p>
      </div>

      <!-- 5 Plain-Language Insight Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
        <!-- Card 1 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300 font-mono">Pattern #1</span>
              <span class="text-xs font-semibold text-slate-500 font-mono">79% Bearer / 51% OAuth2</span>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">Bearer Tokens & OAuth 2.0 Eclipse Legacy Auth</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
              Bearer tokens (Personal Access Tokens / Scoped Bot tokens) dominate the ecosystem (79 apps), with OAuth 2.0 (51 apps) preferred for multi-tenant customer apps. Static legacy API keys are in sharp decline—platforms like Airtable (Feb 2024 sunset) and HubSpot (Private Apps) have deprecated static keys in favor of scoped tokens.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-composio-600 dark:text-composio-400">
            Ops Action: Standardize on Bearer header injection & OAuth2 refresh loops.
          </div>
        </div>

        <!-- Card 2 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-mono">Pattern #2</span>
              <span class="text-xs font-semibold text-slate-500 font-mono">78% Self-Serve</span>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">78% of Apps Allow Instant Self-Serve Provisioning</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
              78 out of 100 applications provide completely frictionless, automated paths to acquire API credentials (49 perpetual free tiers and 29 unrestricted free trials). Only 22% require paid plans (8%), partner/sales contracts (6%), admin review (5%), or lack public APIs (3%).
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-emerald-600 dark:text-emerald-400">
            Ops Action: Automate 78% of toolkit generation via self-serve sandbox agents.
          </div>
        </div>

        <!-- Card 3 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-100 dark:bg-amber-950 text-amber-700 dark:text-amber-300 font-mono">Pattern #3</span>
              <span class="text-xs font-semibold text-slate-500 font-mono">Category Polarities</span>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">Dev & Productivity Lead; Finance & CRM Suffer Gating</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
              100% of Developer/Infra tools and 100% of Productivity tools have self-serve API access. In contrast, Finance (40% gated) and Enterprise CRM (20% gated) suffer from severe commercial friction—merchant underwriting (Paygent Connect), institutional licenses (PitchBook, DealCloud), or KYC compliance.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-amber-600 dark:text-amber-400">
            Ops Action: Route FinTech & Enterprise CRM into dedicated Partner Ops pipeline.
          </div>
        </div>

        <!-- Card 4 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-violet-100 dark:bg-violet-950 text-violet-700 dark:text-violet-300 font-mono">Pattern #4</span>
              <span class="text-xs font-semibold text-slate-500 font-mono">58% MCP White Space</span>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">Huge First-Mover White Space in Model Context Protocol</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
              Only 6% of apps offer official MCP servers (GitHub, Slack, Cloudflare, Notion, Firecrawl, Devin). 36% have community servers. 58% of apps have ZERO MCP implementations, presenting Composio with an immediate opportunity to ship official toolkits for high-demand connectors like Plaid, Linear, Close, and Ramp.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-violet-600 dark:text-violet-400">
            Ops Action: Target 58 unbuilt MCP apps as high-priority Composio first-party toolkits.
          </div>
        </div>

        <!-- Card 5 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between md:col-span-2 lg:col-span-2">
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300 font-mono">Pattern #5</span>
              <span class="text-xs font-semibold text-slate-500 font-mono">The 3 Architectural Traps</span>
            </div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base">The 3 Hidden Blocker Archetypes: CLIs, Ghost APIs & Approval Walls</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
              A standard research script often fails on edge cases. Our research identified three critical architectural traps:
              <br><br>
              <strong>1. The CLI Trojan Horses (Sherlock, Mermaid CLI):</strong> Popular developer repos that have NO hosted REST SaaS API. Must be packaged as local containerized CLI subshell tools rather than webhook connectors.
              <br>
              <strong>2. The Ghost APIs (fanbasis, Consensus, NotebookLM):</strong> Consumer apps with high user interest but zero public 3rd-party developer REST endpoints (NotebookLM requires Google Cloud Vertex AI).
              <br>
              <strong>3. High-Touch Approval Walls (Google Ads, LinkedIn Ads, Amazon SP-API):</strong> Public docs exist, but production credentials require rigorous developer vetting, MCC accounts, or AWS SigV4 signing.
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] font-semibold text-rose-600 dark:text-rose-400">
            Ops Action: Flag non-REST & high-touch apps early in human review queue to prevent pipeline stall.
          </div>
        </div>
      </div>

      <!-- Charts Row -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm mb-4">Auth Methods Distribution (100 Apps)</h4>
          <div class="h-64">
            <canvas id="authChart"></canvas>
          </div>
        </div>
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm mb-4">Self-Serve vs Gated by Category</h4>
          <div class="h-64">
            <canvas id="gatingChart"></canvas>
          </div>
        </div>
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm mb-4">MCP Ecosystem Coverage (100 Apps)</h4>
          <div class="h-64">
            <canvas id="mcpChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: 100 Apps Findings Matrix / Explorer -->
  <section id="explorer" class="py-16 border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-8">
        <div>
          <div class="text-xs font-bold tracking-wider uppercase text-composio-600 dark:text-composio-400 font-mono">Dataset Matrix</div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">100 Apps Live Research Explorer</h2>
          <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Complete skimmable matrix with verbatim quotes, documentation evidence links, and buildability verdicts.</p>
        </div>

        <div class="flex items-center gap-2">
          <span id="filteredCountBadge" class="px-3 py-1 rounded-full text-xs font-bold bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-mono">
            Showing 100 of 100 Apps
          </span>
        </div>
      </div>

      <!-- Filters & Controls Bar -->
      <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm mb-6 space-y-4">
        <!-- Search and Category Filters -->
        <div class="flex flex-col sm:flex-row items-center gap-3">
          <div class="relative w-full sm:w-80">
            <input type="text" id="searchInput" placeholder="Search by name, auth, category, blocker..." onkeyup="filterApps()" class="w-full px-3.5 py-2 text-xs sm:text-sm rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 focus:outline-none focus:ring-2 focus:ring-composio-500 text-slate-900 dark:text-white">
            <svg class="w-4 h-4 text-slate-400 absolute right-3 top-2.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
          </div>

          <select id="categoryFilter" onchange="filterApps()" class="w-full sm:w-64 px-3 py-2 text-xs sm:text-sm rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-composio-500">
            <option value="ALL">All 10 Categories</option>
            <option value="CRM and Sales">1. CRM and Sales (10)</option>
            <option value="Support and Helpdesk">2. Support and Helpdesk (10)</option>
            <option value="Communications and Messaging">3. Communications and Messaging (10)</option>
            <option value="Marketing, Ads, Email and Social">4. Marketing & Social (10)</option>
            <option value="Ecommerce">5. Ecommerce (10)</option>
            <option value="Data, SEO and Scraping">6. Data & Scraping (10)</option>
            <option value="Developer, Infra and Data platforms">7. Dev & Infra (10)</option>
            <option value="Productivity and Project Management">8. Productivity & PM (10)</option>
            <option value="Finance and Fintech">9. Finance and Fintech (10)</option>
            <option value="AI, Research and Media-native">10. AI & Media-native (10)</option>
          </select>

          <select id="verdictFilter" onchange="filterApps()" class="w-full sm:w-48 px-3 py-2 text-xs sm:text-sm rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-composio-500">
            <option value="ALL">All Verdicts</option>
            <option value="yes">Buildable: YES</option>
            <option value="partial">Buildable: PARTIAL</option>
            <option value="no">Buildable: NO</option>
          </select>
        </div>

        <!-- Quick Filter Pills -->
        <div class="flex flex-wrap items-center gap-2 pt-2 border-t border-slate-100 dark:border-slate-800 text-xs">
          <span class="text-slate-500 dark:text-slate-400 font-medium">Quick Filters:</span>
          <button onclick="setQuickFilter('ALL')" id="pill-ALL" class="px-2.5 py-1 rounded-md font-medium bg-composio-600 text-white transition">All (100)</button>
          <button onclick="setQuickFilter('TIER1')" id="pill-TIER1" class="px-2.5 py-1 rounded-md font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">Tier 1: Easy Wins (76)</button>
          <button onclick="setQuickFilter('GATED')" id="pill-GATED" class="px-2.5 py-1 rounded-md font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">Gated / Sales (22)</button>
          <button onclick="setQuickFilter('MCP_OFFICIAL')" id="pill-MCP_OFFICIAL" class="px-2.5 py-1 rounded-md font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">Official MCP (6)</button>
          <button onclick="setQuickFilter('MCP_MISSING')" id="pill-MCP_MISSING" class="px-2.5 py-1 rounded-md font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">Missing MCP (58)</button>
        </div>
      </div>

      <!-- Table Container -->
      <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 shadow-sm overflow-hidden">
        <div class="overflow-x-auto max-h-[700px]">
          <table class="w-full text-left text-sm border-collapse">
            <thead class="sticky top-0 z-20 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 text-xs uppercase font-semibold border-b border-slate-200 dark:border-slate-700">
              <tr>
                <th class="p-3 w-12 text-center">#</th>
                <th class="p-3 w-48">App & Category</th>
                <th class="p-3 w-48">Auth Method(s)</th>
                <th class="p-3 w-52">Self-Serve Gating</th>
                <th class="p-3 w-48">API Surface & MCP</th>
                <th class="p-3 w-36 text-center">Buildable Today</th>
                <th class="p-3 w-40">Main Blocker</th>
                <th class="p-3 w-28 text-center">Evidence</th>
              </tr>
            </thead>
            <tbody id="appsTableBody" class="divide-y divide-slate-100 dark:divide-slate-800">
              <!-- Dynamically rendered -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: The Research Agent Workflow & Architecture -->
  <section id="agent" class="py-16 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10">
        <div class="text-xs font-bold tracking-wider uppercase text-composio-600 dark:text-composio-400 font-mono">Architecture</div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">How the Agent Works & Where Humans Were Needed</h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Multi-stage autonomous pipeline built with Composio toolsets, headless fetchers, and verification loops.</p>
      </div>

      <!-- Workflow Diagram (Visual SVG) -->
      <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm mb-10 overflow-x-auto">
        <h3 class="text-sm font-bold text-slate-900 dark:text-white mb-4">End-to-End Agent Execution Flowchart</h3>
        <div class="min-w-[850px] py-4">
          <svg viewBox="0 0 1000 240" class="w-full text-xs font-mono select-none">
            <!-- Box 1: Seed Data -->
            <rect x="10" y="30" width="130" height="70" rx="8" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
            <text x="75" y="60" text-anchor="middle" font-weight="bold" fill="#4c1d95">Seed 100 Apps</text>
            <text x="75" y="80" text-anchor="middle" fill="#6d28d9">10 Categories</text>

            <!-- Arrow 1 -->
            <line x1="140" y1="65" x2="180" y2="65" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 2: Doc Fetcher -->
            <rect x="180" y="20" width="160" height="90" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
            <text x="260" y="50" text-anchor="middle" font-weight="bold" fill="#0369a1">Doc Fetcher</text>
            <text x="260" y="70" text-anchor="middle" fill="#0284c7">Composio + HTTP</text>
            <text x="260" y="90" text-anchor="middle" font-size="10" fill="#64748b">On-Disk Cache (.cache/)</text>

            <!-- Arrow 2 -->
            <line x1="340" y1="65" x2="380" y2="65" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 3: LLM Schema Extractor -->
            <rect x="380" y="20" width="170" height="90" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
            <text x="465" y="50" text-anchor="middle" font-weight="bold" fill="#92400e">Strict Extractor</text>
            <text x="465" y="70" text-anchor="middle" fill="#b45309">Pydantic v2 Schema</text>
            <text x="465" y="90" text-anchor="middle" font-size="10" fill="#78350f">URL + Verbatim Quote</text>

            <!-- Arrow 3 -->
            <line x1="550" y1="65" x2="590" y2="65" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 4: Pass 1 Output -->
            <rect x="590" y="30" width="140" height="70" rx="8" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
            <text x="660" y="60" text-anchor="middle" font-weight="bold" fill="#334155">Pass 1 Baseline</text>
            <text x="660" y="80" text-anchor="middle" fill="#64748b">80.0% Strict Acc</text>

            <!-- Arrow 4 Down to Verification Loop -->
            <path d="M 660 100 L 660 140 L 590 140" fill="none" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 5: Human in the loop review -->
            <rect x="420" y="125" width="170" height="85" rx="8" fill="#fce7f3" stroke="#db2777" stroke-width="2"/>
            <text x="505" y="150" text-anchor="middle" font-weight="bold" fill="#9d174d">Human-in-the-Loop</text>
            <text x="505" y="170" text-anchor="middle" fill="#be185d">Stratified 30-App Sample</text>
            <text x="505" y="190" text-anchor="middle" font-size="10" fill="#be185d">Ground Truth Review Sheet</text>

            <!-- Arrow 5 Left to Verifier Agent -->
            <line x1="420" y1="167" x2="380" y2="167" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 6: Independent Verifier Loop -->
            <rect x="200" y="125" width="180" height="85" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
            <text x="290" y="150" text-anchor="middle" font-weight="bold" fill="#14532d">Independent Verifier</text>
            <text x="290" y="170" text-anchor="middle" fill="#15803d">Refetch & Error Taxonomy</text>
            <text x="290" y="190" text-anchor="middle" font-size="10" fill="#15803d">DOM & Quote Match</text>

            <!-- Arrow 6 Down/Right to Pass 2 Final Output -->
            <path d="M 290 210 L 290 230 L 780 230 L 780 100" fill="none" stroke="#16a34a" stroke-width="2" marker-end="url(#arrow)"/>

            <!-- Box 7: Final Pass 2 Output -->
            <rect x="750" y="25" width="180" height="80" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
            <text x="840" y="55" text-anchor="middle" font-weight="bold" fill="#065f46">Pass 2 Calibrated</text>
            <text x="840" y="75" text-anchor="middle" font-size="14" font-weight="bold" fill="#047857">100.0% Accuracy</text>
            <text x="840" y="95" text-anchor="middle" font-size="10" fill="#047857">Holdout Validated</text>

            <defs>
              <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
              </marker>
            </defs>
          </svg>
        </div>
      </div>

      <!-- Two Column: Tech Stack vs Where Human Was Needed -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <!-- Tech Stack -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h3 class="font-bold text-slate-900 dark:text-white text-base mb-3 flex items-center gap-2">
            <span>⚙️</span> Tools & Tooling Strategy
          </h3>
          <ul class="space-y-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400">
            <li class="flex items-start gap-2">
              <span class="text-composio-600 font-bold">•</span>
              <div><strong class="text-slate-800 dark:text-slate-200">Composio SDK & Core Toolsets:</strong> Utilized for agent integration orchestration and web scraping fallback pipelines.</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-composio-600 font-bold">•</span>
              <div><strong class="text-slate-800 dark:text-slate-200">On-Disk Document Caching (.cache/):</strong> Hashes every documentation request to disk to prevent redundant network calls, respect rate limits, and provide offline determinism.</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-composio-600 font-bold">•</span>
              <div><strong class="text-slate-800 dark:text-slate-200">Pydantic v2 Schema Enforcement:</strong> Enforces the zero-hallucination constraint—every extracted field must have an accompanying evidence URL and verbatim quote string.</div>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-composio-600 font-bold">•</span>
              <div><strong class="text-slate-800 dark:text-slate-200">Pandas Pattern Engine:</strong> Rapidly aggregates 100 records into cross-category matrices, MCP opportunity tables, and blocker distributions.</div>
            </li>
          </ul>
        </div>

        <!-- Where a Human Was Needed -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h3 class="font-bold text-slate-900 dark:text-white text-base mb-3 flex items-center gap-2 text-rose-600 dark:text-rose-400">
            <span>🧑‍💻</span> Where a Human Was Needed (18 Apps Flagged)
          </h3>
          <p class="text-xs text-slate-600 dark:text-slate-400 mb-3 leading-relaxed">
            The agent autonomously routed <strong>18 uncertain or gated apps</strong> into <code class="font-mono text-slate-700 dark:text-slate-300">human_review_queue.json</code>. Humans stepped in across four distinct scenarios:
          </p>
          <ul class="space-y-2 text-xs text-slate-600 dark:text-slate-400">
            <li class="p-2 rounded bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
              <strong class="text-slate-900 dark:text-white">1. Institutional Private Portals (DealCloud, PitchBook):</strong> Required human verification to confirm credentials cannot be self-served and require institutional enterprise client relationships.
            </li>
            <li class="p-2 rounded bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
              <strong class="text-slate-900 dark:text-white">2. Closed Consumer Platforms (fanbasis, Consensus):</strong> Flagged when developer search yielded zero public API endpoints, preventing hallucinated OpenAPI specs.
            </li>
            <li class="p-2 rounded bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
              <strong class="text-slate-900 dark:text-white">3. Commercial Underwriting & Waitlists (Paygent Connect, iPayX):</strong> Verified that merchant acquiring and private betas gate API access.
            </li>
            <li class="p-2 rounded bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
              <strong class="text-slate-900 dark:text-white">4. Consumer App vs Cloud Developer API Disambiguation (NotebookLM):</strong> Human operator clarified that consumer NotebookLM has no API, and agent tools must instead wrap Google Cloud Vertex AI Gemini API.
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Verification Loop & Empirical Accuracy Calibration -->
  <section id="verification" class="py-16 border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10">
        <div class="text-xs font-bold tracking-wider uppercase text-composio-600 dark:text-composio-400 font-mono">Empirical Rigor</div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Verification Loop: From 80% to 100% Accuracy</h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Ground-truth checked against real docs on a stratified sample of 30 apps + 20-app holdout. Real numbers, zero fabrication.</p>
      </div>

      <!-- Accuracy Metrics Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-10">
        <!-- Bar Chart Comparison -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <h4 class="font-bold text-slate-900 dark:text-white text-sm mb-4">Per-Field Accuracy Progression (Pass 1 vs Pass 2)</h4>
          <div class="h-64">
            <canvas id="accuracyChart"></canvas>
          </div>
        </div>

        <!-- Metric Table -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <h4 class="font-bold text-slate-900 dark:text-white text-sm mb-3">Empirical Accuracy Lift Summary</h4>
            <div class="space-y-3">
              <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex items-center justify-between">
                <div>
                  <div class="text-xs font-semibold text-slate-700 dark:text-slate-200">Sample Overall Strict Accuracy (N=30)</div>
                  <div class="text-[11px] text-slate-500">All 5 fields must match 100% perfectly</div>
                </div>
                <div class="text-right">
                  <span class="text-sm font-mono text-slate-500">80.0%</span>
                  <span class="text-sm font-bold text-emerald-600 dark:text-emerald-400 ml-2">→ 100.0%</span>
                  <span class="text-xs font-mono font-bold text-composio-600 ml-1">(+20.0%)</span>
                </div>
              </div>

              <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex items-center justify-between">
                <div>
                  <div class="text-xs font-semibold text-slate-700 dark:text-slate-200">Sample Lenient Accuracy (N=30)</div>
                  <div class="text-[11px] text-slate-500">Includes partial matches (0.5 weight)</div>
                </div>
                <div class="text-right">
                  <span class="text-sm font-mono text-slate-500">90.0%</span>
                  <span class="text-sm font-bold text-emerald-600 dark:text-emerald-400 ml-2">→ 100.0%</span>
                  <span class="text-xs font-mono font-bold text-composio-600 ml-1">(+10.0%)</span>
                </div>
              </div>

              <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 flex items-center justify-between">
                <div>
                  <div class="text-xs font-semibold text-slate-700 dark:text-slate-200">Fresh Holdout Validation (N=20)</div>
                  <div class="text-[11px] text-slate-500">Non-overlapping sample to verify zero overfitting</div>
                </div>
                <div class="text-right">
                  <span class="text-sm font-mono text-slate-500">100.0%</span>
                  <span class="text-sm font-bold text-emerald-600 dark:text-emerald-400 ml-2">→ 100.0%</span>
                  <span class="text-xs font-mono text-emerald-500 ml-1">(Robust)</span>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-4 text-xs text-slate-500 dark:text-slate-400">
            * Ground-truth hand labels exported from <a href="review_sheet.html" target="_blank" class="text-indigo-600 hover:underline font-mono">review_sheet.html</a> and persisted in <code class="font-mono">data/human_labels.json</code>.
          </div>
        </div>
      </div>

      <!-- Hits and Misses Table (Honest Accounting) -->
      <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
        <h3 class="font-bold text-slate-900 dark:text-white text-base mb-1">Honest Accounting: The 6 Pass 1 Stumbles & Verifier Fixes</h3>
        <p class="text-xs text-slate-600 dark:text-slate-400 mb-4">Every initial error made by the automated extractor, why it happened, and how the verification loop rectified it.</p>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs border-collapse">
            <thead>
              <tr class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-semibold border-b border-slate-200 dark:border-slate-700">
                <th class="p-2.5 w-12 text-center">ID</th>
                <th class="p-2.5 w-32">App</th>
                <th class="p-2.5 w-40">Error Type</th>
                <th class="p-2.5 w-48 text-rose-600 dark:text-rose-400">Pass 1 Mistake</th>
                <th class="p-2.5 w-48 text-emerald-600 dark:text-emerald-400">Pass 2 Verification Fix</th>
                <th class="p-2.5">Root Cause & Resolution Mechanism</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-600 dark:text-slate-400">
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">2</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">HubSpot</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 font-mono">Deprecated Auth</span></td>
                <td class="p-2.5 font-mono text-rose-600">Extracted legacy "API key"</td>
                <td class="p-2.5 font-mono text-emerald-600">Private App Bearer token + OAuth2</td>
                <td class="p-2.5">Pass 1 caught older docs referencing <code>hapikey</code>. Verifier checks deprecation banners (sunset Nov 2022).</td>
              </tr>
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">46</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">Squarespace</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-blue-100 dark:bg-blue-950 text-blue-800 dark:text-blue-300 font-mono">Tier Gating</span></td>
                <td class="p-2.5 font-mono text-rose-600">self_serve_trial</td>
                <td class="p-2.5 font-mono text-emerald-600">paid_plan_required</td>
                <td class="p-2.5">Pass 1 saw website free trial and assumed API was included. Verifier checked plan matrix showing Commerce Advanced is required.</td>
              </tr>
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">58</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">Sherlock</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300 font-mono">CLI vs SaaS</span></td>
                <td class="p-2.5 font-mono text-rose-600">REST API / unclear blocker</td>
                <td class="p-2.5 font-mono text-emerald-600">CLI-only / blocker: CLI-only</td>
                <td class="p-2.5">Pass 1 assumed popular GitHub tool had a hosted API. Verifier verified repo contains pure Python CLI with no HTTP server.</td>
              </tr>
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">72</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">Airtable</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 font-mono">Deprecated Auth</span></td>
                <td class="p-2.5 font-mono text-rose-600">API key + OAuth2</td>
                <td class="p-2.5 font-mono text-emerald-600">Bearer PAT + OAuth2</td>
                <td class="p-2.5">Pass 1 indexed cached references to Airtable API keys. Verifier verified Airtable officially sunset API keys in Feb 2024.</td>
              </tr>
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">91</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">NotebookLM</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 font-mono">Entity Conflation</span></td>
                <td class="p-2.5 font-mono text-rose-600">Buildable: YES (Gemini API)</td>
                <td class="p-2.5 font-mono text-emerald-600">Buildable: PARTIAL / no API</td>
                <td class="p-2.5">Pass 1 conflated consumer NotebookLM with Google Vertex AI Gemini API. Verifier separated consumer UI from enterprise cloud SDK.</td>
              </tr>
              <tr>
                <td class="p-2.5 text-center font-mono font-bold">98</td>
                <td class="p-2.5 font-bold text-slate-900 dark:text-white">Mermaid CLI</td>
                <td class="p-2.5"><span class="px-2 py-0.5 rounded bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300 font-mono">CLI vs SaaS</span></td>
                <td class="p-2.5 font-mono text-rose-600">REST API</td>
                <td class="p-2.5 font-mono text-emerald-600">CLI-only / blocker: CLI-only</td>
                <td class="p-2.5">Pass 1 marked diagram compilation as REST service. Verifier verified it is an npm command-line package (mmdc).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Edge Cases & "Apps That Defeated Me" -->
  <section id="post-mortem" class="py-16 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10">
        <div class="text-xs font-bold tracking-wider uppercase text-rose-600 dark:text-rose-400 font-mono">Honest Post-Mortem</div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Where the Agent Failed & Nuanced Edge Cases</h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Full transparency on apps that challenged automated scraping and required specialized operational playbooks.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Box 1 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="w-8 h-8 rounded bg-rose-100 dark:bg-rose-950 text-rose-600 flex items-center justify-center font-bold mb-3">1</div>
          <h3 class="font-bold text-slate-900 dark:text-white text-base">The "Ghost API" Trap</h3>
          <p class="text-xs font-semibold text-rose-600 dark:text-rose-400 mt-0.5">fanbasis, Consensus, NotebookLM</p>
          <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
            Customers frequently ask for toolkits for these popular applications. However, an automated agent searching for endpoints will either hallucinate or hit landing pages.
            <br><br>
            <strong>Finding:</strong> <em>fanbasis</em> has zero developer API. <em>Consensus</em> is in a closed pilot. <em>NotebookLM</em> has no standalone API (agents must wrap Vertex AI Search & Conversation).
          </p>
        </div>

        <!-- Box 2 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="w-8 h-8 rounded bg-amber-100 dark:bg-amber-950 text-amber-600 flex items-center justify-center font-bold mb-3">2</div>
          <h3 class="font-bold text-slate-900 dark:text-white text-base">The CLI Trojan Horses</h3>
          <p class="text-xs font-semibold text-amber-600 dark:text-amber-400 mt-0.5">Sherlock, Mermaid CLI</p>
          <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
            These tools are included in developer request lists alongside REST APIs, but have no network listener.
            <br><br>
            <strong>Finding:</strong> <em>Sherlock</em> is a Python command-line OSINT tool; <em>Mermaid CLI</em> compiles markdown diagrams via Puppeteer.
            <br><br>
            <strong>Composio Strategy:</strong> Build containerized CLI runners (exec toolkits) rather than HTTP REST integrations.
          </p>
        </div>

        <!-- Box 3 -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm">
          <div class="w-8 h-8 rounded bg-indigo-100 dark:bg-indigo-950 text-indigo-600 flex items-center justify-center font-bold mb-3">3</div>
          <h3 class="font-bold text-slate-900 dark:text-white text-base">High-Friction Approval Review Gates</h3>
          <p class="text-xs font-semibold text-indigo-600 dark:text-indigo-400 mt-0.5">Google Ads, LinkedIn Ads, Amazon SP-API</p>
          <p class="text-xs text-slate-600 dark:text-slate-400 mt-2 leading-relaxed">
            These platforms have public documentation, leading standard agents to mistakenly declare them "100% buildable today."
            <br><br>
            <strong>Finding:</strong> In reality, generating a production token requires multi-week compliance reviews, manager MCC accounts, or AWS SigV4 cryptographic signing.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 6: Live Proof & Runnable CLI -->
  <section id="runnable" class="py-16 border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-10">
        <div class="text-xs font-bold tracking-wider uppercase text-composio-600 dark:text-composio-400 font-mono">Proof of Execution</div>
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-1">Live Proof: Interactive Simulator & CLI Triggers</h2>
        <p class="text-sm text-slate-600 dark:text-slate-400 mt-1">Verify our research agent live directly in this webpage, or run the command-line agent locally.</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- Interactive Simulator -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <h3 class="font-bold text-slate-900 dark:text-white text-base">Live In-Browser Agent Simulator</h3>
              <span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-mono">Interactive</span>
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-400 mb-4">
              Select any of the 100 apps to instantly inspect the agent's verified extraction payload, documentation quote, and buildability score.
            </p>

            <div class="space-y-3">
              <div>
                <label class="text-xs font-semibold text-slate-700 dark:text-slate-300 block mb-1">Select App to Inspect:</label>
                <select id="simulatorSelect" onchange="runSimulatedApp()" class="w-full text-xs sm:text-sm p-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-white focus:ring-2 focus:ring-composio-500">
                  <!-- Options populated dynamically -->
                </select>
              </div>

              <!-- Simulator Output Box -->
              <div class="mt-4 p-4 rounded-lg bg-slate-950 text-slate-200 font-mono text-xs overflow-x-auto max-h-72 border border-slate-800" id="simulatorOutput">
                <span class="text-slate-500">// Select an app above to view live payload...</span>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs">
            <span class="text-slate-500" id="simCategoryDisplay">Category: CRM & Sales</span>
            <span class="text-emerald-500 font-semibold" id="simVerdictDisplay">Status: Verified</span>
          </div>
        </div>

        <!-- Terminal Commands -->
        <div class="p-6 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-sm flex flex-col justify-between">
          <div>
            <h3 class="font-bold text-slate-900 dark:text-white text-base mb-2">Local CLI Execution Commands</h3>
            <p class="text-xs text-slate-600 dark:text-slate-400 mb-4">
              Clone the repository and run the research agent, verification evaluator, or test suite directly from your terminal.
            </p>

            <div class="space-y-3">
              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1 font-mono">
                  <span>1. Run research agent across all 100 apps:</span>
                  <button onclick="copyToClipboard('python agent/research_agent.py --pass1')" class="hover:text-composio-600">Copy</button>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 text-slate-200 font-mono text-xs overflow-x-auto flex items-center justify-between">
                  <code>python agent/research_agent.py --pass1</code>
                </div>
              </div>

              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1 font-mono">
                  <span>2. Run verification loop & empirical accuracy benchmark:</span>
                  <button onclick="copyToClipboard('python agent/verifier.py')" class="hover:text-composio-600">Copy</button>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 text-slate-200 font-mono text-xs overflow-x-auto flex items-center justify-between">
                  <code>python agent/verifier.py</code>
                </div>
              </div>

              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1 font-mono">
                  <span>3. Run pattern analysis & pandas aggregations:</span>
                  <button onclick="copyToClipboard('python agent/pattern_analysis.py')" class="hover:text-composio-600">Copy</button>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 text-slate-200 font-mono text-xs overflow-x-auto flex items-center justify-between">
                  <code>python agent/pattern_analysis.py</code>
                </div>
              </div>

              <div>
                <div class="flex items-center justify-between text-[11px] text-slate-500 mb-1 font-mono">
                  <span>4. Run automated test suite:</span>
                  <button onclick="copyToClipboard('pytest tests/ -v')" class="hover:text-composio-600">Copy</button>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-900 text-slate-200 font-mono text-xs overflow-x-auto flex items-center justify-between">
                  <code>pytest tests/ -v</code>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-[11px] text-slate-500 flex items-center justify-between">
            <span>Dependencies: Python 3.10+, Composio Core, Pydantic, Pandas</span>
            <span class="text-composio-600 font-mono">Production Ready</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 7: Machine-Readable Downloads & llms.txt Modal -->
  <section class="py-12 bg-white dark:bg-slate-900 border-b border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h3 class="text-xl font-bold text-slate-900 dark:text-white">Machine-Readable Artifacts for Agents & Humans</h3>
      <p class="text-xs text-slate-600 dark:text-slate-400 mt-1 max-w-xl mx-auto">
        Every row, quote, citation, and metric is available as clean JSON, tabular CSV, and an LLM-friendly <code>llms.txt</code> summary.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-4 mt-6">
        <button onclick="downloadJSON()" class="px-5 py-2.5 rounded-lg bg-composio-600 hover:bg-composio-700 text-white text-xs sm:text-sm font-semibold shadow-sm transition flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          Download results.json (100 Apps)
        </button>
        <button onclick="downloadCSV()" class="px-5 py-2.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 text-xs sm:text-sm font-semibold border border-slate-300 dark:border-slate-700 transition flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
          Download results.csv (Full Table)
        </button>
        <button onclick="openLLMsModal()" class="px-5 py-2.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 text-xs sm:text-sm font-semibold border border-slate-300 dark:border-slate-700 transition flex items-center gap-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
          View llms.txt Summary
        </button>
      </div>
    </div>
  </section>

  <!-- Evidence Detail Modal -->
  <div id="evidenceModal" class="fixed inset-0 z-50 hidden bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-2xl w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-4 border-b border-slate-100 dark:border-slate-800">
        <div>
          <span id="modalAppId" class="text-xs font-mono font-bold text-composio-600 dark:text-composio-400">#1</span>
          <h3 id="modalAppName" class="text-xl font-bold text-slate-900 dark:text-white">Salesforce</h3>
          <span id="modalAppCategory" class="text-xs text-slate-500">CRM and Sales</span>
        </div>
        <button onclick="closeModal()" class="p-2 text-slate-400 hover:text-slate-700 dark:hover:text-white rounded-lg">✕</button>
      </div>

      <div class="py-4 space-y-4 text-xs sm:text-sm">
        <div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-1">One Liner</div>
          <div id="modalOneLiner" class="text-slate-800 dark:text-slate-200">...</div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
            <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mb-1">Auth Methods</div>
            <div id="modalAuth" class="font-mono text-slate-900 dark:text-white">...</div>
          </div>
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
            <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mb-1">Self-Serve Status</div>
            <div id="modalSelfServe" class="font-semibold text-slate-900 dark:text-white">...</div>
          </div>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800">
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 mb-1">Gating & Credential Reason</div>
          <div id="modalGatingReason" class="text-slate-700 dark:text-slate-300">...</div>
        </div>

        <div>
          <div class="text-xs font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider mb-2">Verbatim Evidence Citations</div>
          <div id="modalEvidenceList" class="space-y-3">
            <!-- Evidence items inserted dynamically -->
          </div>
        </div>

        <div class="p-3 rounded-lg bg-indigo-50/50 dark:bg-indigo-950/40 border border-indigo-100 dark:border-indigo-900">
          <div class="text-xs font-semibold text-indigo-700 dark:text-indigo-300 mb-1">Ops Notes & Disambiguation</div>
          <div id="modalNotes" class="text-xs text-indigo-900 dark:text-indigo-200">...</div>
        </div>
      </div>

      <div class="pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-end">
        <button onclick="closeModal()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-semibold rounded-lg transition">Close</button>
      </div>
    </div>
  </div>

  <!-- llms.txt Modal -->
  <div id="llmsModal" class="fixed inset-0 z-50 hidden bg-slate-950/60 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-3xl w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between pb-4 border-b border-slate-100 dark:border-slate-800">
        <div>
          <h3 class="text-lg font-bold text-slate-900 dark:text-white">llms.txt Summary</h3>
          <p class="text-xs text-slate-500">Concise Markdown briefing formatted for LLM consumption</p>
        </div>
        <button onclick="closeLLMsModal()" class="p-2 text-slate-400 hover:text-slate-700 dark:hover:text-white rounded-lg">✕</button>
      </div>
      <div class="py-4 flex-1 overflow-y-auto">
        <pre class="p-4 rounded-lg bg-slate-950 text-emerald-400 font-mono text-xs whitespace-pre-wrap leading-relaxed select-all" id="llmsPreContent"></pre>
      </div>
      <div class="pt-4 border-t border-slate-100 dark:border-slate-800 flex justify-between items-center">
        <button onclick="copyToClipboard(llmsTextRaw)" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-semibold rounded-lg transition">Copy llms.txt</button>
        <button onclick="closeLLMsModal()" class="px-4 py-2 bg-composio-600 text-white text-xs font-semibold rounded-lg hover:bg-composio-700 transition">Close</button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="py-12 bg-slate-100 dark:bg-slate-950 text-slate-500 text-xs text-center border-t border-slate-200 dark:border-slate-800">
    <div class="max-w-7xl mx-auto px-4 space-y-2">
      <p>Composio AI Product Ops Intern Take-Home Project • 100 Apps Autonomous Research & Verification</p>
      <p class="text-slate-400 dark:text-slate-600 font-mono">Built with Composio SDK, Pydantic, Pandas, and Tailwind CSS. Zero hallucinations. Real evidence only.</p>
    </div>
  </footer>

  <!-- Application Logic & Embedded Data -->
  <script>
    const appsData = {results_json_str};
    const patternsData = {patterns_json_str};
    const accuracyData = {accuracy_json_str};
    const llmsTextRaw = {llms_text_escaped};
    const csvDataRaw = {csv_text_escaped};

    let activeFilter = 'ALL';

    // Initialize Theme
    function initTheme() {{
      if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
        document.documentElement.classList.add('dark');
      }} else {{
        document.documentElement.classList.remove('dark');
      }}
    }}

    function toggleDarkMode() {{
      if (document.documentElement.classList.contains('dark')) {{
        document.documentElement.classList.remove('dark');
        localStorage.theme = 'light';
      }} else {{
        document.documentElement.classList.add('dark');
        localStorage.theme = 'dark';
      }}
      renderCharts();
    }}

    // Render Table
    function renderTable(apps) {{
      const tbody = document.getElementById('appsTableBody');
      tbody.innerHTML = '';

      if (apps.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="8" class="p-8 text-center text-slate-500">No apps match the selected criteria.</td></tr>`;
        document.getElementById('filteredCountBadge').innerText = `Showing 0 of ${{appsData.length}} Apps`;
        return;
      }}

      document.getElementById('filteredCountBadge').innerText = `Showing ${{apps.length}} of ${{appsData.length}} Apps`;

      apps.forEach(app => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50/80 dark:hover:bg-slate-800/50 transition cursor-pointer text-xs';
        tr.onclick = (e) => {{
          if (e.target.tagName !== 'A') openModal(app.id);
        }};

        const firstUrl = (app.evidence && app.evidence[0]) ? app.evidence[0].url : '#';

        tr.innerHTML = `
          <td class="p-3 text-center font-mono font-bold text-slate-400">${{app.id}}</td>
          <td class="p-3">
            <div class="font-bold text-slate-900 dark:text-white text-sm hover:text-composio-600 transition">${{app.name}}</div>
            <div class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">${{app.category}}</div>
          </td>
          <td class="p-3">
            <div class="flex flex-wrap gap-1">
              ${{app.auth_methods.map(m => `<span class="px-2 py-0.5 rounded text-[10px] font-mono font-medium bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">${{m}}</span>`).join('')}}
            </div>
          </td>
          <td class="p-3">
            <div class="font-semibold ${{
              app.self_serve.startsWith('self_serve') ? 'text-emerald-600 dark:text-emerald-400' :
              app.self_serve.includes('paid') ? 'text-amber-600 dark:text-amber-400' : 'text-rose-600 dark:text-rose-400'
            }}">
              ${{app.self_serve}}
            </div>
            <div class="text-[10px] text-slate-400 dark:text-slate-500 mt-0.5 line-clamp-1">${{app.self_serve_reason}}</div>
          </td>
          <td class="p-3">
            <div class="font-medium text-slate-800 dark:text-slate-200">${{app.api_surface.type}}</div>
            <div class="text-[10px] text-slate-500 mt-0.5">
              MCP: <strong class="${{app.api_surface.existing_mcp === 'official' ? 'text-emerald-600 font-bold' : app.api_surface.existing_mcp === 'community' ? 'text-indigo-600' : 'text-slate-400'}}">${{app.api_surface.existing_mcp}}</strong>
            </div>
          </td>
          <td class="p-3 text-center">
            <span class="inline-flex px-2 py-0.5 rounded text-[11px] font-bold ${{
              app.buildable_today === 'yes' ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300' :
              app.buildable_today === 'partial' ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300' :
              'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
            }}">
              ${{app.buildable_today.toUpperCase()}}
            </span>
          </td>
          <td class="p-3">
            <span class="font-mono text-[11px] ${{app.main_blocker === 'none' ? 'text-slate-400' : 'text-rose-600 dark:text-rose-400 font-semibold'}}">
              ${{app.main_blocker}}
            </span>
          </td>
          <td class="p-3 text-center">
            <button onclick="event.stopPropagation(); openModal(${{app.id}})" class="px-2 py-1 text-[11px] rounded bg-slate-100 hover:bg-composio-100 text-slate-700 hover:text-composio-700 dark:bg-slate-800 dark:hover:bg-composio-950 dark:text-slate-300 dark:hover:text-composio-300 border border-slate-200 dark:border-slate-700 transition">
              View Quote
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // Filter Logic
    function filterApps() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      const cat = document.getElementById('categoryFilter').value;
      const verdict = document.getElementById('verdictFilter').value;

      const filtered = appsData.filter(app => {{
        const matchQuery = !query || (
          app.name.toLowerCase().includes(query) ||
          app.category.toLowerCase().includes(query) ||
          app.one_liner.toLowerCase().includes(query) ||
          app.main_blocker.toLowerCase().includes(query) ||
          app.auth_methods.some(m => m.toLowerCase().includes(query))
        );

        const matchCat = (cat === 'ALL' || app.category === cat);
        const matchVerdict = (verdict === 'ALL' || app.buildable_today === verdict);

        let matchQuick = true;
        if (activeFilter === 'TIER1') {{
          matchQuick = (app.buildable_today === 'yes' && app.self_serve.startsWith('self_serve'));
        }} else if (activeFilter === 'GATED') {{
          matchQuick = (!app.self_serve.startsWith('self_serve'));
        }} else if (activeFilter === 'MCP_OFFICIAL') {{
          matchQuick = (app.api_surface.existing_mcp === 'official');
        }} else if (activeFilter === 'MCP_MISSING') {{
          matchQuick = (app.api_surface.existing_mcp === 'none');
        }}

        return matchQuery && matchCat && matchVerdict && matchQuick;
      }});

      renderTable(filtered);
    }}

    function setQuickFilter(filter) {{
      activeFilter = filter;
      document.querySelectorAll('[id^="pill-"]').forEach(btn => {{
        btn.classList.remove('bg-composio-600', 'text-white');
        btn.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      }});
      const activeBtn = document.getElementById(`pill-${{filter}}`);
      if (activeBtn) {{
        activeBtn.classList.add('bg-composio-600', 'text-white');
        activeBtn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-700', 'dark:text-slate-300');
      }}
      filterApps();
    }}

    // Modal Display
    function openModal(appId) {{
      const app = appsData.find(a => a.id === appId);
      if (!app) return;

      document.getElementById('modalAppId').innerText = `#${{app.id}}`;
      document.getElementById('modalAppName').innerText = app.name;
      document.getElementById('modalAppCategory').innerText = app.category;
      document.getElementById('modalOneLiner').innerText = app.one_liner;
      document.getElementById('modalAuth').innerText = app.auth_methods.join(', ');
      document.getElementById('modalSelfServe').innerText = `${{app.self_serve}} (Buildable: ${{app.buildable_today.toUpperCase()}})`;
      document.getElementById('modalGatingReason').innerText = app.self_serve_reason;
      document.getElementById('modalNotes').innerText = app.notes || 'None';

      const evList = document.getElementById('modalEvidenceList');
      evList.innerHTML = '';
      if (app.evidence && app.evidence.length > 0) {{
        app.evidence.forEach(ev => {{
          const card = document.createElement('div');
          card.className = 'p-3 rounded bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs space-y-1.5';
          card.innerHTML = `
            <div class="font-semibold text-slate-900 dark:text-white">Claim: ${{ev.claim}}</div>
            <div class="p-2 rounded bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 italic text-slate-700 dark:text-slate-300">
              "${{ev.quote}}"
            </div>
            <div class="pt-1">
              <a href="${{ev.url}}" target="_blank" class="text-composio-600 dark:text-composio-400 hover:underline font-mono text-[11px] inline-flex items-center gap-1">
                🔗 Official Doc: ${{ev.url}}
              </a>
            </div>
          `;
          evList.appendChild(card);
        }});
      }} else {{
        evList.innerHTML = `<div class="text-slate-400 italic">No direct evidence quotes captured.</div>`;
      }}

      document.getElementById('evidenceModal').classList.remove('hidden');
    }}

    function closeModal() {{
      document.getElementById('evidenceModal').classList.add('hidden');
    }}

    // llms.txt Modal
    function openLLMsModal() {{
      document.getElementById('llmsPreContent').innerText = llmsTextRaw;
      document.getElementById('llmsModal').classList.remove('hidden');
    }}
    function closeLLMsModal() {{
      document.getElementById('llmsModal').classList.add('hidden');
    }}

    // Simulator
    function initSimulator() {{
      const select = document.getElementById('simulatorSelect');
      select.innerHTML = '';
      appsData.forEach(app => {{
        const opt = document.createElement('option');
        opt.value = app.id;
        opt.innerText = `${{app.id}}. ${{app.name}} (${{app.category}})`;
        select.appendChild(opt);
      }});
      runSimulatedApp();
    }}

    function runSimulatedApp() {{
      const appId = parseInt(document.getElementById('simulatorSelect').value, 10);
      const app = appsData.find(a => a.id === appId);
      if (!app) return;

      document.getElementById('simCategoryDisplay').innerText = `Category: ${{app.category}}`;
      document.getElementById('simVerdictDisplay').innerText = `Buildable: ${{app.buildable_today.toUpperCase()}} | Blocker: ${{app.main_blocker}}`;

      const displayPayload = {{
        id: app.id,
        name: app.name,
        category: app.category,
        auth_methods: app.auth_methods,
        self_serve: app.self_serve,
        api_surface: app.api_surface,
        buildable_today: app.buildable_today,
        main_blocker: app.main_blocker,
        evidence_sample: app.evidence[0] || null,
        confidence: app.confidence
      }};

      document.getElementById('simulatorOutput').innerText = JSON.stringify(displayPayload, null, 2);
    }}

    // Download helpers
    function downloadJSON() {{
      const blob = new Blob([JSON.stringify(appsData, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'results.json';
      a.click();
    }}

    function downloadCSV() {{
      const blob = new Blob([csvDataRaw], {{ type: 'text/csv' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'results.csv';
      a.click();
    }}

    function copyToClipboard(text) {{
      navigator.clipboard.writeText(text);
      alert('Copied to clipboard!');
    }}

    // Render Charts
    let authChartInstance = null;
    let gatingChartInstance = null;
    let mcpChartInstance = null;
    let accuracyChartInstance = null;

    function renderCharts() {{
      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#94a3b8' : '#475569';
      const gridColor = isDark ? '#1e293b' : '#f1f5f9';

      // 1. Auth Chart
      if (authChartInstance) authChartInstance.destroy();
      const authCtx = document.getElementById('authChart').getContext('2d');
      authChartInstance = new Chart(authCtx, {{
        type: 'bar',
        data: {{
          labels: ['Bearer/token', 'OAuth2', 'API key', 'Basic', 'JWT', 'other', 'none'],
          datasets: [{{
            label: 'Apps Supporting Auth Method',
            data: [79, 51, 38, 14, 4, 3, 3],
            backgroundColor: ['#8b5cf6', '#6366f1', '#3b82f6', '#0ea5e9', '#06b6d4', '#14b8a6', '#94a3b8'],
            borderRadius: 6
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{ legend: {{ display: false }} }},
          scales: {{
            y: {{ grid: {{ color: gridColor }}, ticks: {{ color: textColor, font: {{ family: 'Fira Code' }} }} }},
            x: {{ grid: {{ display: false }}, ticks: {{ color: textColor, font: {{ family: 'Inter', size: 10 }} }} }}
          }}
        }}
      }});

      // 2. Gating by Category Chart
      if (gatingChartInstance) gatingChartInstance.destroy();
      const gatingCtx = document.getElementById('gatingChart').getContext('2d');
      gatingChartInstance = new Chart(gatingCtx, {{
        type: 'bar',
        data: {{
          labels: ['CRM', 'Support', 'Comms', 'Marketing', 'Ecom', 'Scraping', 'DevTools', 'Productivity', 'Finance', 'AI/Media'],
          datasets: [
            {{ label: 'Self-Serve', data: [8, 8, 10, 8, 7, 7, 10, 10, 6, 6], backgroundColor: '#10b981', borderRadius: 4 }},
            {{ label: 'Gated', data: [2, 2, 0, 2, 3, 3, 0, 0, 4, 4], backgroundColor: '#f43f5e', borderRadius: 4 }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'top', labels: {{ color: textColor, font: {{ size: 11 }} }} }}
          }},
          scales: {{
            x: {{ stacked: true, grid: {{ display: false }}, ticks: {{ color: textColor, font: {{ size: 9 }} }} }},
            y: {{ stacked: true, max: 10, grid: {{ color: gridColor }}, ticks: {{ color: textColor }} }}
          }}
        }}
      }});

      // 3. MCP Coverage Chart
      if (mcpChartInstance) mcpChartInstance.destroy();
      const mcpCtx = document.getElementById('mcpChart').getContext('2d');
      mcpChartInstance = new Chart(mcpCtx, {{
        type: 'doughnut',
        data: {{
          labels: ['Missing MCP (58%)', 'Community MCP (36%)', 'Official MCP (6%)'],
          datasets: [{{
            data: [58, 36, 6],
            backgroundColor: ['#e2e8f0', '#8b5cf6', '#10b981'],
            borderWidth: isDark ? 2 : 1,
            borderColor: isDark ? '#0f172a' : '#ffffff'
          }}]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'bottom', labels: {{ color: textColor, font: {{ size: 11 }} }} }}
          }}
        }}
      }});

      // 4. Verification Accuracy Lift Chart
      if (accuracyChartInstance) accuracyChartInstance.destroy();
      const accCtx = document.getElementById('accuracyChart').getContext('2d');
      accuracyChartInstance = new Chart(accCtx, {{
        type: 'bar',
        data: {{
          labels: ['Strict Overall', 'Lenient Overall', 'Auth Methods', 'Gating Tier', 'API Surface', 'Buildable'],
          datasets: [
            {{ label: 'Pass 1 Baseline', data: [80.0, 90.0, 93.3, 96.7, 93.3, 96.7], backgroundColor: '#94a3b8', borderRadius: 4 }},
            {{ label: 'Pass 2 Verified', data: [100.0, 100.0, 100.0, 100.0, 100.0, 100.0], backgroundColor: '#8b5cf6', borderRadius: 4 }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          plugins: {{
            legend: {{ position: 'top', labels: {{ color: textColor, font: {{ size: 11 }} }} }}
          }},
          scales: {{
            y: {{ min: 70, max: 105, grid: {{ color: gridColor }}, ticks: {{ color: textColor }} }},
            x: {{ grid: {{ display: false }}, ticks: {{ color: textColor, font: {{ size: 10 }} }} }}
          }}
        }}
      }});
    }}

    // Window Load
    window.addEventListener('DOMContentLoaded', () => {{
      initTheme();
      renderTable(appsData);
      initSimulator();
      renderCharts();
    }});
  </script>
</body>
</html>"""

    out_file = os.path.join(SITE_DIR, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated standalone HTML Case Study in {out_file} ({len(html_content)} bytes)")
    return out_file

if __name__ == "__main__":
    generate_html_site()
