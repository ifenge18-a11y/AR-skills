#!/usr/bin/env python3
"""Contract tests that prevent AR/research-wiki documentation drift."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SKILL_ROOT = ROOT / "accounting-research-assistant"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class AccountingResearchAssistantContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = read(SKILL_ROOT / "SKILL.md")
        cls.root_readme = read(ROOT / "README.md")
        cls.skill_readme = read(SKILL_ROOT / "README.md")
        cls.prompt = read(SKILL_ROOT / "agents" / "openai.yaml")
        cls.zotero = read(SKILL_ROOT / "references" / "zotero-literature-workflow.md")
        cls.literature = read(SKILL_ROOT / "references" / "literature-map.md")
        cls.research_base = read(SKILL_ROOT / "references" / "research-base-workflow.md")
        cls.agent_roles = read(SKILL_ROOT / "references" / "agent-roles.md")
        cls.all_current = "\n".join(
            [cls.skill, cls.root_readme, cls.skill_readme, cls.prompt, cls.zotero, cls.literature, cls.research_base, cls.agent_roles]
        )

    def test_versions_are_1_2_0(self) -> None:
        self.assertIn('version: "1.2.0"', self.skill)
        self.assertIn("Version: `v1.2.0`", self.root_readme)
        self.assertIn("Current version: `v1.2.0`", self.skill_readme)

    def test_default_prompt_is_single_agent(self) -> None:
        self.assertIn("ordinary single-agent workflow", self.prompt)
        self.assertNotIn("in Boss-led", self.prompt)
        self.assertIn("only when the user explicitly asks", self.skill)

    def test_canonical_handoff_is_complete(self) -> None:
        for field in (
            "project",
            "zotero_item_key",
            "boss_category",
            "deep_read_priority",
            "boss_screening_reason",
            "pdf_status",
            "project_use",
            "need_fulltext_read",
            "read_level",
            "deep_read_completed",
            "source_route",
            "verification_status",
        ):
            self.assertIn(f"`{field}`", self.zotero)

    def test_priority_and_role_enums_do_not_collide(self) -> None:
        self.assertIn("`deep_read_priority`: only `high`, `medium`, `low`, or `exclude`", self.literature)
        self.assertIn("`deep_read_role`", self.literature)
        for obsolete in ("theory core", "empirical core", "both theory and empirical core", "background only", "no deep read"):
            self.assertNotIn(obsolete, self.all_current.lower())

    def test_paths_are_configured_not_hard_coded(self) -> None:
        self.assertNotIn("Knowledge Base/sources", self.all_current)
        self.assertIn(".research-wiki/config.json", self.skill)
        self.assertIn("<knowledge_base_path>/sources/*.md", self.zotero)

    def test_provenance_verification_and_read_depth_are_separate(self) -> None:
        self.assertIn("source_route: cnki", self.literature)
        self.assertIn("verification_status: verified", self.literature)
        self.assertIn("partially_verified", self.literature)
        self.assertNotRegex(self.all_current, r"`CNKI record`")
        self.assertIn("independent provenance, verification, and evidence-depth dimensions", self.zotero)

    def test_zotero_sqlite_exception_is_removed(self) -> None:
        self.assertIn("Never edit Zotero SQLite files", self.zotero)
        for obsolete in ("authorizes direct database updates", "direct local Zotero database updates", "profile-directory placeholder"):
            self.assertNotIn(obsolete, self.all_current)
        self.assertIn("exact manual actions", self.zotero)

    def test_research_base_terminal_fields_and_acceptance_matrix(self) -> None:
        for field in ("promoted_at", "superseded_by", "decision_reason"):
            self.assertIn(field, self.research_base)
        acceptance = self.research_base.split("## Maintainer Acceptance Matrix", 1)[1]
        matrix_rows = re.findall(r"^\| (?!Scenario|---)([^|]+) \|", acceptance, flags=re.MULTILINE)
        self.assertEqual(len(matrix_rows), 7)
        self.assertIn("`valid`, `errors`, and `warnings`", self.research_base)


if __name__ == "__main__":
    unittest.main()
