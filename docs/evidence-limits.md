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

Two open items that the safety argument rests on:

1. **Whether ISO 10218-2:2025 kept Table A.2 unchanged.** Top open item.
2. **ISO 13482's "no internationally recognised impact data" clause.** Could not be
   fetched verbatim, and it is the sentence the entire import argument depends on.

## Modelled, not measured

- **Zinn's widely cited order-of-magnitude impact reduction** for distributed macro-mini
  actuation is a model result. Graded C. Do not present it as data.

## Descriptive, not a limit

- The **20–40 kPa interface pressure** figure quoted for soft wearable devices describes
  what those devices do. It is **not** a validated safety threshold for aged skin.

## Coverage limits

Several agents exhausted a shared web-search budget near the end of their runs and
finished verification through Crossref, OpenAlex and PMC APIs directly. Coverage is good
but not exhaustive. A1's electroactive-actuator census and E2's instrument set are the most
complete. B2's magnetic soft-proprioception modality is the least covered — every fetch was
blocked, and the source was excluded rather than reported unverified.

Four C2 entries carry explicit `UNVERIFIED-CONTENT` flags: bibliographic record confirmed,
full text unread. One entry (Jacobs & Reiser) has full text read but an unverifiable venue.

## Two INFERRED requirement cells

Shoulder (**≈10 N·m**) and elbow (**≈3 N·m**) gravity-compensation torque are arithmetic
from assumed centre-of-mass moment arms (0.30 m and 0.16 m) that **no source supplies**.
Measure them before freezing the spec.
