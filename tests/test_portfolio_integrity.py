import glob
import json
import os
import re
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

SECRET_PATTERNS = [
    ("OpenAI/OpenRouter-style key", re.compile(r"\bsk-(?:proj-|or-v1-)?[A-Za-z0-9_-]{24,}\b")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("Slack bot/user token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{15,}\b")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]


class PortfolioIntegrityTests(unittest.TestCase):
    def test_all_json_files_are_valid(self):
        json_files = glob.glob(os.path.join(REPO_ROOT, "**", "*.json"), recursive=True)
        self.assertGreater(len(json_files), 0, "Expected JSON workflow exports in repository")

        for path in json_files:
            rel = os.path.relpath(path, REPO_ROOT)
            with self.subTest(file=rel):
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                self.assertIsInstance(data, (dict, list))
                if isinstance(data, dict) and "nodes" in data:
                    self.assertIsInstance(data["nodes"], list)
                    self.assertGreater(len(data["nodes"]), 0)
                    self.assertIn("connections", data)

    def test_all_markdown_relative_links_resolve(self):
        md_files = glob.glob(os.path.join(REPO_ROOT, "**", "*.md"), recursive=True)
        self.assertGreater(len(md_files), 0)

        for md_path in md_files:
            rel_md = os.path.relpath(md_path, REPO_ROOT)
            with open(md_path, encoding="utf-8") as f:
                content = f.read()

            for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
                target = match.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(md_path), target))
                with self.subTest(markdown=rel_md, link=target):
                    self.assertTrue(
                        os.path.exists(resolved),
                        f"Broken relative link '{target}' in {rel_md}",
                    )

    def test_no_unredacted_secrets_in_docs_or_exports(self):
        extensions = ("*.md", "*.json", "*.py", "*.ps1")
        files = []
        for ext in extensions:
            files.extend(glob.glob(os.path.join(REPO_ROOT, "**", ext), recursive=True))

        for path in files:
            rel = os.path.relpath(path, REPO_ROOT)
            with open(path, encoding="utf-8", errors="ignore") as f:
                content = f.read()
            for label, pattern in SECRET_PATTERNS:
                with self.subTest(file=rel, check=label):
                    self.assertIsNone(
                        pattern.search(content),
                        f"Potential {label} found in {rel}",
                    )


if __name__ == "__main__":
    unittest.main()
