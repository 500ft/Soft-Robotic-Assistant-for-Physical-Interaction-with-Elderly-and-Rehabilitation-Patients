# Next Steps

Ordered by dependency. Each phase unblocks the next; items within a phase can run in
parallel. Nothing here requires hardware until Phase 2.

## Phase 0 — Desk work, this week

- [ ] **Design around the one patent that blocks.** GB2622575B (Bioliberty, priority
  2022-09-11) claims estimating a soft actuator's volume, shape, displacement and delivered
  force **from chamber pressure alone**, scale-agnostically. If the proprioception design is
  "pressure in, force out," add an independent measurement channel or state plainly that the
  method is prior art. See [docs/prior-art.md](docs/prior-art.md#the-patent-landscape-says-the-same-thing).
- [ ] **Write the ISO 14971 risk assessment first.** ISO/TR 23482-1 works on the
  principle that the manufacturer derives tests from their own risk assessment, so no
  test method can be specified until it exists. Everything downstream is blocked on this.
- [ ] **Check whether NYU already owns a CoboSafe PFMD or Hybrid III components.** A full
  CoboSafe kit is a four-to-five-figure EUR purchase; borrowing one reshapes the whole
  test plan. Twenty minutes with a librarian or lab manager, potentially decisive.
- [ ] **Resolve the two INFERRED requirement cells.** Measure shoulder and elbow
  centre-of-mass moment arms; the ≈10 N·m and ≈3 N·m figures in
  [docs/requirements.md](docs/requirements.md) depend on assumptions no source supplies.
- [x] ~~Check NYU's standards platforms before spending.~~ **Answered 2026-09-24: NYU's ME
  standards guide lists only Knovel and ASTM Compass. No ISO/IEC access is evidenced.**
- [ ] **Buy ISO/TR 23482-2 (CHF 204) first**, not ISO 13482 itself. Free ISO Online Browsing
  Platform previews expose the scope clauses, which covers most citation needs. Full set at
  list is CHF 1,303 — do not buy it blind.
- [ ] **Watch ISO/FDIS 13482.** Edition 2 reached FDIS stage 50.20 with the ballot initiated
  2026-09-15 and may publish during this project. It renames the standard to *Robotics —
  Safety requirements for service robots* and doubles it to 160 pages, but **keeps the
  medical exclusion**, so the gap this project argues around survives. The open question —
  the highest-value one in the repository — is whether edition 2 publishes contact limits.
  If it does, the ISO 14971 import argument is replaced by direct compliance.
- [ ] **Rewrite the project's safety argument.** Replace "compliance absorbs impact" with
  "a series spring makes force measurable from deflection and bounded when unpowered."
  The first claim is contradicted by the literature; the second is defensible and stronger
  for frail users.
- [ ] **Rewrite the novelty claim** against [docs/prior-art.md](docs/prior-art.md).
  HuggieBot is one search away from any reviewer.

## Phase 1 — Screening analysis, 1–2 days

- [ ] **Run the structural load-path calculation** before any actuator is chosen. Apply
  `M = PπD³/8` to the candidate arm geometry and confirm the inflatable branch is dead on
  the number rather than on assertion. Compare against the ~100 N·m a 200 N lean applies
  at 0.5 m.
- [ ] **Tipping-moment and base-mass calculation** for the freestanding case against the
  ≥330 N hand-height reaction requirement. ROBEAR needed 140 kg of robot to handle a 60 kg
  person; find out what this design needs before committing to a footprint.
- [ ] **Static-hold thermal budget.** Backdrivable transmissions stall under a sustained
  lean. No source characterises tendon or motor thermal limits in that condition, so
  calculate it — Kengoro carries evaporative cooling for exactly this reason.
- [ ] **Actuator down-select against 28 N and ≈10 N·m**, not against the brief's implied
  target. Several families in [A1](literature/sections/A1.md) that look disqualified at
  tens of newton-metres return to range at this number.
- [ ] **Decide tethered vs untethered supply.** If pneumatic, every untethered fluidic
  supply in the verified literature is one to two orders short; the compressor goes in a
  damped base or another room, or the design moves to SEA.

## Phase 2 — Bench characterisation, first hardware

- [ ] **Build the impact rig from the Alhaddad 2019 recipe** — 3D-printed suspended dummy
  head, clay-filled pendulum impactor, 240 fps camera with Tracker. Low hundreds of
  dollars, peer-reviewed precedent. Note its honest null result and power the study
  accordingly.
- [ ] **Characterise the clamping case, which no source covers.** Force ramp at 1 N/s and
  displacement ramp at 1.5 cm/s per Monteleone's protocols, degradable to a winch and a
  load cell. This and tip-over are the two hazards with no published number.
- [ ] **Characterise a tactile skin under sustained lean.** No paper tests a skin under a
  sustained ~200 N load on a compliant trunk. Expect drift — one capacitive skin shows a
  78-minute stress-relaxation constant. This experiment is the team's own contribution.
- [ ] **Measure dB(A) at the patient's ear position** if the design is pneumatic. The
  literature asserts "noisy compressors" qualitatively and moves on; nobody has published
  the number.
- [ ] **Instrument to ≥10 kHz** with 100 Hz Butterworth filtering, and hold pass/fail
  margins no tighter than ~30% given the measurement error budget.

## Phase 3 — Human subjects

- [ ] **Submit IRB early, and understand what it decides.** Beyond the ethics review, the
  **NYU IRB makes the significant-risk / non-significant-risk determination**, and that call
  decides whether an FDA Investigational Device Exemption is needed before anyone gets into
  the machine. 21 CFR 812 engages as soon as a human is used to determine safety or
  effectiveness, and no 812.2(c) exemption covers a body-weight-supporting prototype. The
  Common Rule applies regardless — 45 CFR 46.102(e)(1) says "whether professional or
  **student**." A powered prototype touching vulnerable participants is full-board territory;
  plan a powered contact study on healthy adults plus a non-contact elderly arm.
- [ ] **Know the commercialisation trigger.** The project is exempt from FDA registration
  under 21 CFR 807.65(f) *only* while built solely for research or teaching and never
  commercially distributed. If it were ever commercialised the likely route is **De Novo**,
  with 21 CFR 890.3480 (powered lower-extremity exoskeleton, Class II special controls) as
  the closest existing template.
- [ ] **Confirm whether NYU's IRB requires review for unfunded student design testing.**
  Listed as could-not-determine in [G3.md](literature/sections/G3.md); one email answers it.
- [ ] **Use validated instruments**: Perceived Danger as primary DV, RoSAS for
  approachability, GAToRS as pre-exposure covariate. Do not write a custom questionnaire —
  92% of HRI researchers have relied on non-validated custom scales, and that is the
  failure mode to avoid by name.
- [ ] **Include a rigid control condition.** The paper the team would most want to cite
  (Du Pasquier 2025, n=106, ages 18–89) cannot separate softness from "any successful
  demo" because it has no rigid control. Do not repeat that.
- [ ] **Manipulate motion as well as material.** Every study that varied both found motion
  dominant. A material-only study will likely find nothing.

## Open questions worth a paper

Three gaps are genuinely unoccupied, documented in
[docs/evidence-limits.md](docs/evidence-limits.md):

1. Pain onset is not a valid injury proxy for frail elderly users, and no data closes the
   gap between young-volunteer pain thresholds and elderly-donor injury limits.
2. No published work validates interaction control, sensing, or structure on a
   freestanding compliant torso bearing body weight.
3. No tactile skin has been characterised under a sustained human lean.
