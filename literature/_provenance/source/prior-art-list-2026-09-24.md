# Annotated bibliography of prior art

## Patent search

### Soft robotic assistive device  
**GB2622575B / WO2024052578A1, 2024–2025**

- Soft pneumatic actuator intended to **assist, resist, or actuate movement of a human body part**.
- Uses a compact piezoelectric resonant gas pump instead of a conventional large pneumatic supply.
- Pressure measurements can be used to estimate actuator **shape, displacement, volume, and delivered force**.
- **Direct relevance:** overlaps strongly with pneumatic actuation, rehabilitation assistance, pressure-based sensing, and compact pneumatic hardware.
- **Important distinction:** primarily a wearable/body-mounted device rather than a freestanding bilateral robotic assistant. :chatgpt-content-reference{index="0"}

---

### Soft robotic glove for rehabilitation  
**WO2019223568A1, University of Hong Kong, 2019**

- Uses pneumatically driven soft actuators, flexible rods, and fabric constraints to produce finger flexion and extension.
- Designed to provide useful force while remaining lightweight and compliant.
- Geometry is intended to transmit actuator force to the fingertip with limited loss.
- **Direct relevance:** demonstrates how pneumatic compliance can transmit useful human-assistance forces without a conventional rigid transmission.
- **Limitation relative to project:** only addresses the hand and remains wearable. :chatgpt-content-reference{index="1"}

---

### Pneumatically driven flexible wearable upper-limb rehabilitation system  
**CN110812124A, 2020**

- Pneumatic actuation is applied across an upper-limb wearable rehabilitation system.
- Intended to improve human-machine compatibility compared with conventional rigid rehabilitation robots.
- Extends soft pneumatic assistance beyond the hand toward larger upper-limb motion.
- **Direct relevance:** prior art against any broad claim that pneumatic assistance of the complete upper limb is novel.
- **Project distinction:** the proposed system is a separate robot physically interacting with the patient rather than an exoskeleton attached to the patient. :chatgpt-content-reference{index="2"}

---

### Rehabilitation robot for shoulder rotation  
**CN112263435B, 2020**

- Combines **pneumatic artificial muscles, cables, motorized arc guides, and proportional pressure control**.
- Pneumatic artificial muscles generate pulling forces while mechanical guides determine shoulder motion.
- Provides full circular shoulder rehabilitation through combined actuator motion.
- **Direct relevance:** closely related prior art for pneumatic artificial muscles used to generate shoulder-level assistance.
- **Design implication:** shoulder actuation using PAMs is established prior art, so novelty needs to come from robot architecture, compliant interaction, sensing, or control rather than PAM use alone. :chatgpt-content-reference{index="3"}

---

### Upper-limb rehabilitation robot  
**US20200129365A1**

- Integrates separate mechanisms for the fingers, wrist, and upper limb.
- Designed to change patient joint angles while limiting excessive force.
- Shows prior art for multi-region upper-limb rehabilitation rather than single-joint devices.
- **Direct relevance:** establishes broad patent coverage around integrated upper-limb robotic rehabilitation.
- **Project distinction:** mechanically coupled rehabilitation apparatus rather than a freestanding soft-contact robotic assistant. :chatgpt-content-reference{index="4"}

---

### Upper limb rehabilitation robot  
**US9956130B2, 2018**

- Includes an actuated linkage capable of assistant, active, and resistive rehabilitation modes.
- Mechanical geometry supports horizontal, inclined, and vertical exercises.
- **Direct relevance:** assist-as-needed and configurable upper-limb rehabilitation are already established functions.
- **Project distinction:** conventional mechanism architecture without the whole-arm soft physical interaction central to the proposed concept. :chatgpt-content-reference{index="5"}

---

### Upper limb rehabilitation robot system  
**US10596056B2**

- Five-bar parallel rehabilitation mechanism with cable transmission.
- Provides controlled endpoint force in different directions.
- Includes sensing, computer control, training records, and visual feedback.
- **Direct relevance:** rehabilitation force delivery plus quantitative performance monitoring is established prior art.
- **Design implication:** simply recording forces or rehabilitation progress is unlikely to provide meaningful novelty by itself. :chatgpt-content-reference{index="6"}

---

### Soft robotic gripping assistance  
**US11027436B2**

- Covers soft robotic devices for assisting impaired grasping.
- Patent references include foundational soft pneumatic rehabilitation work by Polygerinos and others.
- Demonstrates substantial existing IP around **soft actuation + human assistance + rehabilitation**.
- **Direct relevance:** reinforces that the project's defensible contribution cannot simply be "soft actuators used for rehabilitation." :chatgpt-content-reference{index="7"}


# Related journal / conference papers

## Physically Assistive Robots: A Systematic Review of Mobile and Manipulator Robots That Physically Assist People with Disabilities  
**Nanavati, Ranganeni & Cakmak, 2024**  
*Annual Review of Control, Robotics, and Autonomous Systems*

- Screened **1,981 papers** and retained **87 studies** involving physically assistive mobile/manipulator robots and users with disabilities or older adults.
- Identifies three major research dimensions:
  - Interaction interfaces
  - Levels of autonomy
  - Adaptation
- Covers ADLs including feeding, dressing, hygiene, mobility, and manipulation.
- **Direct relevance:** strongest high-level map of the research field surrounding this project.
- **Research gap:** many systems solve individual ADLs, but general-purpose physical assistance involving sustained human contact remains difficult. :chatgpt-content-reference{index="8"}

---

## Baloo: A Large-Scale Hybrid Soft Robotic Torso for Whole-Arm Manipulation  
**Johnson, Clawson & Killpack, 2024**

- Human-scale robotic torso with **two approximately 1 m pneumatically driven soft arms**.
- Uses a hybrid rigid-soft architecture rather than making the complete structure compliant.
- Demonstrates contact-rich manipulation of large, heavy objects.
- Develops adaptive control for strongly nonlinear soft-arm dynamics.
- **Direct relevance:** one of the closest existing mechanical architectures to the proposed system.
- **Major difference:** Baloo focuses on whole-arm object manipulation rather than physical rehabilitation or assistance of a human patient. :chatgpt-content-reference{index="9"}

---

## Development and Evaluation of the Human-Interactive Robot RI-MAN  
**Odashima et al., 2007**

- Human-scale nursing-care robot designed specifically for **physical human handling**.
- Designed around safety, softness, whole-body interaction, and sufficient strength for caregiving.
- Demonstrated lifting and holding a human-sized body.
- **Direct relevance:** establishes early prior art for a freestanding robot with soft surfaces physically supporting a person.
- **Major implication:** "a soft robot that physically assists humans" is not a novel concept by itself. :chatgpt-content-reference{index="10"}

---

## Development of Nursing-Care Assistant Robot RIBA  
**Mukai et al., 2010–2011**

- Developed specifically for **bed-to-wheelchair patient transfer**.
- Human-type arms physically lift the patient.
- Uses extensive tactile sensing to guide manipulation and improve safety.
- Demonstrated actual human transfer rather than only mannequin interaction.
- **Direct relevance:** extremely important prior art for high-load physical assistance.
- **Design lesson:** high-force human assistance requires distributed force sensing and deliberate contact management, not only compliant actuators. :chatgpt-content-reference{index="11"}

---

## ROBEAR: Nursing-Care Assistance for Transfer and Standing  
**RIKEN, 2015**

- Uses two human-like arms to:
  - Transfer a patient between a bed and wheelchair.
  - Assist standing.
- Uses several types of force-related sensors in each arm to generate softer interaction.
- **Direct relevance:** perhaps the closest historical functional comparison for physically supporting elderly or mobility-impaired users.
- **Project distinction:** ROBEAR uses high-capacity conventional robotic mechanisms rather than intrinsically compliant pneumatic soft arms. :chatgpt-content-reference{index="12"}

---

## Whole-arm tactile sensing for beneficial and acceptable contact during robotic assistance  
**Jain et al., 2013**

- Demonstrated a PR2 robot intentionally making contact between its arm and the user's body.
- Whole-arm tactile sensing allowed the robot to regulate contact while reaching around a person.
- Tested with people with motor impairments for tasks including pulling a blanket and wiping the face.
- Users generally perceived controlled arm-body contact as safe and comfortable.
- **Direct relevance:** strongly supports deliberate distributed arm contact rather than treating every collision as an emergency.
- **Design implication:** compliant whole-arm contact could become an explicit system capability for the proposed robot. :chatgpt-content-reference{index="13"}

---

## PrioriTouch: Adapting to User Contact Preferences for Whole-Arm Physical Human-Robot Interaction  
**Madan et al., CoRL 2025**

- Targets caregiving tasks such as bathing, dressing, and patient transfer where contact occurs along the robot arm.
- Learns user-specific preferences for acceptable body contact.
- Combines contact-preference learning with force and pose control.
- **Direct relevance:** moves pHRI beyond binary safe/unsafe contact toward **comfortable, individualized contact**.
- **Research direction:** highly relevant if the proposed robot is expected to touch elderly users along the forearm, upper arm, or torso rather than only at its end effector. :chatgpt-content-reference{index="14"}

---

## RABBIT: Robot-Assisted Bed Bathing with Multimodal Perception and Integrated Compliance  
**Madan et al., HRI 2024**

- Uses combined hardware and software compliance for direct physical care.
- RGB and thermal perception distinguish different skin conditions during bathing.
- Includes a compliant cleaning end effector.
- User study included 12 participants, including a participant with severe mobility limitations.
- **Direct relevance:** demonstrates modern caregiver-style physical human-robot interaction with compliance explicitly incorporated into system design. :chatgpt-content-reference{index="15"}

---

## VTTB: A Visuo-Tactile Learning Approach for Robot-Assisted Bed Bathing  
**Gu & Demiris, IEEE RA-L 2024**

- Combines visual body-shape information with tactile contact sensing.
- Robot learns to follow nonlinear human-body surfaces while maintaining physical contact.
- Tested first on a medical mannequin and generalized toward human interaction.
- **Direct relevance:** demonstrates why vision alone is insufficient for sustained physical assistance.
- **Design implication:** tactile/contact information should probably be considered a primary sensing mode in this project. :chatgpt-content-reference{index="16"}

---

## Learning Bimanual Manipulation Policies for Bathing Bed-Bound People  
**Gu & Demiris, IROS 2024**

- Uses two arms simultaneously during caregiving.
- One arm can support or lift a limb while the other performs a task.
- Explicitly controls interaction within safe force bounds.
- **Direct relevance:** directly relevant to the project's proposed **two-arm architecture**.
- **Design implication:** bilateral arms provide capabilities that cannot be reproduced by treating two arms as independent single manipulators. :chatgpt-content-reference{index="17"}

---

## High Fidelity Capture, Reconstruction, and Transfer of Human Demonstrations for Robot-Assisted Bathing  
**Lakshmipathy et al., RSS 2026**

- Captures synchronized human caregiver:
  - Motion.
  - Body geometry.
  - Contact.
  - Interaction force.
- Transfers human caregiving demonstrations to a robot equipped with an arm-mounted soft hand.
- Focuses specifically on sustained, contact-rich human interaction.
- **Direct relevance:** one of the newest examples of transferring actual caregiver physical behavior into robotic assistance.
- **Research implication:** quantitative caregiver force/contact data may provide better design requirements than arbitrary robot force targets. :chatgpt-content-reference{index="18"}

---

## Soft Robotics in Upper Limb Neurorehabilitation and Assistance: Current Clinical Evidence and Recommendations  
**Tanczak et al., 2025**  
*Soft Robotics*

- Reviews clinical evidence for soft upper-limb rehabilitation devices.
- Softness is associated with potential improvements in:
  - Compliance.
  - Comfort.
  - Wearability.
  - Safety.
- Authors emphasize that technical performance alone is insufficient and that clinical evidence remains limited for many soft systems.
- **Direct relevance:** provides the clinical evidence boundary for claims about the benefit of soft rehabilitation robotics.
- **Important conclusion:** softness should not automatically be equated with superior clinical outcomes. :chatgpt-content-reference{index="19"}

---

## Supporting Upper Limb Movements with a Soft Robot after a Brachial Plexus Injury  
**2026, Nature Communications**

- Uses separate pneumatic shoulder and elbow actuators.
- User intent is detected using IMUs.
- Shoulder control incorporates gravity compensation.
- Provides real human upper-limb assistance rather than only benchtop actuator testing.
- **Direct relevance:** current evidence that soft pneumatic actuators can provide functional assistance at the shoulder and elbow.
- **Major distinction:** the actuators are worn by the person, so the human skeleton carries much of the structural loading. :chatgpt-content-reference{index="20"}

---

## Soft Pneumatic Actuator Fascicles for High Force and Reliability  
**Robertson et al., 2017**

- Parallel soft actuator bundles generated **more than 112 N**.
- Four-actuator configuration demonstrated improved force density relative to a geometrically equivalent single actuator.
- Parallel construction also provides partial fault tolerance if one actuator fails.
- **Direct relevance:** one of the strongest papers supporting bundled pneumatic actuators for human-scale force production.
- **Design implication:** multiple smaller actuators arranged in parallel are more defensible than one very large soft actuator. :chatgpt-content-reference{index="21"}

---

## Soft Robotic Glove for Combined Assistance and At-Home Rehabilitation  
**Polygerinos et al., 2015**

- Fiber-reinforced soft actuators mechanically programmed to reproduce finger trajectories.
- Portable hydraulic/pneumatic support system.
- Closed-loop pressure control.
- Demonstrated functional grasping.
- **Direct relevance:** foundational demonstration of soft actuation transitioning from laboratory material research into a complete assistive system.
- **Design lesson:** actuator geometry itself can encode part of the desired kinematics. :chatgpt-content-reference{index="22"}

---

## A Fully Fabric-Based Bidirectional Soft Robotic Glove  
**Yap et al., IEEE RA-L 2017**

- Fabric pneumatic actuators provide active flexion and extension.
- Designed for both rehabilitation and activities of daily living.
- Fabric construction reduces rigid material at the human interface.
- **Direct relevance:** demonstrates lightweight bidirectional pneumatic assistance and provides a fabrication precedent for soft interfaces. :chatgpt-content-reference{index="23"}

---

## Design and Testing of a Soft Parallel Robot Based on Pneumatic Artificial Muscles for Wrist Rehabilitation  
**Wang & Xu, 2021**

- Six pneumatic artificial muscles arranged in a parallel mechanism.
- Provides flexion-extension, abduction-adduction, and pronation-supination.
- Uses an EMG sensor to evaluate rehabilitation activity.
- Parallel architecture increases effective stiffness while retaining actuator compliance.
- **Direct relevance:** strong example of combining a rigid kinematic architecture with compliant pneumatic actuation.
- **Design implication:** compliance and structural stiffness do not have to be mutually exclusive. :chatgpt-content-reference{index="24"}

---

## Design and Control of Soft Rehabilitation Robots Actuated by Pneumatic Muscles: State of the Art  
**2020**

- Reviews pneumatic-muscle rehabilitation robot architectures and control methods.
- Identifies nonlinear actuator behavior as a central control problem.
- Covers mechanical arrangements and control strategies rather than treating pneumatic muscle selection alone as the design problem.
- **Direct relevance:** useful foundation for actuator/control architecture selection. :chatgpt-content-reference{index="25"}

---

## Assist-as-Needed Control of a Soft Rehabilitation Robot  
**2025**

- Uses an interaction torque observer rather than requiring a dedicated interaction torque sensor.
- Assistance changes according to the patient's voluntary movement.
- Combines position control and estimated interaction force.
- **Direct relevance:** supports **assist-as-needed** rather than forcing a predefined trajectory.
- **Design implication:** rehabilitation assistance should ideally supplement patient effort instead of replacing it. :chatgpt-content-reference{index="26"}

---

## Robot Collisions: A Survey on Detection, Isolation, and Identification  
**Haddadin, De Luca & Albu-Schäffer, 2017**

- Establishes the major collision-management sequence:
  - Detection.
  - Isolation.
  - Identification.
  - Classification.
  - Reaction.
- Covers whole-robot collision handling for systems operating around humans.
- **Direct relevance:** provides the core safety-control framework for unintended contact.
- **Limitation for this project:** intentional sustained contact must be distinguished from hazardous collision. :chatgpt-content-reference{index="27"}

---

## Semantic-Physical Sensor Fusion for Safe Physical Human-Robot Interaction in Dual-Arm Rehabilitation  
**2026**

- Combines force/torque, posture, visual, and semantic information.
- Estimates internal joint torque from external sensing.
- Demonstrated responses to impacts, instability, and visual occlusion.
- Reported approximately **223 ms end-to-end safety decision latency**.
- **Direct relevance:** specifically addresses dual-arm rehabilitation safety using heterogeneous sensor information.
- **Design implication:** redundant sensing is preferable to depending on one collision metric. :chatgpt-content-reference{index="28"}

---

## EmArm: Whole-Arm Tactile Sensing and Adaptive Robotic Manipulation  
**2026**

- Rigid robotic arm covered with large-area soft tactile sensing.
- Provides high-resolution contact localization over the arm body.
- Uses tactile information for intention recognition and trajectory replanning.
- **Direct relevance:** shows an alternative to making the entire structural arm soft:
  - Rigid internal load-bearing structure.
  - Soft, instrumented external skin.
- **Design implication:** this architecture may be more practical for the proposed robot than a fully soft arm if substantial loads must be carried. :chatgpt-content-reference{index="29"}


# Other relevant prior art

## ISO 13482:2014  
**Safety requirements for personal care robots**

- Explicitly covers:
  - Mobile servant robots.
  - Physical assistant robots.
  - Person carrier robots.
- Addresses close human-robot physical contact.
- Requires hazards to be eliminated or reduced through inherently safe design and protective measures.
- **Direct relevance:** likely the most relevant non-medical safety framework if the robot is classified as a personal-care/assistive system rather than a medical device.
- A revision is currently progressing through ISO. :chatgpt-content-reference{index="30"}

---

## ISO/TR 23482-1:2020  
**Safety-related test methods for personal care robots**

- Provides test methods corresponding to ISO 13482 safety requirements.
- Testing parameters are expected to follow the robot-specific risk assessment.
- **Direct relevance:** useful for converting abstract safety requirements into future prototype tests. :chatgpt-content-reference{index="31"}

---

## ISO/TR 23482-2:2019  
**Application guidelines for ISO 13482**

- Provides guidance specifically for close physical interaction and human contact.
- Covers physical assistant robots and other personal-care robot classes.
- **Direct relevance:** useful when developing the project's eventual hazard analysis and verification plan. :chatgpt-content-reference{index="32"}

---

## IEC 80601-2-78:2019 + AMD1:2024  
**Medical robots for rehabilitation, assessment, compensation or alleviation**

- Applies specifically to medical robots that **physically interact with a patient with an impairment**.
- Addresses basic safety and essential performance.
- The consolidated current edition includes the 2024 amendment.
- A second edition is already under development.
- **Direct relevance:** considerably more appropriate than industrial collaborative-robot standards if the system is ultimately intended as a medical rehabilitation robot. :chatgpt-content-reference{index="33"}

---

## ISO 14971:2019  
**Medical-device risk management**

- Requires systematic:
  - Hazard identification.
  - Risk estimation.
  - Risk control.
  - Monitoring of risk-control effectiveness.
- Applies throughout the medical-device life cycle.
- **Direct relevance:** provides the appropriate framework for hazards such as excessive contact force, pneumatic failure, unexpected movement, pinch points, instability, sensor failure, and loss of pressure. :chatgpt-content-reference{index="34"}

---

## FDA: Robotic Medical Devices

- FDA explicitly includes robotic rehabilitation systems within robotic medical devices.
- Current regulatory attention increasingly includes autonomous and remotely operated robotic systems.
- FDA recommends early regulatory engagement for novel robotic medical devices.
- **Direct relevance:** important if the senior-design concept later progresses toward a clinical product rather than remaining a research prototype. :chatgpt-content-reference{index="35"}


# Prior-art conclusion

- **Soft pneumatic rehabilitation actuation already exists extensively.**
- **Pneumatic artificial muscles for the shoulder and upper limb already exist.**
- **Freestanding robots capable of lifting or supporting people already exist.**
- **Whole-arm compliant contact with disabled users already exists.**
- **Dual-arm caregiving systems already exist.**
- **Distributed tactile sensing for contact-rich assistance already exists.**

### Stronger remaining research space

- Combine **human-scale bilateral physical assistance** with intrinsically compliant or hybrid soft actuation.
- Allow **safe intentional whole-arm contact**, rather than only end-effector interaction.
- Provide assistance appropriate to rehabilitation without requiring the patient to wear a full exoskeleton.
- Integrate distributed contact sensing with **assist-as-needed force control**.
- Design one freestanding upper-body platform around both **rehabilitation exercises and physical ADL assistance**.
- Establish quantitative force, stability, failure, and safety requirements specifically for interaction with elderly or mobility-impaired users.

### Most relevant comparison systems

**Closest mechanical architecture**
- Baloo. :chatgpt-content-reference{index="36"}

**Closest caregiving architecture**
- RIBA / ROBEAR. :chatgpt-content-reference{index="37"}

**Closest whole-arm contact work**
- Jain et al. and PrioriTouch. :chatgpt-content-reference{index="38"}

**Closest modern rehabilitation literature**
- Tanczak et al. and Nanavati et al. :chatgpt-content-reference{index="39"}

**Closest actuation precedent**
- Robertson et al. :chatgpt-content-reference{index="40"}

**Closest applicable safety framework**
- IEC 80601-2-78 for a medical rehabilitation robot, or ISO 13482 for a non-medical physical-assistance robot. :chatgpt-content-reference{index="41"}