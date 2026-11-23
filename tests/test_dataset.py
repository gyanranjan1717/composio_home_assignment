"""Automated test suite verifying the 100-app dataset and research pipeline."""

import os
import json
import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_dataset(filename):
    path = os.path.join(DATA_DIR, filename)
    assert os.path.exists(path), f"File {path} does not exist"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_seed_apps_count_and_numbering():
    apps = load_dataset("apps.json")
    assert len(apps) == 100, f"Expected 100 seed apps, found {len(apps)}"
    ids = [a["id"] for a in apps]
    assert ids == list(range(1, 101)), "App IDs must be strictly numbered 1 to 100"


def test_results_schema_and_completeness():
    results = load_dataset("results.json")
    assert len(results) == 100, f"Expected 100 results, found {len(results)}"

    valid_auth = {"OAuth2", "API key", "Basic", "Bearer/token", "JWT", "other", "none"}
    valid_self_serve = {
        "self_serve_free", "self_serve_trial", "paid_plan_required",
        "admin_approval", "partner_or_contact_sales", "no_public_api", "unclear"
    }
    valid_verdicts = {"yes", "partial", "no"}

    for r in results:
        assert "id" in r and 1 <= r["id"] <= 100
        assert "name" in r and len(r["name"]) > 0
        assert "category" in r and len(r["category"]) > 0
        assert "one_liner" in r and len(r["one_liner"]) > 5
        assert isinstance(r["auth_methods"], list) and len(r["auth_methods"]) > 0
        assert all(a in valid_auth for a in r["auth_methods"]), f"Invalid auth in app {r['name']}: {r['auth_methods']}"
        assert r["self_serve"] in valid_self_serve, f"Invalid self_serve in app {r['name']}: {r['self_serve']}"
        assert r["buildable_today"] in valid_verdicts, f"Invalid verdict in app {r['name']}: {r['buildable_today']}"
        assert "api_surface" in r and isinstance(r["api_surface"], dict)
        assert r["api_surface"]["existing_mcp"] in {"none", "official", "community"}
        assert "evidence" in r and isinstance(r["evidence"], list)
        assert len(r["evidence"]) > 0, f"App {r['name']} must have at least one evidence item"
        for ev in r["evidence"]:
            assert "claim" in ev and len(ev["claim"]) > 5
            assert "url" in ev and ev["url"].startswith("http")
            assert "quote" in ev and len(ev["quote"]) > 5


def test_verification_metrics_consistency():
    metrics = load_dataset("accuracy_metrics.json")
    assert "sample_30_in_sample" in metrics
    assert "holdout_20_unseen" in metrics
    assert metrics["sample_30_in_sample"]["pass1"]["strict_accuracy"] == 80.0
    assert metrics["sample_30_in_sample"]["pass2"]["strict_accuracy"] == 93.3
    assert metrics["sample_30_in_sample"]["strict_delta"] == 13.3
    assert metrics["holdout_20_unseen"]["pass2"]["strict_accuracy"] == 85.0
    assert metrics["holdout_20_unseen"]["strict_delta"] == 10.0


def test_human_review_queue():
    queue = load_dataset("human_review_queue.json")
    assert len(queue) >= 10, f"Expected at least 10 flagged items, got {len(queue)}"
    flagged_ids = [q["id"] for q in queue]
    # DealCloud, fanbasis, Paygent, iPayX, NotebookLM must be flagged
    for must_have in [10, 50, 84, 85, 91]:
        assert must_have in flagged_ids, f"App id {must_have} must be present in human review queue"
