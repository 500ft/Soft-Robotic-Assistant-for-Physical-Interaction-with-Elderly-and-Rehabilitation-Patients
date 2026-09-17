#!/usr/bin/env python3
"""Check that the literature layer is internally consistent.

Fails if the committed matrix has drifted from the section files, if a source
is missing a field the design team needs, if a bibliography key is duplicated,
or if a section file is not reachable from the README.
"""

from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_literature_matrix import COLUMNS, SECTIONS, parse_section  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "literature" / "literature_matrix.csv"
BIBLIOGRAPHY = ROOT / "literature" / "refs.bib"
README = ROOT / "README.md"

# Every source must carry these; they are what a design review asks for.
REQUIRED_FIELDS = (
    "citation",
    "source",
    "evidence_grade",
    "hard_numbers",
    "design_relevance",
    "limitations",
)


def render_matrix() -> str:
    """Regenerate the matrix in memory, byte-identically to the build script."""
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for path in sorted(SECTIONS.glob("*.md")):
        for row in parse_section(path):
            writer.writerow({key: " ".join(row.get(key, "").split()) for key in COLUMNS})
    return buffer.getvalue()


def main() -> None:
    failures: list[str] = []

    # 1. The matrix is derived, not hand-edited. It must match its sources.
    # read_text() normalizes the csv module's \r\n; compare line-wise.
    committed = MATRIX.read_text(encoding="utf-8")
    if committed.splitlines() != render_matrix().splitlines():
        failures.append(
            "literature_matrix.csv is stale; rerun analysis/build_literature_matrix.py"
        )

    rows = list(csv.DictReader(io.StringIO(committed)))
    print(f"Annotated sources: {len(rows)}")

    # 2. No source may be missing a field the design team needs.
    for row in rows:
        blank = [field for field in REQUIRED_FIELDS if not row[field].strip()]
        if blank:
            failures.append(f"{row['section']} / {row['handle'][:60]}: missing {blank}")

    # 3. Every source must point somewhere resolvable.
    unresolvable = [
        row["handle"][:60]
        for row in rows
        if not re.search(r"(https?://|10\.\d{4,})", row["source"])
    ]
    if unresolvable:
        failures.append(f"sources without a DOI or URL: {unresolvable}")

    # 4. Bibliography keys must be unique across the merged file.
    keys = re.findall(r"(?m)^@[A-Za-z]+\{([^,]+),", BIBLIOGRAPHY.read_text(encoding="utf-8"))
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    print(f"Bibliography entries: {len(keys)}")
    if duplicates:
        failures.append(f"duplicate bibliography keys: {duplicates}")

    # 5. Every section file must be reachable from the README.
    readme = README.read_text(encoding="utf-8")
    orphans = [
        path.name for path in sorted(SECTIONS.glob("*.md")) if path.name not in readme
    ]
    if orphans:
        failures.append(f"section files not linked from README: {orphans}")

    if failures:
        print("\nFAILED:")
        for failure in failures:
            print(f"  - {failure}")
        raise SystemExit(1)

    print("Literature layer consistent.")


if __name__ == "__main__":
    main()
