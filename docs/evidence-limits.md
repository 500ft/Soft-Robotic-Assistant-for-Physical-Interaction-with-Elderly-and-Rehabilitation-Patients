# Evidence limits

Read before quoting any number from this repository.

## Nothing here is measured

Every value is transcribed from a published source. No hardware exists, no test has been
run. Each source in [`literature/sections/`](../literature/sections/) carries an evidence
grade, a note naming the URL actually fetched to verify it, and a limitations field.

Grades: **A** hardware-validated with human subjects or a standardized test · **B**
hardware-validated, no humans · **C** simulation or concept · **D** review or position ·
**I** industry or non-peer-reviewed instrumentation source.

## The standards gap

Verified verbatim from three scope statements:

- IEC 80601-2-78 hands personal care robots to ISO 13482.
- ISO 13482 publishes no contact limits.
- ISO/TS 15066 states it does not apply to non-industrial robots.

The limits used in [docs/requirements.md](requirements.md) are therefore **imported under
a documented ISO 14971 argument**. That is an argument, not a compliance claim, and the
final report must say so.

ISO/TS 15066 Tables A.1–A.4 were read verbatim (fetched as binary, extracted with
`pdftotext -layout`), and the derived velocity table was validated by reproducing ISO's
own Table A.4 energies from Formula (A.1) across seven body regions.

**ISO's own admissions, verbatim from the standard:** the pressure limits come from a
single Mainz study of 100 subjects at the 75th percentile, and the **force limits were
never measured** — they are a 188-source literature estimate the standard itself flags as
provisional and says will be replaced.

**The ISO chest numbers are too high.** Behrens (n=112), Park (n=90) and Han (n=40)
independently land 2.4–3× below ISO on every region a torso contacts. Sternum: ISO
120 N/cm², Behrens 50, Han 39.4 at onset. Design against Behrens.

## The population mismatch

The pain-threshold data underlying the standards comes from healthy volunteers — one
underlying cohort is 40 men in their twenties. The cadaver injury data comes
disproportionately from *elderly* donors with wide confidence intervals. Two halves of the
safety case, two different populations, **neither one the intended user**.

El Tumi confirms pressure-pain threshold is significantly lower over age 62 (p=0.018);
the effect magnitude could not be verified, so the requirement says "de-rating required,
magnitude TBD" rather than inventing a factor.

Because reduced protective sensation travels with reduced tissue tolerance, **pain onset
is not a valid proxy for injury onset in this population**. This is a genuine open
question and a place the project can contribute.

## Citation traps caught during verification

Recorded rather than quietly fixed, because each one would have survived into a report.

| What was wrong | What is correct |
|---|---|
| A fetch summary attributed the "soft arms are creepy and fragile" finding to **"Tejada et al. 2022"** | No such paper exists. Traced through the survey's raw HTML bibliography to **Kim, MacDonald, McDaid, Kawamura, Kim, Bean, Fraser & Broadbent, RO-MAN 2016**, confirmed via Crossref. |
| A **"43 N·m peak deltoid torque"** figure circulating in search results | Not present in the paper it is attributed to (fetched in full) and not traceable to any source. Do not use it. |
| Godspeed author order printed as Bartneck, Croft, Kulić | Correct order is **Bartneck, Kulić, Croft, Zoghbi**. |
| Trust-in-automation scale cited as the 1998 HFES proceedings paper | Correct source is **Jian et al. 2000**, *IJCE* 4(1):53–71. |
| A search summary said Abidi & Cianchetti critique HIC and ISO/TS 15066 | Fetching the paper showed they do not. |
| Proximity-sensing survey dated 2021 | Crossref gives **T-RO 38(3):1599–1620, 2022**. |
| Wong et al. treated as a preprint | Published, **T-ASE 21:3205–3215, 2024**. |
| Paine & Sentis prismatic SEA venue guessed | **ROBIO 2012, pp. 1759–1766**, confirmed via Crossref. |

## Citation traps caught in the second pass (2026-09-24)

An externally supplied prior-art list of 52 items was verified before ingest. **None were
fabricated**, but 14 carried metadata errors. The ones that would have survived into a
report:

| What was wrong | What is correct |
|---|---|
| "Jain et al. 2013" for the PR2 whole-arm contact study | **Grice et al. 2013** — Advait Jain is third author. Especially dangerous because Jain has a *separate real* 2013 whole-arm tactile paper in IJRR, so the wrong citation looks right. |
| RI-MAN "demonstrated lifting and holding a human-sized body" | It lifted a **doll**. Real title: *Development and Evaluation of a Human-interactive Robot Platform "RI-MAN"*, J. Robotics Soc. Japan 25(4):554–565. |
| "EmArm: Whole-Arm Tactile Sensing and Adaptive Robotic Manipulation" | **No paper has that title.** Real: Tang et al., *Embodied sensorimotor integration for whole-arm tactile sensing and adaptive robotic manipulation*, Nature Sensors 1(8):681–690. |
| Baloo cited as a published paper | **arXiv preprint 2409.08420v2.** Submitted to T-Mech; no journal version exists. |
| "223 ms end-to-end safety decision latency" | The 223 ms is **edge-LLM inference time on a laptop**; the total control loop is ≤240 ms. No human subjects — validated on an instrumented prosthetic leg. |
| CN110812124A assignee per Google Patents | **Shanghai University.** Google Patents is wrong. Filed 2019, not 2020. |
| CN112263435B assignee per Google Patents | **Henan Polytechnic University**, not "Henan University of Technology" — a different institution. B-grant published 2023, not 2020. |
| US9956130B2 modes "assistant/active/resistive" | **Passive**/active/resistive; resistance comes from a variable damper. |
| ISO/TR 23482-1 and -2 titles | Both are parts of an *"Robotics — Application of ISO 13482"* series, not the standalone titles quoted. |
| "Assist-as-Needed Control of a Soft Rehabilitation Robot" described as general-purpose | It is a **finger** robot (Besharati et al., Eur. J. Control 86:101395). |
| Wang & Xu 2021 as six PAMs | Six PAMs **plus a central linear electric motor**; EMG is assessment, not control. |
| Yap et al. 2017 implied patient testing | **5 healthy participants**, despite "Hand Impaired Patients" in the title. |

### Robertson 2017 reconciled

Two sources quoted this paper with different figures — 112 N and 18 N·m — and both are
correct because they describe different devices. From Table 2 at 200 kPa:

| Device | Output |
|---|---|
| Single soft pneumatic actuator | 26 N |
| SPA 4Pack (four in parallel) | **112 N** (model predicted 122 N; measured 8.2% low) |
| Multi-DoF platform, four packs | **468 N cumulative, 18.00 N·m** blocked moment, ±5° travel |

Quote the device, not just the number. A 2019 correction exists but changes an equation
sign only, no values.

## Do not quote until someone opens the PDF

| Figure | Problem |
|---|---|
| Kengoro 1.7 m / 116 muscles / 174 DOF | Secondary sources only; only the 56 kgf mass is confirmed at source. |
| RIBA's 61 kg lift | Appears only in news coverage. |
| COMAN 0.95 m / 31 kg | Could not be confirmed from any page fetched. |
| ARMin III torque table | No retrievable mirror; someone must download it manually. |
| Zeng & Bone 50 N pain threshold | Search snippet of a paywalled abstract. |
| Bruder 2023 | NASA NTRS mirror returned 503 three times; no numbers extracted. |
| Box and Block MCID | No primary source verified, so no number is reported anywhere here. |
| Harvard exosuit figures | Metadata Crossref-verified; numbers from abstract and news text (science.org returned 403). |
| TIAGo arm payload | PAL's own two documents disagree — 3 kg datasheet vs 2 kg handbook. Reported unresolved. |

## Unverified and load-bearing

1. **Whether ISO 10218-2:2025 kept Table A.2 unchanged.** Still open, and now the top item.
2. **Whether ISO/FDIS 13482 edition 2 publishes contact limits.** The revision reached FDIS
   stage 50.20 with the ballot initiated 2026-09-15 and could publish during this project.
   If edition 2 carries limits, the import argument below is replaced by direct compliance.
   Highest-value open question in this repository.

### Resolved 2026-09-24

**ISO 13482's own admission is now confirmed verbatim** from the standard's abstract:

> "no exhaustive and internationally recognized data (e.g. pain or injury limits) exist at
> the time of publication"

This was previously the repository's most load-bearing unverified claim — the sentence the
entire ISO 14971 import argument depends on. It is now primary-sourced.

Also confirmed verbatim, IEC 80601-2-78's exclusion list reads "personal care ROBOTS (use
ISO 13482)", closing the standards circle from the other side. And ISO/FDIS 13482 edition 2
**keeps the medical exclusion**, so the gap survives the revision.

## Modelled, not measured

- **Zinn's widely cited order-of-magnitude impact reduction** for distributed macro-mini
  actuation is a model result. Graded C. Do not present it as data.

## Descriptive, not a limit

- The **20–40 kPa interface pressure** figure quoted for soft wearable devices describes
  what those devices do. It is **not** a validated safety threshold for aged skin.

## Standards access

NYU's mechanical engineering standards guide lists only **Knovel and ASTM Compass** — no
ISO or IEC access is evidenced, so do not assume the library route works. Full set at list
price is **CHF 1,303**. Free ISO Online Browsing Platform previews expose the scope clauses,
which covers most citation needs. If buying exactly one document, buy **ISO/TR 23482-2**
(CHF 204) before ISO 13482 itself.

## Coverage limits

Several agents exhausted a shared web-search budget near the end of their runs and
finished verification through Crossref, OpenAlex and PMC APIs directly. Coverage is good
but not exhaustive. A1's electroactive-actuator census and E2's instrument set are the most
complete. B2's magnetic soft-proprioception modality is the least covered — every fetch was
blocked, and the source was excluded rather than reported unverified.

Four C2 entries carry explicit `UNVERIFIED-CONTENT` flags: bibliographic record confirmed,
full text unread. One entry (Jacobs & Reiser) has full text read but an unverifiable venue.

In the second pass, four G2 references were paywalled and **not read** — Polygerinos 2015,
Liu 2020, Besharati 2025, Tang 2026 — and every number attached to them is marked
UNVERIFIED rather than repeated. The G3 agent lost web search partway and navigated by
direct URL and ISO's TC 299 committee catalogue instead; it lists eight items it could not
determine. Patent grades use a separate scale: **P-VERIFIED** (number resolves and matches),
**P-PARTIAL** (resolves, metadata differs), **P-NOTFOUND**, **P-WRONG**.

## Two INFERRED requirement cells

Shoulder (**≈10 N·m**) and elbow (**≈3 N·m**) gravity-compensation torque are arithmetic
from assumed centre-of-mass moment arms (0.30 m and 0.16 m) that **no source supplies**.
Measure them before freezing the spec.
