# Rail to Digital automated up to autonomous train operation

D13.1

## Moving Block Specifications applying a train-centric approach Introduction

Due date of deliverable: 31/08/2024

Actual submission date: 08/07/2025

Leader/Responsible of this Deliverable: ATSA

Reviewed: Y


[
  {
    "Document status": "Description"
  },
  {
    "Document status": "Draft"
  },
  {
    "Document status": "Released after review"
  },
  {
    "Document status": "Updated after TMT review"
  },
  {
    "Document status": "This document now notes that comments from the JU review about the Safety Analysis will be handled as part of WP14."
  },
  {
    "Document status": "Editorial"
  }
]


[
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "Dissemination Level"
  },
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "X"
  },
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "Sensitive - limited under the conditions of the Grant Agreement"
  }
]

---

Start date: 01/12/2022

Duration: 42 months

[
  {
    "ABBREVIATIONS AND ACRONYMS": "Automatic Train Operation"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "Control-Command and Signalling"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "European Train Control System"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "Rail to Digital automated up to autonomous train operation"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "Shift2Rail"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "System Theoretic Process Analysis"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "Trackside Train Detection"
  },
  {
    "ABBREVIATIONS AND ACRONYMS": "Work package"
  }
]

---

## TABLE OF CONTENTS

Acknowledgements.....2  
Report Contributors.....2  
Executive Summary.....3  
Abbreviations and Acronyms.....4  
Table of Contents.....5  
2 Introduction.....6  
2.1 Task 13.1: System Definition.....6  
2.2 Task 13.2: Moving Block Specification – Requirements, engineering, and operational rules.....6  
2.3 Task 13.3: Moving Block Safety Analysis.....6  
3 Conclusions.....7

---

## 2 INTRODUCTION

This document introduces the Deliverable 13.1 which consists of three parts corresponding to tasks within the work package. Those parts are shortly described below.

#### 2.1 TASK 13.1: SYSTEM DEFINITION

The objective of this Task (13.1) is to define the signalling system, called Moving Block System, in particular the system objectives, capabilities, boundaries, functions, operational requirements and assumptions in order to cooperate with the Moving Block concept and constitutes the first part of the Deliverable 13.1.

#### 2.2 TASK 13.2: MOVING BLOCK SPECIFICATION – REQUIREMENTS, ENGINEERING, AND OPERATIONAL RULES

Based on the System Definition the purpose of this task is to analyse the impact of the System Pillar on System Requirements and to develop a Moving Block Specification. The work on the Moving Block Specification is organized in an iterative and incremental fashion in five releases. The first three releases are planned for WP13 and releases 4 and 5 are planned for WP14. The contents of each release are defined in collaboration with the stakeholders (e.g. prototype developers and the demonstrators WP). Each release leads to an intermediate and reviewed version of the Moving Block Specification.

#### 2.3 Task 13.3: Moving Block Safety Analysis

The subject of this task was the safety analysis for the "Moving Block System" (MBS) that has been specified in Tasks 13.1 and 13.2. To move a step beyond what was previously done in S2R (e.g., in-depth analysis of relevant operational scenarios) a novel method – called System Theoretic Process Analysis (STPA) - was applied to the matter. This STPA focuses on "unsafe control actions" in control and feedback loops within complex systems. An advantage over previous methods is the potential to identify emergent risks stemming from the interaction between those (sub)systems, which are often overlooked.

---

## 3 CONCLUSIONS

The aim of this Deliverable is to define the System Architecture, Requirements and a Safety Analysis for a Moving Block System based on a train-centric approach using Full Moving block principles with Trackside Train Detection (TTD).

The Deliverable serves as a basis for prototype development of a Moving Block System and the alignment process with the System Pillar to define the CCS target architecture.

The work on the System Definition, Specification and Safety Analysis will be continued in WP14 Task 14.4.

---

# Rail to Digital automated up to autonomous train operation

# D13.1 – Moving Block Specifications applying a train-centric approach

Part 1 – System Definition

Due date of deliverable: 31/10/2024

Actual submission date: 06/06/2025

Leader/Responsible of this Deliverable: Thomas Naulin, GTSD

Reviewed: Y


[
  {
    "Document status": "Description"
  },
  {
    "Document status": "First issue"
  },
  {
    "Document status": "Incorporated review comments by WP13 Review Group"
  },
  {
    "Document status": "Version after consolidation of review comments in WP13"
  },
  {
    "Document status": "Incorporated review comments from WP27 (DR), WP44/45 (Demonstrator) and System Pillar. Aligned with release 3 of System Specification"
  },
  {
    "Document status": "Updated after review by TMT."
  },
  {
    "Document status": "Names of authors and reviewers introduced"
  },
  {
    "Document status": "Incorporation of comments by ERA"
  }
]


[
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "Dissemination Level"
  },
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "✗"
  },
  {
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "Sensitive - limited under the conditions of the Grant Agreement"
  }
]

---

Start date: 01/12/2022

Duration: 42 month

[
  {
    "Name": "Bertrand Badot, Staffan Pettersson",
    "Company": "ATSA",
    "Details of Contribution": "Author"
  },
  {
    "Name": "Konstantinos Emmannouil, Martin Woiton",
    "Company": "DB",
    "Details of Contribution": "Author"
  },
  {
    "Name": "Nader Nayeri, Thomas Naulin",
    "Company": "GTSD",
    "Details of Contribution": "Author"
  },
  {
    "Name": "Manuel Schleiffelder",
    "Company": "OBB-Infra",
    "Details of Contribution": "Author"
  },
  {
    "Name": "Bettina Morman",
    "Company": "SBB",
    "Details of Contribution": "Author"
  },
  {
    "Name": "Alfonso Lorenzo",
    "Company": "ADIF (INECO)",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Daniel Kolar",
    "Company": "AZD",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Marta Garcia, Ivan Velado Martinez",
    "Company": "CAF",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Christian Sadowski, Gregor Kolokewitsch, Philipp Schneider, Frank Skowron",
    "Company": "DB",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Christian Loeffler",
    "Company": "GTSD",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Giuseppe Pagliarulo",
    "Company": "MERMEC",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Ulrich Schöni",
    "Company": "SBB",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Simon Chadwick",
    "Company": "SMO",
    "Details of Contribution": "Reviewer"
  },
  {
    "Name": "Adelaide Vitiello, Giacomo Donati",
    "Company": "STS",
    "Details of Contribution": "Reviewer"
  }
]

---

The information in this document is provided "as is", and no guarantee or warranty is given that the information is fit for any particular purpose. The content of this document reflects only the author's view – the Joint Undertaking is not responsible for any use that may be made of the information it contains. The users use the information at their sole risk and liability.

## Disclaimer

---

## EXECUTIVE SUMMARY

This document contains the System Definition for a train-centric signalling system that aims to provide high capacity with low cost and high reliability and enables moving block operation.

This document is part of the Moving Block System specification deliverable.

This document defines the signalling system, called Moving Block System, in particular the system objectives, capabilities, boundaries, functions, operational requirements and assumptions in order to cooperate with the Moving Block concept.

---

## ABBREVIATIONS AND ACRONYMS


[
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Area of Control"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Change Request"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Control, Command and Signalling"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Digital Register"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Europe&#x27;s Rail Joint Undertaking"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "ETCS Level 2"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Interlocking"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Moving Block System"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Object Controller"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Operator Panel"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Operation and Traffic Management"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Plan Execution"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Rail to Digital automated up to autonomous train operation"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Reference CCS Architecture"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Shift2Rail"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Trackside Asset"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Trackside Asset Control and Supervision"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Train Integrity Monitoring System"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Traffic Management System"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Technical Specifications for Interoperability"
  },
  {
    "For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].": "Trackside Train Detection"
  }
]

---

## WORK PACKAGE GLOSSARY

Note: Some of those terms are currently also defined in the Glossary of other documents (e.g., System Specification, Safety Analysis) of D13.1. Therefore, as long as there is no separate Glossary document available, care must be taken to keep the definitions synchronised.


[
  {
    "Term": "Area of Control",
    "Definition": "The Area of Control is the topologically limited extent and the infrastructural Trackside Assets in this geographical extent. The term is used here for defining the technical and operational responsibility of one MBS."
  },
  {
    "Term": "Domain Data",
    "Definition": "The Domain Data refers to use case specific configuration data for the MBS to define the specific application. These can be broadly classified as Map Data, Segment Profiles, and Parameter Data. As a part of configuration process, the MBS needs Domain Data. Potential updates of Domain Data will be realised by a centralised provisioning process incl. synchronous activation of the new data version."
  },
  {
    "Term": "Operational Plan",
    "Definition": "The Operational Plan is the result of the planning process performed by the planning system (TMS). It describes either a planned Operational Movement, Operational Restriction or Operational Warning Measure through a temporal sequence of Operational Events to be implemented by underlying subsystems in the Area of Control."
  },
  {
    "Term": "Operational State",
    "Definition": "The Operational State consists of train-related information (e.g., permissions, authorisations or train position) and track-related information (e.g., state of Trackside Assets)."
  },
  {
    "Term": "System Capability",
    "Definition": "A System Capability is a service an actor requires from the system to fulfil its business goals. System capabilities are realised by exploiting one or multiple functions, usually in a chain of functions. System capabilities in terms of this document are very similar to use cases and the theory behind it."
  },
  {
    "Term": "Train-centric",
    "Definition": "A train-centric approach from a trackside point of view focuses on the train as the true business object. A train object is derived by a train-centric signalling system using the currently available sensor information from the train and the trackside. This allows the safety logic of train-centric signalling system to operate on the train objects instead on the auxiliary information ‘occupancy’ only as today in conventional block-centric signalling systems."
  },
  {
    "Term": "Trackside Asset",
    "Definition": "Trackside Assets are elements on or near the track which are used to monitor (using sensors) and/or control (using actuators) the movement of vehicles through the railway network. to provide a safe route through the railway network. They can be switchable or non-switchable and are controlled by the actors Trackside Asset Control and Supervision."
  }
]

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Usage Area</td><td style='text-align: center;'>Restriction</td><td style='text-align: center;'>A Usage Restriction Area (URA) limits or constraints operation on a part within the Area of Control. URAs can be created according to an Operational Plan (e.g. for enabling construction works) or in response to an incident (e.g. as a mitigation measure). There are various limitations possible for a URA, e.g. speed restriction, full track closure or deactivate automatic operation.</td></tr></table>

---

## TABLE OF CONTENTS

Acknowledgements.....2  
Report Contributors.....2  
Executive Summary.....4  
Abbreviations and Acronyms.....5  
Work Package Glossary.....6  
Table of Contents.....8  
List of Figures.....10  
List of Tables.....10  
1 Introduction.....11  
2 System objective.....12  
2.1 Description of the system under consideration.....12  
2.1.1 System capabilities.....12  
2.2 Long term operating strategy and conditions.....13  
2.3 System life-time considerations.....13  
2.4 Logistic considerations.....13  
3 System boundaries.....14  
3.1 Interfaces and interactions with other technological system.....15  
3.1.1 Adjacent System.....15  
3.1.2 Diagnostics System.....15  
3.1.3 Digital Register.....16  
3.1.4 ETCS on-board.....16  
3.1.5 Operator Panel.....16  
3.1.6 Plan Execution.....17  
3.1.7 Security Service.....17  
3.1.8 Trackside Asset Control and Supervision.....18  
3.2 Interfaces and interactions with physical environment.....18  
3.3 Interfaces and interactions with humans.....19  
3.4 Interfaces and interactions with other railway duty holders.....19  
System functions and elements.....20  
Scope of operational requirements influencing the system.....21  
5.1 Constraints imposed by existing infrastructure.....21  
5.2 System operating conditions and constraints.....21  
5.3 System maintenance conditions.....22  
5.4 Logistic support considerations.....22  
5.5 Review of past experience data for similar systems.....22

---

5.6 Influence on operational and maintenance personnel, passengers and public ..... 23  
5.7 Description of operating procedures ..... 23  
5.8 Modes of operation ..... 24  
6 Assumptions and Existing safety measures ..... 25  
6.1 Assumptions ..... 25  
6.2 Existing safety measures ..... 26  
7 Conclusions ..... 27  
References ..... 28

---

Figure 1: System Boundaries ..... 14  
  
LIST OF TABLES  
  
Table 2: Assumptions ..... 25

## LIST OF FIGURES

---

## 1 INTRODUCTION

The part 1 of D13.1 Moving Block ETCS Level 3 – Specification within the project FP2 - R2DATO has been developed to define the System Definition of the Moving Block System, including the assumptions.

According to EN50126 this System Definition addresses the following issues:

• System objectives

• System capabilities

• System boundaries including functional interfaces

• System functions and elements

• Scope of operational requirements influencing the system

• Assumptions and existing safety measures

This document contributes as input to the following documents, respectively work packages

D13.1 Part 2 – System Specification

D13.1 Part 3 – Safety Analysis

WP14: Moving Block ETCS Level 3 – Prototype development & Analysis

- WP44: Moving Block ETCS L3 Demonstrator – Specification

---

## 2 SYSTEM OBJECTIVE

### 2.1 DESCRIPTION OF THE SYSTEM UNDER CONSIDERATION

The Moving Block System (MBS) is based on a train-centric approach using Full Moving block principles with the overall objective to engineer high capacity, low cost, high reliability signalling systems. The MBS is defined as a single system, without enforcing the conventional separation of Radio Block Centre (RBC) and interlocking (IXL). The MBS is based on ETCS cab signalling without lineside signals. It uses a more generic and simplified safety logic by abandoning the traditional block concept mainly relying on signals. By emphasising the safety logic, the dependency on country specific operational processes is reduced.

The Moving Block System builds on the Functional Railway System Architecture defined by the System Pillar and the Moving Block specification defined in Shift2Rail  $ [4] $  and RCA initiative  $ [3] $ . Depending on the requirements and needs, the MBS can operate within an environment where TTD equipment is installed but also within an environment where TTD equipment is not installed. The rationale for considering TTD is to support migration, recovery from degraded situations, and to facilitate sensor fusion principles to foster different localisation inputs.

#### 2.1.1 System capabilities

The fundamental objectives of the MBS are to ensure safe train movement and prevent railway accidents. They can be split into the following system capabilities:

- MBS manages communication sessions with Trackside Assets (TA) via specified interfaces within its Area of Control (AoC).

- MBS manages communication sessions with trains via specified interfaces within its AoC and adjacent areas where trains are supposed to establish or terminate a communication session.

• MBS controls all TAs within its AoC.

- MBS manages the current trackside state and determines the state of the track from information given during runtime by trains and TAs within its AoC.

- MBS manages all track path allocations for all trains and vehicles within its AoC. This contains an adequate and risk-based protection of requested pieces of track for an intentional train movement.

- MBS issues authorisations for train movements based on requested and accepted track path allocations.

- MBS supervises trains and TAs to prevent railway accidents. This includes especially any collision, derailment or over-speeding.

- MBS stores an up-to-date, reliable and consistent current Operational State and provides this Operational State to systems connected to MBS.

• MBS manages Domain Data changes e.g., by introducing new parts of the track.

---

• MBS manages Usage Restriction Areas (URA) and ensures that any URA limitations or constraints are considered for operation.

• MBS handles a safe transition of train movement from and to adjacent systems.

The system is providing Moving Block operation but it needs to be understood that its application is more generic. As it authorises a movement to an arbitrary (operationally sensible) location which might or might not be the rear end of the preceding train, it is in its core moving block agnostic, as the on-board unit is. Thus, the MBS is capable of supporting fixed block, virtual fixed block and moving block operation. It depends on the requesting Plan Execution (PE) system which operation is actually performed.

### 2.2 LONG TERM OPERATING STRATEGY AND CONDITIONS

MBS shall offer increased operational flexibility (e.g., by enabling train movements from anywhere to anywhere, not using pre-defined paths) allowing for both the minimisation of manual operation by the dispatcher/operator and enabling faster recovery from degraded and emergency situations.

The long-term operating strategy of the MBS in combination with the interfacing systems revolves around a high grade of operational automation. In the case of deviations from normal operation, the higher level of automation facilitates the choice of flexible, operational alternatives as well as the reduction of risks associated with human errors by providing improved technical assistance (e.g., for construction workers, maintenance staff, operators).

All in all, MBS should contribute to the increase in capacity by utilising shorter headways enabled by the more efficient use of the infrastructure, the use of information of the running trains and the more precise occupancy information through the combination of information sources (e.g., axle counters, track circuits, Train Position Reports).

### 2.3 SYSTEM LIFE-TIME CONSIDERATIONS

System life-time is understood as system life-cycle within this system definition. MBS is foreseen with a modular functional approach. Regarding this approach several life-cycle considerations have to be considered:

MBS life-cycle is independent from life-cycles of surrounding systems. Any changes in PE, Digital Register (DR) or Trackside Asset Control and Supervision (TACS) do not affect MBS as long as interfaces used are unchanged. Due to generic safety logic, MBS life-cycle is independent from life-cycle of Domain Data provided by DR. Changes in infrastructure and TAs only affect the Domain Data of the MBS without change the software of the MBS. MBS requirements lifecycle is envisioned independent from hardware components and their operating systems.

The only dependency is given by the MBS functional lifecycle itself.

### 2.4 LOGISTIC CONSIDERATIONS

The MBS as described within this system definition is not a physical product. At this stage of development, logistic considerations are not necessary.

---

## 3 SYSTEM BOUNDARIES

This section defines the environment and boundaries of the Moving Block System (MBS) by defining the interfaces and interactions with other technological systems, the environment, humans and other railway duty holders.

As there is no target CCS reference architecture available yet, this chapter is based on the assumptions consolidated in WP13. It is expected that the interfaces or details of the interface is subject to change based on the evolvement of the target CCS reference architecture.

An overview is shown in the following figure with the mentioned technological systems, environment, humans and other railway duty holders further described in the following subchapters.

[
  {
    "Attribute": "Name",
    "Content": "Adjacent System"
  },
  {
    "Attribute": "Description",
    "Content": "An Adjacent System can be either radio-based ETCS related neighbouring system or a neighbouring system not related to radio-based ETCS.A radio-based ETCS related neighbouring system can be either another MBS or a neighbouring Radio Block Centre (RBC) and an IXL. The interface to such a neighbouring system allows trains to pass the border to/from a neighbouring Level 2 area without changing the driver responsibility and the cab-signalling.A neighbouring system not related to radio based ETCS is an IXL. The interface to such a neighbouring system allows trains to pass the border to/from an area not equipped with Level 2. The cab-signalling is replaced by optical signals."
  },
  {
    "Attribute": "Cardinality",
    "Content": "n"
  },
  {
    "Attribute": "Interface",
    "Content": "The interface to a radio-based ETCS related neighbouring system is based on the existing ETCS specifications [1], namely Subset-039 and Subset-098.For the interface to a neighbouring IXL system it is recommended, but not mandatory, to use the SCI-ILS interface as published in EULYNX [2].Notes:- Interfaces to neighbouring IXL systems depend on the supported interface capabilities of the IXL and have to be adapted, e.g., by using adapter solutions.- An interface to an adjacent MBS may also require enhancements to the existing ETCS specifications."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Diagnostics System"
  },
  {
    "Attribute": "Description",
    "Content": "Diagnostics is, as in any system, a fundamental feature."
  }
]

---

[
  {
    "Cardinality": "Interface",
    "1": "For the target architecture this interface may base on the SDI interface specification published in EULYNX [2]. This will be finally defined by the System Pillar."
  }
]

#### 3.1.3 Digital Register


[
  {
    "Attribute": "Name",
    "Content": "Digital Register"
  },
  {
    "Attribute": "Description",
    "Content": "The Digital Register (DR) provides reliable (meaning complete, accurate, current, and consistent, verified and validated), interoperable and accessible infrastructure information as a critical enabler for safety-related and non-safety-related functions. The Digital Register includes static infrastructure information (static speed profile, gradients, cant, etc.) and configuration data, which are approved after engineering process. The interface between the DR and the MBS is used to update the data in the MBS."
  },
  {
    "Attribute": "Cardinality",
    "Content": "1"
  },
  {
    "Attribute": "Interface",
    "Content": "The interface between the DR and the MBS is not standardised yet. It will be defined in coordination with WP27 considering both the data model and the handling of parameter/configuration data as defined by System Pillar Domain TCCS (SD1, SD3)."
  }
]

#### 3.1.4 ETCS on-board


[
  {
    "Attribute": "Name",
    "Content": "ETCS on-board"
  },
  {
    "Attribute": "Description",
    "Content": "The ERTMS/ETCS on-board (OBU) equipment is a computer-based system that supervises the movement of the train to which it belongs, on basis of information exchanged with the MBS."
  },
  {
    "Attribute": "Cardinality",
    "Content": "n"
  },
  {
    "Attribute": "Interface",
    "Content": "The interface to the OBU is based on existing ETCS specifications [1], namely Subset-026, Subset-037."
  }
]

#### 3.1.5 Operator Panel


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr></table>

---

[
  {
    "Name": "Description",
    "Operator Panel": "The Operator Panel is used to perform manual interaction with MBS."
  },
  {
    "Name": "Cardinality",
    "Operator Panel": "1"
  },
  {
    "Name": "Interface",
    "Operator Panel": "The interface between the Operator Panel and the MBS is not standardised yet. It will be defined considering the principles described in RCA and the work of X2Rail-5 Moving Block WP."
  }
]

#### 3.1.6 Plan Execution


[
  {
    "Attribute": "Name",
    "Content": "Plan Execution"
  },
  {
    "Attribute": "Description",
    "Content": "The Plan Execution (PE) requests the setting of field elements and the submission of authorisation for train movements e.g., according to Operational Plan from TMS (TMS is out of scope).The MBS provides the Operational State to the PE."
  },
  {
    "Attribute": "Cardinality",
    "Content": "1"
  },
  {
    "Attribute": "Interface",
    "Content": "The interface between the PE and the MBS is not standardised yet. It will be defined considering the principles described in RCA and the work of X2Rail-5 Moving Block WP."
  }
]

[
  {
    "Attribute": "Name",
    "Content": "Security Service"
  },
  {
    "Attribute": "Description",
    "Content": "The Security Service summarises all technological systems that are necessary to manage and provide the cryptographic artefacts (e.g., keys or certificates) to ensure the confidentiality, authenticity and integrity (Information Security Triad) of the communication between  - the MBS and the OBUs and  - the MBS and an Adjacent System either being a neighbouring RBC/IXL or  - another MBS and  - The MBS and the Trackside Assets."
  }
]

---

[
  {
    "Notes:  - This list is not exhaustive. In future there may be other interfaces which require securing the communication using cryptographic artefacts from the Security Service.  - For some interfaces only, a subset of the Information Security Triad is applied, e.g., for the communication between MBS and the OBUs it is only necessary to ensure the authenticity and integrity.": "1"
  },
  {
    "Notes:  - This list is not exhaustive. In future there may be other interfaces which require securing the communication using cryptographic artefacts from the Security Service.  - For some interfaces only, a subset of the Information Security Triad is applied, e.g., for the communication between MBS and the OBUs it is only necessary to ensure the authenticity and integrity.": "For managing the authentication keys between MBS and OBUs, neighbouring RBC or another MBS, the interface to the Security Service is based on the existing ETCS specifications [1], namely Subset-114, Subset-137 and Subset-146. For managing the cryptographic artefacts between MBS and the Trackside Assets, the SSI interface specification as published in EULYNX [2] may be used. This will be finally defined by the System Pillar."
  }
]

#### 3.1.8 Trackside Asset Control and Supervision


[
  {
    "Attribute": "Name",
    "Content": "Trackside Asset Control and Supervision"
  },
  {
    "Attribute": "Description",
    "Content": "The Trackside Asset Control and Supervision (TACS) reports the state of the Trackside Assets (TAs). The MBS mainly uses this interface to trigger setting the state of a TA, e.g., moving a point, and to receive status information from TAs (e.g., occupancy information from TTD). The interface also includes safety relevant maintenance issues, e.g., resetting an axle counter."
  },
  {
    "Attribute": "Cardinality",
    "Content": "n"
  },
  {
    "Attribute": "Interface",
    "Content": "For the target architecture this interface bases on the specification published in EULYNX [2]. For migration phase other interfaces, even proprietary ones, are possible."
  }
]

### 3.2 INTERFACES AND INTERACTIONS WITH PHYSICAL ENVIRONMENT

The MBS as described within this system definition is not a physical product. Therefore, at this stage of development, no interfaces and interactions with physical environment are necessary.

The MBS has to be used in a common railways' environment and therefore the system environmental conditions for railways applications as defined by EN50125 and EN50121 have to be considered whereas:

---

# Contract No. HE – 101102001

- the scope of the standards EN50125 covers the definitions and ranges of the following parameters: Altitude, temperature, humidity, air movement, rain, snow and hail, ice, solar radiation, lightning and pollution and

the standard EN50121 describes the characteristics of the railway system which affect electromagnetic compatibility (EMC) behaviour.

### 3.3 INTERFACES AND INTERACTIONS WITH HUMANS

The MBS as described within this system definition is not a physical product. Therefore, at this stage of development, no interfaces and interactions with humans are necessary and foreseen.

When using the MBS in a common railways' environment in future, an interface to a Maintenance Staff via Diagnostic System may be necessary.

For test purposes additional interactions with humans may be necessary as required by testing staff, e.g., test interfaces, additional data capture needs, etc.

### 3.4 INTERFACES AND INTERACTIONS WITH OTHER RAILWAY DUTY HOLDERS

The MBS as described within this system definition is not a physical product. Therefore, at this stage of development, no interfaces and interactions with other railway duty holders are necessary and foreseen. If there are requirements of other duty holders (e.g., railway undertakings), they will be fulfilled using the existing interfaces to the actors as described above.

When using the MBS in a common railways' environment in future, an interface to other railway duty holders may be necessary. This needs to be covered in specific projects.

---

## 4 SYSTEM FUNCTIONS AND ELEMENTS

The system functions, derived from the system capabilities in chapter 2.1.1 are outlined in the System Specification [6] whereas the System Specification comprehensively defines and elaborates on each system function by detailing its purpose, behaviour, inputs, outputs, and any dependencies and constraints.

---

# 5 SCOPE OF OPERATIONAL REQUIREMENTS INFLUENCING THE SYSTEM

### 5.1 CONSTRAINTS IMPOSED BY EXISTING INFRASTRUCTURE

The existing infrastructure today has the following characteristics that can impose constraints to the system:

- Wide range of application of baselines and system versions

Different application of L1, L1 with infill, L1 with loops, L2 with light signals, L2 only, etc.

- Highly specialised to fit to "traditional" country-specific rules

- Implement national laws that are sometimes indirectly related to rail traffic, e.g., laws for public roads that affect the use of level crossings

In conclusion, to avoid Moving Block System (MBS) dialects (e.g., in ETCS today), operational harmonisation is necessary. This would drastically minimise the need for adjustments to MBS on a national level.

Nevertheless, considering that the MBS will be integrated into existing railway infrastructure, MBS shall be able to receive necessary information from these legacy systems to be able to ensure safe movements inside its Area of Control (AoC). A major interface that needs to be established is the interfaces for adjacent interlockings and RBCs to ensure a safe handover. The integration of legacy Traffic Management Systems (TMS), control systems and object controllers have to be analysed as well for migration purposes. Therefore, requirements have to be identified and exported to these systems so that adapter solutions can be developed to connect them to MBS. MBS itself shall ideally only communicate to another MBS and the systems specified in the target Traffic CS architecture defined by the System Pillar. Legacy systems have to be adapted in order to communicate with MBS.

Note: The interface for handover to and from a legacy system (see also chapter 3.1.1) is out of scope for R2DATO Phase 1 and will thus be excluded in the following subchapters. The scope of R2DATO Phase 2 is not yet specified.

### 5.2 SYSTEM OPERATING CONDITIONS AND CONSTRAINTS

The following operating constraints apply to MBS:

Operation with national ATP is not possible

- No light signalling is supported (with the potential exception of transition areas).

There are several operating conditions that apply to MBS:

MBS supports ETCS Level 2. Flexible migration of fleets concerning the ETCS equipment have to be considered, e.g., handling of different ETCS versions, functions and non-equipped trains.

Trains that deliver their train integrity and safe train length information to MBS as well as trains that do not send this information have to be supported.

- The aim is a minimum or no manual interaction between driver and signaller.

---

All movements inside the AoC of MBS are supervised. Furthermore, the logical handling of all movements is the same, meaning that there is no distinction between shunting routes and train routes anymore. The setting and protection of any kind of train/vehicle movement (scheduled or not) is executed with the same set of functions that only change parameters according to the intended movement on the track. However, this does not mean, that the operational process of shunting (e.g., in the mode SH or SM) will not be necessary or is planned to be eliminated. Only the technical implementation in MBS is referred to in this operational condition.

MBS is applicable for different types of railways lines (regional, low density, urban, main line, high speed).

The loading and activation of Domain Data to MBS is possible during MBS' runtime. Thus, MBS shall be independent from Domain Data update and change lifecycles.

### 5.3 SYSTEM MAINTENANCE CONDITIONS

The maintenance strategy provides the use of IT deployment strategies like continuous integration based on reliable automatic configuration and test procedures. This enables a faster adaptation of the infrastructure to operational needs than today. This includes the update of infrastructure data, e.g., topology data update without restarting MBS, as well as other configuration data. MBS should support the development of easily maintainable solutions e.g., with a feasible degree of modularity, thus reducing the maintenance effort for the staff e.g., changing the configuration of the system, installing updates, etc.

Note: The physical aspects of maintenance are out of scope for now, thus e.g., changing of hardware, cabling etc. is not considered.

Regarding the interface with actor Maintenance Staff, the necessity of an HMI has to be analysed further during system specification. This interface will exclude some maintenance functionalities like the activation of Domain Data as this is coordinated by the interfacing system Digital Register.

### 5.4 LOGISTIC SUPPORT CONSIDERATIONS

Physical architecture of the system is out of scope. Thus, no considerations about logistic support.

### 5.5 REVIEW OF PAST EXPERIENCE DATA FOR SIMILAR SYSTEMS

The general experience with a substantial subset of today's interlockings (IXL) is that there is no standardised interface to it which causes a lot of project engineering and development effort in interfacing systems. Oftentimes, the interfacing systems, like for example the control system, needs detailed knowledge about the behaviour of the IXL to properly command it. Every change of the IXL's baseline leads to changes of all interfacing systems as they have to support new/changed functionalities. High coordination effort to align the rollout and migration of all the affected railway systems, e.g., control system, Radio Block Centre (RBC), TMS and track worker safety systems, is needed. This is not only costly and prone to compatibility issues, but also significantly prolongs project durations.

A more specific example is the operation with ETCS. Due to the fact that the OPE TSI has a lot of non-harmonised rules, major differences remain in the implementation of the same operational processes in different countries. This is due to the freedom of choice and application of the trackside

---

(e.g., whether or not to "stop if in SR" balise, whether or not to apply packet 88, whether or not to apply reference balises, the start of mission procedure used). Additionally, differences arise from the use of different class B systems. But even if the application of the TSI is chosen (i.e., ETCS), there appear to be differences in the implementation and rules of operational processes. Also, this "loophole" to use NTC/STM when implementing ETCS ultimately delays the rollout and operation with ETCS. An example for this can be seen in the complex integration projects, e.g., for Abellio with 3 national ATPs and ETCS integrated on-board.

The integration of ETCS also depends on the used interlocking. For example, when entering an occupied track. Today, this is sometimes done in mode OS, sometimes done in SR or even in SH. In most cases, the difference is due to differences in the functionality of the interlocking which is used. Also, with relatively modern interlockings, which can support OS, SR or SH is implemented nonetheless.

Note: EULYNX [2] is excluded from consideration here because there are no implementations of this standard yet in operation.

### 5.6 INFLUENCE ON OPERATIONAL AND MAINTENANCE PERSONNEL, PASSENGERS AND PUBLIC

There is no influence on passengers and public expected besides safety by design.

As the new system MBS needs to be maintained throughout its lifecycle, new maintenance procedures and protocols are to be expected. From a hardware perspective, MBS components shall be able to run on a new safe computing platform (standardised by the System Pillar). The deployment on existing legacy hardware through e.g., emulation, can be analysed in a later specification level.

The MBS is expected to influence the operational procedures and conditions at least regarding the available automated assistance for operational personnel, new procedures for Level 2 operation in compliance with the ETCS Specifications  $ [1] $  and for entering an occupied track. Therefore, it has to be specified how MBS is supporting and managing operation and what is needed on the operational side of things. The operational procedures to handle MBS shall not include business “logic” but be based on necessary issues, not on national particularities/sensitivities.

Note: The definition of the exact operational procedures is out of scope, because this is within the scope of operational harmonisation in the System Pillar.

In order to use the MBS, training as well as operating manuals have to be provided to the railway staff.

### 5.7 DESCRIPTION OF OPERATING PROCEDURES

The operation of MBS requires operating procedures as well as maintenance procedures. Similar to EULYNX, there is an "operating mode" and "maintenance mode" of the system envisioned. If the system enters "maintenance mode", procedures for system installation, loading of new software data and configurations can proceed. The maintenance mode as well as the start of the procedures can be activated either manually by e.g., actor Maintenance Staff, or automatically by an external actor e.g., Plan Execution (PE) for planned maintenance. The transition to the "operating mode" of the system is only possible after a successful system test activating the changes made to the system during maintenance. Either MBS does the system test autonomously or/and in interaction with local staff.

---

that ensures that no one is endangered by the system activation e.g., by checking and confirming that no obstacles are in the area affected by the system update.

### 5.8 MODES OF OPERATION

Modes of operation in the following three major categories according to the TSI OPE  $ [5] $  are covered by the system:

- Normal operation

- Degraded operation

- Handling of emergency situations

Several use cases that are part of the listed modes of operation have to be handled by the MBS.

Firstly, the downgrade from normal situations to degraded situations have to be covered by MBS. For this consideration, degraded situations can be defined as “the system with limited functionality”. Then, the recovery procedure to normal operation needs to be handled by MBS, with or without interaction with interfacing systems.

Furthermore, the recovery from emergency situations to operation in degraded situations has to be handled by MBS. For example, the loss of train integrity monitoring on-board might trigger an emergency reaction first. After the train integrity is assessed once more, the train can continue in degraded situations with localisation by Trackside Train Detection (TTD).

As a general principle, the handling of degraded situation shall be automated as much as possible. This means that the operator shall intervene when a degraded situation can't be handled by rules (interplay between PE and MBS). In order to ensure safety, the human ability to judge and assess a situation is needed either by technical means or through legal obligation.

---

## 6 ASSUMPTIONS AND EXISTING SAFETY MEASURES

6.1 ASSUMPTIONS


[
  {
    "This chapter contains assumptions related to external systems or actors interacting with the Moving Block System (MBS) or related to input from external systems that are not covered somewhere else yet (e.g., in the corresponding standard).": "Assumption"
  },
  {
    "This chapter contains assumptions related to external systems or actors interacting with the Moving Block System (MBS) or related to input from external systems that are not covered somewhere else yet (e.g., in the corresponding standard).": "Virtual Coupling is out of scope.Justification: Virtual Coupling is not part of the Grant Agreement of WP13."
  },
  {
    "This chapter contains assumptions related to external systems or actors interacting with the Moving Block System (MBS) or related to input from external systems that are not covered somewhere else yet (e.g., in the corresponding standard).": "If a train is equipped with a TIMS and this trains confirms its train integrity, then the MBS can trust the train for:- Train Length - Received in Validated Train Data as L_TRAIN, which is the maximum length of the train in rear of the engine, counted from the front end of the engine considering the active cab, and considering the coupling play and/or any other uncertainties in the length information.- Train Position Reports - including Q_LENGTH, L_TRAININTThis is consistent with the approach in the ETCS Specifications [1]:- On-Board can only confirm Train Integrity to Trackside if the train length can be treated as SIL4.Justification: This means that the train length and information from the train position reports (e.g., train integrity information) can be used by the MBS to release track behind the train, and for length calculations during splitting and joining.Note: This implies that the MBS won&#x27;t trust the train for the Train Length if the train has never confirmed its train integrity (e.g. because the train is not equipped with a TIMS)"
  },
  {
    "This chapter contains assumptions related to external systems or actors interacting with the Moving Block System (MBS) or related to input from external systems that are not covered somewhere else yet (e.g., in the corresponding standard).": "In case of joining or splitting of trains, this causes the external Train Integrity Monitoring System (TIMS) devices (in each train) to report loss of train integrity.As long as MBS has not acknowledged the new train data (incl. train length), the train integrity is not confirmed again by the train(s).Justification: The safe train length is not valid anymore when trains physically join or split."
  }
]

[
  {
    "Document status": "Description"
  },
  {
    "Document status": "First issueChapter 8 to 10 are still draft (not to be reviewed)"
  },
  {
    "Document status": "Second issue for Release 1Comments on first issue answeredChapters 8 to 10 completed and available for review"
  },
  {
    "Document status": "First issue for Release 2Comments on document revision 2 answered"
  },
  {
    "Document status": "Last issue for Release 2 with answers to the Reviewer&#x27;s comments.Scope of work for Release 3 anticipated in chapter 2"
  },
  {
    "Document status": "First intermediate issue for Release 3.Chapter 6.11 Functional requirements for flank protection (Risk Path) is work in progress and should not be reviewed."
  },
  {
    "Document status": "Second issue for Release 3."
  },
  {
    "Document status": "Update according to comments received on Revision 05.Chapter 5.10 and 6.11 updated for Flank Protection.Flank protection is now ready for review.Chapter 5.15 and related functions revisited for cooperative MP request."
  },
  {
    "Document status": "Last issue for Release 3 with answers to the Reviewer&#x27;s comments."
  },
  {
    "Document status": "Updated according to TMT review."
  },
  {
    "Document status": "Names of authors and reviewers introduced"
  },
  {
    "Document status": "Update according to Review Sheet consolidated D13.1 (ERA + external reviewers)"
  },
  {
    "Document status": "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme"
  },
  {
    "Document status": "Dissemination Level"
  },
  {
    "Document status": "X"
  },
  {
    "Document status": "Sensitiv - limited under the conditions of the Grant Agreement"
  },
  {
    "Document status": "Details of Contribution"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Area of Control"
  },
  {
    "Document status": "Control, Command and Signalling"
  },
  {
    "Document status": "Drive Protection Section"
  },
  {
    "Document status": "Drive Protection Section Group"
  },
  {
    "Document status": "Digital Register"
  },
  {
    "Document status": "Europe&#x27;s Rail Joint Undertaking"
  },
  {
    "Document status": "Moving Block System"
  },
  {
    "Document status": "Movement Permission"
  },
  {
    "Document status": "Min(imum) Safe Front End"
  },
  {
    "Document status": "Max(imum) Safe Front End"
  },
  {
    "Document status": "Min(imum) Safe Rear End"
  },
  {
    "Document status": "Max(imum) Safe Rear End"
  },
  {
    "Document status": "Plan Execution"
  },
  {
    "Document status": "Rail to Digital automated up to autonomous train operation"
  },
  {
    "Document status": "Risk Buffer"
  },
  {
    "Document status": "Reference CCS Architecture"
  },
  {
    "Document status": "Risk Path"
  },
  {
    "Document status": "Standard Communication Interface (EULYNX)"
  },
  {
    "Document status": "Standard Communication Interface - Command"
  },
  {
    "Document status": "Standard Communication Interface - Point"
  },
  {
    "Document status": "Standard Communication Interface - Train Detection System"
  },
  {
    "Document status": "Shift2Rail"
  },
  {
    "Document status": "Trackside Asset"
  },
  {
    "Document status": "Trackside Asset Control and Supervision"
  },
  {
    "Document status": "Transversal CCS (Control Command and Signalling)"
  },
  {
    "Document status": "Train Detection System"
  },
  {
    "Document status": "Track Edge Point"
  },
  {
    "Document status": "Track Edge Section"
  },
  {
    "Document status": "Train Integrity Monitoring System"
  },
  {
    "Document status": "Definition"
  },
  {
    "Document status": "Allocation Sections express gauge clearance conflicts between different tracks.For example, Allocation Sections are associated to the representation of switchable Track Assets and further track connections like diamond crossings.The Allocation Sections are used in terms of granting a Movement Permission request as condition for clearance in a certain area.See also /FlankProtection/"
  },
  {
    "Document status": "The Area of Control is the topologically limited extent used here for defining the technical and operational responsibility of one instance of MBS."
  },
  {
    "Document status": "The Domain Data refers to use case specific configuration data for the MBS to define the specific application. These can be broadly classified as Map Data, Segment Profiles, and Parameter Data. As a part of configuration process, the MBS needs Domain Data. Potential updates of Domain Data will be realised by a centralised provisioning process incl. synchronous activation of the new data version.Source: /SD1DM/"
  },
  {
    "Document status": "A Domain Object is an abstract object for which a Domain (e.g. Moving Block System) has the main responsibility. There might be other Domains who are consumers of this object as well. In general, it is based on or linked to the Domain Data."
  },
  {
    "Document status": "A Drive Protection Section is a linear contiguous stretch of track with a driveability (passage possible yes/no) state.A Drive Protection Section (DPS) represents a Track Edge Section that can be brought to different driveability states to ensure the driveability or safety of a track route. As such, it is an abstraction for any location on the railway network that may adopt different states due to Switchable Trackside Asset (e.g. points or level crossings).Source: RCA"
  },
  {
    "Document status": "MBS Operational State is the collection of all of Domain Objects instantiated by the MBS to manage its operations and supervise the train movements.This includes:  · Train Objects,  · Unresolved Trackbound Objects,  · Trackside Asset Objects,  · Movement Permission,  · Etc..."
  },
  {
    "Document status": "MBS is operational when it is in a state allowing the MBS to perform its fundamental function ensuring safe train movement and preventing railway accidents, incidents... From now on, communication sessions to the external systems (e.g., OBU, PE, etc.) can be established and supervised."
  },
  {
    "Document status": "The Movement Permission defines the part of the track that is reserved for the movement of a train.It includes:- Movement Permission Extent- Risk Buffer- Risk Path- Requested Maximum Speed- ETCS Movement Mode- List of DPS Groups that must not be used as flank protection measure"
  },
  {
    "Document status": "A Movement Permission Extent is a linear contiguous stretch of track that is reserved for the movement of a train. The Movement Permission is translated to an authorisation (e.g. Movement Authority) according to the /ETCS/ - SUBSET-026 that is transmitted to the train.The Movement Permission Extent is part of the Movement Permission.Source: RCA"
  },
  {
    "Document status": "A Non-switchable Trackside Asset is a Trackside Asset which provides information to the MBS (e.g. Trackside Train Detection) but cannot be controlled to a particular state."
  },
  {
    "Document status": "The position information contained in a Train Position Report (Position Report or SoM Position Report with status valid) can be considered as ambiguous in case MBS is not able to safely locate the train within the track layout. Since the Train Position Report only contains a (directed) distance to the LRBG, MBS might not be able to locate the train on the correct position in the track layout, e.g. in case of a zig-zag movement"
  },
  {
    "Document status": "(see Hazard 0003 in /ETCS/ - SUBSET-113) or when there is a facing pair of points between the LRBG and the position of the train."
  },
  {
    "Document status": "The Risk Buffer is a linear contiguous stretch of track that serves as the overrun protection and in the event of a rollback of a chased train. It is part of a Movement Permission.A Risk Buffer exists if there is a Danger Point or a safe margin (project specific) greater than zero.Source: RCA"
  },
  {
    "Document status": "A Risk Path is one potential path (a linear contiguous stretch of track) by which a non-permitted vehicle movement could result in a flank collision with a vehicle moving along the Movement Permission Extent.A Movement Permission can contain zero or more Risk Paths.Source: RCA"
  },
  {
    "Document status": "A Switchable Trackside Asset is a Trackside Asset which enables (e.g. points, derailers, movable bridges, gates) or allows (e.g. light signals at border, level crossings) the continuation of movement beyond this asset when this latter is controlled to particular state."
  },
  {
    "Document status": "See entry for Domain Data"
  },
  {
    "Document status": "Track Edge is a linear object that defines an uninterrupted stretch of a railway track without divergence or convergence. A Track Edge is defined along the centre line of the 2D or 3D track alignment and has a finite length.The Track Edges have an implicit direction (from start to end).The start/end of Track Edge shall correspond to the location of a simple point, or any form of end of track.Source: RCA, /SD1DM/"
  },
  {
    "Document status": "A Track Edge Point is a spot location on a Track Edge.Example usage: balise locationSource: RCA, /SD1DM/"
  },
  {
    "Document status": "A Track Edge Section is a linear extent between two Track Edge Points on (the same) Track Edge and can be directed.Example usage: Track properties like gradient, SSP, DPSSource: RCA, /SD1DM/"
  },
  {
    "Document status": "Trackside Assets are elements on or near the track which are used to monitor (using sensors) and/or control (using actuators) the movement of vehicles through the railway network. They can be switchable or non-switchable and are controlled by the actors Trackside Asset Control and Supervision (TACS). See also Switchable Trackside Asset and Non-switchable Trackside Asset definition."
  },
  {
    "Document status": "The Trackside Asset Control and Supervision (TACS) is a subsystem supervising and controlling Trackside Assets."
  },
  {
    "Document status": "Trackside Train Detection is a system which determines the occupancy status of TTD sections. TTD section may be a Track Circuit or an Axle Counting system. EULYNX synonym: Track Vacancy Proving Section (TVPS)"
  },
  {
    "Document status": "Train Location is the MBS interpretation of the unambiguous location of the train, based on Train Position Reports, Validated Train Data and other inputs if available, e.g. TTD. Train Location is a linear contiguous stretch of track that has a front and a rear. X2R5 source: Train Location RCA source: rMOB extent"
  },
  {
    "Document status": "Train Object is the object needed by the MBS to manage the connected trains currently performing their mission. Note: This Train Object could nevertheless correspond to a train not (yet) localised by MBS. If a Train Object is referenced as a geometric extent, the extent is the extent of the Train Location. RCA source: (rMOB)"
  },
  {
    "Document status": "The term Train Position Report refers to either Position Report packet (packet number 0) or Position Report based on two balise groups packet (packet number 1) according to /ETCS/ - SUBSET-026, chapter 7."
  },
  {
    "Document status": "Unresolved Trackbound Object is the object needed by the MBS to manage a contiguous track area where track vacancy is not proven and cannot be linked to any connected train (Train Object). RCA source: uMOB X2R5 source: Unknown Track Status Area (partly)"
  },
  {
    "Document status": "it later for the specification of the System Requirements. A justification is provided for each of the consolidated concepts."
  },
  {
    "Document status": "Chapter 5"
  },
  {
    "Document status": "Chapter 6"
  },
  {
    "Document status": "Chapter 7"
  },
  {
    "Document status": "Chapter(s) in System Specification"
  },
  {
    "Document status": "5.6 SysC: Start communication with one TACS"
  },
  {
    "Document status": "5.7 SysC: Respond to initiation of communication session by OBU5.14 SysC: Terminate Train Mission"
  },
  {
    "Document status": "5.8 SysC: Control Switchable Trackside Assets"
  },
  {
    "Document status": "5.12 SysC: Start of Train5.10 SysC: Update MBS Operational State5.14 SysC: Terminate Train Mission"
  },
  {
    "Document status": "5.13 SysC: Provide MA to Train"
  },
  {
    "Document status": "5.13 SysC: Provide MA to Train"
  },
  {
    "Document status": "Out of scope for current releases"
  },
  {
    "Document status": "5.10 SysC: Update MBS Operational State5.11 SysC: Report MBS Operational State"
  },
  {
    "Document status": "5.2 SysC: Preload Topology Data5.3 SysC: Approve Topology Data activation5.4 SysC: Activate Topology Data"
  },
  {
    "Document status": "Out of scope for current releases"
  },
  {
    "Document status": "Different scenarios outlining the MPS behind."
  },
  {
    "Document status": "This capability allows to start and maintain MBS communication to actors."
  },
  {
    "Document status": "MBS is operational"
  },
  {
    "Document status": "None"
  },
  {
    "Document status": "The Moving Block System has been started and is operational."
  },
  {
    "Document status": "The Moving Block System is not operational."
  },
  {
    "Document status": "DR, PE, OBU, TACS"
  },
  {
    "Document status": "MBS is started"
  },
  {
    "Document status": "1. MBS supervises the communication to actors (This is done in a continuous loop.)"
  },
  {
    "Document status": "None"
  },
  {
    "Document status": "Only for release 2.4:1. If loading or checking the Topology Data fails, the start procedure terminates."
  },
  {
    "Document status": "MBS could either be started by an external event or automatically when recovering from a failure for example.The communication patterns raise events &lt;actor&gt;CommEstablished and &lt;actor&gt;CommLost for every actor &lt;actor&gt;(UML: lost message). Other capabilities can react (UML: found message) to these events and react accordingly (e.g. initialising a safe state)."
  }
]

---

[
  {
    "Description": "Goal",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "MBS has loaded (initial or new version of) Topology Data and related Domain Objects"
  },
  {
    "Description": "Precondition(s)",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "No Topology Data available (no Topology Data loaded) at startup"
  },
  {
    "Description": "Postcondition(s) (Success)",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "Up to release 4: MBS has loaded, approved, and activated Topology Data MBS is operational"
  },
  {
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "From release 5 on (more granular steps so this capability only does preloading): MBS has loaded Topology Data MBS is operational"
  },
  {
    "Description": "Postcondition(s) (Failure)",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "MBS state related to Topology Data has not changed MBS is not operational"
  },
  {
    "Description": "Involved actor(s)",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "DR"
  },
  {
    "Description": "Trigger(s)",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "1. MBS starts up2. (For further release) MBS receives the Topology Data from DR"
  },
  {
    "Description": "Main Sequence",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "Up to release 4:1. MBS establishes a communication session with DR.2. MBS requests Topology Data from DR3. MBS receives Topology Data and activates them"
  },
  {
    "Description": "Main Sequence",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "From release 5 on:1. MBS establishes a communication session with DR.2. MBS requests Topology Data from DR3. MBS receives Topology Data and pre-loads them.4. MBS approves the activation of Topology Data5. MBS activates Topology Data"
  },
  {
    "Description": "Alternate Sequence",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "From release 5 on:At any point in time, DR can send Topology Data to MBS (continues then from 3. on)"
  },
  {
    "Description": "Failure Sequence",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "4. MBS rejects the approval when there are e.g. conflicting Movement Permissions (for further release)"
  },
  {
    "Description": "Comments",
    "This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects": "Before release 5, there are the following restrictions  ·The scope of Topology Data is the full Area of Control (so no partial update)  ·Topology Data are loaded only once at startup and remain unchanged (so no update during run-time)  ·It is assumed that neither connecting to DR, nor loading the Topology Data from there fails (exclusion of unhappy paths)The scenario will thus widen in a later release: data are not only loaded and immediately activated, but pre-loaded, approved, and activated. In order to save work already knowing the future state, the function to load Topology Data is already named ‘preload’ and not only ‘load’. The term ‘preloaded’ can be read as ‘loaded’."
  }
]

---

#### 5.2.1 Scenario: Preload Topology Data

[
  {
    "Description": "Goal",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "MBS has distributed its MBS Operational State to PE."
  },
  {
    "Description": "Precondition(s)",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "MBS is operational"
  },
  {
    "Description": "Postcondition(s) (Success)",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "The MBS Operational State is synchronised with PE"
  },
  {
    "Description": "Postcondition(s) (Failure)",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "No communication session to PE"
  },
  {
    "Description": "Involved actor(s)",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "PE"
  },
  {
    "Description": "Trigger(s)",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "Event PECommEstablished"
  },
  {
    "Description": "Main Sequence",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "1. MBS distributes its MBS Operational State to PE."
  },
  {
    "Description": "Alternate Sequence",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "None"
  },
  {
    "Description": "Failure Sequence",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "1. MBS cannot distribute the MBS Operational State to PE. MBS closes the communication session"
  },
  {
    "Description": "Comments",
    "This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.": "This capability may be triggered after start of MBS or when the communication session to the PE needs to be re-established for any reason. When - in failure case - the communication session is closed, the capability ‘Start and Maintain MBS’ will re-establish the session and this triggers this capability again."
  }
]

---

#### 5.5.1 Scenario: Respond to initiation of communication session by PE

[
  {
    "Description": "Goal",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "Domain Objects of MBS are synchronised with TACS and subsequently MBS has distributed the corresponding Domain Object state to PE."
  },
  {
    "Description": "Precondition(s)",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "MBS is operational)"
  },
  {
    "Description": "Postcondition(s) (Success)",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "MBS has distributed the corresponding Domain Object state to PE."
  },
  {
    "Description": "Postcondition(s) (Failure)",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "No communication session to TACS"
  },
  {
    "Description": "Involved actor(s)",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "PE, TACS"
  },
  {
    "Description": "Trigger(s)",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "Event TACSCommEstablished(TACSId)"
  },
  {
    "Description": "Main Sequence",
    "This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.\nMBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)": "1. MBS synchronises with TACS."
  }
]

---

[
  {
    "2. MBS updates and distributes the corresponding Domain Objects state to PE (according to the capability &#x27;Update MBS Operational State&#x27;)": "None"
  },
  {
    "2. MBS updates and distributes the corresponding Domain Objects state to PE (according to the capability &#x27;Update MBS Operational State&#x27;)": "1. The synchronisation with TACS failed MBS closes the communication session"
  },
  {
    "2. MBS updates and distributes the corresponding Domain Objects state to PE (according to the capability &#x27;Update MBS Operational State&#x27;)": "This capability may be triggered after start of MBS or when the communication session to a TACS was re-established for any reason. When - in failure case - the communication session is closed, the capability &#x27;Start and Maintain MBS&#x27; will re-establish the session and trigger this capability again."
  }
]

[
  {
    "Description": "Goal",
    "This capability manages the establishment of the communication session between the MBS and an OBU considering the requirements of\n• chapter 3.5.3 (Establishing a communication session) of /ETCS/\n- SUBSET-026.\n• /ETCS/ - SUBSET-037.": "A communication session with an OBU is established."
  }
]

---

[
  {
    "Precondition(s)": "Postcondition(s)(Success)",
    "MBS is operational": "A communication session with an OBU was established."
  },
  {
    "Precondition(s)": "Postcondition(s)(Failure)",
    "MBS is operational": "A communication session with an OBU could not be established."
  },
  {
    "Precondition(s)": "Involved actor(s)",
    "MBS is operational": "OBU, PE"
  },
  {
    "Precondition(s)": "Trigger(s)",
    "MBS is operational": "An OBU requests to set-up a safe radio connection with the MBS."
  },
  {
    "Precondition(s)": "Main Sequence",
    "MBS is operational": "1. MBS sets-up a safe radio connection and communication session according to /ETCS/ considering using System Version 2.1. MBS creates a Train Object for this OBU and subsequently informs PE about this through the capability &#x27;Update MBS Operational State&#x27;."
  },
  {
    "Precondition(s)": "Alternate Sequence",
    "MBS is operational": "None."
  },
  {
    "Precondition(s)": "Failure Sequence",
    "MBS is operational": "1. If a condition to establish a safe connection or communication session is not fulfilled, then MBS ends the procedure to set-up a safe radio connection and communication session by terminating the safe connection, if any."
  },
  {
    "Precondition(s)": "Comments",
    "MBS is operational": "The failure sequence may be triggered e.g. in the following case:  ·There is no key (KMAC) available within MBS for this OBU."
  }
]

---

[
  {
    "Description": "Goal",
    "This capability allows PE to change the state of a Switchable Trackside Asset by sending a corresponding TA State Request to MBS. MBS has to verify if the request is valid. If it is valid, MBS carries it out by sending the corresponding command to the TACS related to the Switchable Trackside Asset.": "Due to a request from PE, a Switchable Trackside Asset is commanded to change its state by sending a command to its TACS."
  }
]

---

[
  {
    "Preconditions": "Postcondition (Success)",
    "MBS is operational 5.1.2": "Granting of request is indicated to PE."
  },
  {
    "Preconditions": "Postcondition (Success)",
    "MBS is operational 5.1.2": "Command for changing its state is sent to TACS."
  },
  {
    "Preconditions": "Postcondition (Failure)",
    "MBS is operational 5.1.2": "Rejecting of a valid request from PE. Command for changing its state is not sent to TACS."
  },
  {
    "Preconditions": "Involved Actors",
    "MBS is operational 5.1.2": "PE, TACS"
  },
  {
    "Preconditions": "Trigger",
    "MBS is operational 5.1.2": "Request from PE to change the position of a Switchable Trackside Asset via its TACS."
  },
  {
    "Preconditions": "Main Sequence",
    "MBS is operational 5.1.2": "A valid request is granted and carried out by MBS (see: Scenario: Control Switchable Trackside Assets) and MBS informs PE about granting this request"
  },
  {
    "Preconditions": "Alternate Sequence"
  },
  {
    "Preconditions": "Failure Sequence",
    "MBS is operational 5.1.2": "An invalid request is rejected by MBS (see: Scenario: Control Switchable Trackside Assets) and MBS informs PE about rejecting this request."
  },
  {
    "Preconditions": "Comments",
    "MBS is operational 5.1.2": "None"
  }
]

#### 5.8.1 Scenario: Control Switchable Trackside Assets

The figure below contains the main sequence and the failure sequence of the SysC Control Switchable Trackside Asset.

When the MBS receives a TA State Request, it performs the safety checks (Function: Authorise TA State Request) for the request.

If the safety checks are successful, MBS responds to PE the granting of the request and translates the request to a TACS command (Function: Translate TA State Request to TACS Command). The TACS command is then sent to the related TACS (Function: Send TACS Command).

If the safety checks fail, MBS responds to PE system the rejecting of the request and performs no further actions for the request.

---

[
  {
    "Description": "Goal",
    "This capability updates the MBS Operational State.": "Update the state of MBS Operational State"
  },
  {
    "Description": "Precondition",
    "This capability updates the MBS Operational State.": "MBS is operational)"
  },
  {
    "Description": "Postcondition (Success)",
    "This capability updates the MBS Operational State.": "MBS has updated its MBS Operational State"
  },
  {
    "Description": "Postcondition (Failure)",
    "This capability updates the MBS Operational State.": "None (no failure)"
  },
  {
    "Description": "Involved Actors",
    "This capability updates the MBS Operational State.": "• TACS• OBU• PE"
  },
  {
    "Description": "Trigger",
    "This capability updates the MBS Operational State.": "• Any change of MBS Operational State is detected (inexhaustive list):"
  }
]

---

[
  {
    "• MBS receives a state update report from the TACS• MBS detects that there is no communication with TACS anymore• MBS receives a position report from OBU• MBS receives validated train data from OBU• The communication between MBS and an OBU is established• MBS detects that there is no communication with OBU anymore": "Scenario 1: Update MBS Operational State when TA state report is receivedScenario 2: Update MBS Operational State when a train position report or validated train data are received"
  },
  {
    "• MBS receives a state update report from the TACS• MBS detects that there is no communication with TACS anymore• MBS receives a position report from OBU• MBS receives validated train data from OBU• The communication between MBS and an OBU is established• MBS detects that there is no communication with OBU anymore": "Scenario 3: Update MBS Operational State when no communication with TACS anymoreScenario 4: Update MBS Operational State when no communication with OBU anymore"
  },
  {
    "• MBS receives a state update report from the TACS• MBS detects that there is no communication with TACS anymore• MBS receives a position report from OBU• MBS receives validated train data from OBU• The communication between MBS and an OBU is established• MBS detects that there is no communication with OBU anymore": "None"
  },
  {
    "• MBS receives a state update report from the TACS• MBS detects that there is no communication with TACS anymore• MBS receives a position report from OBU• MBS receives validated train data from OBU• The communication between MBS and an OBU is established• MBS detects that there is no communication with OBU anymore": "None"
  }
]

#### 5.10.1 Scenario 1: Update MBS Operational state when TA state report is received

This scenario covers the nominal scenario (all communications are established), when a TA state report is received from a TACS.

Train Location or Unresolved Trackbound Object are updated when a TTD section status changes. Risk Path, part of the Movement Permission, may be updated when a Point status changes.

---

[
  {
    "Description": "Goal",
    "When triggered, this capability reports the MBS Operational State.": "Report the state of MBS Operational State"
  },
  {
    "Description": "Precondition",
    "When triggered, this capability reports the MBS Operational State.": "MBS is operational 5.1.2"
  },
  {
    "Description": "Postcondition (Success)",
    "When triggered, this capability reports the MBS Operational State.": "PE has received the MBS Operational State for the given Domain Object Instance"
  },
  {
    "Description": "Postcondition (Failure)",
    "When triggered, this capability reports the MBS Operational State.": "None (no failure)"
  },
  {
    "Description": "Involved Actors",
    "When triggered, this capability reports the MBS Operational State.": "• PE"
  },
  {
    "Description": "Trigger",
    "When triggered, this capability reports the MBS Operational State.": "Triggered for a given Domain Object Instance by other capabilities"
  },
  {
    "Description": "Main Sequence",
    "When triggered, this capability reports the MBS Operational State.": "Scenario: Report of MBS Operational State"
  },
  {
    "Description": "Alternate Sequence"
  },
  {
    "Description": "Failure Sequence",
    "When triggered, this capability reports the MBS Operational State.": "None"
  },
  {
    "Description": "Comments",
    "When triggered, this capability reports the MBS Operational State.": "None"
  }
]

---

#### 5.11.1 Scenario: Report of MBS Operational State when triggered

[
  {
    "Description": "Goal",
    "Start of Train": "A train successfully has started up according to /ETCS/ and MBS has subsequently sent an Authorisation Requested message to PE."
  },
  {
    "Description": "Precondition(s)",
    "Start of Train": "MBS is operational 5.1.2"
  },
  {
    "Description": "Postcondition(s) (Success)",
    "Start of Train": "MBS has sent an Authorisation Requested message to PE after receiving a first MA request during the Start of Mission procedure."
  },
  {
    "Description": "Postcondition(s) (Failure)",
    "Start of Train": "None"
  },
  {
    "Description": "Involved actor(s)",
    "Start of Train": "OBU, PE"
  },
  {
    "Description": "Trigger(s)",
    "Start of Train": "MBS receives a SoM Position Report message from an OBU."
  },
  {
    "Description": "Main Sequence",
    "Start of Train": "1. MBS determines that the position is valid and unambiguous.\nMBS updates the Train Object."
  },
  {
    "Description": "Main Sequence",
    "Start of Train": "2. MBS receives Train Data, Train Running Number from OBU and subsequently acknowledges the train data to the OBU.\nMBS updates the Train Object."
  },
  {
    "Description": "Main Sequence",
    "Start of Train": "3. MBS receives an MA Request from OBU.\nMBS provides an Authorisation Requested message to PE."
  },
  {
    "Description": "Alternate Sequence",
    "Start of Train": "1.a) MBS receives a SoM Position Report with invalid / unknown position.\nMBS updates the Train Object indicating that the position is invalid / unknown and sends Train Accepted to OBU. Afterwards the flow continues with step 2 of the main sequence."
  }
]

---

[
  {
    "1.b) MBS receives a SoM Position Report with a valid position, but the position is ambiguous.MBS updates the Train Object indicating that the position is ambiguous and continues with step 2 of the main sequence.": "None"
  },
  {
    "1.b) MBS receives a SoM Position Report with a valid position, but the position is ambiguous.MBS updates the Train Object indicating that the position is ambiguous and continues with step 2 of the main sequence.": "Please consider that mode change to SH is currently excluded by the scope of the document and thus there is no failure sequence aborting this capability in such case. The same also applies for using the &#x27;Override&#x27; function.Additionally, it is also not foreseen yet to revalidate the train position (using the SoM Position Report Confirmed message) since this may depend on the operational procedures which are not available yet."
  }
]

#### 5.12.1 Scenario: Start of Train

Please consider that during this scenario after each Train Position Report (packet number 0 or packet number 1), respectively after receiving the SoM Position Report, MBS updates the Train Object by the capability "Update MBS Operational State" and reports this to the PE. This handling of Train Position Reports is not explicitly illustrated in the figure to limit the sequence diagram to the Start of Train capability.

During this scenario, after the acknowledgment of Train Data, it is possible (when the OBU is equipped with a TIMS) that the MBS receives the first Train Position Report with integrity confirmed. Then especially the extent of the Train Location using the confirmed rear end is updated.

---

[
  {
    "Description": "Goal",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "After receiving an MP request from PE, MBS checks all safety constraints, generates a Movement Permission for a dedicated train run and translates it into an Authorisation which is sent to the OBU."
  },
  {
    "Description": "Precondition",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "None"
  },
  {
    "Description": "Postcondition (Success)",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "Authorisation issued by MBS to the OBU corresponding to the Train Object; Movement Permission reported to PE."
  },
  {
    "Description": "Postcondition (Failure)",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "None"
  },
  {
    "Description": "Involved Actors",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "• OBU• PE"
  },
  {
    "Description": "Trigger",
    "This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.": "• MBS receives a Movement Permission Request"
  }
]

---

[
  {
    "Main Sequence": "Alternate Sequence",
    "When all checks are successful, MBS indicates this to PE, updates the Train Object with the Movement Permission and issues an Authorisation to OBU based on the Movement Permission Request received from PE.": "None"
  },
  {
    "Main Sequence": "Failure Sequence",
    "When all checks are successful, MBS indicates this to PE, updates the Train Object with the Movement Permission and issues an Authorisation to OBU based on the Movement Permission Request received from PE.": "When at least one check fails, MBS reports a Request Rejected to PE indicating the reason why the Movement Permission Request could not be granted."
  },
  {
    "Main Sequence": "Comments",
    "When all checks are successful, MBS indicates this to PE, updates the Train Object with the Movement Permission and issues an Authorisation to OBU based on the Movement Permission Request received from PE.": "•"
  }
]

#### 5.13.1 Scenario: Provide MA to Train

[
  {
    "Description": "Goal",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Terminate the mission of a given train"
  },
  {
    "Description": "Precondition",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Communication between the OBU and the MBS is established"
  },
  {
    "Description": "Postcondition (Success)",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Communication between the OBU and the MBS is terminated. Train Object is converted into Unresolved Trackbound Object"
  },
  {
    "Description": "Postcondition (Failure)"
  },
  {
    "Description": "Involved Actors",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "· OBU· PE"
  },
  {
    "Description": "Trigger",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "· A message triggering the order to terminate the communication session is received from OBU (see scenario 1)· Message “termination of communication session” is received from OBU (see scenario 2)· Communication with OBU is lost for more than Session Timeout (see scenario 3)"
  },
  {
    "Description": "Main Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Scenario 1: Train End of Mission"
  },
  {
    "Description": "Alternate Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Scenario 2: Termination of communication session by OBUScenario 3: end mission when no communication anymore with an OBU"
  },
  {
    "Description": "Failure Sequence"
  },
  {
    "Description": "Comments"
  },
  {
    "Description": "Description",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "The purpose of this capability is to perform a co-operative shortening of MA, applying the principles of /ETCS/ - SUBSET-026, chapter 3.8.6 (/ETCS/). This may be necessary for the operational scenarios “Joining” or to reschedule train movements."
  },
  {
    "Description": "Goal",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "After receiving a cooperative shortening request indicating that it is requested to cooperatively shorten the MA from PE, MBS checks all safety constraints and subsequently performs the cooperative shortening of MA with the OBU."
  },
  {
    "Description": "Precondition",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "None"
  },
  {
    "Description": "Postcondition (Success)",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "After the OBU has accepted the new MA and has informed MBS about this, the MBS has updated the Movement Permission and informs PE about the success of the cooperative shortening of MA procedure."
  },
  {
    "Description": "Postcondition (Failure)",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "Failure 1: After the OBU has rejected the new MA and has informed MBS about this, the MBS informs PE about the failure of the cooperative shortening of MA procedure. The previously received MA remains valid on-board. Failure 2: The MBS has rejected the Cooperative Shortening Request."
  },
  {
    "Description": "Involved Actors",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "• OBU\n• PE"
  },
  {
    "Description": "Trigger",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "• MBS receives a Cooperative Shortening Request from PE indicating that it is requested to co-operatively shorten the MA."
  },
  {
    "Description": "Main Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "1. When all checks are successful, then MBS indicates this to PE and subsequently sends a Request to Shorten MA message to the OBU based on the Cooperative Shortening Request received from PE."
  },
  {
    "Description": "Main Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "2. When MBS receives the Request to shorten MA is granted message from the OBU, then MBS indicates this to the PE. Subsequently the Train Object (including the Movement Permission) is updated and PE is also informed about that."
  },
  {
    "Description": "Alternate Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "None"
  },
  {
    "Description": "Failure Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "1.a) When at least one check is not successful, then the MBS indicates this to PE. The co-operative shortening of MA procedure is aborted."
  },
  {
    "Description": "Failure Sequence",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "2.a) When MBS receives the Request to shorten MA rejected message from the OBU, then MBS indicates this to PE. The co-operative shortening of MA procedure is finished."
  },
  {
    "Description": "Comments",
    "This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE": "None"
  }
]

[
  {
    "System Capability as listed in chapter 5": "5.1 SysC: Start and Maintain MBS",
    "Used function as listed in chapter 6": "6.19 SysF Supervise&lt;Actor&gt;Communication 6.20 SysF Establish&lt;Actor&gt;Communication"
  },
  {
    "System Capability as listed in chapter 5": "5.2 SysC: Preload Topology Data",
    "Used function as listed in chapter 6": "6.6 SysF Preload Topology Data"
  },
  {
    "System Capability as listed in chapter 5": "5.3 SysC: Approve Topology Data activation"
  },
  {
    "System Capability as listed in chapter 5": "5.4 SysC: Activate Topology Data"
  },
  {
    "System Capability as listed in chapter 5": "5.5 SysC: Respond to initiation of communication session by PE"
  },
  {
    "System Capability as listed in chapter 5": "5.6 SysC: Start communication with one TACS"
  },
  {
    "System Capability as listed in chapter 5": "5.7 SysC: Respond to initiation of communication session by OBU",
    "Used function as listed in chapter 6": "6.8 SysF Create Train Object"
  },
  {
    "System Capability as listed in chapter 5": "5.8 SysC: Control Switchable Trackside Assets",
    "Used function as listed in chapter 6": "6.2 SysF Authorise TA State Request 6.3 SysF Translate TA State request to TACS command 6.4 SysF Send TACS command"
  },
  {
    "System Capability as listed in chapter 5": "5.9 SysC: Shutdown MBS"
  },
  {
    "System Capability as listed in chapter 5": "5.10 SysC: Update MBS Operational State",
    "Used function as listed in chapter 6": "6.5 SysF Update Domain Object state 6.7 SysF Assign a safe value to a Domain Object 6.9 SysF Localise Train 6.10 SysF Manage Unresolved Trackbound Object 6.18 SysF Update Movement Permission"
  },
  {
    "System Capability as listed in chapter 5": "5.11 SysC: Report MBS Operational State",
    "Used function as listed in chapter 6": "6.1 SysF Report MBS Operational State"
  },
  {
    "System Capability as listed in chapter 5": "5.12 SysC: Start of Train",
    "Used function as listed in chapter 6": "6.9 SysF Localise Train 6.16 SysF Request Movement Permission"
  },
  {
    "System Capability as listed in chapter 5": "5.13 SysC: Provide MA to Train",
    "Used function as listed in chapter 6": "6.11 SysF Authorise MP Request6.13 SysF Translate MP Request to Movement Authority"
  },
  {
    "System Capability as listed in chapter 5": "5.14 SysC: Terminate Train Mission",
    "Used function as listed in chapter 6": "6.15 SysF Delete Train Object"
  },
  {
    "System Capability as listed in chapter 5": "5.15 SysC: Revoke MA cooperatively by PE",
    "Used function as listed in chapter 6": "6.12 Authorise Cooperative Shortening Request6.14 SysF Translate Cooperative Shortening Request to Request to Shorten MA6.18 SysF Update Movement Permission"
  },
  {
    "System Capability as listed in chapter 5": "Component",
    "Used function as listed in chapter 6": "Description"
  },
  {
    "System Capability as listed in chapter 5": "left",
    "Used function as listed in chapter 6": "Movement Permission Extent"
  },
  {
    "System Capability as listed in chapter 5": "right",
    "Used function as listed in chapter 6": "Risk Buffer"
  },
  {
    "System Capability as listed in chapter 5": "left",
    "Used function as listed in chapter 6": "Drive Protection Section"
  },
  {
    "System Capability as listed in chapter 5": "right",
    "Used function as listed in chapter 6": "(FULL or NONE)"
  },
  {
    "System Capability as listed in chapter 5": "REQ-0029",
    "Used function as listed in chapter 6": "FOR FURTHER RELEASE"
  },
  {
    "System Capability as listed in chapter 5": "The MBS shall utilise valid Stored Information to enable faster initialisation.",
    "Used function as listed in chapter 6": "The MBS shall utilise valid Stored Information to enable faster initialisation."
  },
  {
    "System Capability as listed in chapter 5": "Rationale:",
    "Used function as listed in chapter 6": "Rationale:"
  },
  {
    "System Capability as listed in chapter 5": "Historic information on the state of the railway from before the MBS was restarted can enhance the Initialisation process.",
    "Used function as listed in chapter 6": "Historic information on the state of the railway from before the MBS was restarted can enhance the Initialisation process."
  },
  {
    "System Capability as listed in chapter 5": "Guidance:",
    "Used function as listed in chapter 6": "Guidance:"
  },
  {
    "System Capability as listed in chapter 5": "The location of all trains in communication prior to the restart, along with the extent of any MAs issued will be valuable information to be utilised.",
    "Used function as listed in chapter 6": "The location of all trains in communication prior to the restart, along with the extent of any MAs issued will be valuable information to be utilised."
  },
  {
    "System Capability as listed in chapter 5": "The validity of the information used must be carefully considered, as if the MBS has been offline for some time the State of the Railway is likely to have changed.",
    "Used function as listed in chapter 6": "The validity of the information used must be carefully considered, as if the MBS has been offline for some time the State of the Railway is likely to have changed."
  },
  {
    "System Capability as listed in chapter 5": "Criteria for considering Stored information as valid are project dependent e.g. during MBS Initialisation, if the time passed is smaller than a configured value.",
    "Used function as listed in chapter 6": "Criteria for considering Stored information as valid are project dependent e.g. during MBS Initialisation, if the time passed is smaller than a configured value."
  },
  {
    "System Capability as listed in chapter 5": "Operational Rules:",
    "Used function as listed in chapter 6": "None"
  },
  {
    "System Capability as listed in chapter 5": "Engineering Rules:",
    "Used function as listed in chapter 6": "ENG-TrackInit-1"
  },
  {
    "System Capability as listed in chapter 5": "REQ-0030",
    "Used function as listed in chapter 6": "FOR FURTHER RELEASE"
  },
  {
    "System Capability as listed in chapter 5": "The MBS shall, if configured, provide a means for the person responsible for the MBS Initialisation to confirm that the procedure is completed.",
    "Used function as listed in chapter 6": "The MBS shall, if configured, provide a means for the person responsible for the MBS Initialisation to confirm that the procedure is completed."
  },
  {
    "System Capability as listed in chapter 5": "Rationale:",
    "Used function as listed in chapter 6": "Rationale:"
  },
  {
    "System Capability as listed in chapter 5": "If Stored Information is not valid, the person in charge of initialising the MBS has to confirm when the procedure is completed. They have the authority to confirm that all the obstacles on the railway are known to the MBS.",
    "Used function as listed in chapter 6": "If Stored Information is not valid, the person in charge of initialising the MBS has to confirm when the procedure is completed. They have the authority to confirm that all the obstacles on the railway are known to the MBS."
  },
  {
    "System Capability as listed in chapter 5": "Guidance:",
    "Used function as listed in chapter 6": "Guidance:"
  },
  {
    "System Capability as listed in chapter 5": "If Stored information is used to initialise the MBS, this confirmation is not needed and it is project specific to implement it.",
    "Used function as listed in chapter 6": "If Stored information is used to initialise the MBS, this confirmation is not needed and it is project specific to implement it."
  },
  {
    "System Capability as listed in chapter 5": "Operational Rules:",
    "Used function as listed in chapter 6": "OPE-TrackInit-4"
  },
  {
    "System Capability as listed in chapter 5": "Engineering Rules:",
    "Used function as listed in chapter 6": "ENG-TrackInit-2"
  },
  {
    "System Capability as listed in chapter 5": "Create-move Train Location Reasons",
    "Used function as listed in chapter 6": "Notes"
  },
  {
    "System Capability as listed in chapter 5": "Train SoM position report received",
    "Used function as listed in chapter 6": "Train location created from min Safe Front End to max Safe Front End (before having received train data)"
  },
  {
    "System Capability as listed in chapter 5": "First Train Position Report",
    "Used function as listed in chapter 6": "For example, PR without SoM process"
  }
]

---

[
  {
    "Update front by Train Max SFE": "Update rear by Train CRE",
    "Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report": "Rear of the Train Location is updated using the Confirmed Rear End derived from the Train Position Report",
    "REQ-TrainLoc-7": "REQ-TrainLoc-8REQ-TrainLoc-9"
  },
  {
    "Update front by Train Max SFE": "Update rear with new value of Train Length",
    "Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report": "Rear of the Train Location is updated using the new value of Train Length",
    "REQ-TrainLoc-7": "REQ-TrainLoc-6"
  },
  {
    "Update front by Train Max SFE": "Update front by clear TTD",
    "Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report": "Front of the Train Location is shortened using clear TTD section",
    "REQ-TrainLoc-7": "REQ-TTD-2REQ-TTD-4"
  },
  {
    "Update front by Train Max SFE": "Update rear by clear TTD",
    "Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report": "Rear of the Train Location is shortened using clear TTD",
    "REQ-TrainLoc-7": "REQ-TTD-3REQ-TTD-4"
  },
  {
    "Update front by Train Max SFE": "Update front by occupied TTD for mute train",
    "Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report": "Update front of the Train Location when a TTD becomes occupied for a mute train",
    "REQ-TrainLoc-7": "REQ-TTD-5"
  }
]

Table 10 – Reasons to create or move Train Location

There are several reasons to delete a Train Location, as shown in Table 11:


[
  {
    "Delete Train Location Reasons": "Train is no longer in communication",
    "Notes": "MBS considers that a train is no longer in communication",
    "Requirements": "REQ-TrainLoc-10 REQ-0040"
  }
]

Table 11 – Reasons to delete Train Location

#### 6.9.2 Inputs

• Train Position Reports

• Validated Train Data

• Domain Data

• TTD section status (Domain Object state)

#### 6.9.3 Outputs

• Train Location

---

#### 6.9.4 General Train Location Requirements

## REQ-0063

To create or move a Train Location, the MBS shall perform the requirements sequentially in the order they are found in Table 10.

Rationale: For example, the position report requires the updating of the train front location prior the updating of the train rear location. Once the Train Location has been updated by the position report, it can be updated again by the clear TTD.

Guidance: None

Operational Rules: None

Engineering Rules: None

#### 6.9.5 Requirements to create a Train Location

## REQ-TrainLoc-5

The MBS shall create a Train Location for the Train Object from the Min Safe Front End to the Max Safe Front End derived from the Train Position Report if the following conditions are fulfilled:

- Train Position Report from an OBU where the reported position is unambiguous to the MBS is received, AND

• there is no Train Location for this OBU. AND

• mode is different from SB

## Rationale:

This is to enable the MBS to record the Train Location of all communicating trains in the Area of Control.

## Guidance:

The MBS will need to create a new Train Location:

- For an OBU which has started a communication session within the Area of Control, but which is not performing Start of Mission.

• For an OBU which has entered the Area of Control.

For a train which has started a communication session within the Area of Control, but which is not performing Start of Mission, the new Train Location will be from Max Safe Front End to Min Safe Front End, as there will be no train length provided yet.

---

# Contract No. HE – 101102001

For a train which has entered the Area of Control, and which has not confirmed Train Integrity, the new Train Location will be at least from the Max Safe Front End to the border of the Area of Control. This applies to both Handovers and Transitions.

How and when the first Train Location is established at the border to an Area of Control is project specific.

Note: When Train Data message is received for a train not yet localised (i.e. without existing Train Location), the Train Location is created for the front of the train due to the Train Position Report contained in this message. The train rear is afterwards localised using the Train Length (L_TRAIN) contained in the Train Data message (see REQ-TrainLoc-6).

Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-4

When receiving a Start of Mission Train Position Report which status is valid from a train where the reported position is unambiguous to the MBS, the MBS shall create a Train Location for that Train Object from the Min Safe Front End to the Max Safe Front End derived from the Train Position Report.

## Rationale:

For a train which has a new connection to the MBS, the MBS must create a new Train Location for the reported position.

## Guidance:

At Start of Mission, before the receipt of Validated Train Data, only the Estimated Front End and its Confidence Interval are known to the MBS. The Train Location is then only from Max Safe Front End to Min Safe Front End, as shown in Figure 22.

[
  {
    "REQ-TMS-1": "The TMS shall provide means for a Signaller to assign a position to a train that is reporting a position during Start of Mission which is unknown or invalid, or a position which the MBS considers ambiguous.",
    "FOR FURTHER RELEASE": "The TMS shall provide means for a Signaller to assign a position to a train that is reporting a position during Start of Mission which is unknown or invalid, or a position which the MBS considers ambiguous.",
    "[X2R5 REQ-TMS-1]": "The TMS shall provide means for a Signaller to assign a position to a train that is reporting a position during Start of Mission which is unknown or invalid, or a position which the MBS considers ambiguous."
  },
  {
    "REQ-TMS-1": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:",
    "[X2R5 REQ-TMS-1]": "Rationale:"
  },
  {
    "REQ-TMS-1": "This is to allow the MBS to locate a train in its Area of Control after a specific operational procedure.",
    "FOR FURTHER RELEASE": "This is to allow the MBS to locate a train in its Area of Control after a specific operational procedure.",
    "[X2R5 REQ-TMS-1]": "This is to allow the MBS to locate a train in its Area of Control after a specific operational procedure."
  },
  {
    "REQ-TMS-1": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:",
    "[X2R5 REQ-TMS-1]": "Guidance:"
  },
  {
    "REQ-TMS-1": "How the Signaller enters the position of a train in the TMS is project specific, but the MBS cannot accept a position in a clear area of track.",
    "FOR FURTHER RELEASE": "How the Signaller enters the position of a train in the TMS is project specific, but the MBS cannot accept a position in a clear area of track.",
    "[X2R5 REQ-TMS-1]": "How the Signaller enters the position of a train in the TMS is project specific, but the MBS cannot accept a position in a clear area of track."
  },
  {
    "REQ-TMS-1": "The Signaller may need to contact the Driver to determine an estimated location for the train.",
    "FOR FURTHER RELEASE": "The Signaller may need to contact the Driver to determine an estimated location for the train.",
    "[X2R5 REQ-TMS-1]": "The Signaller may need to contact the Driver to determine an estimated location for the train."
  },
  {
    "REQ-TMS-1": "Operational Rules:",
    "FOR FURTHER RELEASE": "OPE-SoM-4"
  },
  {
    "REQ-TMS-1": "Engineering Rules:",
    "FOR FURTHER RELEASE": "None"
  },
  {
    "REQ-TMS-1": "FOR FURTHER RELEASE [X2R5 REQ-TrainLoc-12]",
    "FOR FURTHER RELEASE": "FOR FURTHER RELEASE [X2R5 REQ-TrainLoc-12]"
  },
  {
    "REQ-TMS-1": "If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall react to transition the system to a safe state.",
    "FOR FURTHER RELEASE": "If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall react to transition the system to a safe state."
  },
  {
    "REQ-TMS-1": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:"
  },
  {
    "REQ-TMS-1": "The MBS is reliant upon trains reporting their position to separate traffic safely and the MBS must therefore react if it detects a potentially hazardous situation.",
    "FOR FURTHER RELEASE": "The MBS is reliant upon trains reporting their position to separate traffic safely and the MBS must therefore react if it detects a potentially hazardous situation."
  },
  {
    "REQ-TMS-1": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:"
  },
  {
    "REQ-TMS-1": "A train reporting an unexpected position can be a hazard even when there is TTD if more than one train is in the same TTD section, but the situation is more severe in an area without TTD.",
    "FOR FURTHER RELEASE": "A train reporting an unexpected position can be a hazard even when there is TTD if more than one train is in the same TTD section, but the situation is more severe in an area without TTD."
  },
  {
    "REQ-TMS-1": "The MBS will only be able to detect conflicts with other train movements which have been authorised by the MBS.",
    "FOR FURTHER RELEASE": "The MBS will only be able to detect conflicts with other train movements which have been authorised by the MBS."
  },
  {
    "REQ-TMS-1": "There are several situations where a position report from a train may require immediate action from the MBS to avoid a potential hazard, for example:",
    "FOR FURTHER RELEASE": "There are several situations where a position report from a train may require immediate action from the MBS to avoid a potential hazard, for example:"
  },
  {
    "REQ-TMS-1": "a train reporting a position in an area previously considered clear, e.g. at Start of Mission, OR",
    "FOR FURTHER RELEASE": "a train reporting a position in an area previously considered clear, e.g. at Start of Mission, OR"
  },
  {
    "REQ-TMS-1": "a train which has been allocated a Reserved Status Area reporting a position which cannot be linked with that Reserved Status Area, OR",
    "FOR FURTHER RELEASE": "a train which has been allocated a Reserved Status Area reporting a position which cannot be linked with that Reserved Status Area, OR"
  },
  {
    "REQ-TMS-1": "a train reporting a position locating it within a Reserved Status Area allocated to another train.",
    "FOR FURTHER RELEASE": "a train reporting a position locating it within a Reserved Status Area allocated to another train."
  },
  {
    "REQ-TMS-1": "The specific reaction applied will depend on the situation and application specific requirements. Possible reactions include:",
    "FOR FURTHER RELEASE": "The specific reaction applied will depend on the situation and application specific requirements. Possible reactions include:"
  },
  {
    "REQ-TMS-1": "shortening of the Movement Authority for the affected train(s),",
    "FOR FURTHER RELEASE": "shortening of the Movement Authority for the affected train(s),"
  },
  {
    "REQ-TMS-1": "sending an Unconditional Emergency Stop message to the affected train(s).",
    "FOR FURTHER RELEASE": "sending an Unconditional Emergency Stop message to the affected train(s)."
  },
  {
    "REQ-TMS-1": "Note that the Train Location is created or updated by other requirements.",
    "FOR FURTHER RELEASE": "Note that the Train Location is created or updated by other requirements."
  },
  {
    "REQ-TMS-1": "Operational Rules:",
    "FOR FURTHER RELEASE": "None"
  },
  {
    "REQ-TMS-1": "Engineering Rules:",
    "FOR FURTHER RELEASE": "None"
  },
  {
    "REQ-TMS-1": "EQ-TrainLoc-13",
    "FOR FURTHER RELEASE": "FOR FURTHER RELEASE [X2R5 REQ-TrainLoc-13]"
  },
  {
    "REQ-TMS-1": "If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall alert the PE to the situation.",
    "FOR FURTHER RELEASE": "If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall alert the PE to the situation."
  }
]

---

## Rationale:

This is to make the TMS and Signallers aware in case the reported position could be a real or potential hazard for other train movements.

## Guidance:

A train reporting an unexpected position can be a hazard even when there is TTD if more than one train is in the same TTD section, but the situation is more severe in an area without TTD.

The MBS will only be able to detect conflict with other train movements which have been authorised by the MBS.

There are several situations where a position report from a train may require additional intervention from the TMS or Signaller to manage the degraded situation. For example:

- a train reporting a position in an area previously considered clear, e.g. at Start of Mission, OR

- a train reporting a position locating it within a Reserved Status Area allocated to another train.

Operational Rules: None

Engineering Rules: None

#### 6.9.8 Impact from TTD on Train Locations

## REQ-TTD-1

For a system using TTD, the MBS shall manage the asynchronicity between TTD section status and Train Position Reports for a communicating train.

## Rationale:

It will occur that the train physically occupies a TTD section before it has reported its position within the TTD section (or vice versa). Similarly, the train may physically leave a TTD section before it has reported its position beyond the TTD section (or vice versa). The MBS must correlate these events.

## Guidance:

The MBS must be designed to allow for:

- A TTD section becoming Occupied by a train before the train has reported a position within the TTD section.

- A train reporting a position within the TTD section before TTD section becomes Occupied.

- A TTD section becoming Clear after a train has left the TTD section before the train has reported a position clear of the TTD section.

---

- A train reporting a position clear of the TTD section before the TTD section becomes Clear.

The MBS could use a variety of technical solutions to correlate TTD occupancy to Train Position Reports. For example:

- Sending a Conditional Emergency Stop when a TTD is occupied, to stop a train that is approaching a boundary of the TTD if it is not the one that occupied the TTD.

- Use of a delay timer, to account for lack of synchronisation between Train Position Reports and TTD occupancy. If a train is still not detected when the timer expires, the MBS would react suitably.

• Tracking of TTD section occupancy and correlation with Train Position Reporting, to ensure a normal sequence is observed.

Note: a combination of these techniques may be used, depending on project specific requirements.

Operational Rules: None

Engineering Rules: None

## REQ-TTD-2

For a system using TTD, if the Max Safe Front End reported by a train is located in a clear TTD section while the Min Safe Front End is not in this TTD section, then the MBS shall shorten the front of the Train Location for this train, by the extent of each TTD section that is detected. Clear between the Min Safe Front End and the Max Safe Front End.

## Rationale:

TTD information can be used to improve the MBS knowledge about the status of the track in the Area of Control, thus improving the performance of the system.

## Guidance:

The effect of a Clear TTD section in the front part of a Train Location is to update the front of the Train Location.

This can be used to avoid locking points and level crossings in front of the train. Both the reception of TTD status and the receiving of a Train Position Report can be the trigger for updating the Train Location.

---

A clear TTD section in front of a train can shorten the front part of the Train Location of the train, as shown in Figure 28:

[
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "For a system using TTD, when using Clear TTD sections to shorten a Train Location, the MBS shall ensure that the length of the reduced Train Location is not shorter than the length of the train."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Applying shortening should not result in the extent of the remaining Train Location being less than the length of the train."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Guidance:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "If the application of shortening the Train Location results in the length of the Train Location being less than the length of the train, it is project specific what alternative action the MBS takes. For example, an application may decide to not apply any shortening to the Train Location, or to apply equal shortening to the front and rear."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "At boundaries, projects might decide to truncate the Train Location and as a result, Train Location could be shorter than length of the train."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "FOR FURTHER RELEASE [X2R5 REQ-TTD-5]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "For a system using TTD, when detecting an expected TTD occupancy within the Movement Permission allocated to a train, after its Mute Timer has expired, the MBS shall extend the Train Location of the train up to the closest of:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "• the end of the Movement Permission&#x27;s Risk Buffer, OR"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "• the next boundary of this Occupied TTD section"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The MBS can use TTD occupation to extend the Train Location of a train where the Mute Timer has expired and is moving along the railway within the Movement Permission allocated to it, thus maintaining the link between the Train Location and the train, thereby facilitating recovery if communication is re-established."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Guidance:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "A train where the Mute Timer has expired can move forward within the Movement Permission allocated to that train and occupy a previously clear TTD. That occupation can be attributed to a normal train movement. The MBS can adjust the knowledge about where the train might be by extending the Train Location of this train."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "FOR FURTHER RELEASE [X2R5 REQ- LossComms-1]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "FOR FURTHER RELEASE [X2R5 REQ-LossComms-2]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "FOR FURTHER RELEASE [X2R5 REQ-LossComms-3]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "When the Mute Timer expires for a train which has not entered an announced Radio Hole, and which was not reporting in RV mode, then the MBS shall convert the Train Object into an Unresolved Trackbound Object. The Unresolved Trackbound Object area shall correspond to the Train Location extended to the end of the Movement Permission or the end of the MA, whichever is shorter."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "[X2R5 REQ-EoM-4]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The MBS shall be able to cope with differences in the confidence interval provided in the position report of a train that reported EoM even when related to the same train position. Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "This is due to an ambiguity in the ETCS specifications around how to calculate the Train Location accuracy when linking information is deleted due to the change to SB mode. See REQ-EoM-4"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Guidance:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "This issue is the subject of CR1318 in the ERA CCM Process [CRProcess]. The MBS must be able to deal with On-boards which have not applied the solution to CR1318. Operational Rules: None Engineering Rules: None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "[X2R5 REQ-LossComms-4]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "If the Mute Timer is not considered for use on a particular application, the MBS shall react when the session timer expires by converting the Train Object into an Unresolved Trackbound Object. The Unresolved Trackbound Object shall correspond to the Train Location extended to the end of the Movement Permission, except if the train was reporting in RV mode. Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "This is so that, even for applications not utilising the Mute timer functionality, the Trackside is protected when communications with a train expire according to the existing session expiry timer in the ETCS specifications [BL3 R2]."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Guidance:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Whether or not to use the Mute Timer will depend on whether it is required to detect loss of communication before expiry of the session timer. This in turn will depend on traffic density and the typical speed of trains. Once a train is reporting in RV mode, it is not able to move forwards without performing EoM and Start of Mission, so it is not necessary to extend the Unresolved Trackbound Object to the end of the Movement Permission."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Requirements"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-25, REQ-TrackStatus-10"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrainLoc-10 REQ-0040"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Requirements"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-0028"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TTD-9, REQ-TTD-10"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TTD-12"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrainLoc-14, REQ-TrainLoc-15, REQ-TrainLoc-16, REQ-TrainLoc-17"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Requirements"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-9"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-10"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-12 REQ-TrackStatus-15"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-14"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TrackStatus-19 REQ-TTD-8"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "REQ-TTD-7"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "[X2R5 REQ-TrackStatus-26]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "If an Unresolved Trackbound Object is created that is within a Movement Permission allocated to a train, then the MBS shall react to transition the system to a safe state."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "A new Unresolved Trackbound Object within a Movement Permission allocated to a train may require urgent action from the MBS in order to avoid a hazard."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Guidance:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The specific reaction applied will depend on the scenario and application specific requirements. Possible reactions include shortening of the Movement Authority for another train; sending an Unconditional Emergency Stop to one or multiple trains etc."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Notes"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The extent of the Unresolved Trackbound Object."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The length of train associated with this Unresolved Trackbound Object, if any. Note: this length is not the same as the extent of the UTO."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The NID_ENGINE of the train associated with this UTO, if any."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The reason why the UTO was created. There might be more than one reason."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "The increase in the train length for the Train Location will be because the MBS has received Validated Train Data with an increased value of L_TRAIN."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "A train is expected to send Validated Train Data with an increased value of L_TRAIN if it has performed a joining operation. In this case, there should be one or more adjacent Unresolved Trackbound Object, where the additional Recorded Train Length(s) can account for the increased train length."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "If there are no adjacent Unresolved Trackbound Object which can account for the increased train length, then some error has occurred, and the TMS will be alerted."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "An inconsistency in the reported length from a train and the length stored by the MBS could be due to an error in the stored data, or failure in the application of Operational Rules. The MBS may decide to take a protective reaction, such as extending an Unresolved Trackbound Object to cover the Train Location. This reaction is project specific."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "FOR FURTHER RELEASE [X2R5 REQ-TrackStatus-12]"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "If the MBS is configured to accept Train Integrity confirmed by Driver, when Train Integrity is confirmed by Driver for a train associated with an Unresolved Trackbound Object, and the length (L_TRAIN) of this train is less than the Recorded Train Length of the Unresolved Trackbound Object, then the MBS shall:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "• reduce the Recorded Train Length of the Unresolved Trackbound Object by the length of the train that confirmed Train Integrity"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "Rationale:"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "An Unresolved Trackbound Object cannot be fully removed if a reported train length does not account for all the Recorded Train Length of that area."
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  },
  {
    "FOR FURTHER RELEASE [X2R5 REQ-TTD-4]": "None"
  }
]


[
  {
    "EQ-TrackStatus-13": "When Train Integrity is confirmed for a train associated with an Unresolved Trackbound Object located within an Activated Temporary Shunting Area, then the MBS shall reduce the Recorded Train Length of the Unresolved Trackbound Object associated with the Shunting Area by the length of the train that confirmed Train Integrity.",
    "FOR FURTHER RELEASE": "When Train Integrity is confirmed for a train associated with an Unresolved Trackbound Object located within an Activated Temporary Shunting Area, then the MBS shall reduce the Recorded Train Length of the Unresolved Trackbound Object associated with the Shunting Area by the length of the train that confirmed Train Integrity.",
    "[X2R5 REQ-TrackStatus-13]": "When Train Integrity is confirmed for a train associated with an Unresolved Trackbound Object located within an Activated Temporary Shunting Area, then the MBS shall reduce the Recorded Train Length of the Unresolved Trackbound Object associated with the Shunting Area by the length of the train that confirmed Train Integrity."
  },
  {
    "EQ-TrackStatus-13": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:",
    "[X2R5 REQ-TrackStatus-13]": "Rationale:"
  },
  {
    "EQ-TrackStatus-13": "This is required for the MBS to maintain the Track Status within its Area of Control.",
    "FOR FURTHER RELEASE": "This is required for the MBS to maintain the Track Status within its Area of Control.",
    "[X2R5 REQ-TrackStatus-13]": "This is required for the MBS to maintain the Track Status within its Area of Control."
  },
  {
    "EQ-TrackStatus-13": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:",
    "[X2R5 REQ-TrackStatus-13]": "Guidance:"
  },
  {
    "EQ-TrackStatus-13": "If all the train length recorded for an Active Shunting Area is accounted for when the area is deactivated, then the Unresolved Trackbound Object that was associated with the Shunting Area can be removed, else it will remain but be Sweepable.",
    "FOR FURTHER RELEASE": "If all the train length recorded for an Active Shunting Area is accounted for when the area is deactivated, then the Unresolved Trackbound Object that was associated with the Shunting Area can be removed, else it will remain but be Sweepable.",
    "[X2R5 REQ-TrackStatus-13]": "If all the train length recorded for an Active Shunting Area is accounted for when the area is deactivated, then the Unresolved Trackbound Object that was associated with the Shunting Area can be removed, else it will remain but be Sweepable."
  },
  {
    "EQ-TrackStatus-13": "Operational Rules:",
    "FOR FURTHER RELEASE": "None"
  },
  {
    "EQ-TrackStatus-13": "Engineering Rules:",
    "FOR FURTHER RELEASE": "None"
  }
]

---

## REQ-TrackStatus-14

When the front of the train has passed a part or all of an Unresolved Trackbound Object that existed before the Train Location was updated, then the MBS shall reduce that Unresolved Trackbound Object for the part of it from the previous min Safe Front End up to the new min Safe Front End of the train.

## Rationale:

This is to enable sweeping of the area passed between received position reports.

## Guidance:

Sweeping is performed by the Min Safe Front End (mSFE) of a train, as it cannot be guaranteed that there is no obstruction between the mSFE and the Max Safe Front End (MSFE) which is the Confidence Interval where the front of the train can be.

Figure 37 shows the sweeping by Train Location for a train with Train Integrity confirmed in a Sweepable Unresolved Trackbound Object ahead of the train.

[
  {
    "EQ-TTD-11": "For a system using TTD, on request from the TMS, the MBS shall be able to remove an Unresolved Trackbound Object caused by a faulty TTD.",
    "FOR FURTHER RELEASE": "For a system using TTD, on request from the TMS, the MBS shall be able to remove an Unresolved Trackbound Object caused by a faulty TTD.",
    "[X2R5 REQ-TTD-11]": "For a system using TTD, on request from the TMS, the MBS shall be able to remove an Unresolved Trackbound Object caused by a faulty TTD."
  },
  {
    "EQ-TTD-11": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:",
    "[X2R5 REQ-TTD-11]": "Rationale:"
  },
  {
    "EQ-TTD-11": "This will allow the MBS to help restore normal operation on the line.",
    "FOR FURTHER RELEASE": "This will allow the MBS to help restore normal operation on the line.",
    "[X2R5 REQ-TTD-11]": "This will allow the MBS to help restore normal operation on the line."
  },
  {
    "EQ-TTD-11": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:",
    "[X2R5 REQ-TTD-11]": "Guidance:"
  },
  {
    "EQ-TTD-11": "This function could be used to improve the reliability of the system and overrule false occupation reported by TTD (e.g. malfunctioning axle counters).",
    "FOR FURTHER RELEASE": "This function could be used to improve the reliability of the system and overrule false occupation reported by TTD (e.g. malfunctioning axle counters).",
    "[X2R5 REQ-TTD-11]": "This function could be used to improve the reliability of the system and overrule false occupation reported by TTD (e.g. malfunctioning axle counters)."
  },
  {
    "EQ-TTD-11": "In MBS operations, when all train movements are supervised by OBU with train position reporting and train integrity confirmation, a faulty TTD could be detected, e.g. dependent on the states of the neighbouring TTDs and position reports.",
    "FOR FURTHER RELEASE": "In MBS operations, when all train movements are supervised by OBU with train position reporting and train integrity confirmation, a faulty TTD could be detected, e.g. dependent on the states of the neighbouring TTDs and position reports.",
    "[X2R5 REQ-TTD-11]": "In MBS operations, when all train movements are supervised by OBU with train position reporting and train integrity confirmation, a faulty TTD could be detected, e.g. dependent on the states of the neighbouring TTDs and position reports."
  },
  {
    "EQ-TTD-11": "The implementation of this requirement will need to prevent a new Unresolved Trackbound Object being created whilst the TTD remains Occupied.",
    "FOR FURTHER RELEASE": "The implementation of this requirement will need to prevent a new Unresolved Trackbound Object being created whilst the TTD remains Occupied.",
    "[X2R5 REQ-TTD-11]": "The implementation of this requirement will need to prevent a new Unresolved Trackbound Object being created whilst the TTD remains Occupied."
  },
  {
    "EQ-TTD-11": "Operational Rules:",
    "FOR FURTHER RELEASE": "OPE-Generic-1, OPE-Generic-2",
    "[X2R5 REQ-TTD-11]": "OPE-Generic-1, OPE-Generic-2"
  },
  {
    "EQ-TTD-11": "Engineering Rules:",
    "FOR FURTHER RELEASE": "ENG-Generic-7",
    "[X2R5 REQ-TTD-11]": "ENG-Generic-7"
  },
  {
    "EQ-TTD-11": "6.10.7 Requirements related to Operator panel - FOR FURTHER RELEASE",
    "FOR FURTHER RELEASE": "6.10.7 Requirements related to Operator panel - FOR FURTHER RELEASE"
  },
  {
    "EQ-TTD-11": "REQ-TrackStatus-22",
    "FOR FURTHER RELEASE": "[X2R5 REQ-TrackStatus-22]"
  },
  {
    "EQ-TTD-11": "On request from the PE/Operator panel, the MBS shall create an Unresolved Trackbound Object flagged as Sweepable provided the area is longer than the configurable minimum length.",
    "FOR FURTHER RELEASE": "On request from the PE/Operator panel, the MBS shall create an Unresolved Trackbound Object flagged as Sweepable provided the area is longer than the configurable minimum length."
  },
  {
    "EQ-TTD-11": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:"
  },
  {
    "EQ-TTD-11": "This is to allow the MBS to have all relevant information concerning obstructions.",
    "FOR FURTHER RELEASE": "This is to allow the MBS to have all relevant information concerning obstructions."
  },
  {
    "EQ-TTD-11": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:"
  },
  {
    "EQ-TTD-11": "For example, this can be used in the degraded situation of a non-communicating train. A train without communications has to be moved inside an Unresolved Trackbound Object, so that the MBS is aware that this area is protected for a specific train.",
    "FOR FURTHER RELEASE": "For example, this can be used in the degraded situation of a non-communicating train. A train without communications has to be moved inside an Unresolved Trackbound Object, so that the MBS is aware that this area is protected for a specific train."
  },
  {
    "EQ-TTD-11": "The Unresolved Trackbound Object may be created automatically by the TMS, or via dispatcher interaction with the TMS or Operator Panel.",
    "FOR FURTHER RELEASE": "The Unresolved Trackbound Object may be created automatically by the TMS, or via dispatcher interaction with the TMS or Operator Panel."
  },
  {
    "EQ-TTD-11": "Unresolved Trackbound Object can be created independently.",
    "FOR FURTHER RELEASE": "Unresolved Trackbound Object can be created independently."
  },
  {
    "EQ-TTD-11": "The Sweepable Unresolved Trackbound Object needs to be longer than the configurable minimum length for removal of Unresolved Trackbound Object, as defined in ENG-Generic-3.",
    "FOR FURTHER RELEASE": "The Sweepable Unresolved Trackbound Object needs to be longer than the configurable minimum length for removal of Unresolved Trackbound Object, as defined in ENG-Generic-3."
  },
  {
    "EQ-TTD-11": "Operational Rules:",
    "FOR FURTHER RELEASE": "OPE-TrackInit-2; OPE-Generic-7; OPE-LossComms-1; OPE-LossTI-1"
  },
  {
    "EQ-TTD-11": "Engineering Rules:",
    "FOR FURTHER RELEASE": "ENG-Generic-3"
  },
  {
    "EQ-TTD-11": "REQ-TrackStatus-23",
    "FOR FURTHER RELEASE": "[X2R5 REQ-TrackStatus-23]"
  },
  {
    "EQ-TTD-11": "On request from the PE/Operator Panel, the MBS shall create an Unresolved Trackbound Object flagged as Non-Sweepable.",
    "FOR FURTHER RELEASE": "On request from the PE/Operator Panel, the MBS shall create an Unresolved Trackbound Object flagged as Non-Sweepable."
  },
  {
    "EQ-TTD-11": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:"
  },
  {
    "EQ-TTD-11": "When the PE/Operator Panel requests a Non-Sweepable Unresolved Trackbound Object, it may be for a reason that would make it unsuitable to be swept e.g. a known permanent obstacle on the line.",
    "FOR FURTHER RELEASE": "When the PE/Operator Panel requests a Non-Sweepable Unresolved Trackbound Object, it may be for a reason that would make it unsuitable to be swept e.g. a known permanent obstacle on the line."
  },
  {
    "EQ-TTD-11": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:"
  },
  {
    "EQ-TTD-11": "Non-Sweepable Unresolved Trackbound Object will only be cleared at the request of the TMS. The MBS will retain a Non-Sweepable Unresolved Trackbound Object after traversal by a train which has confirmed Train Integrity.",
    "FOR FURTHER RELEASE": "Non-Sweepable Unresolved Trackbound Object will only be cleared at the request of the TMS. The MBS will retain a Non-Sweepable Unresolved Trackbound Object after traversal by a train which has confirmed Train Integrity."
  },
  {
    "EQ-TTD-11": "Unresolved Trackbound Object can be created independently, i.e. they can overlap existing Unresolved Trackbound Object or Train Location.",
    "FOR FURTHER RELEASE": "Unresolved Trackbound Object can be created independently, i.e. they can overlap existing Unresolved Trackbound Object or Train Location."
  },
  {
    "EQ-TTD-11": "For example, creating Unresolved Trackbound Object in parts of the track might be due to external systems detecting fallen objects, or landslides.",
    "FOR FURTHER RELEASE": "For example, creating Unresolved Trackbound Object in parts of the track might be due to external systems detecting fallen objects, or landslides."
  },
  {
    "EQ-TTD-11": "Operational Rules:",
    "FOR FURTHER RELEASE": "OPE-TrackInit-2, OPE-Generic-7; OPE-LossComms-1; OPE-LossTI-1"
  },
  {
    "EQ-TTD-11": "Engineering Rules:",
    "FOR FURTHER RELEASE": "None"
  },
  {
    "EQ-TTD-11": "REQ-TrackStatus-24",
    "FOR FURTHER RELEASE": "[X2R5 REQ-TrackStatus-24]"
  },
  {
    "EQ-TTD-11": "On request from the PE/Operator Panel, the MBS shall remove, reduce or extend Unresolved Trackbound Object.",
    "FOR FURTHER RELEASE": "On request from the PE/Operator Panel, the MBS shall remove, reduce or extend Unresolved Trackbound Object."
  },
  {
    "EQ-TTD-11": "Rationale:",
    "FOR FURTHER RELEASE": "Rationale:"
  },
  {
    "EQ-TTD-11": "MBS must allow the TMS to remove, reduce or extend Unresolved Trackbound Object based on the result of operational procedures.",
    "FOR FURTHER RELEASE": "MBS must allow the TMS to remove, reduce or extend Unresolved Trackbound Object based on the result of operational procedures."
  },
  {
    "EQ-TTD-11": "Guidance:",
    "FOR FURTHER RELEASE": "Guidance:"
  },
  {
    "EQ-TTD-11": "An Unresolved Trackbound Object, both Sweepable and Non-Sweepable, can be removed, reduced or extended by the PE/Operator Panel.",
    "FOR FURTHER RELEASE": "An Unresolved Trackbound Object, both Sweepable and Non-Sweepable, can be removed, reduced or extended by the PE/Operator Panel."
  },
  {
    "EQ-TTD-11": "For example, some Infrastructure Managers may permit Unresolved Trackbound Object to be removed or reduced based on the observations of a Driver sweeping on an adjacent line.",
    "FOR FURTHER RELEASE": "For example, some Infrastructure Managers may permit Unresolved Trackbound Object to be removed or reduced based on the observations of a Driver sweeping on an adjacent line."
  },
  {
    "EQ-TTD-11": "Projects may, if providing the necessary information, allow the Dispatcher via PE/Operator Panel to remove or reduce parts of an Unresolved Trackbound Object, e.g. by stating a certain length to be removed.",
    "FOR FURTHER RELEASE": "Projects may, if providing the necessary information, allow the Dispatcher via PE/Operator Panel to remove or reduce parts of an Unresolved Trackbound Object, e.g. by stating a certain length to be removed."
  },
  {
    "EQ-TTD-11": "In case there is a train length stored for an Unresolved Trackbound Object requested for removal, it is recommended that the MBS prevents removing this Unresolved Trackbound Object unless the removal is supported by some additional measure(s).",
    "FOR FURTHER RELEASE": "In case there is a train length stored for an Unresolved Trackbound Object requested for removal, it is recommended that the MBS prevents removing this Unresolved Trackbound Object unless the removal is supported by some additional measure(s)."
  },
  {
    "EQ-TTD-11": "Flank Protection by",
    "FOR FURTHER RELEASE": "Termination Requirement SC-RP_TERM_",
    "[X2R5 REQ-TTD-11]": "Variable"
  },
  {
    "EQ-TTD-11": "Search Options",
    "FOR FURTHER RELEASE": "--",
    "[X2R5 REQ-TTD-11]": "fpSearch"
  },
  {
    "EQ-TTD-11": "Search Options",
    "FOR FURTHER RELEASE": "--",
    "[X2R5 REQ-TTD-11]": "fpSearchOnDependentAs"
  },
  {
    "EQ-TTD-11": "Search Options",
    "FOR FURTHER RELEASE": "--",
    "[X2R5 REQ-TTD-11]": "rpMaxSearchDistance"
  },
  {
    "EQ-TTD-11": "Switchable Track Element",
    "FOR FURTHER RELEASE": "DPS",
    "[X2R5 REQ-TTD-11]": "rpTermAtDpsOnly"
  },
  {
    "EQ-TTD-11": "Switchable Track Element",
    "FOR FURTHER RELEASE": "DPS",
    "[X2R5 REQ-TTD-11]": "dpsProvidesFlankProtection"
  },
  {
    "EQ-TTD-11": "Switchable Track Element",
    "FOR FURTHER RELEASE": "DPS",
    "[X2R5 REQ-TTD-11]": "dpsMaxFlankProtectionSpeed"
  },
  {
    "EQ-TTD-11": "Movement Permission",
    "FOR FURTHER RELEASE": "RB MP",
    "[X2R5 REQ-TTD-11]": "rpTermAllowedAtRbAndMp"
  },
  {
    "EQ-TTD-11": "Train Object",
    "FOR FURTHER RELEASE": "TO",
    "[X2R5 REQ-TTD-11]": "rpTermAllowedAtTo"
  },
  {
    "EQ-TTD-11": "Flank Protection by",
    "FOR FURTHER RELEASE": "Termination Requirement SC-RP_TERM_",
    "[X2R5 REQ-TTD-11]": "Variable"
  },
  {
    "EQ-TTD-11": "Sufficient Distance",
    "FOR FURTHER RELEASE": "DIST",
    "[X2R5 REQ-TTD-11]": "rpTermAllowedAfterMaxDistance"
  },
  {
    "EQ-TTD-11": "Operational Rules (UTO found)",
    "FOR FURTHER RELEASE": "UTO",
    "[X2R5 REQ-TTD-11]": "rpTermAllowedAtUto"
  },
  {
    "EQ-TTD-11": "Operational Rules (UTO found)",
    "FOR FURTHER RELEASE": "UTO",
    "[X2R5 REQ-TTD-11]": "rpTermMaxSpeedUto"
  },
  {
    "EQ-TTD-11": "Application Example",
    "FOR FURTHER RELEASE": "T01",
    "[X2R5 REQ-TTD-11]": "TE4"
  },
  {
    "EQ-TTD-11": "Movement Permission"
  },
  {
    "EQ-TTD-11": "Risk Path"
  },
  {
    "EQ-TTD-11": "Risk Buffer"
  },
  {
    "EQ-TTD-11": "Train Object (Train Location)"
  },
  {
    "EQ-TTD-11": "DPS in state FULL"
  },
  {
    "EQ-TTD-11": "DPS in state NONE"
  },
  {
    "EQ-TTD-11": "Unresolved Trackbound Object"
  },
  {
    "FOR FURTHER RELEASE": "MP",
    "[X2R5 REQ-TTD-11]": "TO/UTO"
  },
  {
    "EQ-TTD-11": "MP",
    "FOR FURTHER RELEASE": "REQ-SC_MP_MP",
    "[X2R5 REQ-TTD-11]": "FS MandatoryREQ-SC_MP_TOREQ-SC_MP_UTO"
  },
  {
    "EQ-TTD-11": "RB",
    "FOR FURTHER RELEASE": "REQ-SC_RB_MP",
    "[X2R5 REQ-TTD-11]": "FS Mandatory OR ConfigREQ-SC_RB_TOREQ-SC_RB_UTO"
  },
  {
    "FOR FURTHER RELEASE": "MP",
    "[X2R5 REQ-TTD-11]": "TO/UTO"
  },
  {
    "EQ-TTD-11": "MP",
    "FOR FURTHER RELEASE": "REQ-SC_MP_MP_AS",
    "[X2R5 REQ-TTD-11]": "FS Mandatory\nREQ-SC_MP_TO_AS\nREQ-SC_MP_UTO_AS"
  },
  {
    "EQ-TTD-11": "RB",
    "FOR FURTHER RELEASE": "REQ-SC_RB_MP_AS",
    "[X2R5 REQ-TTD-11]": "FS Mandatory OR Config\nREQ-SC_RB_TO_AS\nREQ-SC_RB_UTO_AS"
  }
]

Red = Check is always performed

Orange = Check is performed depending on operational situation

Yellow = Check is configuration dependent

Green = No Check

Additional safety checks for flank protection are performed by:

- Requirement REQ-RP_SEARCH, which search the elements providing (or not) flank protection

- Requirement REQ-SC_RP_TERM which check the found elements

---

#### 6.11.2 Inputs

MP Request message according to I_PE

Domain Object State

#### 6.11.3 Outputs

Message “request granted” according to I_PE

Requested and validated state of the Movement Permission

- Message “request rejected” according to I_PE

---

#### 6.11.4 Functional requirements

## REQ-SAFETY

The MBS shall perform a series of checks given by the following ordered list when it receives an Authorise MP Request through I_PE:

1. REQ-SYNTAX

2. REQ-TO_ EXISTS

3. REQ-TO_RADY

4. REQ-TOPO1

5. REQ-TOPO2

6. REQ-TOPO3

7. REQ-TOPO4

8. REQ-TOPO5

9. REQ-TRANSLATE

10. REQ-SC_MP_SPEED

11. REQ-SC_RB_SPEED

12. REQ-SC_MP_SPEED_LOWER

13. REQ-SC_MODE

14. REQ-SC_MODE_MISMATCH

15. REQ-SC_MP_SHORTER

16. REQ-SC_RB_SHORTER

17. REQ-SC_MP_TO

18. REQ-SC_MP_UTO

19. REQ-SC_RB_TO

20. REQ-SC_RB_UTO

21. REQ-SC_MP_TO_AS

22. REQ-SC_MP_UTO_AS

23. REQ-SC_RB_TO_AS

24. REQ-SC_RB_UTO_AS

25. REQ-SC_MP_MP

26. REQ-SC_MP_RB

27. REQ-SC_MP_RP

---

28. REQ-SC_MP_MP_AS

29. REQ-SC_MP_RB_AS

30. REQ-SC RB MPPS

31. REQ-SC RB RB

32. REQ-SC RB RP

33. REQ-SC RB MP AS

34. REQ-SC RB RB AS

35. REQ-SC RB SIZE

36. REQ-SC MPPS DPS

37. REQ-SC RB DPS

38. REQ-RP SEARCH

39. REQ-SC RP TERM

40. REQ-COOP_PENDING

Rationale: The request to allow a train movement shall be safeguarded.

Guidance: This is the top requirement for all (safety) checks.

Operational Rules: None

Engineering Rules: None

## REQ-0032

The MBS shall abort checking an Authorise MP Request received through I_PE if any performed safety check fails and send a request rejected message.

Rationale: A safety check could require the correct execution of a previous safety check.

Guidance: If a check discovers a mismatch between the topology in PE and MBS, further checks might lead to illegal function calls within MBS as this part of the topology is not present in the current operating state of MBS.

Operational Rules: None

Engineering Rules: None

## REQ-0033

If none of the safety checks fails, MBS shall send an "MP_REQUEST_GRANTED" reply.

Rationale: PE shall be informed about the successful check of the request.

Guidance: None

Operational Rules: None

---

Engineering Rules: None

##### 6.11.4.1 General Safety Checks

## REQ-SYNTAX

The MBS shall perform a syntax check on the received message and if the check fails, the MBS shall send a "SYNTAX" reject code.

Rationale: An invalid command syntax might lead to illegal state.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ- TO EXISTS

The MBS shall check that the Train Object referenced in the request exists within the operating state of the MBS and if the check fails, the MBS shall send a "INCONSISTENT_WITH_TO" reject code.

Rationale: The train for which the Movement Permission shall be granted has to be present.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TO_READY

The MBS shall check that train data has been received and acknowledged for the train referenced in the request and if the check fails, the MBS shall send a "TO_NOT_READY" reject code.

Rationale: The OBU accepts a Movement Authority only if the train data has been acknowledged.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TOPO1

The MBS shall check that every referenced topology element in the request exists in the currently active topology and if the check fails, the MBS shall send a "INVALID TOPOLOGY" reject code.

Rationale: Referencing a different topology could possibly lead into a wrongly issued Movement Authority.

---

## Guidance:

Every topology reference in the request (mainly Track Edges, Track Edges Links and Track Edge Points) shall match the currently active topology objects.

Operational Rules: None

Engineering Rules: None

## REQ-TOPO2

MBS shall check that every LinkedPath in the request is well-formed (i.e. is truly a LinkedPath) and if the check fails, the MBS shall send a "INVALID_TOPOLOGY" reject code.

---

Rationale: Every Linked Path shall be correctly formed (contiguous non branching path on the network)

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TOPO3

The MBS shall check that any attributes that can have different values along the Movement Permission are covering the full extent of the Movement Permission and if the check fails, the MBS shall send a "INVALID_TOPOLOGY" reject code.

Rationale:

Every attribute (like Movement Mode) shall cover the full Movement Permission Extent.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TOPO4

The MBS shall check that the last Movement Permission Extent Segment in running direction and the Risk Buffer form a contiguous path and if the check fails, the MBS shall send a "INVALID_TOPOLOGY" reject code.

Rationale: The Risk Buffer has to be a direct extension of the end of the train’s running path and shall not branch off it or start somewhere along the path.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TOPO5

The MBS shall check that the Train Location of the Train Object the MP Requests refers to, is completely overlapped by the Movement Permission Extent given within the request.

Rationale: If all Movement Permission Path Segment are outside the Train Location of the Train Object, the train could not move. Additionally, any switchable

---

element below the Train Objects Location shall be in the proper state when a movement happens.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TRANSLATE

The MBS shall translate the requested MP into an Authorisation as if it was granted. If the translation from a Movement Permission into an Authorisation fails, MBS shall send a "MA_CONSTRUCTION_FAILED" reject code.

Rationale: e.g. if the MP results in an Authorisation longer than 500 bytes. it shall not be accepted.

Guidance: None

Operational Rules: None

Engineering Rules: None

##### 6.11.4.2 Speed and Mode related Safety Checks

## REQ-SC_MP_SPEED

At every location along the Movement Permission Extent, the MBS shall check that the maximum speed given in the requested Movement Permission is equal to or lower than the maximum speed defined in the topology at that location for the concerned train and if the check fails, the MBS shall send a "SPEED_PROFILE" rejection code.

Rationale: The Movement Permission is to be translated into a Movement Authority and the train shall not exceed the maximum speed on the network for the concerned train (possibly considering the train cant deficiency, other train category, train axle load,...).

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC RB SPEED

At every location along the Risk Buffer, the MBS shall check that the maximum speed given in the requested Movement Permission is equal to or lower than the maximum speed defined in the topology at that location for the concerned train and if the check fails, the MBS shall send a "SPEED_PROFILE" rejection code.

---

Rationale: The Movement Permission is to be translated into a Movement Authority and the train shall not exceed the maximum speed on the network for the concerned train (possibly considering the train cant deficiency, other train category, train axle load, …). The Static Speed Profile has to be defined until the SvL (i.e. the danger point inside the Risk Buffer).

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC_MP_SPEED_LOWER

If a Movement Permission is already present for a Train Object, the MBS shall check that the speed in the request is at every point equal to or higher than in the existing Movement Permission and if the check fails, the MBS shall send a "SPEED_LOWER" rejection code.

Rationale: If the speed in the new MP is lower than in the currently active MP, it is not guaranteed that the train is able to brake. Thus, MBS rejects the MP request if the requested speed is lower than the one already sent to the OBU.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC MODE

The MBS shall check that the movement mode along the Movement Permission only consists of FS or OS and if the check fails, the MBS shall send a "SAFETY RESPONSIBILITY PROFILE_INVALID" reject code.

Rationale: Currently only FS and OS are in scope for the MBS.

Guidance: The current version of this requirement is only concerning train movements in Full Supervision and or On Sight.

Operational Rules: None

Engineering Rules: None

## REQ-SC MP MODE MISMATCH

If a Movement Permission is already present for a Train Object, the MBS shall check that the movement mode of the requested Movement Permission is either FS or equals the mode of the existing Movement Permission and if the check fails, the MBS shall send a "SAFETY RESPONSIBILITY PROFILE MISMATCH" rejection code.

Rationale: If the train shall operate in a different mode, a change on time is not guaranteed.

---

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-SC_MP_SHORTER

If a Movement Permission is already present for a Train Object, the MBS shall check that the requested Movement Permission Extent is equal to or longer than the existing Movement Permission Extent and if the check fails, the MBS shall send a "MP_SHORTER" rejection code.

Rationale: If the new Movement Permission is shorter than the currently active Movement Permission, it is not guaranteed that the train is able to break in rear of the new EoA when receiving a shorter MA.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC RB SHORTER

If a Movement Permission is already present for a Train Object and the Movement Permission Extent of the requested MP equals the Movement Permission Extent of the already present MP, the MBS shall check that the requested Risk Buffer is equal to or longer than the existing Risk Buffer and if the check fails, the MBS shall send a "MP_SHORTER" rejection code.

Rationale: If the new Risk Buffer would become shorter than the currently present Risk Buffer, the train might receive an emergency brake reaction.

Guidance: None

Operational Rules: None

Engineering Rules: None

##### 6.11.4.3 Vehicle related Safety Checks

REQ-SC MP TO

The MBS shall check that, if a Movement Permission overlaps another Train Object in advance of the mSFE of the train for which the Movement Permission is requested, the mode for that part is OS, and if the check fails, the MBS shall send a "PATH_OCCUPIED" reject code.

---

Rationale: The running path of a train shall be free of other vehicles if operating under FS.

Guidance:

[
  {
    "Component": "Movement Permission Extent",
    "Description": "The movement permission to move."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The risk buffer."
  },
  {
    "Component": "Train Object",
    "Description": "The train object."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The movement permission for the object."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The risk buffer for the object."
  },
  {
    "Component": "Unresolved Trackbound Object",
    "Description": "The unresolved trackbound object."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Train Object",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Allocation Section",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "left",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "right",
    "Description": "Unresolved Trackbound Object"
  },
  {
    "Component": "left",
    "Description": "Allocation Section"
  },
  {
    "Component": "right",
    "Description": "Allocation Section"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Buffer",
    "Description": "The first stage where the Risk Transfer System is expected to occur."
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The second stage where the Risk Transfer System is expected to occur."
  },
  {
    "Component": "Train Object",
    "Description": "The third stage where the Risk Transfer System is expected to occur."
  },
  {
    "Component": "Allocation Section",
    "Description": "The fourth stage where the Risk Transfer System is expected to occur."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Buffer",
    "Description": "The first layer of the risk layer."
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The second layer of the risk layer."
  },
  {
    "Component": "Unresolved Trackbound Object",
    "Description": "The third layer of the risk layer."
  },
  {
    "Component": "Allocation Section",
    "Description": "The fourth layer of the risk layer."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "left",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "right",
    "Description": "Allocation Section"
  },
  {
    "Component": "left",
    "Description": "Risk Buffer"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "left",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "right",
    "Description": "Allocation Section"
  },
  {
    "Component": "left",
    "Description": "Risk Buffer"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Train Object",
    "Description": "The left hand and the right hand."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The left hand hand."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The right hand hand."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Path",
    "Description": "The path to the risk."
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The extent to which the risk is allowed to be allowed."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The function to be allowed to be allowed."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "left",
    "Description": "Start of flow"
  },
  {
    "Component": "right",
    "Description": "End of flow"
  },
  {
    "Component": "left",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "right",
    "Description": "Allocation Section"
  },
  {
    "Component": "left",
    "Description": "Risk Buffer"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "left",
    "Description": "Start of flow"
  },
  {
    "Component": "right",
    "Description": "End of flow"
  },
  {
    "Component": "left",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "right",
    "Description": "Allocation Section"
  },
  {
    "Component": "left",
    "Description": "Risk Buffer"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "Risk Path",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "DPS in state FULL",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "DPS in state NONE",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "Risk Buffer",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "Risk Path",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "DPS in state FULL",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "DPS in state NONE",
    "Description": "The left hand and right hand."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission",
    "Description": "Permission to move."
  },
  {
    "Component": "Allocation Section",
    "Description": "Section to分配."
  },
  {
    "Component": "Risk Path",
    "Description": "Path to risk."
  },
  {
    "Component": "DPS in state FULL",
    "Description": "Full."
  },
  {
    "Component": "DPS in state NONE",
    "Description": "None."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Movement Permission"
  },
  {
    "Component": "Allocation Section"
  },
  {
    "Component": "Risk Path"
  },
  {
    "Component": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Buffer",
    "Description": "The first layer of risk management."
  },
  {
    "Component": "Movement Permission",
    "Description": "The second layer of risk management."
  },
  {
    "Component": "Risk Path",
    "Description": "The third layer of risk management."
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "DPS",
    "Description": "DPS 1.2"
  },
  {
    "Component": "TE1",
    "Description": "TEE1"
  },
  {
    "Component": "TE2",
    "Description": "TEE2"
  },
  {
    "Component": "DPS",
    "Description": "DPS 1.1"
  },
  {
    "Component": "TE3",
    "Description": "TEE3"
  },
  {
    "Component": "TE5",
    "Description": "TEE5"
  },
  {
    "Component": "Risk Path",
    "Description": "Risk Path"
  },
  {
    "Component": "DPS in state FULL",
    "Description": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE",
    "Description": "DPS in state NONE"
  },
  {
    "Component": "Section",
    "Description": "Description"
  },
  {
    "Component": "TE1",
    "Description": "Allocation Section"
  },
  {
    "Component": "TE2",
    "Description": "DPS 1.1"
  },
  {
    "Component": "TE3",
    "Description": "DPS 1.2"
  },
  {
    "Component": "TE4",
    "Description": "DPS 2.2"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "DPS 1.2"
  },
  {
    "Component": "Risk Path",
    "Description": "DPS 2.1"
  },
  {
    "Component": "DPS in state FULL",
    "Description": "DPS 2.2"
  },
  {
    "Component": "DPS in state NONE",
    "Description": "DPS 2.1"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Buffer",
    "Description": "The first layer of risk management."
  },
  {
    "Component": "Movement Permission",
    "Description": "The second layer of risk management."
  },
  {
    "Component": "Risk Path",
    "Description": "The third layer of risk management."
  },
  {
    "Component": "Section",
    "Description": "Description"
  },
  {
    "Component": "DPS1.1",
    "Description": "DPS 1.1"
  },
  {
    "Component": "DPS1.2",
    "Description": "DPS 1.2"
  },
  {
    "Component": "DPS2.1",
    "Description": "DPS 2.1"
  },
  {
    "Component": "DPS2.2",
    "Description": "DPS 2.2"
  },
  {
    "Component": "DPS3.1",
    "Description": "DPS 3.1"
  },
  {
    "Component": "DPS3.2",
    "Description": "DPS 3.2"
  },
  {
    "Component": "Allocation Section",
    "Description": "Allocation Section"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "Risk Path",
    "Description": "Risk Path"
  },
  {
    "Component": "DPS in state FULL",
    "Description": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE",
    "Description": "DPS in state NONE"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Train Object",
    "Description": "The training data."
  },
  {
    "Component": "Risk Path",
    "Description": "The路演路径."
  },
  {
    "Component": "Section",
    "Description": "Description"
  },
  {
    "Component": "Allocation Section",
    "Description": "Allocation Section"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "Risk Path",
    "Description": "Risk Path"
  },
  {
    "Component": "DPS in state FULL",
    "Description": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE",
    "Description": "DPS in state NONE"
  },
  {
    "Component": "Stage",
    "Description": "Description"
  },
  {
    "Component": "1",
    "Description": "Allocation Section"
  },
  {
    "Component": "2",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "3",
    "Description": "Risk Path"
  },
  {
    "Component": "4",
    "Description": "DPS in state FULL"
  },
  {
    "Component": "5",
    "Description": "DPS in state NONE"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Train Object"
  },
  {
    "Component": "Allocation Section"
  },
  {
    "Component": "Movement Permission Extent"
  },
  {
    "Component": "Risk Path"
  },
  {
    "Component": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Unresolved Trackbound Object",
    "Description": "The first level of resolution."
  },
  {
    "Component": "Allocation Section",
    "Description": "The second level of resolution."
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "The third level of resolution."
  },
  {
    "Component": "Risk Path",
    "Description": "The fourth level of resolution."
  },
  {
    "Component": "DPS in state FULL",
    "Description": "The fifth level of resolution."
  },
  {
    "Component": "DPS in state NONE",
    "Description": "The fifth level of resolution."
  },
  {
    "Component": "Section",
    "Description": "Description"
  },
  {
    "Component": "DPS",
    "Description": "DPS 1.2"
  },
  {
    "Component": "Allocation Section",
    "Description": "Allocation Section"
  },
  {
    "Component": "Movement Permission Extent",
    "Description": "Movement Permission Extent"
  },
  {
    "Component": "Risk Path",
    "Description": "Risk Path"
  },
  {
    "Component": "DPS in state FULL",
    "Description": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE",
    "Description": "DPS in state NONE"
  },
  {
    "Component": "Component",
    "Description": "Description"
  },
  {
    "Component": "Risk Buffer"
  },
  {
    "Component": "Allocation Section"
  },
  {
    "Component": "Movement Permission Extent"
  },
  {
    "Component": "Risk Path"
  },
  {
    "Component": "DPS in state FULL"
  },
  {
    "Component": "DPS in state NONE"
  },
  {
    "Component": "REQ-TrainLoc-11",
    "Description": "FOR FURTHER RELEASE"
  },
  {
    "Component": "The MBS shall remove the Train Location for a train which has completely left the Area of Control.",
    "Description": "The MBS shall remove the Train Location for a train which has completely left the Area of Control."
  },
  {
    "Component": "Rationale:",
    "Description": "Rationale:"
  },
  {
    "Component": "The MBS does not need to maintain a Train Location for trains beyond its Area of Control.",
    "Description": "The MBS does not need to maintain a Train Location for trains beyond its Area of Control."
  },
  {
    "Component": "Guidance:",
    "Description": "Guidance:"
  },
  {
    "Component": "This applies to both Handovers and Transitions.",
    "Description": "This applies to both Handovers and Transitions."
  },
  {
    "Component": "How the removal is achieved is project specific. Options include:",
    "Description": "How the removal is achieved is project specific. Options include:"
  },
  {
    "Component": "• Monitoring the Train Location for a train which is leaving the Area of Control, until it is completely beyond the boundary of the Area of Control.",
    "Description": "• Monitoring the Train Location for a train which is leaving the Area of Control, until it is completely beyond the boundary of the Area of Control."
  },
  {
    "Component": "• Truncating the Train Location at the boundary for a train which is leaving the Area of Control, until it has zero length within the Area of Control.",
    "Description": "• Truncating the Train Location at the boundary for a train which is leaving the Area of Control, until it has zero length within the Area of Control."
  },
  {
    "Component": "It is also possible to use short TTD sections at boundaries of the Area of Control to determine when a train has left the area.",
    "Description": "It is also possible to use short TTD sections at boundaries of the Area of Control to determine when a train has left the area."
  },
  {
    "Component": "Projects may decide to maintain the Train Location beyond the border until ordering the train to terminate the communication session.",
    "Description": "Projects may decide to maintain the Train Location beyond the border until ordering the train to terminate the communication session."
  },
  {
    "Component": "Projects may decide to implement different solutions at different borders of the Area of Control.",
    "Description": "Projects may decide to implement different solutions at different borders of the Area of Control."
  },
  {
    "Component": "Operational Rules:",
    "Description": "None"
  },
  {
    "Component": "Engineering Rules:",
    "Description": "None"
  },
  {
    "Component": "REQ-0045",
    "Description": "REQ-0045"
  },
  {
    "Component": "The MBS shall be able to perform all the functions of the RBC Basic Interoperability Constituent (IC) in the Control-Command and Signalling Trackside Subsystem (see /BalnCon/)",
    "Description": "The MBS shall be able to perform all the functions of the RBC Basic Interoperability Constituent (IC) in the Control-Command and Signalling Trackside Subsystem (see /BalnCon/)"
  },
  {
    "Component": "Rationale:",
    "Description": "From ETCS point of view, the MBS is an RBC Basic Interoperability Constituent (IC). The MBS supplier shall supply an RBC-IC NoBo Certificate for his MBS Product."
  },
  {
    "Component": "Guidance:",
    "Description": "None"
  },
  {
    "Component": "Operational Rules:",
    "Description": "None"
  },
  {
    "Component": "Engineering Rules:",
    "Description": "None"
  },
  {
    "Component": "REQ-0010",
    "Description": "FOR FURTHER RELEASE"
  },
  {
    "Component": "MBS shall log all incoming and outgoing messages to the I_DIAG interface.",
    "Description": "MBS shall log all incoming and outgoing messages to the I_DIAG interface."
  },
  {
    "Component": "Rationale:",
    "Description": "This is requested for diagnostic."
  },
  {
    "Component": "Guidance:",
    "Description": "None"
  },
  {
    "Component": "Operational Rules:",
    "Description": "None"
  },
  {
    "Component": "Engineering Rules:",
    "Description": "None"
  },
  {
    "Component": "REQ-0046",
    "Description": "FOR FURTHER RELEASE"
  },
  {
    "Component": "If an OBU message has to be acknowledged (M_ACK = 1), MBS shall repeat this message periodically until the OBU acknowledgement is received.",
    "Description": "If an OBU message has to be acknowledged (M_ACK = 1), MBS shall repeat this message periodically until the OBU acknowledgement is received."
  },
  {
    "Component": "Rationale:",
    "Description": "MBS should send again a message if the OBU acknowledgement is not received after a period, because there is a risk that the OBU has not received the message."
  },
  {
    "Component": "Guidance:",
    "Description": "None"
  },
  {
    "Component": "Operational Rules:",
    "Description": "None"
  },
  {
    "Component": "Engineering Rules:",
    "Description": "None"
  },
  {
    "Component": "/BalnCon/",
    "Description": "Basic interoperability constituents in the Control-Command and Signalling Trackside SubsystemTable 5.2 in Legal framework of /CCSTSI/"
  },
  {
    "Component": "/SysDef/",
    "Description": "R2DATOD13.1 - Moving Block Specifications applying a train-centric approachPart 1 - System Definition"
  },
  {
    "Component": "/CCSTSI/",
    "Description": "Control Command and Signalling TSICommission Implementing Regulation (EU) 2023/1695 of 10 August 2023"
  },
  {
    "Component": "/ETCS/",
    "Description": "ETCS SpecificationsAnnex A for the /CCSTSI/Set of Specifications (ETCS B4 R1)"
  },
  {
    "Component": "/S2R/",
    "Description": "S2RMoving Block Specification Releasehttps://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5f58a710a&amp;appId=PPGMS"
  },
  {
    "Component": "/RCA/",
    "Description": "RACARCA Baseline 1 Release 0https://public.3.basecamp.com/p/KeehzqFmXv5R2N7tGDjaEokq"
  },
  {
    "Component": "/EULYNX/",
    "Description": "EuLynxBaseline Set 4 Release 2https://rail-research.europa.eu/system_pillar/system-pillar-outputs/trackside-assets-specifications/"
  },
  {
    "Component": "/SD1DM/",
    "Description": "SPT2-TransversalSystemsTCCS SD1 - Data Model"
  },
  {
    "Component": "/EuArch/",
    "Description": "Eu.Doc.16 - EULYNX System architecture specification"
  },
  {
    "Component": "/POS/",
    "Description": "Eu.Doc.100 - Specification of Point of Service"
  },
  {
    "Component": "/SCI/",
    "Description": "Eu.Doc.92 - Interface definition SCI"
  },
  {
    "Component": "/SCI-Gen/",
    "Description": "Eu.Doc.93 - Interface specification SCI Generic"
  },
  {
    "Component": "/SCI-P/",
    "Description": "Eu.Doc.38 - Interface specification SCI-P"
  },
  {
    "Component": "/SCI-TDS/",
    "Description": "Eu.Doc.44 - Interface specification SCI-TDS"
  },
  {
    "Component": "/SCI-LX/",
    "Description": "Eu.Doc.112 - Interface specification SCI-LX"
  },
  {
    "Component": "/SCI-GenIF/",
    "Description": "Eu.Doc.119 - Generic interface and subsystem requirements for SCI"
  },
  {
    "Component": "/ReqSubsP/",
    "Description": "Eu.Doc.36 - Requirements specification for subsystem Point"
  },
  {
    "Component": "/OpCon/",
    "Description": "SP-CCS-TMS-CMS-Operational-vision.pdf (europa.eu) (?)"
  },
  {
    "Component": "/RCA.Doc.61/",
    "Description": "RCAAPS Concept Operating State and APS Domain Objects"
  },
  {
    "Component": "/RCA.Doc.62/",
    "Description": "RCAAPS Concept: Route setting and route protection"
  },
  {
    "Component": "/GSL/",
    "Description": "Geometric Safety Logic in a nutshellNote: this document already uses other abstract concepts than Drive Protection Section which are not yet agreed in the authors&#x27; working group. Please take them as indicative for understanding."
  },
  {
    "Component": "/FlankProtection/",
    "Description": "ADI.023 Concept: Flank Protection (Allocation Section, Risk Path)"
  },
  {
    "Component": "/SempR2/",
    "Description": "SEMP Annex R2 - Requirements patterns syntax"
  },
  {
    "Component": "/SempR3/",
    "Description": "SEMP Annex R3 - Rules for writing textual requirements"
  },
  {
    "Component": "Chapter",
    "Description": "Reviewer"
  },
  {
    "Component": "REQ-0010",
    "Description": "Ivan"
  },
  {
    "Component": "8.7 SYSFESTABLISH COMMUNICATION SESSION WITH TACS",
    "Description": "Daniel"
  },
  {
    "Component": "REQ-0016",
    "Description": "Ivan"
  },
  {
    "Description": "Kostas"
  },
  {
    "Component": "8.9 SYS F LOAD AND CHECK DOMAIN DATA",
    "Description": "Kostas"
  },
  {
    "Component": "Description",
    "Description": "&lt;description&gt;"
  },
  {
    "Component": "Goal",
    "Description": "&lt;description&gt;"
  },
  {
    "Component": "Precondition(s)",
    "Description": "- &lt;precondition&gt;"
  },
  {
    "Component": "Postcondition(s)(Success)",
    "Description": "- &lt;postcondition&gt;"
  },
  {
    "Component": "Postcondition(s)(Failure)",
    "Description": "- &lt;postcondition&gt;"
  },
  {
    "Component": "Involved actor(s)",
    "Description": "- &lt;actor&gt;"
  },
  {
    "Component": "Trigger(s)",
    "Description": "- &lt;trigger&gt;"
  },
  {
    "Component": "Main Sequence",
    "Description": "&lt;(link to related scenario)&gt;"
  },
  {
    "Component": "Alternate Sequence",
    "Description": "&lt;(link to related scenario)&gt;"
  },
  {
    "Component": "Failure Sequence",
    "Description": "&lt;(link to related scenario)&gt;"
  },
  {
    "Component": "Comments",
    "Description": "&lt;additional&gt;"
  }
]

## Scenario: Template Scenario

The scenario “Template Scenario” is shown. It contains a description of the elements to be used in the scenarios and some examples.

---

This Visio file template is available inside Project Place, directory "System Specification"

[
  {
    "Document status": "Description"
  },
  {
    "Document status": "Draft for internal review"
  },
  {
    "Document status": "Draft for internal review"
  },
  {
    "Document status": "Internal review comment implemented"
  },
  {
    "Document status": "Update to new document template"
  },
  {
    "Document status": "JU comments solved"
  },
  {
    "Document status": "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme"
  },
  {
    "Document status": "Dissemination Level"
  },
  {
    "Document status": "X"
  },
  {
    "Document status": "Sensitive - limited under the conditions of the Grant Agreement"
  },
  {
    "Document status": "Details of Contribution"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author"
  },
  {
    "Document status": "Author / Task Lead"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  },
  {
    "Document status": "Reviewer"
  }
]

## Disclaimer

The information in this document is provided “as is”, and no guarantee or warranty is given that the information is fit for any particular purpose. The content of this document reflects only the author's view – the Joint Undertaking is not responsible for any use that may be made of the information it contains. The users use the information at their sole risk and liability.

---

## ABBREVIATIONS AND ACRONYMS


[
  {
    "AoC": "APS",
    "Area of Control": "Advanced Protection System"
  },
  {
    "AoC": "AS",
    "Area of Control": "Adjacent System (neighbouring systems)"
  },
  {
    "AoC": "ASM",
    "Area of Control": "Assumption"
  },
  {
    "AoC": "CBO",
    "Area of Control": "Common Business Objectives"
  },
  {
    "AoC": "CCS",
    "Area of Control": "Command, Control, and Signalling"
  },
  {
    "AoC": "CELEX",
    "Area of Control": "Communitatis Europaea Lex"
  },
  {
    "AoC": "CES",
    "Area of Control": "Conditional Emergency Stop"
  },
  {
    "AoC": "CMD",
    "Area of Control": "Cold Movement Detection"
  },
  {
    "AoC": "CS",
    "Area of Control": "Control and Supervision"
  },
  {
    "AoC": "CSM-RA",
    "Area of Control": "Common Safety Method for Risk Evaluation and Assessment"
  },
  {
    "AoC": "DMI",
    "Area of Control": "Driver Machine Interface"
  },
  {
    "AoC": "DPS",
    "Area of Control": "Drive Protection Section"
  },
  {
    "AoC": "DR",
    "Area of Control": "Digital Register"
  },
  {
    "AoC": "EB",
    "Area of Control": "Emergency brake"
  },
  {
    "AoC": "EoM",
    "Area of Control": "End of Mission"
  },
  {
    "AoC": "ERA",
    "Area of Control": "European Railway Agency"
  },
  {
    "AoC": "ERJU",
    "Area of Control": "Europe&#x27;s Rail Joint Undertaking"
  },
  {
    "AoC": "ERTMS",
    "Area of Control": "European Rail Traffic Management System"
  },
  {
    "AoC": "ETCS",
    "Area of Control": "European Train Control System"
  },
  {
    "AoC": "EULYNX",
    "Area of Control": "European initiative by 14 Infrastructure Managers to standardise interfaces and elements of the signalling systems"
  },
  {
    "AoC": "FA",
    "Area of Control": "Flagship Area (1 or 2) of ERJU IP"
  },
  {
    "AoC": "FRMCS",
    "Area of Control": "Future Railway Mobile Communication System"
  },
  {
    "AoC": "FS",
    "Area of Control": "Full Supervision"
  },
  {
    "AoC": "GSMR",
    "Area of Control": "Global System for Mobile Communications – Railway"
  },
  {
    "AoC": "HCS",
    "Area of Control": "Hierarchical Control Structure"
  },
  {
    "AoC": "ID",
    "Area of Control": "Unique Identifier"
  },
  {
    "AoC": "IM",
    "Area of Control": "Infrastructure Manager"
  },
  {
    "AoC": "IP",
    "Area of Control": "Innovation Pillar"
  },
  {
    "AoC": "IVV",
    "Area of Control": "Integration, Verification and Validation"
  }
]

---

## FP2R2DATO


[
  {
    "IXL": "JU",
    "Interlocking": "Joint Undertaking"
  },
  {
    "IXL": "L2",
    "Interlocking": "Level 2 (ETCS level definition)"
  },
  {
    "IXL": "L3",
    "Interlocking": "Level 3 (ETCS level definition), obsolete with enactment of TSI 2023"
  },
  {
    "IXL": "LX",
    "Interlocking": "Level Crossing"
  },
  {
    "IXL": "MA",
    "Interlocking": "Movement Authority"
  },
  {
    "IXL": "MBD",
    "Interlocking": "Moving Block Demonstrator"
  },
  {
    "IXL": "MBS",
    "Interlocking": "Moving Block System"
  },
  {
    "IXL": "OBU",
    "Interlocking": "On-Board Unit"
  },
  {
    "IXL": "OC",
    "Interlocking": "Object Controller"
  },
  {
    "IXL": "OM",
    "Interlocking": "Operations Manager"
  },
  {
    "IXL": "OS",
    "Interlocking": "On Sight"
  },
  {
    "IXL": "PDI",
    "Interlocking": "Process Data Interface protocol"
  },
  {
    "IXL": "PE",
    "Interlocking": "Plan Execution"
  },
  {
    "IXL": "Picop",
    "Interlocking": "Person in charge of possession"
  },
  {
    "IXL": "PKI",
    "Interlocking": "Public Key Infrastructure"
  },
  {
    "IXL": "PRAMSS",
    "Interlocking": "Performance Reliability Availability Maintainability Safety and Security"
  },
  {
    "IXL": "R2DATO",
    "Interlocking": "Rail to Digital automated up to autonomous train operation"
  },
  {
    "IXL": "RAMS",
    "Interlocking": "Reliability, Availability, Maintainability and Safety"
  },
  {
    "IXL": "RBC",
    "Interlocking": "Radio Block Centre"
  },
  {
    "IXL": "RCA",
    "Interlocking": "Reference CCS Architecture"
  },
  {
    "IXL": "Ref",
    "Interlocking": "Reference"
  },
  {
    "IXL": "RU",
    "Interlocking": "Railway Undertaking"
  },
  {
    "IXL": "SB",
    "Interlocking": "Stand By"
  },
  {
    "IXL": "SCI",
    "Interlocking": "Standard Command Interface"
  },
  {
    "IXL": "SCP",
    "Interlocking": "Safe Communication Protocol"
  },
  {
    "IXL": "SDI",
    "Interlocking": "Standard Diagnostics Interface"
  },
  {
    "IXL": "SDR",
    "Interlocking": "Safety Design Recommendation"
  },
  {
    "IXL": "SFE",
    "Interlocking": "Safe Front End"
  },
  {
    "IXL": "SH",
    "Interlocking": "Shunting"
  },
  {
    "IXL": "SIL",
    "Interlocking": "Safety Integrity Level"
  },
  {
    "IXL": "SL",
    "Interlocking": "Sleeping"
  },
  {
    "IXL": "SLC",
    "Interlocking": "System Level Constraints"
  }
]

---

## FP2R2DATO


[
  {
    "SMI": "SOC",
    "Standard Maintenance Interface": "Security Operations Centre"
  },
  {
    "SMI": "SoM",
    "Standard Maintenance Interface": "Start of Mission"
  },
  {
    "SMI": "SP",
    "Standard Maintenance Interface": "System Pillar"
  },
  {
    "SMI": "SPAD",
    "Standard Maintenance Interface": "Signal Passed At Danger"
  },
  {
    "SMI": "SR",
    "Standard Maintenance Interface": "Staff Responsible"
  },
  {
    "SMI": "SRE",
    "Standard Maintenance Interface": "Safe Rear End"
  },
  {
    "SMI": "STAMP",
    "Standard Maintenance Interface": "System-Theoretic Accident Model and Processes"
  },
  {
    "SMI": "STPA",
    "Standard Maintenance Interface": "System-Theoretic Process Analysis"
  },
  {
    "SMI": "SuC",
    "Standard Maintenance Interface": "System under Consideration"
  },
  {
    "SMI": "SysC",
    "Standard Maintenance Interface": "System Capability"
  },
  {
    "SMI": "SysF",
    "Standard Maintenance Interface": "System Function"
  },
  {
    "SMI": "TA",
    "Standard Maintenance Interface": "Trackside Assets"
  },
  {
    "SMI": "TACS",
    "Standard Maintenance Interface": "Trackside Asset Control and Supervision"
  },
  {
    "SMI": "TAF",
    "Standard Maintenance Interface": "Track Ahead Free"
  },
  {
    "SMI": "TBD",
    "Standard Maintenance Interface": "To Be Defined"
  },
  {
    "SMI": "TDS",
    "Standard Maintenance Interface": "Train Detection System"
  },
  {
    "SMI": "TIM",
    "Standard Maintenance Interface": "Train Integrity Monitoring"
  },
  {
    "SMI": "TIMS",
    "Standard Maintenance Interface": "Train Integrity Monitoring System"
  },
  {
    "SMI": "TMS",
    "Standard Maintenance Interface": "Traffic Management System"
  },
  {
    "SMI": "TRL",
    "Standard Maintenance Interface": "Technology Readiness Level"
  },
  {
    "SMI": "TTD",
    "Standard Maintenance Interface": "Trackside Train Detection"
  },
  {
    "SMI": "TU",
    "Standard Maintenance Interface": "Train Unit"
  },
  {
    "SMI": "UA",
    "Standard Maintenance Interface": "Unsupervised Area"
  },
  {
    "SMI": "UCA",
    "Standard Maintenance Interface": "Unsafe Control Action"
  },
  {
    "SMI": "UES",
    "Standard Maintenance Interface": "Unconditional Emergency Stop"
  },
  {
    "SMI": "URA",
    "Standard Maintenance Interface": "Usage Restriction Area"
  },
  {
    "SMI": "WP",
    "Standard Maintenance Interface": "Work Package"
  },
  {
    "SMI": "WSP",
    "Standard Maintenance Interface": "Wheel Slip Protection"
  }
]

---

GLOSSARY

Check: General procedure which ascertains if certain conditions hold (e.g., [check if] each end of a railway point is connected to a track section).

Configuration Data: Further information relevant for system operation that is not contained in topology, topography or infrastructure data (e.g., identifiers & connection parameters for object controllers and parameters for safety checks.)

Static Speed Profile: A static speed profile that is dynamically calculated by MBS and subsequently provided to the relevant train onboard unit.

Hazard: A hazard is defined as “a system state or set of conditions that, together with a particular set of worst-case environmental conditions, will lead to a loss”  $ [1] $ .

Infrastructure data: Additional information not contained in the topography but necessary for physical train operations (e.g., static speed profiles, cant, ...)

Loss: Within STPA, a loss is defined as an unacceptable event which harms “something of value to stakeholders.”  $ [1] $ . Typical values to protect include human life (loss of life), system function (loss of mission), the environment (loss of environment), etc.

Movement Authority: Permission for a train to run to a specific location within the constraints of the infrastructure  $ [19] $ .

Movement Permission: Request from PE to MBS to grant a defined MA for a certain train.

Safety Design Recommendation: Exported less stringent “recommendation” regarding the findings in this document versus more stringent “safety requirements” that may result from a later generation of this analysis.

Safety Requirement: A requirement based on findings from a safety analysis (see safety design recommendation).

Safety Responsibility: Defined responsibility with regards to safety functions of individual actors, systems or sub-systems.

Topography: Refers to geographical map information regarding the features of the terrain that correctly represent physical reality (geographical position, elevation, ...).

Topology: Subset of topography with linked track sections and identified track elements.

Unsafe Control Action: “An Unsafe Control Action (UCA) is a control action that, in a particular context and worst-case environment, will lead to a hazard” $ ^{[1]} $ .

System Level Constraints: "A system-level constraint specifies system conditions or behaviours that need to be satisfied to prevent hazards (and ultimately prevent losses)"  $ [1] $ .

Validation: "Confirmation, through the provision of objective evidence, that the requirements for a specific intended use or application have been fulfilled." $ ^{[3]} $  This means validation is intended to ensure that the MBS meets the operational needs of the user.

Verification: "Confirmation, through the provision of objective evidence, that specified requirements have been fulfilled."[3] This means verification is intended to check that the MBS meets its set of design specifications.

---

## TABLE OF CONTENTS

AcknowledgementS ..... 3  
Report Contributors ..... 3  
Abbreviations and Acronyms ..... 4  
Glossary ..... 7  
Table of Contents ..... 8  
List of Figures ..... 11  
List of Tables ..... 11  
1 Introduction ..... 14  
2 Scope ..... 16  
2.1 System Boundary ..... 16  
2.2 Connected Systems ..... 17  
2.2.1 Neighbouring (MBS/RBC) System ..... 17  
2.2.2 Diagnostics System ..... 18  
2.2.3 Digital Register ..... 18  
2.2.4 ETCS on-board ..... 18  
2.2.5 Operator Panel ..... 19  
2.2.6 Plan Execution ..... 19  
2.2.7 Security Service ..... 19  
2.2.8 Trackside Asset Control and Supervision ..... 19  
2.2.9 IM Data System ..... 20  
2.2.10 Traffic Management System ..... 20  
3 Inputs ..... 21  
3.1 System Pillar Inputs ..... 21  
3.1.1 CBO ([6], p.18) - Optimize safety strategies and standards ..... 21  
3.1.2 Operational Vision ([7], p.20) - Enhanced safety assurance process ..... 21  
3.1.3 Operational Scenarios ..... 21  
3.2 X2Rail Documentation ..... 22  
3.3 RCA Documents ..... 22  
3.4 R2DATO Documents ..... 22  
4 Safety Analysis Methodeology ..... 23  
4.1 COMMON SAFETY METHODS ..... 24  
4.2 CENELEC STANDARDS ..... 24  
4.3 STPA ..... 24  
5 Risk Analysis ..... 24  
5.1 Losses ..... 25

---

5.2 Hazards ..... 26  
5.3 System Level Constraints ..... 29  
5.3.1 Collision Avoidance ..... 29  
5.3.2 Clearance Gauge – Derailment ..... 30  
5.3.3 High Forces ..... 31  
5.3.4 Runaway Trains ..... 31  
5.3.5 Unsafe Regions ..... 32  
5.3.6 Utilization Conditions ..... 32  
5.4 Hierarchical Control Structure (HCS) ..... 33  
5.5 Assumptions ..... 35  
5.6 Safety Responsibilities ..... 38  
5.6.1 Moving Block System (MBS) ..... 38  
5.6.2 Infrastructure Manager (IM) ..... 42  
5.6.3 Operator ..... 43  
5.6.4 Driver ..... 44  
5.6.5 On Board Unit (OBU) ..... 45  
5.6.6 Maintenance workers ..... 46  
5.6.7 Digital Register ..... 46  
5.7 Control Loop Analysis ..... 48  
5.7.1 I_OP Interface ..... 48  
5.7.2 I_OBU Interface ..... 54  
5.7.3 I_TACS Interface ..... 61  
5.7.4 I_DR Interface ..... 65  
5.7.5 I_PE Interface ..... 70  
6 Interface Criticality ..... 72  
6.1 System Safety Boundary ..... 72  
6.2 Interface Tables ..... 73  
6.2.1 I_AS ..... 73  
6.2.2 I_DR ..... 74  
6.2.3 I_OBU ..... 75  
6.2.4 I_OP ..... 76  
6.2.5 I_PE ..... 77  
6.2.6 I_TACS ..... 78  
6.2.7 I_PEOP ..... 79  
6.2.8 I_PETMS ..... 79  
7 Mapping of X2Rail Safety Analysis ..... 80

---

7.1 4.1 Track status erroneously cleared ..... 80  
7.2 4.2 Error in train location ..... 83  
7.3 4.3 Error in Train Length ..... 85  
7.4 4.4 CMD Erroneously Validates Position ..... 86  
7.5 4.5 Undetected Movements ..... 87  
7.6 4.6 TTD erroneously indicates track clear ..... 90  
7.7 4.7 Points Moved under train ..... 90  
7.8 4.8 Hazards identified but present already in ETCS L2 ..... 91  
8 Compiled Design Recommendations ..... 93  
8.1 Unsafe Control Actions towards On Board Unit ..... 93  
8.2 Unsafe Control Actions towards Operator Panel ..... 94  
8.3 Unsafe Control Actions towards Trackside Assets Control & Supervision ..... 95  
8.4 Unsafe Control Actions regarding Domain Data & Updates ..... 96  
9 Safety Results & Conclusion ..... 100  
9.1 Structure of the Results ..... 100  
9.2 Starting Point ..... 100  
9.3 Positioning and Objectives ..... 101  
9.4 Discussion of Main Results ..... 101  
9.5 Open Points and Future Work ..... 102  
References ..... 104

---

## LIST OF FIGURES

Figure 1: Localization of MBS within a simplified view of "moving block" trackside CS ..... 14  
Figure 2 - MBS System Boundary ..... 17  
Figure 3 – Safety Analysis in Relation to the Hourglass Model ..... 23  
Figure 4: Traceability from STPA outputs from [1] ..... 25  
Figure 5 - Simple control-loop ..... 33  
Figure 6 - High level control structure of the CCS system. The red rectangle highlights the controller containing the MBS system ..... 34  
Figure 7 - Schematic second level control structure with focus on the trackside automation system. The red rectangle highlights the Moving Block Demonstrator (MBD) ..... 35  
Figure 8 - MBS System Boundary and Interface Definition ..... 72  
Figure 9: Generic Safety Logic ..... 96  
Figure 10: Example for tracing of safety responsibility for topography & configuration data ..... 97  
Figure 11: Example for tracing of safety responsibility for update URA ..... 98  
Figure 12: Example for verifying URA status ..... 99  
Figure 13: CENELEC V-Cycle ..... 101

## LIST OF TABLES

Table 1 – Neighbouring System Definition ..... 18  
Table 2 – Diagnostics System Definition ..... 18  
Table 3 – Digital Register Definition ..... 18  
Table 4 – ETCS on-board Definition ..... 18  
Table 5 – Operator Panel Definition ..... 19  
Table 6 – Plan Execution Definition ..... 19  
Table 7 – Security Service Definition ..... 19  
Table 8 – Trackside Asset Control and Supervision Definition ..... 20  
Table 9 – IM Data System Definition ..... 20  
Table 10 – Traffic Management System Definition ..... 20  
Table 11 – Losses ..... 26  
Table 12 – Hazards ..... 28  
Table 13 – Collision Avoidance ..... 30  
Table 14 – Clearance Gauge ..... 31  
Table 15 – High Forces ..... 31  
Table 16 – Runaway Trains ..... 32  
Table 17 – Unsafe Regions ..... 32  
Table 18 – Utilization Conditions ..... 32  
Table 19 – Assumptions ..... 37

---

Table 20 – Moving Block System Safety Responsibilities ..... 42  
Table 21 – Infrastructure Manager Safety Responsibilities ..... 42  
Table 22 – Operator Safety Responsibilities ..... 43  
Table 23 – Driver Safety Responsibilities ..... 45  
Table 24 – On Board Unit Safety Responsibilities ..... 46  
Table 25 – Maintenance Workers Safety Responsibilities ..... 46  
Table 26 – Digital Register Safety Responsibilities ..... 47  
Table 27 – I_AS Interface Definition ..... 73  
Table 28 – I_DR Interface Definition ..... 74  
Table 29 – I_OBU Interface Definition ..... 75  
Table 30 – I_OP Interface Definition ..... 76  
Table 31 – I_PE Interface Definition ..... 77  
Table 32 – I_TACS Interface Definition ..... 78  
Table 33 – I_PEOP Interface Definition ..... 79  
Table 34 – I_PETMS Interface Definition ..... 80  
Table 35 – 4.1.1 Dispatcher interaction in L3 Trackside initialisation ..... 80  
Table 36 – 4.1.2 Using invalid/outdated stored information for L3 Trackside initialisation ..... 81  
Table 37 – 4.1.3 Deactivating Temporary Shunting Area ..... 81  
Table 38 – 4.1.4 Driver confirms train integrity ..... 82  
Table 39 – 4.1.5 Recovery of a failed train ..... 83  
Table 40 – 4.2.1 Confidence interval reduced at End of Mission ..... 83  
Table 41 – 4.2.1 Lack of linking information ..... 84  
Table 42 – 4.3.1 Reported train length shorter than actual ..... 85  
Table 43 – 4.3.2 Reported train length longer than actual ..... 86  
Table 44 – 4.4.1 Wrong side failure of CMD ..... 86  
Table 45 – 4.5.1 Rollback after standstill ..... 87  
Table 46 – 4.5.2 Unreported Movement ..... 87  
Table 47 – 4.5.3 At entrance to Level 3 area ..... 88  
Table 48 – 4.5.4 After End of Mission ..... 89  
Table 49 – 4.5.5 Loss of Train Integrity ..... 89  
Table 50 – 4.5.6 Propelling train ..... 89  
Table 51 – 4.5.7 Shunting train ..... 90  
Table 52 – 4.6.1 Wrong side failure of TTD ..... 90  
Table 53 – 4.7.1 Points Moved After Communications failure ..... 91  
Table 54 – 4.8.1 Mixed traffic ..... 92  
Table 55 – 4.8.2 Reversing ..... 92

---

Table 56 – 4.1.1 Dispatcher interaction in L3 Trackside initialisation.....92

---

## 1 INTRODUCTION

This present document constitutes the technical contribution from Task 13.3 "Safety Analysis" to the Deliverable D13.1 "Moving Block Specifications applying a train-centric approach" in the framework of WP13, of FP2 R2DATO.

“The objective of this task was to work collaboratively to analyze the impact of System Pillar activities and Tasks (13.1 Definition/13.2 Specification) to develop a Moving Block Safety Analysis considering also the S2R results.” /R2DATO Grant Agreement/

To move a step beyond what was previously done in S2R (e.g., in-depth analysis of relevant scenarios) a novel method – called System Theoretic Process Analysis (STPA) – shall be applied to the matter. This STPA focuses on “unsafe control actions” in control and feedback loops within complex systems. An advantage over previous methods is the potential to identify emergent risks stemming from the interaction between those (sub)systems, which are often overlooked.

The subject of this analysis is the "Moving Block System" (MBS) that is being defined and specified in WP13. The figure below shows its localization within the planned Moving Block Demonstrator (MBD) from WP44/45. In this preliminary architecture it is foreseen that the MBS receives its topology model (Domain Data) from an entity designated as Digital Register (DR). Various commands and requests (e.g., requests to move a point/request to grant a movement permission) come from the Plan Execution (PE) that executes the operational plan from the Traffic Management System (TMS). On the other side, MBS facilitates communication with and also commands the Onboard-Units (OBU) and Trackside Asset Control & Supervision (TACS) – aka trackside object controllers.

[
  {
    "Attribute": "Name",
    "Content": "Neighbouring (MBS/RBC) System [Adjacent System in 13.1/13.2]"
  },
  {
    "Attribute": "Description",
    "Content": "A neighbouring System can be either another MBS, a different radio-based ETCS related neighbouring system (e.g., RBC) or e.g., an RBC/IXL combination with traditional route logic. The interface to a radio-based ETCS related neighbouring system allows trains to pass the border to/from a neighbouring Level 2 area without changing the driver responsibility and the cab-signalling."
  },
  {
    "Content": "The interface to a neighbouring system not related to radio-based ETCS allows trains to pass the border to/from an area not equipped with Level 2. The cab-signalling is replaced by optical signals and vice versa."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Management &amp; Diagnostics System"
  },
  {
    "Attribute": "Description",
    "Content": "The Diagnostics system monitors the state of the MBS and logs parameters of interest. For this purpose, MBS transmits log, status, and diagnostic data to the Diagnostic system for status evaluation and analysis."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Digital Register"
  },
  {
    "Attribute": "Description",
    "Content": "The Digital Register (DR) provides reliable (meaning complete, accurate, current, consistent, verified and validated), interoperable and accessible infrastructure information as a critical enabler for safety-related and non-safety-related functions. The Digital Register includes static infrastructure information (static speed profile, gradients, cant, etc.) and configuration data, which are approved after the engineering process. The interface between the DR and the MBS is used to update the data in the MBS."
  }
]

[
  {
    "Attribute": "Name",
    "Content": "ETCS on-board"
  },
  {
    "Attribute": "Description",
    "Content": "The ERTMS/ETCS on-board (OBU) equipment is a computer-based system that supervises the movement of the train to which it belongs, on basis of information exchanged with the MBS. Its system requirement specification is defined in UNISIG subset 26 [2]"
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Operator Panel"
  },
  {
    "Attribute": "Description",
    "Content": "The Operator Panel is a system that provides the human-machine interface with the Operations Manager in order to provide status information on the operation of the railway system and accept input for the resolution of degraded situations."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Plan Execution"
  },
  {
    "Attribute": "Description",
    "Content": "The PE operationalizes the “operational plan” or “timetable” as received from TMS via the I_OP interface. The functional split between PE and MBS is along a virtual SIL-boundary (allowing PE to be classified as SIL-basic integrity only). PE actually conceives the Movement Permissions and the individual commands for trackside assets, while MBS is a “gatekeeper” that validates (safety logic) and forwards commands and Movement Authorities to trackside assets and trains. The MBS only acts upon dedicated emergency patterns and provides the Operational State to the PE."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Security Service"
  },
  {
    "Attribute": "Description",
    "Content": "The Security Service summarises all technological systems that are necessary to manage and provide the cryptographic artefacts (e.g., keys or certificates) to ensure the confidentiality, authenticity and integrity (Information Security Triad) of the communication between subsystems."
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Trackside Asset Control and Supervision"
  },
  {
    "Attribute": "Description",
    "Content": "The Trackside Asset Control and Supervision (TACS) reports the state of the Trackside Assets (TAs). The MBS mainly uses this interface to trigger setting the state of a TA, e.g., moving a point, and to receive status information from TAs (e.g., occupancy information from TDS)"
  },
  {
    "Attribute": "Attribute",
    "Content": "Content"
  },
  {
    "Attribute": "Name",
    "Content": "Infrastructure manager (IM) Data System"
  },
  {
    "Attribute": "Description",
    "Content": "Infrastructure Manager Data System describes the body or firm responsible for the management of all relevant infrastructure data, traffic management, and control-command and signalling in alignment with key term definition in Directive 2012/34/EU."
  }
]

[
  {
    "Attribute": "Name",
    "Content": "Traffic Management System (TMS)"
  },
  {
    "Attribute": "Description",
    "Content": "Traffic Management System provides functionality for preparing and optimising the entire schedule within an Area of Control. This schedule will be represented by operational plans for each individual Train Unit. This operational plan is provided to the PE where it is operationalized into specific commands and movement permissions. PE provides the current operation state to TMS as feedback."
  }
]

[
  {
    "ID": "L-1",
    "Name": "Loss of life or injury to people on the train (including injury because of incorrect braking technique without derailment or collision)• Passengers• Railway staff (crew on the train)"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "L-2",
    "Name": "Loss of life or injury to people outside the train• Level crossing users (by any means of transportation or by foot)• People on the platform or neighbourhood of tracks• Railway workers• Trespassers (persons present on railway premises where such presence is forbidden)"
  },
  {
    "ID": "L-3",
    "Name": "Environmental loss (i.e. transport of dangerous goods)"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-1]",
    "Name": "Train does not maintain safe distance to other trains (front, back, flank)"
  },
  {
    "ID": "[H-1.1]",
    "Name": "Train deceleration is insufficient"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-1.2]",
    "Name": "Train deceleration is too late"
  },
  {
    "ID": "[H-1.3]",
    "Name": "Train passes over point which has lost its end position (“Endlage”)"
  },
  {
    "ID": "[H-1.4]",
    "Name": "Train passes over point which indicates a wrong position"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-2]",
    "Name": "Train does not maintain safe distance to other obstacles (obstacles include railway workers, vehicles on level crossings, end of line)"
  },
  {
    "ID": "[H-2.1]",
    "Name": "Train deceleration is insufficient"
  },
  {
    "ID": "[H-2.2]",
    "Name": "Train deceleration is too late"
  },
  {
    "ID": "[H-2.3]",
    "Name": "Train passes over point which has lost its end position (Endlage)"
  },
  {
    "ID": "[H-2.4]",
    "Name": "Train passes over point which indicates a wrong position"
  },
  {
    "ID": "[H-2.5]",
    "Name": "Level crossing occupied by road vehicle or pedestrians"
  },
  {
    "ID": "[H-2.6]",
    "Name": "Railway workers on track or near track (might be dangerous at high speed)"
  },
  {
    "ID": "[H-2.7]",
    "Name": "Trucks and other construction trains"
  },
  {
    "ID": "[H-2.8]",
    "Name": "Runaway railway trains"
  },
  {
    "ID": "[H-2.9]",
    "Name": "Level crossing blocked longer than necessary"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-3]",
    "Name": "Train leaves allowed/provisioned/allocated/reserved clearance gauge"
  },
  {
    "ID": "[H-3.1]",
    "Name": "Train derailment and possibly collision with railway trains or other obstacles"
  },
  {
    "ID": "[H-3.2]",
    "Name": "Train violating clearance gauge due to e.g., overhanging cargo"
  },
  {
    "ID": "[H-3.3]",
    "Name": "Train violating clearance gauge due to running on two tracks simultaneously (“Gabelfahrt”)"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-4]",
    "Name": "Train exposes passengers to high forces"
  },
  {
    "ID": "[H-4.1]",
    "Name": "Train applies non-appropriate (excessive) braking technique"
  },
  {
    "ID": "[H-4.2]",
    "Name": "Train coupling with too high speed"
  },
  {
    "ID": "[H-4.3]",
    "Name": "Train overspeeding in curves"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-5]",
    "Name": "Train exposes people outside the train to high forces (e.g., platform, level crossing, railway workers)"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-6]",
    "Name": "Train loses integrity of the train frame"
  },
  {
    "ID": "[H-6.1]",
    "Name": "Environmental damage due to loss of dangerous goods"
  },
  {
    "ID": "[H-6.2]",
    "Name": "Runaway wagon (train integrity lost - train brakes apart)"
  },
  {
    "ID": "[H-6.3]",
    "Name": "Train frame damaged due to obstacle violating clearance gauge Note: This is currently not controllable"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-7]",
    "Name": "Train enters an unsafe region (e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, etc.) or train cannot leave unsafe region (e.g., tunnel fire) in acceptable time frame"
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[H-8]",
    "Name": "Train violates utilization conditions of the infrastructure"
  },
  {
    "ID": "[H-8.1]",
    "Name": "Train exceeds maximum allowed speed - overspeeding"
  },
  {
    "ID": "[H-8.2]",
    "Name": "Train not covered by allowed train types (axle load, track gauge, clearance gauge, emergency running characteristics, air-tight system, etc.)"
  },
  {
    "ID": "[H-8.3]",
    "Name": "Damage to infrastructure after temporary change of utilization conditions, which in consequence can cause derailment of following trains."
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[SC-1]",
    "Name": "Trains must maintain a safe distance to other trains or obstacles."
  },
  {
    "ID": "[SC-1.1]",
    "Name": "Areas reserved for train movement must not overlap."
  },
  {
    "ID": "[SC-1.2]",
    "Name": "The permissible speed must be such that it is always possible to decelerate/brake the train in the area reserved for it."
  },
  {
    "ID": "[SC-1.3]",
    "Name": "Conditions which limit the braking performance must be taken into account. (e.g. wet tracks or leaves on the track)"
  },
  {
    "ID": "[SC-1.4]",
    "Name": "The safety distance must be large enough so that the residual risk of a collision is acceptable even if the braking performance is worse than expected. (coupling of trains should still be possible → “safe collision” of trains)"
  },
  {
    "ID": "[SC-1.5]",
    "Name": "The ability of trains to maintain the braking curve must be supervised, a violation must be detected and measures taken to prevent collisions. (e.g. emergency brake and/or deceleration of other trains, warning/closing of level crossings)"
  },
  {
    "ID": "[SC-1.6]",
    "Name": "If a point in an area reserved for train movement loses its end position, this must be detected and the train must be prevented from passing over it or at least the severity must be reduced by decelerating controlled trains and other vehicles."
  },
  {
    "ID": "[SC-1.7]",
    "Name": "The current state of railway points must be correct with a very high probability. (MBS has no influence on this, except that certain safety application conditions can be required)"
  },
  {
    "ID": "[SC-2]",
    "Name": "If trains violate safe distances to other trains or obstacles, this violation must be detected and measures taken to prevent collision."
  },
  {
    "ID": "[SC-2.1]",
    "Name": "Level crossings in an area reserved for train movement must be secured in a timely manner and other level crossing users must be warned in advance."
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[SC-2.2]",
    "Name": "Trains must not pass level crossings too fast, depending on the local conditions (i.e. not completely secured level crossing)."
  },
  {
    "ID": "[SC-2.3]",
    "Name": "If it can be detected that a level crossing is occupied by some other level crossing users, then measures must be taken to reduce the risk of collision to a tolerable level."
  },
  {
    "ID": "[SC-2.4]",
    "Name": "Railway workers must be warned in time when a train approaches a construction site."
  },
  {
    "ID": "[SC-2.5]",
    "Name": "Trains must not pass railway workers (construction sites) too fast. (speed depends on the distance of the train to the railway workers)"
  },
  {
    "ID": "[SC-2.6]",
    "Name": "If trucks or other construction trains intersect an area reserved for a train movement, this must be detected and measures taken to prevent collision."
  },
  {
    "ID": "[SC-2.7]",
    "Name": "Runaway railway trains must be detected (e.g. detection using TIMS, TTD, etc.) and measures taken to reduce the risk of collision to a tolerable level."
  },
  {
    "ID": "[SC-2.8]",
    "Name": "Level crossings must not be blocked longer as necessary (i.e. barriers are to be opened as soon as the train has passed over the level crossing)."
  },
  {
    "ID": "ID",
    "Name": "Name"
  },
  {
    "ID": "[SC-3]",
    "Name": "Trains must stay within their reserved clearance gauge."
  },
  {
    "ID": "[SC-3.1]",
    "Name": "Trains must be compatible with the infrastructure. (i.e. if axle load, track gauge, clearance gauge, minimum brake performance, ... do not match or is not met, the train must not use this section of line)"
  },
  {
    "ID": "[SC-3.2]",
    "Name": "Trains must comply with the utilization conditions of the infrastructure. (i.e. the maximum permitted speed, which may depend on the actual train, must not be exceeded) Note: Here (SC-3.1 and SC-3.2) a distinction is made between the more static and the more dynamic conditions."
  },
  {
    "ID": "[SC-3.3]",
    "Name": "If the utilization conditions are violated by a train, this must be detected and measures taken to reduce the risk of derailment."
  }
]

---

[
  {
    "ID": "[SC-3.4]",
    "Name": "If the clearance gauge is violated by a train, this must be detected (e.g. using checkpoint installations) and measures taken to reduce the risk of accidents. Note: checkpoint installations may be able to detect more issues like fire in the train, hot box, hot wheel, derailed axle.",
    "ID Hazards": "[H-3.2]"
  }
]

[
  {
    "ID": "[SC-4]",
    "Name": "Train must not expose passengers to high forces.",
    "ID Hazards": "[H-4]"
  },
  {
    "ID": "[SC-4.1]",
    "Name": "Trains must not use excessive braking technique (i.e. emergency brake), if other measures are possible that reduce the risk of passenger injury to an acceptable value.",
    "ID Hazards": "[H-4.1]"
  },
  {
    "ID": "[SC-4.2]",
    "Name": "Coupling of trains must be done at a speed so that the risk of passenger injury is acceptable.",
    "ID Hazards": "[H-4.2]"
  },
  {
    "ID": "[SC-4.3]",
    "Name": "The speed of trains in curves must not expose passengers to an unacceptable risk. Note: This maximum speed depends on the radius of the curve, superelevation and tilting technology.",
    "ID Hazards": "[H-4.3]"
  },
  {
    "ID": "[SC-5]",
    "Name": "Trains must not expose people outside the train to high forces.",
    "ID Hazards": "[H-5]"
  },
  {
    "ID": "[SC-6]",
    "Name": "If train loses its train integrity, this must be detected and measures taken to prevent collision.",
    "ID Hazards": "[H-6]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Hazards": "ID Hazards"
  },
  {
    "ID": "[SC-6.1]",
    "Name": "If train loses its train integrity (i.e. runaway wagon), this must be detected and measures taken to reduce the risk of accidents. Note: This can be detected by monitoring train integrity (TIM), cold movement detectors or by TTD where available.",
    "ID Hazards": "[H-6.2]"
  },
  {
    "ID": "[SC-6.2]",
    "Name": "If trains lose dangerous goods, this must be detected and measures taken to reduce the risk of environmental damage. Note: What measures are possible still needs to be investigated.",
    "ID Hazards": "[H-6.1]"
  }
]

---

[
  {
    "ID": "[SC-6.3]",
    "Name": "If the train frame is damaged, this must be detected and measures taken to reduce the risk of passenger injury. Note: Usually handled during inspections or through observant staff.",
    "ID Hazards": "[H-6.3]"
  }
]

[
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "ID Hazards"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-7]"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-7]"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-7]"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "ID Hazards"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-8]"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-8.1, H-8.2]"
  },
  {
    "Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.": "[H-8.3]"
  }
]

[
  {
    "ID": "[ASM-1]",
    "Name": "MBS communicates using standardized interfaces with the field elements (Eulynx).",
    "ID Overall": "[14]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID Overall"
  },
  {
    "ID": "[ASM-2]",
    "Name": "MBS receives position information from the trains OBU and uses the train position information to derive movement authorities (train centric approach).",
    "ID Overall": "[G1]"
  },
  {
    "ID": "[ASM-3]",
    "Name": "Only ETCS Level 2 (previously Level 2/3 or R) equipped trains are supported by the MBS during normal operation. Trains without TIMS are supported for migration scenarios, when TTDs are available.",
    "ID Overall": "[G2]"
  },
  {
    "ID": "[ASM-4]",
    "Name": "MBS does not require TTDs but supports them for migration scenarios.",
    "ID Overall": "[G3]"
  },
  {
    "ID": "[ASM-5]",
    "Name": "MBS aims to have as little manual intervention (e.g. by the operator) as possible.",
    "ID Overall": "[G4]"
  },
  {
    "ID": "[ASM-6]",
    "Name": "MBS operation assumes trains are equipped with a TIMS (Train integrity monitoring system). However, in degraded modes and for migration purposes operation without TIMS is supported as well.",
    "ID Overall": "[G5]"
  },
  {
    "ID": "[ASM-7]",
    "Name": "MBS is responsible for safety control and should contain a generic and simple safety logic. The operational commands are generated by other systems.",
    "ID Overall": "[A2]"
  },
  {
    "ID": "[ASM-8]",
    "Name": "Train length and train integrity confirmation are relevant for a SIL 4 functions and therefore have to be provided with appropriate correctness guarantees for these functions.",
    "ID Overall": "[T0]"
  },
  {
    "ID": "[ASM-9]",
    "Name": "The train length reported by the OBU represents the maximum train length (e.g. after stretching).",
    "ID Overall": "[T1]"
  },
  {
    "ID": "[ASM-10]",
    "Name": "Changes in the communication technology to the Trains will neither affect the content of the messages defined in the ETCS Definitions nor the transit time (TBD s) of the messages between the Moving Block System and the trains.",
    "ID Overall": "[T2]"
  },
  {
    "ID": "[ASM-11]",
    "Name": "MBS functionality does not change whether the train is operated by a human driver or ATO.",
    "ID Overall": "[T3, T4]"
  },
  {
    "ID": "[ASM-12]",
    "Name": "MBS requires that the cold movement of trains is detected. This could be performed e.g. by a cold movement detection device (CMD device).",
    "ID Overall": "[T7]"
  },
  {
    "ID": "[ASM-13]",
    "Name": "The Train OBU and the infrastructure elements/OCs are SIL-4 systems.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-14]",
    "Name": "The PE can be a SIL Basic Integrity safety related and non-safety related system.",
    "ID Overall": "-"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID Overall"
  },
  {
    "ID": "[ASM-15]",
    "Name": "The integrity of communication between the train OBU and MBS is ensured by a SIL-4 system.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-16]",
    "Name": "The integrity of communication between the train infrastructure elements/OCs and MBS is ensured by a SIL-4 system.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-17]",
    "Name": "Object controllers are correctly installed and configured. This can be checked by operational procedures with optional automated support (e.g. flagging the configuration as correct after multiple successful train passages) (i.e. the position reported by a railway point will not be incorrect due to wrong wiring of the 4-wire-bus).",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-18]",
    "Name": "Every train is identified by a unique and unchangeable identifier.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-19]",
    "Name": "MBS assumes that the train is declared compliant (&quot;zugelassen&quot;) with the tracks by the IM.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-20]",
    "Name": "A train must be able to stop before the EoA/danger point. The braking curve is supervised by the trains OBU.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-21]",
    "Name": "Safety Related text messages will not be sent by the operator. Instead, such message should be generated by automated systems (e.g., MBS).",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-22]",
    "Name": "Interaction between the operator and MBS only involves safety related information.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-23]",
    "Name": "Other interactions of the operator with the system are done via the PE or the TMS.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-25]",
    "Name": "All information received from the operator panel is relevant for one AoC only. This implies that it is not necessary to exchange this information between MBS and neighbouring systems.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-26]",
    "Name": "The received information about the infrastructure (geographical position of tracks, points, etc.) correctly represent physical reality. An external controller is responsible for the data validation process. Rationale: MBS safety functions depend on this input but cannot verify the input independently.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-27]",
    "Name": "When train integrity is lost, the main reservoir pipe is vented and the train emergency breaks engage.",
    "ID Overall": "-"
  },
  {
    "ID": "[ASM-28]",
    "Name": "Operator informs the MBS, about all regions where a train movement has been manually authorised by the operator. This also includes situations, where the radio connections to the OBU is lost.",
    "ID Overall": "-"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Collision Avoidance:",
    "Name": "Collision Avoidance:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-1]",
    "Name": "Calculate the intersection of the area of movement permissions requested by the PE with other areas reserved for train movements (and the area of trains itself). Movement permissions which intersect or have insufficient distance shall be rejected.",
    "ID Overall": "[SC-1.1]"
  },
  {
    "ID": "[Resp-MBS-2]",
    "Name": "Provide speed restrictions, gradients and national values defined by the IM to the OBU.",
    "ID Overall": "[SC-1.2, SC-3.3]"
  },
  {
    "ID": "[Resp-MBS-3]",
    "Name": "Provide adhesion factor profile based on information of the operator, automatic detection (e.g. WSP) or weather forecast.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "[Resp-MBS-4]",
    "Name": "Check the dynamically (within MBS) generated static speed profile of trains, taking into account the train properties, the utilization conditions and the national values of the infrastructure.",
    "ID Overall": "[SC-1.2, SC-1.4]"
  },
  {
    "ID": "[Resp-MBS-5]",
    "Name": "Verify that the safe distance between the EoA and other authorizations, trains or obstacles is big enough (depends on the mode: SR, OS, FS).",
    "ID Overall": "[SC-1.4, SC-3.3]"
  },
  {
    "ID": "[Resp-MBS-6]",
    "Name": "Verify that the max permitted distance for a train that runs in SR mode is clear of other authorizations, trains or obstacles.",
    "ID Overall": "[SC-1.4]"
  },
  {
    "ID": "[Resp-MBS-7]",
    "Name": "Check the location (and speed) reported by the trains and provide emergency stop command to the OBU, if the probability for leaving the reservation area is too high (or the permitted speed is violated).",
    "ID Overall": "[SC-1.5, SC-3.3]"
  },
  {
    "ID": "[Resp-MBS-8]",
    "Name": "Monitor location/speed reported by trains and in case that they will probably leave the area reserved for their movement protect and warn the affected environment.",
    "ID Overall": "[SC-1.5]"
  },
  {
    "ID": "[Resp-MBS-9]",
    "Name": "Supervise required point positions (in areas reserved for movement) and in case a point loses its end position and performs safety reaction.",
    "ID Overall": "[SC-1.6]"
  },
  {
    "ID": "[Resp-MBS-10]",
    "Name": "Support checking the infrastructure after maintenance (e.g., allowing the first train only to pass in OS mode after track maintenance).",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-MBS-11]",
    "Name": "Prohibit usage of malfunctioning infrastructure elements (e.g., set a usage restriction for a malfunctioning point reported by a train driver to the operator).",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-MBS-12]",
    "Name": "Detect malfunctioning infrastructure elements (e.g., train takes wrong direction passing a point) and report those to the operator.",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-MBS-13]",
    "Name": "Check and monitor that level crossing in areas reserved for train movement are secured in a timely manner.",
    "ID Overall": "[SC-2.1]"
  },
  {
    "ID": "[Resp-MBS-14]",
    "Name": "Check that the speed of trains passing over not completely secured level crossings is not too high. Note: this restriction is already part of the static speed profile of movement permissions.",
    "ID Overall": "[SC-2.2, SC-5]"
  },
  {
    "ID": "[Resp-MBS-15]",
    "Name": "If obstacles are detected on a level crossing that is/was secured for train movement perform safety reaction.",
    "ID Overall": "[SC-2.3]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "[Resp-MBS-16]",
    "Name": "Register/remove warning areas for construction sites (including location on the tracks) reported by the railway worker warning systems.",
    "ID Overall": "[SC-2.4]"
  },
  {
    "ID": "[Resp-MBS-17]",
    "Name": "Check that the warning system for railway workers is activated in a timely manner, in case a train is approaching the warning area.",
    "ID Overall": "[SC-2.4]"
  },
  {
    "ID": "[Resp-MBS-18]",
    "Name": "Check that the speed of trains passing construction sites is not too high (e.g. TSR, This is part of the static speed profile of movement permissions and depends on the distance of the train to the railway workers).",
    "ID Overall": "[SC-2.5, SC-5]"
  },
  {
    "ID": "[Resp-MBS-19]",
    "Name": "If construction trains or other obstacles occupy the tracks of a construction site perform safety reaction.",
    "ID Overall": "[SC-2.6]"
  },
  {
    "ID": "[Resp-MBS-21]",
    "Name": "Warn the operator if runaway trains or other obstacles are detected.",
    "ID Overall": "[SC-2.7, SC-6.2]"
  },
  {
    "ID": "[Resp-MBS-22]",
    "Name": "Supervise secured state of level crossings (in areas reserved for movement) and perform safety reaction in case the level crossing loses its secured state.",
    "ID Overall": "[SC-2.1]"
  },
  {
    "ID": "[Resp-MBS-23]",
    "Name": "Report level crossings which are behind areas reserved for movements and did not open in reasonable time to the operator.",
    "ID Overall": "[SC-2.8]"
  },
  {
    "ID": "[Resp-MBS-45]",
    "Name": "Increase train location accuracy by combining train position reports with TTD occupancy information.",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "Communication with trackside infrastructure elements:",
    "Name": "Communication with trackside infrastructure elements:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-46]",
    "Name": "Receive the current position of all railway points.",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-47]",
    "Name": "Command the throw over a railway point.",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-48]",
    "Name": "Receive the current occupancy status of all trackside train detection systems (TTDs).",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-49]",
    "Name": "Receive the current status of all level crossings.",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-50]",
    "Name": "Command the opening/closing of level crossings.",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "Train Handover with neighbouring regions:",
    "Name": "Train Handover with neighbouring regions:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-39]",
    "Name": "When a train approaches the border of the controlled region, inform the neighbouring system (MBS or interlocking (N-IXL)) and perform a handover.",
    "ID Overall": "[SC-1.1]"
  },
  {
    "ID": "[Resp-MBS-40]",
    "Name": "When a train approaches the border of the controlled region, inform the neighbouring system (MBS or RBC (N-RBC)) and perform a handover.",
    "ID Overall": "[SC-1.1]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "[Resp-MBS-41]",
    "Name": "Continue monitoring the train until its rear end has left the rear of control.",
    "ID Overall": "[SC-1.1, SC-2]"
  },
  {
    "ID": "[Resp-MBS-42]",
    "Name": "When an N-RBC announces a train entering the controlled region, check that the risk of the new train is acceptable and - if so - accept the handover from the N-RBC.",
    "ID Overall": "[SC-1.1]"
  },
  {
    "ID": "[Resp-MBS-43]",
    "Name": "When an N-IXL announces a train entering the controlled region, check that the risk of the new train is acceptable and - if so - accept the handover from the N-IXL.",
    "ID Overall": "[SC-1.1]"
  },
  {
    "ID": "[Resp-MBS-44]",
    "Name": "Start supervision of the train once it has entered the controlled region.",
    "ID Overall": "[SC-1.1, SC-2]"
  },
  {
    "ID": "Clearance Gauge - Derailment:",
    "Name": "Clearance Gauge - Derailment:",
    "ID Overall": "[SC-3]"
  },
  {
    "ID": "[Resp-MBS-24]",
    "Name": "Before authorizing a movement permission for a train, check if the infrastructure properties are compatible with the properties of the train.",
    "ID Overall": "[SC-3.1]"
  },
  {
    "ID": "[Resp-MBS-25]",
    "Name": "Check the consistency of train properties reported by the train itself and provided by the DR/TMS/Operator.",
    "ID Overall": "[SC-3.1]"
  },
  {
    "ID": "[Resp-MBS-26]",
    "Name": "Before authorizing a movement permission for a train, verify if the utilization conditions are respected by the movement permission.",
    "ID Overall": "[SC-3.2, SC-5]"
  },
  {
    "ID": "[Resp-MBS-27]",
    "Name": "If utilization conditions for a requested movement permission are violated, the movement permission shall not be authorized.",
    "ID Overall": "[SC-3.3]"
  },
  {
    "ID": "[Resp-MBS-29]",
    "Name": "If a violation of utilization conditions (e.g., violation of the clearance gauge, hot box, hot wheel, fire on board, derailed axle, ...) is reported perform safety reaction.",
    "ID Overall": "[SC-3.4]"
  },
  {
    "ID": "Unsafe Regions:",
    "Name": "Unsafe Regions:",
    "ID Overall": "[SC-7]"
  },
  {
    "ID": "[Resp-MBS-32]",
    "Name": "Inform the operator about conditions of regions which prevent a safe passage of trains.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-MBS-33]",
    "Name": "If movement permissions are requested which enter unsafe regions, this movement permissions shall not be authorized.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-MBS-34]",
    "Name": "If conditions of unsafe regions are detected in the area reserved for train movement perform safety reaction.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-MBS-35]",
    "Name": "Ensure that the risk of reversing trains entering emergency propelling areas is tolerable.",
    "ID Overall": "[SC-7.2]"
  },
  {
    "ID": "Utilization Conditions:",
    "Name": "Utilization Conditions:",
    "ID Overall": "[SC-8]"
  },
  {
    "ID": "[Resp-MBS-37]",
    "Name": "Before new topography data is used for production, plausibility checks (topological properties, e.g., like",
    "ID Overall": "[SC-8.1]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "Name": "connectivity) shall be performed. May be delegated to a different controller."
  },
  {
    "ID": "[Resp-MBS-38]",
    "Name": "Temporary changes in utilization conditions of infrastructure elements shall be taken into account when assessing whether a risk is tolerable.",
    "ID Overall": "[SC-8.2]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Collision Avoidance:",
    "Name": "Collision Avoidance:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-IM-1]",
    "Name": "Provide national values which are compliant with the requirements of static risk assessment.",
    "ID Overall": "[SC-1.2, SC-4.1]"
  },
  {
    "ID": "[Resp-IM-2]",
    "Name": "Instructions for operators and drivers concerning low adhesion factor conditions.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "Clearance Gauge - Derailment:",
    "Name": "Clearance Gauge - Derailment:",
    "ID Overall": "[SC-1.2, SC-4.1]"
  },
  {
    "ID": "[Resp-IM-3]",
    "Name": "Provide topography, topology, configuration- and infrastructure data. (e.g. axle load, track gauge, clearance gauge, traction system, static speed profile, etc.).",
    "ID Overall": "[SC-3.1, SC-4.3, SC-5]"
  },
  {
    "ID": "Utilization Conditions:",
    "Name": "Utilization Conditions:"
  },
  {
    "ID": "[Resp-IM-5]",
    "Name": "The quality of data from [Resp-IM-3] shall be such that safety-critical decisions can be based on it. This includes guaranteed limits for accuracy and specifying confidence intervals for numerical values.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "[Resp-IM-6]",
    "Name": "Changes (temporary or permanent) of the topography description shall be provided to the system in a timely manner.",
    "ID Overall": "[SC-8.1, SC-8.2]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Collision Avoidance:",
    "Name": "Collision Avoidance:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-OP-1]",
    "Name": "Inform Train about track conditions lowering the adhesion factor.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "[Resp-OP-2]",
    "Name": "Setup/Revoke areas with low adhesion factor.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "[Resp-OP-3]",
    "Name": "Setup/remove usage restriction areas for malfunctioning infrastructure elements (e.g., set a “Befahrbarkeitssperre” for a malfunctioning point reported by a train driver).",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-OP-4]",
    "Name": "Setup/remove warning areas for construction sites (together with the Picop and provide further information of warning time, max allowed speed, ...).",
    "ID Overall": "[SC-2.4, SC-2.5, SC-5]"
  },
  {
    "ID": "[Resp-OP-5]",
    "Name": "Inform MBS about runaway trains, including location on the tracks (and their assumed direction and speed).",
    "ID Overall": "[SC-2.7]"
  },
  {
    "ID": "Clearance Gauge - Derailment:",
    "Name": "Clearance Gauge - Derailment:",
    "ID Overall": "[SC-3]"
  },
  {
    "ID": "[Resp-OP-6]",
    "Name": "Optionally provide missing train properties.",
    "ID Overall": "[SC-3.1]"
  },
  {
    "ID": "Unsafe Regions:",
    "Name": "Unsafe Regions:",
    "ID Overall": "[SC-7]"
  },
  {
    "ID": "[Resp-OP-8]",
    "Name": "Inform MBS about conditions of regions, which prohibit a safe passage of trains.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-OP-9]",
    "Name": "Prepare emergency propelling areas for reversing trains in unsafe regions.",
    "ID Overall": "[SC-7.2]"
  },
  {
    "ID": "[Resp-OP-10]",
    "Name": "Command trains to leave unsafe regions.",
    "ID Overall": "[SC-7.2]"
  },
  {
    "ID": "Utilization Conditions:",
    "Name": "Utilization Conditions:",
    "ID Overall": "[SC-8]"
  },
  {
    "ID": "[Resp-OP-11]",
    "Name": "Inform MBS about temporary changed utilization conditions of infrastructure elements.",
    "ID Overall": "[SC-8.2]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Collision Avoidance:",
    "Name": "Collision Avoidance:",
    "ID Overall": "[SC-1, SC-2]"
  },
  {
    "ID": "[Resp-DRV-1]",
    "Name": "Inform Operator about track conditions lowering the adhesion factor.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "[Resp-DRV-2]",
    "Name": "Adjust adhesion factor manually.",
    "ID Overall": "[SC-1.3]"
  },
  {
    "ID": "[Resp-DRV-3]",
    "Name": "Decelerate train to respect the permitted speed and distance to run.",
    "ID Overall": "[SC-1.4, SC-1.5, SC-5]"
  },
  {
    "ID": "[Resp-DRV-4]",
    "Name": "Report malfunctioning infrastructure elements, when checking is required (e.g., checking point position in OS mode).",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-DRV-5]",
    "Name": "Check if the level crossing is free and warn other level crossing users. EB if tracks occupied by obstacles or level crossing users.",
    "ID Overall": "[SC-2.2, SC-2.3]"
  },
  {
    "ID": "[Resp-DRV-6]",
    "Name": "EB if construction site is occupied by railway workers, construction trains or other obstacles.",
    "ID Overall": "[SC-2.6]"
  },
  {
    "ID": "[Resp-DRV-x]",
    "Name": "Check that the track is clear/free (TAF), if required.",
    "ID Overall": "[SC-1]"
  },
  {
    "ID": "Clearance Gauge - Derailment:",
    "Name": "Clearance Gauge - Derailment:",
    "ID Overall": "[SC-3]"
  },
  {
    "ID": "[Resp-DRV-7]",
    "Name": "Enter the correct train properties (validated train data).",
    "ID Overall": "[SC-3.1, SC-8.1]"
  },
  {
    "ID": "High Forces:",
    "Name": "High Forces:",
    "ID Overall": "[SC-4, SC-5, SC-6]"
  },
  {
    "ID": "[Resp-DRV-8]",
    "Name": "Coupling of trains shall be done at a speed so that the risk of passenger injury is acceptable.",
    "ID Overall": "[SC-4.2]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "[Resp-DRV-10]",
    "Name": "If loss of dangerous goods is detected, this shall be reported to the operator.",
    "ID Overall": "[SC-6.2]"
  },
  {
    "ID": "[Resp-DRV-11]",
    "Name": "If a damage of the train frame is apparent, this shall be reported to the operator.",
    "ID Overall": "[SC-6.3]"
  },
  {
    "ID": "Unsafe Regions:",
    "Name": "Unsafe Regions:",
    "ID Overall": "[SC-7]"
  },
  {
    "ID": "[Resp-DRV-12]",
    "Name": "Report conditions which prohibit a safe passage of trains.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-DRV-13]",
    "Name": "If leaving unsafe regions, keep the train movement inside the received distance to run.",
    "ID Overall": "[SC-7.2]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Collision Avoidance",
    "Name": "Collision Avoidance"
  },
  {
    "ID": "[Resp-OBU-1]",
    "Name": "Calculation of the dynamic speed profile, taking into account the running/braking characteristics of the train and the track conditions/adhesion factor (specified in the UNISIG-26)",
    "ID Overall": "[SC-1.2, SC-1.3, SC-1.4, SC-5]"
  },
  {
    "ID": "[Resp-OBU-2]",
    "Name": "Trip the train, if train speed exceeds the permitted speed/ceiling speed or authority is overrun (distance)",
    "ID Overall": "[SC-1.2, SC-1.4, SC-1.5]"
  },
  {
    "ID": "[Resp-OBU-3]",
    "Name": "Cab signalling - display train speed, permitted speed, target distance, target speed to the driver",
    "ID Overall": "[SC-1.4, SC-1.5, SC-5]"
  },
  {
    "ID": "[Resp-OBU-4]",
    "Name": "Supervise movement against running in the direction opposite to the train orientation (reverse movement protection)",
    "ID Overall": "[SC-1.5]"
  },
  {
    "ID": "[Resp-OBU-5]",
    "Name": "Trip the train (apply emergency brake) if commanded by MBS",
    "ID Overall": "[SC-1.5, SC-1.6, SC-2.3, SC-2.6, SC-2.7]"
  },
  {
    "ID": "[Resp-OBU-6]",
    "Name": "Inform the driver when OS mode entered and request an acknowledgement from the driver",
    "ID Overall": "[SC-1.7]"
  },
  {
    "ID": "[Resp-OBU-7]",
    "Name": "Inform the driver when approaching a level crossing",
    "ID Overall": "[SC-2.2, SC-2.3]"
  },
  {
    "ID": "Clearance Gauge - Derailment",
    "Name": "Clearance Gauge - Derailment"
  },
  {
    "ID": "[Resp-OBU-8]",
    "Name": "Provide the train properties (validated train data)",
    "ID Overall": "[SC-3.1, SC-8.1]"
  },
  {
    "ID": "[Resp-OBU-9]",
    "Name": "Periodically send position reports (interval parameters requested/configured by the track-side or national values; including position, direction, speed and the accuracy of this values)",
    "ID Overall": "[SC-3.3]"
  },
  {
    "ID": "High Forces",
    "Name": "High Forces"
  },
  {
    "ID": "[Resp-OBU-10]",
    "Name": "The driver shall be supported in coupling activities so that the risk of passenger injury is acceptable. (e.g. measure distance, display it and issue distance warnings)",
    "ID Overall": "[SC-4.2]"
  },
  {
    "ID": "Unsafe Regions",
    "Name": "Unsafe Regions"
  },
  {
    "ID": "[Resp-OBU-11]",
    "Name": "Supervise movement in reversing mode (distance and ceiling speed)",
    "ID Overall": "[SC-7.2]"
  },
  {
    "ID": "Utilization Conditions",
    "Name": "Utilization Conditions"
  },
  {
    "ID": "[Resp-OBU-12]",
    "Name": "Provide and check the system version",
    "ID Overall": "[SC-8.1]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Unsafe Regions:",
    "Name": "Unsafe Regions:",
    "ID Overall": "[SC-7]"
  },
  {
    "ID": "[Resp-MNT-1]",
    "Name": "Inform operator of conditions of infrastructure elements on-site.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "[Resp-MNT-2]",
    "Name": "Determine on-site whether train passage over infrastructure element is safe.",
    "ID Overall": "[SC-7.1, SC-1.6]"
  },
  {
    "ID": "[Resp-MNT-3]",
    "Name": "Repair damaged infrastructure elements and restore drivability of such elements.",
    "ID Overall": "[SC-7.1]"
  },
  {
    "ID": "ID",
    "Name": "Name",
    "ID Overall": "ID SLC"
  },
  {
    "ID": "Utilization Conditions:",
    "Name": "Utilization Conditions:",
    "ID Overall": "[SC-7, SC-8]"
  },
  {
    "ID": "[Resp-DR-1]",
    "Name": "Validates that the topology and topography data is consistent with physical reality.",
    "ID Overall": "[SC-8.1]"
  },
  {
    "ID": "[Resp-DR-2]",
    "Name": "Verifies that the topology and topography data meet the data engineering and validation rules.",
    "ID Overall": "[SC-7.1, SC-8.1]"
  },
  {
    "ID": "[Resp-DR-3]",
    "Name": "Provides validated topology and topography data to PE, MBS and OBU relevant for their region of control.",
    "ID Overall": "[SC-8.1]"
  },
  {
    "ID": "[Resp-DR-4]",
    "Name": "Ensures synchronized activation of new data versions in PE, MBS and OBU.",
    "ID Overall": "[SC-7.1, SC-8.2]"
  },
  {
    "ID": "Controllers",
    "Name": "·Operator Panel:·MBS:"
  },
  {
    "ID": "Control Actions:",
    "Name": "·OP -&gt; MBS:      ○ Set known infrastructure state      ○ Setup/revoke temporary Usage Restriction Area      ○ Emergency Text Messages to Driver (seldomly used)      ○ Conditional/Unconditional emergency Stop      ○ Command confirmation (command dependent)      ○ Setup/revoke warning areas for construction sites"
  },
  {
    "ID": "Feedbacks:",
    "Name": "·MBS -&gt; OP:      ○ Command Received/Rejected      ○ Safety/Operational implications      ○ Request command confirmation (command dependent)      ○ Operation Succeeded/Failed + Reason"
  }
]

---

[
  {
    "○ Operational State": "• MBS○ Operational State• OP○ Panel: Request state/Command state○ Operator: TMS/PE System View / Operational knowledge / Real world knowledge"
  },
  {
    "○ Operational State": "• MBS○ Semantic/Syntactic command check○ Determine safety implications○ Confirmation loop (command dependent)○ Forward command and/or update known infrastructure state.○ Provide feedback• OP○ Operational Rules○ Operational state from MBS○ Known state of real world from other sources○ Mental model of command implications."
  },
  {
    "○ Operational State": "Operator shall be able to conduct temporary safety related interventions and enact temporary infrastructure restrictions.Only safety related commands are considered via the I_OP interface. Non-critical/standard commands can be sent via PE and subsequently I_PE."
  }
]

[
  {
    "Hazardous when": "Provided too late/early"
  },
  {
    "Hazardous when": "UCA-OP-3: Operator provides a known infrastructure state too late when that state is worse in reality than the operational state of MBS [H-8.1, H-8.3]"
  }
]

---

[
    {
      "UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]": "UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]",
      "UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]",
      "UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]"
    },
    {
      "UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]": "UCA-OP-5: Operator provides revocation of temporary usage restriction area when the usage restriction should still be applied [H-8.1, H-8.2]",
      "UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-26: Operator provides revocation of temporary usage restriction area too early when the usage restriction should still be applied [H-8.1, H-8.2]",
      "UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-26: Operator provides revocation of temporary usage restriction area too early when the usage restriction should still be applied [H-8.1, H-8.2]"
    },
    {
      "UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]": "UCA-OP-14: Operator provides emergency stop command for wrong train [H-4.1] UCA-OP-15: Operator provides conditional emergency stop command with wrong stopping position [H-1, H-2] UCA-OP-16: Operator provides conditional emergency stop command where an unconditional emergency stop command is required [H-1, H-2]",
      "UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-17: Operator does not provide safety related conditional/unconditional emergency stop [H-1, H-2]",
      "UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-18: Operator provides safety related conditional/unconditional emergency stop too late [H-1, H-2]"
    },
    {
      "UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]": "UCA-OP-19: Operator provides command confirmation for the wrong train/",
      "UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-21: Operator does not provide command confirmation (any of the unsafe",
      "UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]": "UCA-OP-22: Operator provides command confirmation too late (any of the unsafe"
    }
]

---

[
  {
    "infrastructure element / message [H1, H2, H7, H8] UCA-OP-20: Operator provides command confirmation without consideration of safety implications for other trains [H1, H2, H7, H8]": "UCA-OP-23: Operator provides command to revoke warning are for construction site when the railway workers are still on site. [H-5]",
    "actions above) [H1, H2, H7, H8]": "UCA-OP-25: Operator provides command to revoke warning are for construction site to early when the railway workers are still on site. [H-5]"
  }
]

Scenarios for unsafe control actions:

[S1-UCA-OP-1]: Two railway points P1 and P2 report a lost end position and are unable to execute throwover commands by the operator. As the railway points are within close proximity, a single maintenance team is dispatched to investigate the two points. The maintenance team is able to fix the position of P1 and reports work completed this to the Operator. The operator mistakenly believes the team also fixed the position of point P2, which the team was also tasked to investigate. As a result, the operator provides an infrastructure state not matching reality to MBS [UCA-OP-1]

=> [SDR-1]: Provide an operational rule set which explicitly determines to which infrastructure item a completed (safety related) intervention refers/referred to.

[S2-UCA-OP-2]: When passing a protected level crossing, the train driver notices that the bars on one side are not fully closed and reports this to the operator. As this particular level crossing had problems in the past, the operator mistakenly believes that this was already entered into the operator panel. As a result, a required URA is not applied to the MA [UCA-OP-2].

=> [SDR-2]: When changes to the operational state are reported by personnel, the operator shall always check if they are already entered in the operation state of MBS, even if the operator believes this has already been done in the past => [SDR-3]: The operator panel shall provide easily accessible information on all currently manually entered infrastructure state with the required confidence for a safety related function.

[S3-UCA-OP-3]: A construction team is in the field upgrading multiple railway points. The construction is scheduled sequentially so that the impact on the railway traffic is minimized. Due to unforeseen problems on site, the construction order of the points is switched and this is reported to the operator. As the operators shift ends shortly and the change only affects the next shift, he leaves a note for the next shift. When the next shift starts, an operational disturbance keeps the operator

---

busy. As a result, the note concerning the construction schedule is read only after construction has already begun and the operator reports the known operational state to MBS too late [UCA-OP-3]

=> [SDR-4]: The interface for the operator shall allow to pre-schedule usage restriction areas.

=> [SDR-5]: The operator shift handover shall include either an operational process or digital means that prevent a loss of (safety related) information during the handover.

[S4-UCA-OP-4]: Due to construction work, a temporary usage restriction area with a speed reduction shall be established. When entering the speed restriction, the operator makes a typo leading to a usage restriction area with an excessive speed limit [UCA-OP-4].

=> [SDR-6]: The operator panel should implement procedures to verify the entered usage restriction data, before the entered data is passed to the MBS system.

[S5-UCA-OP-5]: A maintenance team performs work on two tracks T1 and T2 closely located to each other. When the team reports that it has completed its work for T1, the operator mistakenly believes that the work on both tracks has been completed. As a result, the operator revokes the usage restriction area for T1 and T2 when it still should be applied for T2 [UCA-OP-5].

=> See [SDR-1] and [SDR-3]

[S6-UCA-OP-6]: The operator receives a report from a train driver that there are leaves on the track reducing braking performance. The operator knows a corresponding usage restriction has already been entered by the previous shift. However, this usage restriction has since expired. The operator mistakenly believes the usage restriction is still applied and as a result does not provide the usage restriction to the operational state of MBS as needed [UCA-OP-6].

=> See [SDR-2] and [SDR-3]

[S7-UCA-OP-7]: An operational disturbance requires the operator to manually manage a large number of trains. As the timetable should be upheld as much as possible, the operator is under time pressure. In this situation a construction team reports that it will begin constructions on track T1 in half an hour. The operator takes note and is immediately occupied with train management again. Due to time pressure, the operator only follows up on the note after the construction has already begun. As a result, the operator provides the usage restriction area for the construction site too late to MBS [UCA-OP-7].

=> [SDR-7]: Entering usage restriction areas shall take priority over the regular management of running trains

=> see also [SDR-4]

[S8-UCA-OP-26]: The operator receives a report from the construction team that construction will be completed in half an hour. However, unforeseen difficulties on the construction site cause the operation to take longer. Emerged in their work the construction team does not report this delay to the operator. The operator mistakenly believes that the team has finished their work as planned and revokes the usage restriction area too early [UCA-OP-26].

=> [SDR-8]: The operator shall always verify with the construction team on site that the work has actually been completed before removing the corresponding usage restriction area.

[S9-UCA-OP-14/17/18]: Similar reasoning to [S7-UCA-OP-9] (handling of commands under time pressure, selecting the wrong train) [UCA-OP-14, UCA-OP-17, UCA-OP-18]

---

[S10-UCA-OP-15]: The Operator wants to stop a train before a danger point. The interface requires that the operator enters the stopping position manually. While entering the stopping position, the operator makes a typo. As a result, the operator provides a conditional emergency stop command with the wrong position. As the train has already passed this position, the command is ignored by the OBU [UCA-OP-15].

=> [SDR-9]: The operator panel shall be designed to support the operator with contextual information when executing operator commands. I.e. the operator shall be able to select the stopping position based on an interface with information about the physical elements/trackside assets and select a stopping position based on the physical elements position.

[S11-UCA-OP-16]: The operator receives information that part of a track has become unexpectedly occupied. A train currently has a valid MA over the obstructed portion of the track. The operator believes the train is still at a large distance from the obstructed portion and issues a conditional emergency stop. However, the train position report was outdated and the train is already past the stopping position for the conditional emergency stop. As a result, the operator fails to provide the required unconditional emergency stop command. [UCA-OP-16]

=> [SDR-10]: The operator shall receive a (visual) indication about the reported train position age. (e.g., information outdated longer than for a defined threshold should be indicated).

[S12-UCA-OP-19/20/21/22]: Similar to [S5-UCA-OP-5] and [S5-UCA-OP-7]. [UCA-OP-19, UCA-OP-20, UCA-OP-21, UCA-OP-22]

[S13-UCA-OP-23]: Similar to [S1-UCA-OP-1] and [S1-UCA-OP-5]. [UCA-OP-23]

[S14-UCA-OP-24]: Similar to [S6-UCA-OP-6]. [UCA-OP-24]

[S15-UCA-OP-25]: Similar to [S8-UCA-OP-26]. [UCA-OP-25]

---

[
  {
    "Controllers": "Control Actions:",
    "• MBS• OBU": "• MBS -&gt; OBU:1    ○ Configuration Values (National values)    ○ SR Authorization (distance)    ○ FS/OS Movement Authority    ○ Conditional/Unconditional Emergency Stop (CES/UES)    ○ Shorten MA"
  },
  {
    "Controllers": "Feedbacks:",
    "• MBS• OBU": "• OBU -&gt; MBS:2    ○ MA Request    ○ Train Position Report    ○ Validated Train Data    ○ Acknowledge CES"
  },
  {
    "Controllers": "Process Model",
    "• MBS• OBU": "• OBU    ○ Static and dynamic properties of train    ○ Current train position (including uncertainties)    ○ Current train speed    ○ ETCS mode    ○ Train Data (train length, running number, etc.)• MBS    ○ Operational state    • Reported train location    • Reported track occupations    • Granted MAs    ○ Infrastructure state    • Topography and geometry    • State of infrastructure elements    • Utilization conditions"
  }
]

---

[
  {
    "• Temporary speed restrictions\n• National Values": "• OBU\n    • Supervise train braking curve\n    • Supervise train speed\n    • Service break\n    • Emergency break\n• MBS\n    • Safety Logic before granting MA\n    • Command conditional/unconditional emergency stop\n    • Updating operational state expanded process model\n    • Handover to neighboring systems"
  }
]

[
  {
    "Hazardous when": "Provided too late/early"
  },
  {
    "Hazardous when": "[UCA-MBS-1] MBS does not provide national values to OBU when these values are more restrictive than default values [H-1.1, H-2.1, H-8.1]"
  },
  {
    "Hazardous when": "[UCA-MBS-2] MBS does not provide temporary speed restrictions to the OBU [H-2.6, H-5, H-8.3]"
  },
  {
    "Hazardous when": "[UCA-MBS-3] MBS does not provide track gradients to the OBU [H-1.1, H-2.1]"
  }
]

---

[
    {
        "FS/OS Movement Authority": "[UCA-MBS-7] MBS provides MA to the OBU when train type/properties are not compatible to infrastructure [H-3.1, H-8.2] [UCA-MBS-8] MBS provides MA to the OBU when the MA is intersecting a reservation area of another train [H-1]. [UCA-MBS-9] MBS provides MA to the OBU when the MA has a too small safety distance to other potential obstacles [H-1.1, H-2.1, H-3.1] [UCA-MBS-10] MBS provides FS/OS MA",
        "[UCA-MBS-4] MBS does not provide inhibition of defined type of brake to the OBU [H-1.1, H-2.1] [UCA-MBS-5] MBS does not provide the adhesion factor to the OBU when the adhesion conditions are worse than normal [H-1.1, H-2.1]": "",
        "[UCA-MBS-18] MBS provides MA too early for OBU when not all infrastructure elements along the MA are secured and passable for the train movement [H-1.4, H-2.4, H-3.3]": ""
    }
]

---

[
    {
        "to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]": "[UCA-MBS-11] MBS provides FS MA passing over a not completely secured level-crossing [H-2.5, H-5]",
        "": "",
        "": ""
    },
    {
        "to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]": "[UCA-MBS-12] MBS provides MA to OBU when the MA is directing into an unsafe area [H-7].",
        "": "",
        "": ""
    },
    {
        "to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]": "[UCA-MBS-13] MBS provides FS MA to OBU when coupling trains [H-4.2]",
        "": "",
        "": ""
    },
    {
        "to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]": "[UCA-MBS-14] MBS provides MA to OBU when the MA speed profile exceeds the most restrictive speed profile for this train given the running path [H-4.3, H-8.1]",
        "": "",
        "": ""
    },
    {
        "to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]": "[UCA-MBS-15] MBS provides MA to OBU when the MA is ending within a",
        "": "",
        "": ""
    }
]

---

[
  {
    "non-stopping area [H-7] [UCA-MBS-16] MBS provides FS MA to OBU when the area reserved for train is not clear of other trains or obstacles [H-1.1, H-2.1] [UCA-MBS-17] MBS provides MA to OBU when other train or obstacles have insufficient distance from the flank of the area reserved for train movement [H-1.1, H-2.1, H-2.8, H-3.1]": "[UCA-MBS-19] MBS provides SR authorization with a too long permitted distance, or into the wrong direction [H-1.1, H-2.1] (Note: this is used only if the position of the train is not known)"
  }
]

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>shorten MA to OBU when the train is approaching a point which lost its end position or indicates the wrong position [H-1.3, H-2.3, H-3.1] [UCA-MBS-22] MBS does not provide shorten MA command, if train is approaching a level crossing which is not secured anymore [H-2.5, H-5]</td><td style='text-align: center;'></td></tr></table>

Scenarios for selected unsafe control actions:

The unsafe control actions [UCA-MBS-16] and [UCA-MBS-17] were selected, as they are closely associated with the running path protection, which may be handled differently between fixed block and moving block systems.

[S1-UCA-MBS-16] Train T1 is a train composed of two consists, T1a and T1b, with one OBU per consist. The train is initially at standstill, and both consists are unpowered and coupled and no TTDs are located at the track. The consists T1a and T1b are uncoupled while the train is powered off. The driver enters the cab of T1a, opens the desk and enters the validated train data. He mistakenly believes that T1b is still coupled and inputs the total of T1a and T1b as train length into the DMI. As the consist T1a is still integer, the TIMS reports integrity confirmed. When PE requests an MA for T1a from MBS, MBS mistakenly believes that a train with a length of T1 is moved, while in reality train T1b is still standing on the tracks. As a result, after releasing the MA behind T1a, MBS grants another train T2 a MA into the region where T1b is still standing, leading to a collision [UCA-MBS-16]

=> [SDR-11]: MBS shall always be aware when a change of train length is expected (i.e. due to splitting and joining).

[S2-UCA-MBS-16] Train T1 with length LEN1 is initially at standstill and located on track TR1. T1 is not equipped with a functioning TIMS and no TTDs are available for TR1. The driver opens the desk and enters the validated train data. Due to operational changes, additional cars have been added to the train. The driver enters a too short train length LEN2, because he is not aware that the train is longer than during normal operations. As he is already behind schedule and there are visual obstructions blocking his view to the end of the train, the driver confirms the train integrity without seeing the last train cars. Therefore, MBS mistakenly believes T1 has length LEN2, which is shorter than the real train length LEN1, and grants an MA to T1 based on LEN2. As a result, after releasing the MA behind T1, MBS grants another train T2 a MA into the region where T1 is still standing, leading to a collision [UCA-MBS-16]

---

=> [SDR-12]: If MBS is aware of the expected train length (i.e. by transmitting the expected train length together with the train running number from the PE) it shall compare the expected train length with the reported train length in the validated train data and require addition confirmation if the two lengths differ.

[S3-UCA-MBS-16] Train T1 is initially at parked and located at L1, near the bottom of a valley. The train is powered down and no TTDs are available for this section of the track. After applying the parking brakes, the railway personal does not add the brake shoes below the wheels. Therefore, after the air pressure is no longer sufficient to keep the train at standstill, T1 starts to move towards the bottom of the valley and is now located at L2. MBS mistakenly believes that T1 is still located at its last known location L1. As a result, MBS grants another train T2 a MA into L2, leading to a collision [UCA-MBS-16]

=> [SDR-13]: In regions where the parking of vehicles is expected, methods for detecting the presence of trains independent of train position reports shall be available (i.e. installing TTDs in these regions)

[S4-UCA-MBS-16] Train T1 is initially at standstill and located at L1. T1 is in no power mode and no TTDs are available. The driver opens the desk and enters the validated train data. The OBU does not know the current train position. The driver therefore tells the operator the train position, and requests a staff responsible movement authorization. However, as the driver cannot see the track kilometer board due to visual obstructions, he mistakenly reports the wrong train position L2 to the operator. The operator permits a train movement based on a L2, while the train is in reality located at L1. As a result, MBS grants another train T2 a MA into L1, leading to a collision [UCA-MBS-16].

=> [SDR-14]: When moving a train based on a train position transmitted by the driver, the operator shall perform additional validity checks from a second source (i.e. planned start location of the train) before granting a SR authorization.

[S5-UCA-MBS-16]: Light Maintenance vehicle M1 is powered off and located at L1 on track TR1. TR1 is equipped with a track circuit TTD1, which is unable to detect the maintenance vehicle M1. At MBS initialization, TTD1 is reported as clear. Therefore, MBS is unaware of the presence of M1 at L1. As a result, MBS grants another train T1 a MA into L1, leading to a collision [UCA-MBS-16]

=> [SDR-15]: When the presence of maintenance vehicles is expected, track circuits alone should not be sufficient to clear the track, if these circuits can miss occupations by some vehicle types (i.e. light maintenance vehicles). Note: This may adversely impact operational performance at system startup or when clearing areas previously occupied by maintenance vehicles.

[S1-UCA-MBS-17] Train T1 is at standstill and located at the left track of railway point P1. The reported train length of LEN1 or T1 is shorter than the physical train length LEN2. Therefore, MBS mistakenly assumes that T1 is outside the fouling point of P1. As a result, MBS grants another train T2 a MA over P1, leading to a flank collision between T1 and T2 [UCA-MBS-17]

=> see [SDR-12]

[S2-UCA-MBS-17] Unsupervised area UA1 is reachable via the left track of railway point P1. Train T1 is located in UA1, and neither the UA1 nor the tracks of P1 are equipped with TTDs. Due to degraded braking performance, T1 skids outside the region UA1, and beyond the fouling point of P1. As a result, MBS grants another train T2 a MA over P1, leading to a flank collision between T1 and T2 [UCA-MBS-17]

---

=> [SDR-16]: Between controlled region and unsupervised region, the movement of non-communicating trains shall be detectable, i.e. using TTDs, or preventable using a point/derailer (similar to [SDR-13])

[S3-UCA-MBS-17] Maintenance vehicle M1 located within worksite W1 on track TR1 and equipped with a movable crane arm. Track TR2 runs parallel to TR1. If fully extended, the crane arm of M1 can reach into the maximum permitted clearance gauge TR2. Because worksite W1 is located on TR1, MBS mistakenly believes this worksite cannot affect trains running on TR2. As a result, an MA for another train T2 running on TR2 is granted while the crane arm of M1 is extended into TR2, leading to a clearance gauge violation [UCA-MBS-17].

=> [SDR-17]: The effects of Maintenance on neighboring tracks shall be taken into account (conceptionally, e.g., as function in MBS or as additional TSR with the URA from planning data or operator input) when granting a MA.

[S4-UCA-MBS-17] Train T1 performs end of mission on side Track TR1 which is connected to the main track TR2 via point P1. Due to an operational error the train was not protected against roll-away. After some time, the pressure in the brake tanks drops and the train starts to roll toward P1. In the mean-time another MA was granted for Train T2 on the main track TR2 leading over P1. Since MBS cannot detect the unexpected occupation on P1 nor the unexpected vacancy of the TTD on T1 in time, train T1 collides with train T2 leading to a flank collision.

=> [SDR-18] Simple detection of track occupation is not sufficient to prevent flank collisions in all cases. Technical means to secure a sufficiently large vacant area before the fouling point is required.

[S5-UCA-MBS-17] A side-track TR1 is equipped with TTD and via the point P1 connected to the main track TR2. Train T1 and train T3 are both located in the same TTD are on track TR1. Both trains have performed end of mission. Due to an operational error train T1 was not secured against roll-away. After break tank pressure drops, the train T1 rolls toward P1.

=> [SDR-18]

#### 5.7.3 I TACS Interface

MBS <-> TACS (SCI-XX.PDI, SCI-P, SCI-LC, SCI-TDS)


[
  {
    "Controllers": "Control Actions:",
    "• MBS• TACS": "• MBS -&gt; TACS:    ○ Manage PDI connection³    ○ Move point (SCI-P) ⁴    ○ Open/close/isolate level crossing (SCI-LC)⁵"
  }
]

---

[
  {
    "○ Reset track occupancy status (SCI-TDS)6": "· TACS -&gt; MBS:      ○ Manage PDI connection      ○ Report point state (SCI-P)      ○ Report level crossing state (SCI-LC)      ○ Report track occupancy state (SCI-TDS)      ○ Heartbeat [RASTA Protocol]"
  },
  {
    "○ Reset track occupancy status (SCI-TDS)6": "· MBS      ○ Operational State· TACS      ○ TACS configuration / parameters      ○ TACS state      ○ TA state"
  },
  {
    "○ Reset track occupancy status (SCI-TDS)6": "· MBS      ○ Safety Logic      ○ Supervise TACS heartbeat      ○ Determine safety implications of commands      ○ React to safety related events      ○ Establish communication with TACS      ○ Forward commands to OBU      ○ Sensor fusion· TACS      ○ Provide heartbeat      ○ Compare between TACS state and TA state      ○ Obstacle detection (only LC/LX)      ○ Command new state (for switchable TAs)      ○ Report state update (incl. timeout, degraded states and obstacles)"
  },
  {
    "○ Reset track occupancy status (SCI-TDS)6": "Most of this is regulated in the EULYNX Specification."
  }
]

---

[
  {
    "Hazardous when": "Stopped too soon"
  },
  {
    "Hazardous when": "[UCA-TACS-9]\nMBS stops the supervision of the moved point too soon when the point is still required for a reserved area and the point loses its end position. [H-1.3, H-2.3, H-3.1, H-3.3, H-4.3]."
  }
]

---

[
  {
    "Open/close level-crossing": "Reset track occupancy state",
    "[UCA-TACS-10] MBS provides open level crossing command while the level crossing is still reserved for train movement [H-2.5] [UCA-TACS-11] MBS provides close level crossing command when the level crossing is not required for train movement [H-2.9]": "[UCA-TACS-19] MBS provides reset track occupancy command while a train inside the track occupancy section [H-1, H-2, H-6.2]",
    "[UCA-TACS-12] MBS does not provide close level crossing command when the level crossing needs to be closed for train movement [H-2.5] [UCA-TACS-13] MBS does not provide the open level crossing command when the level crossing is no longer required for train movement [H-2.9]": "/ Note: this may reduce availability but is not related to safety",
    "[UCA-TACS-14] MBS provides close level crossing command too early when a train is approaching [H-2.9]. [UCA-TACS-15] MBS provides close level crossing command too late when a train is approaching [H-2.5]. [UCA-TACS-16]: MBS provides open level crossing command too early when a train is still within the level crossing [H-2.5] [UCA-TACS-17]: MBS provides close level crossing command too late when a train is already within the level crossing [H-2.9]": "[UCA-TACS-20] MBS provides reset track occupancy command too soon while a wagon is still inside the track",
    "[UCA-TACS-18] Supervision of closed level crossing is stopped to soon when still required for train movement [H-2.5].": "[UCA-TACS-21] MBS stops the supervision of the track occupancy state too soon while a supervision is still required for train"
  }
]

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>occupancy section [H-1, H-2, H-6.2]</td><td style='text-align: center;'>movement [H-1, H-2]</td></tr></table>

The loss scenarios for trackside assets occur together with unsafe control actions on the I_OBU interface (e.g. granting an MA) and the I_OP interface (e.g., manually reseat a TDS). Often, the state of the trackside assets constitutes the context under which control actions to the OBU or the operator panel becomes unsafe. These loss scenarios are not repeated here, as details on them are already listed in the previous section.

#### 5.7.4 I\_DR Interface

[
  {
    "Controllers": "Control Actions:",
    "DRMBSS": "DR -&gt; MBS• Provide validated topology and topography data.• Provide utilization restrictions (e.g., URA) for topology change.• Activate validated data version (Note: this assumes a new data version was previously provided)• Request currently used validated data version (Note: not safety related)"
  },
  {
    "Controllers": "Feedbacks:",
    "DRMBSS": "MBS -&gt; DR• Confirm data reception• Confirm/reject activation of utilization restriction• Confirm/Reject activation of new data version• Report currently used data version (Assumption: not safety related)"
  },
  {
    "Controllers": "Process Model",
    "DRMBSS": "MBS○ Current operational state (includes utilization restriction)○ Current active data version○ Currently inactive data versions○ Data verification &amp; validation signatures• DR○ Topology and Topography data○ Usage restrictions required for activation○ Data verification &amp; validation signatures"
  },
  {
    "Controllers": "Control Algorithm",
    "DRMBSS": "MBS"
  }
]

---

[
  {
    "○ Check if received data is malformed (Note: syntactic check only)○ Check if new data version is compatible with current operational state before activation○ Verify data signatures○ Verify required usage restrictions for topology change are active.• DR○ Validate data input against physical reality (or export responsibility to other entity -&gt;[ASM-26])○ Verify data against data engineering and validation rules○ Compile data version relevant for region of control○ Distribute data to consuming systems.○ Activate new data version synchronously for all recipients": "-"
  }
]

[
  {
    "Hazardous when": "Stopped too soon"
  },
  {
    "Hazardous when": "[UCA-DR-6] DR does not resend new topography data to MBS if the previous transmission failed. [H-8] (e.g. not checking that the data reception was confirmed)"
  }
]

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Activate validated data version</td><td style='text-align: center;'>[UCA-DR-7] DR provides activation of a data version to MBS when the data version to activate is not contained in the inactive data versions of MBS [H-8] [UCA-DR-8] DR provides activation of a data version to MBS when the activated data version does not match physical reality [H-8] [UCA-DR-13] DR provides activation of a data version for which MBS has not activated the required usage restriction. [UCA-DR-14] DR provides activation of a data version for which MBS has activated a wrong or insufficient usage restriction.</td><td style='text-align: center;'>[UCA-DR-9] DR does not provide activation of a new data version to MBS when current data version is more permissive than physical reality [H-8.3] (i.e. due to construction work)</td><td style='text-align: center;'>[UCA-DR-10] DR provides activation of a data version to MBS too late when the activated data version is more restrictive than the current data version [H-8.3] (e.g. speed restriction due to construction work) [UCA-DR-11] DR provides activation of a data version to MBS too early when the activated data version is more permissive than physical reality [H-8] (e.g. raising the speed limit before infrastructure has been completed)</td><td style='text-align: center;'>[UCA-DR-12] DR does not retry activation of a data version to MBS when the previous activation was rejected. [H-8] (e.g. not checking that the activation was confirmed)</td></tr></table>

Note: this design may add new UCA to MBS (e.g. performing safety checks against inactive data versions, activating a data version which endangers trains with granted movement permissions, not activating new data version, not verifying data signature, ...)

## Scenarios for selected unsafe control actions:

[S1-UCA-DR-1/2] DR provides a new set of domain data to MBS which has not been verified to comply with the given engineering rules, or which is malformed in other ways. Since no further checks are applied on MBS side a data type for the configuration of railway point P1 is misinterpreted such that point position "left" actually corresponds to point position "right". MBS then allows the movement of train T1 over point P1 leading to collision or derailment on a side track.

---

-> [SDR-25] DR shall include a set of verification functions that ensure that processed data follows the required engineering rules and is not malformed.

[S1-UCA-DR-3] DR provides a new set of domain data to MBS, however the distance between railway point P1 and railway point P2 in the data is longer than in reality. MBS is thus not aware that the Train T1 is actually reaching over P1 and allows P1 to be switched under T1 leading to a derailment.

-> [SDR-19] There shall be a “safety responsible” entity which is in a valid position to verify the correctness (correspondence to the physical reality) of the input data for MBS with a certainty corresponding to a SIL-4 function.

[S2-UCA-DR-3] DR provides a new set of domain data to MBS that was originally validated by a safety responsible according to [SDR-19], however the data was altered in and intermediate processing step such that the distance between railway point P1 and railway point P2 is now longer than in reality. MBS is thus not aware that the Train T1 is actually reaching over P1 and allows P1 to be switched under T1 leading to a derailment.

-> [SDR-20] MBS shall include a function that ensures that the input data (here Domain Data) received corresponds exactly to what has been verified and validated by the above (in UCA-DR-1) mentioned safety responsible (e.g. by means of a dedicated signature or safety code).

[S1-UCA-DR-4/5] Construction work to shorten a side track was scheduled for a certain date. Due to operational changes the actual construction work starts early, and a URA for work site protection is created together with the dispatcher. After the construction work is finished, the dispatcher lifts the worksite URA, although the topography and configuration data in MBS was not yet updated to reflect a shorter track. As a result, a train is authorized to enter the side track and collides with the buffer stop.

-> [SDR-21] An operational rule may be required, that ensures that any infrastructure changes have to be preceded by a (sufficiently large & restrictive) URA, and that this URA may only be lifted if the changes have been updated in the topography & configuration data of MBS.

[S1-UCA-DR-11] For some reason it was decided that domain data should be updated before the actual construction work on the tracks took place. To secure the area where track changes will occur a URA was foreseen. However, MBS was not commanded to activate this URA before the following topology/domain data update. Since MBS has no means of deciding if such a URA would have been required it activates the new domain data version right away. Subsequently, MBS allows a train to move into the site with a higher velocity than allowed for safe operation.

=> [SDR-24] If an URA for safe activation of new set of domain data is required the domain data shall include the reference for this URA (e.g. by means of a dedicated safety code).

---

[S1-UCA-DR-12] As in [S1-UCA-DR-11] but MBS received a URA from a Non-SIL system where an undetected error occurred that led to the URA being wrong/too small/too unrestrictive.

=> [SDR-22] There shall be a “safety responsible” entity which is in a valid position to define a (sufficiently large & restrictive) URA which covers the area in said AoC which is about to change during the upcoming data (Domain Data) update. Again, with a certainty corresponding to a SIL-4 function.

[S2-UCA-DR-12] As in [S1-UCA-DR-12] but the undetected error occurred during transmission and led to the URA being wrong/too small/too unrestrictive.

=> [SDR-23] MBS shall include a function that ensures that the received URA corresponds exactly to what was defined by the aforementioned safety responsible (e.g. by means of a dedicated safety code).

---

#### 5.7.5 I_PE Interface


[
  {
    "Controllers": "Control Actions:",
    "• PE• MBS": "PE -&gt; MBS• Connection    ○ Domain Data Version Check    ○ Synchronization Complete    ○ Close Connection• Command Change DPS state• Request Movement Authority• Revoke Movement Authority• Heartbeat"
  },
  {
    "Controllers": "Feedbacks:",
    "• PE• MBS": "MBS -&gt; PE• Connection    ○ Domain Data Version Check    ○ Synchronize Operational State    ○ Close Connection• Share operational state    ○ Report TACS State    ○ Report Train Object State• Reject command/request• Accept command/request    ○ Allow/grant command/request    ○ Deny command/request"
  },
  {
    "Controllers": "Process Model",
    "• PE• MBS": "• PE    ○ Operational State    ○ Safety Logic (needs to be aware what SL will do/grant)    ○ Operationally synchronized timetable• MBS    ○ Operational State    ○ Safety Logic"
  }
]

---

## FP2R2DATO


[
  {
    "Control Algorithm": "Remarks",
    "• MBS\n    ○ Check command/request validity\n    ○ Check command/request safety\n    ○ Incident/Emergency Routines\n    ○ Supervise heartbeat\n• PE\n    ○ Sequence Movement Authorities according to plan\n    ○ Command changed DPS state according to plan\n    ○ Request Movement Authority according to plan\n    ○ High-level Incident/Emergency Routines/Optimization\n    ○ Provide heartbeat": "Since PE performs only functions with SIL basic integrity, all commands from PE have to be checked by MBS an associated risk to safety in order to be suitable for SIL 4 functions."
  }
]

---

## 6 INTERFACE CRITICALITY

This chapter details the results of the safety analysis of the MBS safety boundary analysis and the related interfaces. The aim of this analysis is to identify safety related connections and systems relating to the MBS. The MBD shall support different modes of operation. This chapter analysis these modes for the impact to the MBS.

### 6.1 SYSTEM SAFETY BOUNDARY

The system boundary is given through the “system definition” from task 13.1 and was further analyzed from the safety perspective. The following figure classifies the sub systems of the MBD into safety related and non safety related controllers.

[
  {
    "Interface Name": "Interface description",
    "I_AS": "This interface represents the connection between the MBS and the neighbouring systems (MBS/RBC). The communication is done according to the specification of the ERTMS/ETCS SUBSET-037 and ERTMS/ETCS SUBSET-039."
  },
  {
    "Interface Name": "Connection",
    "I_AS": "Moving Block System (MBS) &lt;-&gt; Neighbouring (MBS/RBC) System Adjacent System"
  },
  {
    "Interface Name": "Safety related",
    "I_AS": "Yes"
  },
  {
    "Interface Name": "Remarks",
    "I_AS": "MBS &lt;-&gt; MBS/RBC handover not in scope of this analysis."
  },
  {
    "Interface Name": "Interface Name",
    "I_AS": "I_DR"
  },
  {
    "Interface Name": "Interface description",
    "I_AS": "This interface represents the connection between the DR and the MBS. DR provides updates of existing and new data to the MBS by using a standardised data format."
  },
  {
    "Interface Name": "Connection",
    "I_AS": "Digital Register (DR) &lt;-&gt; Moving Block System (MBS)"
  },
  {
    "Interface Name": "Safety related",
    "I_AS": "Overall system safety depends on data veracity but not e.g., on interface availability."
  },
  {
    "Interface Name": "Safety implication",
    "I_AS": "Safety measures"
  },
  {
    "Interface Name": "Interface integrity (MBS needs information to be unmodified)",
    "I_AS": "Integrity could be verified by using a data/bulk checksum."
  },
  {
    "Interface Name": "Correctness of data (MBS needs information to represent the correct state)",
    "I_AS": "Ensured through dependable external system/actor signature, e.g., if data is pre-validated."
  },
  {
    "Interface Name": "Availability of connection (relevant for MBS safety function)",
    "I_AS": "No safety related implications."
  },
  {
    "Interface Name": "Remarks",
    "I_AS": "-"
  },
  {
    "Interface Name": "Interface Name",
    "I_AS": "I_OBU"
  },
  {
    "Interface Name": "Interface description",
    "I_AS": "This interface represents the connection between the MBS and the ETCS on-board unit (OBU). The communication is done according to the specification of the ERTMS/ETCS SUBSET-026 and ERTMS/ETCS SUBSET-037."
  },
  {
    "Interface Name": "Connection",
    "I_AS": "Moving Block System (MBS) &lt;-&gt; ECTS on-board (OBU)"
  },
  {
    "Interface Name": "Safety related",
    "I_AS": "Yes"
  },
  {
    "Interface Name": "Safety implication",
    "I_AS": "Safety measures"
  },
  {
    "Interface Name": "Interface integrity (MBS needs information to be unmodified)",
    "I_AS": "Integrity already ensured through SS-026/SS037."
  },
  {
    "Interface Name": "Correctness of data (MBS needs information to represent the correct state)",
    "I_AS": "Correctness already ensured through SS-026/SS037."
  },
  {
    "Interface Name": "Availability of connection (relevant for MBS safety function)",
    "I_AS": "Monitoring of continuous connection already ensured through SS-026/SS-037."
  },
  {
    "Interface Name": "Remarks",
    "I_AS": "-"
  }
]

[
  {
    "Interface Name": "Interface description",
    "I_OP": "This interface represents the connection between the MBS and the operator position with the intend to exchange operation relevant information for SIL-2 functions (e.g.: railway point lock)."
  },
  {
    "Interface Name": "Connection",
    "I_OP": "Moving Block System (MBS) &lt;-&gt; Operator Position"
  },
  {
    "Interface Name": "Safety related",
    "I_OP": "Yes"
  },
  {
    "Interface Name": "Safety implication",
    "I_OP": "Comment"
  },
  {
    "Interface Name": "Interface integrity (MBS needs information to be unmodified)",
    "I_OP": "Technical/Operational considerations required"
  },
  {
    "Interface Name": "Correctness of data (MBS needs information to represent the correct state)",
    "I_OP": "Technical/Operational considerations required"
  },
  {
    "Interface Name": "Availability of connection (relevant for MBS safety function)",
    "I_OP": "Technical/Operational considerations required"
  },
  {
    "Interface Name": "Remarks",
    "I_OP": "-"
  },
  {
    "Interface Name": "Interface Name",
    "I_OP": "I_PE"
  },
  {
    "Interface Name": "Interface description",
    "I_OP": "This interface represents the connection between the MBS and the PE. For the data exchange between the MBS and the PE a standardised data format is used."
  },
  {
    "Interface Name": "Connection",
    "I_OP": "Moving Block System (MBS) &lt;-&gt; Plan Execution (PE)"
  },
  {
    "Interface Name": "Safety related",
    "I_OP": "No"
  },
  {
    "Interface Name": "Safety implication",
    "I_OP": "Comment"
  },
  {
    "Interface Name": "Interface integrity (MBS needs information to be unmodified)",
    "I_OP": "Already set / Not critical"
  },
  {
    "Interface Name": "Correctness of data (MBS needs information to represent the correct state)",
    "I_OP": "Already set / Not critical"
  },
  {
    "Interface Name": "Availability of connection (relevant for MBS safety function)",
    "I_OP": "Already set / Not critical"
  },
  {
    "Interface Name": "Remarks",
    "I_OP": "As the MBS shall reject requests from PE which can result in an unsafe system state. This interface is not considered safety related, as unsafe requests are simply rejected."
  }
]

[
  {
    "Interface Name": "Interface description",
    "I_TACS": "This interface represents the connection between the MBS and the Trackside Assets Control and Supervision (TACS) according to the specification of the EULYNX standards."
  },
  {
    "Interface Name": "Connection",
    "I_TACS": "Moving Block System (MBS) &lt;-&gt; Trackside Assets Control and Supervision (TACS)"
  },
  {
    "Interface Name": "Safety related",
    "I_TACS": "Yes"
  },
  {
    "Interface Name": "Safety implication",
    "I_TACS": "Comment"
  },
  {
    "Interface Name": "Interface integrity (MBS needs information to be unmodified)",
    "I_TACS": "Already set / Not critical"
  },
  {
    "Interface Name": "Correctness of data (MBS needs information to represent the correct state)",
    "I_TACS": "[minor] operational considerations required"
  },
  {
    "Interface Name": "Availability of connection (relevant for MBS safety function)",
    "I_TACS": "Already set / Not critical"
  },
  {
    "Interface Name": "Remarks",
    "I_TACS": "-"
  }
]

[
  {
    "Interface Name": "Interface description",
    "I_PEOP": "This interface represents the connection between the plan execution (PE) and the operator position with the intent to exchange operation relevant information for none safety related functions."
  },
  {
    "Interface Name": "Connection",
    "I_PEOP": "Plan Execution &lt;-&gt; Operator Panel"
  },
  {
    "Interface Name": "Safety related",
    "I_PEOP": "No"
  },
  {
    "Interface Name": "Safety implication",
    "I_PEOP": "Comment"
  },
  {
    "Interface Name": "Interface integrity",
    "I_PEOP": "-"
  },
  {
    "Interface Name": "Correctness of data",
    "I_PEOP": "-"
  },
  {
    "Interface Name": "Availability of connection",
    "I_PEOP": "-"
  },
  {
    "Interface Name": "Remarks",
    "I_PEOP": "Not further assessed, as it is assumed, that the data input is correct and completely provided and this interface has no direct communication to the MBS system."
  }
]

[
  {
    "Interface Name": "Interface description",
    "I_PETMS": "This interface represents the connection between the PE and TMS and has no interface to the MBS."
  },
  {
    "Interface Name": "Connection",
    "I_PETMS": "Plan Execution (PE) &lt;-&gt; Traffic Management System (TMS)"
  },
  {
    "Interface Name": "Safety related",
    "I_PETMS": "No"
  },
  {
    "Interface Name": "Safety implication",
    "I_PETMS": "Comment"
  },
  {
    "Interface Name": "Interface integrity",
    "I_PETMS": "-"
  },
  {
    "Interface Name": "Correctness of data",
    "I_PETMS": "-"
  }
]

---

[
  {
    "Availability of connection": "Remarks",
    "No safety related implications.": "Not further assessed, as it is assumed, that the data input is correct and completely provided and this interface has no direct communication to the MBS system.",
    "-": "Not further assessed, as it is assumed, that the data input is correct and completely provided and this interface has no direct communication to the MBS system."
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "Track Status Area erroneously cleared during L3 Trackside initialisation by dispatcher leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "At L3 Trackside initialisation, in addition to communicating trains there could be non-communicating trains (e.g. in modes SH, NP, etc.) or other obstructions such as vehicles not equipped with ETCS, work areas, etc. After initialisation (either in planned circumstances or as a consequence of a system fault) the Level 3 Trackside has to ascertain the Train Location of all vehicles and obstructions in the Area. If the L3 Trackside allows for a responsible person to declare Clear Track Status Areas, then it is critical that the area is only determined Clear when it is truly clear to avoid a Movement Authority into an Occupied Track Status Area, that could lead to a collision."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "[UCA-OP-1], [SDR-1], [SDR-3]."
  },
  {
    "Hazard": "Hazard",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "4.1.2 Using invalid/outdated stored information for L3 Trackside initialisation"
  },
  {
    "Hazard": "Hazard headline",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "Track Status Area erroneously cleared during L3 Trackside initialisation by system leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "&quot;At L3 Trackside initialisation, in addition to communicating trains there could be non-communicating trains (e.g. in modes SH, NP, etc.) or other obstructions such as vehicles not equipped with ETCS, work areas, etc.After initialisation (either in planned circumstances or as a consequence of a system fault) the Level 3 Trackside has to ascertain the Train Location of all vehicles in the Area.If the L3 Trackside utilises stored information to clear Track Status Areas, then it is critical that this information is correct to avoid a Movement Authority into an occupied area, that would lead to a collision.The information may no longer be correct and erroneously consider the track clear when it is still occupied.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "Depends on specific implementation (utilizing previously stored data after initialization) and this is out of scope at this state of analysis."
  },
  {
    "Hazard": "Hazard",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "4.1.3 Deactivating Temporary Shunting Area"
  },
  {
    "Hazard": "Hazard headline",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "Track Status Area erroneously cleared after deactivation of a Temporary Shunting Area leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "The L3 Trackside considers the track status in an Active Shunting Area as Unknown Track Status Area, except for the Train Location of communicating trains. When deactivating a Shunting Area, responsible staff may have the possibility to clear any remaining Unknown Track Status Area. Doing this, an occupied area of track could be set to clear, leading to collision."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.1.1 Dispatcher interaction in L3 Trackside initialisation": "[out of scope]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.1.4 Driver confirms train integrity": "Track Status Area erroneously cleared by driver confirming Train Integrity leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.1.4 Driver confirms train integrity": "In case a train driver confirms Train Integrity after a part of the train has been lost, the lost part will be not detected (unless there is TTD), which could lead to collision with other trains approaching the area where the lost part is. This situation could occur when operating trains without TIMS or for a train with a failed TIMS."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.1.4 Driver confirms train integrity": "[H-1][SC-2.7][SC-6.1][ASM-3][ASM-6][ASM-8][SDR-12]The analysis considers in the unsafe control actions of the I_OBU interface different scenarios about unknown train position."
  },
  {
    "Hazard": "Hazard",
    "4.1.4 Driver confirms train integrity": "4.1.5 Recovery of a failed train"
  },
  {
    "Hazard": "Hazard headline",
    "4.1.4 Driver confirms train integrity": "Track Status Area erroneously cleared by TIMS device not being able to detect loss of train integrity after coupling trains leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.1.4 Driver confirms train integrity": "&quot;When a train is coupled with another train they should be considered as one train with a common train integrity. However, this depends on if the TIMS devices in the coupled trains are compatible or if the TIMS in the rear part is operational. In case the driver updates the train length to that of the coupled trains without knowing the status of the TIMS device in the rear part, a loss of integrity in the rear part will not be detected and reported by the TIMS in the front part of the train. This could happen in a rescue situation when there is need to pull out a failed train and lead to a collision if the track is cleared based on information which is not valid for the complete train and a part of it is lost without being detected.&quot;"
  }
]

---

[
  {
    "Trace to R2DATO": "[SC-2.7]"
  },
  {
    "Trace to R2DATO": "[SC-6.1]"
  },
  {
    "Trace to R2DATO": "[ASM-3]"
  },
  {
    "Trace to R2DATO": "[ASM-6]"
  },
  {
    "Trace to R2DATO": "[ASM-8]"
  },
  {
    "[H-1]": "The analysis considers in the unsafe control actions of the I_OBU interface different scenarios about unknown train position."
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.2.1 Confidence interval reduced at End of Mission": "Error in Train Location from reduced confidence interval at End of Mission leads to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.2.1 Confidence interval reduced at End of Mission": "&quot;The L3 Trackside needs to determine the area that could be occupied by a train performing End of Mission (EoM) in order to protect it. To that aim, the L3 Trackside is expected to use the location information received from the train. However, as part of the ERA CCM Process an ambiguity in the specifications has been identified which makes it unclear how the ETCS On-board calculates the confidence interval reported at EoM. This is because linking information, including balise location accuracy used in the confidence interval, is deleted when changing to SB mode. If the location accuracy of the LRBG has a larger value than the National Value (Q_NVLOCACC) and the ETCS On-board uses the National Value in the EoM Position Report, this could lead to a collision if the Unknown Track Status Area for protecting the train is unduly shortened, not covering the whole length of the train.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.2.1 Confidence interval reduced at End of Mission": "[not applicable - described hazard results from a specific implementation]"
  },
  {
    "Hazard": "Hazard",
    "4.2.1 Confidence interval reduced at End of Mission": "4.2.1 Lack of linking information"
  },
  {
    "Hazard": "Hazard headline",
    "4.2.1 Confidence interval reduced at End of Mission": "Error in Train Location from lack of linking information leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.2.1 Confidence interval reduced at End of Mission": "When relocation is done for a new balise group without linking information (Subset-026, 3.4.4 [BL3 R2]) the ETCS On-board uses the estimated distance travelled between the previous LRBG and the new LRBG. Next figure illustrates the potential issue that arises."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.2.1 Confidence interval reduced at End of Mission": "Figure 1: On-board mSRE relocation in the absence of linking information At time T0 (i.e. the time when the train was last known to be integer), the LRBG was BG_A. At time T1, BG_B is encountered, the ETCS On-board then relocates the Min Safe Rear end at T0 to the new LRBG. If linking information is not available or not used, the ETCS On-board then sends a position report to the L3 Trackside using the estimated distance between BG_A and BG_B when calculating the safe train length. If this estimate is shorter than the real distance between BG_A and BG_B, the L3 Trackside believes that the confirmed rear end is closer to BG_A than it actually is. This means that in case the train has been broken between time T0 and T1, but not yet detected by the TIMS device, there could be a part of the train in the section of track that was just cleared, but the L3 Trackside is not aware of this."
  },
  {
    "Hazard": "Hazard",
    "4.2.1 Confidence interval reduced at End of Mission": "4.3.1 Reported train length shorter than actual"
  },
  {
    "Hazard": "Hazard headline",
    "4.2.1 Confidence interval reduced at End of Mission": "Train Length value shorter than the actual length leading to collision, derailment, or exceeding speed limits"
  },
  {
    "Hazard": "Hazard description",
    "4.2.1 Confidence interval reduced at End of Mission": "&quot;In case the Train Length given in the Validated Train Data to the L3 Trackside is shorter than the physical train length, this could result in:  ·Another train being authorised beyond the rear of this train located in front, OR  ·Infrastructure released (points moved) under the train, OR  ·Train does not achieve calculated braking curves, OR  ·Train permitted to accelerate earlier after speed restrictions.The error in Train Length could be caused by:  ·Incorrect train length provided by an external system.  ·Incorrect train length entered by the Driver at Start of Mission.  ·Driver does not update the train length after joining.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.2.1 Confidence interval reduced at End of Mission": "R2DATO assumes in the [ASM-8] and [ASM-9] the correct reporting of the correct train length and train integrity.To show why these assumptions are needed, the analysis considers in [S2-UCA-MBS-16] the safety implications of a reported train length shorter than physical reality. This also results in recommendations regarding expected splitting and joining operations ([SDR-11] and [SDR-12])"
  },
  {
    "Hazard": "Hazard",
    "4.2.1 Confidence interval reduced at End of Mission": "4.3.2 Reported train length longer than actual"
  },
  {
    "Hazard": "Hazard headline",
    "4.2.1 Confidence interval reduced at End of Mission": "Train Length value longer than the actual length leading to collision or exceeding speed limits"
  },
  {
    "Hazard": "Hazard description",
    "4.2.1 Confidence interval reduced at End of Mission": "&quot;In case the Train Length given in the Validated Train Data to the L3 Trackside is longer than the physical train length, this could result in a Track Status Area which is Occupied or Unknown being cleared while still occupied by another vehicle, or that the calculated braking curves are not met by the train. The error in Train Length could be caused by:  ·Incorrect train length provided by an external system.  ·Incorrect train length entered by the Driver at Start of Mission."
  }
]

---

[
  {
    "☐ Driver does not update the train length after splitting.&quot;": "R2DATO assumes in the [ASM-8] and [ASM-9] the correct reporting of the correct train length and train integrity.To show why these assumptions are needed, the analysis considers in [S1-UCA-MBS-16] the safety implications of a reported train length longer than physical reality. This also results in recommendations regarding expected splitting and joining operations ([SDR-11] and [SDR-12])"
  }
]

[
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "4.4.1 Wrong side failure of CMD"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "CMD erroneously validates a position which is incorrect leading to collision or derailment"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "&quot;In case CMD validates the position of a train after being moved in NP mode, the L3 Trackside can give this train a Movement Authority based on the position at End of Mission while the train is now somewhere else. This may lead to derailment or collision.Note that some CMD equipment may allow for a short movement of a train whilst still reporting “no cold movement detected”.Potential mitigations:The following considerations could be taken as mitigation measures:• Hazardous failure rate for CMD to be considered.• Use linking reaction for the first expected Balise Group in the linking chain when authorising trains to move, which will brake the train if it is not found as expected.• Use TTD where trains start after NP mode. However, this is not enough on its own.&quot;"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "[S3-UCA-MBS-16][S4-UCA-MBS-16][mainly concerns the SIL classification of the CMD device]"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "This section describes causes which result in undetected movement of a train"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "4.5.1 Rollback after standstill"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "Undetected backward movement after standstill leading to collision"
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "If a train moves backwards after reaching standstill, it could compromise the authorisation for another train. It can take some time before the L3 Trackside can react on this potentially hazardous situation and try to prevent a collision."
  },
  {
    "This section describes the result of a CMD system erroneously validating the location of a train": "[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.5.2 Unreported Movement": "Unreported Train movement leading to collision or derailment"
  },
  {
    "Hazard": "Hazard description",
    "4.5.2 Unreported Movement": "&quot;If a non-communicating train is moved, the movement is not reported to the trackside, and therefore, the L3 Trackside has no knowledge of the movement, and may authorise a conflicting train movement.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.2 Unreported Movement": "[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.5.3 At entrance to Level 3 area": "Undetected movement entering the L3 area leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.3 At entrance to Level 3 area": "In degraded situations, it could occur that a train incorrectly enters the L3 Area when it is not authorised, and it is not detected by the L3 Trackside."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.3 At entrance to Level 3 area": "[ASM-4-v2]"
  },
  {
    "Hazard": "Hazard",
    "4.5.3 At entrance to Level 3 area": "4.5.4 After End of Mission"
  },
  {
    "Hazard": "Hazard headline",
    "4.5.3 At entrance to Level 3 area": "Undetected movement after End of Mission leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.3 At entrance to Level 3 area": "If a train in SB mode rolls away, Standstill Supervision will result in a brake application once the train moves beyond the distance D_NVROLL. This results in the train being brought to a halt, after which the driver can acknowledge the standstill supervision, releasing the brake. There is no limit on the number of acknowledgements the driver is allowed to make, since this may inhibit Splitting operations. This functionality can enable the driver to use consecutive acknowledgements of the standstill supervision activation to move the train. Figure 3 illustrates the movement that could occur."
  }
]

---

[
  {
    "consecutive roll away movements.": "[ASM-4-v2]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.5.5 Loss of Train Integrity": "Undetected movement of a part of the train after loss of integrity leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.5 Loss of Train Integrity": "In case train integrity has been lost and part of the train rolls backwards due to the gradient profile, this may result in a collision with other vehicles. In case of derailment, collisions can also occur on adjacent tracks."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.5 Loss of Train Integrity": "[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.5.6 Propelling train": "Undetected movement beyond the secured area for a propelling train leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.6 Propelling train": "&quot;In case a train is pushing another train in front of it (propelling movement) there is a risk that the front of the propelled train overpasses the area reserved for this movement as the driver in the propelling train cannot see where the front is. This can happen if there is need to rescue a failed train from the rear. The rescue train will then be propelling a piece of rolling stock in front of it that cannot report its position.If the front of this movement overpasses the reserved area, a collision may occur as the L3 Trackside is not aware of the real &quot;&quot;front end&quot;&quot; (belonging to the failed train) and able to react on this situation to protect other movements. As mSFE and Train length doesn&#x27;t match with the real train this could lead to a wrong track status.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.6 Propelling train": "[rescue train out of scope]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.5.7 Shunting train": "Undetected movement out of an Active Shunting Area leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.7 Shunting train": "Shunting movements may unintentionally move beyond the border of an Active Shunting Area without the L3 Trackside being aware of this and therefore being unable to protect other movements in the vicinity of the Shunting Area."
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.7 Shunting train": "[shunting out of scope]"
  },
  {
    "Hazard": "This section describes the result of a TTD which erroneously indicates a section of track as Clear Track Status Area",
    "4.5.7 Shunting train": "This section describes the result of a TTD which erroneously indicates a section of track as Clear Track Status Area"
  },
  {
    "Hazard": "Hazard",
    "4.5.7 Shunting train": "4.6.1 Wrong side failure of TTD"
  },
  {
    "Hazard": "Hazard headline",
    "4.5.7 Shunting train": "TTD erroneously indicates a Clear Track Status Area leading to collision or derailment"
  },
  {
    "Hazard": "Hazard description",
    "4.5.7 Shunting train": "&quot;If TTD is used to clear track irrespective of Train Locations, then:  ◦ An Unknown Track Status Area could be cleared without being swept,  ◦ Infrastructure could be released or moved under a train,  ◦ Erroneously updating the CRE of the train in front, and consequently providing an MA to a following train that could result in a collision.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.7 Shunting train": "[according to assumption ASM-13 TTD is considered a SIL4 function]"
  },
  {
    "Hazard": "Hazard",
    "4.5.7 Shunting train": "4.7.1 Points Moved After Communications failure"
  },
  {
    "Hazard": "Hazard headline",
    "4.5.7 Shunting train": "A point is moved in an Unknown/Occupied/Reserved Track Status Area with a train over it, or when it is about to pass over it, leading to derailment"
  },
  {
    "Hazard": "Hazard description",
    "4.5.7 Shunting train": "&quot;The Dispatcher needs to move a train inside an Unknown, Occupied or Reserved Track Status Area to a new location. Figure 4 illustrates the situation with a train approaching a set of points inside an Unknown Track Status Area. Figure 4: Unknown Track Status Area due a Communication failureThe Dispatcher would need to move points so that the train can be moved to a siding. In the absence of TTD, moving a point could cause a derailment if moved when a train is over or about to pass it.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.7 Shunting train": "[ASM-4-v2]"
  },
  {
    "Hazard": "Hazard",
    "4.5.7 Shunting train": "4.8.1 Mixed traffic"
  },
  {
    "Hazard": "Hazard headline",
    "4.5.7 Shunting train": "Non-ETCS train erroneously enters a route for an ETCS L3 train leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.7 Shunting train": "&quot;Drivers that operate both ETCS and non-ETCS fitted trains may mistakenly use a &#x27;proceed for ETCS&#x27; aspect when operating a non-ETCS train due to confusion of ETCS and non-ETCS experience. Such a situation may result in a SPAD (Signal Passed At Danger) and a collision. This could happen at borders to the L3 Area but also inside an area with mixed traffic where L3 is used as an overlay to a conventional system with optical signals. This hazard is the same as in Level 2. It is the same situation as a non-ETCS train erroneously entering a route set for a Level 2 train in a mixed traffic area.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.7 Shunting train": "[assumption [ASM-3] – there are no non-ETCS trains with regular movements]"
  },
  {
    "Hazard": "Hazard",
    "4.5.7 Shunting train": "4.8.2 Reversing"
  },
  {
    "Hazard": "Hazard headline",
    "4.5.7 Shunting train": "Train moves backwards after loss of train integrity leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.5.7 Shunting train": "&quot;In case a train needs to reverse after a loss of train integrity it may collide with the part of the train that was lost:Figure 5: Train reversing after loss of integrityFigure 5: Train reversing after loss of integrityThis hazard is the same as in Level 2, and in conventional signalling.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.5.7 Shunting train": "[reversing out of scope]"
  }
]

[
  {
    "Hazard": "Hazard headline",
    "4.8.3 Loss of train integrity": "Derailment after loss of train integrity causes obstruction in adjacent tracks leading to collision"
  },
  {
    "Hazard": "Hazard description",
    "4.8.3 Loss of train integrity": "&quot;After a loss of train integrity, the lost part of the train could derail causing an obstruction in the adjacent track resulting in a collision. This hazard is the same as in Level 2, and in traditional signalling.&quot;"
  },
  {
    "Hazard": "Trace to R2DATO",
    "4.8.3 Loss of train integrity": "[S3-UCA-MBS-16][S4-UCA-MBS-17][S5-UCA-MBS-17]"
  }
]

<div style="text-align: center;">Table 56 – 4.1.1 Dispatcher interaction in L3 Trackside initialisation</div>

---

## 8 COMPILED DESIGN RECOMMENDATIONS

This chapter contains the compiled safety design recommendations for the analyzed control loops supplemented with rationale, guidance &/or example statements. Although these enriched recommendations should be self-explanatory, it might make sense to look up the linked (hypothetical) scenarios for each, that led to unsafe control actions in the chapters above.

### 8.1 UNSAFE CONTROL ACTIONS TOWARDS ON BOARD UNIT

=>[SDR-13]: In regions where the parking of vehicles is expected, methods for detecting the presence of trains independent of train position reports shall be available (i.e. installing TTDs in these regions)

Rationale Uncontrolled train movements, like runaway cars after parking, are not constrained by a movement authority. Such a scenario is described in  $ [S3-UCA-MBS-16] $ 

=> [SDR-16]: Between controlled region and unsupervised region, the movement of non-communicating trains shall be detectable, i.e. using TTDs, or preventable using a point/derailer (similar to [SDR-13])

Rationale Detecting or preventing the presence of uncontrolled trains out of unsupervised regions (e.g. at the borders of the region of control) is needed for assumption 2. A corresponding scenario is described in [S2-UCA-MBS-17].

=> [SDR-18] Simple detection of track occupation is not sufficient to prevent flank collisions in all cases. Technical means to secure a sufficiently large vacant area before the fouling point is required.

Rationale Even when the train presence is detected according to assumption 1., the reaction times can be insufficient to prevent a flank collision hazard, making further measures necessary:

=> [ASM-4-v2] MBS does not require TTDs for controlled train movement but supports them for migration purposes or systems where the chance of uncontrolled movement cannot be sufficiently controlled by other means.

Rationale The assumption that TTDs can completely be eliminated while still guarding against all loss scenarios found in our analysis is too strong. As long as uncontrolled train movement cannot be eliminated, their presence is still required.

---

=> [SDR-11]: MBS shall always be aware when a change of train length is expected (i.e. due to splitting and joining).

Rationale If the MBS detects an unexpected difference between the reported and expected train length, this could indicate a wrong data input (either by the driver or in the operation plan).

Example This can be done e.g. by informing the MBS that splitting or joining is performed via the plan execution.

### 8.2 UNSAFE CONTROL ACTIONS TOWARDS OPERATOR PANEL

=> [SDR-1]: Provide an operational rule set which explicitly determines to which infrastructure item a completed (safety related) intervention refers/referred to.

Rationale Since safety functions of MBS directly depend on the correctness of its operational state, special care has to be taken where a human operator is allowed to issue safety related commands or settings.

=> [SDR-2]: When changes to the operational state are reported by personnel, the operator shall always check if they are already entered in the operation state of MBS, even if the operator believes this has already been done in the past

Rationale as above.

=> [SDR-3]: The operator panel shall provide easily accessible information on all currently manually entered infrastructure state with the required confidence for a safety related function.

Rationale The operator shall have a means to reproduce origin and the reliability of the presented data.

=> [SDR-4]: The interface for the operator shall allow to pre-schedule usage restriction areas.

Rationale In order to avoid secondary (possibly non-SIL systems) tools, or even pen & paper solutions the system shall include safe and transparent means for pre-scheduling.

=> [SDR-5]: The operator shift handover shall include either an operational process or digital means that prevent a loss of (safety related) information during the handover.

Guidance Ideally all relevant information as well as the handover- procedure itself are foreseen in the operator panel/system.

Example Whenever the operator confirms a (safety related) request from any other stakeholder, this confirmation shall contain a token (e.g., safety code) either from MBS or a trustworthy operator panel, guaranteeing that the said intervention is either already in place or dependably pre-scheduled.

=> [SDR-6]: The operator panel should implement procedures to verify the entered usage restriction data, before the entered data is passed to the MBS system.

---

Rationale Since the operator is still a human being, additional procedures to verify the inputs are recommended.

=> [SDR-7]: Entering usage restriction areas shall take priority over the regular management of running trains

Rationale E.g., a usage restriction that was issued to late is a safety risk.

Guidance Maybe an even more general prioritization of tasks could be implemented. The life-cycle of URAs -> is a design decision potentially influencing multiple systems.

=> [SDR-8]: The operator shall always verify with the construction team on site that the work has actually been completed before removing the corresponding usage restriction area.

Rationale Again, possibly safety related information from/through human beings needs to be re-checked by adequate processes and rules.

=> [SDR-9]: The operator panel shall be designed to support the operator with contextual information when executing operator commands. I.e. the operator shall be able to select the stopping position based on an interface with information about the physical elements/trackside assets and select a stopping position based on the physical elements position.

Rationale With processes that have a “human in the loop” also the feedback to this human – e.g., its readability and its correctness - may have safety implications.

=> [SDR-10]: The operator shall receive a (visual) indication about the reported train position age. (e.g., information outdated longer than for a defined threshold should be indicated).

Rationale Edge cases that result from timing interrelation (e.g., max. GSM-R signal roundtrip) in the greater system need to be – at least - visible to the operator.

### 8.3 UNSAFE CONTROL ACTIONS TOWARDS TRACKSIDE ASSESTS CONTROL & SUPERVISION

Those UCAs are either covered with measures defined in the EULYNX specification or are directly linked to moving trains - and thus covered by UCAs towards the onboard unit (8.1.).

---

### 8.4 UNSAFE CONTROL ACTIONS REGARDING DOMAIN DATA & UPDATES

=> [SDR-25] DR shall include a set of verification functions that ensure that processed data follows the required engineering rules and is not malformed.

Rationale as with [SDR-19].

=> [SDR-19] There shall be a “safety responsible” entity which is in a valid position to verify the correctness (correspondence to the physical reality) of the input data for MBS with a certainty corresponding to a SIL-4 function.

Rationale With the concept of a “generic” Safety Logic the functional behavior of MBS depends on the correctness (conformity with physical reality) of its input topography- and configuration data (here Domain Data) from an external source.

Guidance This is a nonnegligible advantage over past and current approaches (see Figure 9). For example, MBS allows for much greater flexibility with regards to setting MAs instead of relying on pre-defined routes. However, since MBS cannot verify that correspondence to physical reality by itself, an exported requirement demanding proof, as well as a clear path of responsibility shall be established.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0e12fa31-2086-4478-a54f-9be7510baa76/markdown_0/imgs/img_in_image_box_118_851_981_1068.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A50%3A57Z%2F-1%2F%2Fd31d8dbe8f4462b25d42f2ce8938f86ffab32327c5509891dbe262b0942e8bc7" alt="Image" width="72%" /></div>


<div style="text-align: center;">Figure 9: Generic Safety Logic</div>


=> [SDR-20] MBS shall include a function that ensures that the input data (here Domain Data) received corresponds exactly to what has been verified and validated by the above (in UCA-DR-1) mentioned safety responsible (e.g. by means of a dedicated signature or safety code).

Rationale If there are intermediaries between the entity that validated the input data for MBS and MBS itself, then a method is required to assure that the data has not been altered/changed in between.

Example The following figure shows how such a tracing of the safety responsibility for new topography and configuration data could be implemented. In this case the responsibility lies with the engineering data supplier:

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8430975d-1476-4909-8ff7-2ccc4ef31d7a/markdown_0/imgs/img_in_image_box_126_193_822_757.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A51%3A01Z%2F-1%2F%2F8f144502f435be1e0ee3badd4fe66744ec13310a550c30df64df324fa6d69336" alt="Image" width="58%" /></div>


<div style="text-align: center;">Figure 10: Example for tracing of safety responsibility for topography & configuration data</div>


=> [SDR-21] An operational rule may be required, that ensures that any infrastructure changes have to be preceded by a (sufficiently large & restrictive) URA, and that this URA may only be lifted if the changes have been updated in the topography & configuration data of MBS.

Rationale MBS lacks the information to verify that the URAs are sufficiently restrictive for the infrastructure change to be safely performed. This verification must therefore be performed by other means, e.g. an operational rule.

=> [SDR-22] There shall be a “safety responsible” entity which is in a valid position to define a (sufficiently large & restrictive) URA which covers the area in said AoC which is about to change during the upcoming data (Domain Data) update. Again, with a certainty corresponding to a SIL-4 function.

Rationale Similar to the correctness of topography and configuration for normal operations, it is paramount that the URA covering the area that is about to change during an update (of Domain Data) is sufficiently large and correct.

Alternative MBS could have a capability that allows to derive the delta between the current and the uploaded new/next Domain data update. However, a separate (and safe) concept on how to derive a sufficiently large URA would be required.

---

=> [SDR-23] MBS shall include a function that ensures that the received URA corresponds exactly to what was defined by the aforementioned safety responsible (e.g. by means of a dedicated safety code).

Rationale If there are intermediaries between the entity that defined the URA and MBS itself, then a method is required to assure that the data has not been altered/changed in between.

Example Similarly, the engineering data supplier could also provide the extent/type of the required URA, even though it is then timed/initiated through TMS/PE:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7641e283-92cb-423c-89f0-de118acaf0f0/markdown_0/imgs/img_in_image_box_108_488_794_1000.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A51%3A04Z%2F-1%2F%2F73180de7a54a82496b8bf43c4187a9c96091716203870dba5cd39d6a94d69cd3" alt="Image" width="57%" /></div>


<div style="text-align: center;">Figure 11: Example for tracing of safety responsibility for update URA</div>


Finally, MBS would only have to check if the URA is in place before activating the update within itself:

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b7775131-3ec3-40e0-9fc8-3cbf6c0a3930/markdown_0/imgs/img_in_image_box_198_191_835_728.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A51%3A07Z%2F-1%2F%2Faa57a4069c474836f3dd1d568b8e4e60de6eefacfe1d157ffad97bebc76e6f19" alt="Image" width="53%" /></div>


<div style="text-align: center;">Figure 12: Example for verifying URA status.</div>


=> [SDR-24] If an URA for safe activation of new set of domain data is required the domain data shall include the reference for this URA (e.g. by means of a dedicated safety code).

Rationale MBS (or DR if designed with sufficient SIL) shall be able to decide if the required precautions were taken before activating a new version of domain data.

---

## 9 SAFETY RESULTS & CONCLUSION

### 9.1 STRUCTURE OF THE RESULTS

The results of this document are presented in three separate chapters:

Chapter 6 “Interface Criticality” contains the analysis of the safety relevance of the interfaces connected directly to the MBS. The neighbouring system is specified in the name of the interface (e.g.: I_DR is the interface between the MBS and the DR). An analysis with respect to the correctness and integrity of the data as well as the availability of the connection was also conducted for each interface. The following interface are listed as safety related: I_AS, I_OBU, I_OP, I_TACS.

Chapter 7 “Mapping of X2Rail Safety Analysis” covers the safety analysis results [X2RAIL-5] of the project X2RAIL to ensure that they are adequately considered in this analysis. This is done by analyzing each hazard from the X2Rail results and by providing a trace to different artefacts of the STPA analysis. It can be stated that the X2RAIL results - where applicable (not bound to a S2R specific solution) - are fully covered by the artifacts (e.g. assumptions, design recommendations, interface analysis, ...) from this task.

Chapter 8 “Compiled Design Recommendations” contains the results of the risk analysis in Chapter 5 above, supplemented with rationale, guidance & example statements where applicable. Although these enriched recommendations should be self-explanatory, it makes sense to look up the linked unsafe control actions in the chapters above. They describe how such a hypothetical scenario could have occurred and form the background for the recommendations.

### 9.2 STARTING POINT

The basis for this analysis was the rough system architecture that is baked into the grant agreement as well as various sources from previous projects (see chapter 3). However, essential inputs from system pillar were not available at the time. Thus, an own list of assumptions (see chapter 5.5) was created, compared, mapped, and supplemented with a similar list from the system definition task (13.1). Similarly, the operational context was rather compiled and derived from state-of-the-art procedures in the participating railway companies than given from the normative side. Another factor shaping the work in this task, were the resources at hand, and the parallelized work structure given through the grant agreement.

---

### 9.3 POSITIONING AND OBJECTIVES

Overall, the undertaking in this task can best be compared to step 3 in the classic V-Cycle from the CENELEC norms.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a6c8b1b0-57c9-4159-8b6b-12abd849eff3/markdown_0/imgs/img_in_image_box_103_292_868_805.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A51%3A14Z%2F-1%2F%2F41fb8d29e7a0a862b8b82b2c29d04d2fd110df12d7942bf6c2ada58d5c75125c" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 13: CENELEC V-Cycle</div>


The first part of the original objectives stated in the grant agreement "analysis of the impact of the system pillar inputs" was not feasible due to a lack of the inputs regarding the concepts and the operational context. But the missing inputs were substituted from other sources as stated in 9.2. The results of this task can conversely serve as input for the ongoing discussion in the system pillar.

Due to limited time and resources, the authors decided to focus on system hazards, by analyzing the control interactions between the moving block system and the systems with which it interfaces directly. The chosen method is explained and exemplified in chapter 5.

We expect that the results can be utilized to update the system concepts, the system definition as well as the operational context and then further the system specification for the continuing innovation pillar work on the Moving Block Demonstrator. Some of the results can also be exported adjacent work packages, like WP27 where the Digital Register is being specified, or to the demonstrator work packages WP44/45 where operational concepts, and an operator console/workbench will come into play.

Even though a proof of completeness with respect to functional safety is not in part of this task, we were able to show that we cover the whole set of results from X2Rail safety work in chapter 7.

### 9.4 Discussion of Main Results

An advantage of the chosen approach was that it allowed to connect the beforehand stated assumptions with the relevant loss scenarios they affect. Some of the used assumptions were well established (e.g., the SIL classification of the OBU, OCs), while others were relatively novel (e.g.,

---

not requiring TTDs for detection of train presence). The safety analysis therefore provided an opportunity to validate or - if necessary - update these assumptions.

For example, under the assumption that TTDs are not required ([ASM-4]), we generated loss scenarios for the relevant unsafe control actions to see if the hazard could still be prevented. This is closely connected to two further assumptions about MBS:

1. Up to date knowledge of all (potential) train positions on the tracks

2. Ability to constrain all train movement within a known area (i.e., movement authority)

The respective set of loss scenarios (concerning runaway wagons, loss of communication, parking vehicles and so on) led to the specific design recommendations [SDR-13], [SDR-16] & [SDR-18]. The summary of those in turn leads to the conclusion, that the assumption that TTDs can completely be eliminated while still guarding against all loss scenarios found in our analysis is too strong. In short, if uncontrolled train movement cannot be eliminated, their presence is still required. Henceforth, [ASM-4] was updated to [ASM-4-v2] "MBS does not require TTDs for controlled train movement but supports them for migration purposes or systems where the chance of uncontrolled movement cannot be sufficiently controlled by other means."

A second class of assumptions is concerned with the correspondence between reported data and physical reality. This includes assumptions about the reported train length ([ASM-8]) as well as the geographical position of infrastructure elements like points, tracks, etc. ([ASM-26]). For train length, partial validation is possible in the case of splitting or joining trains. However, the validation alone may not be sufficient to achieve the desired level of confidence required for a SIL 4 function (e.g., if two trains enter the same TTD section and maneuvers like joining, splitting, or turning take place). Thus [SDR-11] states that "MBS shall always be aware when a change of train length is expected (i.e. due to splitting and joining)."

The correctness of information on the geographical position of infrastructure elements is even more critical for MBS. Some controller constraints depend on geometrical information (e.g. ensuring that there are no intersections between movement authorities, [Resp-MBS-1]) which need the required level of precision to ensure that no intersections are undetected. MBS lacks the information to validate the provided information by itself, but depends on it for SIL-4 functions. Thus, the corresponding assumption [ASM-26] has the rank of exported requirement, provided in a higher level of granularity through the design recommendations [SDR-18] to [SDR-24].

The third class of results concerns the control loops where a human actor is involved. Several design recommendations in section 8.4 concern the Operator Panel, its ability to display safety related information, to re-verify human entered values, to schedule safety related commands, or more general operational procedures that could be linked to respective loss scenarios in our analysis.

### 9.5 OPEN POINTS AND FUTURE WORK

Even though the major pain points were likely highlighted in this analysis, they are not yet verifiably settled or solved. In that regard, the design recommendations will have to be considered in the system definitions of MBS, DR and the Operator Panel - to be then re-checked/validated in a further

---

step of the safety analysis (e.g., protection against side-on collisions; domain data safety responsible entity).

Some of the assumptions defined at the beginning of the work packages simplified the analysis and might have to be re-opened in a later stage when extending the system scope (e.g., SIL of train length / train integrity information; handover to neighboring MBS- or legacy systems). Finally, there are some use-cases that were postponed to a later stage of the demonstrator (e.g., supervised shunting) that must be analyzed as soon as first concept drafts are available.

The results of the safety analysis review from D13.1 will be further developed and addressed within WP14. Regarding any form of proof of completeness, e.g., for a later certification will likely have to move to a possible second phase of the R2DATO project.

---

[1] Nancy G. Leveson, John P. Thomas; STPA Handbook; March 2018, STPA Handbook (MIT-STAMP-001)

[2] UNISIG, Subset 026, ERTMS/ETCS System requirements specification, Issue 4.0.0, July 2023

[3] CENELEC, EN 50126-1:2017, Railway Applications - The Specification and Demonstration of Reliability, Availability, Maintainability and Safety (RAMS) - Part 1: Generic RAMS Process

[4] CENELEC, EN 50126-2:2017, Railway Applications - The Specification and Demonstration of Reliability, Availability, Maintainability and Safety (RAMS) - Part 2: Systems Approach to Safety

[5] CENELEC, EN 50129:2018, Railway applications - Communication, signalling and processing systems - Safety related electronic systems for signalling

[6] System Pillar Common Business Objectives, Version 1, 25/07/2022, (https://rail-research.europa.eu/wp-content/uploads/2022/10/SP-Common-Business-Objectives.pdf)

[7] System Pillar Operational Visions, Version 1, 11/07/2022, (https://rail-research.europa.eu/wp-content/uploads/2022/10/SP-CCS-TMS-CMS-Operational-vision.pdf)

[8] Common Safety Method for Risk Evaluation and Assessment, CELEX (EU) No 402/2013 (https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A32013R0402), CELEX (EU) 2015/1136 (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L.2015.185.01.0006.01.ENG).

[9] X2Rail-1, https://projects.shift2rail.org/s2r ip2 n.aspx?p=X2RAIL-1

[10] X2Rail-3, https://projects.shift2rail.org/s2r ip2 n.aspx?p=X2RAIL-3

[11] X2Rail-5, https://projects.shift2rail.org/s2r ip2 n.aspx?p=X2RAIL-5

[12] RCA, https://ertms.be/activities/target-archi-ccs-architecture

[13] R2DATO WP13 Task 13.1 System Definition

[14] R2DATO WP13 Task 13.2 System Specification

[15] R2DATO WP44 Task 44.3 System Definition

[16] R2DATO WP44 Task 44.3 System Specification

[17] R2DATO WP13 Task 13.1 System Definition - Assumptions

[18] R2DATO_WP13_SystemDefinition_Assumptions.xlsx (Work Package internal File)

[19] UNISIG, Subset 023, ERTMS/ETCS Glossary of Terms and Abbreviations, Issue 4.0.0, July 2023

[20] ISO 16290:2013-Space systems — Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment