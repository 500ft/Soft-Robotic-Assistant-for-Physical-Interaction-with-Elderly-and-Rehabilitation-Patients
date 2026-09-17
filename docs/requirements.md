# Derived requirements

Every row traces to a source in [`literature/literature_matrix.csv`](../literature/literature_matrix.csv).
Cells marked **INFERRED** are arithmetic, not citations, and must be measured before
the spec is frozen.

## Specification

| Requirement | Value | Source | Status |
|---|---|---|---|
| End-effector assistive force | **28 N** (45 N ceiling) | MIT-MANUS; chosen as the elbow-extension strength of a weak seated woman | cited (E1) |
| Assist-as-needed modulation band | **±6 N** | Arantes 2023, n=5 stroke patients; corroborated independently in D1 | cited (E1, D1) |
| Shoulder gravity-compensation torque | **≈10 N·m** | arithmetic from arm mass, COM arm 0.30 m | **INFERRED** — moment arm not cited |
| Elbow gravity-compensation torque | **≈3 N·m** | arithmetic from forearm mass, COM arm 0.16 m | **INFERRED** — moment arm not cited |
| Structural reaction at hand height, no tipping | **≥330 N** | derived from sit-to-stand load literature | cited (E1) |
| Max end-effector velocity | **1.06 m/s** at 3 kg reflected inertia | ISO/TS 15066 Formula (A.1), chest-governed | derived, arithmetic validated |
| Sternum contact pressure limit | **50 N/cm²** — *not* ISO's 120 | Behrens n=112; corroborated by Park n=90, Han n=40 | cited (C1) |
| Sternum blunt impact force | **≈110 N** — *not* the 280 N in circulation | Behrens 2022, 28 body regions | cited (C2) |
| Session protocol | 45 min × 3/week × 8–12 weeks ≈ 24 h total | RATULS, ARMin and T-WREX converge | cited (E1) |
| Repetition cycle time | **≤12 s** | 322 reps/hour demonstrated vs 32/session conventional | cited (E1) |
| Test rig sampling | ≥10 kHz, 100 Hz Butterworth | impacts are 6–10 ms events | cited (C2) |
| Pass/fail margin | no tighter than **~30%** | certified devices disagree ±10%; transient underestimation 10–25% | cited (C2) |

The force target is far below what the brief implies. That is the single most useful
number here: against ≈10 N·m rather than tens of newton-metres, several actuator
families that look disqualified in [A1](../literature/sections/A1.md) return to range.

## The safety argument that survives

The brief's premise is that compliance is the mechanism that earns trust, implying
compliance is what makes contact safe. The literature does not support that as stated.

Haddadin (IROS 2010) shows intrinsic joint elasticity does **not** reduce HIC or peak
impact force versus conventional actuation with some joint elasticity, and identifies
conditions where compliant actuation is *more* dangerous because the spring stores
energy. The 2007 crash tests show the other half: a DLR LWR-III scored HIC36 < 25 at
2 m/s against a EuroNCAP limit of 650, and HIC saturates with robot mass. That paper's
own conclusion is that no robot of any mass becomes dangerous at 2 m/s by these criteria
**as long as clamping is excluded**.

For a torso a person leans on, clamping is not excluded. It is the normal case.

Four sections arrive here independently ([A2](../literature/sections/A2.md),
[B1](../literature/sections/B1.md), [C2](../literature/sections/C2.md),
[D1](../literature/sections/D1.md)). Švarný's 2250 measurements make it concrete: a
passive soft cover cuts *transient* impact force ~40%, and stops helping in the
quasi-static case.

**The argument to make instead:** a series spring makes interaction force *measurable
from deflection* and *bounded when unpowered*. For frail users that is a strong claim,
and it is a different claim from "compliance absorbs impact."

Consequences for the test campaign: cite clamping, not HIC. Clamping and tip-over have
no number in any retrieved source and need FMEA rows and a bench test of their own.

## Architecture implications

| Question | What the evidence supports | Section |
|---|---|---|
| Structure | Rigid grounded load path, compliance in the actuation, designed soft covering at contact. Fully inflatable fails on `M = PπD³/8`: a Ø150 mm arm at 20 kPa folds at ~26 N·m against the ~100 N·m a 200 N lean applies. | B1 |
| Actuation | SEA over VSA. VSA costs a second motor and sensor chain per joint for stiffness scheduling the schedule will not use. Do not close a torque gap with a worm drive — friction corrupts the torque relationship and kills backdrivability. | A2 |
| Interaction control | Impedance, not admittance. Structural compliance between force sensor and actuator is exactly what destroys admittance passivity, and that compliance is the point of the design. | D1 |
| Sensing | Skin reports *where and when*; load cells at base and shoulder report *how much*. A capacitive skin with a 78-minute stress-relaxation constant cannot hold a sustained lean reading. | B2 |
| Static hold | Backdrivable transmissions backdrive under a static lean too. The lean case needs an explicit braked or self-locking state, not treatment as a disturbance. | B1 |
| Gravity compensation first | T-WREX, a purely passive elastic gravity balancer with no motors, beat its control group at 6 months on ~4 min of therapist attention per hour. | E1 |

## Human-subject campaign

Instruments, ranked by psychometric rating from the GMU HRI Scale Database:
**Perceived Danger** (Molan 2025, 12 items, free scoring PDF, 100%) as primary DV;
**RoSAS** (18 items, 85%) for approachability; **GAToRS** (20 items, CC-BY, 100%) as a
pre-exposure covariate; Godspeed's 3-item safety index for comparability only, noting
Godspeed rates 23%. Drop NARS (superseded), Jian (46%, never validated by its authors),
Schaefer (31%). All are free; the cost is library access, not licensing.

Realistic design for a senior-design calendar: a powered contact study on healthy
adults plus a **non-contact** elderly arm. A powered prototype touching vulnerable
participants is full-board IRB territory the schedule cannot absorb.

## Findings that complicate the project

Recorded because a design review will raise them.

- **Robot therapy does not beat dose-matched conventional therapy.** RATULS (n=770)
  was null on its primary outcome. The ARMin RCT beat conventional therapy by 0.78
  Fugl-Meyer points against a 4.25-point MCID. Cochrane's effect is small and measured
  mostly against *less* therapy. The defensible thesis is dose, not kinematics.
- **Sit-to-stand is out of reach.** Crutch-free STS costs >121 N·m hip and >140 N·m
  knee; a commercial lower-limb exoskeleton already fails that, and this project does
  not actuate legs. What survives is the ≥330 N structural reaction requirement.
- **Softness earns trust weakly and narrowly.** The one clean causal result (Block &
  Kuchenbecker 2019: foam covering raised perceived safety, F(2,58)=5.28, p=0.0078) is
  n=30 young engineering students, and in the same study softness had no significant
  effect on perceived sociality or caring. Every study manipulating both material and
  motion found motion dominant. Kim 2016 found soft arms more human-like but *more
  fragile*. Obayashi 2022 — the only soft robot tested in a real nursing home, mean age
  86.8 — found the softness advantage not significant.
- **Older adults are hostile to this form factor.** Pino 2015 measured healthy older
  adults' adoption intention at **0.13 out of 3.0**, with explicit hostility to humanoid
  form.
- **The reliability bar is brutal.** HOBBIT's object pickup worked reliably on 18% of
  372 deployment days while its navigation ran >98%.
- **Safe force and assistive force are different numbers on the same hardware.**
  Baxter: 2.2 kg per arm in safety mode, 25 kg with safety disabled.
- **Nothing validates unsupervised contact with a frail elderly person.** The entire
  requirements table above is a *supervised-use* spec. The brief's unsupervised-operation
  framing has no clinical evidence behind it yet.
