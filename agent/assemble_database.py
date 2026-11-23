"""Assembles and verifies all 100 app research records."""

import os
import json
from models import AppResearchRecord, EvidenceItem, ApiSurface
from curated_knowledge import APP_KNOWLEDGE_BASE
from populate_part2 import part2_data
from apps_31_60 import apps_31_60
from apps_61_100 import apps_61_100

def assemble_all():
    all_apps = {}
    
    # 1-10
    for app_id, data in APP_KNOWLEDGE_BASE.items():
        data["id"] = app_id
        if "needs_human" not in data:
            data["needs_human"] = (data.get("self_serve") in ["partner_or_contact_sales", "no_public_api"])
            data["human_reason"] = "Partner/sales gated or no public API" if data["needs_human"] else None
        all_apps[app_id] = data

    # 11-30
    for app_id, data in part2_data.items():
        data["id"] = app_id
        if "needs_human" not in data:
            data["needs_human"] = (data.get("self_serve") in ["partner_or_contact_sales", "no_public_api"])
            data["human_reason"] = "Partner/sales gated or no public API" if data["needs_human"] else None
        all_apps[app_id] = data

    # 31-60
    for app_id, data in apps_31_60.items():
        data["id"] = app_id
        if "needs_human" not in data:
            data["needs_human"] = (data.get("self_serve") in ["partner_or_contact_sales", "no_public_api"])
            data["human_reason"] = "Partner/sales gated or no public API" if data["needs_human"] else None
        all_apps[app_id] = data

    # 61-100
    for app_id, data in apps_61_100.items():
        data["id"] = app_id
        if "needs_human" not in data:
            data["needs_human"] = (data.get("self_serve") in ["partner_or_contact_sales", "no_public_api"])
            data["human_reason"] = "Partner/sales gated or no public API" if data["needs_human"] else None
        all_apps[app_id] = data

    print(f"Total apps assembled: {len(all_apps)}")
    assert len(all_apps) == 100, f"Expected 100 apps, got {len(all_apps)}"

    # Validate against Pydantic schema
    validated_records = []
    for app_id in range(1, 101):
        assert app_id in all_apps, f"Missing app id {app_id}"
        raw = all_apps[app_id]
        rec = AppResearchRecord(**raw)
        validated_records.append(rec.model_dump())

    out_file = os.path.join(os.path.dirname(__file__), "..", "data", "apps_ground_truth.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(validated_records, f, indent=2)

    print(f"Successfully validated all 100 records and saved to {out_file}")
    return validated_records

if __name__ == "__main__":
    assemble_all()
