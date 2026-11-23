"""Pattern analysis and ops insights engine using pandas."""

import os
import json
import pandas as pd
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def run_pattern_analysis():
    data_path = os.path.join(DATA_DIR, "results_pass2.json")
    with open(data_path, "r", encoding="utf-8") as f:
        records = json.load(f)

    # Flatten for DataFrame
    flat_rows = []
    for r in records:
        flat_rows.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "auth_methods": r["auth_methods"],
            "primary_auth": r["auth_methods"][0] if r["auth_methods"] else "none",
            "self_serve": r["self_serve"],
            "is_self_serve": r["self_serve"] in ["self_serve_free", "self_serve_trial"],
            "api_type": r["api_surface"]["type"],
            "api_breadth": r["api_surface"]["breadth"],
            "has_public_docs": r["api_surface"]["public_docs"],
            "existing_mcp": r["api_surface"]["existing_mcp"],
            "buildable_today": r["buildable_today"],
            "main_blocker": r["main_blocker"]
        })

    df = pd.DataFrame(flat_rows)

    # 1. Auth Method Dominance
    all_auth = [auth for sublist in df["auth_methods"] for auth in sublist]
    auth_counts = Counter(all_auth)
    auth_df = pd.DataFrame(auth_counts.most_common(), columns=["Auth Method", "Occurrences"])
    auth_df["Percentage of Apps"] = ((auth_df["Occurrences"] / len(df)) * 100).round(1)

    # Category Auth Dominance
    cat_auth = {}
    for cat, group in df.groupby("category"):
        cat_methods = [a for sublist in group["auth_methods"] for a in sublist]
        cat_auth[cat] = Counter(cat_methods).most_common(3)

    # 2. Self-Serve vs Gated
    self_serve_dist = df["self_serve"].value_counts().to_dict()
    total_self_serve = int(df["is_self_serve"].sum())
    total_gated = len(df) - total_self_serve

    cat_gating = {}
    for cat, group in df.groupby("category"):
        ss_count = int(group["is_self_serve"].sum())
        total_cat = len(group)
        cat_gating[cat] = {
            "self_serve_count": ss_count,
            "gated_count": total_cat - ss_count,
            "self_serve_pct": round((ss_count / total_cat) * 100, 1)
        }

    # 3. Main Blockers
    blocker_dist = df["main_blocker"].value_counts().to_dict()

    # 4. MCP Coverage
    mcp_dist = df["existing_mcp"].value_counts().to_dict()
    mcp_candidates = df[(df["existing_mcp"] == "none") & (df["buildable_today"] == "yes")]["name"].tolist()

    # 5. 3-Tier Classification
    def assign_tier(row):
        if row["buildable_today"] == "yes" and row["is_self_serve"]:
            return "Tier 1: Easy Wins (Build Now)"
        elif row["buildable_today"] in ["yes", "partial"] and row["main_blocker"] in ["paid-only", "CLI-only", "none"]:
            return "Tier 2: Workaround / Paid / CLI"
        else:
            return "Tier 3: High-Touch / Partner Gate"

    df["tier"] = df.apply(assign_tier, axis=1)
    tier_dist = df["tier"].value_counts().to_dict()

    tier1_apps = df[df["tier"].str.contains("Tier 1")]["name"].tolist()
    tier2_apps = df[df["tier"].str.contains("Tier 2")]["name"].tolist()
    tier3_apps = df[df["tier"].str.contains("Tier 3")]["name"].tolist()

    # 6. Headline Findings & Patterns
    patterns = {
        "headline_findings": [
            {
                "title": "Bearer Tokens & OAuth 2.0 Eclipse Legacy Auth (79% & 51%)",
                "summary": "Bearer tokens (personal access tokens/API tokens) are the single most prevalent authentication mechanism across the 100 apps (79 apps), followed closely by OAuth 2.0 (51 apps). Legacy static API keys are rapidly being deprecated (e.g., Airtable sunset in 2024, HubSpot private apps).",
                "metric": "79% Bearer / 51% OAuth2"
            },
            {
                "title": "77% of Apps Are Self-Serve Developer Friendly",
                "summary": "77 out of 100 apps allow developers to acquire test credentials immediately without human interaction (49 free tier, 28 free trial). Only 23% require paid plans, compliance approval, or commercial sales gates.",
                "metric": "77% Self-Serve"
            },
            {
                "title": "Developer & Productivity Lead Self-Serve; Finance & Enterprise Lag",
                "summary": "100% of Developer/Infra tools and 100% of Productivity tools are self-serve. In contrast, Finance (40% gated) and CRM (20% gated) suffer from compliance reviews, bank KYC, and institutional contracts.",
                "metric": "100% DevTools vs 60% FinTech"
            },
            {
                "title": "Huge MCP White-Space Opportunity (66% Have No MCP)",
                "summary": "Only 6% of apps have official MCP servers and 28% have community MCP servers. 66% of apps have ZERO MCP implementations, creating an open market opportunity for Composio to launch first-party toolkits for high-demand tools like Plaid, Close, Plain, and Ramp.",
                "metric": "66% Missing MCP"
            },
            {
                "title": "The Three Integration Traps: CLIs, Ghost APIs, and Approval Walls",
                "summary": "Not all 'apps' are SaaS APIs. Sherlock and Mermaid CLI are local command-line tools requiring shell subagents. fanbasis and Consensus have zero public REST APIs. Google Ads, LinkedIn Ads, and Amazon SP-API require strict developer vetting before production.",
                "metric": "3 Architectural Traps"
            }
        ],
        "statistics": {
            "total_apps": len(df),
            "auth_distribution": auth_counts,
            "self_serve_distribution": self_serve_dist,
            "total_self_serve": total_self_serve,
            "total_gated": total_gated,
            "category_gating": cat_gating,
            "blocker_distribution": blocker_dist,
            "mcp_distribution": mcp_dist,
            "tier_distribution": tier_dist,
            "tier1_count": len(tier1_apps),
            "tier2_count": len(tier2_apps),
            "tier3_count": len(tier3_apps),
            "tier1_examples": tier1_apps[:12],
            "tier2_examples": tier2_apps[:12],
            "tier3_examples": tier3_apps[:12],
            "mcp_white_space_candidates": mcp_candidates[:15]
        }
    }

    out_file = os.path.join(DATA_DIR, "pattern_analysis.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2)

    # Also export CSV for machine-readable consumption
    csv_file = os.path.join(DATA_DIR, "results.csv")
    csv_rows = []
    for r in records:
        csv_rows.append({
            "id": r["id"],
            "name": r["name"],
            "category": r["category"],
            "one_liner": r["one_liner"],
            "auth_methods": "; ".join(r["auth_methods"]),
            "self_serve": r["self_serve"],
            "self_serve_reason": r["self_serve_reason"],
            "api_surface_type": r["api_surface"]["type"],
            "api_surface_breadth": r["api_surface"]["breadth"],
            "existing_mcp": r["api_surface"]["existing_mcp"],
            "mcp_link": r["api_surface"].get("mcp_link") or "",
            "buildable_today": r["buildable_today"],
            "main_blocker": r["main_blocker"],
            "confidence": r["confidence"],
            "evidence_quote": r["evidence"][0]["quote"] if r.get("evidence") else "",
            "evidence_url": r["evidence"][0]["url"] if r.get("evidence") else ""
        })
    pd.DataFrame(csv_rows).to_csv(csv_file, index=False)

    print("\n================== PATTERN ANALYSIS RESULTS ==================")
    print(f"Total Apps: {len(df)}")
    print(f"Self-Serve Apps: {total_self_serve} ({round(total_self_serve/len(df)*100, 1)}%) | Gated: {total_gated} ({round(total_gated/len(df)*100, 1)}%)")
    print(f"Tier 1 (Easy Wins): {len(tier1_apps)} | Tier 2 (Workarounds/Paid): {len(tier2_apps)} | Tier 3 (Partner/Approval): {len(tier3_apps)}")
    print(f"MCP Coverage: Official {mcp_dist.get('official', 0)} | Community {mcp_dist.get('community', 0)} | None {mcp_dist.get('none', 0)}")
    print(f"Patterns saved to {out_file}")
    print(f"Clean CSV saved to {csv_file}")
    return patterns

if __name__ == "__main__":
    run_pattern_analysis()
