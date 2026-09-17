# Contributing

This repository keeps annotated sources, the derived matrix, the bibliography, and the
requirements connected. A contribution should update every affected layer.

No third-party dependencies. Python 3.11 standard library only.

## Adding a source

1. Add a `###` block to the right file in `literature/sections/`, following the existing
   format. Required bullets: **Citation**, **DOI/URL**, **Open access**, **What it shows**,
   **Hard numbers**, **Design relevance**, **Evidence grade**, **Limitations**.
2. Add its BibTeX entry to `literature/refs.bib` with a unique key of the form
   `firstauthorlastnameYYYYkeyword`, and to the matching `literature/_provenance/<section>.bib`.
3. Regenerate the matrix and run the checks:

```bash
python analysis/build_literature_matrix.py
python -m unittest discover -s analysis/tests -v
python analysis/check_literature_coverage.py
```

`literature_matrix.csv` is derived. Never hand-edit it — the coverage check regenerates it
and fails if the committed copy has drifted.

## Rules for source entries

**Verify before you cite.** Fetch a record that actually shows the paper — Crossref,
OpenAlex, Semantic Scholar, PMC, arXiv, or the publisher page — and name that route in the
**DOI/URL** bullet. An unverified plausible citation is worse than no citation.

**Do not invent numbers.** If a paper reports none, write "none reported". If a paper is
paywalled and you could not read it, say so in the **Hard numbers** field rather than
carrying a figure from a search snippet. Figures that could not be confirmed belong in the
do-not-quote table in `docs/evidence-limits.md`.

**Do not infer what a source does not report.** Materials, dimensions, test conditions,
and effect sizes are either in the source or marked absent.

**Record corrections, do not silently fix them.** If verification contradicts a widely
repeated figure or attribution, add a row to the citation-traps table in
`docs/evidence-limits.md`. That table is part of the evidence, not an appendix.

## Changing a requirement

Every row in `docs/requirements.md` must trace to a source in the matrix, or be marked
**INFERRED** with the arithmetic shown. A requirement with neither does not belong in the
table. When a source is superseded, update the requirement and the section entry together.

## Evidence grades

**A** hardware-validated with human subjects or a standardized test · **B**
hardware-validated, no humans · **C** simulation or concept · **D** review or position ·
**I** industry or non-peer-reviewed instrumentation source.

Grade honestly. A review by the lab that originated the technology is a D even when its
underlying numbers are strong; say that in the entry.
