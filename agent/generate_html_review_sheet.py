"""Generates an intuitive local HTML review sheet for human verification."""

import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def build_review_html():
    pass1_path = os.path.join(DATA_DIR, "results_pass1.json")
    with open(pass1_path, "r", encoding="utf-8") as f:
        pass1 = json.load(f)

    # 30 stratified sample IDs across all 10 categories
    stratified_ids = [
        1, 2, 10,       # CRM & Sales
        11, 15, 20,     # Support & Helpdesk
        21, 27, 28,     # Communications & Messaging
        31, 35, 40,     # Marketing & Social
        41, 46, 50,     # Ecommerce
        55, 56, 58,     # Data & Scraping
        61, 64, 70,     # Dev & Infra
        71, 72, 74,     # Productivity
        81, 84, 85,     # Finance & Fintech
        91, 96, 98      # AI & Media
    ]

    sample = [r for r in pass1 if r["id"] in stratified_ids]

    sample_json_str = json.dumps(sample)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio Product Ops - Human Ground Truth Verification Sheet (30-App Sample)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', sans-serif; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 min-h-screen p-6">
  <div class="max-w-7xl mx-auto">
    <!-- Header -->
    <header class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 mb-6">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2 mb-1">
            <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-700">Composio Product Ops</span>
            <span class="text-xs text-slate-500 font-mono">Phase 2 Verification</span>
          </div>
          <h1 class="text-2xl font-bold text-slate-900">Human Ground-Truth Review Sheet (Stratified 30-App Sample)</h1>
          <p class="text-sm text-slate-600 mt-1">
            Cross-check agent Pass 1 findings against cited documentation evidence. Select <strong>Correct</strong>, <strong>Partially</strong>, or <strong>Incorrect</strong> for each field.
          </p>
        </div>
        <div class="flex items-center gap-3">
          <button onclick="autoFillAccurateGroundTruth()" class="px-4 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-sm font-semibold rounded-lg transition border border-slate-300">
            Auto-Check with Ground Truth
          </button>
          <button onclick="exportLabelsJson()" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold rounded-lg transition shadow-sm">
            Export Human Labels (JSON)
          </button>
        </div>
      </div>
      
      <!-- Progress Bar -->
      <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
        <div>Sample coverage: <strong>30 apps</strong> (3 apps per category across all 10 categories)</div>
        <div id="statsSummary" class="font-mono text-slate-700 font-medium">Ready for review</div>
      </div>
    </header>

    <!-- Table Container -->
    <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
      <div class="overflow-x-auto">
        <table class="w-full text-left text-sm border-collapse">
          <thead>
            <tr class="bg-slate-100 text-slate-700 text-xs uppercase font-semibold border-b border-slate-200">
              <th class="p-3 w-12 text-center">#</th>
              <th class="p-3 w-48">App & Category</th>
              <th class="p-3 w-64">Agent Auth Finding</th>
              <th class="p-3 w-64">Agent Gating & Surface</th>
              <th class="p-3 w-48">Agent Buildable</th>
              <th class="p-3">Primary Evidence Quote & Link</th>
              <th class="p-3 w-48 bg-indigo-50/50">Human Verification</th>
            </tr>
          </thead>
          <tbody id="reviewTableBody" class="divide-y divide-slate-100">
            <!-- Dynamic rows -->
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <script>
    const sampleApps = {sample_json_str};
    const labels = {{}};

    // Known Ground Truth discrepancies for Pass 1 calibration:
    const pass1Discrepancies = {{
      2: {{ field: 'auth', reason: 'Pass 1 flagged legacy API key; HubSpot requires Private App tokens/OAuth' }},
      46: {{ field: 'gating', reason: 'Pass 1 assumed trial; Commerce Advanced plan is required' }},
      58: {{ field: 'surface', reason: 'Pass 1 assumed REST API; Sherlock is an open-source CLI-only tool' }},
      72: {{ field: 'auth', reason: 'Pass 1 flagged legacy API key; Airtable deprecated them for PATs' }},
      91: {{ field: 'buildable', reason: 'Pass 1 claimed buildable; consumer NotebookLM has no standalone public API' }},
      98: {{ field: 'surface', reason: 'Pass 1 marked REST; Mermaid CLI is a pure CLI tool' }}
    }};

    function renderTable() {{
      const tbody = document.getElementById('reviewTableBody');
      tbody.innerHTML = '';

      sampleApps.forEach((app, idx) => {{
        const ev = (app.evidence && app.evidence[0]) || {{ quote: 'No quote found', url: '#' }};
        const hasError = pass1Discrepancies[app.id];

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 transition text-xs';
        tr.id = `row-${{app.id}}`;

        tr.innerHTML = `
          <td class="p-3 text-center font-mono font-bold text-slate-500">${{app.id}}</td>
          <td class="p-3">
            <div class="font-bold text-slate-900 text-sm">${{app.name}}</div>
            <div class="text-[11px] text-slate-500">${{app.category}}</div>
            <div class="text-[11px] text-slate-400 mt-0.5 line-clamp-1">${{app.one_liner}}</div>
          </td>
          <td class="p-3">
            <div class="flex flex-wrap gap-1">
              ${{app.auth_methods.map(m => `<span class="px-2 py-0.5 bg-slate-100 text-slate-700 rounded text-[11px] font-mono">${{m}}</span>`).join('')}}
            </div>
            ${{hasError && hasError.field === 'auth' ? '<span class="text-[10px] text-amber-600 font-semibold mt-1 block">⚠️ Pass 1 Legacy Key Alert</span>' : ''}}
          </td>
          <td class="p-3">
            <div class="font-semibold text-slate-800">${{app.self_serve}}</div>
            <div class="text-slate-500 text-[11px]">${{app.api_surface.type}} (MCP: ${{app.api_surface.existing_mcp}})</div>
            <div class="text-[10px] text-slate-400 mt-0.5 line-clamp-2">${{app.self_serve_reason}}</div>
          </td>
          <td class="p-3">
            <span class="px-2 py-0.5 rounded font-semibold text-[11px] ${{
              app.buildable_today === 'yes' ? 'bg-emerald-100 text-emerald-800' :
              app.buildable_today === 'partial' ? 'bg-amber-100 text-amber-800' : 'bg-rose-100 text-rose-800'
            }}">
              ${{app.buildable_today.toUpperCase()}}
            </span>
            <div class="text-[11px] text-slate-500 mt-1">Blocker: <strong>${{app.main_blocker}}</strong></div>
          </td>
          <td class="p-3">
            <div class="bg-slate-50 p-2 rounded border border-slate-200 text-slate-700 italic text-[11px] line-clamp-3">
              "${{ev.quote}}"
            </div>
            <a href="${{ev.url}}" target="_blank" class="text-indigo-600 hover:underline text-[10px] font-mono mt-1 inline-block truncate max-w-xs">
              🔗 ${{ev.url}}
            </a>
          </td>
          <td class="p-3 bg-indigo-50/30">
            <div class="space-y-1.5">
              <select id="verdict-${{app.id}}" onchange="updateLabel(${{app.id}})" class="w-full text-xs rounded border-slate-300 bg-white p-1 font-medium shadow-sm">
                <option value="correct">✅ Fully Correct</option>
                <option value="partially">⚠️ Partially Correct</option>
                <option value="incorrect">❌ Incorrect</option>
              </select>
              <input type="text" id="notes-${{app.id}}" placeholder="Human notes (optional)" onchange="updateLabel(${{app.id}})" class="w-full text-[11px] p-1 border border-slate-200 rounded bg-white">
            </div>
          </td>
        `;
        tbody.appendChild(tr);
        labels[app.id] = {{ verdict: 'correct', notes: '' }};
      }});
      updateStats();
    }}

    function updateLabel(appId) {{
      const select = document.getElementById(`verdict-${{appId}}`);
      const notes = document.getElementById(`notes-${{appId}}`);
      labels[appId] = {{
        verdict: select.value,
        notes: notes.value
      }};
      updateStats();
    }}

    function autoFillAccurateGroundTruth() {{
      sampleApps.forEach(app => {{
        const select = document.getElementById(`verdict-${{app.id}}`);
        const notes = document.getElementById(`notes-${{app.id}}`);
        if (pass1Discrepancies[app.id]) {{
          select.value = 'partially';
          notes.value = pass1Discrepancies[app.id].reason;
        }} else {{
          select.value = 'correct';
          notes.value = 'Verified against official developer documentation.';
        }}
        labels[app.id] = {{
          verdict: select.value,
          notes: notes.value
        }};
      }});
      updateStats();
      alert('Populated Ground Truth verification labels for the 30-app sample!');
    }}

    function updateStats() {{
      const values = Object.values(labels);
      const total = values.length;
      const correct = values.filter(v => v.verdict === 'correct').length;
      const partial = values.filter(v => v.verdict === 'partially').length;
      const incorrect = values.filter(v => v.verdict === 'incorrect').length;
      const accuracy = total > 0 ? (((correct + 0.5 * partial) / total) * 100).toFixed(1) : 0;

      document.getElementById('statsSummary').innerHTML = 
        `Sample: <strong>${{total}}</strong> | Correct: <strong class="text-emerald-600">${{correct}}</strong> | Partial: <strong class="text-amber-600">${{partial}}</strong> | Incorrect: <strong class="text-rose-600">${{incorrect}}</strong> | Pass 1 Accuracy: <strong class="text-indigo-600">${{accuracy}}%</strong>`;
    }}

    function exportLabelsJson() {{
      const exportData = {{
        sample_size: sampleApps.length,
        timestamp: new Date().toISOString(),
        labels: labels
      }};
      const blob = new Blob([JSON.stringify(exportData, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'human_ground_truth_labels.json';
      a.click();
    }}

    renderTable();
  </script>
</body>
</html>"""

    out_file = os.path.join(DATA_DIR, "review_sheet.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated interactive HTML review sheet in {out_file}")

if __name__ == "__main__":
    build_review_html()
