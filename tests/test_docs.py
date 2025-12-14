from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_readme_mentions_docs():
    readme = (ROOT / "README.md").read_text()
    assert "AI Agency CMS" in readme
    assert "docs/ai-agency-cms.md" in readme


def test_cms_doc_has_key_sections():
    content = (ROOT / "docs" / "ai-agency-cms.md").read_text()
    for phrase in [
        "Objectives",
        "Customer Journey & CMS Modules",
        "Data Model Sketch",
        "Workflow Automation",
        "Dashboards & Reporting",
        "Security & Governance",
        "Implementation Roadmap",
        "Testing & QA Strategy",
    ]:
        assert phrase in content, f"Missing section: {phrase}"


def test_roadmap_has_milestones():
    content = (ROOT / "docs" / "ai-agency-cms.md").read_text()
    assert "Phase 1" in content and "Phase 2" in content, "Roadmap should include phased milestones"
    assert "production hardening" in content.lower()
