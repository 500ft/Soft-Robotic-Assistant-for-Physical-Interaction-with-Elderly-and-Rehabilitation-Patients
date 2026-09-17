# Prior art and the defensible claim

Full entries with verification routes in [`literature/sections/F1.md`](../literature/sections/F1.md).

## The novelty claim in the brief is false as written

The brief states that "few systems attempt to deliver meaningful assistive torque from
a soft, freestanding humanoid upper body." Three systems already occupy that ground.

- **HuggieBot 2.0/3.0** — Block & Kuchenbecker, ACM THRI 2023. Freestanding, human-sized,
  inflated PVC torso that doubles as a contact sensor, two 6-DOF arms, foam padding,
  torque-threshold stopping, **48 human subjects in uncontrolled full-body contact**.
  This is the nearest neighbour and it is very near.
- **King Louie** — Best & Killpack, Humanoids 2015. A **14-DOF fully inflatable fabric
  humanoid** with two arms and a torso joint. Softer than anything this project will build.
- **Niiyama et al.**, Frontiers in Robotics and AI 2021. Blower-powered inflatable hugging
  robot at 50–300 Pa.

A reviewer finds HuggieBot in one search. Reframe before the design review.

## The field is bimodal, and it is a physics problem

| Group | Assistive force | Status |
|---|---|---|
| Rigid patient-handling robots | RIBA 61 kg, RIBA-II 80 kg (on a 230 kg robot), RoNA 500 lb claimed | Discontinued. RIKEN-SRK closed March 2015; RIKEN's own page states none were deployed in care facilities. |
| Genuinely soft arms | No published assistive force at all. Only compliant-arm payload found: GummiArm, **4.4 N**. | Research prototypes. |
| Worn assistive devices | Harvard shoulder exosuit **6.6 N·m / 150 g per limb**; ALS wearable n=10, Sci Transl Med | The only group delivering *measured* assistance to *actual patients*. |

**Nothing lives between ~4 N and ~600 N.** That band is empty because routing the load
path through a compliant structure to the floor costs one to two orders of magnitude.
The field's answer was to put the load path on the patient's own skeleton instead.

Other reference points: Rollin' Justin 200 kg robot / 20 kg payload; Care-O-bot 4 140 kg
robot / 5 kg arm; Baxter 2.2 kg per arm in safety mode against 25 kg with safety disabled.

## The claim that survives

> A characterised, instrumented contact-force envelope for a specified low-force task —
> steadying, guiding, positioning — measured rather than asserted.

Every system in the prior-art table either asserts a force number or never measures one.
Producing a measured envelope is a real contribution and it survives contact with a
reviewer. It is also achievable on a senior-design calendar, which the original framing
is not.

## No certification exists to point at

No vendor or paper page retrieved cites a certification number against ISO 13482,
ISO 10218 or ISO/TS 15066 — not Care-O-bot 4, not KUKA iiwa. KUKA's human-robot
collaboration claim is prose. This is consistent with the standards gap documented in
[docs/evidence-limits.md](evidence-limits.md): there is no number to cite because no
standard both governs these devices and publishes limits.

## Documented failure modes to budget for

- Inflatable **seam and valve leaks** — HuggieBot rebuilt its torso.
- **Bladder pinching** that consumed a third of the pressure range — King Louie ran
  0–17 psi of a 0–25 psi rating.
- **Tendon failure at attachment points** plus elastomer creep — GummiArm.
- **Porous elastomer that will not hold pressure** — Disney.
- **Thermal stall under sustained static load.** No paper characterises this, but Kengoro
  carries evaporative cooling precisely because holding a pose stalls motors. A leaning
  patient is that condition indefinitely.

## Commercial record

Every commercial attempt in this space is dead: Rethink Robotics 2018, Pepper 2021
(~27k units), RIKEN-SRK 2015, Willow Garage 2014. RoNA and HOBBIT never shipped.
HOBBIT's €16k bill of materials remained unaffordable for its intended users.
