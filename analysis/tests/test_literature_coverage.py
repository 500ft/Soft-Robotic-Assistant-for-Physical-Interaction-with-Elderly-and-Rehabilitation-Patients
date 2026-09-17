"""The parser is the load-bearing part: if it silently drops a field, the
matrix looks fine and the evidence quietly disappears. These pin that down."""

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from build_literature_matrix import parse_block, parse_section, SECTIONS


class TestParseBlock(unittest.TestCase):
    def test_reads_standard_bullets(self):
        fields = parse_block(
            "- **Citation:** Someone, 2020. A paper.\n"
            "- **DOI/URL:** https://doi.org/10.1000/xyz\n"
            "- **Evidence grade:** B\n"
        )
        self.assertEqual(fields["citation"], "Someone, 2020. A paper.")
        self.assertEqual(fields["source"], "https://doi.org/10.1000/xyz")
        self.assertEqual(fields["evidence_grade"], "B")

    def test_reads_qualified_label(self):
        """Agents qualified labels in place; the alias must still resolve."""
        fields = parse_block("- **Hard numbers (read from the PDF):** 28 N peak.\n")
        self.assertEqual(fields["hard_numbers"], "28 N peak.")

    def test_folds_alternate_labels(self):
        fields = parse_block(
            "- **What it is:** A robot.\n- **Where it fell short:** It did not ship.\n"
        )
        self.assertEqual(fields["contribution"], "A robot.")
        self.assertEqual(fields["limitations"], "It did not ship.")

    def test_joins_continuation_lines(self):
        fields = parse_block("- **Citation:** Someone, 2020,\n  a long title.\n")
        self.assertEqual(fields["citation"], "Someone, 2020, a long title.")

    def test_ignores_unknown_labels(self):
        self.assertEqual(parse_block("- **Vibes:** good\n"), {})


class TestParseSection(unittest.TestCase):
    def test_skips_blocks_without_a_citation(self):
        """Verdict prose uses ### too; it must not become a source row."""
        rows = parse_section(_write("### Prior-art table\n\nSome prose.\n"))
        self.assertEqual(rows, [])

    def test_strips_numeric_prefix_from_handle(self):
        rows = parse_section(_write("### 3. A paper — Author, 2024\n- **Citation:** X\n"))
        self.assertEqual(rows[0]["handle"], "A paper — Author, 2024")

    def test_every_committed_section_yields_sources(self):
        for path in sorted(SECTIONS.glob("*.md")):
            with self.subTest(section=path.stem):
                self.assertGreater(len(parse_section(path)), 5)


def _write(text: str) -> Path:
    import tempfile

    path = Path(tempfile.mkdtemp()) / "S1.md"
    path.write_text(text, encoding="utf-8")
    return path


if __name__ == "__main__":
    unittest.main()
