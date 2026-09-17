#!/usr/bin/env python3
"""Build literature/literature_matrix.csv from the annotated section files.

Each `###` block in literature/sections/*.md that carries a `- **Citation:**`
bullet becomes one row. Blocks without a citation bullet are synthesis prose
(verdicts, prior-art tables) and are skipped.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "literature" / "sections"
MATRIX = ROOT / "literature" / "literature_matrix.csv"

# Agents used slightly different labels for the same field; fold them here.
FIELD_ALIASES = {
    "citation": "citation",
    "doi/url": "source",
    "open access": "open_access",
    "what it shows": "contribution",
    "what it is": "contribution",
    "hard numbers": "hard_numbers",
    "design relevance": "design_relevance",
    "evidence grade": "evidence_grade",
    "limitations": "limitations",
    "where it fell short": "limitations",
}

COLUMNS = [
    "section",
    "handle",
    "citation",
    "source",
    "open_access",
    "contribution",
    "hard_numbers",
    "design_relevance",
    "evidence_grade",
    "limitations",
]

def resolve(label: str) -> str | None:
    """Map a bullet label onto a column.

    Agents qualified some labels in place -- "Hard numbers (extracted from the
    PDF)" -- so match on the leading alias rather than the whole string.
    """
    for alias, column in FIELD_ALIASES.items():
        if label.startswith(alias):
            return column
    return None


HEADING = re.compile(r"(?m)^###\s+(.*)$")
BULLET = re.compile(r"^-\s+\*\*([^:*]+):?\*\*:?\s*(.*)$")


def parse_block(text: str) -> dict[str, str]:
    """Pull `- **Key:** value` bullets out of one heading block."""
    fields: dict[str, str] = {}
    current: str | None = None
    for line in text.splitlines():
        match = BULLET.match(line)
        if match:
            label = match.group(1).strip().rstrip(":").lower()
            current = resolve(label)
            if current:
                fields[current] = match.group(2).strip()
            continue
        # Continuation of the previous bullet, including nested sub-bullets.
        if current and line.strip() and not line.startswith("#"):
            fields[current] = (fields[current] + " " + line.strip()).strip()
    return fields


def parse_section(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    headings = list(HEADING.finditer(text))
    rows = []
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        fields = parse_block(text[heading.end():end])
        if "citation" not in fields:
            continue  # synthesis prose, not a source
        handle = re.sub(r"^\d+\.\s*", "", heading.group(1).strip())
        rows.append({"section": path.stem, "handle": handle, **fields})
    return rows


def main() -> None:
    rows: list[dict[str, str]] = []
    for path in sorted(SECTIONS.glob("*.md")):
        found = parse_section(path)
        print(f"{path.stem}: {len(found)} sources")
        rows.extend(found)

    with MATRIX.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: " ".join(row.get(key, "").split()) for key in COLUMNS})

    print(f"Wrote {len(rows)} rows to {MATRIX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
