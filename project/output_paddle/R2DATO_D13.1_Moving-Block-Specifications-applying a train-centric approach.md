# Rail to Digital automated up to autonomous train operation

D13.1

## Moving Block Specifications applying a train-centric approach Introduction

Due date of deliverable: 31/08/2024

Actual submission date: 08/07/2025

Leader/Responsible of this Deliverable: ATSA

Reviewed: Y


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Document status</td></tr><tr><td style='text-align: center;'>Revision</td><td style='text-align: center;'>Date</td><td style='text-align: center;'>Description</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>14/10/2024</td><td style='text-align: center;'>Draft</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>15/10/2024</td><td style='text-align: center;'>Released after review</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>04/12/2024</td><td style='text-align: center;'>Updated after TMT review</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>17/06/2025</td><td style='text-align: center;'>This document now notes that comments from the JU review about the Safety Analysis will be handled as part of WP14.</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>08/07/2025</td><td style='text-align: center;'>Editorial</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Project funded from the European Union&#x27;s Horizon Europe research and innovation programme</td></tr><tr><td colspan="3">Dissemination Level</td></tr><tr><td style='text-align: center;'>PU</td><td style='text-align: center;'>Public</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>SEN</td><td style='text-align: center;'>Sensitive - limited under the conditions of the Grant Agreement</td><td style='text-align: center;'></td></tr></table>

---

Start date: 01/12/2022

Duration: 42 months

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1805d47f-c7d9-4df1-9421-54bcb36e4084/markdown_0/imgs/img_in_image_box_100_308_271_426.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A23%3A49Z%2F-1%2F%2F98160fafdefd51e194d8ab88830dd2e159d30a962ceec056262aa1526b477fd5" alt="Image" width="14%" /></div>


## ACKNOWLEDGEMENTS

This project has received funding from the Europe's Rail Joint Undertaking (ERJU) under the Grant Agreement no. 101102001. The JU receives support from the European Union's Horizon Europe research and innovation programme Rail JU members other than the Union.

and the Europe’s Rail JU members other than the Union.

## REPORT CONTRIBUTORS

For the report contributors please refer to the corresponding sections of the Deliverable.

## Disclaimer

The information in this document is provided "as is", and no guarantee or warranty is given that the information is fit for any particular purpose. The content of this document reflects only the author's view – the Joint Undertaking is not responsible for any use that may be made of the information it contains. The users use the information at their sole risk and liability.

---

## EXECUTIVE SUMMARY

This Deliverable contains an Architecture description, Requirements, and Hazard Analysis for an ETCS Moving Block System, in accordance with the GA Project 101102001 — FP2 - R2DATO and represents the collaborative WP approach of refining the System Pillar work e.g. CCS architecture and harmonized operational rules to derive a System Specification for a Moving Block System.

This document is a Deliverable from WP13 Moving Block ETCS Level 3 – Specification. The Deliverable consists of four parts. The first part is the introduction, the second part the result of the Task 13.1 - System Definition, the third the result of the Task 13.2 - System Specification and the fourth part the result of the Task 13.3, namely the Safety Analysis.

Work on this deliverable is actively progressing within WP14. As part of this effort, the Safety Analysis is being updated to address the outstanding comment raised by the external reviewer.

---

<div style="text-align: center;">ABBREVIATIONS AND ACRONYMS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">ABBREVIATIONS AND ACRONYMS</td></tr><tr><td style='text-align: center;'>ATO</td><td style='text-align: center;'>Automatic Train Operation</td></tr><tr><td style='text-align: center;'>CCS</td><td style='text-align: center;'>Control-Command and Signalling</td></tr><tr><td style='text-align: center;'>ETCS</td><td style='text-align: center;'>European Train Control System</td></tr><tr><td style='text-align: center;'>R2DATO</td><td style='text-align: center;'>Rail to Digital automated up to autonomous train operation</td></tr><tr><td style='text-align: center;'>S2R</td><td style='text-align: center;'>Shift2Rail</td></tr><tr><td style='text-align: center;'>STPA</td><td style='text-align: center;'>System Theoretic Process Analysis</td></tr><tr><td style='text-align: center;'>TTD</td><td style='text-align: center;'>Trackside Train Detection</td></tr><tr><td style='text-align: center;'>WP</td><td style='text-align: center;'>Work package</td></tr></table>

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


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Document status</td></tr><tr><td style='text-align: center;'>Revision</td><td style='text-align: center;'>Date</td><td style='text-align: center;'>Description</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>27/04/2023</td><td style='text-align: center;'>First issue</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>05/06/2023</td><td style='text-align: center;'>Incorporated review comments by WP13 Review Group</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>15/06/2023</td><td style='text-align: center;'>Version after consolidation of review comments in WP13</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>07/10/2024</td><td style='text-align: center;'>Incorporated review comments from WP27 (DR), WP44/45 (Demonstrator) and System Pillar. Aligned with release 3 of System Specification</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>02/12/2024</td><td style='text-align: center;'>Updated after review by TMT.</td></tr><tr><td style='text-align: center;'>06</td><td style='text-align: center;'>20/01/2025</td><td style='text-align: center;'>Names of authors and reviewers introduced</td></tr><tr><td style='text-align: center;'>07</td><td style='text-align: center;'>06/06/2025</td><td style='text-align: center;'>Incorporation of comments by ERA</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Project funded from the European Union&#x27;s Horizon Europe research and innovation programme</td></tr><tr><td colspan="3">Dissemination Level</td></tr><tr><td style='text-align: center;'>PU</td><td style='text-align: center;'>Public</td><td style='text-align: center;'>✗</td></tr><tr><td style='text-align: center;'>SEN</td><td style='text-align: center;'>Sensitive - limited under the conditions of the Grant Agreement</td><td style='text-align: center;'></td></tr></table>

---

Start date: 01/12/2022

Duration: 42 month

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1b56a7a2-5906-4e2c-8286-02f5a503338c/markdown_0/imgs/img_in_image_box_84_240_261_356.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A24%3A29Z%2F-1%2F%2Fa85b4dbe86542f77b372f896764bb80f777fa94e6947483f3bdcd13cce770d60" alt="Image" width="14%" /></div>


## ACKNOWLEDGEMENTS

This project has received funding from the Europe’s Rail Joint Undertaking (ERJU) under the Grant Agreement no. 101102001. The JU receives support from the European Union’s Horizon Europe research and innovation programme.

and the Europe’s Rail JU members other than the Union.

<div style="text-align: center;">REPORT CONTRIBUTORS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Company</td><td style='text-align: center;'>Details of Contribution</td></tr><tr><td style='text-align: center;'>Bertrand Badot, Staffan Pettersson</td><td style='text-align: center;'>ATSA</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Konstantinos Emmannouil, Martin Woiton</td><td style='text-align: center;'>DB</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Nader Nayeri, Thomas Naulin</td><td style='text-align: center;'>GTSD</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Manuel Schleiffelder</td><td style='text-align: center;'>OBB-Infra</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Bettina Morman</td><td style='text-align: center;'>SBB</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Alfonso Lorenzo</td><td style='text-align: center;'>ADIF (INECO)</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Daniel Kolar</td><td style='text-align: center;'>AZD</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Marta Garcia, Ivan Velado Martinez</td><td style='text-align: center;'>CAF</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Christian Sadowski, Gregor Kolokewitsch, Philipp Schneider, Frank Skowron</td><td style='text-align: center;'>DB</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Christian Loeffler</td><td style='text-align: center;'>GTSD</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Giuseppe Pagliarulo</td><td style='text-align: center;'>MERMEC</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Ulrich Schöni</td><td style='text-align: center;'>SBB</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Simon Chadwick</td><td style='text-align: center;'>SMO</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Adelaide Vitiello, Giacomo Donati</td><td style='text-align: center;'>STS</td><td style='text-align: center;'>Reviewer</td></tr></table>

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


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to Subset 023, [1].</td></tr><tr><td style='text-align: center;'>AoC</td><td style='text-align: center;'>Area of Control</td></tr><tr><td style='text-align: center;'>CR</td><td style='text-align: center;'>Change Request</td></tr><tr><td style='text-align: center;'>CCS</td><td style='text-align: center;'>Control, Command and Signalling</td></tr><tr><td style='text-align: center;'>DR</td><td style='text-align: center;'>Digital Register</td></tr><tr><td style='text-align: center;'>ERJU</td><td style='text-align: center;'>Europe&#x27;s Rail Joint Undertaking</td></tr><tr><td style='text-align: center;'>L2</td><td style='text-align: center;'>ETCS Level 2</td></tr><tr><td style='text-align: center;'>IXL</td><td style='text-align: center;'>Interlocking</td></tr><tr><td style='text-align: center;'>MBS</td><td style='text-align: center;'>Moving Block System</td></tr><tr><td style='text-align: center;'>OC</td><td style='text-align: center;'>Object Controller</td></tr><tr><td style='text-align: center;'>OP</td><td style='text-align: center;'>Operator Panel</td></tr><tr><td style='text-align: center;'>OPE</td><td style='text-align: center;'>Operation and Traffic Management</td></tr><tr><td style='text-align: center;'>PE</td><td style='text-align: center;'>Plan Execution</td></tr><tr><td style='text-align: center;'>R2DATO</td><td style='text-align: center;'>Rail to Digital automated up to autonomous train operation</td></tr><tr><td style='text-align: center;'>RCA</td><td style='text-align: center;'>Reference CCS Architecture</td></tr><tr><td style='text-align: center;'>S2R</td><td style='text-align: center;'>Shift2Rail</td></tr><tr><td style='text-align: center;'>TA</td><td style='text-align: center;'>Trackside Asset</td></tr><tr><td style='text-align: center;'>TACS</td><td style='text-align: center;'>Trackside Asset Control and Supervision</td></tr><tr><td style='text-align: center;'>TIMS</td><td style='text-align: center;'>Train Integrity Monitoring System</td></tr><tr><td style='text-align: center;'>TMS</td><td style='text-align: center;'>Traffic Management System</td></tr><tr><td style='text-align: center;'>TSI</td><td style='text-align: center;'>Technical Specifications for Interoperability</td></tr><tr><td style='text-align: center;'>TTD</td><td style='text-align: center;'>Trackside Train Detection</td></tr></table>

---

## WORK PACKAGE GLOSSARY

Note: Some of those terms are currently also defined in the Glossary of other documents (e.g., System Specification, Safety Analysis) of D13.1. Therefore, as long as there is no separate Glossary document available, care must be taken to keep the definitions synchronised.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Term</td><td style='text-align: center;'>Definition</td></tr><tr><td style='text-align: center;'>Area of Control</td><td style='text-align: center;'>The Area of Control is the topologically limited extent and the infrastructural Trackside Assets in this geographical extent. The term is used here for defining the technical and operational responsibility of one MBS.</td></tr><tr><td style='text-align: center;'>Domain Data</td><td style='text-align: center;'>The Domain Data refers to use case specific configuration data for the MBS to define the specific application. These can be broadly classified as Map Data, Segment Profiles, and Parameter Data. As a part of configuration process, the MBS needs Domain Data. Potential updates of Domain Data will be realised by a centralised provisioning process incl. synchronous activation of the new data version.</td></tr><tr><td style='text-align: center;'>Operational Plan</td><td style='text-align: center;'>The Operational Plan is the result of the planning process performed by the planning system (TMS). It describes either a planned Operational Movement, Operational Restriction or Operational Warning Measure through a temporal sequence of Operational Events to be implemented by underlying subsystems in the Area of Control.</td></tr><tr><td style='text-align: center;'>Operational State</td><td style='text-align: center;'>The Operational State consists of train-related information (e.g., permissions, authorisations or train position) and track-related information (e.g., state of Trackside Assets).</td></tr><tr><td style='text-align: center;'>System Capability</td><td style='text-align: center;'>A System Capability is a service an actor requires from the system to fulfil its business goals. System capabilities are realised by exploiting one or multiple functions, usually in a chain of functions. System capabilities in terms of this document are very similar to use cases and the theory behind it.</td></tr><tr><td style='text-align: center;'>Train-centric</td><td style='text-align: center;'>A train-centric approach from a trackside point of view focuses on the train as the true business object. A train object is derived by a train-centric signalling system using the currently available sensor information from the train and the trackside. This allows the safety logic of train-centric signalling system to operate on the train objects instead on the auxiliary information ‘occupancy’ only as today in conventional block-centric signalling systems.</td></tr><tr><td style='text-align: center;'>Trackside Asset</td><td style='text-align: center;'>Trackside Assets are elements on or near the track which are used to monitor (using sensors) and/or control (using actuators) the movement of vehicles through the railway network. to provide a safe route through the railway network. They can be switchable or non-switchable and are controlled by the actors Trackside Asset Control and Supervision.</td></tr></table>

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

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fc52b607-bb68-4aa3-84ad-d5d97d8de1de/markdown_0/imgs/img_in_image_box_102_544_1170_1565.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A25%3A10Z%2F-1%2F%2F1cb33e4bd46667b1891bca874b04d4afb7cd0ba838b0727728e9f835ceef1b79" alt="Image" width="89%" /></div>


<div style="text-align: center;">Figure 1: System Boundaries</div>

---

### 3.1 INTERFACES AND INTERACTIONS WITH OTHER TECHNOLOGICAL SYSTEM

This chapter defines the interfaces and interactions between the MBS and other technological systems. For each technological system a description, the cardinality (from one MBS instance) and the applicable standard (if any) to be used for the corresponding interface is provided.

#### 3.1.1 Adjacent System


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Adjacent System</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>An Adjacent System can be either radio-based ETCS related neighbouring system or a neighbouring system not related to radio-based ETCS.A radio-based ETCS related neighbouring system can be either another MBS or a neighbouring Radio Block Centre (RBC) and an IXL. The interface to such a neighbouring system allows trains to pass the border to/from a neighbouring Level 2 area without changing the driver responsibility and the cab-signalling.A neighbouring system not related to radio based ETCS is an IXL. The interface to such a neighbouring system allows trains to pass the border to/from an area not equipped with Level 2. The cab-signalling is replaced by optical signals.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>n</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>The interface to a radio-based ETCS related neighbouring system is based on the existing ETCS specifications [1], namely Subset-039 and Subset-098.For the interface to a neighbouring IXL system it is recommended, but not mandatory, to use the SCI-ILS interface as published in EULYNX [2].Notes:- Interfaces to neighbouring IXL systems depend on the supported interface capabilities of the IXL and have to be adapted, e.g., by using adapter solutions.- An interface to an adjacent MBS may also require enhancements to the existing ETCS specifications.</td></tr></table>

<div style="text-align: center;">3.1.2 Diagnostics System</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Diagnostics System</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>Diagnostics is, as in any system, a fundamental feature.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>For the target architecture this interface may base on the SDI interface specification published in EULYNX [2]. This will be finally defined by the System Pillar.</td></tr></table>

#### 3.1.3 Digital Register


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Digital Register</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Digital Register (DR) provides reliable (meaning complete, accurate, current, and consistent, verified and validated), interoperable and accessible infrastructure information as a critical enabler for safety-related and non-safety-related functions. The Digital Register includes static infrastructure information (static speed profile, gradients, cant, etc.) and configuration data, which are approved after engineering process. The interface between the DR and the MBS is used to update the data in the MBS.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>The interface between the DR and the MBS is not standardised yet. It will be defined in coordination with WP27 considering both the data model and the handling of parameter/configuration data as defined by System Pillar Domain TCCS (SD1, SD3).</td></tr></table>

#### 3.1.4 ETCS on-board


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>ETCS on-board</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The ERTMS/ETCS on-board (OBU) equipment is a computer-based system that supervises the movement of the train to which it belongs, on basis of information exchanged with the MBS.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>n</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>The interface to the OBU is based on existing ETCS specifications [1], namely Subset-026, Subset-037.</td></tr></table>

#### 3.1.5 Operator Panel


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Operator Panel</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Operator Panel is used to perform manual interaction with MBS.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>The interface between the Operator Panel and the MBS is not standardised yet. It will be defined considering the principles described in RCA and the work of X2Rail-5 Moving Block WP.</td></tr></table>

#### 3.1.6 Plan Execution


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Plan Execution</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Plan Execution (PE) requests the setting of field elements and the submission of authorisation for train movements e.g., according to Operational Plan from TMS (TMS is out of scope).The MBS provides the Operational State to the PE.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>The interface between the PE and the MBS is not standardised yet. It will be defined considering the principles described in RCA and the work of X2Rail-5 Moving Block WP.</td></tr></table>

<div style="text-align: center;">3.1.7 Security Service</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Security Service</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Security Service summarises all technological systems that are necessary to manage and provide the cryptographic artefacts (e.g., keys or certificates) to ensure the confidentiality, authenticity and integrity (Information Security Triad) of the communication between  - the MBS and the OBUs and  - the MBS and an Adjacent System either being a neighbouring RBC/IXL or  - another MBS and  - The MBS and the Trackside Assets.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>Notes:  - This list is not exhaustive. In future there may be other interfaces which require securing the communication using cryptographic artefacts from the Security Service.  - For some interfaces only, a subset of the Information Security Triad is applied, e.g., for the communication between MBS and the OBUs it is only necessary to ensure the authenticity and integrity.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>For managing the authentication keys between MBS and OBUs, neighbouring RBC or another MBS, the interface to the Security Service is based on the existing ETCS specifications [1], namely Subset-114, Subset-137 and Subset-146. For managing the cryptographic artefacts between MBS and the Trackside Assets, the SSI interface specification as published in EULYNX [2] may be used. This will be finally defined by the System Pillar.</td></tr></table>

#### 3.1.8 Trackside Asset Control and Supervision


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Trackside Asset Control and Supervision</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Trackside Asset Control and Supervision (TACS) reports the state of the Trackside Assets (TAs). The MBS mainly uses this interface to trigger setting the state of a TA, e.g., moving a point, and to receive status information from TAs (e.g., occupancy information from TTD). The interface also includes safety relevant maintenance issues, e.g., resetting an axle counter.</td></tr><tr><td style='text-align: center;'>Cardinality</td><td style='text-align: center;'>n</td></tr><tr><td style='text-align: center;'>Interface</td><td style='text-align: center;'>For the target architecture this interface bases on the specification published in EULYNX [2]. For migration phase other interfaces, even proprietary ones, are possible.</td></tr></table>

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


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">This chapter contains assumptions related to external systems or actors interacting with the Moving Block System (MBS) or related to input from external systems that are not covered somewhere else yet (e.g., in the corresponding standard).</td></tr><tr><td style='text-align: center;'>Identifier</td><td style='text-align: center;'>Allocation</td><td style='text-align: center;'>Assumption</td></tr><tr><td style='text-align: center;'>G1</td><td style='text-align: center;'>General</td><td style='text-align: center;'>Virtual Coupling is out of scope.Justification: Virtual Coupling is not part of the Grant Agreement of WP13.</td></tr><tr><td style='text-align: center;'>T1</td><td style='text-align: center;'>Train</td><td style='text-align: center;'>If a train is equipped with a TIMS and this trains confirms its train integrity, then the MBS can trust the train for:- Train Length - Received in Validated Train Data as L_TRAIN, which is the maximum length of the train in rear of the engine, counted from the front end of the engine considering the active cab, and considering the coupling play and/or any other uncertainties in the length information.- Train Position Reports - including Q_LENGTH, L_TRAININTThis is consistent with the approach in the ETCS Specifications [1]:- On-Board can only confirm Train Integrity to Trackside if the train length can be treated as SIL4.Justification: This means that the train length and information from the train position reports (e.g., train integrity information) can be used by the MBS to release track behind the train, and for length calculations during splitting and joining.Note: This implies that the MBS won&#x27;t trust the train for the Train Length if the train has never confirmed its train integrity (e.g. because the train is not equipped with a TIMS)</td></tr><tr><td style='text-align: center;'>T2</td><td style='text-align: center;'>Train</td><td style='text-align: center;'>In case of joining or splitting of trains, this causes the external Train Integrity Monitoring System (TIMS) devices (in each train) to report loss of train integrity.As long as MBS has not acknowledged the new train data (incl. train length), the train integrity is not confirmed again by the train(s).Justification: The safe train length is not valid anymore when trains physically join or split.</td></tr></table>

<div style="text-align: center;">Table 2: Assumptions</div>

---

### 6.2 EXISTING SAFETY MEASURES

The MBS is based on ETCS and hence all safety measures required by the ETCS Specifications $ ^{[1]} $  are applied also for MBS.

---

## 7 CONCLUSIONS

The aim of this document is to define the System Definition of the Moving Block System (MBS).

To achieve this, the document has provided the objective of the Moving Block System (MBS).

Hereby, the document focuses on the description of the capabilities, the boundaries (incl. a brief description of the interfaces to other technological systems) and the system functions. Additionally, the scope of operational requirements influencing the system have been elaborated. Further on, this document also lists the necessary assumptions for the Moving Block System.

---

[1] ETCS Specifications

Annex A for the TSI CCS according

Commission Implementing Regulation (EU) 2023/1695

of 10 August 2023

Set of Specifications( ETCS B4 R1, RMR GSM-R B1 MR1 + FRMCS B0, ATO B1 R1 )

System Version 2.1

[2] EuLynx

Baseline Set 4 Release 2

https://rail-research.europa.eu/system_pillar/system-pillar-outputs/trackside-assets-specifications/

[3] RCA

RCA Baseline 1 Release 0

https://public.3.basecamp.com/p/KeehzqFmXv5R2N7tGDjaEokq





[4] S2R

Moving Block Specification Release

https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5f58a710a&appId=PPGMS

[5] Operation and Traffic Management TSI Under regulation 2019/773

https://www.era.europa.eu/domains/technical-specifications-interoperability/operation-and-traffic-management-tsi_en

[6] D13.1 - Moving Block Specifications applying a train-centric approach Part 2 - System Specification

---

# Rail to Digital automated up to autonomous train operation

# D13.1 – Moving Block Specifications applying a train-centric approach

## Part 2 - System Specification (Release 3)

Due date of deliverable: 31/10/2024

Actual submission date: 07/07/2025

Leader/Responsible of this Deliverable: Bertrand Badot, ATSA

Reviewed: Y


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Document status</td></tr><tr><td style='text-align: center;'>Revision</td><td style='text-align: center;'>Date</td><td style='text-align: center;'>Description</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>17/07/2023</td><td style='text-align: center;'>First issueChapter 8 to 10 are still draft (not to be reviewed)</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>03/10/2023</td><td style='text-align: center;'>Second issue for Release 1Comments on first issue answeredChapters 8 to 10 completed and available for review</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>31/01/2024</td><td style='text-align: center;'>First issue for Release 2Comments on document revision 2 answered</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>16/04/2024</td><td style='text-align: center;'>Last issue for Release 2 with answers to the Reviewer&#x27;s comments.Scope of work for Release 3 anticipated in chapter 2</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>05/06/2024</td><td style='text-align: center;'>First intermediate issue for Release 3.Chapter 6.11 Functional requirements for flank protection (Risk Path) is work in progress and should not be reviewed.</td></tr><tr><td style='text-align: center;'>06</td><td style='text-align: center;'>08/08/2024</td><td style='text-align: center;'>Second issue for Release 3.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>Update according to comments received on Revision 05.Chapter 5.10 and 6.11 updated for Flank Protection.Flank protection is now ready for review.Chapter 5.15 and related functions revisited for cooperative MP request.</td></tr><tr><td style='text-align: center;'>07</td><td style='text-align: center;'>15/10/2024</td><td style='text-align: center;'>Last issue for Release 3 with answers to the Reviewer&#x27;s comments.</td></tr><tr><td style='text-align: center;'>08</td><td style='text-align: center;'>05/12/2024</td><td style='text-align: center;'>Updated according to TMT review.</td></tr><tr><td style='text-align: center;'>09</td><td style='text-align: center;'>20/01/2025</td><td style='text-align: center;'>Names of authors and reviewers introduced</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>07/07/2025</td><td style='text-align: center;'>Update according to Review Sheet consolidated D13.1 (ERA + external reviewers)</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Project funded from the European Union&#x27;s Horizon Europe research and innovation programme</td></tr><tr><td colspan="3">Dissemination Level</td></tr><tr><td style='text-align: center;'>PU</td><td style='text-align: center;'>Public</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>SEN</td><td style='text-align: center;'>Sensitiv - limited under the conditions of the Grant Agreement</td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9faf5e28-d7c8-44b9-bae8-429ea5a52f47/markdown_0/imgs/img_in_image_box_84_201_264_320.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A26%3A12Z%2F-1%2F%2F4bb89c8be1ad0610266d6346f253fb1657fd7d9f8d3b34f9b70ce7c2e8d1aa86" alt="Image" width="15%" /></div>


## ACKNOWLEDGEMENTS

This project has received funding from the Europe’s Rail Joint Undertaking (ERJU) under the Grant Agreement no. 101102001. The JU receives support from the European Union’s Horizon Europe research and innovation programme and the Europe’s Rail JU members other than the Union.

## REPORT CONTRIBUTORS


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Company</td><td style='text-align: center;'>Details of Contribution</td></tr><tr><td style='text-align: center;'>Bertrand Badot, Staffan Pettersson</td><td style='text-align: center;'>ATSA</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Frank Skowron</td><td style='text-align: center;'>DB</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Nader Nayeri, Thomas Naulin</td><td style='text-align: center;'>GTSD</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Stephan Bischoff, Bettina Morman</td><td style='text-align: center;'>SBB</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Lucia Blanco</td><td style='text-align: center;'>ADIF (INECO)</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Daniel Kolar</td><td style='text-align: center;'>AZD</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Eivind Lenschow</td><td style='text-align: center;'>Bane NOR</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Ivan Velado Martinez, Marta Garcia</td><td style='text-align: center;'>CAF</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Martin Woiton, Konstantinos Emmannouil, Petra Hubrig, Christian Sadowski</td><td style='text-align: center;'>DB</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Andreas Distler</td><td style='text-align: center;'>DLR</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Felix Schaber, Gerhard Wipplinger, Andrej Kiriviga</td><td style='text-align: center;'>GTSD</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Giuseppe Pagliarulo</td><td style='text-align: center;'>MERMEC</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Manuel Schleiffelder, Hubert König, Salome Christiani</td><td style='text-align: center;'>OBB-Infra</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Simon Chadwick, Craig McLellan</td><td style='text-align: center;'>SMO</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Adelaide Vitiello</td><td style='text-align: center;'>STS</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Anders Lindfelt</td><td style='text-align: center;'>TRV (KTH)</td><td style='text-align: center;'>Reviewer</td></tr></table>

---

The information in this document is provided "as is", and no guarantee or warranty is given that the information is fit for any particular purpose. The content of this document reflects only the author's view – the Joint Undertaking is not responsible for any use that may be made of the information it contains. The users use the information at their sole risk and liability.

## Disclaimer

---

## EXECUTIVE SUMMARY

This document specifies the signalling system, called Moving Block System, in particular the system capabilities, functions, interfaces, and the specific domain objects.

This document contains the System Specification for a train-centric signalling system providing high capacity with low cost and high reliability, enabling moving block operation.

This document is part of the Moving Block System specification deliverable.

---

## ABBREVIATIONS AND ACRONYMS

For abbreviations and acronyms used in the ERTMS/ETCS specifications, please refer to /ETCS/SUBSET-023 and SUBSET-026 chapter 7 for ETCS variables.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>AoC</td><td style='text-align: center;'>Area of Control</td></tr><tr><td style='text-align: center;'>CCS</td><td style='text-align: center;'>Control, Command and Signalling</td></tr><tr><td style='text-align: center;'>DPS</td><td style='text-align: center;'>Drive Protection Section</td></tr><tr><td style='text-align: center;'>DPSG</td><td style='text-align: center;'>Drive Protection Section Group</td></tr><tr><td style='text-align: center;'>DR</td><td style='text-align: center;'>Digital Register</td></tr><tr><td style='text-align: center;'>ERJU</td><td style='text-align: center;'>Europe&#x27;s Rail Joint Undertaking</td></tr><tr><td style='text-align: center;'>MBS</td><td style='text-align: center;'>Moving Block System</td></tr><tr><td style='text-align: center;'>MP</td><td style='text-align: center;'>Movement Permission</td></tr><tr><td style='text-align: center;'>mSFE</td><td style='text-align: center;'>Min(imum) Safe Front End</td></tr><tr><td style='text-align: center;'>MSFE</td><td style='text-align: center;'>Max(imum) Safe Front End</td></tr><tr><td style='text-align: center;'>mSRE</td><td style='text-align: center;'>Min(imum) Safe Rear End</td></tr><tr><td style='text-align: center;'>MSRE</td><td style='text-align: center;'>Max(imum) Safe Rear End</td></tr><tr><td style='text-align: center;'>PE</td><td style='text-align: center;'>Plan Execution</td></tr><tr><td style='text-align: center;'>R2DATO</td><td style='text-align: center;'>Rail to Digital automated up to autonomous train operation</td></tr><tr><td style='text-align: center;'>RB</td><td style='text-align: center;'>Risk Buffer</td></tr><tr><td style='text-align: center;'>RCA</td><td style='text-align: center;'>Reference CCS Architecture</td></tr><tr><td style='text-align: center;'>RP</td><td style='text-align: center;'>Risk Path</td></tr><tr><td style='text-align: center;'>SCI</td><td style='text-align: center;'>Standard Communication Interface (EULYNX)</td></tr><tr><td style='text-align: center;'>SCI-CMD</td><td style='text-align: center;'>Standard Communication Interface - Command</td></tr><tr><td style='text-align: center;'>SCI-P</td><td style='text-align: center;'>Standard Communication Interface - Point</td></tr><tr><td style='text-align: center;'>SCI-TDS</td><td style='text-align: center;'>Standard Communication Interface - Train Detection System</td></tr><tr><td style='text-align: center;'>S2R</td><td style='text-align: center;'>Shift2Rail</td></tr><tr><td style='text-align: center;'>TA</td><td style='text-align: center;'>Trackside Asset</td></tr><tr><td style='text-align: center;'>TACS</td><td style='text-align: center;'>Trackside Asset Control and Supervision</td></tr><tr><td style='text-align: center;'>TCCS</td><td style='text-align: center;'>Transversal CCS (Control Command and Signalling)</td></tr><tr><td style='text-align: center;'>TDS</td><td style='text-align: center;'>Train Detection System</td></tr><tr><td style='text-align: center;'>TEP</td><td style='text-align: center;'>Track Edge Point</td></tr><tr><td style='text-align: center;'>TES</td><td style='text-align: center;'>Track Edge Section</td></tr><tr><td style='text-align: center;'>TIMS</td><td style='text-align: center;'>Train Integrity Monitoring System</td></tr></table>

---

TO Train Object  

TTD Trackside Train Detection



UTO Unresolved Trackbound Object

---

GLOSSARY

Note: Some of those terms are currently also defined in the Glossary of other documents (e.g., System Definition, Safety Analysis) of WP13. Therefore, as long as there is no separate Glossary document available, care must be taken to keep the definitions synchronised.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Term</td><td style='text-align: center;'>Definition</td></tr><tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>Allocation Sections express gauge clearance conflicts between different tracks.For example, Allocation Sections are associated to the representation of switchable Track Assets and further track connections like diamond crossings.The Allocation Sections are used in terms of granting a Movement Permission request as condition for clearance in a certain area.See also /FlankProtection/</td></tr><tr><td style='text-align: center;'>Area of Control (AoC)</td><td style='text-align: center;'>The Area of Control is the topologically limited extent used here for defining the technical and operational responsibility of one instance of MBS.</td></tr><tr><td style='text-align: center;'>Domain Data</td><td style='text-align: center;'>The Domain Data refers to use case specific configuration data for the MBS to define the specific application. These can be broadly classified as Map Data, Segment Profiles, and Parameter Data. As a part of configuration process, the MBS needs Domain Data. Potential updates of Domain Data will be realised by a centralised provisioning process incl. synchronous activation of the new data version.Source: /SD1DM/</td></tr><tr><td style='text-align: center;'>Domain Object</td><td style='text-align: center;'>A Domain Object is an abstract object for which a Domain (e.g. Moving Block System) has the main responsibility. There might be other Domains who are consumers of this object as well. In general, it is based on or linked to the Domain Data.</td></tr><tr><td style='text-align: center;'>Drive Protection Section (DPS)</td><td style='text-align: center;'>A Drive Protection Section is a linear contiguous stretch of track with a driveability (passage possible yes/no) state.A Drive Protection Section (DPS) represents a Track Edge Section that can be brought to different driveability states to ensure the driveability or safety of a track route. As such, it is an abstraction for any location on the railway network that may adopt different states due to Switchable Trackside Asset (e.g. points or level crossings).Source: RCA</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>MBS Operational State</td><td style='text-align: center;'>MBS Operational State is the collection of all of Domain Objects instantiated by the MBS to manage its operations and supervise the train movements.This includes:  · Train Objects,  · Unresolved Trackbound Objects,  · Trackside Asset Objects,  · Movement Permission,  · Etc...</td></tr><tr><td style='text-align: center;'>MBS is operational</td><td style='text-align: center;'>MBS is operational when it is in a state allowing the MBS to perform its fundamental function ensuring safe train movement and preventing railway accidents, incidents... From now on, communication sessions to the external systems (e.g., OBU, PE, etc.) can be established and supervised.</td></tr><tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'>The Movement Permission defines the part of the track that is reserved for the movement of a train.It includes:- Movement Permission Extent- Risk Buffer- Risk Path- Requested Maximum Speed- ETCS Movement Mode- List of DPS Groups that must not be used as flank protection measure</td></tr><tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>A Movement Permission Extent is a linear contiguous stretch of track that is reserved for the movement of a train. The Movement Permission is translated to an authorisation (e.g. Movement Authority) according to the /ETCS/ - SUBSET-026 that is transmitted to the train.The Movement Permission Extent is part of the Movement Permission.Source: RCA</td></tr><tr><td style='text-align: center;'>Non-switchable Trackside Asset</td><td style='text-align: center;'>A Non-switchable Trackside Asset is a Trackside Asset which provides information to the MBS (e.g. Trackside Train Detection) but cannot be controlled to a particular state.</td></tr><tr><td style='text-align: center;'>Position is ambiguous</td><td style='text-align: center;'>The position information contained in a Train Position Report (Position Report or SoM Position Report with status valid) can be considered as ambiguous in case MBS is not able to safely locate the train within the track layout. Since the Train Position Report only contains a (directed) distance to the LRBG, MBS might not be able to locate the train on the correct position in the track layout, e.g. in case of a zig-zag movement</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>(see Hazard 0003 in /ETCS/ - SUBSET-113) or when there is a facing pair of points between the LRBG and the position of the train.</td></tr><tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The Risk Buffer is a linear contiguous stretch of track that serves as the overrun protection and in the event of a rollback of a chased train. It is part of a Movement Permission.A Risk Buffer exists if there is a Danger Point or a safe margin (project specific) greater than zero.Source: RCA</td></tr><tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>A Risk Path is one potential path (a linear contiguous stretch of track) by which a non-permitted vehicle movement could result in a flank collision with a vehicle moving along the Movement Permission Extent.A Movement Permission can contain zero or more Risk Paths.Source: RCA</td></tr><tr><td style='text-align: center;'>Switchable Trackside Asset</td><td style='text-align: center;'>A Switchable Trackside Asset is a Trackside Asset which enables (e.g. points, derailers, movable bridges, gates) or allows (e.g. light signals at border, level crossings) the continuation of movement beyond this asset when this latter is controlled to particular state.</td></tr><tr><td style='text-align: center;'>Topology Data</td><td style='text-align: center;'>See entry for Domain Data</td></tr><tr><td style='text-align: center;'>Track Edge (TE)</td><td style='text-align: center;'>Track Edge is a linear object that defines an uninterrupted stretch of a railway track without divergence or convergence. A Track Edge is defined along the centre line of the 2D or 3D track alignment and has a finite length.The Track Edges have an implicit direction (from start to end).The start/end of Track Edge shall correspond to the location of a simple point, or any form of end of track.Source: RCA, /SD1DM/</td></tr><tr><td style='text-align: center;'>Track Edge Point (TEP)</td><td style='text-align: center;'>A Track Edge Point is a spot location on a Track Edge.Example usage: balise locationSource: RCA, /SD1DM/</td></tr><tr><td style='text-align: center;'>Track Edge Section (TES)</td><td style='text-align: center;'>A Track Edge Section is a linear extent between two Track Edge Points on (the same) Track Edge and can be directed.Example usage: Track properties like gradient, SSP, DPSSource: RCA, /SD1DM/</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Trackside Asset (TA)</td><td style='text-align: center;'>Trackside Assets are elements on or near the track which are used to monitor (using sensors) and/or control (using actuators) the movement of vehicles through the railway network. They can be switchable or non-switchable and are controlled by the actors Trackside Asset Control and Supervision (TACS). See also Switchable Trackside Asset and Non-switchable Trackside Asset definition.</td></tr><tr><td style='text-align: center;'>Trackside Asset Control and Supervision (TACS)</td><td style='text-align: center;'>The Trackside Asset Control and Supervision (TACS) is a subsystem supervising and controlling Trackside Assets.</td></tr><tr><td style='text-align: center;'>Trackside Train Detection (Section)</td><td style='text-align: center;'>Trackside Train Detection is a system which determines the occupancy status of TTD sections. TTD section may be a Track Circuit or an Axle Counting system. EULYNX synonym: Track Vacancy Proving Section (TVPS)</td></tr><tr><td style='text-align: center;'>Train Location</td><td style='text-align: center;'>Train Location is the MBS interpretation of the unambiguous location of the train, based on Train Position Reports, Validated Train Data and other inputs if available, e.g. TTD. Train Location is a linear contiguous stretch of track that has a front and a rear. X2R5 source: Train Location RCA source: rMOB extent</td></tr><tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>Train Object is the object needed by the MBS to manage the connected trains currently performing their mission. Note: This Train Object could nevertheless correspond to a train not (yet) localised by MBS. If a Train Object is referenced as a geometric extent, the extent is the extent of the Train Location. RCA source: (rMOB)</td></tr><tr><td style='text-align: center;'>Train Position Report</td><td style='text-align: center;'>The term Train Position Report refers to either Position Report packet (packet number 0) or Position Report based on two balise groups packet (packet number 1) according to /ETCS/ - SUBSET-026, chapter 7.</td></tr><tr><td style='text-align: center;'>Unresolved Trackbound Object</td><td style='text-align: center;'>Unresolved Trackbound Object is the object needed by the MBS to manage a contiguous track area where track vacancy is not proven and cannot be linked to any connected train (Train Object). RCA source: uMOB X2R5 source: Unknown Track Status Area (partly)</td></tr></table>

---

## TABLE OF CONTENTS

Acknowledgements.....3  
Report Contributors.....3  
Executive Summary.....5  
Abbreviations and Acronyms.....6  
Glossary.....8  
Table of Contents.....12  
List of Figures.....18  
List of Tables.....19  
1 Introduction.....20  
2 Scope of work.....21  
2.1 General limitations.....22  
3 Approach and methodology.....23  
4 MBS Overview.....25  
5 System Capabilities Specification.....26  
5.1 SysC: Start and Maintain MBS.....27  
5.1.1 Communication patterns.....27  
5.1.2 Capability.....31  
5.1.3 Scenario: Start and Maintain MBS.....32  
5.2 SysC: Preload Topology Data.....33  
5.2.1 Scenario: Preload Topology Data.....34  
5.3 SysC: Approve Topology Data activation.....34  
5.4 SysC: Activate Topology Data.....35  
5.5 SysC: Respond to initiation of communication session by PE.....36  
5.5.1 Scenario: Respond to initiation of communication session by PE.....37  
5.6 SysC: Start communication with one TACS.....37  
5.6.1 Scenario: Start communication session with a TACS.....38  
5.7 SysC: Respond to initiation of communication session by OBU.....38  
5.7.1 Scenario: Start communication session with an OBU.....40  
5.8 SysC: Control Switchable Trackside Assets.....40  
5.8.1 Scenario: Control Switchable Trackside Assets.....41  
5.9 SysC: Shutdown MBS.....42  
5.10 SysC: Update MBS Operational State.....42  
5.10.1 Scenario 1: Update MBS Operational state when TA state report is received.....43  
5.10.2 Scenario 2: Update MBS Operational State when a train position report or validated train data are received.....44

---

5.10.3 Scenario 3: Update MBS Operational State when no communication with TACS anymore ..... 45  
5.10.4 Scenario 4: Update MBS Operational State when no communication with OBU anymore ..... 46  
5.11 SysC: Report MBS Operational State ..... 47  
5.11.1 Scenario: Report of MBS Operational State when triggered ..... 48  
5.12 SysC: Start of Train ..... 48  
5.12.1 Scenario: Start of Train ..... 49  
5.13 SysC: Provide MA to Train ..... 50  
5.13.1 Scenario: Provide MA to Train ..... 51  
5.14 SysC: Terminate Train Mission ..... 51  
5.14.1 Scenario 1: Train End of Mission ..... 52  
5.14.2 Scenario 2: Termination of communication session by OBU ..... 53  
5.14.3 Scenario 3: end mission when no communication anymore with an OBU ..... 54  
5.15 SysC: Revoke MA cooperatively by PE ..... 55  
5.15.1 Scenario: Revoke MA cooperatively by PE ..... 55  
6 System Function specifications ..... 57  
6.1 SysF Report MBS Operational State ..... 58  
6.1.1 Overview ..... 58  
6.1.2 Inputs ..... 58  
6.1.3 Outputs ..... 58  
6.1.4 Functional requirements ..... 59  
6.2 SysF Authorise TA State Request ..... 59  
6.2.1 Overview ..... 59  
6.2.2 Input ..... 59  
6.2.3 Outputs ..... 59  
6.2.4 Functional requirements ..... 60  
6.3 SysF Translate TA State request to TACS command ..... 65  
6.3.1 Overview ..... 65  
6.3.2 Inputs ..... 66  
6.3.3 Outputs ..... 66  
6.3.4 Functional requirements ..... 66  
6.4 SysF Send TACS command ..... 66  
6.4.1 Overview ..... 66  
6.4.2 Inputs ..... 66  
6.4.3 Outputs ..... 66  
6.4.4 Functional requirements ..... 67

---

6.5 SysF Update Domain Object state ..... 67  
6.5.1 Overview ..... 67  
6.5.2 Input ..... 67  
6.5.3 Output ..... 67  
6.5.4 Functional requirements ..... 68  
6.6 SysF Preload Topology Data ..... 70  
6.6.1 Overview ..... 70  
6.6.2 Input ..... 70  
6.6.3 Output ..... 70  
6.6.4 Functional requirements ..... 71  
6.7 SysF Assign a safe value to a Domain Object ..... 72  
6.7.1 Overview ..... 72  
6.7.2 Inputs ..... 72  
6.7.3 Outputs ..... 72  
6.7.4 Functional requirements ..... 72  
6.8 SysF Create Train Object ..... 73  
6.8.1 Overview ..... 73  
6.8.2 Inputs ..... 74  
6.8.3 Outputs ..... 74  
6.8.4 Functional requirements ..... 74  
6.9 SysF Localise Train ..... 75  
6.9.1 Overview ..... 75  
6.9.2 Inputs ..... 76  
6.9.3 Outputs ..... 76  
6.9.4 General Train Location Requirements ..... 77  
6.9.5 Requirements to create a Train Location ..... 77  
6.9.6 Requirements to update a Train Location ..... 79  
6.9.7 Reaction to Unexpected Train Locations – FOR FURTHER RELEASE ..... 85  
6.9.8 Impact from TTD on Train Locations ..... 86  
6.9.9 Requirements to delete Train Location and to create Unresolved Trackbound Object ..... 94  
6.9.10 Requirements for train integrity ..... 95  
6.10 SysF Manage Unresolved Trackbound Object ..... 97  
6.10.1 Overview ..... 97  
6.10.2 Propagation concept ..... 99  
6.10.3 Storage requirements ..... 99  
6.10.4 Requirements to update Unresolved Trackbound Objects ..... 101

---

6.10.5 Removing an Unresolved Trackbound Object ..... 111  
6.10.6 Impact from TTD on Unresolved Trackbound Objects ..... 112  
6.10.7 Requirements related to Operator panel – FOR FURTHER RELEASE ..... 119  
6.11 SysF Authorise MP Request ..... 122  
6.11.1 Overview ..... 122  
6.11.2 Inputs ..... 128  
6.11.3 Outputs ..... 128  
6.11.4 Functional requirements ..... 129  
6.12 Authorise Cooperative Shortening Request ..... 164  
6.12.1 Overview ..... 164  
6.12.2 Inputs ..... 164  
6.12.3 Outputs ..... 164  
6.12.4 Functional requirements ..... 165  
6.13 SysF Translate MP Request to Movement Authority ..... 167  
6.13.1 Overview ..... 167  
6.13.2 Inputs ..... 168  
6.13.3 Outputs ..... 168  
6.13.4 Functional requirements ..... 169  
6.14 SysF Translate Cooperative Shortening Request to Request to Shorten MA ..... 173  
6.14.1 Overview ..... 173  
6.14.2 Inputs ..... 173  
6.14.3 Outputs ..... 173  
6.14.4 Functional requirements ..... 174  
6.15 SysF Delete Train Object ..... 174  
6.15.1 Overview ..... 174  
6.15.2 Inputs ..... 175  
6.15.3 Outputs ..... 175  
6.15.4 Functional Requirements ..... 175  
6.16 SysF Request Movement Permission ..... 177  
6.16.1 Overview ..... 177  
6.16.2 Inputs ..... 177  
6.16.3 Outputs ..... 177  
6.16.4 Functional requirements ..... 177  
6.17 General requirements ..... 178  
6.18 SysF Update Movement Permission ..... 178  
6.18.1 Overview ..... 178

---

6.18.2 Inputs.....178  
6.18.3 Outputs.....179  
6.18.4 Functional requirements.....179  
6.18.5 Functional requirements for Risk Path update.....180  
6.19 SysF supervise<Actor>Communication.....181  
6.19.1 Overview.....181  
6.19.2 Inputs.....181  
6.19.3 Outputs.....181  
6.19.4 Functional requirements.....182  
6.20 SysF establish<Actor>Communication.....182  
6.20.1 Overview.....182  
6.20.2 Inputs.....182  
6.20.3 Outputs.....182  
6.20.4 Functional requirements.....183  
7 Interface Specifications.....183  
7.1 Description of the external interface I_TACS.....183  
7.1.1 Role of the external interface.....183  
7.1.2 Overview.....184  
7.1.3 Physical level.....184  
7.1.4 Protocol level.....184  
7.1.5 Application level.....185  
7.1.6 Input Application Layer Messages.....186  
7.1.7 Output Application Layer Messages.....186  
7.1.8 Implicit choices and justification.....186  
7.2 Description of the external interface I_PE.....186  
7.2.1 Role of the external interface.....186  
7.2.2 Overview.....186  
7.2.3 Physical level.....186  
7.2.4 Protocol level.....187  
7.2.5 Application level.....187  
7.2.6 Input Application Layer Messages.....187  
7.2.7 Output Application Layer Messages.....187  
7.2.8 Implicit choices and justification.....187  
7.3 Description of the external interface I_OBU.....187  
7.3.1 Role of the external interface.....187  
7.3.2 Overview.....187

---

7.3.3 Physical level ..... 187  
7.3.4 Protocol level ..... 188  
7.3.5 Application level ..... 188  
7.3.6 Input Application Layer Messages ..... 188  
7.3.7 Output Application Layer Messages ..... 188  
7.3.8 Implicit choices and justification ..... 188  
7.4 Description of the external interface I_DR ..... 188  
7.4.1 Role of the external interface ..... 188  
7.4.2 Overview ..... 188  
7.4.3 Physical level ..... 189  
7.4.4 Protocol level ..... 189  
7.4.5 Application level ..... 189  
7.4.6 Input Application Layer Messages ..... 189  
7.4.7 Output Application Layer Messages ..... 190  
7.4.8 Implicit choices and justification ..... 191  
7.5 Description of the external interface I_OP ..... 191  
7.6 Description of the external interface I_AS ..... 191  
7.7 Description of the external interface I_SEC ..... 191  
7.8 Description of the external interface I_Diagn_and_Maint ..... 191  
8 References ..... 192  
Annex 1 ..... 194  
Annex 2: templates ..... 196

---

## LIST OF FIGURES

Figure 1 – System Boundaries ..... 25  
Figure 2 – Scenario pattern: Initiate communication ..... 28  
Figure 3 – Scenario pattern: Respond to communication initiation ..... 29  
Figure 4 – Scenario: Start and Maintain MBS ..... 32  
Figure 5: Scenario to pre-load Topology Data ..... 34  
Figure 6 – Scenario: Respond to Initiation of communication session by PE ..... 37  
Figure 7 – Scenario: Start communication session with a TACS ..... 38  
Figure 8 – Scenario: Start communication session with an OBU ..... 40  
Figure 9 – Scenario: Control Switchable Trackside Assets ..... 42  
Figure 10 – Scenario 1: Update MBS Operational State when TA state report is received ..... 44  
Figure 11 – Scenario 2: Update MBS Operational State when train position report or validated train data are received ..... 45  
Figure 12 – Scenario 3: Update of status when no communication with TACS anymore ..... 46  
Figure 13 – Scenario 4: Update of MBS Operational State when no communication with OBU anymore ..... 47  
Figure 14 – Scenario: Report of MBS Operational State when triggered ..... 48  
Figure 15 – Scenario 1: Start of Train ..... 50  
Figure 16 – Scenario: Provide MA to Train ..... 51  
Figure 17 – Scenario 1: Train End of Mission ..... 53  
Figure 18 – Scenario 2: Termination of communication session by OBU ..... 54  
Figure 19 – Scenario 3: end mission when no communication anymore with an OBU ..... 54  
Figure 20 – Scenario 1: Revoke MA cooperatively by PE ..... 56  
Figure 21: Terms used for Train Location ..... 75  
Figure 22: Train Location from Start of Mission Train Position Report ..... 78  
Figure 23: Front of Train Location updated from new Train Position Report ..... 80  
Figure 24: Rear of Train Location updated from new Train Position Report, Integrity Confirmed ..... 81  
Figure 25: Train Location when receiving Validated Train Data during Start of Mission ..... 83  
Figure 26: Train Location when receiving Validated Train Data, L_TRAIN decreased ..... 83  
Figure 27: Train Location when receiving Validated Train Data, L_TRAIN increased ..... 84  
Figure 28: Shortening of front of Train Location due to clear TTD ..... 88  
Figure 29: No shortening of front of Train Location due to clear TTD ..... 88  
Figure 30: Shortening of rear of Train Location due to clear TTD ..... 89  
Figure 31: No shortening of rear of Train Location due to clear TTD ..... 89  
Figure 32 Extension of Train Location after Mute Timer has expired by Occupied TTD ..... 91  
Figure 33: Train Location after confirmation of Train Integrity ..... 103  
Figure 34: UTO creation when receiving Validated Train Data, L_TRAIN decreased ..... 104

---

Figure 35: Unresolved Trackbound Object remains when Front Train after Splitting leaves ..... 106  
Figure 36: Unresolved Trackbound Object updated after integrity confirmed by Driver ..... 108  
Figure 37: Train with Train Integrity confirmed Sweeping an Unresolved Trackbound Object ..... 109  
Figure 38: Existing Unresolved Trackbound Object swept by a passing train ..... 109  
Figure 39: New Unresolved Trackbound Object swept by a passing train ..... 110  
Figure 40: Short Unresolved Trackbound Object at crossover ..... 112  
Figure 41: Creation of Unresolved Trackbound Object for unexpected Clear TTD ..... 116  
Figure 42: UTO propagation with a train in the same direction ..... 117  
Figure 43: UTO propagation with a train in the opposite direction ..... 117  
Figure 44: UTO creation for a non-integer train ..... 118  
Figure 45 - Scenario: Template Scenario ..... 197

## LIST OF TABLES

Table 1 – Description of SysC: Start and Maintain MBS.....31  
Table 2 – Description of SysC: Respond to initiation of communication session by PE.....36  
Table 3 – Description of SysC: Start communication with one TACS.....37  
Table 4 – Description of SysC: Control Switchable Trackside Assets.....40  
Table 5 – Description of SysC: Update MBS Operational State.....42  
Table 6 – Description of SysC: Report MBS Operational State.....47  
Table 7 – Description of SysC: Provide MA to Train.....50  
Table 8 – Description of SysC: Terminate Train Mission.....51  
Table 9 – Description of SysC: Revoke MA cooperatively by PE.....55  
Table 10 – Reasons to create or move Train Location.....76  
Table 11 – Reasons to delete Train Location.....76  
Table 12 – Reasons to create or extend Unresolved Trackbound Object.....98  
Table 13 – Reasons to remove (even partly) Unresolved Trackbound Object.....98  
Table 14 – Unresolved Trackbound Object Stored Data.....100  
Table 15 – Flank Protection measures configuration.....125  
Table 16 – Description of SysC: <Template>.....196

---

## 1 INTRODUCTION

The task 13.2 "Moving Block Specification – Requirements, engineering and operational rules" within the WP13 of the project FP2 – R2DATO has got the objective to develop a Moving Block Specification.

As a result of this task, the present document specifies the Moving Block System, as firstly defined in the Moving Block System Definition (document /SysDef/).

This specification focuses on the functional requirements. Non-functional requirements are considered in a later release of this document.

This document is related to the following work packages:

- WP13: Task 13.3: Moving Block Safety Analysis

- WP14: Moving Block ETCS Level 3 – Prototype development & Analysis



WP44-45: Moving Block ETCS L3 Demonstrator – Specification

---

The scope of release 3 of the System Specification is limited as follows¹:

Capability:

• Start up the system

• Load Domain Data at start-up

• Control the Trackside Assets (SCI-P only)

• Establish, maintain and terminate communication session with Trackside Assets

• Manage track path allocation (including Release allocated portion of track path which has been passed by the train and Release allocated portion of track in front of the train)

• Manage authorisations for train movement (Movement Authority, Request to Shorten MA)

• Manage the current trackside state and determine the state of the track from information given during runtime by trains and Trackside Assets within its Area of Control

- Store an up-to-date, reliable and consistent MBS Operational State and provide this to consuming systems (PE only)

• Establish, maintain and terminate communication session with OBU

## I nterface with

• Trackside Assets (SCI-P and SCI-TDS) via Trackside Asset Control and Supervision (TACS) instances

• Plan Execution (PE)

• ETCS On-board (OBU)

• Digital Register (DR)

The following needs are covered:

• Flank Protection

• Splitting, joining, turning (with/without Cold Movement Detection)

• DPS Group

• Propagation of UTOs

• Train length (L TRAIN) reliability

All other interfacing systems according to /SysDef/ are out of scope for this release.

For Trackside Asset, only SCI-P and TTD sections are considered.

---

# Contract No. HE – 101102001

(Degraded) operational scenarios are not defined/analysed/covered (e.g. odometry issues, reset of axle counters, etc...)

Override is out of scope

Only the ETCS modes SB, FS, OS are covered inside the AoC.

Transitions (from/to adjacent interlockings, RBC, and MBS) are out of scope.

### 2.1 GENERAL LIMITATIONS

This chapter contains general limitations that are valid for all releases of the System Specification.

Disclaimer: this specification is not yet part of a complete safety analysis.

As the System Specification also contains the functionality of an RBC, the MBS shall be able to perform all the functions of the RBC Basic Interoperability Constituent (IC). Instead of repeating the /ETCS/, this document focuses on the essential functions of the MBS rather than specifying each function in detail of the RBC functionality.

This System Specification does not explicitly specify the rules to provide national values, position report parameters and MA request parameters to the OBU. This depends on e.g. the operational rules and therefore is assumed to be application specific.

- This System Specification focuses on functional requirements.

- The swinging overlaps are currently not supported (see REQ-SC_DPS_RB).

The System Version 2.1 of /ETCS/ is only supported by the MBS.

☐ Justification: This System Specification is used by the demonstrators using OBUs. But there are no OBUs available yet supporting a newer System Version than 2.1. In later editions of the System Specification newer System Versions will be supported.

This System Specification does not explicitly specify how the cryptographic artefacts (e.g. KMACS) for the communication between MBS and the trains are made known to the MBS.

Justification: According to chapter 2 this interface is out of scope of this System Specification.

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>it later for the specification of the System Requirements. A justification is provided for each of the consolidated concepts.</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>Then the System Capabilities (as listed in the /SysDef/) related to the operational scenarios are detailed. Afterwards this detailing is used to derive sequence diagrams depicting the interactions of the MBS with neighbouring systems connected to it. The sequence diagrams are additionally utilised to derive the necessary System Functions. The same System Function may be used by several capabilities or scenarios.</td><td style='text-align: center;'>Chapter 5</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>Subsequently the derived System Functions are described and the specific requirements for them are listed considering the consolidated concepts (in step 1), if applicable.</td><td style='text-align: center;'>Chapter 6</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>Based on the scenarios, the interface needs (e.g., messages, etc.) are described considering existing standards and the concepts, if applicable.</td><td style='text-align: center;'>Chapter 7</td></tr></table>

---

## 4 MBS OVERVIEW

An overview of the environment and boundaries of the Moving Block System (MBS) is shown in the following figure with the mentioned technological systems, environment, humans and other railway duty holders.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d9ce76bf-30bd-4af9-b3da-8c13ecb4ea4d/markdown_0/imgs/img_in_image_box_100_333_1118_1315.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A32%3A33Z%2F-1%2F%2Fac5264da3c01702925cfd1c4acae3e2f5d5c2f95d1bf18d3ce7b9a927d899267" alt="Image" width="85%" /></div>


<div style="text-align: center;">Figure 1 – System Boundaries</div>


Note: The interface to the Operator Panel, amongst others, is not standardised yet and has to be defined. The Figure 1 considers two options. As this design decision is not clear yet, this is highlighted in red.

For more information about the system boundaries, please refer to the System Definition (ref./SysDef/) chapter 3.

---

## 5 SYSTEM CAPABILITIES SPECIFICATION

This chapter further details the system capabilities defined in /SysDef/.

The following table provides a mapping from the system capabilities listed in /SysDef/ to the system capabilities detailed in this System Specification.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>System Capability as listed in /SysDef/</td><td style='text-align: center;'>Chapter(s) in System Specification</td></tr><tr><td style='text-align: center;'>MBS manages communication sessions with Trackside Assets (TA) via specified interfaces within its Area of Control (AoC).</td><td style='text-align: center;'>5.6 SysC: Start communication with one TACS</td></tr><tr><td style='text-align: center;'>MBS manages communication sessions with trains via specified interfaces within its AoC and adjacent areas where trains are supposed to establish or terminate a communication session.</td><td style='text-align: center;'>5.7 SysC: Respond to initiation of communication session by OBU5.14 SysC: Terminate Train Mission</td></tr><tr><td style='text-align: center;'>MBS controls all TAs within its AoC.</td><td style='text-align: center;'>5.8 SysC: Control Switchable Trackside Assets</td></tr><tr><td style='text-align: center;'>MBS manages the current trackside state and determines the state of the track from information given during runtime by trains and TAs within its AoC.</td><td style='text-align: center;'>5.12 SysC: Start of Train5.10 SysC: Update MBS Operational State5.14 SysC: Terminate Train Mission</td></tr><tr><td style='text-align: center;'>MBS manages all track path allocations for all trains and vehicles within its AoC. This contains an adequate and risk-based protection of requested pieces of track for an intentional train movement.</td><td style='text-align: center;'>5.13 SysC: Provide MA to Train</td></tr><tr><td style='text-align: center;'>MBS issues authorisations for train movements based on requested and accepted track path allocations.</td><td style='text-align: center;'>5.13 SysC: Provide MA to Train</td></tr><tr><td style='text-align: center;'>MBS supervises trains and TAs to prevent railway accidents. This includes especially any collision, derailment or over-speeding.</td><td style='text-align: center;'>Out of scope for current releases</td></tr><tr><td style='text-align: center;'>MBS stores an up-to-date, reliable and consistent current Operational State and provides this Operational State to systems connected to MBS.</td><td style='text-align: center;'>5.10 SysC: Update MBS Operational State5.11 SysC: Report MBS Operational State</td></tr><tr><td style='text-align: center;'>MBS manages Domain Data changes (e.g., by introducing new parts and/or changes of the track)</td><td style='text-align: center;'>5.2 SysC: Preload Topology Data5.3 SysC: Approve Topology Data activation5.4 SysC: Activate Topology Data</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>MBS handles a safe transition of train movement from and to adjacent systems.</td><td style='text-align: center;'>Out of scope for current releases</td></tr><tr><td colspan="2">Different scenarios outlining the MPS behind.</td></tr></table>

Different scenarios outlining the MBS behaviour are defined for each capability.

Please refer to “Annex 2: Template” for explanation of the following capability tables and sequence diagrams.

### 5.1 SysC: START AND MAINTAIN MBS

#### 5.1.1 Communication patterns

MBS has communication sessions to its actors according to the following list. For every actor it is described why there is the initiator/responder role:

(MBS as session initiator)

- DR: DR is a service which provides topology data to its clients. It therefore acts in a server role which means that clients (like MBS) establish the communication to the server.

- TACS: Defined by EULYNX, the interlocking (here: MBS) is responsible to initiate the communication.

(MBS as session initiation responder)

- PE: MBS is a service to PE which serves requests to set Switchable Trackside Assets and grant Movement Permissions. MBS therefore acts in a server role which means that PE establishes the communication to the server (MBS).

- OBU: It initiates the communication as MBS won't know all trains in its area until they connect (/ETCS/ - SUBSET-026 §3.5.3.4 of /ETCS/).

MBS also supervises the communication so it can react to a loss of communication.

If MBS is the session initiator, it means whenever a supervision function of MBS detects that there is no communication, it establishes a communication (which might be the very first establishment at start of MBS or a re-establishment after a communication loss):

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1a661eed-035f-45bd-b867-b415dd7ada51/markdown_0/imgs/img_in_image_box_258_189_966_929.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A32%3A44Z%2F-1%2F%2F7e4830d9519619a815eeb464d26a8bc0de79f3923f6d13865e83d24cbb8a2a9e" alt="Image" width="59%" /></div>


<div style="text-align: center;">Figure 2 – Scenario pattern: Initiate communication</div>


<Actor> can be DR or TACS.

---

If MBS is the session responder, it needs not to care for re-establishment (but the actor):

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0e98568f-cc9c-4248-82a4-ba1136e8129a/markdown_0/imgs/img_in_image_box_243_230_1012_902.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A32%3A46Z%2F-1%2F%2F80e76b3dcb818063b07abfa49d3fca370ffd50f45e80a161d03c5a49257459fc" alt="Image" width="64%" /></div>


<div style="text-align: center;">Figure 3 – Scenario pattern: Respond to communication initiation <Actor> can be PE or OBU.</div>

---

The <actor>CommEstablished event can be used to trigger further scenarios like the synchronisation of TACS in case of <actor> == TACS or initialisation of a related state.

The <actor>CommLost event can be used to trigger further scenarios like setting (a) related Domain Object(s) to the safe state.

With this, MBS can react independently on the raised internal events:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d27d6e61-332e-4bcb-85b6-481ee119a4e3/markdown_0/imgs/img_in_image_box_97_414_1132_1372.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A32%3A49Z%2F-1%2F%2Fecdef774763153553718001e291e938fa7a79cc8c35318023db0a7b05f8c5558" alt="Image" width="86%" /></div>

---

#### 5.1.2 Capability

The named communication pattern is applied to MBS in order to supervise communication to actors ((re-)establish/maintain communication).

<div style="text-align: center;">Table 1 – Description of SysC: Start and Maintain MBS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability allows to start and maintain MBS communication to actors.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>MBS is operational</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Success)</td><td style='text-align: center;'>The Moving Block System has been started and is operational.</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Failure)</td><td style='text-align: center;'>The Moving Block System is not operational.</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>DR, PE, OBU, TACS</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>MBS is started</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>1. MBS supervises the communication to actors (This is done in a continuous loop.)</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>Only for release 2.4:1. If loading or checking the Topology Data fails, the start procedure terminates.</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>MBS could either be started by an external event or automatically when recovering from a failure for example.The communication patterns raise events &lt;actor&gt;CommEstablished and &lt;actor&gt;CommLost for every actor &lt;actor&gt;(UML: lost message). Other capabilities can react (UML: found message) to these events and react accordingly (e.g. initialising a safe state).</td></tr></table>

---

<div style="text-align: center;">5.1.3 Scenario: Start and Maintain MBS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//25e48077-491b-4281-960d-3b6bc46cb944/markdown_0/imgs/img_in_image_box_97_200_1131_693.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A32%3A55Z%2F-1%2F%2F888dcd9202ccc557dcf30f5c39c69bb961f2d8e2a530a093c3815a90c65bcc32" alt="Image" width="86%" /></div>


<div style="text-align: center;">Figure 4 - Scenario: Start and Maintain MBS</div>

---

<div style="text-align: center;">5.2 SYSC: PRELOAD TOPOLOGY DATA</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability allows to provide MBS with Topology Data initially. This finally results into topology-related Domain Objects</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>MBS has loaded (initial or new version of) Topology Data and related Domain Objects</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>No Topology Data available (no Topology Data loaded) at startup</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Success)</td><td style='text-align: center;'>Up to release 4: MBS has loaded, approved, and activated Topology Data MBS is operational</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>From release 5 on (more granular steps so this capability only does preloading): MBS has loaded Topology Data MBS is operational</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Failure)</td><td style='text-align: center;'>MBS state related to Topology Data has not changed MBS is not operational</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>DR</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>1. MBS starts up2. (For further release) MBS receives the Topology Data from DR</td></tr><tr><td rowspan="2">Main Sequence</td><td style='text-align: center;'>Up to release 4:1. MBS establishes a communication session with DR.2. MBS requests Topology Data from DR3. MBS receives Topology Data and activates them</td></tr><tr><td style='text-align: center;'>From release 5 on:1. MBS establishes a communication session with DR.2. MBS requests Topology Data from DR3. MBS receives Topology Data and pre-loads them.4. MBS approves the activation of Topology Data5. MBS activates Topology Data</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>From release 5 on:At any point in time, DR can send Topology Data to MBS (continues then from 3. on)</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>4. MBS rejects the approval when there are e.g. conflicting Movement Permissions (for further release)</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>Before release 5, there are the following restrictions  ·The scope of Topology Data is the full Area of Control (so no partial update)  ·Topology Data are loaded only once at startup and remain unchanged (so no update during run-time)  ·It is assumed that neither connecting to DR, nor loading the Topology Data from there fails (exclusion of unhappy paths)The scenario will thus widen in a later release: data are not only loaded and immediately activated, but pre-loaded, approved, and activated. In order to save work already knowing the future state, the function to load Topology Data is already named ‘preload’ and not only ‘load’. The term ‘preloaded’ can be read as ‘loaded’.</td></tr></table>

---

#### 5.2.1 Scenario: Preload Topology Data

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6fcd2c3d-b16e-4fd4-bf75-8e341d910ae9/markdown_0/imgs/img_in_image_box_218_285_1026_1302.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A03Z%2F-1%2F%2Fb94701c2cd954d0b8b18ba34e35a2c2a087a13fb26d185f3922a0a66c0e0622c" alt="Image" width="67%" /></div>


<div style="text-align: center;">Figure 5: Scenario to pre-load Topology Data</div>


### 5.3 SysC: Approve Topology Data Activation

Note: This capability checks if data in the to-be-updated area can be approved from MBS point of view (e.g. no Movement Permissions are in conflict) and will be part of a further release. Until then, there is no such check and data are regarded as approved already within function 'Preload Topology Data'.

---

Note: This capability finally activates the data and will be part of a further release. Until then, there is no such procedure and data are regarded as activated already within function, preload Topology.

Data.

5.4 SYS: ACTIVATE TOPLOGY DATA

---

### 5.5 SysC: RESPOND TO INITIATION OF COMMUNICATION SESSION BY PE

<div style="text-align: center;">Table 2 – Description of SysC: Respond to initiation of communication session by PE</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability responds to the communication session establishment by PE. This communication session is crucial to e.g., be able to receive requests for Movement Permissions for trains. After the communication session is established, the MBS distributes its MBS Operational State (e.g., state of Trackside Assets) to PE.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>MBS has distributed its MBS Operational State to PE.</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>MBS is operational</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Success)</td><td style='text-align: center;'>The MBS Operational State is synchronised with PE</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Failure)</td><td style='text-align: center;'>No communication session to PE</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>PE</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>Event PECommEstablished</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>1. MBS distributes its MBS Operational State to PE.</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>1. MBS cannot distribute the MBS Operational State to PE. MBS closes the communication session</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>This capability may be triggered after start of MBS or when the communication session to the PE needs to be re-established for any reason. When - in failure case - the communication session is closed, the capability ‘Start and Maintain MBS’ will re-establish the session and this triggers this capability again.</td></tr></table>

---

#### 5.5.1 Scenario: Respond to initiation of communication session by PE

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1f60412b-5bdd-4842-a273-cb2ce788d079/markdown_0/imgs/img_in_image_box_252_226_981_726.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A12Z%2F-1%2F%2F46a8f96066901f18e325514398d7505d19e11f51a995dcab99425b2b8f7d9092" alt="Image" width="61%" /></div>


<div style="text-align: center;">Figure 6 - Scenario: Respond to Initiation of communication session by PE</div>


This system capability is not detailed further since there is no defined interface specification (e.g. SCI-CMD) yet.

Currently it is assumed that the initiation of the communication session is triggered by PE whereupon MBS shall be able to receive commands from PE and provide information (e.g. MBS Operational State) to PE.

### 5.6 SysC: START COMMUNICATION WITH ONE TACS

<div style="text-align: center;">Table 3 – Description of SysC: Start communication with one TACS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability responds to the communication session establishment between the MBS and one TACS; the capability is applied for each TACS.
MBS performs the synchronisation with TACS, updates the related Domain Objects and distributes their state to PE (by capability ‘Report MBS Operational State’)</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>Domain Objects of MBS are synchronised with TACS and subsequently MBS has distributed the corresponding Domain Object state to PE.</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>MBS is operational)</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Success)</td><td style='text-align: center;'>MBS has distributed the corresponding Domain Object state to PE.</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Failure)</td><td style='text-align: center;'>No communication session to TACS</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>PE, TACS</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>Event TACSCommEstablished(TACSId)</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>1. MBS synchronises with TACS.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>2. MBS updates and distributes the corresponding Domain Objects state to PE (according to the capability &#x27;Update MBS Operational State&#x27;)</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>1. The synchronisation with TACS failed MBS closes the communication session</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>This capability may be triggered after start of MBS or when the communication session to a TACS was re-established for any reason. When - in failure case - the communication session is closed, the capability &#x27;Start and Maintain MBS&#x27; will re-establish the session and trigger this capability again.</td></tr></table>

<div style="text-align: center;">5.6.1 Scenario: Start communication session with a TACS</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bd9c6fcb-4551-4a71-a6aa-697e43056a45/markdown_0/imgs/img_in_image_box_100_585_1064_1021.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A16Z%2F-1%2F%2Fdf68037cdf11a850fb3bff7fa6e06a0f1dc37fde11538e3585dc27e5458ab92a" alt="Image" width="80%" /></div>


<div style="text-align: center;">Figure 7 - Scenario: Start communication session with a TACS</div>


The capability “Establish communication session with a TACS” is responsible for establishing a communication session with a TACS. Generally, when MBS detects that there is no communication session with the TACS, the MBS shall establish a communication session with a TACS. This capability is not further detailed in this chapter. Instead the details are described in chapter 7.1 of this document.

<div style="text-align: center;">5.7 SysC: Respond to Initiation of Communication Session by OBU</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability manages the establishment of the communication session between the MBS and an OBU considering the requirements of
• chapter 3.5.3 (Establishing a communication session) of /ETCS/
- SUBSET-026.
• /ETCS/ - SUBSET-037.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>A communication session with an OBU is established.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>MBS is operational</td></tr><tr><td style='text-align: center;'>Postcondition(s)(Success)</td><td style='text-align: center;'>A communication session with an OBU was established.</td></tr><tr><td style='text-align: center;'>Postcondition(s)(Failure)</td><td style='text-align: center;'>A communication session with an OBU could not be established.</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>OBU, PE</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>An OBU requests to set-up a safe radio connection with the MBS.</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>1. MBS sets-up a safe radio connection and communication session according to /ETCS/ considering using System Version 2.1. MBS creates a Train Object for this OBU and subsequently informs PE about this through the capability &#x27;Update MBS Operational State&#x27;.</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None.</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>1. If a condition to establish a safe connection or communication session is not fulfilled, then MBS ends the procedure to set-up a safe radio connection and communication session by terminating the safe connection, if any.</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>The failure sequence may be triggered e.g. in the following case:  ·There is no key (KMAC) available within MBS for this OBU.</td></tr></table>

---

<div style="text-align: center;">5.7.1 Scenario: Start communication session with an OBU</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//67b30f45-7517-4beb-900e-87b55c7aa968/markdown_0/imgs/img_in_image_box_148_214_1088_886.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A23Z%2F-1%2F%2F9d7d1db96cc563df6dd3c5af6adabea7445149cb6ee6477e62cace2545581cc9" alt="Image" width="78%" /></div>


<div style="text-align: center;">Figure 8 - Scenario: Start communication session with an OBU</div>


The capability “Establish safe radio connection and communication session with an OBU” referenced in the scenario is responsible for managing the safe radio connection and communication session establishment between MBS and an OBU considering the requirements of:

• Chapter 3.5.3 (Establishing a communication session) of /ETCS/ - SUBSET-026 and

• /ETCS/ - SUBSET-037.

This capability is not detailed further on since the requirements are already provided in the /ETCS/ as stated above.

<div style="text-align: center;">5.8 SysC: Control Switchable Trackside Assets</div>


<div style="text-align: center;">Table 4 – Description of SysC: Control Switchable Trackside Assets</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability allows PE to change the state of a Switchable Trackside Asset by sending a corresponding TA State Request to MBS. MBS has to verify if the request is valid. If it is valid, MBS carries it out by sending the corresponding command to the TACS related to the Switchable Trackside Asset.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>Due to a request from PE, a Switchable Trackside Asset is commanded to change its state by sending a command to its TACS.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Preconditions</td><td style='text-align: center;'>MBS is operational 5.1.2</td></tr><tr><td rowspan="2">Postcondition (Success)</td><td style='text-align: center;'>Granting of request is indicated to PE.</td></tr><tr><td style='text-align: center;'>Command for changing its state is sent to TACS.</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'>Rejecting of a valid request from PE. Command for changing its state is not sent to TACS.</td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>PE, TACS</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>Request from PE to change the position of a Switchable Trackside Asset via its TACS.</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>A valid request is granted and carried out by MBS (see: Scenario: Control Switchable Trackside Assets) and MBS informs PE about granting this request</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>An invalid request is rejected by MBS (see: Scenario: Control Switchable Trackside Assets) and MBS informs PE about rejecting this request.</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>None</td></tr></table>

#### 5.8.1 Scenario: Control Switchable Trackside Assets

The figure below contains the main sequence and the failure sequence of the SysC Control Switchable Trackside Asset.

When the MBS receives a TA State Request, it performs the safety checks (Function: Authorise TA State Request) for the request.

If the safety checks are successful, MBS responds to PE the granting of the request and translates the request to a TACS command (Function: Translate TA State Request to TACS Command). The TACS command is then sent to the related TACS (Function: Send TACS Command).

If the safety checks fail, MBS responds to PE system the rejecting of the request and performs no further actions for the request.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//545df040-123b-4341-87e3-d9ccc7e2eb93/markdown_0/imgs/img_in_image_box_125_161_1108_923.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A31Z%2F-1%2F%2F4b03dad4bc14b036cc4b35f392c66f0f79fc10fe41934715bdc5296399ffb323" alt="Image" width="82%" /></div>


<div style="text-align: center;">Figure 9 - Scenario: Control Switchable Trackside Assets</div>


Note that the response from the Switchable Trackside Asset is not shown here, it is asynchronously sent (refer to the next section).

### 5.9 SysC: Shutdown MBS

Out of scope for this release

### 5.10 SysC: Update MBS Operational State

<div style="text-align: center;">Table 5 – Description of SysC: Update MBS Operational State</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability updates the MBS Operational State.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>Update the state of MBS Operational State</td></tr><tr><td style='text-align: center;'>Precondition</td><td style='text-align: center;'>MBS is operational)</td></tr><tr><td style='text-align: center;'>Postcondition (Success)</td><td style='text-align: center;'>MBS has updated its MBS Operational State</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'>None (no failure)</td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>• TACS• OBU• PE</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>• Any change of MBS Operational State is detected (inexhaustive list):</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>• MBS receives a state update report from the TACS• MBS detects that there is no communication with TACS anymore• MBS receives a position report from OBU• MBS receives validated train data from OBU• The communication between MBS and an OBU is established• MBS detects that there is no communication with OBU anymore</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>Scenario 1: Update MBS Operational State when TA state report is receivedScenario 2: Update MBS Operational State when a train position report or validated train data are received</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>Scenario 3: Update MBS Operational State when no communication with TACS anymoreScenario 4: Update MBS Operational State when no communication with OBU anymore</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>None</td></tr></table>

#### 5.10.1 Scenario 1: Update MBS Operational state when TA state report is received

This scenario covers the nominal scenario (all communications are established), when a TA state report is received from a TACS.

Train Location or Unresolved Trackbound Object are updated when a TTD section status changes. Risk Path, part of the Movement Permission, may be updated when a Point status changes.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ca67570e-5120-4ad8-8185-0281f4bd161c/markdown_0/imgs/img_in_image_box_125_179_1092_913.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A36Z%2F-1%2F%2F486e1f3df1f5b5269cabb6310cd512d3312cf9d5d86dfd5a996012c50732e259" alt="Image" width="81%" /></div>


<div style="text-align: center;">Figure 10 - Scenario 1: Update MBS Operational State when TA state report is received</div>


#### 5.10.2 Scenario 2: Update MBS Operational State when a train position report or validated train data are received

This scenario covers the nominal scenario (all communications are established), when a position report or validated train data are received from the train.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//cc76fae4-149e-47af-868c-531f27f37c2b/markdown_0/imgs/img_in_image_box_103_208_1099_939.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A40Z%2F-1%2F%2Fe80bbfa59566b038d4f7fd05630e7d609e16ae346ee71aa7f03f117f33da0c6d" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 11 - Scenario 2: Update MBS Operational State when train position report or validated train data are received</div>


#### 5.10.3 Scenario 3: Update MBS Operational State when no communication with TACS anymore

This scenario covers the status to be reported when the communication with the TACS is lost.

When the MBS detects that the communication with a TACS is lost, the MBS sets and reports the safe value of the related Domain Object to the PE, Train Location and UTO are also updated if impacted by a TTD section change.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ce94a09e-da8d-4fb7-9a8e-8e50d3427366/markdown_0/imgs/img_in_image_box_103_203_1104_1014.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A43Z%2F-1%2F%2Fe128d0ebb9db284ffa04c52f03f7192fcd62e0bb7a00e81cd6758827732da970" alt="Image" width="84%" /></div>


<div style="text-align: center;">Figure 12 - Scenario 3: Update of status when no communication with TACS anymore</div>


#### 5.10.4 Scenario 4: Update MBS Operational State when no communication with OBU anymore

This scenario covers the status to be reported when the communication with the OBU is lost.

When the MBS detects that the communication with the OBU is lost, the MBS reports this information to the PE in the Train Object.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a083baee-a403-4d78-b3be-40f5e2abaad7/markdown_0/imgs/img_in_image_box_133_175_1092_586.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A46Z%2F-1%2F%2Fa9277332809775f6e7398ff3d3cc176fd959965bc19ad6635a2ca63dc583bba9" alt="Image" width="80%" /></div>


<div style="text-align: center;">Figure 13 - Scenario 4: Update of MBS Operational State when no communication with OBU anymore</div>


<div style="text-align: center;">5.11 SysC: Report MBS Operational State</div>


<div style="text-align: center;">Table 6 – Description of SysC: Report MBS Operational State</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>When triggered, this capability reports the MBS Operational State.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>Report the state of MBS Operational State</td></tr><tr><td style='text-align: center;'>Precondition</td><td style='text-align: center;'>MBS is operational 5.1.2</td></tr><tr><td style='text-align: center;'>Postcondition (Success)</td><td style='text-align: center;'>PE has received the MBS Operational State for the given Domain Object Instance</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'>None (no failure)</td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>• PE</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>Triggered for a given Domain Object Instance by other capabilities</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>Scenario: Report of MBS Operational State</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>None</td></tr></table>

---

#### 5.11.1 Scenario: Report of MBS Operational State when triggered

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ce7bc865-c773-4b92-b4da-cabd00da61ca/markdown_0/imgs/img_in_image_box_273_210_923_571.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A50Z%2F-1%2F%2F42d1101d577bc3c4cc80f3802c71dedad548e0935f987b28ae8f9ceae33e300b" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 14 - Scenario: Report of MBS Operational State when triggered</div>


<div style="text-align: center;">5.12 SysC: START OF TRAIN</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>Start of Train</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>A train successfully has started up according to /ETCS/ and MBS has subsequently sent an Authorisation Requested message to PE.</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>MBS is operational 5.1.2</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Success)</td><td style='text-align: center;'>MBS has sent an Authorisation Requested message to PE after receiving a first MA request during the Start of Mission procedure.</td></tr><tr><td style='text-align: center;'>Postcondition(s) (Failure)</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>OBU, PE</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>MBS receives a SoM Position Report message from an OBU.</td></tr><tr><td rowspan="3">Main Sequence</td><td style='text-align: center;'>1. MBS determines that the position is valid and unambiguous.
MBS updates the Train Object.</td></tr><tr><td style='text-align: center;'>2. MBS receives Train Data, Train Running Number from OBU and subsequently acknowledges the train data to the OBU.
MBS updates the Train Object.</td></tr><tr><td style='text-align: center;'>3. MBS receives an MA Request from OBU.
MBS provides an Authorisation Requested message to PE.</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>1.a) MBS receives a SoM Position Report with invalid / unknown position.
MBS updates the Train Object indicating that the position is invalid / unknown and sends Train Accepted to OBU. Afterwards the flow continues with step 2 of the main sequence.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>1.b) MBS receives a SoM Position Report with a valid position, but the position is ambiguous.MBS updates the Train Object indicating that the position is ambiguous and continues with step 2 of the main sequence.</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>Please consider that mode change to SH is currently excluded by the scope of the document and thus there is no failure sequence aborting this capability in such case. The same also applies for using the &#x27;Override&#x27; function.Additionally, it is also not foreseen yet to revalidate the train position (using the SoM Position Report Confirmed message) since this may depend on the operational procedures which are not available yet.</td></tr></table>

#### 5.12.1 Scenario: Start of Train

Please consider that during this scenario after each Train Position Report (packet number 0 or packet number 1), respectively after receiving the SoM Position Report, MBS updates the Train Object by the capability "Update MBS Operational State" and reports this to the PE. This handling of Train Position Reports is not explicitly illustrated in the figure to limit the sequence diagram to the Start of Train capability.

During this scenario, after the acknowledgment of Train Data, it is possible (when the OBU is equipped with a TIMS) that the MBS receives the first Train Position Report with integrity confirmed. Then especially the extent of the Train Location using the confirmed rear end is updated.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//213e55f2-6681-4e03-b0cb-3596a3c15f1e/markdown_0/imgs/img_in_image_box_83_156_1135_915.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A56Z%2F-1%2F%2F2b69738195684d1fe1c58bb3121923410143e937dcf7953470ed07ef6c628087" alt="Image" width="88%" /></div>


<div style="text-align: center;">Figure 15 - Scenario 1: Start of Train</div>


### 5.13 SysC: Provide MA to Train

<div style="text-align: center;">Table 7 – Description of SysC: Provide MA to Train</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability generates a Movement Permission for a dedicated train run and issues an Authorisation for a particular OBU.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>After receiving an MP request from PE, MBS checks all safety constraints, generates a Movement Permission for a dedicated train run and translates it into an Authorisation which is sent to the OBU.</td></tr><tr><td style='text-align: center;'>Precondition</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Postcondition (Success)</td><td style='text-align: center;'>Authorisation issued by MBS to the OBU corresponding to the Train Object; Movement Permission reported to PE.</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>• OBU• PE</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>• MBS receives a Movement Permission Request</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>When all checks are successful, MBS indicates this to PE, updates the Train Object with the Movement Permission and issues an Authorisation to OBU based on the Movement Permission Request received from PE.</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>When at least one check fails, MBS reports a Request Rejected to PE indicating the reason why the Movement Permission Request could not be granted.</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>•</td></tr></table>

#### 5.13.1 Scenario: Provide MA to Train

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//47bdce74-551f-4739-b33f-fda2880a1b39/markdown_0/imgs/img_in_image_box_74_545_1156_1450.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A33%3A59Z%2F-1%2F%2F1f968d7d24d34cca7c91517aa86144c838dd8a67475ca4d5601188ba3a922cbd" alt="Image" width="90%" /></div>


<div style="text-align: center;">Table 8 – Description of SysC: Terminate Train Mission</div>


### 5.14 SSC: Terminate Train Mission

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>This capability manages the termination of the mission of a train. It manages:  · End of mission according to /ETCS/ - SUBSET-026 chapter 5.5  · Termination of the communication session according to /ETCS/ - SUBSET-026 chapter 3.5.5.  · Loss of communicationIt converts the Train Object into an Unresolved Trackbound Object (needed by the MBS to manage the occupied area and a further start of mission for this train).It reports the information to the PE</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>Terminate the mission of a given train</td></tr><tr><td style='text-align: center;'>Precondition</td><td style='text-align: center;'>Communication between the OBU and the MBS is established</td></tr><tr><td style='text-align: center;'>Postcondition (Success)</td><td style='text-align: center;'>Communication between the OBU and the MBS is terminated. Train Object is converted into Unresolved Trackbound Object</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>· OBU· PE</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>· A message triggering the order to terminate the communication session is received from OBU (see scenario 1)· Message “termination of communication session” is received from OBU (see scenario 2)· Communication with OBU is lost for more than Session Timeout (see scenario 3)</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>Scenario 1: Train End of Mission</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>Scenario 2: Termination of communication session by OBUScenario 3: end mission when no communication anymore with an OBU</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'></td></tr></table>

#### 5.14.1 Scenario 1: Train End of Mission

This scenario covers the nominal scenario when a message triggering the order to terminate the communication session is received from the OBU.

Following messages are considered:

- message End of Mission is sent by the onboard to the MBS when the driver closes the desk, (including a change of mode to SB).

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b28b7350-42f9-4503-b599-3cf36adad806/markdown_0/imgs/img_in_image_box_107_197_1087_955.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A07Z%2F-1%2F%2F3e45b749d852b5d2e0be2b911e61024ab224401032d74c9b60348a4899fc0da9" alt="Image" width="82%" /></div>


<div style="text-align: center;">Figure 17 - Scenario 1: Train End of Mission</div>


The functions “Request Session Termination” and “Terminate communication session with OBU” referenced in the scenarios are not further detailed in this document as the behaviour is specified in in /ETCS/ SUBSET-026 chapter 3.5.5.

#### 5.14.2 Scenario 2: Termination of communication session by OBU

This scenario covers the case when a message “termination of communication session” is directly received from the OBU.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//43cc9145-e478-4c71-babd-e7ebb5dd5cda/markdown_0/imgs/img_in_image_box_110_216_1097_793.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A10Z%2F-1%2F%2F145eecfcbf155c69204a9c0ecc4338088bbfebe538acbab1cdb9af1be3808b7c" alt="Image" width="82%" /></div>


<div style="text-align: center;">Figure 18 - Scenario 2: Termination of communication session by OBU</div>


#### 5.14.3 Scenario 3: end mission when no communication anymore with an OBU

This scenario covers the degraded scenario when communication with the OBU is lost for more than a configured Session Timeout.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//43cc9145-e478-4c71-babd-e7ebb5dd5cda/markdown_0/imgs/img_in_image_box_109_1052_1107_1472.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A10Z%2F-1%2F%2F602514c06d40fba9c083bd7902c64da2721633e60057589beec8f47f87e22f38" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 19 - Scenario 3: end mission when no communication anymore with an OBU</div>


The functions “Request Session Termination” and “Terminate communication session with OBU” referenced in the scenarios are not further detailed as the behaviour is specified in the /ETCS/

---

<div style="text-align: center;">5.15 SysC: Revoke MA cooperatively by PE</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The purpose of this capability is to perform a co-operative shortening of MA, applying the principles of /ETCS/ - SUBSET-026, chapter 3.8.6 (/ETCS/). This may be necessary for the operational scenarios “Joining” or to reschedule train movements.</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>After receiving a cooperative shortening request indicating that it is requested to cooperatively shorten the MA from PE, MBS checks all safety constraints and subsequently performs the cooperative shortening of MA with the OBU.</td></tr><tr><td style='text-align: center;'>Precondition</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Postcondition (Success)</td><td style='text-align: center;'>After the OBU has accepted the new MA and has informed MBS about this, the MBS has updated the Movement Permission and informs PE about the success of the cooperative shortening of MA procedure.</td></tr><tr><td style='text-align: center;'>Postcondition (Failure)</td><td style='text-align: center;'>Failure 1: After the OBU has rejected the new MA and has informed MBS about this, the MBS informs PE about the failure of the cooperative shortening of MA procedure. The previously received MA remains valid on-board. Failure 2: The MBS has rejected the Cooperative Shortening Request.</td></tr><tr><td style='text-align: center;'>Involved Actors</td><td style='text-align: center;'>• OBU
• PE</td></tr><tr><td style='text-align: center;'>Trigger</td><td style='text-align: center;'>• MBS receives a Cooperative Shortening Request from PE indicating that it is requested to co-operatively shorten the MA.</td></tr><tr><td rowspan="2">Main Sequence</td><td style='text-align: center;'>1. When all checks are successful, then MBS indicates this to PE and subsequently sends a Request to Shorten MA message to the OBU based on the Cooperative Shortening Request received from PE.</td></tr><tr><td style='text-align: center;'>2. When MBS receives the Request to shorten MA is granted message from the OBU, then MBS indicates this to the PE. Subsequently the Train Object (including the Movement Permission) is updated and PE is also informed about that.</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>None</td></tr><tr><td rowspan="2">Failure Sequence</td><td style='text-align: center;'>1.a) When at least one check is not successful, then the MBS indicates this to PE. The co-operative shortening of MA procedure is aborted.</td></tr><tr><td style='text-align: center;'>2.a) When MBS receives the Request to shorten MA rejected message from the OBU, then MBS indicates this to PE. The co-operative shortening of MA procedure is finished.</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>None</td></tr></table>

<div style="text-align: center;">Table 9 – Description of SysC: Revoke MA cooperatively by PE</div>


#### 5.15.1 Scenario: Revoke MA cooperatively by PE

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c1423221-d410-4d0e-a1c2-6786274be1bf/markdown_0/imgs/img_in_image_box_141_168_1135_1356.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A17Z%2F-1%2F%2F8b0f9e26e1f62541194dcd4059d59e8f0d14a0f8dad42b480e3c63bf686f6d7d" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 20 - Scenario 1: Revoke MA cooperatively by PE</div>

---

## 6 SYSTEM FUNCTION SPECIFICATIONS

This chapter further details the functions introduced in the scenario of the System Capabilities.

For each function, an overview, the inputs, the outputs and the functional requirements are described.

The following table provides a mapping between the System Capabilities and the functions that are used by these capabilities inside the scenario.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>System Capability as listed in chapter 5</td><td style='text-align: center;'>Used function as listed in chapter 6</td></tr><tr><td style='text-align: center;'>5.1 SysC: Start and Maintain MBS</td><td style='text-align: center;'>6.19 SysF Supervise&lt;Actor&gt;Communication 6.20 SysF Establish&lt;Actor&gt;Communication</td></tr><tr><td style='text-align: center;'>5.2 SysC: Preload Topology Data</td><td style='text-align: center;'>6.6 SysF Preload Topology Data</td></tr><tr><td style='text-align: center;'>5.3 SysC: Approve Topology Data activation</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.4 SysC: Activate Topology Data</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.5 SysC: Respond to initiation of communication session by PE</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.6 SysC: Start communication with one TACS</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.7 SysC: Respond to initiation of communication session by OBU</td><td style='text-align: center;'>6.8 SysF Create Train Object</td></tr><tr><td style='text-align: center;'>5.8 SysC: Control Switchable Trackside Assets</td><td style='text-align: center;'>6.2 SysF Authorise TA State Request 6.3 SysF Translate TA State request to TACS command 6.4 SysF Send TACS command</td></tr><tr><td style='text-align: center;'>5.9 SysC: Shutdown MBS</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>5.10 SysC: Update MBS Operational State</td><td style='text-align: center;'>6.5 SysF Update Domain Object state 6.7 SysF Assign a safe value to a Domain Object 6.9 SysF Localise Train 6.10 SysF Manage Unresolved Trackbound Object 6.18 SysF Update Movement Permission</td></tr><tr><td style='text-align: center;'>5.11 SysC: Report MBS Operational State</td><td style='text-align: center;'>6.1 SysF Report MBS Operational State</td></tr><tr><td style='text-align: center;'>5.12 SysC: Start of Train</td><td style='text-align: center;'>6.9 SysF Localise Train 6.16 SysF Request Movement Permission</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>5.13 SysC: Provide MA to Train</td><td style='text-align: center;'>6.11 SysF Authorise MP Request6.13 SysF Translate MP Request to Movement Authority</td></tr><tr><td style='text-align: center;'>5.14 SysC: Terminate Train Mission</td><td style='text-align: center;'>6.15 SysF Delete Train Object</td></tr><tr><td style='text-align: center;'>5.15 SysC: Revoke MA cooperatively by PE</td><td style='text-align: center;'>6.12 Authorise Cooperative Shortening Request6.14 SysF Translate Cooperative Shortening Request to Request to Shorten MA6.18 SysF Update Movement Permission</td></tr></table>

### 6.1 SysF Report MBS Operational State

#### 6.1.1 Overview

MBS Operational State for a given Domain Object Instance has to be reported to the PE.

#### 6.1.2 Inputs

• MBS Domain Object

#### 6.1.3 Outputs

• MBS Operational State report according to I_PE interface

---

# Contract No. HE – 101102001

#### 6.1.4 Functional requirements

## REQ-0001

When this function is triggered for a given MBS Domain Object Instance, MBS shall send the state of the MBS Domain Object instance (MBS Operational State) to PE according to I_PE.

Rationale: Update of (changed) information OR provision of information as result of the previous request to provide the state.

Guidance: None

Operational Rules: None

Engineering Rules: None

### 6.2 SysF Authorise TA State Request

#### 6.2.1 Overview

This function executes a series of safety checks on the received TA State Request.

The purpose of these Safety checks is to ensure that the requested state of the TA and the application of the corresponding TACS command by the MBS will not cause any hazards.

#### 6.2.2 Input

TA State Request message according to I_PE

- MBS Operational State

#### 6.2.3 Outputs

- Message “request granted” according to I_PE

- Message “request rejected” according to I_PE

---

#### 6.2.4 Functional requirements

## REQ-SAFETY

The MBS shall perform a series of checks in the sequence given by the following ordered list of requirement references when it receives a DPS Group Request through I_PE:

1. REQ-SC_SYNTAX

2. REQ-SC_DPSG_EXISTS



3. REQ-SC DPS EXISTS

4. REQ-SC DPS DPSG

5. REQ-SC_DPSG_REACHABLE

6. REQ- SC DPSG CHANGE

7. REQ-SC DPSG STATE

8. REQ-SC DPS TO

9. REQ-SC DPS UTO

10. REQ-SC DPS MP

11. REQ-SC DPS RB

12. REQ-SC DPS RP

Rationale: The purpose of these checks is to ensure that the requested state of the TA and the application of the corresponding TACS command by the MBS will not cause any hazards

Guidance: This is the head requirement for all safety checks.

Operational Rules: None

Engineering Rules: None

## REQ-0004

The MBS shall abort checking a DPS Group Request received through I_PE if any performed safety check failed.

Rationale: If a check for example discovers a message syntax error, further checks might lead to illegal function calls within MBS.

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-SC SYNTAX

---

If the syntax of the DPS Group Request message is not in accordance with the I_PE interface, MBS shall send a "SYNTAX" reject code.

Rationale: The MBS must be able to decode the request from PE.

Guidance: An invalid command syntax might lead to invalid state.

Operational Rules: None

Engineering Rules: None

## REQ-SC_DPSG_EXIST

MBS shall check that the DPS Group referenced in the DPS Group Request is known to MBS and if the check fails, MBS shall send a "DPS_UNKNOWN" reject code.

Rationale: The MBS must know the TA to be able to send a command to the corresponding TACS.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-SC DPS EXISTS

MBS shall check that every DPS referenced in the DPS Group Request is known to MBS and if the check fails, MBS shall send a "DPS UNKNOWN" reject code.

Rationale: The MBS must know the TA to be able to send a command to the corresponding TACS.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-SC DPS DPSG

MBS shall check that every DPS referenced in the DPS Group Request is associated with the DPS Group referenced in the DPS Group Request and if the check fails, MBS shall send a "DPS_UNKNOWN" reject code.

Rationale: A DPS that is referenced shall be part of a DPS Group, otherwise a check could be performed for a DPS on another DPS Group.

Guidance: None.

Operational Rules: None

Engineering Rules: None

REQ-SC_DPSG_REACHABLE

---

# Contract No. HE – 101102001

MBS shall check that the TACS associated with the DPS Group referenced in the DPS Group Request are connected to MBS and able to receive commands and if the check fails, MBS shall send a "DPS_GROUP_NOT_READY" reject code.

Rationale: The MBS must be in communication with the TACS to be able to send a command to the corresponding TACS.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ- SC DPSG CHANGE

MBS shall check that the DPS states in the DPS Group Request are different to the target states currently in the referenced DPS Group and if the check fails, MBS shall send a "DPS GROUP NO CHANGE" reject code

Rationale: MBS rejects the request if the DPSs are already in the state requested in the command. If all other safety checks would pass, MBS would set the reported state of all DPS to NONE and the DPS Group state to PROCESSING.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC_DPSG_STATE

MBS shall check that the combination of requested drivability states for each DPS referenced in the DPS Group Request matches one of the allowed combinations of the DPS Group and if the check fails, MBS shall send a "INVALID_COMBINATION" reject code.

Rationale: The MBS must be able to translate the state of the TA into a valid command for the corresponding TACS. The MBS checks that the requested state is

---

allowed for this TA by the Domain Data (see Drive Protection Section Group in System Pillar TCCS SD1 Data Model /SD1DM/).

Guidance: None.

/SD1DM/

Operational Rules: None

Engineering Rules: None

## REQ-SC DPS TO

MBS shall check that no DPS of the DPS Group referenced in the DPS Group Request overlaps with a Train Location of a Train Object and if the check fails, the MBS shall send a "DPS_OCCUPIED" reject code.

Rationale: To move a TA, it must be free for state change (not occupied by a train).

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//cc1a9920-99a0-4fda-b6a8-2df17e5bf91e/markdown_0/imgs/img_in_image_box_119_729_902_896.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A43Z%2F-1%2F%2F3b98339440683d97871af7b38e22ed0ca75dc389d25e369f85d5a650188f23a5" alt="Image" width="65%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC_DPS_UTO

MBS shall check that no DPS of the DPS Group referenced in the DPS Group Request overlaps with an Unresolved Trackbound Object and if the check fails, the MBS shall send a "DPS_OCCUPIED" reject code.

Rationale: To move a TA, it must be free for state change (not possibly occupied by a train).

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//cc1a9920-99a0-4fda-b6a8-2df17e5bf91e/markdown_0/imgs/img_in_image_box_115_1312_981_1478.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A43Z%2F-1%2F%2F667b10dea65ff45ae0e9b6de8f7a5e234d6aa7322c3bd0bedb95f589f26cb353" alt="Image" width="72%" /></div>


Operational Rules: None

Engineering Rules: None

---

# Contract No. HE – 101102001

## REQ-SC_DPS_MP

MBS shall check that no DPS of the DPS Group referenced in the DPS Group Request overlaps with a Movement Permission Extent and if the check fails, the MBS shall send a "DPS_LOCKED" reject code.

Rationale: To move a TA, it must not be allocated to any Movement Permission.

Guidance:

In the following figure, a Movement Permission overlaps a DPS of a DPS Group associated with the TA point, it is forbidden to move the point as this could cause a derailment. The same principle is also applied to other Trackside Asset types.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4b51a3d3-be9b-439a-81a0-af4565f51660/markdown_0/imgs/img_in_image_box_110_560_975_740.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A34%3A52Z%2F-1%2F%2F0d2f99d6ef7a7897d6cb7bd65b8e491bc42f5b5164dacafedd48811db5142938" alt="Image" width="72%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC DPS RB

MBS shall check that no DPS of the DPS Group referenced in the DPS Group Request overlaps with a Risk Buffer and if the check fails, the MBS shall send a "DPS_LOCKED" reject code.

Rationale: To move a TA, it must not be allocated to any Movement Permission or locked in Risk Buffer. This implies that swinging overlaps are currently not supported.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Risk Buffer</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Drive Protection Section</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>(FULL or NONE)</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

---

## REQ-SC AS RP

MBS shall check that no Risk Path is terminated on a DPS belonging to this TA according to REQ-SC_RP_TERM_DPS and if this check fails, MBS shall send a "DPS_SECURING_RISKPATH" rejected code.

Rationale: To move a TA, it must not be providing flank protection.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0005

If the DPS Group Request is not rejected, then MBS shall grant the request from PE to change the state of a Switchable TA and send the message "request granted" to PE.

Rationale: The request needs an answer to be sent to the PE.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0003

If the DPS Group Request is not rejected, then MBS shall set the currentDriveability for all associated DPS to NONE and the dpsGroupState to PROCESSING.

Rationale: When command is in progress, DPS driveability is set to a safe state (NONE) immediately after granting the request as this DPS cannot be used until the reported state is equal to the requested state.

Guidance: None.

Operational Rules: None

Engineering Rules: None

### 6.3 SysF Translate TA State request to TACS command

#### 6.3.1 Overview

The requested state of the abstracted Switchable TA is being translated into a specific command for the real trackside element controller (TACS).

---

#### 6.3.2 Inputs

Requested state of the Switchable TA.

#### 6.3.3 Outputs

TACS command according to I TACS

#### 6.3.4 Functional requirements

REQ-0006

If the request to change the state of a Switchable TA has been authorised, then MBS shall translate the request to a command to change the TA state to the requested one, according to the I_TACS interface.

Once the TA State Request has been successfully checked, this TA State Request is translated into a TACS command to be sent to the corresponding TACS.

Guidance: None

Operational Rules: None

Engineering Rules: None

### 6.4 SysF SEND TACS COMMAND

#### 6.4.1 Overview

When this function is triggered by a translated TACS command, it sends the corresponding message to the requested TACS according to the I TACS interface.

#### 6.4.2 Inputs

TACS command.

#### 6.4.3 Outputs

See I TACS.

---

# Contract No. HE – 101102001

#### 6.4.4 Functional requirements

## REQ-0007

If a TACS command is translated, MBS shall send this TACS command to the corresponding TACS according to the I_TACS interface.

Rationale: To be able to operate a Switchable TA.

Guidance: /ReqSubsP/

Operational Rules: None

Engineering Rules: None

### 6.5 SysF Update Domain Object State

#### 6.5.1 Overview

This function translates the TA and its state from a valid TACS report to the related Domain Object and updates its state.

Note: The state change of a Domain Object in case of communication loss is handled by the capability SysC: Update MBS Operational State.

#### 6.5.2 Input

• TACS report

• OBUCommLost, OBUCommEstablished

#### 6.5.3 Output

• Domain Object state

---

# Contract No. HE – 101102001

#### 6.5.4 Functional requirements

## REQ-0008

When a TACS report is received, MBS shall check the syntactical correctness of the message according to the I_TACS interface and if the check fails, the message shall be discarded.

Rationale: To be able to operate a Switchable TA.

Guidance: None

Operational Rules: None

Engineering Rules: None

Open point: check safety relevance (is discarding a safe measure?). Note: if a message is discarded at application layer, can the communication status still be considered

---

established or is it needed to be torn down as safety reaction? [SAFETY_ANALYSIS]

## REQ-0009

When a TACS report is decoded, MBS shall discard the message if this TACS does not exist in the Domain Objects.

Rationale: For a message received on a given communication channel, MBS should know the name of the TACS and the corresponding TACS type (e.g., Points, Level Crossing)

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0011

When a TACS report is decoded, MBS shall update the related Domain Object reported state according to the TACS report.

Rationale: Keep the MBS Operational state up to date.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0061

When a TACS report for a Switchable TA is received and no command is in progress (dpsGroupState is not PROCESSING), MBS shall update the DPS state according to the TACS report.

Rationale: Keep the MBS Operational state up to date. When no command is in progress, the reported state is always considered.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0062

When a TACS report for a Switchable TA is received and a command is in progress (dpsGroupState is PROCESSING), MBS shall update the DPS state according to the TACS report only if the reported state corresponds to the requested state.

Rationale: When a command is in progress, the DPS driveability is updated only if it corresponds to the requested state.

---

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0035

If a Switchable TA is now in the state requested, then MBS shall consider that a command is no more in progress and set (dpsGroupState to READY) for the corresponding Switchable TA.

Rationale: Once the TA is in the requested state, the command is no more in progress.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0094

When MBS detects that the safe connection with an OBU is lost or (re)established, MBS shall update the connection status of the corresponding Train Object.

Rationale: The connection status of OBU must be reported to other systems.

Guidance: None

Operational Rules: None

Engineering Rules: None

### 6.6 SysF Preload Topology Data

#### 6.6.1 Overview

With this function, MBS processes Topology Data received from DR (stores them, builds the Domain Objects within MBS).

#### 6.6.2 Input

• Topology Data from DR in message Domain Data

#### 6.6.3 Output

• Message Domain Data Request

• Message Domain Data Acknowledgement

---

# Contract No. HE – 101102001

#### 6.6.4 Functional requirements

REQ-0018

When MBS has no Topology Data, it shall send the message Domain Data Request according to I-DR to DR to get initial Topology Data. The parameter version is not used.

When MBS has Topology Data, it shall send the message Domain Data Request according to I-DR to DR to check if available Topology Data still are in the required version. The parameter version refers to the version of the existing data.

Rationale: None

Guidance: It is up to the implementation if MBS stores Topology Data persistently or not. If it does not store it, it would request Topology Data with every (re)start. If it stores Topology Data persistently, it has to assure while restoring them, that stored data have not been falsified.

Operational Rules: None

Engineering Rules: None

## REQ-0017

When MBS receives the message Domain Data from DR, MBS shall convert the received data into Domain Objects.

Upon successful conversion and storage, MBS shall send the message Domain Data Acknowledgement according to I_DR to DR with parameter preLoadingStatus == success.

Up to release 4: The Topology Data shall be considered active immediately and MBS be considered operational.

Rationale: None

Guidance: The correctness check covers for example the following aspects: Syntax, integrity, authenticity, version etc.

Operational Rules: None

Engineering Rules: None

## REQ-0019

When MBS receives the message Domain Data from DR, MBS shall convert the received data into Domain Object data.

Upon unsuccessful conversion and storage, MBS shall discard the data and send the message Domain Data Acknowledgement according to I_DR to DR with parameter preLoadingStatus == failure.

---

Rationale: None

Guidance: None

Operational Rules: None

Engineering Rules: None

### 6.7 SysF Assign A SAFE VALUE TO A DOMAIN OBJECT

#### 6.7.1 Overview

This function assigns a safe value to a Domain Object.

#### 6.7.2 Inputs

• Domain Object

#### 6.7.3 Outputs

• Domain Object State

#### 6.7.4 Functional requirements

## REQ-0020

When created, a Domain Object shall be initialised with a safe value. When MBS cannot receive an up-to-date information from the related real-world object, it shall set the Domain Object to a safe value.

Rationale: MBS must assume the safe value when it cannot know the real value.

Guidance: Setting the safe value is needed during MBS (re)start and when MBS detects that the communication session to the provider of the original information is lost.

The safe value for a switchable Trackside Asset is NONE for all related DPSs and OCCUPIED for a TVPS.

Operational Rules: None

Engineering Rules: None

## REQ-0028

When MBS starts up, the MBS shall create one or several Unresolved Trackbound Objects covering the complete AoC.

## Rationale:

This is to start with the most restrictive state.

Guidance:

To consider the AoC as unresolved, the MBS creates one or several Unresolved Trackbound Objects covering the complete AoC.

---

Operational Rules: None

Engineering Rules: None


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-0029</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TrackInit-2]</td></tr><tr><td colspan="3">The MBS shall utilise valid Stored Information to enable faster initialisation.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">Historic information on the state of the railway from before the MBS was restarted can enhance the Initialisation process.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">The location of all trains in communication prior to the restart, along with the extent of any MAs issued will be valuable information to be utilised.</td></tr><tr><td colspan="3">The validity of the information used must be carefully considered, as if the MBS has been offline for some time the State of the Railway is likely to have changed.</td></tr><tr><td colspan="3">Criteria for considering Stored information as valid are project dependent e.g. during MBS Initialisation, if the time passed is smaller than a configured value.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>ENG-TrackInit-1</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>REQ-0030</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TrackInit-3]</td></tr><tr><td colspan="3">The MBS shall, if configured, provide a means for the person responsible for the MBS Initialisation to confirm that the procedure is completed.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">If Stored Information is not valid, the person in charge of initialising the MBS has to confirm when the procedure is completed. They have the authority to confirm that all the obstacles on the railway are known to the MBS.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">If Stored information is used to initialise the MBS, this confirmation is not needed and it is project specific to implement it.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>OPE-TrackInit-4</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>ENG-TrackInit-2</td><td style='text-align: center;'></td></tr></table>

### 6.8 SysF Create Train Object

#### 6.8.1 Overview

When MBS has successfully established a communication session with an OBU, then a Train Object for this OBU is established in the MBS. This Train Object subsequently covers all train-related information (e.g. Train Data, Train Location, etc.) as soon as this information is available.

---

#### 6.8.2 Inputs

Successfully established communication session between MBS and an OBU

#### 6.8.3 Outputs

Train Object

#### 6.8.4 Functional requirements

## REQ-CreateTrain-0001

As soon as there is an established communication session between MBS and an OBU, the MBS creates a Train Object for this OBU.

Rationale: None

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-2

The MBS shall store a Train Object for all communicating trains within its Area of Control. When available, the following information shall be stored:

1. Train ID (NID_ENGINE)

2. Train Data (including L TRAIN)

3. Most recent Train Position Report information

4. Train Location (when determined)

5. Time when the stored information was last valid

6. Train Running Number

## Rationale:

This ensures that MBS has an up-to-date image of all train-related information. Most recent Train Position report information is used to e.g. store detailed position information (e.g. mSFE).

## Guidance:

The time when the stored information was last valid is required in order to enable the possible use of the stored information during Trackside Initialisation.

Operational Rules: None

Engineering Rules: None

---

### 6.9 SysF Localise Train

#### 6.9.1 Overview

This function localises a communicating train within the Area of Control. The Train Location information is stored in the Train Object.

Within the MBS, the Train Location for a train is the MBS interpretation of the location of the train, based on Train Position Reports, Validated Train Data and other inputs if available, e.g. TTD sections.

A Train Location has a front and a rear:

The front of the Train Location is the MBS view of the furthest position for the front of the train, based on Train Position Reports and other inputs, e.g. TTD sections.

The rear of the Train Location is the MBS view of the furthest position for the rear of the train, based on Train Position Reports, Validated Train Data, and other inputs, e.g. TTDs.

The different terms used within this section to determine a Train Location are summarised in Figure 21.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0e0122c7-d40c-4b4e-8cba-975ea7a63d98/markdown_0/imgs/img_in_image_box_184_768_1044_1171.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A35%3A43Z%2F-1%2F%2F289387f352e55e5d833cf57b68c19699f13e30e060dc0b2211dec6eb93013364" alt="Image" width="72%" /></div>


<div style="text-align: center;">Figure 21: Terms used for Train Location</div>


<div style="text-align: center;">There are several reasons to create or move a Train Location, as shown in Table 10:</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Create-move Train Location Reasons</td><td style='text-align: center;'>Notes</td><td style='text-align: center;'>Requirements</td></tr><tr><td style='text-align: center;'>Train SoM position report received</td><td style='text-align: center;'>Train location created from min Safe Front End to max Safe Front End (before having received train data)</td><td style='text-align: center;'>REQ-TrainLoc-4</td></tr><tr><td style='text-align: center;'>First Train Position Report</td><td style='text-align: center;'>For example, PR without SoM process</td><td style='text-align: center;'>REQ-TrainLoc-5</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Update front by Train Max SFE</td><td style='text-align: center;'>Front of the Train Location is updated using Max Safe Front End derived from the Train Position Report</td><td style='text-align: center;'>REQ-TrainLoc-7</td></tr><tr><td style='text-align: center;'>Update rear by Train CRE</td><td style='text-align: center;'>Rear of the Train Location is updated using the Confirmed Rear End derived from the Train Position Report</td><td style='text-align: center;'>REQ-TrainLoc-8REQ-TrainLoc-9</td></tr><tr><td style='text-align: center;'>Update rear with new value of Train Length</td><td style='text-align: center;'>Rear of the Train Location is updated using the new value of Train Length</td><td style='text-align: center;'>REQ-TrainLoc-6</td></tr><tr><td style='text-align: center;'>Update front by clear TTD</td><td style='text-align: center;'>Front of the Train Location is shortened using clear TTD section</td><td style='text-align: center;'>REQ-TTD-2REQ-TTD-4</td></tr><tr><td style='text-align: center;'>Update rear by clear TTD</td><td style='text-align: center;'>Rear of the Train Location is shortened using clear TTD</td><td style='text-align: center;'>REQ-TTD-3REQ-TTD-4</td></tr><tr><td style='text-align: center;'>Update front by occupied TTD for mute train</td><td style='text-align: center;'>Update front of the Train Location when a TTD becomes occupied for a mute train</td><td style='text-align: center;'>REQ-TTD-5</td></tr></table>

Table 10 – Reasons to create or move Train Location

There are several reasons to delete a Train Location, as shown in Table 11:


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Delete Train Location Reasons</td><td style='text-align: center;'>Notes</td><td style='text-align: center;'>Requirements</td></tr><tr><td style='text-align: center;'>Train is no longer in communication</td><td style='text-align: center;'>MBS considers that a train is no longer in communication</td><td style='text-align: center;'>REQ-TrainLoc-10 REQ-0040</td></tr></table>

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

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2f0aba58-9407-4e1c-9fa4-acd9923fe361/markdown_0/imgs/img_in_image_box_307_1120_939_1364.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A35%3A56Z%2F-1%2F%2Fa91af2761cdafbc23ab9b675641df38e34e1332cddf5774864e226f8460e08b6" alt="Image" width="53%" /></div>


<div style="text-align: center;">Figure 22: Train Location from Start of Mission Train Position Report</div>


In Figure 22, the Train Object is shown with Train Integrity not confirmed. Train integrity cannot be confirmed until Validated Train Data has been acknowledged by the MBS.

How a Train Location which is partially outside the Area of Control is processed will be project specific.

---

There are other requirements (e.g. REQ-TMS-1) covering the situations when the reported location is invalid or unknown, or is valid but ambiguous to the MBS.

Operational Rules: None

Engineering Rules: None


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-TMS-1</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TMS-1]</td></tr><tr><td colspan="3">The TMS shall provide means for a Signaller to assign a position to a train that is reporting a position during Start of Mission which is unknown or invalid, or a position which the MBS considers ambiguous.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">This is to allow the MBS to locate a train in its Area of Control after a specific operational procedure.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">How the Signaller enters the position of a train in the TMS is project specific, but the MBS cannot accept a position in a clear area of track.</td></tr><tr><td colspan="3">The Signaller may need to contact the Driver to determine an estimated location for the train.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>OPE-SoM-4</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr></table>

#### 6.9.6 Requirements to update a Train Location

## REQ-TrainLoc-7

When receiving a Train Position Report from a train and the position is not ambiguous to the MBS, the MBS shall update the front of the Train Location for this train using the Max Safe Front End derived from the Train Position Report

## Rationale:

The MBS uses the information in Train Position Reports to update the Train Location of trains in its area.

## Guidance:

The front of the Train Location for a train can be updated with every position report received, including trains in RV mode, if the position is known to the MBS.

Figure 23 shows how the front of the Train Location is updated with a new train position report.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ecc25591-8c68-49c7-bf26-971a6172aba0/markdown_0/imgs/img_in_image_box_328_174_947_586.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A04Z%2F-1%2F%2Fa8a8f4196d5eaf8291b6d19452a78450c563438a8c695dab9efd4142a67e8ac6" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 23: Front of Train Location updated from new Train Position Report</div>


Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-8

When receiving a Train Position Report from a train where:

- the position is not ambiguous to the MBS. AND

• there is a Train Location for that train. AND

• the train is in FS, OS or SB, AND

• Train Integrity is confirmed by external source.

then the MBS shall update the rear of the Train Location for this train using the Confirmed Rear End derived from the Train Position Report.

## Rationale:

The MBS uses the information in Train Position Reports to maintain the Train Location of trains in its Area of Control.

## Guidance:

The Confirmed Rear End is only known when receiving a Train Position Report with the Train Integrity confirmed. From the ladder the MBS can locate the confirmed rear end of the train.

Figure 24 shows how the CRE is updated with a new train position report with Train Integrity Confirmed.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//118a4aa2-41eb-40eb-ac87-eea7ff874103/markdown_0/imgs/img_in_image_box_366_194_898_400.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A08Z%2F-1%2F%2F9be5065bf30e1d06e7f6445f869cdb9b257efe8c597f35d4b047792633c6e3af" alt="Image" width="44%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//118a4aa2-41eb-40eb-ac87-eea7ff874103/markdown_0/imgs/img_in_image_box_360_535_895_749.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A08Z%2F-1%2F%2F9773ff1b3a809cec643a864b4a66126352ba4916d2a691d6dc0adbcb9ce2f78f" alt="Image" width="44%" /></div>


<div style="text-align: center;">Figure 24: Rear of Train Location updated from new Train Position Report, Integrity Confirmed</div>


Train Position Reports from trains in FS and OS will be from trains where linking is used. Train Position Reports from trains in SB allow for defining a Train Location at Start of Mission. Other modes, including SR, are excluded as there are issues with relocation.

Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-9

When receiving a Train Position Report from a train where:

- the position is known to the MBS. AND

• there is a Train Location for that train. AND

• the train is in FS, OS or SB, AND

• Train Integrity is confirmed by Driver, AND

- the MBS is configured to accept Train Integrity confirmed by Driver,

then the MBS shall update the rear of the Train Location for this train using the Confirmed Rear End derived from the Train Position Report.

---

# Contract No. HE – 101102001

## Rationale:

The MBS uses the information in Train Position Reports to update the Train Location of trains in its Area of Control.

## Guidance:

The Confirmed Rear End is only known when receiving a Train Position Report with Train Integrity confirmed from which the MBS can locate the rear of the train.

If Train Integrity is confirmed by the driver, then the Train Location is only updated if the MBS is configured to accept this.

Train Position Reports from trains in FS and OS will be from trains where linking is used. Train Position Reports from trains in SB allow for defining a Train Location at Start of Mission. Other modes, including SR, are excluded as there are issues with relocation.

Operational Rules: OPE-Generic-3

Engineering Rules: ENG-LossTI-2

## REQ-TrainLoc-6

When receiving a new value of Train Length in Validated Train Data from a train, the MBS shall update the Rear End of the Train Location for this train using the new value of Train Length.

## Rationale:

The receipt of a new value of Train Length in Validated Train Data represents new information from the train, which must be used to update the Train Location.

## Guidance:

The only information used from the Validated Train Data to determine Train Location is the train length ( $ L_{TRAIN} $ ).

A new value of L_TRAIN means either the first value received since the Train Location was created, or a changed value received at some later time.

If this is the first value for L_TRAIN received since the Train Location was created, then the Train Location is extended as shown in Figure 25.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ea2a01a5-6c6b-462c-a1c5-effbbe2909a0/markdown_0/imgs/img_in_image_box_357_163_890_703.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A16Z%2F-1%2F%2Ff67b3dfceef096d472fbc2cb9740935111dada5fba829617f75a71462fd6bf68" alt="Image" width="44%" /></div>


<div style="text-align: center;">Figure 25: Train Location when receiving Validated Train Data during Start of Mission</div>


If this is a changed value of L_TRAIN, then the new value of L_TRAIN could be shorter than the previous value, for example after Splitting, as shown in Figure 26. In this case, a UTO is also created according to requirement REQ-TrackStatus-25 to manage the missing part.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ea2a01a5-6c6b-462c-a1c5-effbbe2909a0/markdown_0/imgs/img_in_image_box_369_918_891_1492.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A16Z%2F-1%2F%2F16592884a722bfbc578cb7f52b91486e7ac65e27889d209baa6bde6b3d76e40d" alt="Image" width="43%" /></div>


<div style="text-align: center;">Figure 26: Train Location when receiving Validated Train Data, L_TRAIN decreased</div>

---

If this is a changed value of  $ L_{TRAIN} $ , then the new value of  $ L_{TRAIN} $  could be longer than the previous value, for example after Joining, as shown in Figure 27.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4fc4a1da-429e-43ab-826e-d16e8cefe7ba/markdown_0/imgs/img_in_image_box_234_248_1027_799.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A19Z%2F-1%2F%2F8e04efdf649e2e426ed8427981362b9f73b380011c249429b577fb1a1d8aaec8" alt="Image" width="66%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4fc4a1da-429e-43ab-826e-d16e8cefe7ba/markdown_0/imgs/img_in_image_box_232_822_1018_1157.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A19Z%2F-1%2F%2Fc97b80ceec88006e1640590b49265d9c72d19586f975438a7e43f375193d2a71" alt="Image" width="65%" /></div>


<div style="text-align: center;">Figure 27: Train Location when receiving Validated Train Data, L TRAIN increased</div>


If the new Train Location extends outside the Area of Control, the handling is not managed in the current release.

Operational Rules: None

Engineering Rules: None

---

<div style="text-align: center;">6.9.7 Reaction to Unexpected Train Locations – FOR FURTHER RELEASE</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">FOR FURTHER RELEASE [X2R5 REQ-TrainLoc-12]</td></tr><tr><td colspan="2">If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall react to transition the system to a safe state.</td></tr><tr><td colspan="2">Rationale:</td></tr><tr><td colspan="2">The MBS is reliant upon trains reporting their position to separate traffic safely and the MBS must therefore react if it detects a potentially hazardous situation.</td></tr><tr><td colspan="2">Guidance:</td></tr><tr><td colspan="2">A train reporting an unexpected position can be a hazard even when there is TTD if more than one train is in the same TTD section, but the situation is more severe in an area without TTD.</td></tr><tr><td colspan="2">The MBS will only be able to detect conflicts with other train movements which have been authorised by the MBS.</td></tr><tr><td colspan="2">There are several situations where a position report from a train may require immediate action from the MBS to avoid a potential hazard, for example:</td></tr><tr><td colspan="2">a train reporting a position in an area previously considered clear, e.g. at Start of Mission, OR</td></tr><tr><td colspan="2">a train which has been allocated a Reserved Status Area reporting a position which cannot be linked with that Reserved Status Area, OR</td></tr><tr><td colspan="2">a train reporting a position locating it within a Reserved Status Area allocated to another train.</td></tr><tr><td colspan="2">The specific reaction applied will depend on the situation and application specific requirements. Possible reactions include:</td></tr><tr><td colspan="2">shortening of the Movement Authority for the affected train(s),</td></tr><tr><td colspan="2">sending an Unconditional Emergency Stop message to the affected train(s).</td></tr><tr><td colspan="2">Note that the Train Location is created or updated by other requirements.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>EQ-TrainLoc-13</td><td style='text-align: center;'>FOR FURTHER RELEASE [X2R5 REQ-TrainLoc-13]</td></tr><tr><td colspan="2">If a train reports a position that is unexpected or in conflict with other train movements, the MBS shall alert the PE to the situation.</td></tr></table>

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

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//95101e10-088a-4402-93ff-1b4a24ffe3a3/markdown_0/imgs/img_in_image_box_156_277_1126_835.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A36Z%2F-1%2F%2F80b61aae5cc0da56c9a5d066f7a0867a13d5d0de34ec5e4b9161445c21069132" alt="Image" width="81%" /></div>


<div style="text-align: center;">Figure 28: Shortening of front of Train Location due to clear TTD</div>


Figure 29 shows the situation where the min Safe Front End is reported within the same Clear TTD as the Max Safe Front End, and therefore no shortening:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//95101e10-088a-4402-93ff-1b4a24ffe3a3/markdown_0/imgs/img_in_image_box_162_986_1077_1096.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A36Z%2F-1%2F%2F14860d33e285e28bbc33ac6a13b9cae49aa7e170422fa257830dbb0a9298eb7c" alt="Image" width="76%" /></div>


<div style="text-align: center;">Figure 29: No shortening of front of Train Location due to clear TTD</div>


Operational Rules: None

Engineering Rules: ENG-Generic-4

## REQ-TTD-3

For a system using TTD, if the Rear End of the Train Location is located in a clear TTD section while the Max Safe Rear End is not in this TTD section, then the MBS shall shorten the rear of the Train Location for this train, by the extent of each TTD section that is Clear between the Rear End of the Train Location and Max Safe Rear End.

---

## Rationale:

TTD information can be used to improve the MBS knowledge about the status of the track in the Area of Control, thus improving the performance of the system.

## Guidance:

The effect of the Clear TTD section in the rear part of the Train Location is to update the rear of the Train Location.

This could be used to release points and level crossings faster. Both the reception of TTD section status and the receiving of a Train Position Report can be the trigger for updating the Train Location.

Care must be taken to allow for the overhang of vehicles at the boundary between an occupied and a clear TTD section.

A clear TTD section in rear of a train can shorten the rear part of the Train Location of the train, as shown in Figure 30:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//16512fd6-c748-4875-ad59-7b56a38bf1f1/markdown_0/imgs/img_in_image_box_196_678_1059_1144.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A40Z%2F-1%2F%2F4d5d6f2d313b1130636eedf3fa09d2995b64f19645e19d8ddad720c532dab5f8" alt="Image" width="72%" /></div>


<div style="text-align: center;">Figure 30: Shortening of rear of Train Location due to clear TTD</div>


Figure 31 shows the situation where the Max Safe Rear End is reported within the same Clear TTD section as the Min Safe Rear End, and there is no shortening:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//16512fd6-c748-4875-ad59-7b56a38bf1f1/markdown_0/imgs/img_in_image_box_247_1286_1009_1490.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A40Z%2F-1%2F%2Fed4c40846bcf85bc8bccd8943ddb5e561d7891c95c87ce4006d7e2d2ac0e79fb" alt="Image" width="63%" /></div>


<div style="text-align: center;">Figure 31: No shortening of rear of Train Location due to clear TTD</div>


Operational Rules: None

---

Engineering Rules: ENG-Generic-4


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">FOR FURTHER RELEASE [X2R5 REQ-TTD-4]</td></tr><tr><td colspan="3">For a system using TTD, when using Clear TTD sections to shorten a Train Location, the MBS shall ensure that the length of the reduced Train Location is not shorter than the length of the train.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">Applying shortening should not result in the extent of the remaining Train Location being less than the length of the train.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">If the application of shortening the Train Location results in the length of the Train Location being less than the length of the train, it is project specific what alternative action the MBS takes. For example, an application may decide to not apply any shortening to the Train Location, or to apply equal shortening to the front and rear.</td></tr><tr><td colspan="3">At boundaries, projects might decide to truncate the Train Location and as a result, Train Location could be shorter than length of the train.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>EQ-TTD-5</td><td colspan="2">FOR FURTHER RELEASE [X2R5 REQ-TTD-5]</td></tr><tr><td colspan="3">For a system using TTD, when detecting an expected TTD occupancy within the Movement Permission allocated to a train, after its Mute Timer has expired, the MBS shall extend the Train Location of the train up to the closest of:</td></tr><tr><td colspan="3">• the end of the Movement Permission&#x27;s Risk Buffer, OR</td></tr><tr><td colspan="3">• the next boundary of this Occupied TTD section</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">The MBS can use TTD occupation to extend the Train Location of a train where the Mute Timer has expired and is moving along the railway within the Movement Permission allocated to it, thus maintaining the link between the Train Location and the train, thereby facilitating recovery if communication is re-established.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">A train where the Mute Timer has expired can move forward within the Movement Permission allocated to that train and occupy a previously clear TTD. That occupation can be attributed to a normal train movement. The MBS can adjust the knowledge about where the train might be by extending the Train Location of this train.</td></tr></table>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2596f07a-e0e5-40e7-9d9a-b7e5bee4701e/markdown_0/imgs/img_in_image_box_73_162_1167_1517.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A47Z%2F-1%2F%2F32fda111f4e3c9b69c04954097e42412e411656440fd68d2cb2573d5306c1f86" alt="Image" width="91%" /></div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-0037</td><td style='text-align: center;'>FOR FURTHER RELEASE [X2R5 REQ- LossComms-1]</td></tr><tr><td style='text-align: center;'>The MBS shall, if configured, for each train with which it has an active communication session supervise a defined timeout (a Mute Timer) after which the communication with this train is considered lost. Rationale: This is to enable the MBS to react faster to the potential loss of communication with an OBU than the timeout in the ETCS specifications. The ETCS specification timer of 5 minutes might be considered too long for some ETCS Level 3 systems. Guidance: This Requirement is mandatory if the Mute timer is used. This is an optional functionality to be defined at application level based on the needs of the system. The value of the Mute timer will be longer than the variable T_NVCONTACT and shorter than the communication session expiry, as defined in [SS026]. Operational Rules: Engineering Rules:</td><td style='text-align: center;'>FOR FURTHER RELEASE [X2R5 REQ-LossComms-2]</td></tr><tr><td style='text-align: center;'>When receiving a message from a train and if the use of a Mute Timer is configured, the MBS shall (re-)start the Mute Timer for this train. Rationale: This is for the MBS to be able to react if a message from the train is not received within a configured time. Guidance: This Requirement is mandatory if the Mute timer is used. If a Mute Timer is configured it is only active when there is a communication session with the train. Operational Rules: Engineering Rules:</td><td style='text-align: center;'>FOR FURTHER RELEASE [X2R5 REQ-LossComms-3]</td></tr><tr><td style='text-align: center;'>When the Mute Timer expires for a train which has not entered an announced Radio Hole, and which was not reporting in RV mode, then the MBS shall convert the Train Object into an Unresolved Trackbound Object. The Unresolved Trackbound Object area shall correspond to the Train Location extended to the end of the Movement Permission or the end of the MA, whichever is shorter.</td><td style='text-align: center;'></td></tr></table>

---

## Rationale:

This is the area where the non-communicating train could be located, and as such needs to be protected.

## Guidance:

This Requirement is mandatory if the Mute timer is used.

If the extent of the MA sent to the train is less than the Movement Permission, then the extension of the Unresolved Trackbound Object may only be to the end of the MA sent to the train.

The criteria for establishing whether a train has entered a Radio Hole are project specific and could include the train having received radio hole track condition information from the MBS.

Once a train is reporting in RV mode, it is not able to move forwards without performing EoM. Start of Mission, so it is not necessary to extend the Unresolved Trackbound Object to the end of the Reserved Status Area or MA.

The MBS will maintain the communication session with OBU as active even when the Mute timer has expired until the maximum time to maintain a communication session as specified in SUBSET-026 [BL3 R2] has elapsed.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2e5d2d08-f090-47a5-9777-44ff6b6d7b1a/markdown_0/imgs/img_in_image_box_101_840_1118_1553.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A36%3A55Z%2F-1%2F%2Fb32d42300be2750e889f8536bde5129813ed766aec8d7f98b23fa29958bdf969" alt="Image" width="85%" /></div>


Engineering Rules: None

---

6.9.9 Requirements to delete Train Location and to create Unresolved Trackbound Object


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>EQ-0036</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-EoM-4]</td></tr><tr><td colspan="3">The MBS shall be able to cope with differences in the confidence interval provided in the position report of a train that reported EoM even when related to the same train position. Rationale:</td></tr><tr><td colspan="3">This is due to an ambiguity in the ETCS specifications around how to calculate the Train Location accuracy when linking information is deleted due to the change to SB mode. See REQ-EoM-4</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">This issue is the subject of CR1318 in the ERA CCM Process [CRProcess]. The MBS must be able to deal with On-boards which have not applied the solution to CR1318. Operational Rules: None Engineering Rules: None</td></tr><tr><td style='text-align: center;'>EQ-0040</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-LossComms-4]</td></tr><tr><td colspan="3">If the Mute Timer is not considered for use on a particular application, the MBS shall react when the session timer expires by converting the Train Object into an Unresolved Trackbound Object. The Unresolved Trackbound Object shall correspond to the Train Location extended to the end of the Movement Permission, except if the train was reporting in RV mode. Rationale:</td></tr><tr><td colspan="3">This is so that, even for applications not utilising the Mute timer functionality, the Trackside is protected when communications with a train expire according to the existing session expiry timer in the ETCS specifications [BL3 R2].</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">Whether or not to use the Mute Timer will depend on whether it is required to detect loss of communication before expiry of the session timer. This in turn will depend on traffic density and the typical speed of trains. Once a train is reporting in RV mode, it is not able to move forwards without performing EoM and Start of Mission, so it is not necessary to extend the Unresolved Trackbound Object to the end of the Movement Permission.</td></tr></table>

---

For a system using TTD, there may be clear TTDs ahead of the train within the Movement Permission. In this case, the Unresolved Trackbound Object can be extended to the least distant position of the next TTD that is clear. This is equivalent to extending the Unresolved Trackbound Object up to the end of the MA, in accordance with this requirement, and then clearing those parts in accordance with TTD requirements.

Important note: this requirement assumes that the train is at standstill (or low speed) when the session timer expires.

Operational Rules: None

Engineering Rules: None

/ETCS/

#### 6.9.10 Requirements for train integrity

## REQ-0027

When receiving a position report from a train with the information 'Train Integrity is confirmed by External Source', then the MBS shall mark the Train Object associated to this train as "integrity confirmed".

## Rationale:

When the train is confirmed by External Source, the information about train integrity for the Train Object needs to be updated.

Guidance:

None.

Operational Rules: None

Engineering Rules: None

## REQ-LossTI-2

When receiving a position report from a train with the information ‘Train integrity lost’, the MBS shall mark the Train Object associated with this train as “integrity not confirmed”.

## Rationale:

In this situation, the status for the Train Location of the train changes to integrity not confirmed, while the extent of the Train Location is updated by other requirements, changing the front end from the information in the position report while the rear end is maintained.

Guidance:

None

Operational Rules: None

---

# Contract No. HE – 101102001

Engineering Rules: None

## REQ-LossTI-7

If the MBS receives Validated Train Data for a train with a train length different from previously reported within the same communication session, then the MBS shall mark the Train Object as “integrity not confirmed”.

## Rationale:

If the train reports loss of Train Integrity because of joining or splitting, then this will already result in the Train Object marked as “integrity not confirmed”. This requirement is to cover the situation where the new train length is received before the loss of Train Integrity.

## Guidance:

When new train data is entered, the OBU will not confirm Train Integrity until the new train data is acknowledged by the MBS. This behaviour is as defined in Change Request 940 [CR940].

Operational Rules: None

Engineering Rules: None

## REQ-LossTI-4

The MBS shall mark the Train Object as “integrity not confirmed” when ‘No train integrity information’ is reported longer than a configurable time (Integrity Wait Timer).

## Rationale:

This is to provide to other consumers entity as PE the information about the train integrity.

## Guidance:

Once Train Integrity is considered Lost by the MBS, the mechanism in REQ-LossTI-2 is applied.

It is application specific whether to implement this function. The timer will have a special value that means the function is disabled.

Note that using this timer the Driver will not be aware of the train Integrity being treated as Lost by the MBS and as such cannot be expected to react in any manner.

If the MBS is configured not to accept Train Integrity confirmed by Driver, and Train Integrity confirmed by Driver is reported, then the MBS will treat this as “No train integrity information”.

There is no specific relation between the length of the Mute Timer and the Integrity Wait timer.

Operational Rules: None

---

# Contract No. HE – 101102001

Engineering Rules: ENG-LossTI-1

## REQ-LossTI-5

When the Integrity Wait Timer is configured, the MBS shall start/restart it with every message from the train with the information 'Train integrity confirmed by external source'.

Rationale:

This is for the MBS to implement an appropriate reaction in case a train does not send a position report with integrity confirmed by external source within the configured time.

Guidance:

The MBS does not start/restart the Integrity Wait Timer when driver confirms integrity. It is application specific whether to implement the Integrity Wait Timer.

Operational Rules: None

Engineering Rules: ENG-LossTI-1

### 6.10 SysF MANAGE UNRESOLVED TRACKBOUND OBJECT

#### 6.10.1 Overview

The MBS must be aware of all parts of the track that are potentially occupied.

- For communicating trains that are localised, the occupancy is managed by the Train Location inside Train Object. The MBS will create and update a Train Object for each communicating train.

- For all other situations, the (potential) occupancy is managed by Unresolved Trackbound Object. The MBS will create and update Unresolved Trackbound Object in these cases.

An Unresolved Trackbound Object may exist for a specific train, but may also exist for another reason, not associated with a specific train.

There are several reasons to create or extend an Unresolved Trackbound Object, as shown in Table 12:


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Unresolved Trackbound Object Reasons</td><td style='text-align: center;'>Notes</td><td style='text-align: center;'>Requirements</td></tr><tr><td style='text-align: center;'>Reporting train with a shorter value of L_TRAIN</td><td style='text-align: center;'>MBS is receiving Train Position Reports, and has also received a new shorter value of L_TRAIN (splitting is assumed). A new UTO is created for the missing length</td><td style='text-align: center;'>REQ-TrackStatus-25, REQ-TrackStatus-10</td></tr><tr><td style='text-align: center;'>Train is no longer in communication</td><td style='text-align: center;'>MBS considers that a train is no longer in communication</td><td style='text-align: center;'>REQ-TrainLoc-10 REQ-0040</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Unresolved Trackbound Object Reasons</td><td style='text-align: center;'>Notes</td><td style='text-align: center;'>Requirements</td></tr><tr><td style='text-align: center;'>Unresolved Trackbound Object created by MBS at Initialisation</td><td style='text-align: center;'>At initialisation of the MBS, the status of the complete Area of Control is unknown</td><td style='text-align: center;'>REQ-0028</td></tr><tr><td style='text-align: center;'>Unexpected TTD section occupancy</td><td style='text-align: center;'>A TTD section is unexpectedly Occupied</td><td style='text-align: center;'>REQ-TTD-9, REQ-TTD-10</td></tr><tr><td style='text-align: center;'>Unexpected TTD section clearance</td><td style='text-align: center;'>A TTD section is unexpectedly Cleared</td><td style='text-align: center;'>REQ-TTD-12</td></tr><tr><td style='text-align: center;'>UTO propagation</td><td style='text-align: center;'>UTO is propagated until the TTD limit or until Train Location limit.</td><td style='text-align: center;'>REQ-TrainLoc-14, REQ-TrainLoc-15, REQ-TrainLoc-16, REQ-TrainLoc-17</td></tr></table>

Table 12 – Reasons to create or extend Unresolved Trackbound Object

There are several reasons to remove (even partly) an Unresolved Trackbound Object, as shown in Table 13:


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Unresolved Trackbound Object Reasons</td><td style='text-align: center;'>Notes</td><td style='text-align: center;'>Requirements</td></tr><tr><td style='text-align: center;'>UTO is replaced by Train Location</td><td style='text-align: center;'>UTO is removed when it is replaced by the Train Location of a (newly) connected train. This is performed if the total recorded length of the UTOs to be replaced is matching the length (L_TRAIN) of the connected train</td><td style='text-align: center;'>REQ-TrackStatus-9</td></tr><tr><td style='text-align: center;'>UTO is shortened by Train Location</td><td style='text-align: center;'>UTO is shortened when it is partly replaced by the Train Location of a (newly) connected train. This is performed if the recorded length of the UTO is greater than the length of the connected train.</td><td style='text-align: center;'>REQ-TrackStatus-10</td></tr><tr><td style='text-align: center;'>Sweeping UTO under the train</td><td style='text-align: center;'>Remove the part of UTO between the min Safe Front End to the Max Safe Rear End of the train, i.e. under the train</td><td style='text-align: center;'>REQ-TrackStatus-12 REQ-TrackStatus-15</td></tr><tr><td style='text-align: center;'>Sweeping UTO by train front</td><td style='text-align: center;'>Remove the part of UTO from the previous min Safe Front End up to the new min Safe Front End of the train</td><td style='text-align: center;'>REQ-TrackStatus-14</td></tr><tr><td style='text-align: center;'>Remaining UTO is too small</td><td style='text-align: center;'>Remove UTO for which the extent is less than a configurable minimum length</td><td style='text-align: center;'>REQ-TrackStatus-19 REQ-TTD-8</td></tr><tr><td style='text-align: center;'>Removed by clear TTD</td><td style='text-align: center;'>Remove all or part of UTO corresponding to a TTD section which is clear</td><td style='text-align: center;'>REQ-TTD-7</td></tr></table>

Table 13 – Reasons to remove (even partly) Unresolved Trackbound Object

---

# Contract No. HE – 101102001

#### 6.10.2 Propagation concept

The concept of propagation is based on the idea that an Unresolved Trackbound Object needs to be increased, possibly after a period of time, to allow for the fact that any railway vehicles in the Unresolved Trackbound Object area may move without knowledge of the MBS.

Within a signalling system with 100% Trackside Train Detection (TTD), any movement which crosses a TTD boundary is likely to be detected (see REQ-TTD-9, REQ-TTD-10, REQ-TTD-12).

In case of loss of communication, the Movement Permission is also considered as a possible envelope for movements of non-reporting vehicles (see REQ-TrainLoc-10).

Without TTD or if the TTD is already occupied, movements of non-reporting rail vehicles will not be detected by the MBS.

For stationary vehicles, the period of time before propagation is applied could be associated with the length of time for which railway vehicle brakes can be expected to remain active, and so keep the vehicle(s) stationary.

Measures are generally put in place at railway project level to prevent or detect and mitigate the risk of rolling vehicles moving such that they conflict with other movements:

• Use of trap points or derailers in station areas and/or sidings

• Use of Trackside Train Detection in station areas and/or sidings

If hazard analysis on a particular railway identifies that the remaining risk of unexpected vehicle movement causing a collision is still not acceptable, MBS includes a propagation algorithm within TTD (see REQ-TrainLoc-14, REQ-TrainLoc-15 and REQ-TrainLoc-16) to mitigate this risk.

#### 6.10.3 Storage requirements


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-TrackStatus-26</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TrackStatus-26]</td></tr><tr><td colspan="3">If an Unresolved Trackbound Object is created that is within a Movement Permission allocated to a train, then the MBS shall react to transition the system to a safe state.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">A new Unresolved Trackbound Object within a Movement Permission allocated to a train may require urgent action from the MBS in order to avoid a hazard.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">The specific reaction applied will depend on the scenario and application specific requirements. Possible reactions include shortening of the Movement Authority for another train; sending an Unconditional Emergency Stop to one or multiple trains etc.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr></table>

---

## REQ-TrackStatus-27

The MBS shall store and update data for each Unresolved Trackbound Object within its Area of Control in accordance with the following table:


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Data item</td><td style='text-align: center;'>Type or Possible Values</td><td style='text-align: center;'>Notes</td></tr><tr><td style='text-align: center;'>Extent</td><td style='text-align: center;'>Definition of the extent of the Unresolved Trackbound Object</td><td style='text-align: center;'>The extent of the Unresolved Trackbound Object.</td></tr><tr><td style='text-align: center;'>Recorded Train Length</td><td style='text-align: center;'>As for L_TRAIN</td><td style='text-align: center;'>The length of train associated with this Unresolved Trackbound Object, if any. Note: this length is not the same as the extent of the UTO.</td></tr><tr><td style='text-align: center;'>Train ID</td><td style='text-align: center;'>As for NID_ENGINE</td><td style='text-align: center;'>The NID_ENGINE of the train associated with this UTO, if any.</td></tr><tr><td style='text-align: center;'>Reason</td><td style='text-align: center;'>From enumerated list see Table 12.</td><td style='text-align: center;'>The reason why the UTO was created. There might be more than one reason.</td></tr></table>

Table 14 – Unresolved Trackbound Object Stored Data

## Rationale:

The Stored Data will be used by recovery mechanisms, for example at Start of Mission, recovery after loss of communication, etc.

Stored Information can also aid with initialising the MBS after a restart.

## Guidance:

The Train ID stored will be the NID_ENGINE of the train associated with the Unresolved Trackbound Object, if any.

There may be more than one reason for an Unresolved Trackbound Object.

Stored Data for Unresolved Trackbound Object can be used in the following situations:

a) Joining/Splitting: The Length of trains involved in Splitting and Joining is recorded, and the MBS ensures that the full length is accounted for before and after the procedure

b) Start of Mission: Comparing the new train length to the stored train length for an Unresolved Trackbound Object, and removing the Unresolved Trackbound Object if the train lengths match

c) Recovery after loss of communication (new session): New train length received is compared with that stored to check that it is the same train reconnecting.

The enumerated list of reasons for an Unresolved Trackbound Object will include the reasons listed in Table 12.

---

Operational Rules: None

Engineering Rules: None

## REQ-TrackStatus-3

[X2R5 REQ-TrackStatus-3]

When at Start of Mission a Train Location has been created for a train with the min Safe Front End located within an Unresolved Trackbound Object, then this Train Location shall be associated with this Unresolved Trackbound Object if the following conditions are fulfilled:

- The min Safe Front End is located inside exactly one Unresolved Trackbound Object, and



• There is a recorded train length for this Unresolved Trackbound Object, and

- The Unresolved Trackbound Object is not associated to any train.

## Rationale:

This is to manage the reduction or removal of the associated Unresolved Trackbound Object when the train confirms integrity (see for example REQ-TrackStatus-9).

Guidance:

In case there are several UTO overlapping the Train Location, it is project specific to decide on which one of them the Train Location shall be associated with, if any.

Operational Rules: None

Engineering Rules: None

#### 6.10.4 Requirements to update Unresolved Trackbound Objects

## REQ-TrackStatus-8

FOR FURTHER RELEASE [X2R5 REQ-TrackStatus-8]

The MBS shall alert the PE to the situation if:

- the MBS has updated the Train Location for a train, AND

- the rear of the Train has moved backward AND

- there are no adjacent Unresolved Trackbound Object where the rear of the train is localised.

## Rationale:

If a train has reported new Validated Train Data where the train length has increased, and the increase in length cannot be accounted for by the Recorded Train Length in some adjacent Unresolved Trackbound Object, then there may have been an error when updating the length of this or another train, which should be brought to the attention of the PE.

---

## Guidance:


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">The increase in the train length for the Train Location will be because the MBS has received Validated Train Data with an increased value of L_TRAIN.</td></tr><tr><td colspan="2">A train is expected to send Validated Train Data with an increased value of L_TRAIN if it has performed a joining operation. In this case, there should be one or more adjacent Unresolved Trackbound Object, where the additional Recorded Train Length(s) can account for the increased train length.</td></tr><tr><td colspan="2">If there are no adjacent Unresolved Trackbound Object which can account for the increased train length, then some error has occurred, and the TMS will be alerted.</td></tr><tr><td colspan="2">An inconsistency in the reported length from a train and the length stored by the MBS could be due to an error in the stored data, or failure in the application of Operational Rules. The MBS may decide to take a protective reaction, such as extending an Unresolved Trackbound Object to cover the Train Location. This reaction is project specific.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr></table>

## REQ-TrackStatus-9

When Train Integrity is confirmed by External Source for a train associated with an Unresolved Trackbound Object and the length of this train (L_TRAIN) is equal to the recorded length of the UTO, then the MBS shall delete the Unresolved Trackbound Object.

When Train Integrity is confirmed by External Source for a train associated with an Unresolved Trackbound Object and the total recorded length of this UTO plus all other UTOs overlapping this latter matches the length of the train (L_TRAIN), then MBS shall delete all UTOs matching the length of this train.

## Rationale:

The Unresolved Trackbound Object is “replaced” by the Train Location of the Train Object in this case. It is assumed that when a train confirms its train integrity then the MBS can trust the length of this train ( $ L_{TRAIN} $ ).  $ L_{TRAIN} $  matches the real length of the train (considering stretching).

## Guidance:

The length of the train could be longer than what is recorded for the Unresolved Trackbound Object in case two trains were joined after performing EoM and the joined train is associated with one of two Unresolved Trackbound Object.

Projects may decide to allow for some tolerance in matching the length of a train with what is recorded for the Unresolved Trackbound Object. In that case, the tolerance can be the configurable minimum length of Unresolved Trackbound Object, as defined

---

in ENG-Generic-3. Projects may also decide to check if there is another Unresolved Trackbound Object nearby that could explain the new longer Train Length and to alert the TMS if this is not the case.

Figure 33 shows the relationship between Train Location and the associated Unresolved Trackbound Object for an individual train with Train Integrity, one where the length of the train is the same as that recorded for the Unresolved Trackbound Object and one where the length is longer (e.g. after joining.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4cfdd8f7-0c6f-464e-a868-f6c9d386d02b/markdown_0/imgs/img_in_image_box_152_428_1114_860.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A37%3A39Z%2F-1%2F%2Fc9b26e72335dd7589fadcda4a0b1bad090cb79e54099a7b7ba49780b20624fdb" alt="Image" width="80%" /></div>


<div style="text-align: center;">Figure 33: Train Location after confirmation of Train Integrity</div>


In the righthand example, there is a step missing when the Train Location is updated with the Train Length after receiving Validated Train Data. In the end, when the total length matches the length of the 2 UTOs, the result is the same as in the lefthand figure (i.e. both UTOs are deleted by the established Train Location).

Operational Rules: None

Engineering Rules: ENG-Generic-3

---

## REQ-TrackStatus-25

When receiving Validated Train Data from a train indicating that the train length has been decreased, then MBS shall, before applying REQ-TrackStatus-10

- create an Unresolved Trackbound Object from the rear of the Train Location (considering the old train length) to the max safe rear end position of the train (considering the new train length)

• associate the Unresolved Trackbound Object to this train

- store the old Train Length (L_TRAIN) in the created Unresolved Trackbound Object if the train is marked as integrity confirmed.

## Rationale:

As the Train Location is shortened according to REQ-TrainLoc-6, it is necessary to create an UTO to manage the remaining length of the train that is now unresolved. It is assumed that when a train confirms its train integrity then the MBS can trust the length of this train (L_TRAIN). L_TRAIN matches the real length of the train (considering stretching).

## Guidance:

If this is a changed value of L_TRAIN, then the new value of L_TRAIN could be shorter than the previous value, for example after Splitting, as shown in Figure 34.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//11da4275-110d-4771-a3cf-221c74797d18/markdown_0/imgs/img_in_image_box_144_908_1121_1175.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A37%3A43Z%2F-1%2F%2F15cc5244cf1e2b3eabea1df7bda9b2f10be96b809f52678ac03ea60129d19eeb" alt="Image" width="82%" /></div>


<div style="text-align: center;">Figure 34: UTO creation when receiving Validated Train Data, L_TRAIN decreased</div>


The created UTO will then be updated according to REQ-TrackStatus-10 (update of the Recorded Length).

Operational Rules: None

Engineering Rules: None

---

# Contract No. HE – 101102001

## REQ-TrackStatus-10

When Train Integrity is confirmed by External Source for a train associated with an Unresolved Trackbound Object and the length (L_TRAIN) of this train is less than the Recorded Train Length, then the MBS shall:

- remove the part of the Unresolved Trackbound Object between the Min Safe Front End to the Max Safe Rear End of the train if the front ends do not overlap with the rear ends, AND

• reduce the Recorded Train Length of the remaining Unresolved Trackbound Object by the length of the train that confirmed Train Integrity, AND

• dissociate the Unresolved Trackbound Object from this train

## Rationale:

This is required for the MBS to maintain the Unresolved Trackbound Object within its Area of Control when all the train length recorded for an Unresolved Trackbound Object is not accounted for by a train confirming integrity.

## Guidance:

An Unresolved Trackbound Object cannot be fully recovered if the reported train length does not account for all the train length recorded for that area. In this case, the Unresolved Trackbound Object must remain with the recorded train length reduced by the length of the train that confirmed integrity.

The extent of the Unresolved Trackbound Object will also be reduced because the new Train Location will sweep the part of the Unresolved Trackbound Object from its Min Safe Front End to the Max Safe Rear End. This could result in this area being split in two, depending on the Train Location. In that case the recorded train length is the same for both Unresolved Trackbound Object.

Figure 35 shows an example of a train accounting for part of the length recorded for an Unresolved Trackbound Object after splitting and that area being split by the train when it confirms integrity. Here, the Front Train After Splitting, train 1 in the figure, confirms integrity and leaves before the rear part has performed SoM. As the train moves away, it sweeps the part of the Unresolved Trackbound Object at the front of the train, while the overlapped part at the rear becomes visible.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//441f3056-46e8-4fcb-93c8-65be5a0b7bed/markdown_0/imgs/img_in_image_box_139_180_1077_767.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A37%3A52Z%2F-1%2F%2F2c27a0c402ff0fb274c06a588ad4957d8c5e76fdac02eeb87965719bd7f12bea" alt="Image" width="78%" /></div>


<div style="text-align: center;">Figure 35: Unresolved Trackbound Object remains when Front Train after Splitting leaves</div>


The process above is repeated if another train performs Start of Mission in the remaining Unresolved Trackbound Object. After splitting, any end could perform Start of Mission first, but the handling is the same.

Projects may decide to allow for some tolerance in matching the length of a train with what is recorded for the Unresolved Trackbound Object. In that case, the tolerance can be the configurable minimum length of Unresolved Trackbound Object, as defined in ENG-Generic-3.

Additionally, projects may decide to additionally remove the UTO in front of the train in case the MBS can unambiguously determine that there is no other (part of a) train in front, e.g. by comparing the Train ID from the UTO with the Train ID from the train performing Start of Mission.

Additionally, after splitting, very short UTO may be removed according to requirement TrackStatus-19.

Operational Rules: None

Engineering Rules: ENG-Generic-3

## REQ-TrackStatus-11

When an Unresolved Trackbound Object is split and this has a Recorded Train Length, then the MBS shall store this length for all Unresolved Trackbound Object resulting from this split.

---

# Contract No. HE – 101102001

## Rationale:

This is to avoid that some train and/or waggons are lost to the MBS when an Unresolved Trackbound Object is split.

## Guidance:

Unresolved Trackbound Object can be split by a TTD section detected clear or by a train. In some situations, e.g. over a set of points, an Unresolved Trackbound Object could even be split in more than two parts.

If the split is due to a train which confirms integrity, this requirement is performed after REQ-TrackStatus-10.

Even if the extents of the split areas are very different, the MBS cannot safely judge if one of them should have more of the recorded length than the other and what that length should be. This is the same situation as if an Unresolved Trackbound Object is split by a clear TTD section.

Figure 35 Operational Rules: None

Engineering Rules: None


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-TrackStatus-12</td><td style='text-align: center;'>FOR FURTHER RELEASE [X2R5 REQ-TrackStatus-12]</td></tr><tr><td style='text-align: center;'>If the MBS is configured to accept Train Integrity confirmed by Driver, when Train Integrity is confirmed by Driver for a train associated with an Unresolved Trackbound Object, and the length (L_TRAIN) of this train is less than the Recorded Train Length of the Unresolved Trackbound Object, then the MBS shall:</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>• reduce the Recorded Train Length of the Unresolved Trackbound Object by the length of the train that confirmed Train Integrity</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Rationale:</td><td style='text-align: center;'></td></tr><tr><td colspan="2">An Unresolved Trackbound Object cannot be fully removed if a reported train length does not account for all the Recorded Train Length of that area.</td></tr></table>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b537fe36-65c0-4d63-9cac-906c5ffe46ff/markdown_0/imgs/img_in_image_box_90_198_1117_854.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A37%3A59Z%2F-1%2F%2F26553f5b9ae97ffdc5f66b1d0dd2e7e40a462c10df18e6c1112313d502ee3ff9" alt="Image" width="86%" /></div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>EQ-TrackStatus-13</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TrackStatus-13]</td></tr><tr><td colspan="3">When Train Integrity is confirmed for a train associated with an Unresolved Trackbound Object located within an Activated Temporary Shunting Area, then the MBS shall reduce the Recorded Train Length of the Unresolved Trackbound Object associated with the Shunting Area by the length of the train that confirmed Train Integrity.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">This is required for the MBS to maintain the Track Status within its Area of Control.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">If all the train length recorded for an Active Shunting Area is accounted for when the area is deactivated, then the Unresolved Trackbound Object that was associated with the Shunting Area can be removed, else it will remain but be Sweepable.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr></table>

---

## REQ-TrackStatus-14

When the front of the train has passed a part or all of an Unresolved Trackbound Object that existed before the Train Location was updated, then the MBS shall reduce that Unresolved Trackbound Object for the part of it from the previous min Safe Front End up to the new min Safe Front End of the train.

## Rationale:

This is to enable sweeping of the area passed between received position reports.

## Guidance:

Sweeping is performed by the Min Safe Front End (mSFE) of a train, as it cannot be guaranteed that there is no obstruction between the mSFE and the Max Safe Front End (MSFE) which is the Confidence Interval where the front of the train can be.

Figure 37 shows the sweeping by Train Location for a train with Train Integrity confirmed in a Sweepable Unresolved Trackbound Object ahead of the train.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//eb5f6e62-f5b4-4b4c-80e3-89f9810fb829/markdown_0/imgs/img_in_image_box_133_705_1133_1044.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A03Z%2F-1%2F%2F160f2be87ba0c2f850fc57616118fc4ab0f36250ef1057a33c511e853224d2bf" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 37: Train with Train Integrity confirmed Sweeping an Unresolved Trackbound Object</div>


Figure 38 below shows a train having passed a sweepable Unresolved Trackbound Object between a new and the previous Train Location. The train sweeps that Unresolved Trackbound Object.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//eb5f6e62-f5b4-4b4c-80e3-89f9810fb829/markdown_0/imgs/img_in_image_box_191_1208_1027_1451.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A03Z%2F-1%2F%2Facb99c62adac580f7172d70a62462ea4912fba6c089a39dd14aacafdb1e82c86" alt="Image" width="70%" /></div>


<div style="text-align: center;">Figure 38: Existing Unresolved Trackbound Object swept by a passing train</div>


The passage of a train through a Sweepable Unresolved Trackbound Object sweeps that Unresolved Trackbound Object.

---

Sweeping will not be applied when a train reports in RV. A reversing train will not sweep Unresolved Trackbound Object. However, the Max Safe Front end is updated as the train reports while reversing.

Operational Rules: None

Engineering Rules: None

## REQ-TrackStatus-15

When a Train Location is updated and this train has passed a part or all of an Unresolved Trackbound Object that did not exist before the Train Location was updated, then the MBS shall reduce that Unresolved Trackbound Object for the part of it between the Min Safe Front End and the Max Safe Rear End of the train.

## Rationale:

This is to enable (partial) sweeping of an Unresolved Trackbound Object that was created between received position reports.

## Guidance:

Sweeping is performed by the Min Safe Front End (mSFE) of a train, as it cannot be guaranteed that there is no obstruction between the mSFE and the Max Safe Front End (MSFE) which is the Confidence Interval where the front of the train can be.

A hazardous situation may arise if an Unresolved Trackbound Object is swept by a train if this Unresolved Trackbound Object was created only after the train had passed it.

Figure 39 below shows a train having passed a Sweepable Unresolved Trackbound Object between a new and the previous Train Location. As the area did not exist before the Train Location was updated, it only sweeps that Unresolved Trackbound Object from the new min Safe Front End and the new Max Safe Rear End of the train.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6141d1ba-5d23-4cc0-82f1-cce8c93787e7/markdown_0/imgs/img_in_image_box_189_1083_1073_1502.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A07Z%2F-1%2F%2F7c4b20158393a8c93eca486946c7204a99c6894c44216680a147bc885bb7adb2" alt="Image" width="74%" /></div>


<div style="text-align: center;">Figure 39: New Unresolved Trackbound Object swept by a passing train</div>

---

Operational Rules: None

Engineering Rules: None

## REQ-TrackStatus-16

FOR FURTHER RELEASE [X2R5 REQ-TrackStatus-16]

When the MBS considers the communication session with a train is terminated, the MBS shall convert the Train Location to an Unresolved Trackbound Object, except if the train is completely located inside an Active Shunting Area.

## Rationale:

This is the area where the train could be located, and as such needs to be protected by an Unresolved Trackbound Object.

## Guidance:

This requirement applies at EoM for trains not inside an Active Shunting Area.

For a train located completely inside an Active Shunting Area, there is no need for an Unresolved Trackbound Object since there is already an Unresolved Trackbound Object associated with the Active Shunting Area which will protect the train.

If a train is partially located inside an Active Shunting Area, it is project specific whether the MBS authorises the transition to Shunting Mode. Similarly, it is project specific how the MBS subsequently manages the overlapping Unresolved Trackbound Object that is created for the location of this train.

For a train leaving the MBS Area, another requirement deals with the relevant Unresolved Trackbound Object that could be removed when the train has left the area, i.e. before the communication session has been terminated.

Loss of communications is handled by other requirements.

Operational Rules: None

Engineering Rules: None

#### 6.10.5 Removing an Unresolved Trackbound Object

## REQ-TrackStatus-19

The MBS shall automatically remove Unresolved Trackbound Object for which the extent is less than or equal to a configurable minimum length.

## Rationale:

This is to avoid having small Unresolved Trackbound Object that have to be swept when it is known that there cannot be a vehicle inside them.

## Guidance:

Small Unresolved Trackbound Object could arise from splitting and joining procedures, or from sweeping.

---

For example, this requirement could apply to cross-over areas, as in Figure 40:

Figure 40: Short Unresolved Trackbound Object at crossover

The configurable minimum length could be related to the length of the shortest vehicle that could be running on the line. The Unresolved Trackbound Object can be removed, regardless of the status of adjacent areas.

In case an Unresolved Trackbound Object is split in two, e.g. by a clear TTD section, and if one of these areas is shorter than the configured minimum distance, then it can be removed even if it has a Recorded Train Length because that length is also recorded in the other area. Thus, there is no risk of trains and/or waggons becoming lost.

Operational Rules: None

Engineering Rules: ENG-Generic-3

#### 6.10.6 Impact from TTD on Unresolved Trackbound Objects

REQ-TTD-7

For a system using TTD, the MBS shall remove all or part of a Unresolved Trackbound Object, corresponding to a TTD section which is Clear.

Rationale:

TTD information can be used to clear the track under degraded situations.

Guidance:

TTD can assist with recovery as there is no need to sweep clear TTD sections.

Only the part of the Unresolved Trackbound Object corresponding to the Clear TTD section can be removed according to this requirement. This might mean that part of the Unresolved Trackbound Object may remain.

Operational Rules: None

Engineering Rules: None

---

# Contract No. HE – 101102001

## REQ-TTD-8

For a system using TTD, if the MBS has shortened the extent of an Unresolved Trackbound Object, then the MBS shall ensure the resulting Unresolved Trackbound Object is not shorter than the Recorded Train Length stored for it.

## Rationale:

Applying shortening could result in the extent of the remaining Unresolved Trackbound Object being less than the Recorded Train Length.

An Unresolved Trackbound Object with an extent shorter than the stored train length could represent a hazard.

## Guidance:

When the application of shortening the Unresolved Trackbound Object results in the length of the Unresolved Trackbound Object being less than Recorded Train Length, it is project specific what alternative action the MBS takes. For example, an application may decide to not apply any shortening to the Unresolved Trackbound Object, or to apply equal shortening to the front and rear whilst maintaining the length of the Recorded Train Length.

If an Unresolved Trackbound Object is one part of an Unresolved Trackbound Object which has been split, for example by a clear TTD, then project-specific rules may be needed, as the Recorded Train Length will be recorded in two Unresolved Trackbound Objects; see REQ-TrackStatus-11.

Operational Rules: None

Engineering Rules: None

## REQ-TTD-9

For a system using TTD, when detecting a TTD occupancy not associated with any expected train movement, the MBS shall create a Unresolved Trackbound Object for that TTD section (if there is not UTO to be extended from the next TTD according to requirement REQ-TTD-10).

## Rationale:

A TTD occupancy not associated with any expected train movement should be considered a potential hazard.

## Guidance:

Unexpected TTD occupancy also includes a TTD remaining Occupied when it might be expected to become Clear. For example, a TTD remaining Occupied behind a train which has sent a Train Position Report which gives a position clear of the TTD might indicate the presence of a Ghost Train. Implementation of such a function is project-specific and will likely require the use of a timer to compensate for the latency between Train Position Reports and TTD inputs.

---

If the TTD section is a short TTD section protecting a boundary of the MBS Area of Control, then projects may decide to create a larger Unresolved Trackbound Object if the TTD becomes unexpectedly occupied. This would require engineering, to determine the size of the Unresolved Trackbound Object to be created if the short boundary TTD becomes unexpectedly occupied.

There are other requirements relating to reactions for expected TTD occupancy.

Operational Rules: None

Engineering Rules: None

## REQ-TTD-10

For a system using TTD, when detecting a TTD occupancy not associated with any movement permission and adjacent to a TTD containing an existing Unresolved Trackbound Object which has a Recorded Train Length greater than zero, the MBS shall extend the Unresolved Trackbound Object up to the next boundary of this TTD section.

## Rationale:

A TTD occupancy not associated with any expected train movement should be considered a potential hazard.

## Guidance:

A train which is not communicating can move and occupy a previously clear TTD. That occupation can be attributed to the train in the adjacent TTD. The MBS can adjust the knowledge about where the train might be by extending the existing Unresolved Trackbound Object.

Unexpected TTD occupancy also includes a TTD remaining Occupied when it might be expected to become Clear. For example, a TTD remaining Occupied behind a train which has sent a Train Position Report which gives a position clear of the TTD might indicate the presence of a Ghost Train. Implementation of such a function is project-specific and will likely require the use of a timer to compensate for the latency between Train Position Reports and TTD inputs.

There are other requirements relating to reactions for expected TTD occupancy.

Operational Rules: None

Engineering Rules: None

---

## REQ-TTD-11


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>EQ-TTD-11</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TTD-11]</td></tr><tr><td colspan="3">For a system using TTD, on request from the TMS, the MBS shall be able to remove an Unresolved Trackbound Object caused by a faulty TTD.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">This will allow the MBS to help restore normal operation on the line.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">This function could be used to improve the reliability of the system and overrule false occupation reported by TTD (e.g. malfunctioning axle counters).</td></tr><tr><td colspan="3">In MBS operations, when all train movements are supervised by OBU with train position reporting and train integrity confirmation, a faulty TTD could be detected, e.g. dependent on the states of the neighbouring TTDs and position reports.</td></tr><tr><td colspan="3">The implementation of this requirement will need to prevent a new Unresolved Trackbound Object being created whilst the TTD remains Occupied.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td colspan="2">OPE-Generic-1, OPE-Generic-2</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td colspan="2">ENG-Generic-7</td></tr></table>

## REQ-TTD-12

For a system using TTD, when detecting a TTD clearance which cannot be associated with any regular train movement or Train Location, the MBS shall create an Unresolved Trackbound Object for each adjacent area if the adjacent area is not completely covered by UTO, or is known as cleared (by TTD if available).

## Rationale:

A TTD clearance which cannot be associated with any regular train movement or Train Location, should be considered a potential hazard, as such the MBS needs to protect other train movements by either creating or extending Unresolved Trackbound Objects.

## Guidance:

A TTD becoming unexpectedly clear might be due to several reasons. For example, a non-communicating train is moved such that the TTD becomes clear.

The MBS must react, for example by creating an additional Unresolved Trackbound Objects to protect the movement of trains.

Figure 41 shows the creation of Unresolved Trackbound Objects adjacent to a Clear TTD which has become unexpectedly Clear.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bc09250f-ff4b-415a-9fab-2526e588bdb6/markdown_0/imgs/img_in_image_box_151_152_1093_472.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A34Z%2F-1%2F%2F6f545c0161b9db08618efe14183fb61ed3b6a1bbbb3b2754e07000169762b8b6" alt="Image" width="79%" /></div>


<div style="text-align: center;">Figure 41: Creation of Unresolved Trackbound Object for unexpected Clear TTD</div>


Projects should consider the impact of creation of the Unresolved Trackbound Object on railway operations.

Depending on the implementation, project-specific engineering rules may be required.

Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-14

When the propagation timer of a UTO expires, the MBS shall extend the UTO in both directions:

• until the TTD section limit, or

- until the first Max Safe Rear End location found from the UTO to the TTD limit applicable in the same direction, or

- until the first Min Safe Front location found from the UTO to the TTD limit applicable in the opposite direction.

## Rationale:

Due to the presence of a UTO, uncontrolled movements are possible inside the occupied TTD section, the UTO is then extended to the TTD limit or the first found Train Location (see chapter 6.10.2). Uncontrolled movements outside the currently occupied TTD are managed by other requirements.

## Guidance:

The propagation time is configurable at Project level.

If the propagation time is set to 0, the propagation is performed immediately.

If the propagation time is set to the specific value “infinite”, the propagation is never performed.

Figure 42 below shows the propagation of the UTO when the propagation timer expires and a train is present in the same direction.

---

The UTO will be propagated every time the train 1 moves forward.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6c039e60-2ba5-4aa6-89c2-2fa01089aafc/markdown_0/imgs/img_in_image_box_144_267_1143_615.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A38Z%2F-1%2F%2F9e7b5c260989d84502cfb8960d6781a1aa97c8cef1725d3f65d662bd2d3df3e1" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 42: UTO propagation with a train in the same direction.</div>


Figure 43 below shows the propagation of the UTO when the propagation timer expires with the presence of a train in the opposite direction.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6c039e60-2ba5-4aa6-89c2-2fa01089aafc/markdown_0/imgs/img_in_image_box_127_796_1160_1150.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A38Z%2F-1%2F%2Ff92bdfa4f351bae11cdf39732c59ccd22aeb33501192c15acba093a3598dfdcf" alt="Image" width="86%" /></div>


<div style="text-align: center;">Figure 43: UTO propagation with a train in the opposite direction.</div>


Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-17

After the propagation timer of a UTO has expired, if the UTO is terminated at a Max Safe Rear End location of a Train Location, when this train moves, the MBS shall update the extent of the UTO to closest of:

- the new Max Safe Rear End location of the train, or

• the TTD limit.

---

## Rationale:

When UTO has been propagated to the rear of a train according to REQ-TrainLoc-14, the UTO is propagated every time the train moves, until the rear of the train has passed the TTD limit.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-TrainLoc-15

When a Train Object is marked as “integrity not confirmed” for more than a given propagation time, then MBS shall create a UTO associated to this train from the Max Safe Rear End of the train up to the next TTD limit in reverse direction.

## Rationale:

Due to the Train Location with integrity not confirmed, an uncontrolled roll-away movement is possible inside the occupied TTD section. A UTO is then created to the TTD limit. Uncontrolled movement outside the current occupied TTD are managed by other requirements. Max Safe Rear End is considered here according to splitting scenario.

## Guidance:

<div style="text-align: center;">Figure 44 below shows the creation of the UTO for a non-integer train when the propagation time expires</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d6f3b582-c41d-4972-a6d9-4cbf64e48a3a/markdown_0/imgs/img_in_image_box_124_996_1119_1525.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A38%3A42Z%2F-1%2F%2Fcbd7674bc1eada60a7d14da335b76cec07904c6f4fbfe40a99ffd8d192ea6ec1" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 44: UTO creation for a non-integer train.</div>

---

Operational Rules: None

Engineering Rules: None

REQ-TrainLoc-16

Once a UTO has been created according to requirement REQ-TrainLoc-15, the propagation time shall be considered as expired for this UTO.

Rationale:

Any movement of the train in front of the UTO should extend the current UTO by propagation immediately according to requirement REQ-TrainLoc-14.

Guidance: None

Operational Rules: None

Engineering Rules: None


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">6.10.7 Requirements related to Operator panel - FOR FURTHER RELEASE</td></tr><tr><td style='text-align: center;'>REQ-TrackStatus-22</td><td style='text-align: center;'>[X2R5 REQ-TrackStatus-22]</td></tr><tr><td colspan="2">On request from the PE/Operator panel, the MBS shall create an Unresolved Trackbound Object flagged as Sweepable provided the area is longer than the configurable minimum length.</td></tr><tr><td colspan="2">Rationale:</td></tr><tr><td colspan="2">This is to allow the MBS to have all relevant information concerning obstructions.</td></tr><tr><td colspan="2">Guidance:</td></tr><tr><td colspan="2">For example, this can be used in the degraded situation of a non-communicating train. A train without communications has to be moved inside an Unresolved Trackbound Object, so that the MBS is aware that this area is protected for a specific train.</td></tr><tr><td colspan="2">The Unresolved Trackbound Object may be created automatically by the TMS, or via dispatcher interaction with the TMS or Operator Panel.</td></tr><tr><td colspan="2">Unresolved Trackbound Object can be created independently.</td></tr><tr><td colspan="2">The Sweepable Unresolved Trackbound Object needs to be longer than the configurable minimum length for removal of Unresolved Trackbound Object, as defined in ENG-Generic-3.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>OPE-TrackInit-2; OPE-Generic-7; OPE-LossComms-1; OPE-LossTI-1</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>ENG-Generic-3</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-TrackStatus-23</td><td style='text-align: center;'>[X2R5 REQ-TrackStatus-23]</td></tr><tr><td colspan="2">On request from the PE/Operator Panel, the MBS shall create an Unresolved Trackbound Object flagged as Non-Sweepable.</td></tr><tr><td colspan="2">Rationale:</td></tr><tr><td colspan="2">When the PE/Operator Panel requests a Non-Sweepable Unresolved Trackbound Object, it may be for a reason that would make it unsuitable to be swept e.g. a known permanent obstacle on the line.</td></tr><tr><td colspan="2">Guidance:</td></tr><tr><td colspan="2">Non-Sweepable Unresolved Trackbound Object will only be cleared at the request of the TMS. The MBS will retain a Non-Sweepable Unresolved Trackbound Object after traversal by a train which has confirmed Train Integrity.</td></tr><tr><td colspan="2">Unresolved Trackbound Object can be created independently, i.e. they can overlap existing Unresolved Trackbound Object or Train Location.</td></tr><tr><td colspan="2">For example, creating Unresolved Trackbound Object in parts of the track might be due to external systems detecting fallen objects, or landslides.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>OPE-TrackInit-2, OPE-Generic-7; OPE-LossComms-1; OPE-LossTI-1</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>REQ-TrackStatus-24</td><td style='text-align: center;'>[X2R5 REQ-TrackStatus-24]</td></tr><tr><td colspan="2">On request from the PE/Operator Panel, the MBS shall remove, reduce or extend Unresolved Trackbound Object.</td></tr><tr><td colspan="2">Rationale:</td></tr><tr><td colspan="2">MBS must allow the TMS to remove, reduce or extend Unresolved Trackbound Object based on the result of operational procedures.</td></tr><tr><td colspan="2">Guidance:</td></tr><tr><td colspan="2">An Unresolved Trackbound Object, both Sweepable and Non-Sweepable, can be removed, reduced or extended by the PE/Operator Panel.</td></tr><tr><td colspan="2">For example, some Infrastructure Managers may permit Unresolved Trackbound Object to be removed or reduced based on the observations of a Driver sweeping on an adjacent line.</td></tr><tr><td colspan="2">Projects may, if providing the necessary information, allow the Dispatcher via PE/Operator Panel to remove or reduce parts of an Unresolved Trackbound Object, e.g. by stating a certain length to be removed.</td></tr><tr><td colspan="2">In case there is a train length stored for an Unresolved Trackbound Object requested for removal, it is recommended that the MBS prevents removing this Unresolved Trackbound Object unless the removal is supported by some additional measure(s).</td></tr></table>

---

Robust operational procedures are required in order to permit the Dispatcher, via the PE/Operator Panel, to remove or reduce Unresolved Trackbound Object.

In case of overlapping Unresolved Trackbound Object conditions might be considered when removing an Unresolved Trackbound Object.

If the Unresolved Trackbound Object is Sweepable, the MBS will remove it if it is reduced to a length shorter than the configurable minimum length for removal of Unresolved Trackbound Object, as defined in ENG-Generic-3.

Operational Rules: OPE-Generic-2, OPE-Generic-7

Engineering Rules: None

---

### 6.11 SysF Authorise MP Request

#### 6.11.1 Overview

This function is responsible to assess the safety of a request to alter the Authorisation of a Train Object. PE or the operator through the operator panel can request an Authorisation through the SCI-CMD interface which is then checked by MBS if it violates any safety constraint. The MBS shall not alter the request if certain parameters are incorrect (e.g. The operating state has changed during the message transmission between PE and MBS) but only report the failure to PE with the failure reason.

The MP Request shall contain the following information:

- Train Object Identifier

- Movement Permission

The Movement Permission shall have the following attributes

- Risk Buffer (LinkedPath)

- Extent (LinkedPath)

- Requested Maximum Speed in km/h (LinkedPath per different speed)

ETCS Movement Mode (Linked Path per different mode)

- List of DPS Groups that must not be used as flank protection measure

##### 6.11.1.1 Flank Protection Overview

Before authorizing an MP request, MBS evaluates if sufficient protections to limit the risk of side-on collision according to the safety analysis are in observed between the requested MP and any uncontrolled trackbound movement.

To find the flank protecting measures applicable to the MP request, MBS builds Risk Path Candidates that span from the end of the Allocation Sections up to the corresponding elements providing (or not) flank protection (see requirement REQ-RP_SEARCH).

Note: once a risk path has been created, it may also be updated/deleted without the reception of a new MP request (e.g. when a train is moving) through a continuous evaluation (see chapter 6.18).

For each Risk Path Candidate that has been built (according to REQ-SC_RP_SEARCH), the MBS evaluates if the Risk Path is correctly terminated (according to REQ-SC_RP_TERM) on an element authorised to provide flank protection.

The elements that can provide flank protections include:

## • Switchable Track element

Examples: point from trailing side, derailer/catch point, end of track, etc.

The position of these points ensures that any uncontrolled trackbound movement approaching the side of the Movement Permission will be deviated or derailed.

## • Movement Permission

---

# Contract No. HE – 101102001

The side of the Movement Permission is protected by another train supervised by a Movement Permission. As the ETCS on-board unit of the other train supervises the train movement, this reduces the risk that the train will exceed its authority to an extent that could result in a flank collision.

## • Train Object

The side of the Movement Permission is protected by another connected train. If the onboard unit guarantees that the train will not move without any authority, it is ensured that this train will not perform any movements that could result in a flank collision.

## • Protection by a sufficient distance

The side of the Movement Permission is detected as free over a sufficient distance to mitigate the risk a flank collision to an acceptable level.

## • Protection by Operational Rules

If the risk of flank collision cannot be mitigated by the preceding measures, the final option is to reduce the potential consequences of a flank collision if Operational Rules (vehicle should not be moved without permission) are violated.

This imposes a reduced speed.

---

It is possible to configure within the MBS Domain Data the appropriate flank protection measures to be safely verified by the MBS according to Table 15.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Flank Protection by</td><td style='text-align: center;'>Termination Requirement SC-RP_TERM_</td><td style='text-align: center;'>Variable</td><td style='text-align: center;'>Scope</td><td style='text-align: center;'>Type</td><td style='text-align: center;'>Description</td></tr><tr><td rowspan="3">Search Options</td><td rowspan="3">--</td><td style='text-align: center;'>fpSearch</td><td style='text-align: center;'>G</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if Flank Protection is required</td></tr><tr><td style='text-align: center;'>fpSearchOnDependentAs</td><td style='text-align: center;'>AS</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if the dependent Allocation Section needs Flank Protection</td></tr><tr><td style='text-align: center;'>rpMaxSearchDistance</td><td style='text-align: center;'>G</td><td style='text-align: center;'>UINT</td><td style='text-align: center;'>The length in meters after which the Risk Path search is finished</td></tr><tr><td rowspan="3">Switchable Track Element</td><td rowspan="3">DPS</td><td style='text-align: center;'>rpTermAtDpsOnly</td><td style='text-align: center;'>AS</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if a Risk Path originating at this Allocation Section can only be terminated at a DPS</td></tr><tr><td style='text-align: center;'>dpsProvidesFlankProtection</td><td style='text-align: center;'>DPS</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if this DPS can provide flank protection</td></tr><tr><td style='text-align: center;'>dpsMaxFlankProtectionSpeed</td><td style='text-align: center;'>DPS</td><td style='text-align: center;'>UINT</td><td style='text-align: center;'>Speed in km/h up to which this DPS can provide Flank Protection</td></tr><tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'>RB MP</td><td style='text-align: center;'>rpTermAllowedAtRbAndMp</td><td style='text-align: center;'>G</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if Risk Paths terminated at a Movement Permission Extent or Risk Buffer can be used as a flank protection measure.</td></tr><tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>TO</td><td style='text-align: center;'>rpTermAllowedAtTo</td><td style='text-align: center;'>G</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if Risk Path terminated at a Train Object can be used as a flank protection measure.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Flank Protection by</td><td style='text-align: center;'>Termination Requirement SC-RP_TERM_</td><td style='text-align: center;'>Variable</td><td style='text-align: center;'>Scope</td><td style='text-align: center;'>Type</td><td style='text-align: center;'>Description</td></tr><tr><td style='text-align: center;'>Sufficient Distance</td><td style='text-align: center;'>DIST</td><td style='text-align: center;'>rpTermAllowedAfterMaxDistance</td><td style='text-align: center;'>G</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if Risk Path terminated after a defined search distance given in rpMaxSearchDistance can be used as flank protection measure.</td></tr><tr><td rowspan="2">Operational Rules (UTO found)</td><td rowspan="2">UTO</td><td style='text-align: center;'>rpTermAllowedAtUto</td><td style='text-align: center;'>G</td><td style='text-align: center;'>BOOL</td><td style='text-align: center;'>TRUE if Risk Path terminated at an Unresolved Trackbound Object can be used as flank protection measure.</td></tr><tr><td style='text-align: center;'>rpTermMaxSpeedUto</td><td style='text-align: center;'>G</td><td style='text-align: center;'>UINT</td><td style='text-align: center;'>Max Speed for a Movement Permission at the Allocation section if a Risk Path originating from it terminates at a Unresolved Trackbound Object.</td></tr></table>

Table 15 – Flank Protection measures configuration

G = Global

AS = Configurable at every Allocation Section

DPS = Configurable at every Drive Protection Section

UINT = Unsigned Integer

BOOL = Boolean value (TRUE, FALSE)

In tracks (usually secondary tracks) where non-controlled movements can occur (shunting, stabling of vehicles with remaining rollaway risk), the Infrastructure Manager has to ensure that appropriate measures are available:

• Trap points, catch points/derailers;

• Prohibitions of shunting and stabling;

• Equipment with TTD (as otherwise non-controllable movements cannot be detected).

---

The interface between MBS and PE is impacted by the flank protection as follows:

- For each granted Movement Permission, the MBS provides to PE the Risk Path as part of the Movement Permission.

- When requesting a Movement Permission, the PE is able to optionally provide a list of DPS that must not be used as flank protection measure.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Application Example</th><th style='text-align: center;'>T01</th><th style='text-align: center;'>TE4</th><th style='text-align: center;'>TE5</th><th style='text-align: center;'>TE6</th><th style='text-align: center;'>TE7</th><th style='text-align: center;'>TE8</th><th style='text-align: center;'>TE9</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Train Object (Train Location)</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Unresolved Trackbound Object</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

In the example above the maximum speed for TE3 and TE2 is equal, it is different for TE3 and TE4. The whole train running path of TO1 is split in three segments. The split between TE4 and TE3 would be due to the change in maximum speed. The split in TE2 is due to the mode change from FS to OS.

Note: the example is not exhaustive and does not show all possible starting conditions and terminations of a risk path (e.g. risk path termination by Train Object, risk path starting at a diamond crossing).

---

##### 6.11.1.3 Safety Check Overview

Safety Checks performed for direct overlaps between two extents (the first column represents the received request to be checked, other columns represent the current state):


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>MP</td><td style='text-align: center;'>TO/UTO</td><td style='text-align: center;'>RB</td><td style='text-align: center;'>RP</td></tr><tr><td style='text-align: center;'>MP</td><td style='text-align: center;'>REQ-SC_MP_MP</td><td style='text-align: center;'>FS MandatoryREQ-SC_MP_TOREQ-SC_MP_UTO</td><td style='text-align: center;'>REQ-SC_MP_RB</td><td style='text-align: center;'>ConfigREQ-SC_MP_RP</td></tr><tr><td style='text-align: center;'>RB</td><td style='text-align: center;'>REQ-SC_RB_MP</td><td style='text-align: center;'>FS Mandatory OR ConfigREQ-SC_RB_TOREQ-SC_RB_UTO</td><td style='text-align: center;'>ConfigREQ-SC_RB_RB</td><td style='text-align: center;'>ConfigREQ-SC_RB_RP</td></tr></table>

<div style="text-align: center;">Safety Checks performed for overlaps of extents within dependent Allocation Sections:</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>MP</td><td style='text-align: center;'>TO/UTO</td><td style='text-align: center;'>RB</td><td style='text-align: center;'>RP</td></tr><tr><td style='text-align: center;'>MP</td><td style='text-align: center;'>REQ-SC_MP_MP_AS</td><td style='text-align: center;'>FS Mandatory
REQ-SC_MP_TO_AS
REQ-SC_MP_UTO_AS</td><td style='text-align: center;'>REQ-SC_MP_RB_AS</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>RB</td><td style='text-align: center;'>REQ-SC_RB_MP_AS</td><td style='text-align: center;'>FS Mandatory OR Config
REQ-SC_RB_TO_AS
REQ-SC_RB_UTO_AS</td><td style='text-align: center;'>Config
REQ-SC_RB_RB_AS</td><td style='text-align: center;'></td></tr></table>

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

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d67746e4-bdec-4e86-b9ca-dc7160d89b79/markdown_0/imgs/img_in_image_box_143_301_998_397.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A39%3A59Z%2F-1%2F%2F550c81d75c18869ddfe2d30dd80430dd4accfd190e42cbd0abf916ed64ffdc77" alt="Image" width="71%" /></div>


The overlap of MP and TO is not allowed if the Authorisation Type of the Movement Permission Path Segment is set to FS.

Intersection in rear of the minimum Safe Front End is ignored to allow the first train to start in FS in case of splitting.

Operational Rules: None

Engineering Rules: None

## REQ-SC MP UTO

The MBS shall check that, if a Movement Permission overlaps an Unresolved Trackbound Object in advance of the mSFE of the train for which the Movement Permission is requested, the mode for that part is OS, and if the check fails, the MBS shall send a "PATH_OCCUPIED" reject code.

Rationale: The running path of a train shall be free of other vehicles if operating under FS.

Guidance:

Movement Permission Extent

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d67746e4-bdec-4e86-b9ca-dc7160d89b79/markdown_0/imgs/img_in_image_box_138_1013_1011_1105.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A39%3A59Z%2F-1%2F%2Fc6913254a0725cbb2d2c6706bba97b2d5abbf1102becdae3439a27e33d965d6e" alt="Image" width="73%" /></div>


Unresolved Trackbound Object

The overlap of MP and UTO is not allowed if the Authorisation Type of the Movement Permission Path Segment is set to FS.

Intersection in rear of the minimum Safe Front End is ignored to allow the first train to start in FS in case of splitting.

Operational Rules: None

Engineering Rules: None

## REQ-SC RB TO

The MBS shall check that the Risk Buffer of the requested MP shall not overlap the extent of another Train Object, if the requested mode at the end of the Movement Permission Extent is FS and this check is enabled in the configuration, and if the check fails, the MBS shall send a "RISK_BUFFER_OCCUPIED" reject code.

---

Rationale: The Risk Buffer shall be clear of any vehicles if the requested mode was FS at the end of the running path. In some countries the overlap area is not required to be clear of vehicles.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The movement permission to move.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The risk buffer.</td></tr>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>The train object.</td></tr>
  </tbody>
</table>

The overlap of Risk Buffer and TO is not allowed if the Authorisation Type at the end of the Movement Permission is set to FS.

Operational Rules: None

Engineering Rules: None

## REQ-SC RB UTO

The MBS shall check that the Risk Buffer of the requested MP shall not overlap the extent of an Unresolved Trackbound Object, if the requested mode at the end of the Movement Permission is FS and if this check is enabled in the configuration, and if the check fails, the MBS shall send a "RISK_BUFFER_OCCUPIED" reject code.

Rationale: The Risk Buffer shall be clear of any vehicles if the requested mode was FSat the end of the running path. In some countries the overlap area is not required to be clear of vehicles.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The movement permission for the object.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The risk buffer for the object.</td></tr>
    <tr><td style='text-align: center;'>Unresolved Trackbound Object</td><td style='text-align: center;'>The unresolved trackbound object.</td></tr>
  </tbody>
</table>

The overlap of Risk Buffer and UTO is not allowed if the Authorisation Type at the end of the Movement Permission is set to FS.

Operational Rules: None

Engineering Rules: None

REQ-SC_MP_TO_AS

---

The MBS shall check that if the extent of the Movement Permission overlaps an Allocation Section, all mutually exclusive Allocation sections shall not have an overlap with another Train Object and if the check fails, the MBS shall send an "AS_OCCUPIED" reject code.

Rationale: The fouling point shall be clear of other vehicles, otherwise a flank collision might result.

Guidance:



<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
  </tbody>
</table>

Having both Risk Path and a Train Object present in a conflicting Allocation Section is not allowed.

Operational Rules: None

Engineering Rules: None

## REQ-SC MP UTO AS

The MBS shall check that if the extent of the Movement Permission overlaps an Allocation Section, all mutually exclusive Allocation sections shall not have an overlap with an Unresolved Trackbound Object and if the check fails, the MBS shall send an "AS_OCCUPIED" reject code.

Rationale: The fouling point shall be clear of other vehicles, otherwise a flank collision might result.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Unresolved Trackbound Object</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Allocation Section</td></tr>
  </tbody>
</table>

Having both Risk Path and an Unresolved Trackbound Object present on a conflicting Allocation Section is not allowed.

---

Operational Rules: None

Engineering Rules: None

## REQ-SC_RB_TO_AS

The MBS shall check that if the Risk Buffer of the Movement Permission overlaps an Allocation Section, all mutually exclusive Allocation sections shall not have an overlap with the extent of another Train Object and if the check fails, the MBS shall send an "AS_OCCUPIED" reject code.

Rationale: The fouling point of points shall be clear of other vehicles.



Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The first stage where the Risk Transfer System is expected to occur.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The second stage where the Risk Transfer System is expected to occur.</td></tr>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>The third stage where the Risk Transfer System is expected to occur.</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>The fourth stage where the Risk Transfer System is expected to occur.</td></tr>
  </tbody>
</table>

Having both Risk Path and Train Object present in a conflicting Allocation Section is not allowed.

Operational Rules: None

Engineering Rules: None

## REQ-SC_RB_UTO_AS

The MBS shall check that if the Risk Buffer of the Movement Permission overlaps an Allocation Section, all mutually exclusive Allocation sections shall not have an overlap with an Unresolved Trackbound Object and if the check fails, the MBS shall send an "AS_OCCUPIED" reject code.

Rationale:

The fouling point of points shall be clear of other vehicles.





Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The first layer of the risk layer.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The second layer of the risk layer.</td></tr>
    <tr><td style='text-align: center;'>Unresolved Trackbound Object</td><td style='text-align: center;'>The third layer of the risk layer.</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>The fourth layer of the risk layer.</td></tr>
  </tbody>
</table>

---

Having both Risk Path and Unresolved Trackbound Object present in a conflicting Allocation Section is not allowed.

Operational Rules: None

Engineering Rules: None

##### 6.11.4.4 Movement related Safety Checks

## REQ-SC_MP_MP

The MBS shall check that the Movement Permission Extent in advance of the mSFE of the train for which the Movement Permission is requested shall not overlap with a Movement Permission Extent of another train unless the other train is supervised at standstill and if the check fails, the MBS shall send an "EXTENT CONFLICT" reject code.

Rationale: Two trains should not be authorised to perform conflicting movements.

Guidance: The enforcement of OS for the overlap between the MP and the Train Object is covered in REQ-SC_MP_TO.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//de2f120f-04bd-4564-bf4b-56cfb30b72f9/markdown_0/imgs/img_in_image_box_113_748_975_963.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A40%3A17Z%2F-1%2F%2Fb29c618d710863195076e44fbd51b4c9d7ced08aa8b5450ecbf42607b6261a35" alt="Image" width="72%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC MP RB

The MBS shall check that the Movement Permission Extent of the requested MP shall not overlap with a Risk Buffer extent of another train and if the check fails, the MBS shall send an "EXTENT CONFLICT reject code.

Rationale: The running path of a train shall be free of other vehicles.

Guidance: The current version of this requirement is only concerning train movements in FS or OS.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//de2f120f-04bd-4564-bf4b-56cfb30b72f9/markdown_0/imgs/img_in_image_box_143_1380_985_1479.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A40%3A17Z%2F-1%2F%2Fbc1158e144af1e7d7e4c19ac254a3bb70aab7713fc254e0c3a47b70c047a899a" alt="Image" width="70%" /></div>


Operational Rules: None

Engineering Rules: None

---

## REQ-SC_MP_RP

The MBS shall check that if the global variable rpTermAllowedAtRbAndMp is set to TRUE, the Movement Permission Extent of the requested MP shall not overlap with a Risk Path extent of another train and if the check fails, the MBS shall send an "EXTENT_CONFLICT reject code.

Rationale: If a Risk Path is not allowed to terminate at a Movement Permission or Risk Buffer, permitting the request would lead to a safety reaction.

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//65820ea8-416d-4cfd-9747-7124a0c5a3a6/markdown_0/imgs/img_in_image_box_157_477_986_571.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A40%3A25Z%2F-1%2F%2Fed006d47ca1aa74f0fdca1eb24a4d97f7de8db5fc434c738f38d818f7333d88a" alt="Image" width="69%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC MP MP AS

The MBS shall check that any Allocation Section a Movement Permission Extent of the requested MP overlaps with, shall not have an overlap with a Movement Permission Extent of another train in all mutually exclusive Allocation Sections and if the check fails, the MBS shall send an "EXTENT_AS_CONFLICT reject code.

Rationale: The fouling point shall not be occupied by another train movement.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Risk Buffer</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_MP_RB_AS

The MBS shall check that an Allocation Section the Movement Permission Extent overlaps with, shall not have an overlap with a Risk Buffer of another train in all mutually exclusive Allocation Sections and if the check fails, the MBS shall send an "EXTENT AS CONFLICT reject code.

---

Rationale:

movement.

The fouling point shall not be occupied by another train



Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Risk Buffer</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RB_MP

The MBS shall check that the Risk Buffer of the requested MP shall not overlap with a Movement Permission Extent of another train unless the other train is supervised at standstill and if the check fails, the MBS shall send a "RISK_BUFFER_CONFLICT" reject code.

Rationale: The overrun protection area of a Movement Permission shall not be in conflict with another train movement.

Guidance: The enforcement of OS for the overlap between the MP and the Train Object is covered in REQ-SC_RB_TO.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>The left hand and the right hand.</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RB_RB

If the safety check is enabled in the configuration, the MBS shall check that the Risk Buffer of the requested MP shall not overlap any Risk Buffer of another Movement Permission and if the check fails, the MBS shall send a "RISK_BUFFER_CONFLICT" reject code.

Rationale: The overrun protection area of a Movement Permission shall not be claimed by the Risk Buffer of another train.

Guidance:

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The left hand hand.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The right hand hand.</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RB_RP

The MBS shall check that if the global variable rpTermAllowedAtRbAndMp is set to TRUE, the Risk Buffer of the requested MP shall not overlap with a Risk Path extent of another train and if the check fails, the MBS shall send an "EXTENT_CONFLICT reject code.

Rationale: If a Risk Path is not allowed to terminate at a Movement Permission or Risk Buffer, permitting the request would lead to a safety reaction.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The path to the risk.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The extent to which the risk is allowed to be allowed.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The function to be allowed to be allowed.</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC RB MP AS

The MBS shall check that any Allocation Section the Risk Buffer of the requested MP overlaps with, shall not have another overlap with a Movement Permission Extent of another train in all mutually exclusive Allocation Sections and if the check fails, the MBS shall send a "RISK_BUFFER_AS_CONFLICT" reject code.

Rationale: The fouling point shall not be occupied by another train movement.

Guidance:

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Start of flow</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>End of flow</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Risk Buffer</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC RB RB AS

If the safety check is enabled in the configuration, the MBS shall check that any Allocation Section the Risk Buffer of the requested MP overlaps with, shall not have another overlap with a Risk Buffer of another train in all mutually exclusive Allocation Sections and if the check fails, the MBS shall send a "RISK_BUFFER_AS_CONFLICT" reject code.

Rationale: The fouling point shall not be occupied by another train movement.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Start of flow</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>End of flow</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>right</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>left</td><td style='text-align: center;'>Risk Buffer</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC RB SIZE

The MBS shall check that the Risk Buffer for the requested MP is longer than or equal to the minimal length of the Risk Buffer according to the MBS configuration and if the check fails, the MBS shall send a "RISK_BUFFER_TOO_SHORT" reject code.

Rationale: The Risk Buffer includes the danger point and a safety margin to guarantee that the train never overpasses the end of the Risk Buffer, this assumes a minimum length for the Risk Buffer. See also REQ-0051.

Guidance: None.

Operational Rules: None

Engineering Rules: TBD how the concrete value shall be calculated. The absolute minimum size will be 6 meters for FS (overhang of vehicle front to first axle).

---

##### 6.11.4.5 DPS related Safety Checks

## REQ-SC_MP_DPS

The MBS shall check that all DPS that overlap with the Movement Permission Extent are in the state "FULL" and if the check fails, the MBS shall send a "DPS_INVALID_STATE" reject code.

Rationale: All Switchable Trackside Assets have to be secured in the correct position for a train movement.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
  </tbody>
</table>

Note: The Risk Path is only shown for completeness.

Operational Rules: None

Engineering Rules: None

## REQ-SC RB DPS

The MBS shall check that all DPS that overlap the Risk Buffer of the requested Movement Permission Extent are in the state "FULL" and if the check fails, the MBS shall send a "RISK_BUFFER_DPS_INVALID_STATE" reject code.

Rationale: All Switchable Trackside Assets have to be in the “secured” position in the overrun protection section of a train movement.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>The left hand and right hand.</td></tr>
  </tbody>
</table>

Note: The Risk Path is only shown for completeness.

Operational Rules: None

---

Engineering Rules: None

## REQ-COOP_PENDING

The MBS shall check that there is no co-operative shortening of MA procedure is pending for the corresponding train and if the check fails, the MBS shall send a "COOP_PENDING" reject code.

Rationale: Sending MAs in parallel with Request to Shorten MA messages could result in inconsistent views between MBS and the on-board.

Guidance: None

Operational Rules: None

Engineering Rules: None

##### 6.11.4.6 Flank Protection related Safety Checks

## REQ-RP SEARCH

If the global configuration variable fpSearch is set to TRUE and the attribute fpSearchOnDependentAs in the Allocation Section the Movement Permission Extent overlaps with is set to TRUE, MBS shall calculate at least one Risk Path starting at the end of each Allocation Section that is dependent to the Allocation Section the Movement Permission Extent overlaps with and set the end of the Risk Path according to the following list:

• REQ-RPS DPS

• REQ-RPS TO

• REQ-RPS_UTO

• REQ-RPS MP

• REQ-RPS RB

• REQ-RPS TE

• REQ-RPS DIST

, while obeying the following rules:

• REQ-RPS NEAREST

• REQ-RPS_SPLIT

Rationale: An Allocation Section marks a stretch of track network where insufficient gauge clearance exists and there shall be no risk of movements against this point. As the risk buffer is used by the train only in degraded situations (i.e. the

---

train overpasses its End of Authority), the risk buffer is intentionally excluded for the risk path search.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'>Permission to move.</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>Section to分配.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>Path to risk.</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>Full.</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>None.</td></tr>
  </tbody>
</table>

In this example AS11 is dependent to AS12 thus a Risk Path must emerge out of AS11 (if fpSearchOnDependentAs is set to TRUE for AS12).

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

In this example a second point is located in the right leg of the first point where the blades start inside the fouling point. The following dependencies exist in this example: AS11-AS13 and AS12-AS13. AS 11 and AS 12 are not dependent to each other.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f83ca269-048c-4bb3-bfcc-089e2426d5d4/markdown_0/imgs/img_in_image_box_139_175_1076_739.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A40%3A55Z%2F-1%2F%2F618fb8320e417d1a82e240fcdc539a848d65ff06778e4a0264ef455f38756548" alt="Image" width="78%" /></div>


In this reduced example of a double slip, the Allocation Sections of DPS Group 2 are shown in a different colour for clarity. The following dependencies exist: AS11 & AS12, AS13 & AS14, AS21 & AS22, AS23 & AS24. According to the rules a Risk Path is needed for AS11, AS13, AS22 and AS24. As the end locations of AS11 & AS13 as well as AS22 & AS24 are equal, only one Risk Path is needed per end location.

Operational Rules: None

Engineering Rules: None

## REQ- RPS TO

When the MBS builds a Risk Path and it finds a Train Object in the search direction, it shall set the end of the Risk Path at the border of the Train Object without overlapping it according to REQ_SC_RP_TO.

Rationale: A Train Object is a possible point for a Risk Path termination but the Risk Path shall not overlap a Train Object.

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f83ca269-048c-4bb3-bfcc-089e2426d5d4/markdown_0/imgs/img_in_image_box_150_1368_869_1474.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A40%3A55Z%2F-1%2F%2F6254e2a4845007210635ddc0efc0f11a6a799b8abc7e450cfa8ddfd2c8b9f19a" alt="Image" width="60%" /></div>


This requirement only concerns the building of the Risk Path Candidate that is then checked through the requirement REQ-SC_RP_TERM

---

Operational Rules: None

Engineering Rules: None

## REQ- RPS_UTO

When the MBS builds a Risk Path and it finds an Unresolved Trackbound Object in the search direction, it shall set the end of the Risk Path at the border of the Unresolved Trackbound Object without overlapping it according to REQ_SC_RP_UTO.

Rationale: An Unresolved Trackbound Object is a possible point for a Risk Path termination but the Risk Path shall not overlap an Unresolved Trackbound Object.

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5cb449fb-f062-4390-874e-6144d6c9b470/markdown_0/imgs/img_in_image_box_158_600_1116_703.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A00Z%2F-1%2F%2F1ca1ffdbe51fdf7b5fbb21ca0e426f5db16ba62f291dbf332c730d6afe4c2c9e" alt="Image" width="80%" /></div>


This requirement only concerns the building of the Risk Path Candidate that is then checked through the requirement REQ-SC_RP_TERM

Operational Rules: None

Engineering Rules: None

## REQ- RPS_MP

When the MBS builds a Risk Path and it finds the end of a Movement Permission Extent in the search direction, it shall set the end of the Risk Path at the end of the Movement Permission Extent without overlapping it according to REQ_SC_RP_MP.

Rationale: The End of a Movement Permission Extent is a possible point for a Risk Path termination but the Risk Path shall not overlap a Movement Permission Extent.

Guidance:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5cb449fb-f062-4390-874e-6144d6c9b470/markdown_0/imgs/img_in_image_box_144_1289_1031_1388.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A00Z%2F-1%2F%2Fdc78a744897eadee69ae9bd4255d7fa9c009e192c9fbefaf7e3e0093f8b0b274" alt="Image" width="74%" /></div>


This requirement only concerns the building of the Risk Path Candidate that is then checked through the requirement REQ-SC_RP_TERM.

Note: this situation is possible only if there is no Risk Buffer for the Movement Permission protecting the Risk Path.

---

# Contract No. HE – 101102001

Operational Rules: None

Engineering Rules: None

## REQ- RPS_RB

When the MBS builds a Risk Path and it finds the end of a Risk Buffer in the search direction, it shall set the end of the Risk Path at the end of the Risk Buffer without overlapping it according to REQ_SC_RP_RB.

Rationale: The End of a Risk Buffer is a possible point for a Risk Path termination but the Risk Path shall not overlap a Risk Buffer.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The first layer of risk management.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'>The second layer of risk management.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The third layer of risk management.</td></tr>
  </tbody>
</table>

This requirement only concerns the building of the Risk Path Candidate that is then checked through the requirement REQ-SC_RP_TERM

---

Operational Rules: None

Engineering Rules: None

## REQ-RPS_DPS

When MBS builds a Risk Path, it shall set the end of the Risk Path to the end of a Track Edge if

• The requirements of SC_RP_TERM_DPS are fulfilled

- The DPS Group checked in SC-RP_TERM_DPS does not belong to the list of DPS Groups that shall not be used as a measure to mitigate the risk of flank collision for this Movement Permission

Rationale: For operational reasons, PE shall be able to mark certain DPS Groups that shall not be used for flank protection, so it remains flexible to be moved.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-RPS TE

When MBS builds a Risk Path, it shall set the end of the Risk Path to the end of a Track Edge if the Track Edge has no Track Edge Links.

Rationale: See SC_RP_TERM_TE

Guidance: See SC RP TERM TE

Operational Rules: None

Engineering Rules: None

## REQ-RPS NEAREST

When MBS builds a Risk Path, it shall use the closest possible terminating element

Rationale: The search for flank protection shall not be extended beyond an element that is already providing protection unless it is operationally necessary (i.e. excluded by the MP request received from PE).

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-RPS_DIST

---

When the MBS builds a Risk Path and no element to terminate is found after the configured search length rpMaxSearchDistance, MBS shall set the end of the Risk Path at the location where the search distance is reached.

Rationale: See SC_RP_TERM_DIST

Guidance: See SC_RP_TERM_DIST

Operational Rules: None

Engineering Rules: None

## REQ-RPS_SPLIT

When MBS builds the Risk Paths for a Movement Permission, a Risk Path overlaps the end of a Track Edge and the Risk Path is not terminated at this Track Edge, MBS shall ensure that a Risk Path is present for every Track Edge linked by a Track Edge Link going in the same direction as the Risk Path unless the linked Track Edge is covered by the same Movement Permission Extent.

Rationale: If the head of a point is facing the requested Movement Permission, the Risk Path shall cover both legs of the point. MBS derives n (usually 2) Risk Paths if it encounters a Track Edge from which it can continue to n Track Edges.

## Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>DPS</td><td style='text-align: center;'>DPS 1.2</td></tr>
    <tr><td style='text-align: center;'>TE1</td><td style='text-align: center;'>TEE1</td></tr>
    <tr><td style='text-align: center;'>TE2</td><td style='text-align: center;'>TEE2</td></tr>
    <tr><td style='text-align: center;'>DPS</td><td style='text-align: center;'>DPS 1.1</td></tr>
    <tr><td style='text-align: center;'>TE3</td><td style='text-align: center;'>TEE3</td></tr>
    <tr><td style='text-align: center;'>TE5</td><td style='text-align: center;'>TEE5</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>Risk Path</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>DPS in state FULL</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>DPS in state NONE</td></tr>
  </tbody>
</table>

TE2 is linked to TE3 and TE4, TE3 and TE4 have links to TE2 but not between them. As a Risk Path is present on TE2, one has to be present for Track Edges TE3 and TE4.

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Section</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>TE1</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>TE2</td><td style='text-align: center;'>DPS 1.1</td></tr>
    <tr><td style='text-align: center;'>TE3</td><td style='text-align: center;'>DPS 1.2</td></tr>
    <tr><td style='text-align: center;'>TE4</td><td style='text-align: center;'>DPS 2.2</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>DPS 1.2</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>DPS 2.1</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>DPS 2.2</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>DPS 2.1</td></tr>
  </tbody>
</table>

---

TE4 is linked to TE2 and TE3, TE2 and TE3 have links to TE4 but not between them. Although a Risk Path is present on TE3, none has to be present at TE4 as it is covered by the Movement Permission Extent itself.

Operational Rules: None

Engineering Rules: None

---

## REQ-SC_RP_TERM

MBS shall check that all Risk Paths build by the MBS are terminated at one of the following termination options:

• SC_RP_TERM_DPS

• SC_RP_TERM_RB

• SC_RP_TERM_MP

• SC_RP_TERM_RP

• SC_RP_TERM_TO

• SC_RP_TERM_UTO

• SC RP TERM DIST

• SC RP TERM TE

and if the check fails, MBS shall send a "RP_TERMINATION_INSUFFICIENT" reject code.

Rationale: Every possible path that leads to a flank protection risk has to be excluded and thus an element has to be identified that provides the risk mitigation measure.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-SC RP TERM DPS

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals the end of the DPS

- The overlap length between the Risk Path and the DPS is greater than zero.

• The overlapped DPS is in the state NONE

• The dependent DPS is in the state FULL

- The configuration attribute dpsProvidesFlankProtection is set to TRUE for the overlapped DPS

- The requested maximum speed at the location where the Risk Path originates from is equal to or lower than the speed configured in the attribute dpsMaxFlankProtectionSpeed for the DPS that is providing flank protection.

Rationale:

---

Points and derailers provide flank protection by means that no train can physically move towards the flank protection seeking element, if the path is set away from the side that needs protection (Check for FULL/NONE). In some cases, the abstracted DPS cannot physically provide flank protection (config variable flankProtection). For derailers a regulation exists (for example in Switzerland) that they must not be used if the speed of the to be protected train is higher than 120 km/h (variable maxFlankProtectionSpeed).

## Guidance:

The termination of the Risk Path was chosen to be the "inner end" of the DPS to have a) a clear point to terminate, b) be able to perform an overlap check if the DPSG is allowed to move or locked as it serves as a flank protection element and c) to distinguish the cases of a DPSG where it is used as a flank protection measure (and thus not able to move) from being in the flank protection area (and thus allowed to move).

Simple Example of one set of points:

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a8f76f87-5a7e-47c7-9d1d-6899ee406fa2/markdown_0/imgs/img_in_image_box_134_741_1108_1037.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A24Z%2F-1%2F%2Fde0774c12a21486b3e57a087adefe77e7e4f35a15e5e4233fe7b30f04a97f92d" alt="Image" width="81%" /></div>


<div style="text-align: center;">DPS 1.1 and 1.2 are in the same DPS Group and Flank Protection Group.</div>


Complex example of double slips:

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c1ce9653-2522-47a5-9fbb-5a2b3c637a85/markdown_0/imgs/img_in_image_box_147_166_993_629.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A28Z%2F-1%2F%2F10cd5919f9e2ac14c7b2d9da93ec744b7ed7e1a1545eecd7c348cfe0622aa3e6" alt="Image" width="71%" /></div>


Example of a double slip: DPS 1.1, 1.2, 1.3 & 1.4 are in DPS Group 1, DPS 2.1, 2.2, 2.3 & 2.4 are in DPS Group 2. The DPS (1.1 & 1.2), (1.3 & 1.4), (2.1 & 2.2) and (2.3 & 2.4) are dependent to each other. The DPS (1.1 & 1.3), (1.2 & 1.4), (2.1 & 2.3) and (2.2 & 2.4) are mechanically linked.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c1ce9653-2522-47a5-9fbb-5a2b3c637a85/markdown_0/imgs/img_in_image_box_118_805_1000_1277.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A28Z%2F-1%2F%2F0d857a80df689efb46286dc55fe28fcbf80ade46127ccff8f458a6f39efc5471" alt="Image" width="74%" /></div>


Operational Rules: None

Engineering Rules: TBD

REQ-SC_RP_TERM_RB

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals the end of a Risk Buffer

• There is no overlap between the Risk Path and the Risk Buffer

• The global variable rpTermAllowedAtRbAndMp is set to TRUE

---

- The attribute rpTermAtDpsOnly is FALSE for the Allocation section the Risk Path originates from

Rationale: The other train movement is supervised to not overpass the end of the Risk Buffer.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'>The first layer of risk management.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission</td><td style='text-align: center;'>The second layer of risk management.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The third layer of risk management.</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RP_TERM_MP

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals the end of a Movement Permission Extent

• There is no overlap between the Risk Path and the Movement Permission Extent

• The global variable rpTermAllowedAtRbAndMp is set to TRUE

- The attribute rpTermAtDpsOnly is FALSE for the Allocation section the Risk Path originates from

Rationale: The other train movement is supervised to not overpass the end of the Movement Permission Path Segment.

Guidance: None

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bdd621ed-3825-4c41-a36c-0bf4726b58cd/markdown_0/imgs/img_in_image_box_167_1165_893_1252.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A32Z%2F-1%2F%2F3b251ff0dadfa53015c66c29e791019c551d0c92f6d7c40ad61c3736b0aa33c5" alt="Image" width="60%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC_RP_TERM_RP

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals the end of a Track Edge

---

- All other linked Track Edges are covered by a Risk Path of the same Movement Permission

Rationale: A Risk Path can be terminated at points if another Risk Path of the same Movement Permission is present on the other leg of the point and continues on the head side.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Section</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>DPS1.1</td><td style='text-align: center;'>DPS 1.1</td></tr>
    <tr><td style='text-align: center;'>DPS1.2</td><td style='text-align: center;'>DPS 1.2</td></tr>
    <tr><td style='text-align: center;'>DPS2.1</td><td style='text-align: center;'>DPS 2.1</td></tr>
    <tr><td style='text-align: center;'>DPS2.2</td><td style='text-align: center;'>DPS 2.2</td></tr>
    <tr><td style='text-align: center;'>DPS3.1</td><td style='text-align: center;'>DPS 3.1</td></tr>
    <tr><td style='text-align: center;'>DPS3.2</td><td style='text-align: center;'>DPS 3.2</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>Risk Path</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>DPS in state FULL</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>DPS in state NONE</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RP_TERM_TO

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals one end of a Train Object

• There is no overlap between the Risk Path and the Train Object

- The global variable rpTermAllowedAtTo is set to TRUE.

- The attribute rpTermAtDpsOnly is FALSE for the Allocation section the Risk Path originates from

Rationale: A Train Object is only created for trains that are communicating through ETCS and are thus supervised to not move unintentionally.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'>The training data.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The路演路径.</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: None

## REQ-SC_RP_TERM_UTO

A Risk Path is correctly terminated if the following conditions are met:

---

- The end of the Risk Path equals one end of an Unresolved Trackbound Object

• There is no overlap between the Risk Path and the Unresolved Trackbound Object

- The requested maximum speed at the location where the Risk Path originates from is equal to or lower than a globally configured variable rpTermMaxSpeedUto

- The length of the Risk Path is equal to or greater than the minimal length required for the requested maximum speed at the location where the Risk Path originates from

• The global variable rpTermAllowedAtUto is set to TRUE

- The attribute rpTermAtDpsOnly is FALSE for the Allocation section the Risk Path originates from

Rationale: A parked vehicle not reporting to the MBS is not expected to move and thus the risk of a flank movement could be acceptable if the speed is low enough.

## Guidance:

The minimal length for the Risk Path is configured in MBS with a lookup table with speed brackets and the minimum length as columns.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//49486fa0-c7e8-4159-a37a-89c80aace503/markdown_0/imgs/img_in_image_box_208_903_1018_994.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A41%3A42Z%2F-1%2F%2F0545b8155d75b35e72e6ce8a31e3e26cf52e894a525cdfb339cdc479ae43d574" alt="Image" width="68%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-SC_RP_TERM_TE

A Risk Path is correctly terminated if the following conditions are met:

- The end of the Risk Path equals the end of a Track Edge

• The Track Edge has no Track Edge Links

Rationale: If the stretch between the Allocation Section and the track net is free of vehicles, the movement cannot be endangered.

Guidance:

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Section</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>Risk Path</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>DPS in state FULL</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>DPS in state NONE</td></tr>
  </tbody>
</table>

Engineering Rules: None

## REQ-SC RP TERM DIST

A Risk Path is correctly terminated if the following conditions are met:

- The maximum search distance according to the global variable rpMaxSearchDistance is reached

- The global variable rpTermAllowedAfterMaxDistance is set to TRUE.

Rationale: An unterminated search could result in quite long search paths. If the distance is long enough, it is unlikely that a vehicle arriving from that side would endanger the train.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Stage</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>1</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>2</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>3</td><td style='text-align: center;'>Risk Path</td></tr>
    <tr><td style='text-align: center;'>4</td><td style='text-align: center;'>DPS in state FULL</td></tr>
    <tr><td style='text-align: center;'>5</td><td style='text-align: center;'>DPS in state NONE</td></tr>
  </tbody>
</table>

Operational Rules: None

Engineering Rules: A safety consideration is to be done for the concrete value of the minimum distance.

## REQ-SC_RP_TO

The MBS shall check that no Risk Path overlaps any Train Location of a Train Object.

---

Rationale: The area between the danger point and the flank protection providing element shall be clear of vehicles.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Train Object</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

Note: The DPS states are only shown for completeness

Operational Rules: None

Engineering Rules: None

## REQ-SC RP UTO

The MBS shall check that no Risk Path overlaps any Unresolved Trackbound Object.

Rationale: The area between the endangerment point and the flank protection providing element shall be clear of vehicles.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Unresolved Trackbound Object</td><td style='text-align: center;'>The first level of resolution.</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>The second level of resolution.</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>The third level of resolution.</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>The fourth level of resolution.</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>The fifth level of resolution.</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>The fifth level of resolution.</td></tr>
  </tbody>
</table>

Note: The DPS states are only shown for completeness.

Operational Rules: None

Engineering Rules: None

---

The MBS shall check that no Risk Path overlaps any Movement Permission Extent of another train.

Rationale: The area between the endangerment point and the flank protection providing element shall be clear of movements.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Section</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>DPS</td><td style='text-align: center;'>DPS 1.2</td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'>Allocation Section</td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'>Movement Permission Extent</td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'>Risk Path</td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'>DPS in state FULL</td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'>DPS in state NONE</td></tr>
  </tbody>
</table>

Note: The DPS states are only shown for completeness

Operational Rules: None

Engineering Rules: None

## REQ-SC RP RB

The MBS shall check that no Risk Path overlaps any Risk Buffer of another train.

Rationale: The area between the danger point and the flank protection providing element shall be clear of movements.

Guidance:

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>Component</th><th style='text-align: center;'>Description</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>Risk Buffer</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Allocation Section</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Movement Permission Extent</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>Risk Path</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state FULL</td><td style='text-align: center;'></td></tr>
    <tr><td style='text-align: center;'>DPS in state NONE</td><td style='text-align: center;'></td></tr>
  </tbody>
</table>

Note: The DPS states are only shown for completeness

Operational Rules: None

Engineering Rules: None

---

### 6.12 AUTHORISE COOPERATIVE SHORTENING REQUEST

#### 6.12.1 Overview

This function is responsible to assess the safety of a request to co-operatively shorten the Movement Authority of a train. The MBS shall not alter the request if certain parameters are incorrect but only report the failure to PE with the failure reason.

The Cooperative Shortening Request shall contain the following information:

Train Object Identifier

- Requested Stop Location

Risk Buffer (LinkedPath)

#### 6.12.2 Inputs

Cooperative Shortening Request message according to I_PE

- Domain Object State

#### 6.12.3 Outputs

- Message “request granted” according to I_PE

- Message “request rejected” according to I_PE

---

#### 6.12.4 Functional requirements

## REQ-SAFETY-COOPERATIVE

The MBS shall perform a series of checks given by the following ordered list when it receives a Cooperative Shortening Request indicating a request to co-operatively shorten an MA through I_PE:

1. REQ-SYNTAX (see 'Authorise MP Request')

2. REQ-TOPO1 (see 'Authorise MP Request')

3. REQ-TOPO2 (see 'Authorise MP Request')

4. REQ-COOP TO EXIST

5. REQ-COOP FS OR OS

6. REQ-STOP LOCATION IN REAR OF EOA

7. REQ-COOP TRANSLATE

8. REQ-COOP RISK BUFFER

9. REQ-COOP_PENDING

Rationale: The request to allow a train movement shall be safeguarded.

Guidance: This is the top requirement for all necessary checks.

Operational Rules: None

Engineering Rules: None

## REQ-COOP-FAILS

The MBS shall abort checking a Cooperative Shortening Request received through I_PE if any performed safety check fails and send a "REQUEST_REJECTED" reply.

Rationale: A safety check could require the correct execution of a previous safety check.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-COOP-SUCCESSFUL

If none of the safety checks fails, MBS shall send an “REQUEST_GRANTED” reply.

Rationale: By this message, PE is informed that the MBS accepts its request and sends the corresponding Request to Shorten MA message to the OBU.

Guidance: None

Operational Rules: None

---

Engineering Rules: None

## REQ-COOP_TO_EXIST

The MBS shall check that the Train Object referenced in the Cooperative Shortening Request exists and if the check fails, the MBS shall send a "COOP_TO_NOT_EXISTENT" reject code.

Rationale: A co-operative shortening can be only applied to a train known to the MBS.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-COOP FS OS

The MBS shall check that the mode of the train is either FS or OS and if the check fails, the MBS shall send a "COOP_INVALID_MODE" reject code.

Rationale: The OBU does not accept a Request to Shorten MA message in other modes (supported by the MBS) according to chapter 4.8.4 (/ETCS/).

Guidance: According to chapter 4.8.4 (/ETCS/), an OBU would also accept a Request to Shorten MA message in the modes LS and AD, but those modes are not in scope of the System Specification of the MBS yet.

Operational Rules: None

Engineering Rules: None

## REQ-STOP LOCATION IN REAR OF EOA

The MBS shall check that the requested stop location of the Cooperative Shortening Request is located within the currently stored Movement Permission and if the check fails, the MBS shall send a COOP NOT IN REAR reject code.

Rationale: According to chapter 4.8.4 (ETCS/), MBS should propose a shortened MA with an EOA closer to the train than the current EOA/LOA.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-COOP TRANSLATE

The MBS shall translate the requested MP into a Request to Shorten MA message as if it was granted by the MBS and if the translation from a Movement Permission into a Request to Shorten MA message fails, MBS shall send a "COOP MA CONSTRUCTION FAILED" reject code.

---

# Contract No. HE – 101102001

Rationale: The generation of a Request to Shorten MA may fail if e.g. the extent in the requested Movement Permission is located in rear of the current LRBG of the train (since a Request to Shorten MA message cannot be sent with a shifted location reference according to /ETCS/).

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-COOP RISK BUFFER

The MBS shall perform all checks related to the Risk Buffer contained in the Cooperative Shortening Request of the function 'Authorise MP Request' and if one of the check fails, the MBS shall send the corresponding reject code.

Rationale: The Cooperative Shortening Request can contain a Risk Buffer and therefore the (safety) checks for the Risk Buffer have to be performed.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-COOP_PENDING

The MBS shall check that there is no pending co-operative shortening for the referenced train in the Cooperative Shortening Request and if the check fails, the MBS shall send a "COOP_PENDING" reject code.

Rationale: It is considered as unlikely that PE would trigger several co-operative shortenings at the same time for one train. Thus, when MBS would allow this, this would unnecessarily the complexity of the MBS system.

Guidance: None

Operational Rules: None

Engineering Rules: None

### 6.13 SysF Translate MP Request to Movement Authority

#### 6.13.1 Overview

To control the train movement in an ETCS based system, the on-board equipment shall receive a Movement Authority.

---

This function converts the authorised Movement Permission into a Movement Authority and transmits it to the on-board.

#### 6.13.2 Inputs

• Authorised Movement Permission

• Domain Object State

#### 6.13.3 Outputs

• Message Movement Authority according to I OBU

---

#### 6.13.4 Functional requirements

## REQ-0048

When a valid Movement Permission is received, the MBS shall translate the Movement Permission into a Movement Authority.

Rationale: The MA is supplied to the on-board to allow the on-board equipment to control the train movement. The Movement Permission has to be supplied to the OBU as a Movement Authority in compliance with the interface I OBU.



Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0049

The End of Movement Authority shall be the location at the end of the Movement Permission Extent.

Rationale: The End of Movement Authority is the target of the Movement Permission and the Risk Buffer starts from there.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0050

The Target Speed at the End of Movement Authority shall be zero.

Rationale: Target speed is set to 0 and Risk Buffer starts just after.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0051

If a Risk Buffer is present in the Movement Permission, the Danger Point of the Movement Authority shall be a location at a fixed distance (safe margin) in rear of the end of the Risk Buffer.

Rationale: The danger point is the Supervised Location that the train shall not overpass. A safe margin is nevertheless added to consider some degraded cases (see Guidance).

---

Guidance: The safe margin (defined at Project Level) considers that it is not always guaranteed that the train stops in rear of the Danger Point if certain assumptions are not fulfilled e.g.:

- That the available wheel-rail adhesion is better than or equal to that assumed in the ETCS braking curve calculation.

- That the train does not accelerate on approach to the EOA (release speed calculation assumes no acceleration).

- That the compensation of speed measurement inaccuracy is not inhibited by national value.

If any of these assumptions are not true, then the SvL protection is not guaranteed by the ETCS OBU. The safe margin provides a mitigation in case any of these assumptions is not fulfilled.

The safe margin also considers the risk associated with the potential rollback of a chased train and the train overhang (between the TTD border and the physical train end).

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0a22afd8-4b78-47a4-943b-270fbbe04ea8/markdown_0/imgs/img_in_image_box_126_752_1127_955.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A42%3A25Z%2F-1%2F%2F288efaf267bdefd5d57041466e331b0dcaccac06f3028847967ce06c1cc41e3f" alt="Image" width="84%" /></div>


Operational Rules: None

Engineering Rules: None

## REQ-0052

If a danger point is defined, the release speed shall be calculated (Project Specific) based on the information contained in the Movement Permission.

Rationale: The release speed as such is an operational decision.

Guidance: The release speed value impacts the length of the associated Risk Buffer.

For example, based on the Project decision, the Release speed can be:

- Set to 0 or to the specific value «calculated on board».

- Set to a value dependent on the Risk Buffer length and/or the train category.

Operational Rules: None

Engineering Rules: None

---

Movement Authority shall be defined without an overlap.

Rationale: The use of overlap is considered as not needed. Once the train is at standstill, it should be possible for the PE to request to reduce the Risk Buffer by Cooperative Shortening Movement Authority if there is an operational need to do so.

Guidance: None.



Operational Rules: None

Engineering Rules: None

## REQ-0055

Movement Authority shall be defined without section timers.

Rationale: No section timers are foreseen within an MA derived from a Movement Permission. The release of a Movement Permission must always be carried out by Cooperative Shortening Movement Authority

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0056

The Mode Profiles defined inside the Movement Permission shall be included inside the Movement Authority.

Rationale: The mode profiles shall be transmitted to the on-board equipment to control the train movement (see /ETCS/ - SUBSET-026).

Guidance: The mode profile distance and length sent in the Movement Authority corresponds the mode extent defined in the Movement Permission. The other Mode Profile parameters are Project Specific.

Operational Rules: None

Engineering Rules: None

## REQ-0057

The track description (excluding SSP) and linking information included inside the Movement Authority shall correspond to the Domain Data, that is entirely or partly covering the Train Location and Movement Permission (Risk Buffer included).

Rationale: Track description covering the minimum safe rear end (to avoid message entry in OS/FS) and the whole distance defined by the MA is supplied to

---

the on-board to allow the on-board equipment to control the train movement. SSP is covered by requirement REQ-0066.

## Guidance:

Track description includes the following information (see /ETCS/ - SUBSET-026 chapter 3.7)

• The gradient profile.

• Optionally Speed restriction to ensure a given permitted braking distance.

• Optionally track conditions.

• Optionally route suitability data.

• Optionally areas where reversing is permitted.

• Optionally changed adhesion factor.

Linking information when available.

Axle load speed profile is ignored here as it will be covered by the SSP in the MBS solution.

When extending or modifying an existing MA, it is sufficient to only include the modified extended part not yet acknowledged by the OBU.

Operational Rules: None

Engineering Rules: None

## REQ-0066

The Static Speed Profile (SSP) included inside the Movement Authority shall correspond to the speed values given in the requested Movement Permission.

Rationale: Track description covering the minimum safe rear end (to avoid message entry in OS/FS) and the whole distance defined by the MA is supplied to the on-board to allow the on-board equipment to control the train movement.

The speed in the requested Moving Permission is safe since the requirements REQ-SC MP SPEED and REQ-SC RB SPEED have been successfully applied before.

Guidance: When extending or modifying an existing MA, it is sufficient to only include the modified extended part not yet acknowledged by the OBU.

Operational Rules: None

Engineering Rules: None

REQ-0058

---

MBS shall request acknowledgement of the reception of each Movement Authority (variable M_ACK is set to 1 inside the MA message).

Rationale: The Movement Authority has to be acknowledged by the OBU to confirm it is well received.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0059

MBS shall send the translated Movement Authority to the corresponding ETCS on-board equipment according to the I_OBU interface.

Rationale: The MA is supplied to the train to allow the ETCS on-board equipment to control the train movement

Guidance: None.

Operational Rules: None

Engineering Rules: None

### 6.14 SysF Translate Cooperative Shortening Request to Request to Shorten MA

#### 6.14.1 Overview

To co-operatively shorten the movement authority of a train, a Request to Shorten MA message shall be sent to the train.

This function converts the authorised Cooperative Shortening Request into a Request to Shorten MA message and transmits it to the on-board.

#### 6.14.2 Inputs

• Authorised Cooperative Shortening Request

• Domain Object State

#### 6.14.3 Outputs

• Message Request to Shorten MA according to I OBU

---

#### 6.14.4 Functional requirements

REQ-0067

When a valid Cooperative Shortening Request is received, the MBS shall translate the Movement Permission into a Request to Shorten MA message.

Rationale: To co-operatively shorten the movement authority of a train, a Request to Shorten MA message shall be sent to the train.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0068

The MBS shall apply the requirements REQ-0049, REQ-0050, REQ-0051, REQ-0052, REQ-0053, REQ-0055, REQ-0056 from the function "Translate MP Request to Movement Authority" using the existing Movement Permission with the new stop location and the risk buffer for the translation of the Request to Shorten MA message.

Rationale: A Request to Shorten MA message sent by MBS contains packet 15 and optionally packet 80. Thus, only a subset of the requirements of “Translate MP Request to Movement Authority” is applied.

Guidance: None.

Operational Rules: None

Engineering Rules: None

## REQ-0069

MBS shall send the translated Request to Shorten MA message according to the I_OBU interface.

Rationale: The Request to Shorten MA is supplied to the train to trigger the co-operative shortening of MA procedure to the ETCS on-board equipment.

Guidance: None.

Operational Rules: None

Engineering Rules: None

### 6.15 SysF Delete Train Object

#### 6.15.1 Overview

When a Train Object inside the AoC is deleted from the MBS, the Train Location for this Train Object is replaced by an Unresolved Trackbound Object to manage the occupation of the track.

---

#### 6.15.2 Inputs

• Trigger (by Terminate communication session with OBU)

#### 6.15.3 Outputs

• Train Object (removed)

• Train Location (removed)

• Unresolved Trackbound Object

#### 6.15.4 Functional Requirements

## REQ-TrainLoc-10

[X2R5 REQ-TrainLoc-10]

When the communication session with a leading OBU is terminated for trackside, then the MBS shall:

- create an Unresolved Trackbound Object corresponding to the Train Location extended to the end of the Movement Permission.

- store the Train Length (L_TRAIN) in the created Unresolved Trackbound Object if the train is marked as integrity confirmed

• delete the Train Location and the Movement Permission

## Rationale:

The MBS cannot determine the Train Location for a train when the communication session has been terminated or is considered terminated.

## Guidance:

Communication session is terminated for trackside according to /ETCS/ - SUBSET-26 chapter 3.5.5 and 3.5.4.2.1

If the train was within or partially within the Area of Control when the communication session was closed, then even though the Train Location is removed, the Unresolved Trackbound Object for the train will remain.

A leading OBU is an OBU not in SL, NL.

Operational Rules: None

Engineering Rules: None

---

## REQ-0065

[X2R5 REQ-TrainLoc-10]

When the communication session is terminated for trackside and when the Train Location has been deleted, then the MBS shall delete the Train Object.

Rationale:



The MBS cannot determine the Train Location for a train when the communication session has been terminated or is considered terminated.

Guidance:

Communication session is terminated for trackside according to /ETCS/ - SUBSET-26 chapter 3.5.5 and 3.5.4.2.1.

If the train was within or partially within the Area of Control when the communication session was closed, then even though the Train Location is removed, the Unresolved Trackbound Object for the train will remain.

Operational Rules: None

Engineering Rules: None


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>REQ-TrainLoc-11</td><td style='text-align: center;'>FOR FURTHER RELEASE</td><td style='text-align: center;'>[X2R5 REQ-TrainLoc-11]</td></tr><tr><td colspan="3">The MBS shall remove the Train Location for a train which has completely left the Area of Control.</td></tr><tr><td colspan="3">Rationale:</td></tr><tr><td colspan="3">The MBS does not need to maintain a Train Location for trains beyond its Area of Control.</td></tr><tr><td colspan="3">Guidance:</td></tr><tr><td colspan="3">This applies to both Handovers and Transitions.</td></tr><tr><td colspan="3">How the removal is achieved is project specific. Options include:</td></tr><tr><td colspan="3">• Monitoring the Train Location for a train which is leaving the Area of Control, until it is completely beyond the boundary of the Area of Control.</td></tr><tr><td colspan="3">• Truncating the Train Location at the boundary for a train which is leaving the Area of Control, until it has zero length within the Area of Control.</td></tr><tr><td colspan="3">It is also possible to use short TTD sections at boundaries of the Area of Control to determine when a train has left the area.</td></tr><tr><td colspan="3">Projects may decide to maintain the Train Location beyond the border until ordering the train to terminate the communication session.</td></tr><tr><td colspan="3">Projects may decide to implement different solutions at different borders of the Area of Control.</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td><td style='text-align: center;'></td></tr></table>

---

### 6.16 SysF Request Movement Permission

#### 6.16.1 Overview

When the MBS receives an MA Request message, then the OBU indicates that e.g., the driver has pressed the start button or that the time before reaching perturbation location is reached. In the first case, this additionally indicates that both the OBU and the driver are ready to accept authorisations (e.g. Movement Authority or SR Authorisation).

Therefore, the MBS shall forward each MA Request message received from OBU to the PE by sending an Authorisation Requested message.

#### 6.16.2 Inputs

MA Request message

#### 6.16.3 Outputs

Authorisation Requested message

#### 6.16.4 Functional requirements

## REQ-0044

When the MBS receives an MA Request message from the OBU, then the MBS shall send an Authorisation Requested message to the PE indicating the reason for this request (e.g. driver has pressed the start button)

## Rationale:

This is necessary to indicate to the PE that e.g., the driver has pressed the start button or the time before reaching perturbation location is reached.

Based on this information, the PE or TMS may decide to send a Movement Permission to the MBS or not.

Guidance: None

Operational Rules: None

Engineering Rules: None

---

### 6.17 GENERAL REQUIREMENTS


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">REQ-0045</td></tr><tr><td colspan="2">The MBS shall be able to perform all the functions of the RBC Basic Interoperability Constituent (IC) in the Control-Command and Signalling Trackside Subsystem (see /BalnCon/)</td></tr><tr><td style='text-align: center;'>Rationale:</td><td style='text-align: center;'>From ETCS point of view, the MBS is an RBC Basic Interoperability Constituent (IC). The MBS supplier shall supply an RBC-IC NoBo Certificate for his MBS Product.</td></tr><tr><td style='text-align: center;'>Guidance:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>REQ-0010</td><td style='text-align: center;'>FOR FURTHER RELEASE</td></tr><tr><td colspan="2">MBS shall log all incoming and outgoing messages to the I_DIAG interface.</td></tr><tr><td style='text-align: center;'>Rationale:</td><td style='text-align: center;'>This is requested for diagnostic.</td></tr><tr><td style='text-align: center;'>Guidance:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>REQ-0046</td><td style='text-align: center;'>FOR FURTHER RELEASE</td></tr><tr><td colspan="2">If an OBU message has to be acknowledged (M_ACK = 1), MBS shall repeat this message periodically until the OBU acknowledgement is received.</td></tr><tr><td style='text-align: center;'>Rationale:</td><td style='text-align: center;'>MBS should send again a message if the OBU acknowledgement is not received after a period, because there is a risk that the OBU has not received the message.</td></tr><tr><td style='text-align: center;'>Guidance:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Operational Rules:</td><td style='text-align: center;'>None</td></tr><tr><td style='text-align: center;'>Engineering Rules:</td><td style='text-align: center;'>None</td></tr></table>

#### 6.18.1 Overview

#### 6.18.2 Inputs

- Train Location

“Request to shorten MA is granted message” according to I OBU

“Request to Shorten MA is rejected message” according to I_OBU

---

#### 6.18.3 Outputs

- Movement Permission

- Message “Cooperative MP Request Granted” according to I PE



- Message “Cooperative MP Request Rejected” according to I_PE

#### 6.18.4 Functional requirements

REQ-0070

After MBS has granted a Movement Permission, it shall store the new Movement Permission as the current MP of the corresponding Train Object.

Rationale: A Movement Permission that has been granted shall become the currently active Movement Permission of a Train Object.

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0071

When there is an update of the Train Location then MBS shall modify the Movement Permission so that the start of the Movement Permission equals the rear of the Train Location.

Rationale: This ensures that any parts of the track that are not used by the train anymore can be (re-)used for train movements of other trains.

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-0072

When MBS receives a “Request to Shorten MA is granted” message, then MBS shall modify the Movement Permission so that the end of the Movement Permission Extent equals the requested stop location and the Risk Buffer corresponds to the one received in the Cooperative Shortening Request, and subsequently informs PE by sending the “Cooperative MP Request Granted” message.

Rationale: When MBS has received the “Request to shorten MA is granted” message, then this implies that the train has accepted the new MA. Thus, the old part of the MA won’t be used by the train anymore and hence can be used for other train movements (e.g. for joining purposes)

The “Cooperative MP Request Granted” message is sent to explicitly inform PE that the co-operative shortening of MA was successful.

---

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-0074

When MBS receives a “Request to Shorten MA is rejected” message then MBS shall provide this information by sending the “Cooperative MP Request Rejected” message to PE.

Rationale: As the OBU has not accepted the new MA in this case, the Movement Permission must not be updated. The message “Cooperative MP Request Rejected” is sent to explicitly inform PE that the co-operative shortening of MA was not successful.

Guidance: None

Operational Rules: None

Engineering Rules: None

#### 6.18.5 Functional requirements for Risk Path update

REQ-0075

When any part of the Movement Permission is updated or deleted, if an Allocation Section does not overlap the Movement Permission Extent anymore, MBS shall delete the Risk Paths calculated from the dependent Allocation Section according to REQ-RP_SEARCH.

Rationale: Flank Protection is not needed anymore if the Allocation Section does not overlap the path anymore.

Guidance: None

Operational Rules: None

Engineering Rules: None

REQ-0076

MBS shall continuously monitor that every Risk Path is terminated according to REQ-SC_RP_TERM and if a Risk Path is not terminated correctly anymore, the Risk Paths of its associated Movement Permission shall be recalculated according to REQ-RP_SEARCH.

Rationale: If the risk mitigation method is not valid anymore, MBS shall search if other appropriate measures are still in place.

Guidance: This version of the requirement does not assume any degraded modes or violation of operational rules.

---

## Operational Rules: None

REQ-0077

MBS shall continuously monitor that every Risk Path has no overlap according to

• REQ-SC RP TO

• REQ-SC RP UTO

• REQ-SC RP MP

• REQ-SC RP RB

and if an overlap is found, the Risk Paths of its associated Movement Permission shall be recalculated according to REQ-RP_SEARCH.

Rationale: If area between the Allocation section and the Risk Path terminating object is not free of vehicles or movements, the situation has to be reassessed.

Guidance: This version of the requirement does not assume any degraded modes or violation of operational rules.

Operational Rules: None

### 6.19 SysF SUPERVISE<Actor>Communication

Hint: <Actor> is a template for DR, TACS, PE, and OBU

#### 6.19.1 Overview

This function supervises the communication state to the actor <actor>. It can detect, if the communication is established, lost (a communication never established is also considered as 'lost') established, and if there is change lost -> established or established -> lost.

#### 6.19.2 Inputs

State of communication session between MBS and actor <actor>

6.19.3 Outputs

Events

• <actor>CommEstablished or

• <actor>CommLost

---

#### 6.19.4 Functional requirements

REQ-1001

MBS shall observe the state of the communication between MBS and the actor <actor> and

- send the internal event <actor>CommEstablished when it detects that the communication session state changed from lost to established;

- send the internal event <actor>CommLost when it detects that the communication session state changed from established to lost.

Hint: For the OBU, the event OBUCommLost occurs when the communication session is lost in the sense of /ETCS/ SS026 3.5.4.2.1

Rationale: Central place to supervise communication and let other capabilities react on this with the appropriate measure.

Guidance: The check can be performed by a main loop pattern centrally in MBS.

Operational Rules: None

Engineering Rules: None

### 6.20 SysF ESTABLISH<Actor>Communication

Hint: <Actor> is a template for DR, TACS, PE, and OBU

#### 6.20.1 Overview

This function establishes the communication state to the actor <actor> according to the related communication protocol.

#### 6.20.2 Inputs

None

#### 6.20.3 Outputs

(Changed) communication session state to <actor>.

---

# Contract No. HE – 101102001

#### 6.20.4 Functional requirements

REQ-1002

When MBS detects that there is no communication established with actor <actor> AND MBS is in the role of the initiator of that communication, MBS shall establish the communication to <actor> actor according to the related communication protocol.

Rationale: None

Guidance: The check can be performed by a main loop pattern centrally in MBS.

Operational Rules: None

Engineering Rules: None

## 7 INTERFACE SPECIFICATIONS

### 7.1 DESCRIPTION OF THE EXTERNAL INTERFACE I TACS

#### 7.1.1 Role of the external interface

The interface I_TACS allows the Moving Block System:

- to send commands to the TACS to move switchable TAs to the required state, and

• to receive from the TACS the state of the TA.

Indeed, to enable a train run from A to B, the Moving Block System commands to the TACS the setting of the TA to the required state to allow the movement of the train from A to B.

To manage the train positioning and the movement of the trains, the Moving Block System also needs to acquire through the TACS the state of all the TA inside its Area of Control (AoC.)

The interface I_TACS covers the following interfaces defined in EULYNX:

• Subsystem – Train Detection System (SCI-TDS) if TTD is used

• Subsystem – Point (SCI-P)

---

#### 7.1.2 Overview

## REQ-0021

According to Project Configuration, the I_TACS interface shall implement TLS over TCP of the EULYNX Process data interface, as specified in the chapter 3 of /EuArch/.

According to EULYNX, TACS communicates either by UDP or TLS over TCP. For new components, it is highly recommended to use TLS over TCP.

Guidance: None.

Operational Rules: None

Engineering Rules: None

#### 7.1.3 Physical level

Not applicable, as the hardware definition of MBS is out of scope of the current specification.

#### 7.1.4 Protocol level

## REQ-0022

The lower layers (network layer, data link layer) of the I_TACS interface shall be compliant with /POS/.

Rationale: None

Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0023

The higher protocol layers (transport layer, safety, retransmission and redundancy layer and application layer) of the I_TACS interface shall be compliant with /POS//SCI/.

Rationale: I TACS is according to the EULYNX specification

Guidance: None

Operational Rules: None

Engineering Rules: None

---

#### 7.1.5 Application level

## REQ-0024

The application layer of the I_TACS generic interface shall be compliant with /SCI-Gen/ and /SCI-GenIF/.

Rationale: I_TACS is according to the EULYNX specification



Guidance: None

Operational Rules: None

Engineering Rules: None

## REQ-0025

The application layer of the I_TACS interface shall be compliant with /SCI-P/ for Point.

Rationale: I_TACS is according to the EULYNX specification

Guidance: None

Operational Rules: None

Engineering Rules: None

---

## REQ-0026

The application layer of the I_TACS interface shall be compliant with /SCI-TDS/ for Train Detection System.

Rationale: None

Guidance: None

Operational Rules: None

Engineering Rules: None

#### 7.1.6 Input Application Layer Messages

• EULYNX telegrams from TACS Point:

☐ Msg_Point_Position : Message "Point Position"

○ Msg_timeout : Message “Timeout” – FOR FURTHER RELEASE

○ Msg_Ability_To_Move_Point : Message “Ability To Move Point” – FOR FURTHER RELEASE

• EULYNX telegrams from TACS Train Detection System:

○ Msg_TVPS_Occupancy_Status : Message “TVPS_Occupancy_Status”

#### 7.1.7 Output Application Layer Messages

• EULYNX telegrams to TACS Point:

☐ Cd Move point : Command "Move Point"

#### 7.1.8 Implicit choices and justification

EULYNX protocol shall be implemented for I TACS interface for the final target Baseline.

### 7.2 DESCRIPTION OF THE EXTERNAL INTERFACE I_PE

#### 7.2.1 Role of the external interface

The interface I_PE allows the Moving Block System:

- to receive commands from the PE to supervise the TACS and trains according to the line operational needs defined by TMS, and

- to send information to PE to allow the line operation.

In the current version of the specifications, only the application layer messages are listed.

#### 7.2.2 Overview

#### 7.2.3 Physical level

Not applicable

---

#### 7.2.4 Protocol level

Out of scope for this Release

#### 7.2.5 Application level

Out of scope for this Release

#### 7.2.6 Input Application Layer Messages

DPS Group Request

Movement Permission Request

Cooperative Shortening Request

#### 7.2.7 Output Application Layer Messages

Request Granted (request id)

This message indicates that a request has been successfully granted by MBS and is now being processed.

Request Rejected (request id, reason)

MBS Operational State Report (Object Id, reported state)

Authorisation Requested (Train Id, MA request reason)

Cooperative MP Request Granted

Cooperative MP Request Rejected

#### 7.2.8 Implicit choices and justification

Not applicable

### 7.3 DESCRIPTION OF THE EXTERNAL INTERFACE I OBU

#### 7.3.1 Role of the external interface

The main objective of this interface is to provide movement authorities to allow the safe movement of trains on the Railway infrastructure area under the responsibility of the MBS.

In the current /ETCS/, this interface corresponds to the RBC - OBU interface.

The MBS can be interfaced to the FRMCS and/or GSM-R radio communication network(s).

#### 7.3.2 Overview

#### 7.3.3 Physical level

Not applicable

---

#### 7.3.4 Protocol level

## REQ-0047

The protocol layers of the I_OBU interface shall be compliant with /ETCS/ - SUBSET-037.

Rationale: None

Guidance: None

Operational Rules: None

Engineering Rules: None

#### 7.3.5 Application level

REQ-0060

The application layer of the I_OBU generic interface shall be compliant with /ETCS/SUBSET-026, especially with Chapter 7 – ERTMS/ETCS language and Chapter 8 – Messages.

Rationale: I OBU is according to the SUBSET-026 RBC - OBU interface.

Guidance: None

Operational Rules: None

Engineering Rules: None

#### 7.3.6 Input Application Layer Messages

See /ETCS/ - SUBSET-026 chapter 8.6, Definition of Radio Messages from Train to Track

#### 7.3.7 Output Application Layer Messages

See /ETCS/ - SUBSET-026 chapter 8.7, Definition of Radio Messages from Track to Train

#### 7.3.8 Implicit choices and justification

Not applicable

### 7.4 DESCRIPTION OF THE EXTERNAL INTERFACE I DR

#### 7.4.1 Role of the external interface

By this interface, MBS gets the static Topology Data. This is the case both at startup and during run-time where there is the possibility to update existing Topology Data to a new version. Particularly it is possible to exchange a part of existing Topology Data e.g. as result of construction work.

#### 7.4.2 Overview

Until release 4, Topology Data will cover the whole Area of Control and will immediately be valid (activated) after reception.

---

In a further release, Topology Data can cover an arbitrary part of the Area of Control and follow a lifecycle:

• First, they will be distributed (pre-loaded)

Then, MBS will be asked for authorisation of the Topology Data activation where it checks for conflicting Movement Permissions and if there is no conflict, establishes a Usage Restriction Area to keep the updated area free of future Movement Permissions until the activation is finished

- Then, Topology Data become pre-activated and MBS can start to synchronise with the TACS (of changed or new Trackside Assets)

- Finally, MBS is asked for activation, removes the Usage Restriction Area and uses the new data from now on

#### 7.4.3 Physical level

Not applicable

#### 7.4.4 Protocol level

Out of scope for current Release.

#### 7.4.5 Application level

Out of scope for current Release.

All messages carry this generic header

• Parameter: messageNumber (unique identifier of the message type)

• Parameter: messageLength (total length of message)

• Parameter: dateTime (sending date and timestamp of message)

Further on, the parameter consumerId will be the unique identification of MBS (configurable value). The parameter DomainId is under discussion. It currently pretends that updateable Topology Data areas are fixed (pre-configured) but it shall be achieved that any sub-area, which cannot be predefined, shall be updateable. Until clarification it is used below, but the inherent future meaning shall be that the Topology Data themselves (parameter requestedDomainData are such that they allow identification of what sub-area they are replacing; the DomainId would then not be needed anymore.

Hint: for the mismatch of Topology Data and Domain Data (reflected in message names below) see the glossary entry for Domain Data.

#### 7.4.6 Input Application Layer Messages

7.4.6.1 Domain Data

• Parameter: header

• Parameter: consumerId

• Parameter: DomainId

---

##### 7.4.6.2 Domain Data Version Check Acknowledgement

• Parameter: header

• Parameter: DomainId (not used in current Release and under discussion)



• Parameter: DomainVersion (not used in current Release)

##### 7.4.6.3 Activation Command

• Parameter: header

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: DomainVersion (not used in current Release)

##### 7.4.6.4 Activation Commit Status

• Parameter: header

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: DomainVersion (not used in current Release)

• Parameter: activationCommitStatus

#### 7.4.7 Output Application Layer Messages

##### 7.4.7.1 Domain Data Request

• Parameter: header

• Parameter: consumerId

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: currentDomainVersion (not used in current Release)

##### 7.4.7.2 Domain Data Acknowledgement

• Parameter: header

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: DomainVersion (not used in current Release)

• Parameter: preLoadingStatus

##### 7.4.7.3 Domain Data Usage Restriction Acknowledgement

• Parameter: header

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: DomainVersion (not used in current Release)

• Parameter: usageRestrictionStatus

##### 7.4.7.4 Activation Acknowledgement

• Parameter: header

---

• Parameter: DomainId (not used in current Release and under discussion)

• Parameter: DomainVersion (not used in current Release)

• Parameter: activationAcknowledgement

#### 7.4.8 Implicit choices and justification

Not applicable

For a further release.

For a further release.

For a further release.

For a further release.

### 7.5 DESCRIPTION OF THE EXTERNAL INTERFACE I OP

### 7.6 DESCRIPTION OF THE EXTERNAL INTERFACE I AS

### 7.7 DESCRIPTION OF THE EXTERNAL INTERFACE I SEC

### 7.8 DESCRIPTION OF THE EXTERNAL INTERFACE I DIAGN AND MAINT

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>/BalnCon/</td><td style='text-align: center;'>Basic interoperability constituents in the Control-Command and Signalling Trackside SubsystemTable 5.2 in Legal framework of /CCSTSI/</td></tr><tr><td style='text-align: center;'>/SysDef/</td><td style='text-align: center;'>R2DATOD13.1 - Moving Block Specifications applying a train-centric approachPart 1 - System Definition</td></tr><tr><td style='text-align: center;'>/CCSTSI/</td><td style='text-align: center;'>Control Command and Signalling TSICommission Implementing Regulation (EU) 2023/1695 of 10 August 2023</td></tr><tr><td style='text-align: center;'>/ETCS/</td><td style='text-align: center;'>ETCS SpecificationsAnnex A for the /CCSTSI/Set of Specifications (ETCS B4 R1)</td></tr><tr><td style='text-align: center;'>/S2R/</td><td style='text-align: center;'>S2RMoving Block Specification Releasehttps://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5f58a710a&amp;appId=PPGMS</td></tr><tr><td style='text-align: center;'>/RCA/</td><td style='text-align: center;'>RACARCA Baseline 1 Release 0https://public.3.basecamp.com/p/KeehzqFmXv5R2N7tGDjaEokq</td></tr><tr><td style='text-align: center;'>/EULYNX/</td><td style='text-align: center;'>EuLynxBaseline Set 4 Release 2https://rail-research.europa.eu/system_pillar/system-pillar-outputs/trackside-assets-specifications/</td></tr><tr><td style='text-align: center;'>/SD1DM/</td><td style='text-align: center;'>SPT2-TransversalSystemsTCCS SD1 - Data Model</td></tr><tr><td style='text-align: center;'>/EuArch/</td><td style='text-align: center;'>Eu.Doc.16 - EULYNX System architecture specification</td></tr><tr><td style='text-align: center;'>/POS/</td><td style='text-align: center;'>Eu.Doc.100 - Specification of Point of Service</td></tr><tr><td style='text-align: center;'>/SCI/</td><td style='text-align: center;'>Eu.Doc.92 - Interface definition SCI</td></tr><tr><td style='text-align: center;'>/SCI-Gen/</td><td style='text-align: center;'>Eu.Doc.93 - Interface specification SCI Generic</td></tr><tr><td style='text-align: center;'>/SCI-P/</td><td style='text-align: center;'>Eu.Doc.38 - Interface specification SCI-P</td></tr><tr><td style='text-align: center;'>/SCI-TDS/</td><td style='text-align: center;'>Eu.Doc.44 - Interface specification SCI-TDS</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>/SCI-LX/</td><td style='text-align: center;'>Eu.Doc.112 - Interface specification SCI-LX</td></tr><tr><td style='text-align: center;'>/SCI-GenIF/</td><td style='text-align: center;'>Eu.Doc.119 - Generic interface and subsystem requirements for SCI</td></tr><tr><td style='text-align: center;'>/ReqSubsP/</td><td style='text-align: center;'>Eu.Doc.36 - Requirements specification for subsystem Point</td></tr><tr><td style='text-align: center;'>/OpCon/</td><td style='text-align: center;'>SP-CCS-TMS-CMS-Operational-vision.pdf (europa.eu) (?)</td></tr><tr><td style='text-align: center;'>/RCA.Doc.61/</td><td style='text-align: center;'>RCAAPS Concept Operating State and APS Domain Objects</td></tr><tr><td style='text-align: center;'>/RCA.Doc.62/</td><td style='text-align: center;'>RCAAPS Concept: Route setting and route protection</td></tr><tr><td style='text-align: center;'>/GSL/</td><td style='text-align: center;'>Geometric Safety Logic in a nutshellNote: this document already uses other abstract concepts than Drive Protection Section which are not yet agreed in the authors&#x27; working group. Please take them as indicative for understanding.</td></tr><tr><td style='text-align: center;'>/FlankProtection/</td><td style='text-align: center;'>ADI.023 Concept: Flank Protection (Allocation Section, Risk Path)</td></tr><tr><td style='text-align: center;'>/SempR2/</td><td style='text-align: center;'>SEMP Annex R2 - Requirements patterns syntax</td></tr><tr><td style='text-align: center;'>/SempR3/</td><td style='text-align: center;'>SEMP Annex R3 - Rules for writing textual requirements</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Chapter</td><td style='text-align: center;'>Reviewer</td><td style='text-align: center;'>Comment</td><td style='text-align: center;'>Answer</td><td style='text-align: center;'>Meeting 21.11.2023</td></tr><tr><td style='text-align: center;'>REQ-0010</td><td style='text-align: center;'>Ivan</td><td style='text-align: center;'>Only when it is discarded? Shouldn&#x27;t all the messages be logged to the Diagnostic system?</td><td style='text-align: center;'>TBD. I agree. Perhaps it would be better to consider an alarm (instead of event) in this case. This is in line with the comment of Bettina here after. This should be clarified within a general chapter &quot;log and alarm&quot; for a further release.</td><td style='text-align: center;'>This should be clarified within a general chapter &quot;log and alarm&quot; for a further release. COMMENT TO BE KEPT</td></tr><tr><td style='text-align: center;'>8.7 SYSFESTABLISH COMMUNICATION SESSION WITH TACS</td><td style='text-align: center;'>Daniel</td><td style='text-align: center;'>from the requirements below, there are additional outputs: + order to establish a communication session + LOG of not established communication</td><td style='text-align: center;'>TBD.</td><td style='text-align: center;'>comment to be kept for further release, COMMENT TO BE KEPT</td></tr><tr><td style='text-align: center;'>REQ-0016</td><td style='text-align: center;'>Ivan</td><td style='text-align: center;'>Should the establishment logged also in the Diagnosis interface? For analysing possible incidences, it can be interesting to know the time when the connection was established.</td><td style='text-align: center;'></td><td style='text-align: center;'>TBD. I agree, this should be clarified within a general chapter &quot;log and alarm&quot; for a further release. See previous comments. COMMENT TO BE KEPT</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>Kostas</td><td style='text-align: center;'>I would expect all operations to logged in for juridical reasons, Diagnostics would only log the abnormalities?</td><td style='text-align: center;'>TBD. I agree, this should be clarified within a general chapter &quot;log and alarm&quot; for a further release. See previous comments.</td><td style='text-align: center;'>TBD. I agree, this should be clarified within a general chapter &quot;log and alarm&quot; for a further release. See previous comments. COMMENT TO BE KEPT</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>8.9 SYS F LOAD AND CHECK DOMAIN DATA</td><td style='text-align: center;'>Kostas</td><td style='text-align: center;'>[Minor] How about using the last validated data (if applicable) and triggering a rollback?</td><td style='text-align: center;'>TBD. Not applicable to release 1 but for release 2?</td><td style='text-align: center;'>COMMENT TO BE KEPT FOR FURTHER RELEASE</td></tr></table>

---

## SysC: System Capability Template

<div style="text-align: center;">ANNEX 2: TEMPLATES</div>


<div style="text-align: center;">Table 16 - Description of SysC: <Template></div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>&lt;description&gt;</td></tr><tr><td style='text-align: center;'>Goal</td><td style='text-align: center;'>&lt;description&gt;</td></tr><tr><td style='text-align: center;'>Precondition(s)</td><td style='text-align: center;'>- &lt;precondition&gt;</td></tr><tr><td style='text-align: center;'>Postcondition(s)(Success)</td><td style='text-align: center;'>- &lt;postcondition&gt;</td></tr><tr><td style='text-align: center;'>Postcondition(s)(Failure)</td><td style='text-align: center;'>- &lt;postcondition&gt;</td></tr><tr><td style='text-align: center;'>Involved actor(s)</td><td style='text-align: center;'>- &lt;actor&gt;</td></tr><tr><td style='text-align: center;'>Trigger(s)</td><td style='text-align: center;'>- &lt;trigger&gt;</td></tr><tr><td style='text-align: center;'>Main Sequence</td><td style='text-align: center;'>&lt;(link to related scenario)&gt;</td></tr><tr><td style='text-align: center;'>Alternate Sequence</td><td style='text-align: center;'>&lt;(link to related scenario)&gt;</td></tr><tr><td style='text-align: center;'>Failure Sequence</td><td style='text-align: center;'>&lt;(link to related scenario)&gt;</td></tr><tr><td style='text-align: center;'>Comments</td><td style='text-align: center;'>&lt;additional&gt;</td></tr></table>

## Scenario: Template Scenario

The scenario “Template Scenario” is shown. It contains a description of the elements to be used in the scenarios and some examples.

---

This Visio file template is available inside Project Place, directory "System Specification"

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0bc60c1d-7317-4ca5-8114-55273658b51e/markdown_0/imgs/img_in_image_box_290_205_909_1035.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A44%3A27Z%2F-1%2F%2F7440e0eae598cd606b93610319bfacf0465b0c2599022edf27278a2b2866acc1" alt="Image" width="51%" /></div>


<div style="text-align: center;">Figure 45 - Scenario: Template Scenario</div>

---

# Rail to Digital automated up to autonomous train operation

# D13.1 – Moving Block Specifications applying a train-centric approach, Part 3 – Safety Analysis

Due date of deliverable: 01/09/2024

Actual submission date: 07/07/2025

## Leader/Responsible of this Deliverable: Manuel Schleiffelder ÖBB-INFRA

Reviewed: Y


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Document status</td></tr><tr><td style='text-align: center;'>Revision</td><td style='text-align: center;'>Date</td><td style='text-align: center;'>Description</td></tr><tr><td style='text-align: center;'>01</td><td style='text-align: center;'>08/01/2024</td><td style='text-align: center;'>Draft for internal review</td></tr><tr><td style='text-align: center;'>02</td><td style='text-align: center;'>29/05/2024</td><td style='text-align: center;'>Draft for internal review</td></tr><tr><td style='text-align: center;'>03</td><td style='text-align: center;'>22/07/2024</td><td style='text-align: center;'>Internal review comment implemented</td></tr><tr><td style='text-align: center;'>04</td><td style='text-align: center;'>03/12/2024</td><td style='text-align: center;'>Update to new document template</td></tr><tr><td style='text-align: center;'>05</td><td style='text-align: center;'>07/07/2025</td><td style='text-align: center;'>JU comments solved</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Project funded from the European Union&#x27;s Horizon Europe research and innovation programme</td></tr><tr><td colspan="3">Dissemination Level</td></tr><tr><td style='text-align: center;'>PU</td><td style='text-align: center;'>Public</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>SEN</td><td style='text-align: center;'>Sensitive - limited under the conditions of the Grant Agreement</td><td style='text-align: center;'></td></tr></table>

Duration: 21 months

---

(Empty result)

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5458c473-12fb-403d-aaad-0e9c3c65c0d2/markdown_0/imgs/img_in_image_box_89_208_267_330.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A44%3A37Z%2F-1%2F%2F88cad94863376979e109f72ec1a9ccdeae93fac913e8da59b3aabe1baf0de612" alt="Image" width="14%" /></div>


## ACKNOWLEDGEMENTS

This project has received funding from the Europe’s Rail Joint Undertaking (ERJU) under the Grant Agreement no. 101102001. The JU receives support from the European Union’s Horizon Europe research and innovation programme and the Europe’s Rail JU members other than the Union.

<div style="text-align: center;">REPORT CONTRIBUTORS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Company</td><td style='text-align: center;'>Details of Contribution</td></tr><tr><td style='text-align: center;'>Lars Behrendt</td><td style='text-align: center;'>ÖBB-PV</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Jürgen Flötzer</td><td style='text-align: center;'>FRQ/ÖBB-Affiliate</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Jens J. Franke</td><td style='text-align: center;'>DB Infra GO</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Andreas Gerstinger</td><td style='text-align: center;'>FRQ/ÖBB-Affiliate</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Felix Schaber</td><td style='text-align: center;'>Thales/GTS_AT</td><td style='text-align: center;'>Author</td></tr><tr><td style='text-align: center;'>Manuel Schleiffelder</td><td style='text-align: center;'>ÖBB-INFRA</td><td style='text-align: center;'>Author / Task Lead</td></tr><tr><td style='text-align: center;'>Balaz Toth</td><td style='text-align: center;'>ÖBB-PV</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Harish Narayanan</td><td style='text-align: center;'>Nextrail</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>F. Javier González</td><td style='text-align: center;'>Renfe</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Daniel Kolár</td><td style='text-align: center;'>AŽD</td><td style='text-align: center;'>Reviewer</td></tr><tr><td style='text-align: center;'>Iván Velado</td><td style='text-align: center;'>CAF</td><td style='text-align: center;'>Reviewer</td></tr></table>

## Disclaimer

The information in this document is provided “as is”, and no guarantee or warranty is given that the information is fit for any particular purpose. The content of this document reflects only the author's view – the Joint Undertaking is not responsible for any use that may be made of the information it contains. The users use the information at their sole risk and liability.

---

## ABBREVIATIONS AND ACRONYMS


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>AoC</td><td style='text-align: center;'>Area of Control</td></tr><tr><td style='text-align: center;'>APS</td><td style='text-align: center;'>Advanced Protection System</td></tr><tr><td style='text-align: center;'>AS</td><td style='text-align: center;'>Adjacent System (neighbouring systems)</td></tr><tr><td style='text-align: center;'>ASM</td><td style='text-align: center;'>Assumption</td></tr><tr><td style='text-align: center;'>CBO</td><td style='text-align: center;'>Common Business Objectives</td></tr><tr><td style='text-align: center;'>CCS</td><td style='text-align: center;'>Command, Control, and Signalling</td></tr><tr><td style='text-align: center;'>CELEX</td><td style='text-align: center;'>Communitatis Europaea Lex</td></tr><tr><td style='text-align: center;'>CES</td><td style='text-align: center;'>Conditional Emergency Stop</td></tr><tr><td style='text-align: center;'>CMD</td><td style='text-align: center;'>Cold Movement Detection</td></tr><tr><td style='text-align: center;'>CS</td><td style='text-align: center;'>Control and Supervision</td></tr><tr><td style='text-align: center;'>CSM-RA</td><td style='text-align: center;'>Common Safety Method for Risk Evaluation and Assessment</td></tr><tr><td style='text-align: center;'>DMI</td><td style='text-align: center;'>Driver Machine Interface</td></tr><tr><td style='text-align: center;'>DPS</td><td style='text-align: center;'>Drive Protection Section</td></tr><tr><td style='text-align: center;'>DR</td><td style='text-align: center;'>Digital Register</td></tr><tr><td style='text-align: center;'>EB</td><td style='text-align: center;'>Emergency brake</td></tr><tr><td style='text-align: center;'>EoM</td><td style='text-align: center;'>End of Mission</td></tr><tr><td style='text-align: center;'>ERA</td><td style='text-align: center;'>European Railway Agency</td></tr><tr><td style='text-align: center;'>ERJU</td><td style='text-align: center;'>Europe&#x27;s Rail Joint Undertaking</td></tr><tr><td style='text-align: center;'>ERTMS</td><td style='text-align: center;'>European Rail Traffic Management System</td></tr><tr><td style='text-align: center;'>ETCS</td><td style='text-align: center;'>European Train Control System</td></tr><tr><td style='text-align: center;'>EULYNX</td><td style='text-align: center;'>European initiative by 14 Infrastructure Managers to standardise interfaces and elements of the signalling systems</td></tr><tr><td style='text-align: center;'>FA</td><td style='text-align: center;'>Flagship Area (1 or 2) of ERJU IP</td></tr><tr><td style='text-align: center;'>FRMCS</td><td style='text-align: center;'>Future Railway Mobile Communication System</td></tr><tr><td style='text-align: center;'>FS</td><td style='text-align: center;'>Full Supervision</td></tr><tr><td style='text-align: center;'>GSMR</td><td style='text-align: center;'>Global System for Mobile Communications – Railway</td></tr><tr><td style='text-align: center;'>HCS</td><td style='text-align: center;'>Hierarchical Control Structure</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Unique Identifier</td></tr><tr><td style='text-align: center;'>IM</td><td style='text-align: center;'>Infrastructure Manager</td></tr><tr><td style='text-align: center;'>IP</td><td style='text-align: center;'>Innovation Pillar</td></tr><tr><td style='text-align: center;'>IVV</td><td style='text-align: center;'>Integration, Verification and Validation</td></tr></table>

---

## FP2R2DATO


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>IXL</td><td style='text-align: center;'>Interlocking</td></tr><tr><td style='text-align: center;'>JU</td><td style='text-align: center;'>Joint Undertaking</td></tr><tr><td style='text-align: center;'>L2</td><td style='text-align: center;'>Level 2 (ETCS level definition)</td></tr><tr><td style='text-align: center;'>L3</td><td style='text-align: center;'>Level 3 (ETCS level definition), obsolete with enactment of TSI 2023</td></tr><tr><td style='text-align: center;'>LX</td><td style='text-align: center;'>Level Crossing</td></tr><tr><td style='text-align: center;'>MA</td><td style='text-align: center;'>Movement Authority</td></tr><tr><td style='text-align: center;'>MBD</td><td style='text-align: center;'>Moving Block Demonstrator</td></tr><tr><td style='text-align: center;'>MBS</td><td style='text-align: center;'>Moving Block System</td></tr><tr><td style='text-align: center;'>OBU</td><td style='text-align: center;'>On-Board Unit</td></tr><tr><td style='text-align: center;'>OC</td><td style='text-align: center;'>Object Controller</td></tr><tr><td style='text-align: center;'>OM</td><td style='text-align: center;'>Operations Manager</td></tr><tr><td style='text-align: center;'>OS</td><td style='text-align: center;'>On Sight</td></tr><tr><td style='text-align: center;'>PDI</td><td style='text-align: center;'>Process Data Interface protocol</td></tr><tr><td style='text-align: center;'>PE</td><td style='text-align: center;'>Plan Execution</td></tr><tr><td style='text-align: center;'>Picop</td><td style='text-align: center;'>Person in charge of possession</td></tr><tr><td style='text-align: center;'>PKI</td><td style='text-align: center;'>Public Key Infrastructure</td></tr><tr><td style='text-align: center;'>PRAMSS</td><td style='text-align: center;'>Performance Reliability Availability Maintainability Safety and Security</td></tr><tr><td style='text-align: center;'>R2DATO</td><td style='text-align: center;'>Rail to Digital automated up to autonomous train operation</td></tr><tr><td style='text-align: center;'>RAMS</td><td style='text-align: center;'>Reliability, Availability, Maintainability and Safety</td></tr><tr><td style='text-align: center;'>RBC</td><td style='text-align: center;'>Radio Block Centre</td></tr><tr><td style='text-align: center;'>RCA</td><td style='text-align: center;'>Reference CCS Architecture</td></tr><tr><td style='text-align: center;'>Ref</td><td style='text-align: center;'>Reference</td></tr><tr><td style='text-align: center;'>RU</td><td style='text-align: center;'>Railway Undertaking</td></tr><tr><td style='text-align: center;'>SB</td><td style='text-align: center;'>Stand By</td></tr><tr><td style='text-align: center;'>SCI</td><td style='text-align: center;'>Standard Command Interface</td></tr><tr><td style='text-align: center;'>SCP</td><td style='text-align: center;'>Safe Communication Protocol</td></tr><tr><td style='text-align: center;'>SDI</td><td style='text-align: center;'>Standard Diagnostics Interface</td></tr><tr><td style='text-align: center;'>SDR</td><td style='text-align: center;'>Safety Design Recommendation</td></tr><tr><td style='text-align: center;'>SFE</td><td style='text-align: center;'>Safe Front End</td></tr><tr><td style='text-align: center;'>SH</td><td style='text-align: center;'>Shunting</td></tr><tr><td style='text-align: center;'>SIL</td><td style='text-align: center;'>Safety Integrity Level</td></tr><tr><td style='text-align: center;'>SL</td><td style='text-align: center;'>Sleeping</td></tr><tr><td style='text-align: center;'>SLC</td><td style='text-align: center;'>System Level Constraints</td></tr></table>

---

## FP2R2DATO


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>SMI</td><td style='text-align: center;'>Standard Maintenance Interface</td></tr><tr><td style='text-align: center;'>SOC</td><td style='text-align: center;'>Security Operations Centre</td></tr><tr><td style='text-align: center;'>SoM</td><td style='text-align: center;'>Start of Mission</td></tr><tr><td style='text-align: center;'>SP</td><td style='text-align: center;'>System Pillar</td></tr><tr><td style='text-align: center;'>SPAD</td><td style='text-align: center;'>Signal Passed At Danger</td></tr><tr><td style='text-align: center;'>SR</td><td style='text-align: center;'>Staff Responsible</td></tr><tr><td style='text-align: center;'>SRE</td><td style='text-align: center;'>Safe Rear End</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>System-Theoretic Accident Model and Processes</td></tr><tr><td style='text-align: center;'>STPA</td><td style='text-align: center;'>System-Theoretic Process Analysis</td></tr><tr><td style='text-align: center;'>SuC</td><td style='text-align: center;'>System under Consideration</td></tr><tr><td style='text-align: center;'>SysC</td><td style='text-align: center;'>System Capability</td></tr><tr><td style='text-align: center;'>SysF</td><td style='text-align: center;'>System Function</td></tr><tr><td style='text-align: center;'>TA</td><td style='text-align: center;'>Trackside Assets</td></tr><tr><td style='text-align: center;'>TACS</td><td style='text-align: center;'>Trackside Asset Control and Supervision</td></tr><tr><td style='text-align: center;'>TAF</td><td style='text-align: center;'>Track Ahead Free</td></tr><tr><td style='text-align: center;'>TBD</td><td style='text-align: center;'>To Be Defined</td></tr><tr><td style='text-align: center;'>TDS</td><td style='text-align: center;'>Train Detection System</td></tr><tr><td style='text-align: center;'>TIM</td><td style='text-align: center;'>Train Integrity Monitoring</td></tr><tr><td style='text-align: center;'>TIMS</td><td style='text-align: center;'>Train Integrity Monitoring System</td></tr><tr><td style='text-align: center;'>TMS</td><td style='text-align: center;'>Traffic Management System</td></tr><tr><td style='text-align: center;'>TRL</td><td style='text-align: center;'>Technology Readiness Level</td></tr><tr><td style='text-align: center;'>TTD</td><td style='text-align: center;'>Trackside Train Detection</td></tr><tr><td style='text-align: center;'>TU</td><td style='text-align: center;'>Train Unit</td></tr><tr><td style='text-align: center;'>UA</td><td style='text-align: center;'>Unsupervised Area</td></tr><tr><td style='text-align: center;'>UCA</td><td style='text-align: center;'>Unsafe Control Action</td></tr><tr><td style='text-align: center;'>UES</td><td style='text-align: center;'>Unconditional Emergency Stop</td></tr><tr><td style='text-align: center;'>URA</td><td style='text-align: center;'>Usage Restriction Area</td></tr><tr><td style='text-align: center;'>WP</td><td style='text-align: center;'>Work Package</td></tr><tr><td style='text-align: center;'>WSP</td><td style='text-align: center;'>Wheel Slip Protection</td></tr></table>

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

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fc222c39-4327-4fa2-bf7d-0f380adfb62e/markdown_0/imgs/img_in_image_box_93_851_1085_1476.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A45%3A24Z%2F-1%2F%2F013e63b10b4f993e7d335b7389ef5550d7d8236db7a263b1fac95e7004aa90ad" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 1: Localization of MBS within a simplified view of “moving block” trackside CS</div>

---

The approach is “train-centric” in the sense that the physical train itself is considered as the main business object instead of indirectly deriving information about the train only by monitoring track occupations. Since we apply “moving block principles”, movement authorities can therefore be issued up to any point on the track, and trains can safely follow each other in absolute braking distance without being bound to wait for the next block section to become free. However, the system shall still be able to utilize information from previously installed Train Detection Systems (TDS) to complement and improve localization information where applicable (e.g. if receiving a OBU radio transmission takes longer than receiving occupation information from the TDS), and/or for migration purposes. Some advantages of the new system are:

• potential performance gains due to smaller train headway times.

• reduced efforts for TDS and obsolete lineside signals (cab side signaling).

- the merger of interlocking and RBC functionality, that enables the MBS system to even consider physical trains (since traditional IXL was only concerned about securing routes).

- the concentration of safety related functions into as few “safety-critical” components as possible (thereby reducing the SIL requirement for other components).

- the (envisaged) capability of runtime configuration updates.

- (envisaged) improved supplier independence due to open/fully defined interfaces.

MBS is thus by design “the component performing safety related functions” within this novel trackside CS. The implications of this approach on overall system safety are of great interest.

Previous investigations were focused on train localization (performance), radio communication (performance and availability), cold movement detection, as well as train length- and train integrity data. Ideally, the safety requirements from there can be mapped to the new results. However, a focus of this analysis are the control (inter-)actions and feedback between the adjacent systems (e.g., what are the main hazards that emerge from command and feedback loop between MBS and a safety operator panel).

---

## 2 SCOPE

The analysis for the Task 13.3 details the results of the safety analysis with focus on the MBS and its interfaces to the other internal and external systems, as depicted in Figure 2 - MBS System Boundary. It is based on the STPA analysis method for the current safety analysis and considers the result from the former X2Rail project. The STPA analysis proved to be the most suitable method at a time, when the system requirements and the system design were still subject to significant changes. Like in traditional safety methods, the efforts involved are highly dependent on the level of depth to which the STPA shall be conducted, and since the task resources are limited (due to overall WP allocation as well as due to the number of active authors) an adaptive approach is applied. While the whole system-stack involved in "command control & signaling" shall be covered at a high abstraction level, certain points of interest (e.g., where valuable information for feedback to the specification task can be generated) can be investigated on a lower abstraction level, down to individual control/feedback telegrams.

The analysis does not provide all the evidence to obtain certification or to fulfil the mandatory requirements or design standards (e.g.: EN50126-1 and -2, EN50128, EN50129, EN50159, ...). However, it will define safety related design recommendations which shall be considered during the development of the MBS and may be mapped to safety requirements in a later stage.

The overall analysis of the whole Moving Block Demonstrator (MBD) as depicted in Figure 1 below is covered in WP44/45 (Task 45.5.).

### 2.1 SYSTEM BOUNDARY

As briefly described in the introduction, the system boundary of MBS is defined through interfaces within the Moving Block Demonstrator (MBD) (e.g., I_PE, I_DR) and also to the outside of the MBD (e.g., I_TACS, I_TACS). Even though similar definitions have already been produced within Task 13.1, 13.2 and 44.3 we decided to reproduce (copy/update/rewrite) such a section here – at least until the documents from these tasks are in a stable version. Within this section there is also a description of all the subsystems depicted in the drawing below. Relevant Interface descriptions can be found in chapter 6 Interface Criticality together with a preliminary analysis of the interface criticality. The handover to neighboring systems is out of scope for this analysis.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9ff71789-5590-4ca6-a930-cf50ddc43092/markdown_0/imgs/img_in_image_box_107_180_1106_898.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A45%3A31Z%2F-1%2F%2Fc4dc8818b59d459ac07dfb2b186bb8141ec9e74d1595bd95244afa657a40b263" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 2 - MBS System Boundary</div>


### 2.2 CONNECTED SYSTEMS

This chapter provides an actual description of the systems the MBS interacts- or has dependencies with, as shown in the system boundary figure above. The description itself is based on the system definition in WP44 Task 44.3.

#### 2.2.1 Neighbouring (MBS/RBC) System


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Neighbouring (MBS/RBC) System [Adjacent System in 13.1/13.2]</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>A neighbouring System can be either another MBS, a different radio-based ETCS related neighbouring system (e.g., RBC) or e.g., an RBC/IXL combination with traditional route logic. The interface to a radio-based ETCS related neighbouring system allows trains to pass the border to/from a neighbouring Level 2 area without changing the driver responsibility and the cab-signalling.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>The interface to a neighbouring system not related to radio-based ETCS allows trains to pass the border to/from an area not equipped with Level 2. The cab-signalling is replaced by optical signals and vice versa.</td></tr></table>

<div style="text-align: center;">Table 1 – Neighbouring System Definition</div>


#### 2.2.2 Diagnostics System


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Management &amp; Diagnostics System</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Diagnostics system monitors the state of the MBS and logs parameters of interest. For this purpose, MBS transmits log, status, and diagnostic data to the Diagnostic system for status evaluation and analysis.</td></tr></table>

<div style="text-align: center;">Table 2 – Diagnostics System Definition</div>


<div style="text-align: center;">2.2.3 Digital Register</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Digital Register</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Digital Register (DR) provides reliable (meaning complete, accurate, current, consistent, verified and validated), interoperable and accessible infrastructure information as a critical enabler for safety-related and non-safety-related functions. The Digital Register includes static infrastructure information (static speed profile, gradients, cant, etc.) and configuration data, which are approved after the engineering process. The interface between the DR and the MBS is used to update the data in the MBS.</td></tr></table>

<div style="text-align: center;">Table 3 – Digital Register Definition</div>


#### 2.2.4 ETCS on-board


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>ETCS on-board</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The ERTMS/ETCS on-board (OBU) equipment is a computer-based system that supervises the movement of the train to which it belongs, on basis of information exchanged with the MBS. Its system requirement specification is defined in UNISIG subset 26 [2]</td></tr></table>

<div style="text-align: center;">Table 4 – ETCS on-board Definition</div>

---

#### 2.2.5 Operator Panel


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Operator Panel</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Operator Panel is a system that provides the human-machine interface with the Operations Manager in order to provide status information on the operation of the railway system and accept input for the resolution of degraded situations.</td></tr></table>

<div style="text-align: center;">Table 5 – Operator Panel Definition</div>


#### 2.2.6 Plan Execution


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Plan Execution</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The PE operationalizes the “operational plan” or “timetable” as received from TMS via the I_OP interface. The functional split between PE and MBS is along a virtual SIL-boundary (allowing PE to be classified as SIL-basic integrity only). PE actually conceives the Movement Permissions and the individual commands for trackside assets, while MBS is a “gatekeeper” that validates (safety logic) and forwards commands and Movement Authorities to trackside assets and trains. The MBS only acts upon dedicated emergency patterns and provides the Operational State to the PE.</td></tr></table>

<div style="text-align: center;">Table 6 – Plan Execution Definition</div>


#### 2.2.7 Security Service


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Security Service</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Security Service summarises all technological systems that are necessary to manage and provide the cryptographic artefacts (e.g., keys or certificates) to ensure the confidentiality, authenticity and integrity (Information Security Triad) of the communication between subsystems.</td></tr></table>

<div style="text-align: center;">Table 7 – Security Service Definition</div>


#### 2.2.8 Trackside Asset Control and Supervision


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Trackside Asset Control and Supervision</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>The Trackside Asset Control and Supervision (TACS) reports the state of the Trackside Assets (TAs). The MBS mainly uses this interface to trigger setting the state of a TA, e.g., moving a point, and to receive status information from TAs (e.g., occupancy information from TDS)</td></tr></table>

<div style="text-align: center;">Table 8 – Trackside Asset Control and Supervision Definition</div>


<div style="text-align: center;">2.2.9 IM Data System</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Infrastructure manager (IM) Data System</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>Infrastructure Manager Data System describes the body or firm responsible for the management of all relevant infrastructure data, traffic management, and control-command and signalling in alignment with key term definition in Directive 2012/34/EU.</td></tr></table>

<div style="text-align: center;">Table 9 – IM Data System Definition</div>


<div style="text-align: center;">2.2.10 Traffic Management System</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Attribute</td><td style='text-align: center;'>Content</td></tr><tr><td style='text-align: center;'>Name</td><td style='text-align: center;'>Traffic Management System (TMS)</td></tr><tr><td style='text-align: center;'>Description</td><td style='text-align: center;'>Traffic Management System provides functionality for preparing and optimising the entire schedule within an Area of Control. This schedule will be represented by operational plans for each individual Train Unit. This operational plan is provided to the PE where it is operationalized into specific commands and movement permissions. PE provides the current operation state to TMS as feedback.</td></tr></table>

<div style="text-align: center;">Table 10 – Traffic Management System Definition</div>

---

3 INPUTS

The documents, project outputs, open standards as well as documents from tasks within R2DATO that are relevant to the work here are listed and briefly described in this chapter.

### 3.1 SYSTEM PILLAR INPUTS

System Pillar provided an envelope for the ERJU activities within the “common business objectives” and the “operational visions” documents. Relevant passages have been cited below and shall be e.g., used as a benchmark for concluding remarks (in a later stage of the document).

##### 3.1.1 CBO ([6], p.18) - Optimize safety strategies and standards

- Safety critical elements of a system should be optimized and simplified through design by moving away from bespoke solutions. The development of these parameters facilitates a common approach to safety and security. (simplified standard safety components)

- Simulation and modelling tools are needed to accurately calculate and validate the performance of systems with an incorporated robust PRAMSS framework controlling for the development process and the RAMSS change impact analysis for changes inside of the life cycle. (validated system performance) (robust PRAMSS framework)

- The safety logic shall have a generic approval and authorization in which it is proven that it just needs a reliable input of topology information and train information and will assure safety on this basis. {safety logic with generic safety approval}

- The exchange of components or connection of new subsystems under production shall happen without a new safety case or preparation processes. {seamless and selective exchange of components under production}

- An authorized vehicle can be operated everywhere on compliant infrastructure without local integration test. {vehicle is interoperable without local integration test}

##### 3.1.2 Operational Vision ( $ [7] $ , p.20) - Enhanced safety assurance process

- Because of a high architecture quality, safe integration of components to a whole safe application is just done by a centralized (online) compliance test (certificate), that is done once (strategy “modular safety”).

- The quality of validation/testing and practical risk assessment for components and “system of systems” reaches a quality level, that allows to simplify bureaucratic development processes of today.

- Independent/redundant/stable safety monitoring systems and actor advisory systems allow a more dynamic change of systems and diversity of configurations and support a continuous improvement process.

#### 3.1.3 Operational Scenarios

Missing. Implicitly defined operational scenarios within the use- and test-cases from Task 44.2. will be analyzed instead until other information is available.

---

### 3.2 X2RAIL DOCUMENTATION

• Safety Analysis from X2RAIL-1 [9]

• Safety Analysis from X2RAIL-3 [10]

• Safety Analysis Update from X2RAIL-5 [11]

The safety requirements from the shift2rail projects (currently to be found in the mapping tables / xlsx / within the project folder) shall be discussed in chapter 7 in a later stage of the document.

### 3.3 RCA Documents

The Reference CCS Architecture (RCA, version 1.0, [12]) is a relevant input in the specification work packages as well as to system pillar activities and shall – at least implicitly – be considered.

### 3.4 R2DATO Documents

The following documents from other tasks within R2DATO WP13/14 and WP44/45 are to be considered for this analysis:

• Task 13.1 provides a high-level definition for the Moving Block System (MBS) [13]

• Task 13.2. provides the (current) specification of the Moving Block System (MBS). [14]

• Task 44.2 Use cases document. [17]

- Task 44.3. provides a high-level definition, as well as the (current) specification of the Moving Block Demonstrator (MBD). [15, 16]

---

## 4 SAFETY ANALYSIS METHODEOLOGY

This chapter describes the used safety analysis methodologies on a very high abstraction level. Even though some aspects of the larger demonstrator (MBD) architecture have to be taken into account, the target of this safety analysis is the Moving Block System (MBS). The analysis is partly based on outputs from predecessor projects, such as X2Rail and RCA, but it also relies on inputs from system pillar, as well as the results from connected tasks within R2DATO.

The envisaged goal for the demonstrator (MBD) is TRL (Technology Readiness Level) 6 [20]. At this stage, the complete safety analysis is qualitative only, not quantitative. Quantitative methods, such as fault trees to verify specific safety objectives, may be added in a later stage when a higher TRL shall be achieved.

Figure 3 shows the scope of the safety analysis in the so called “hourglass model” from CENELEC EN 50126-2.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//13d37d13-2fd0-4c51-a84d-69b88a14820a/markdown_0/imgs/img_in_image_box_275_627_929_1424.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A46%3A11Z%2F-1%2F%2Fae198006efe0a4deaa49c28903b70f2583bb8e6c397ae13d10ad5fb67098a1bf" alt="Image" width="54%" /></div>


<div style="text-align: center;">Figure 3 – Safety Analysis in Relation to the Hourglass Model</div>

---

### 4.1 COMMON SAFETY METHODS

For safety-relevant changes to railroad systems (e.g., technical, operational, regulatory or organizational changes), the risk assessment process in accordance with EU regulations 2015/1136 and 402/2013 (CSM-RA) must be applied.

However, technical changes to a system that are handled with the RAMS management process of the CENELEC standard EN 50126 (+128/129) are generally compliant with the CSM procedure.

### 4.2 CENELEC STANDARDS

Tasks 13.1 and 13.2 within work package 13 are developed along the relevant CENELEC standards. Thus, the following standards apply:

• EN 50126-1:2017: Generic RAMS Process

• EN 50126-2:2017: Systems Approach to Safety

EN 50716:2023: Requirements for software development (supersedes EN 50128:2011: Software)

• EN 50129:2018: Electronic systems

They shall be applied as far as practicable for a TRL 6 system. This means that the standards will be taken as a major input for the development, but some requirements may be interpreted in a more relaxed way as it would be the case for a fully operational system.

### 4.3 STPA

The STPA handbook  $ [1] $  describes the practical application of STPA in great detail. Here, we only provide a very short description and the reason why STPA was chosen.

STPA (System-Theoretic Process Analysis) is a method to identify hazards and related system constraints in complex systems, in order to identify (unsafe) control actions that lead to those hazards (and related losses). Mitigations to avoid these unsafe control actions can then be derived.

The reason why STPA was chosen is that it is geared towards large and complex systems with multiple interactions, where hazards do not necessarily only arise due to component failures, but also due to emergent behavior involving multiple components. The MBS (especially in combination with its interfaces and interactions with the environment) is a novel system, for which this method is believed to be of great value.

## 5 RISK ANALYSIS

This chapter details and documents the results of the conducted STPA analysis as described in chapter 4.3. The analysis focuses on the marked section of the "hourglass model" from CENELEC EN 50126-2 as shown in Figure 3 which is intended to derive the safety requirements from operator point of view. These requirements must be considered by the suppliers of an MBS system. The supplier's safety analysis shall consider these requirements as their safety goals, that can be broken down into further sub-safety goals and requirements.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d718b44-380a-403e-8f7b-fe90bd7661d0/markdown_0/imgs/img_in_image_box_274_199_940_753.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A46%3A19Z%2F-1%2F%2F86a94d823f658f9c65b49426bb0a3ac3579fbc17496d419c70da9be1922d1820" alt="Image" width="55%" /></div>


<div style="text-align: center;">Figure 4: Traceability from STPA outputs from  $ [1] $ </div>


### 5.1 Losses

The first step of the STPA is to define which losses to consider for the analysis. The purpose of the analysis is to find possible causes for accidents. An accident is defined as an undesired or unplanned event that results in a loss. A loss always involves something of value to the stakeholder. Typical examples are loss of human life or injury, but also property damage, environmental pollution or loss of mission.  $ [1] $  For this analysis, three main losses are considered:

Legend of the following table:

ID ... a unique identifier

Name ___ a description of the loss


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td></tr><tr><td style='text-align: center;'>L-1</td><td style='text-align: center;'>Loss of life or injury to people on the train (including injury because of incorrect braking technique without derailment or collision)• Passengers• Railway staff (crew on the train)</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td></tr><tr><td style='text-align: center;'>L-2</td><td style='text-align: center;'>Loss of life or injury to people outside the train• Level crossing users (by any means of transportation or by foot)• People on the platform or neighbourhood of tracks• Railway workers• Trespassers (persons present on railway premises where such presence is forbidden)</td></tr><tr><td style='text-align: center;'>L-3</td><td style='text-align: center;'>Environmental loss (i.e. transport of dangerous goods)</td></tr></table>

<div style="text-align: center;">Table 11 – Losses</div>


Explicitly excluded from this analysis are loss of mission and loss of customer satisfaction, as our focus for this analysis is strictly on safety (e.g., a person's life).

### 5.2 HAZARDS

The next step of the analysis is to find the system level hazards. Within STPA, a hazard is defined as "a system state or set of conditions that, together with a particular set of worst-case environmental conditions, will lead to a loss" $ ^{[1]} $ . Note that this definition differs from the classical definition of a hazard. It is essential that hazards are defined at system level instead of component level, as hazards may also arise from the interaction between components and cannot necessarily be assigned to a single component.

A system is defined as “a set of components that act together as a whole to achieve some common goal, objective, or end”  $ [1] $ . It may contain subsystems and the analysis may be based higher or lower level of abstraction of individual subsystems as needed.

In order to identify system level hazards, it is therefore necessary to identify the system under consideration and the analysis boundary as defined in chapter 2.1 System Boundary. A useful way to define the analysis boundary may be to include only systems within the analysis boundary over which the system designers have some form of control.

To ease readability the hazards are described in a generic form. Each hazard may have multiple sub-hazards, further detailing the high-level hazard.

The hazards differentiate between losses in connection with other trains and hazards in connection with “other obstacles”. For the purposes of this analysis, runaway trains are regarded as “other obstacles”.

Legend of the following table:

ID ___ a unique identifier

Name ... a description of the unsafe condition

ID Losses ... associated losses


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-1]</td><td style='text-align: center;'>Train does not maintain safe distance to other trains (front, back, flank)</td><td style='text-align: center;'>[L-1]</td></tr><tr><td style='text-align: center;'>[H-1.1]</td><td style='text-align: center;'>Train deceleration is insufficient</td><td style='text-align: center;'>-</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-1.2]</td><td style='text-align: center;'>Train deceleration is too late</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-1.3]</td><td style='text-align: center;'>Train passes over point which has lost its end position (“Endlage”)</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-1.4]</td><td style='text-align: center;'>Train passes over point which indicates a wrong position</td><td style='text-align: center;'>-</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-2]</td><td style='text-align: center;'>Train does not maintain safe distance to other obstacles (obstacles include railway workers, vehicles on level crossings, end of line)</td><td style='text-align: center;'>[L-1, L-2]</td></tr><tr><td style='text-align: center;'>[H-2.1]</td><td style='text-align: center;'>Train deceleration is insufficient</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.2]</td><td style='text-align: center;'>Train deceleration is too late</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.3]</td><td style='text-align: center;'>Train passes over point which has lost its end position (Endlage)</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.4]</td><td style='text-align: center;'>Train passes over point which indicates a wrong position</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.5]</td><td style='text-align: center;'>Level crossing occupied by road vehicle or pedestrians</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.6]</td><td style='text-align: center;'>Railway workers on track or near track (might be dangerous at high speed)</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.7]</td><td style='text-align: center;'>Trucks and other construction trains</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.8]</td><td style='text-align: center;'>Runaway railway trains</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-2.9]</td><td style='text-align: center;'>Level crossing blocked longer than necessary</td><td style='text-align: center;'>-</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-3]</td><td style='text-align: center;'>Train leaves allowed/provisioned/allocated/reserved clearance gauge</td><td style='text-align: center;'>[L-1, L-2, L-3]</td></tr><tr><td style='text-align: center;'>[H-3.1]</td><td style='text-align: center;'>Train derailment and possibly collision with railway trains or other obstacles</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-3.2]</td><td style='text-align: center;'>Train violating clearance gauge due to e.g., overhanging cargo</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-3.3]</td><td style='text-align: center;'>Train violating clearance gauge due to running on two tracks simultaneously (“Gabelfahrt”)</td><td style='text-align: center;'>-</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-4]</td><td style='text-align: center;'>Train exposes passengers to high forces</td><td style='text-align: center;'>[L-1]</td></tr><tr><td style='text-align: center;'>[H-4.1]</td><td style='text-align: center;'>Train applies non-appropriate (excessive) braking technique</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-4.2]</td><td style='text-align: center;'>Train coupling with too high speed</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-4.3]</td><td style='text-align: center;'>Train overspeeding in curves</td><td style='text-align: center;'>-</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-5]</td><td style='text-align: center;'>Train exposes people outside the train to high forces (e.g., platform, level crossing, railway workers)</td><td style='text-align: center;'>[L-2]</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-6]</td><td style='text-align: center;'>Train loses integrity of the train frame</td><td style='text-align: center;'>[L-1, L-2, L-3]</td></tr><tr><td style='text-align: center;'>[H-6.1]</td><td style='text-align: center;'>Environmental damage due to loss of dangerous goods</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-6.2]</td><td style='text-align: center;'>Runaway wagon (train integrity lost - train brakes apart)</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-6.3]</td><td style='text-align: center;'>Train frame damaged due to obstacle violating clearance gauge Note: This is currently not controllable</td><td style='text-align: center;'>-</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-7]</td><td style='text-align: center;'>Train enters an unsafe region (e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, etc.) or train cannot leave unsafe region (e.g., tunnel fire) in acceptable time frame</td><td style='text-align: center;'>[L-1]</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Losses</td></tr><tr><td style='text-align: center;'>[H-8]</td><td style='text-align: center;'>Train violates utilization conditions of the infrastructure</td><td style='text-align: center;'>[L-1, L-2, L-3]</td></tr><tr><td style='text-align: center;'>[H-8.1]</td><td style='text-align: center;'>Train exceeds maximum allowed speed - overspeeding</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-8.2]</td><td style='text-align: center;'>Train not covered by allowed train types (axle load, track gauge, clearance gauge, emergency running characteristics, air-tight system, etc.)</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[H-8.3]</td><td style='text-align: center;'>Damage to infrastructure after temporary change of utilization conditions, which in consequence can cause derailment of following trains.</td><td style='text-align: center;'>-</td></tr></table>

<div style="text-align: center;">Table 12 – Hazards</div>

---

### 5.3 SYSTEM LEVEL CONSTRAINTS

Legend of the following table:

ID ___ a unique identifier

Name ... a description of the system level constraints

ID Hazards ... a list of hazards associated with this system level constraints

#### 5.3.1 Collision Avoidance


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-1]</td><td style='text-align: center;'>Trains must maintain a safe distance to other trains or obstacles.</td><td style='text-align: center;'>[H-1, H-2]</td></tr><tr><td style='text-align: center;'>[SC-1.1]</td><td style='text-align: center;'>Areas reserved for train movement must not overlap.</td><td style='text-align: center;'>[H-1]</td></tr><tr><td style='text-align: center;'>[SC-1.2]</td><td style='text-align: center;'>The permissible speed must be such that it is always possible to decelerate/brake the train in the area reserved for it.</td><td style='text-align: center;'>[H-1.1, H-2.1, H-8.1]</td></tr><tr><td style='text-align: center;'>[SC-1.3]</td><td style='text-align: center;'>Conditions which limit the braking performance must be taken into account. (e.g. wet tracks or leaves on the track)</td><td style='text-align: center;'>[H-1.1, H-2.1]</td></tr><tr><td style='text-align: center;'>[SC-1.4]</td><td style='text-align: center;'>The safety distance must be large enough so that the residual risk of a collision is acceptable even if the braking performance is worse than expected. (coupling of trains should still be possible → “safe collision” of trains)</td><td style='text-align: center;'>[H-1.1, H-2.1]</td></tr><tr><td style='text-align: center;'>[SC-1.5]</td><td style='text-align: center;'>The ability of trains to maintain the braking curve must be supervised, a violation must be detected and measures taken to prevent collisions. (e.g. emergency brake and/or deceleration of other trains, warning/closing of level crossings)</td><td style='text-align: center;'>[H-1.2, H-2.2]</td></tr><tr><td style='text-align: center;'>[SC-1.6]</td><td style='text-align: center;'>If a point in an area reserved for train movement loses its end position, this must be detected and the train must be prevented from passing over it or at least the severity must be reduced by decelerating controlled trains and other vehicles.</td><td style='text-align: center;'>[H-1.3, H-2.3, H-3.3]</td></tr><tr><td style='text-align: center;'>[SC-1.7]</td><td style='text-align: center;'>The current state of railway points must be correct with a very high probability. (MBS has no influence on this, except that certain safety application conditions can be required)</td><td style='text-align: center;'>[H-1.4, H-2.4, H-3.3]</td></tr><tr><td style='text-align: center;'>[SC-2]</td><td style='text-align: center;'>If trains violate safe distances to other trains or obstacles, this violation must be detected and measures taken to prevent collision.</td><td style='text-align: center;'>[H-1, H-2]</td></tr><tr><td style='text-align: center;'>[SC-2.1]</td><td style='text-align: center;'>Level crossings in an area reserved for train movement must be secured in a timely manner and other level crossing users must be warned in advance.</td><td style='text-align: center;'>[H-2.5]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-2.2]</td><td style='text-align: center;'>Trains must not pass level crossings too fast, depending on the local conditions (i.e. not completely secured level crossing).</td><td style='text-align: center;'>[H-2.5]</td></tr><tr><td style='text-align: center;'>[SC-2.3]</td><td style='text-align: center;'>If it can be detected that a level crossing is occupied by some other level crossing users, then measures must be taken to reduce the risk of collision to a tolerable level.</td><td style='text-align: center;'>[H-2.5]</td></tr><tr><td style='text-align: center;'>[SC-2.4]</td><td style='text-align: center;'>Railway workers must be warned in time when a train approaches a construction site.</td><td style='text-align: center;'>[H-2.6]</td></tr><tr><td style='text-align: center;'>[SC-2.5]</td><td style='text-align: center;'>Trains must not pass railway workers (construction sites) too fast. (speed depends on the distance of the train to the railway workers)</td><td style='text-align: center;'>[H-2.6]</td></tr><tr><td style='text-align: center;'>[SC-2.6]</td><td style='text-align: center;'>If trucks or other construction trains intersect an area reserved for a train movement, this must be detected and measures taken to prevent collision.</td><td style='text-align: center;'>[H-2.7]</td></tr><tr><td style='text-align: center;'>[SC-2.7]</td><td style='text-align: center;'>Runaway railway trains must be detected (e.g. detection using TIMS, TTD, etc.) and measures taken to reduce the risk of collision to a tolerable level.</td><td style='text-align: center;'>[H-2.8, H-6.2]</td></tr><tr><td style='text-align: center;'>[SC-2.8]</td><td style='text-align: center;'>Level crossings must not be blocked longer as necessary (i.e. barriers are to be opened as soon as the train has passed over the level crossing).</td><td style='text-align: center;'>[H-2.9]</td></tr></table>

<div style="text-align: center;">Table 13 – Collision Avoidance</div>


<div style="text-align: center;">5.3.2 Clearance Gauge – Derailment</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-3]</td><td style='text-align: center;'>Trains must stay within their reserved clearance gauge.</td><td style='text-align: center;'>[H-3]</td></tr><tr><td style='text-align: center;'>[SC-3.1]</td><td style='text-align: center;'>Trains must be compatible with the infrastructure. (i.e. if axle load, track gauge, clearance gauge, minimum brake performance, ... do not match or is not met, the train must not use this section of line)</td><td style='text-align: center;'>[H-3.1, H-8.2]</td></tr><tr><td style='text-align: center;'>[SC-3.2]</td><td style='text-align: center;'>Trains must comply with the utilization conditions of the infrastructure. (i.e. the maximum permitted speed, which may depend on the actual train, must not be exceeded) Note: Here (SC-3.1 and SC-3.2) a distinction is made between the more static and the more dynamic conditions.</td><td style='text-align: center;'>[H-3.1]</td></tr><tr><td style='text-align: center;'>[SC-3.3]</td><td style='text-align: center;'>If the utilization conditions are violated by a train, this must be detected and measures taken to reduce the risk of derailment.</td><td style='text-align: center;'>[H-3.1]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-3.4]</td><td style='text-align: center;'>If the clearance gauge is violated by a train, this must be detected (e.g. using checkpoint installations) and measures taken to reduce the risk of accidents. Note: checkpoint installations may be able to detect more issues like fire in the train, hot box, hot wheel, derailed axle.</td><td style='text-align: center;'>[H-3.2]</td></tr></table>

<div style="text-align: center;">Table 14 – Clearance Gauge</div>


#### 5.3.3 High Forces


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-4]</td><td style='text-align: center;'>Train must not expose passengers to high forces.</td><td style='text-align: center;'>[H-4]</td></tr><tr><td style='text-align: center;'>[SC-4.1]</td><td style='text-align: center;'>Trains must not use excessive braking technique (i.e. emergency brake), if other measures are possible that reduce the risk of passenger injury to an acceptable value.</td><td style='text-align: center;'>[H-4.1]</td></tr><tr><td style='text-align: center;'>[SC-4.2]</td><td style='text-align: center;'>Coupling of trains must be done at a speed so that the risk of passenger injury is acceptable.</td><td style='text-align: center;'>[H-4.2]</td></tr><tr><td style='text-align: center;'>[SC-4.3]</td><td style='text-align: center;'>The speed of trains in curves must not expose passengers to an unacceptable risk. Note: This maximum speed depends on the radius of the curve, superelevation and tilting technology.</td><td style='text-align: center;'>[H-4.3]</td></tr><tr><td style='text-align: center;'>[SC-5]</td><td style='text-align: center;'>Trains must not expose people outside the train to high forces.</td><td style='text-align: center;'>[H-5]</td></tr><tr><td style='text-align: center;'>[SC-6]</td><td style='text-align: center;'>If train loses its train integrity, this must be detected and measures taken to prevent collision.</td><td style='text-align: center;'>[H-6]</td></tr></table>

<div style="text-align: center;">Table 15 – High Forces</div>


<div style="text-align: center;">5.3.4 Runaway Trains</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-6.1]</td><td style='text-align: center;'>If train loses its train integrity (i.e. runaway wagon), this must be detected and measures taken to reduce the risk of accidents. Note: This can be detected by monitoring train integrity (TIM), cold movement detectors or by TTD where available.</td><td style='text-align: center;'>[H-6.2]</td></tr><tr><td style='text-align: center;'>[SC-6.2]</td><td style='text-align: center;'>If trains lose dangerous goods, this must be detected and measures taken to reduce the risk of environmental damage. Note: What measures are possible still needs to be investigated.</td><td style='text-align: center;'>[H-6.1]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-6.3]</td><td style='text-align: center;'>If the train frame is damaged, this must be detected and measures taken to reduce the risk of passenger injury. Note: Usually handled during inspections or through observant staff.</td><td style='text-align: center;'>[H-6.3]</td></tr></table>

<div style="text-align: center;">Table 16 – Runaway Trains</div>


#### 5.3.5 Unsafe Regions


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">Note: A unsafe region is not permanently unsafe (no train would be allowed to pass permanently unsafe regions). A region becomes unsafe due to events that cannot be planned, e.g., tunnel fire, landslide, avalanche, broken rails, storm, flooding, ... Nevertheless, it is possible to detect these events with the use of sensors, or the operator (informed by e.g., the driver) manually instructs the system.</td></tr><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-7]</td><td style='text-align: center;'>Trains must not be exposed to unsafe regions.</td><td style='text-align: center;'>[H-7]</td></tr><tr><td style='text-align: center;'>[SC-7.1]</td><td style='text-align: center;'>Trains must not enter unsafe regions.</td><td style='text-align: center;'>[H-7]</td></tr><tr><td style='text-align: center;'>[SC-7.2]</td><td style='text-align: center;'>Trains must leave unsafe region in acceptable time frame (e.g. tunnel or bridge, where safe passenger egress is not possible (i.e., non-stopping area)).</td><td style='text-align: center;'>[H-7]</td></tr></table>

<div style="text-align: center;">Table 17 – Unsafe Regions</div>


<div style="text-align: center;">5.3.6 Utilization Conditions</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Hazards</td></tr><tr><td style='text-align: center;'>[SC-8]</td><td style='text-align: center;'>Trains must not violate the utilization conditions of the infrastructure.</td><td style='text-align: center;'>[H-8]</td></tr><tr><td style='text-align: center;'>[SC-8.1]</td><td style='text-align: center;'>The utilization conditions must model the infrastructure in a way that compliance with these utilization conditions results in a tolerable risk of train movements. Note: This condition results in a requirement for data quality.</td><td style='text-align: center;'>[H-8.1, H-8.2]</td></tr><tr><td style='text-align: center;'>[SC-8.2]</td><td style='text-align: center;'>Temporary change or degradation of the infrastructure must be incorporated in the utilization conditions modelling the restrictions on how the infrastructure can be used with a tolerable risk.</td><td style='text-align: center;'>[H-8.3]</td></tr></table>

<div style="text-align: center;">Table 18 – Utilization Conditions</div>

---

### 5.4 HIERARCHICAL CONTROL STRUCTURE (HCS)

The hierarchical control structure models the system using functional components called controllers. Higher level controllers may enforce constraints on the controlled system by using control actions. Additionally, controllers may receive information from other controllers as feedback. Together the controllers form feedback control loops, shaping the overall behavior of the system.

Which actions a controller performs is determined by its control algorithm, representing the decision-making process. The information available to the controller at decision time is represented by the process model. A simple case of a control feedback loop is illustrated in Figure 5.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7bca5d82-f338-4c1a-b417-a8f9394de746/markdown_0/imgs/img_in_image_box_323_531_877_987.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A46%3A51Z%2F-1%2F%2F40809f100ca114439c96d1336154b936fc14af89c7348a30b149b86b5c27e58c" alt="Image" width="46%" /></div>


<div style="text-align: center;">Figure 5 - Simple control-loop</div>


The controller in the hierarchical control structure (HCS) is a functional representation, which may represent a single system or multiple system. A controller may be a human as well as a technical system. The control structure may be represented using multiple levels, where system details for lower levels are added as needed for the analysis.

A very high-level control structure for the CCS system is shown in Figure 6.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e0772f3e-1e33-4a0c-aff9-094273fe2db7/markdown_0/imgs/img_in_image_box_91_173_1112_947.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A46%3A54Z%2F-1%2F%2F53966d1fd2fa67cfeabf5807b9294806b5a55d5df5222375ac7c75d5db83fb1a" alt="Image" width="85%" /></div>


<div style="text-align: center;">Figure 6 - High level control structure of the CCS system. The red rectangle highlights the controller containing the MBS system</div>


Further detail is shown in Figure 7. The hierarchical control structure from Figure 6 is further decomposed to highlight the interaction of the moving block subsystem with other controllers.

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//87f7ad4c-3569-49dc-b960-1aef0b3e64f7/markdown_0/imgs/img_in_image_box_105_176_1095_701.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A46%3A58Z%2F-1%2F%2F486f53fefb3cf178df0acd9c54a36f1515315fafabdaae944d995fe8822e6149" alt="Image" width="83%" /></div>


<div style="text-align: center;">Figure 7 - Schematic second level control structure with focus on the trackside automation system. The red rectangle highlights the Moving Block Demonstrator (MBD)</div>


Further below, in chapter 5.7 the MBD will be broken down into individual control loops between MBS and its adjacent systems.

### 5.5 ASSUMPTIONS

When analyzing a (not yet fully specified) system, a number of assumptions about its environment and internal operations are needed. Assumptions from the WP13 System Definition (as recorded in  $ [17] $ ) are used where they are directly relevant for the safety analysis. The corresponding System Description IDs are referenced at the end of the assumptions in square brackets where applicable.

Legend of the following table:

ID ___ a unique identifier

Name ___ a description of the assumption

ID Overall ... a list of overall mitigation associated with these assumptions


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Overall</td></tr><tr><td style='text-align: center;'>[ASM-1]</td><td style='text-align: center;'>MBS communicates using standardized interfaces with the field elements (Eulynx).</td><td style='text-align: center;'>[14]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Overall</td></tr><tr><td style='text-align: center;'>[ASM-2]</td><td style='text-align: center;'>MBS receives position information from the trains OBU and uses the train position information to derive movement authorities (train centric approach).</td><td style='text-align: center;'>[G1]</td></tr><tr><td style='text-align: center;'>[ASM-3]</td><td style='text-align: center;'>Only ETCS Level 2 (previously Level 2/3 or R) equipped trains are supported by the MBS during normal operation. Trains without TIMS are supported for migration scenarios, when TTDs are available.</td><td style='text-align: center;'>[G2]</td></tr><tr><td style='text-align: center;'>[ASM-4]</td><td style='text-align: center;'>MBS does not require TTDs but supports them for migration scenarios.</td><td style='text-align: center;'>[G3]</td></tr><tr><td style='text-align: center;'>[ASM-5]</td><td style='text-align: center;'>MBS aims to have as little manual intervention (e.g. by the operator) as possible.</td><td style='text-align: center;'>[G4]</td></tr><tr><td style='text-align: center;'>[ASM-6]</td><td style='text-align: center;'>MBS operation assumes trains are equipped with a TIMS (Train integrity monitoring system). However, in degraded modes and for migration purposes operation without TIMS is supported as well.</td><td style='text-align: center;'>[G5]</td></tr><tr><td style='text-align: center;'>[ASM-7]</td><td style='text-align: center;'>MBS is responsible for safety control and should contain a generic and simple safety logic. The operational commands are generated by other systems.</td><td style='text-align: center;'>[A2]</td></tr><tr><td style='text-align: center;'>[ASM-8]</td><td style='text-align: center;'>Train length and train integrity confirmation are relevant for a SIL 4 functions and therefore have to be provided with appropriate correctness guarantees for these functions.</td><td style='text-align: center;'>[T0]</td></tr><tr><td style='text-align: center;'>[ASM-9]</td><td style='text-align: center;'>The train length reported by the OBU represents the maximum train length (e.g. after stretching).</td><td style='text-align: center;'>[T1]</td></tr><tr><td style='text-align: center;'>[ASM-10]</td><td style='text-align: center;'>Changes in the communication technology to the Trains will neither affect the content of the messages defined in the ETCS Definitions nor the transit time (TBD s) of the messages between the Moving Block System and the trains.</td><td style='text-align: center;'>[T2]</td></tr><tr><td style='text-align: center;'>[ASM-11]</td><td style='text-align: center;'>MBS functionality does not change whether the train is operated by a human driver or ATO.</td><td style='text-align: center;'>[T3, T4]</td></tr><tr><td style='text-align: center;'>[ASM-12]</td><td style='text-align: center;'>MBS requires that the cold movement of trains is detected. This could be performed e.g. by a cold movement detection device (CMD device).</td><td style='text-align: center;'>[T7]</td></tr><tr><td style='text-align: center;'>[ASM-13]</td><td style='text-align: center;'>The Train OBU and the infrastructure elements/OCs are SIL-4 systems.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-14]</td><td style='text-align: center;'>The PE can be a SIL Basic Integrity safety related and non-safety related system.</td><td style='text-align: center;'>-</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID Overall</td></tr><tr><td style='text-align: center;'>[ASM-15]</td><td style='text-align: center;'>The integrity of communication between the train OBU and MBS is ensured by a SIL-4 system.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-16]</td><td style='text-align: center;'>The integrity of communication between the train infrastructure elements/OCs and MBS is ensured by a SIL-4 system.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-17]</td><td style='text-align: center;'>Object controllers are correctly installed and configured. This can be checked by operational procedures with optional automated support (e.g. flagging the configuration as correct after multiple successful train passages) (i.e. the position reported by a railway point will not be incorrect due to wrong wiring of the 4-wire-bus).</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-18]</td><td style='text-align: center;'>Every train is identified by a unique and unchangeable identifier.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-19]</td><td style='text-align: center;'>MBS assumes that the train is declared compliant (&quot;zugelassen&quot;) with the tracks by the IM.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-20]</td><td style='text-align: center;'>A train must be able to stop before the EoA/danger point. The braking curve is supervised by the trains OBU.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-21]</td><td style='text-align: center;'>Safety Related text messages will not be sent by the operator. Instead, such message should be generated by automated systems (e.g., MBS).</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-22]</td><td style='text-align: center;'>Interaction between the operator and MBS only involves safety related information.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-23]</td><td style='text-align: center;'>Other interactions of the operator with the system are done via the PE or the TMS.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-25]</td><td style='text-align: center;'>All information received from the operator panel is relevant for one AoC only. This implies that it is not necessary to exchange this information between MBS and neighbouring systems.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-26]</td><td style='text-align: center;'>The received information about the infrastructure (geographical position of tracks, points, etc.) correctly represent physical reality. An external controller is responsible for the data validation process. Rationale: MBS safety functions depend on this input but cannot verify the input independently.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-27]</td><td style='text-align: center;'>When train integrity is lost, the main reservoir pipe is vented and the train emergency breaks engage.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>[ASM-28]</td><td style='text-align: center;'>Operator informs the MBS, about all regions where a train movement has been manually authorised by the operator. This also includes situations, where the radio connections to the OBU is lost.</td><td style='text-align: center;'>-</td></tr></table>

<div style="text-align: center;">Table 19 – Assumptions</div>

---

### 5.6 SAFETY RESPONSIBILITIES

The following chapter provides an overview for the safety related responsibilities of MBS and its adjacent systems (MBD components).

Legend of the following table:

ID ... a unique identifier

Name ... a description of the safety responsibilities

ID SLC ... a list of system level constraints associated with this safety responsibility

#### 5.6.1 Moving Block System (MBS)

The responsibilities of MBS essentially comprise the following areas:

- Assess risk of commands for trains and infrastructure elements. Reject commands, which will result in an unsafe situation. Forward or process safety-validated commands.

- Intervention if risk of railway accidents is not tolerable (e.g., point in reservation area loses its end position, train moving too fast, runaway trains, ...).

- Safe communication with trains and field elements

- Provide an up-to-date, reliable and consistent system view of trains, infrastructure and other relevant parties (e.g., level crossings)

They are described in more detail below:


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Collision Avoidance:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-1]</td><td style='text-align: center;'>Calculate the intersection of the area of movement permissions requested by the PE with other areas reserved for train movements (and the area of trains itself). Movement permissions which intersect or have insufficient distance shall be rejected.</td><td style='text-align: center;'>[SC-1.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-2]</td><td style='text-align: center;'>Provide speed restrictions, gradients and national values defined by the IM to the OBU.</td><td style='text-align: center;'>[SC-1.2, SC-3.3]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-3]</td><td style='text-align: center;'>Provide adhesion factor profile based on information of the operator, automatic detection (e.g. WSP) or weather forecast.</td><td style='text-align: center;'>[SC-1.3]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td style='text-align: center;'>[Resp-MBS-4]</td><td style='text-align: center;'>Check the dynamically (within MBS) generated static speed profile of trains, taking into account the train properties, the utilization conditions and the national values of the infrastructure.</td><td style='text-align: center;'>[SC-1.2, SC-1.4]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-5]</td><td style='text-align: center;'>Verify that the safe distance between the EoA and other authorizations, trains or obstacles is big enough (depends on the mode: SR, OS, FS).</td><td style='text-align: center;'>[SC-1.4, SC-3.3]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-6]</td><td style='text-align: center;'>Verify that the max permitted distance for a train that runs in SR mode is clear of other authorizations, trains or obstacles.</td><td style='text-align: center;'>[SC-1.4]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-7]</td><td style='text-align: center;'>Check the location (and speed) reported by the trains and provide emergency stop command to the OBU, if the probability for leaving the reservation area is too high (or the permitted speed is violated).</td><td style='text-align: center;'>[SC-1.5, SC-3.3]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-8]</td><td style='text-align: center;'>Monitor location/speed reported by trains and in case that they will probably leave the area reserved for their movement protect and warn the affected environment.</td><td style='text-align: center;'>[SC-1.5]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-9]</td><td style='text-align: center;'>Supervise required point positions (in areas reserved for movement) and in case a point loses its end position and performs safety reaction.</td><td style='text-align: center;'>[SC-1.6]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-10]</td><td style='text-align: center;'>Support checking the infrastructure after maintenance (e.g., allowing the first train only to pass in OS mode after track maintenance).</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-11]</td><td style='text-align: center;'>Prohibit usage of malfunctioning infrastructure elements (e.g., set a usage restriction for a malfunctioning point reported by a train driver to the operator).</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-12]</td><td style='text-align: center;'>Detect malfunctioning infrastructure elements (e.g., train takes wrong direction passing a point) and report those to the operator.</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-13]</td><td style='text-align: center;'>Check and monitor that level crossing in areas reserved for train movement are secured in a timely manner.</td><td style='text-align: center;'>[SC-2.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-14]</td><td style='text-align: center;'>Check that the speed of trains passing over not completely secured level crossings is not too high. Note: this restriction is already part of the static speed profile of movement permissions.</td><td style='text-align: center;'>[SC-2.2, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-15]</td><td style='text-align: center;'>If obstacles are detected on a level crossing that is/was secured for train movement perform safety reaction.</td><td style='text-align: center;'>[SC-2.3]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td style='text-align: center;'>[Resp-MBS-16]</td><td style='text-align: center;'>Register/remove warning areas for construction sites (including location on the tracks) reported by the railway worker warning systems.</td><td style='text-align: center;'>[SC-2.4]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-17]</td><td style='text-align: center;'>Check that the warning system for railway workers is activated in a timely manner, in case a train is approaching the warning area.</td><td style='text-align: center;'>[SC-2.4]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-18]</td><td style='text-align: center;'>Check that the speed of trains passing construction sites is not too high (e.g. TSR, This is part of the static speed profile of movement permissions and depends on the distance of the train to the railway workers).</td><td style='text-align: center;'>[SC-2.5, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-19]</td><td style='text-align: center;'>If construction trains or other obstacles occupy the tracks of a construction site perform safety reaction.</td><td style='text-align: center;'>[SC-2.6]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-21]</td><td style='text-align: center;'>Warn the operator if runaway trains or other obstacles are detected.</td><td style='text-align: center;'>[SC-2.7, SC-6.2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-22]</td><td style='text-align: center;'>Supervise secured state of level crossings (in areas reserved for movement) and perform safety reaction in case the level crossing loses its secured state.</td><td style='text-align: center;'>[SC-2.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-23]</td><td style='text-align: center;'>Report level crossings which are behind areas reserved for movements and did not open in reasonable time to the operator.</td><td style='text-align: center;'>[SC-2.8]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-45]</td><td style='text-align: center;'>Increase train location accuracy by combining train position reports with TTD occupancy information.</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td colspan="2">Communication with trackside infrastructure elements:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-46]</td><td style='text-align: center;'>Receive the current position of all railway points.</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-47]</td><td style='text-align: center;'>Command the throw over a railway point.</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-48]</td><td style='text-align: center;'>Receive the current occupancy status of all trackside train detection systems (TTDs).</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-49]</td><td style='text-align: center;'>Receive the current status of all level crossings.</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-50]</td><td style='text-align: center;'>Command the opening/closing of level crossings.</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td colspan="2">Train Handover with neighbouring regions:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-39]</td><td style='text-align: center;'>When a train approaches the border of the controlled region, inform the neighbouring system (MBS or interlocking (N-IXL)) and perform a handover.</td><td style='text-align: center;'>[SC-1.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-40]</td><td style='text-align: center;'>When a train approaches the border of the controlled region, inform the neighbouring system (MBS or RBC (N-RBC)) and perform a handover.</td><td style='text-align: center;'>[SC-1.1]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td style='text-align: center;'>[Resp-MBS-41]</td><td style='text-align: center;'>Continue monitoring the train until its rear end has left the rear of control.</td><td style='text-align: center;'>[SC-1.1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-42]</td><td style='text-align: center;'>When an N-RBC announces a train entering the controlled region, check that the risk of the new train is acceptable and - if so - accept the handover from the N-RBC.</td><td style='text-align: center;'>[SC-1.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-43]</td><td style='text-align: center;'>When an N-IXL announces a train entering the controlled region, check that the risk of the new train is acceptable and - if so - accept the handover from the N-IXL.</td><td style='text-align: center;'>[SC-1.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-44]</td><td style='text-align: center;'>Start supervision of the train once it has entered the controlled region.</td><td style='text-align: center;'>[SC-1.1, SC-2]</td></tr><tr><td colspan="2">Clearance Gauge - Derailment:</td><td style='text-align: center;'>[SC-3]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-24]</td><td style='text-align: center;'>Before authorizing a movement permission for a train, check if the infrastructure properties are compatible with the properties of the train.</td><td style='text-align: center;'>[SC-3.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-25]</td><td style='text-align: center;'>Check the consistency of train properties reported by the train itself and provided by the DR/TMS/Operator.</td><td style='text-align: center;'>[SC-3.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-26]</td><td style='text-align: center;'>Before authorizing a movement permission for a train, verify if the utilization conditions are respected by the movement permission.</td><td style='text-align: center;'>[SC-3.2, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-27]</td><td style='text-align: center;'>If utilization conditions for a requested movement permission are violated, the movement permission shall not be authorized.</td><td style='text-align: center;'>[SC-3.3]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-29]</td><td style='text-align: center;'>If a violation of utilization conditions (e.g., violation of the clearance gauge, hot box, hot wheel, fire on board, derailed axle, ...) is reported perform safety reaction.</td><td style='text-align: center;'>[SC-3.4]</td></tr><tr><td colspan="2">Unsafe Regions:</td><td style='text-align: center;'>[SC-7]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-32]</td><td style='text-align: center;'>Inform the operator about conditions of regions which prevent a safe passage of trains.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-33]</td><td style='text-align: center;'>If movement permissions are requested which enter unsafe regions, this movement permissions shall not be authorized.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-34]</td><td style='text-align: center;'>If conditions of unsafe regions are detected in the area reserved for train movement perform safety reaction.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-35]</td><td style='text-align: center;'>Ensure that the risk of reversing trains entering emergency propelling areas is tolerable.</td><td style='text-align: center;'>[SC-7.2]</td></tr><tr><td colspan="2">Utilization Conditions:</td><td style='text-align: center;'>[SC-8]</td></tr><tr><td style='text-align: center;'>[Resp-MBS-37]</td><td style='text-align: center;'>Before new topography data is used for production, plausibility checks (topological properties, e.g., like</td><td style='text-align: center;'>[SC-8.1]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>connectivity) shall be performed. May be delegated to a different controller.</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-MBS-38]</td><td style='text-align: center;'>Temporary changes in utilization conditions of infrastructure elements shall be taken into account when assessing whether a risk is tolerable.</td><td style='text-align: center;'>[SC-8.2]</td></tr></table>

<div style="text-align: center;">Table 20 – Moving Block System Safety Responsibilities</div>


#### 5.6.2 Infrastructure Manager (IM)

The infrastructure manager is responsible for providing a production plan containing the journey timetable. He is also responsible to provide a description of the topology, topography and infrastructure (including axle load, track gauge, clearance gauge, traction system, etc.). The quality of the topography description shall be such that safety-critical decisions can be based on it. This includes guaranteed limits for accuracy and specifying confidence intervals for numerical values. In addition, changes (temporary or permanent) of the topography description shall be provided to the system in a timely manner. This includes emergency measures and other interventions from the operation personnel.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Collision Avoidance:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-IM-1]</td><td style='text-align: center;'>Provide national values which are compliant with the requirements of static risk assessment.</td><td style='text-align: center;'>[SC-1.2, SC-4.1]</td></tr><tr><td style='text-align: center;'>[Resp-IM-2]</td><td style='text-align: center;'>Instructions for operators and drivers concerning low adhesion factor conditions.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td colspan="2">Clearance Gauge - Derailment:</td><td style='text-align: center;'>[SC-1.2, SC-4.1]</td></tr><tr><td style='text-align: center;'>[Resp-IM-3]</td><td style='text-align: center;'>Provide topography, topology, configuration- and infrastructure data. (e.g. axle load, track gauge, clearance gauge, traction system, static speed profile, etc.).</td><td style='text-align: center;'>[SC-3.1, SC-4.3, SC-5]</td></tr><tr><td colspan="2">Utilization Conditions:</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-IM-5]</td><td style='text-align: center;'>The quality of data from [Resp-IM-3] shall be such that safety-critical decisions can be based on it. This includes guaranteed limits for accuracy and specifying confidence intervals for numerical values.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td style='text-align: center;'>[Resp-IM-6]</td><td style='text-align: center;'>Changes (temporary or permanent) of the topography description shall be provided to the system in a timely manner.</td><td style='text-align: center;'>[SC-8.1, SC-8.2]</td></tr></table>

<div style="text-align: center;">Table 21 – Infrastructure Manager Safety Responsibilities</div>

---

#### 5.6.3 Operator

Concerning the operator, we reiterate two important assumptions here:

• interaction between the operator and MBS only involves safety related information [ASM-22]

• other interactions of the operator with the system are done via the PE or the TMS [ASM-23]

The reason for these assumptions is that the PE and TMS implement the operational processes and MBS acts as a gatekeeper that monitors if the risk is tolerable and forwards safe commands/authorities.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Collision Avoidance:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-OP-1]</td><td style='text-align: center;'>Inform Train about track conditions lowering the adhesion factor.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td style='text-align: center;'>[Resp-OP-2]</td><td style='text-align: center;'>Setup/Revoke areas with low adhesion factor.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td style='text-align: center;'>[Resp-OP-3]</td><td style='text-align: center;'>Setup/remove usage restriction areas for malfunctioning infrastructure elements (e.g., set a “Befahrbarkeitssperre” for a malfunctioning point reported by a train driver).</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-OP-4]</td><td style='text-align: center;'>Setup/remove warning areas for construction sites (together with the Picop and provide further information of warning time, max allowed speed, ...).</td><td style='text-align: center;'>[SC-2.4, SC-2.5, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-OP-5]</td><td style='text-align: center;'>Inform MBS about runaway trains, including location on the tracks (and their assumed direction and speed).</td><td style='text-align: center;'>[SC-2.7]</td></tr><tr><td colspan="2">Clearance Gauge - Derailment:</td><td style='text-align: center;'>[SC-3]</td></tr><tr><td style='text-align: center;'>[Resp-OP-6]</td><td style='text-align: center;'>Optionally provide missing train properties.</td><td style='text-align: center;'>[SC-3.1]</td></tr><tr><td colspan="2">Unsafe Regions:</td><td style='text-align: center;'>[SC-7]</td></tr><tr><td style='text-align: center;'>[Resp-OP-8]</td><td style='text-align: center;'>Inform MBS about conditions of regions, which prohibit a safe passage of trains.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-OP-9]</td><td style='text-align: center;'>Prepare emergency propelling areas for reversing trains in unsafe regions.</td><td style='text-align: center;'>[SC-7.2]</td></tr><tr><td style='text-align: center;'>[Resp-OP-10]</td><td style='text-align: center;'>Command trains to leave unsafe regions.</td><td style='text-align: center;'>[SC-7.2]</td></tr><tr><td colspan="2">Utilization Conditions:</td><td style='text-align: center;'>[SC-8]</td></tr><tr><td style='text-align: center;'>[Resp-OP-11]</td><td style='text-align: center;'>Inform MBS about temporary changed utilization conditions of infrastructure elements.</td><td style='text-align: center;'>[SC-8.2]</td></tr></table>

<div style="text-align: center;">Table 22 – Operator Safety Responsibilities</div>

---

#### 5.6.4 Driver

The train driver is responsible for operating the train, this includes e.g.,

• start up the train, perform brake test

• monitor OBU and train status

• selection of the ETCS operation mode

• control traction and brakes

- manually control the train in on-sight mode and decide the speed according to the dispatching orders from the dispatcher

• report emergency information

• take into account journey information from dispatcher to keep the train safe

• provide information to dispatcher when requested to do so

• enter validated train data (i.e., train length)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Collision Avoidance:</td><td style='text-align: center;'>[SC-1, SC-2]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-1]</td><td style='text-align: center;'>Inform Operator about track conditions lowering the adhesion factor.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-2]</td><td style='text-align: center;'>Adjust adhesion factor manually.</td><td style='text-align: center;'>[SC-1.3]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-3]</td><td style='text-align: center;'>Decelerate train to respect the permitted speed and distance to run.</td><td style='text-align: center;'>[SC-1.4, SC-1.5, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-4]</td><td style='text-align: center;'>Report malfunctioning infrastructure elements, when checking is required (e.g., checking point position in OS mode).</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-5]</td><td style='text-align: center;'>Check if the level crossing is free and warn other level crossing users. EB if tracks occupied by obstacles or level crossing users.</td><td style='text-align: center;'>[SC-2.2, SC-2.3]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-6]</td><td style='text-align: center;'>EB if construction site is occupied by railway workers, construction trains or other obstacles.</td><td style='text-align: center;'>[SC-2.6]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-x]</td><td style='text-align: center;'>Check that the track is clear/free (TAF), if required.</td><td style='text-align: center;'>[SC-1]</td></tr><tr><td colspan="2">Clearance Gauge - Derailment:</td><td style='text-align: center;'>[SC-3]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-7]</td><td style='text-align: center;'>Enter the correct train properties (validated train data).</td><td style='text-align: center;'>[SC-3.1, SC-8.1]</td></tr><tr><td colspan="2">High Forces:</td><td style='text-align: center;'>[SC-4, SC-5, SC-6]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-8]</td><td style='text-align: center;'>Coupling of trains shall be done at a speed so that the risk of passenger injury is acceptable.</td><td style='text-align: center;'>[SC-4.2]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td style='text-align: center;'>[Resp-DRV-10]</td><td style='text-align: center;'>If loss of dangerous goods is detected, this shall be reported to the operator.</td><td style='text-align: center;'>[SC-6.2]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-11]</td><td style='text-align: center;'>If a damage of the train frame is apparent, this shall be reported to the operator.</td><td style='text-align: center;'>[SC-6.3]</td></tr><tr><td colspan="2">Unsafe Regions:</td><td style='text-align: center;'>[SC-7]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-12]</td><td style='text-align: center;'>Report conditions which prohibit a safe passage of trains.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-DRV-13]</td><td style='text-align: center;'>If leaving unsafe regions, keep the train movement inside the received distance to run.</td><td style='text-align: center;'>[SC-7.2]</td></tr></table>

<div style="text-align: center;">Table 23 – Driver Safety Responsibilities</div>


#### 5.6.5 On Board Unit (OBU)

The DMI displays to the Driver the current allowed movement authority by using cab signaling (if not an ATO train). The OBU also supervises the speed and ensures that the train does not violate its movement authority. Further it will send the current position as a "train position report" to the MBS.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Collision Avoidance</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-OBU-1]</td><td style='text-align: center;'>Calculation of the dynamic speed profile, taking into account the running/braking characteristics of the train and the track conditions/adhesion factor (specified in the UNISIG-26)</td><td style='text-align: center;'>[SC-1.2, SC-1.3, SC-1.4, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-2]</td><td style='text-align: center;'>Trip the train, if train speed exceeds the permitted speed/ceiling speed or authority is overrun (distance)</td><td style='text-align: center;'>[SC-1.2, SC-1.4, SC-1.5]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-3]</td><td style='text-align: center;'>Cab signalling - display train speed, permitted speed, target distance, target speed to the driver</td><td style='text-align: center;'>[SC-1.4, SC-1.5, SC-5]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-4]</td><td style='text-align: center;'>Supervise movement against running in the direction opposite to the train orientation (reverse movement protection)</td><td style='text-align: center;'>[SC-1.5]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-5]</td><td style='text-align: center;'>Trip the train (apply emergency brake) if commanded by MBS</td><td style='text-align: center;'>[SC-1.5, SC-1.6, SC-2.3, SC-2.6, SC-2.7]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-6]</td><td style='text-align: center;'>Inform the driver when OS mode entered and request an acknowledgement from the driver</td><td style='text-align: center;'>[SC-1.7]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-7]</td><td style='text-align: center;'>Inform the driver when approaching a level crossing</td><td style='text-align: center;'>[SC-2.2, SC-2.3]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">Clearance Gauge - Derailment</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-OBU-8]</td><td style='text-align: center;'>Provide the train properties (validated train data)</td><td style='text-align: center;'>[SC-3.1, SC-8.1]</td></tr><tr><td style='text-align: center;'>[Resp-OBU-9]</td><td style='text-align: center;'>Periodically send position reports (interval parameters requested/configured by the track-side or national values; including position, direction, speed and the accuracy of this values)</td><td style='text-align: center;'>[SC-3.3]</td></tr><tr><td colspan="2">High Forces</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-OBU-10]</td><td style='text-align: center;'>The driver shall be supported in coupling activities so that the risk of passenger injury is acceptable. (e.g. measure distance, display it and issue distance warnings)</td><td style='text-align: center;'>[SC-4.2]</td></tr><tr><td colspan="2">Unsafe Regions</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-OBU-11]</td><td style='text-align: center;'>Supervise movement in reversing mode (distance and ceiling speed)</td><td style='text-align: center;'>[SC-7.2]</td></tr><tr><td colspan="2">Utilization Conditions</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[Resp-OBU-12]</td><td style='text-align: center;'>Provide and check the system version</td><td style='text-align: center;'>[SC-8.1]</td></tr></table>

<div style="text-align: center;">Table 24 – On Board Unit Safety Responsibilities</div>


#### 5.6.6 Maintenance workers

The maintenance workers are responsible for the upkeep of the infrastructure. They perform scheduled maintenance work as well as on-demand maintenance when infrastructure elements fail or report abnormal behavior.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Unsafe Regions:</td><td style='text-align: center;'>[SC-7]</td></tr><tr><td style='text-align: center;'>[Resp-MNT-1]</td><td style='text-align: center;'>Inform operator of conditions of infrastructure elements on-site.</td><td style='text-align: center;'>[SC-7.1]</td></tr><tr><td style='text-align: center;'>[Resp-MNT-2]</td><td style='text-align: center;'>Determine on-site whether train passage over infrastructure element is safe.</td><td style='text-align: center;'>[SC-7.1, SC-1.6]</td></tr><tr><td style='text-align: center;'>[Resp-MNT-3]</td><td style='text-align: center;'>Repair damaged infrastructure elements and restore drivability of such elements.</td><td style='text-align: center;'>[SC-7.1]</td></tr></table>

<div style="text-align: center;">Table 25 – Maintenance Workers Safety Responsibilities</div>


#### 5.6.7 Digital Register

The Digital Register (DR) is responsible for the compilation, versioning, validation and distribution of topology, topography, infrastructure- and configuration data.

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ID</td><td style='text-align: center;'>Name</td><td style='text-align: center;'>ID SLC</td></tr><tr><td colspan="2">Utilization Conditions:</td><td style='text-align: center;'>[SC-7, SC-8]</td></tr><tr><td style='text-align: center;'>[Resp-DR-1]</td><td style='text-align: center;'>Validates that the topology and topography data is consistent with physical reality.</td><td style='text-align: center;'>[SC-8.1]</td></tr><tr><td style='text-align: center;'>[Resp-DR-2]</td><td style='text-align: center;'>Verifies that the topology and topography data meet the data engineering and validation rules.</td><td style='text-align: center;'>[SC-7.1, SC-8.1]</td></tr><tr><td style='text-align: center;'>[Resp-DR-3]</td><td style='text-align: center;'>Provides validated topology and topography data to PE, MBS and OBU relevant for their region of control.</td><td style='text-align: center;'>[SC-8.1]</td></tr><tr><td style='text-align: center;'>[Resp-DR-4]</td><td style='text-align: center;'>Ensures synchronized activation of new data versions in PE, MBS and OBU.</td><td style='text-align: center;'>[SC-7.1, SC-8.2]</td></tr></table>

<div style="text-align: center;">Table 26 – Digital Register Safety Responsibilities</div>

---

### 5.7 CONTROL LOOP ANALYSIS

In the following, relevant control and feedback loops are considered across the most important interfaces. Later in the analysis, these can be explored in greater depth or the respective systems can be broken down into smaller controllers/actors.

A subset of the unsafe control actions was selected for further scenario generation. This was done due to the focus on changes system design, where the behavior of the moving block system differs from traditional fixed block systems.

Legend of the following tables:

Controllers ... modules involved in this analysis

Control Actions ... list of possible control actions to the controlled item

Feedbacks ... list of possible feedbacks from the controlled item

Process Model ... controlled process that fulfils a defined action

Control Algorithm ... a defined function that controls the process

Remarks ... a comment field for additional optional comments or remarks

[UCA-] ... unsafe control action

[SDR-] ... safety design recommendation

#### 5.7.1 I\_OP Interface

<div style="text-align: center;">Operator Panel <-> MBS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Controllers</td><td style='text-align: center;'>·Operator Panel:·MBS:</td></tr><tr><td style='text-align: center;'>Control Actions:</td><td style='text-align: center;'>·OP -&gt; MBS:      ○ Set known infrastructure state      ○ Setup/revoke temporary Usage Restriction Area      ○ Emergency Text Messages to Driver (seldomly used)      ○ Conditional/Unconditional emergency Stop      ○ Command confirmation (command dependent)      ○ Setup/revoke warning areas for construction sites</td></tr><tr><td style='text-align: center;'>Feedbacks:</td><td style='text-align: center;'>·MBS -&gt; OP:      ○ Command Received/Rejected      ○ Safety/Operational implications      ○ Request command confirmation (command dependent)      ○ Operation Succeeded/Failed + Reason</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>○ Operational State</td></tr><tr><td style='text-align: center;'>Process Model</td><td style='text-align: center;'>• MBS○ Operational State• OP○ Panel: Request state/Command state○ Operator: TMS/PE System View / Operational knowledge / Real world knowledge</td></tr><tr><td style='text-align: center;'>Control Algorithm</td><td style='text-align: center;'>• MBS○ Semantic/Syntactic command check○ Determine safety implications○ Confirmation loop (command dependent)○ Forward command and/or update known infrastructure state.○ Provide feedback• OP○ Operational Rules○ Operational state from MBS○ Known state of real world from other sources○ Mental model of command implications.</td></tr><tr><td style='text-align: center;'>Remarks</td><td style='text-align: center;'>Operator shall be able to conduct temporary safety related interventions and enact temporary infrastructure restrictions.Only safety related commands are considered via the I_OP interface. Non-critical/standard commands can be sent via PE and subsequently I_PE.</td></tr></table>

<div style="text-align: center;">Unsafe Control Actions:</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td colspan="3">Hazardous when</td></tr><tr><td style='text-align: center;'>Control action</td><td style='text-align: center;'>Provided</td><td style='text-align: center;'>Not Provided</td><td style='text-align: center;'>Provided too late/early</td></tr><tr><td style='text-align: center;'>Set known infrastructure state</td><td style='text-align: center;'>UCA-OP-1: Operator provides known infrastructure state when set state does not match reality [H1, H2]</td><td style='text-align: center;'>UCA-OP-2: Operator does not provide a known infrastructure state when that known state is worse in reality than the operational state of MBS [H-8.1, H-8.3]</td><td style='text-align: center;'>UCA-OP-3: Operator provides a known infrastructure state too late when that state is worse in reality than the operational state of MBS [H-8.1, H-8.3]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td rowspan="2">Setup/revoke temporary Usage Restriction Area</td><td style='text-align: center;'>UCA-OP-4: Operator provides temporary usage restriction when usage restriction has excessive limits (too high-speed limit) [H-8.1, H-8.2]</td><td style='text-align: center;'>UCA-OP-6: Operator does not provide temporary usage restriction area when conditions (for this area) are worse than depicted in the operational state of MBS [H-8.1, H-8.2]</td><td style='text-align: center;'>UCA-OP-7: Operator provides temporary usage restriction area too late where conditions are worse than depicted in the operational state of MBS [H-8.1, H-8.2]</td></tr><tr><td style='text-align: center;'>UCA-OP-5: Operator provides revocation of temporary usage restriction area when the usage restriction should still be applied [H-8.1, H-8.2]</td><td style='text-align: center;'></td><td style='text-align: center;'>UCA-OP-26: Operator provides revocation of temporary usage restriction area too early when the usage restriction should still be applied [H-8.1, H-8.2]</td></tr><tr><td style='text-align: center;'>Conditional/Unconditional emergency Stop</td><td style='text-align: center;'>UCA-OP-14: Operator provides emergency stop command for wrong train [H-4.1]
UCA-OP-15: Operator provides conditional emergency stop command with wrong stopping position [H-1, H-2]
UCA-OP-16: Operator provides conditional emergency stop command where an unconditional emergency stop command is required [H-1, H-2]</td><td style='text-align: center;'>UCA-OP-17: Operator does not provide safety related conditional/unconditional emergency stop [H-1, H-2]</td><td style='text-align: center;'>UCA-OP-18: Operator provides safety related conditional/unconditional emergency stop too late [H-1, H-2]</td></tr><tr><td style='text-align: center;'>Command confirmation (command dependent)</td><td style='text-align: center;'>UCA-OP-19: Operator provides command confirmation for the wrong train/</td><td style='text-align: center;'>UCA-OP-21: Operator does not provide command confirmation (any of the unsafe</td><td style='text-align: center;'>UCA-OP-22: Operator provides command confirmation too late (any of the unsafe</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>infrastructure element / message [H1, H2, H7, H8] UCA-OP-20: Operator provides command confirmation without consideration of safety implications for other trains [H1, H2, H7, H8]</td><td style='text-align: center;'>actions above) [H1, H2, H7, H8]</td><td style='text-align: center;'>actions above) [H1, H2, H7, H8]</td></tr><tr><td style='text-align: center;'>Setup/revoke warning areas for construction sites</td><td style='text-align: center;'>UCA-OP-23: Operator provides command to revoke warning are for construction site when the railway workers are still on site. [H-5]</td><td style='text-align: center;'>UCA-OP-24: Operator does not provide setup command for area of construction site before the construction begins. [H-5]</td><td style='text-align: center;'>UCA-OP-25: Operator provides command to revoke warning are for construction site to early when the railway workers are still on site. [H-5]</td></tr></table>

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

<div style="text-align: center;">5.7.2 I\_OBU Interface MBS -> OBU</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Controllers</td><td style='text-align: center;'>• MBS• OBU</td></tr><tr><td style='text-align: center;'>Control Actions:</td><td style='text-align: center;'>• MBS -&gt; OBU:1    ○ Configuration Values (National values)    ○ SR Authorization (distance)    ○ FS/OS Movement Authority    ○ Conditional/Unconditional Emergency Stop (CES/UES)    ○ Shorten MA</td></tr><tr><td style='text-align: center;'>Feedbacks:</td><td style='text-align: center;'>• OBU -&gt; MBS:2    ○ MA Request    ○ Train Position Report    ○ Validated Train Data    ○ Acknowledge CES</td></tr><tr><td style='text-align: center;'>Process Model</td><td style='text-align: center;'>• OBU    ○ Static and dynamic properties of train    ○ Current train position (including uncertainties)    ○ Current train speed    ○ ETCS mode    ○ Train Data (train length, running number, etc.)• MBS    ○ Operational state    • Reported train location    • Reported track occupations    • Granted MAs    ○ Infrastructure state    • Topography and geometry    • State of infrastructure elements    • Utilization conditions</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>• Temporary speed restrictions
• National Values</td></tr><tr><td style='text-align: center;'>Control Algorithm</td><td style='text-align: center;'>• OBU
    • Supervise train braking curve
    • Supervise train speed
    • Service break
    • Emergency break
• MBS
    • Safety Logic before granting MA
    • Command conditional/unconditional emergency stop
    • Updating operational state expanded process model
    • Handover to neighboring systems</td></tr></table>

<div style="text-align: center;">Unsafe Control Actions:</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td colspan="3">Hazardous when</td></tr><tr><td style='text-align: center;'>Control action</td><td style='text-align: center;'>Provided</td><td style='text-align: center;'>Not Provided</td><td style='text-align: center;'>Provided too late/early</td></tr><tr><td rowspan="3">Configuration Values (National values)</td><td rowspan="3">[UCA-MBS-6] MBS provides national values to OBU when these values are not conforming to the risk analysis [H-1.1, H-2.1, H-8.1]</td><td style='text-align: center;'>[UCA-MBS-1] MBS does not provide national values to OBU when these values are more restrictive than default values [H-1.1, H-2.1, H-8.1]</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-2] MBS does not provide temporary speed restrictions to the OBU [H-2.6, H-5, H-8.3]</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-3] MBS does not provide track gradients to the OBU [H-1.1, H-2.1]</td><td style='text-align: center;'></td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>[UCA-MBS-4] MBS does not provide inhibition of defined type of brake to the OBU [H-1.1, H-2.1]
[UCA-MBS-5] MBS does not provide the adhesion factor to the OBU when the adhesion conditions are worse than normal [H-1.1, H-2.1]</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>FS/OS Movement Authority</td><td style='text-align: center;'>[UCA-MBS-7] MBS provides MA to the OBU when train type/properties are not compatible to infrastructure [H-3.1, H-8.2]
[UCA-MBS-8] MBS provides MA to the OBU when the MA is intersecting a reservation area of another train [H-1].
[UCA-MBS-9] MBS provides MA to the OBU when the MA has a too small safety distance to other potential obstacles [H-1.1, H-2.1, H-3.1]
[UCA-MBS-10] MBS provides FS/OS MA</td><td style='text-align: center;'></td><td style='text-align: center;'>[UCA-MBS-18] MBS provides MA too early for OBU when not all infrastructure elements along the MA are secured and passable for the train movement [H-1.4, H-2.4, H-3.3]</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="6"></td><td style='text-align: center;'>to the OBU and not all infrastructure elements (points, level crossings, etc.) are prepared and secured for the running path of the train [H-1.4, H-2.4, H-3.3]</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-11] MBS provides FS MA passing over a not completely secured level-crossing [H-2.5, H-5]</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-12] MBS provides MA to OBU when the MA is directing into an unsafe area [H-7].</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-13] MBS provides FS MA to OBU when coupling trains [H-4.2]</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-14] MBS provides MA to OBU when the MA speed profile exceeds the most restrictive speed profile for this train given the running path [H-4.3, H-8.1]</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>[UCA-MBS-15] MBS provides MA to OBU when the MA is ending within a</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>non-stopping area [H-7] [UCA-MBS-16] MBS provides FS MA to OBU when the area reserved for train is not clear of other trains or obstacles [H-1.1, H-2.1] [UCA-MBS-17] MBS provides MA to OBU when other train or obstacles have insufficient distance from the flank of the area reserved for train movement [H-1.1, H-2.1, H-2.8, H-3.1]</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>SR Authorization</td><td style='text-align: center;'>[UCA-MBS-19] MBS provides SR authorization with a too long permitted distance, or into the wrong direction [H-1.1, H-2.1] (Note: this is used only if the position of the train is not known)</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Conditional/Unconditional Emergency Stop (CES/UES)</td><td style='text-align: center;'></td><td style='text-align: center;'>[UCA-MBS-20] MBS does not provide UES to OBU when the train leaves the area reserved for its movement [H-1.2, H-2.2, H-3.1]</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Shorten MA</td><td style='text-align: center;'></td><td style='text-align: center;'>[UCA-MBS-21] MBS does not provide</td><td style='text-align: center;'></td></tr></table>

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


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Controllers</td><td style='text-align: center;'>• MBS• TACS</td></tr><tr><td style='text-align: center;'>Control Actions:</td><td style='text-align: center;'>• MBS -&gt; TACS:    ○ Manage PDI connection³    ○ Move point (SCI-P) ⁴    ○ Open/close/isolate level crossing (SCI-LC)⁵</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>○ Reset track occupancy status (SCI-TDS)6</td></tr><tr><td style='text-align: center;'>Feedbacks:</td><td style='text-align: center;'>· TACS -&gt; MBS:      ○ Manage PDI connection      ○ Report point state (SCI-P)      ○ Report level crossing state (SCI-LC)      ○ Report track occupancy state (SCI-TDS)      ○ Heartbeat [RASTA Protocol]</td></tr><tr><td style='text-align: center;'>Process Model</td><td style='text-align: center;'>· MBS      ○ Operational State· TACS      ○ TACS configuration / parameters      ○ TACS state      ○ TA state</td></tr><tr><td style='text-align: center;'>Control Algorithm</td><td style='text-align: center;'>· MBS      ○ Safety Logic      ○ Supervise TACS heartbeat      ○ Determine safety implications of commands      ○ React to safety related events      ○ Establish communication with TACS      ○ Forward commands to OBU      ○ Sensor fusion· TACS      ○ Provide heartbeat      ○ Compare between TACS state and TA state      ○ Obstacle detection (only LC/LX)      ○ Command new state (for switchable TAs)      ○ Report state update (incl. timeout, degraded states and obstacles)</td></tr><tr><td style='text-align: center;'>Remarks</td><td style='text-align: center;'>Most of this is regulated in the EULYNX Specification.</td></tr></table>

---

<div style="text-align: center;">Unsafe Control Actions</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td colspan="4">Hazardous when</td></tr><tr><td style='text-align: center;'>Control action</td><td style='text-align: center;'>Provided</td><td style='text-align: center;'>Not Provided</td><td style='text-align: center;'>Provided too late/early</td><td style='text-align: center;'>Stopped too soon</td></tr><tr><td style='text-align: center;'>Manage connection</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>Move point</td><td style='text-align: center;'>[UCA-TACS-1]
MBS provides move point command when a train is passing over [H-1.3, H-2.3, H-3.3].
[UCA-TACS-2]
MBS provides move point command when the point is already reserved/locked for another train&#x27;s movement [H-1.3, H-2.3]
[UCA-TACS-3]
MBS provides move point command to wrong direction when preparing reservation area [H-1.4, H-2.4, H-3.1, H-4.3]
[UCA-TACS-4]
MBS provides move point command when the new point position endangers the reservation area of other trains [H-1.4, H-2.4, H-3.1]</td><td style='text-align: center;'>[UCA-TACS-5]
MBS does not move point to required direction when preparing a reservation area [H-1.4, H-2.4, H-3.1].
[UCA-TACS-6]
MBS does not provide move point when a runaway wagon is to be diverted [H-2.8]</td><td style='text-align: center;'>[UCA-TACS-7]
MBS provides move point command too late (after MA has already been sent to the train) when preparing a reservation area [H-1.4, H-2.4, H-3.1, H-3.3, H-4.3]
[UCA-TACS-8]
MBS provides move point command too late (after the wagon has already passed the point) when a runaway wagon is to be diverted [H-2.8]</td><td style='text-align: center;'>[UCA-TACS-9]
MBS stops the supervision of the moved point too soon when the point is still required for a reserved area and the point loses its end position. [H-1.3, H-2.3, H-3.1, H-3.3, H-4.3].</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Open/close level-crossing</td><td style='text-align: center;'>[UCA-TACS-10] MBS provides open level crossing command while the level crossing is still reserved for train movement [H-2.5] [UCA-TACS-11] MBS provides close level crossing command when the level crossing is not required for train movement [H-2.9]</td><td style='text-align: center;'>[UCA-TACS-12] MBS does not provide close level crossing command when the level crossing needs to be closed for train movement [H-2.5] [UCA-TACS-13] MBS does not provide the open level crossing command when the level crossing is no longer required for train movement [H-2.9]</td><td style='text-align: center;'>[UCA-TACS-14] MBS provides close level crossing command too early when a train is approaching [H-2.9]. [UCA-TACS-15] MBS provides close level crossing command too late when a train is approaching [H-2.5]. [UCA-TACS-16]: MBS provides open level crossing command too early when a train is still within the level crossing [H-2.5] [UCA-TACS-17]: MBS provides close level crossing command too late when a train is already within the level crossing [H-2.9]</td><td style='text-align: center;'>[UCA-TACS-18] Supervision of closed level crossing is stopped to soon when still required for train movement [H-2.5].</td></tr><tr><td style='text-align: center;'>Reset track occupancy state</td><td style='text-align: center;'>[UCA-TACS-19] MBS provides reset track occupancy command while a train inside the track occupancy section [H-1, H-2, H-6.2]</td><td style='text-align: center;'>/ Note: this may reduce availability but is not related to safety</td><td style='text-align: center;'>[UCA-TACS-20] MBS provides reset track occupancy command too soon while a wagon is still inside the track</td><td style='text-align: center;'>[UCA-TACS-21] MBS stops the supervision of the track occupancy state too soon while a supervision is still required for train</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>occupancy section [H-1, H-2, H-6.2]</td><td style='text-align: center;'>movement [H-1, H-2]</td></tr></table>

The loss scenarios for trackside assets occur together with unsafe control actions on the I_OBU interface (e.g. granting an MA) and the I_OP interface (e.g., manually reseat a TDS). Often, the state of the trackside assets constitutes the context under which control actions to the OBU or the operator panel becomes unsafe. These loss scenarios are not repeated here, as details on them are already listed in the previous section.

#### 5.7.4 I\_DR Interface

<div style="text-align: center;">MBS <-> DR</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Controllers</td><td style='text-align: center;'>DRMBSS</td></tr><tr><td style='text-align: center;'>Control Actions:</td><td style='text-align: center;'>DR -&gt; MBS• Provide validated topology and topography data.• Provide utilization restrictions (e.g., URA) for topology change.• Activate validated data version (Note: this assumes a new data version was previously provided)• Request currently used validated data version (Note: not safety related)</td></tr><tr><td style='text-align: center;'>Feedbacks:</td><td style='text-align: center;'>MBS -&gt; DR• Confirm data reception• Confirm/reject activation of utilization restriction• Confirm/Reject activation of new data version• Report currently used data version (Assumption: not safety related)</td></tr><tr><td style='text-align: center;'>Process Model</td><td style='text-align: center;'>MBS○ Current operational state (includes utilization restriction)○ Current active data version○ Currently inactive data versions○ Data verification &amp; validation signatures• DR○ Topology and Topography data○ Usage restrictions required for activation○ Data verification &amp; validation signatures</td></tr><tr><td style='text-align: center;'>Control Algorithm</td><td style='text-align: center;'>MBS</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>○ Check if received data is malformed (Note: syntactic check only)○ Check if new data version is compatible with current operational state before activation○ Verify data signatures○ Verify required usage restrictions for topology change are active.• DR○ Validate data input against physical reality (or export responsibility to other entity -&gt;[ASM-26])○ Verify data against data engineering and validation rules○ Compile data version relevant for region of control○ Distribute data to consuming systems.○ Activate new data version synchronously for all recipients</td></tr><tr><td style='text-align: center;'>Remarks</td><td style='text-align: center;'>-</td></tr></table>

<div style="text-align: center;">Unsafe Control Actions</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td colspan="4">Hazardous when</td></tr><tr><td style='text-align: center;'>Control action</td><td style='text-align: center;'>Provided</td><td style='text-align: center;'>Not Provided</td><td style='text-align: center;'>Provided too late/early</td><td style='text-align: center;'>Stopped too soon</td></tr><tr><td style='text-align: center;'>Provide validated topography data</td><td style='text-align: center;'>[UCA-DR-1] DR provides topography data to MBS which has not been verified. [H-8] [UCA-DR-2]: DR provides topography data to MBS which is malformed. [H-8] [UCA-DR-3]: DR provides topography data to MBS which has not been validated against physical reality. [H-8]</td><td style='text-align: center;'>[UCA-DR-4] DR does not provide a new version of topography data to MBS when the infrastructure is changed (i.e. construction work) [H-8.1]</td><td style='text-align: center;'>[UCA-DR-5] DR does provide a new version of topography data to MBS too late when changes to the infrastructure have already been made. [H-8.1]</td><td style='text-align: center;'>[UCA-DR-6] DR does not resend new topography data to MBS if the previous transmission failed. [H-8] (e.g. not checking that the data reception was confirmed)</td></tr></table>

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


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Controllers</td><td style='text-align: center;'>• PE• MBS</td></tr><tr><td style='text-align: center;'>Control Actions:</td><td style='text-align: center;'>PE -&gt; MBS• Connection    ○ Domain Data Version Check    ○ Synchronization Complete    ○ Close Connection• Command Change DPS state• Request Movement Authority• Revoke Movement Authority• Heartbeat</td></tr><tr><td style='text-align: center;'>Feedbacks:</td><td style='text-align: center;'>MBS -&gt; PE• Connection    ○ Domain Data Version Check    ○ Synchronize Operational State    ○ Close Connection• Share operational state    ○ Report TACS State    ○ Report Train Object State• Reject command/request• Accept command/request    ○ Allow/grant command/request    ○ Deny command/request</td></tr><tr><td style='text-align: center;'>Process Model</td><td style='text-align: center;'>• PE    ○ Operational State    ○ Safety Logic (needs to be aware what SL will do/grant)    ○ Operationally synchronized timetable• MBS    ○ Operational State    ○ Safety Logic</td></tr></table>

---

## FP2R2DATO


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Control Algorithm</td><td style='text-align: center;'>• MBS
    ○ Check command/request validity
    ○ Check command/request safety
    ○ Incident/Emergency Routines
    ○ Supervise heartbeat
• PE
    ○ Sequence Movement Authorities according to plan
    ○ Command changed DPS state according to plan
    ○ Request Movement Authority according to plan
    ○ High-level Incident/Emergency Routines/Optimization
    ○ Provide heartbeat</td></tr><tr><td style='text-align: center;'>Remarks</td><td style='text-align: center;'>Since PE performs only functions with SIL basic integrity, all commands from PE have to be checked by MBS an associated risk to safety in order to be suitable for SIL 4 functions.</td></tr></table>

---

## 6 INTERFACE CRITICALITY

This chapter details the results of the safety analysis of the MBS safety boundary analysis and the related interfaces. The aim of this analysis is to identify safety related connections and systems relating to the MBS. The MBD shall support different modes of operation. This chapter analysis these modes for the impact to the MBS.

### 6.1 SYSTEM SAFETY BOUNDARY

The system boundary is given through the “system definition” from task 13.1 and was further analyzed from the safety perspective. The following figure classifies the sub systems of the MBD into safety related and non safety related controllers.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//11e6d5b7-4226-465e-8470-05032b5f307a/markdown_0/imgs/img_in_image_box_81_556_1122_1386.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A49%3A26Z%2F-1%2F%2Fcc462a8d8d4eca9070a8f3851996f24017d75c46ae4b6160df50d67cdaf01319" alt="Image" width="87%" /></div>


<div style="text-align: center;">Figure 8 - MBS System Boundary and Interface Definition</div>

---

### 6.2 INTERFACE TABLES

From the MBS module perspective, the following interfaces are analysed according to their safety relevance to determine which of the interfaces are safety related. The interfaces are further analysed about the kind of communication (unidirectional or bidirectional). This classification shall help to reduce the development effort for such kind of interfaces which are connecting the MBS to non-safety related systems.

Legend of the following table:

Interface Name ___ the name of the interface

Interface Description ... a short description of the interface

Connection ... defines both connection entities of the interface

Communication ... classifies the connection into unidirectional or bidirectional

Safety related ... a classification, whether the interface is safety related (Yes) or not (No)

Remarks ... a comment field for additional optional comments or remarks

6.2.1 I AS


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td style='text-align: center;'>I_AS</td></tr><tr><td style='text-align: center;'>Interface description</td><td style='text-align: center;'>This interface represents the connection between the MBS and the neighbouring systems (MBS/RBC). The communication is done according to the specification of the ERTMS/ETCS SUBSET-037 and ERTMS/ETCS SUBSET-039.</td></tr><tr><td style='text-align: center;'>Connection</td><td style='text-align: center;'>Moving Block System (MBS) &lt;-&gt; Neighbouring (MBS/RBC) System Adjacent System</td></tr><tr><td style='text-align: center;'>Safety related</td><td style='text-align: center;'>Yes</td></tr><tr><td style='text-align: center;'>Remarks</td><td style='text-align: center;'>MBS &lt;-&gt; MBS/RBC handover not in scope of this analysis.</td></tr></table>

<div style="text-align: center;">Table 27 – I AS Interface Definition</div>

---

#### 6.2.2 I\_DR


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_DR</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the DR and the MBS. DR provides updates of existing and new data to the MBS by using a standardised data format.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Digital Register (DR) &lt;-&gt; Moving Block System (MBS)</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">Overall system safety depends on data veracity but not e.g., on interface availability.</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity (MBS needs information to be unmodified)</td><td style='text-align: center;'>Integrity could be verified by using a data/bulk checksum.</td><td style='text-align: center;'>Technical/Operational considerations required</td></tr><tr><td style='text-align: center;'>Correctness of data (MBS needs information to represent the correct state)</td><td style='text-align: center;'>Ensured through dependable external system/actor signature, e.g., if data is pre-validated.</td><td style='text-align: center;'>Technical/Operational considerations required</td></tr><tr><td style='text-align: center;'>Availability of connection (relevant for MBS safety function)</td><td style='text-align: center;'>No safety related implications.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">-</td></tr></table>

<div style="text-align: center;">Table 28 – I\_DR Interface Definition</div>

---

<div style="text-align: center;">6.2.3 I OBU</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_OBU</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the MBS and the ETCS on-board unit (OBU). The communication is done according to the specification of the ERTMS/ETCS SUBSET-026 and ERTMS/ETCS SUBSET-037.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Moving Block System (MBS) &lt;-&gt; ECTS on-board (OBU)</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">Yes</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity (MBS needs information to be unmodified)</td><td style='text-align: center;'>Integrity already ensured through SS-026/SS037.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Correctness of data (MBS needs information to represent the correct state)</td><td style='text-align: center;'>Correctness already ensured through SS-026/SS037.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Availability of connection (relevant for MBS safety function)</td><td style='text-align: center;'>Monitoring of continuous connection already ensured through SS-026/SS-037.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">-</td></tr></table>

<div style="text-align: center;">Table 29 – I_OBU Interface Definition</div>

---

#### 6.2.4 I OP


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_OP</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the MBS and the operator position with the intend to exchange operation relevant information for SIL-2 functions (e.g.: railway point lock).</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Moving Block System (MBS) &lt;-&gt; Operator Position</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">Yes</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity (MBS needs information to be unmodified)</td><td style='text-align: center;'>Integrity shall be verified by using a protocol checksum.</td><td style='text-align: center;'>Technical/Operational considerations required</td></tr><tr><td style='text-align: center;'>Correctness of data (MBS needs information to represent the correct state)</td><td style='text-align: center;'>Correctness shall be verified by using an appropriate protocol e.g., with a signature.</td><td style='text-align: center;'>Technical/Operational considerations required</td></tr><tr><td style='text-align: center;'>Availability of connection (relevant for MBS safety function)</td><td style='text-align: center;'>The operator/role must have the means to interact/influence MBS at any time (e.g., react to safety incident). Appropriate safety reaction may be required if connection is lost.</td><td style='text-align: center;'>Technical/Operational considerations required</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">-</td></tr></table>

<div style="text-align: center;">Table 30 – I_OP Interface Definition</div>

---

<div style="text-align: center;">6.2.5 I_PE</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_PE</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the MBS and the PE. For the data exchange between the MBS and the PE a standardised data format is used.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Moving Block System (MBS) &lt;-&gt; Plan Execution (PE)</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">No</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity (MBS needs information to be unmodified)</td><td style='text-align: center;'>Not required</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Correctness of data (MBS needs information to represent the correct state)</td><td style='text-align: center;'>Not required</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Availability of connection (relevant for MBS safety function)</td><td style='text-align: center;'>Not required</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">As the MBS shall reject requests from PE which can result in an unsafe system state. This interface is not considered safety related, as unsafe requests are simply rejected.</td></tr></table>

<div style="text-align: center;">Table 31 – I_PE Interface Definition</div>

---

<div style="text-align: center;">6.2.6 I TACS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_TACS</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the MBS and the Trackside Assets Control and Supervision (TACS) according to the specification of the EULYNX standards.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Moving Block System (MBS) &lt;-&gt; Trackside Assets Control and Supervision (TACS)</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">Yes</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity (MBS needs information to be unmodified)</td><td style='text-align: center;'>SCI-P / SCI-TDS / SCI-LC / SCI-LX /: Integrity already ensured via RaSTA protocol.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Correctness of data (MBS needs information to represent the correct state)</td><td style='text-align: center;'>SCI-P: Ensured through external SIL4 system. SCI-TDS: We can verify the correctness through a second source</td><td style='text-align: center;'>[minor] operational considerations required</td></tr><tr><td style='text-align: center;'>Availability of connection (relevant for MBS safety function)</td><td style='text-align: center;'>Monitoring of continues connection already ensured via RaSTA heartbeat.</td><td style='text-align: center;'>Already set / Not critical</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">-</td></tr></table>

<div style="text-align: center;">Table 32 – I TACS Interface Definition</div>

---

<div style="text-align: center;">6.2.7 I_PEOP</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_PEOP</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the plan execution (PE) and the operator position with the intent to exchange operation relevant information for none safety related functions.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Plan Execution &lt;-&gt; Operator Panel</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">No</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity</td><td style='text-align: center;'>Integrity shall be verified by using a protocol checksum.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Correctness of data</td><td style='text-align: center;'>No safety related implications.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Availability of connection</td><td style='text-align: center;'>No safety related implications.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">Not further assessed, as it is assumed, that the data input is correct and completely provided and this interface has no direct communication to the MBS system.</td></tr></table>

<div style="text-align: center;">Table 33 – I_PEOP Interface Definition</div>


<div style="text-align: center;">6.2.8 I\_PETMS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Interface Name</td><td colspan="2">I_PETMS</td></tr><tr><td style='text-align: center;'>Interface description</td><td colspan="2">This interface represents the connection between the PE and TMS and has no interface to the MBS.</td></tr><tr><td style='text-align: center;'>Connection</td><td colspan="2">Plan Execution (PE) &lt;-&gt; Traffic Management System (TMS)</td></tr><tr><td style='text-align: center;'>Safety related</td><td colspan="2">No</td></tr><tr><td style='text-align: center;'>Safety implication</td><td style='text-align: center;'>Safety measures</td><td style='text-align: center;'>Comment</td></tr><tr><td style='text-align: center;'>Interface integrity</td><td style='text-align: center;'>Integrity shall be verified by using a protocol checksum.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Correctness of data</td><td style='text-align: center;'>No safety related implications.</td><td style='text-align: center;'>-</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Availability of connection</td><td style='text-align: center;'>No safety related implications.</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Remarks</td><td colspan="2">Not further assessed, as it is assumed, that the data input is correct and completely provided and this interface has no direct communication to the MBS system.</td></tr></table>

<div style="text-align: center;">Table 34 – I_PETMS Interface Definition</div>


## 7 MAPPING OF X2RAIL SAFETY ANALYSIS

This chapter covers the safety analysis results [X2RAIL-5] of the project X2RAIL to ensure that they are adequately considered in this analysis. This is done by analyzing each hazard from the X2RAIL results and by providing a trace to different artefacts of this STPA analysis.

#### 7.1 4.1 TRACK STATUS ERRONEOUSLY CLEARED

This section describes causes which result in a Clear Track Status Area by the L3 Trackside, when there is in fact an obstruction present


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.1.1 Dispatcher interaction in L3 Trackside initialisation</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Track Status Area erroneously cleared during L3 Trackside initialisation by dispatcher leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>At L3 Trackside initialisation, in addition to communicating trains there could be non-communicating trains (e.g. in modes SH, NP, etc.) or other obstructions such as vehicles not equipped with ETCS, work areas, etc. After initialisation (either in planned circumstances or as a consequence of a system fault) the Level 3 Trackside has to ascertain the Train Location of all vehicles and obstructions in the Area. If the L3 Trackside allows for a responsible person to declare Clear Track Status Areas, then it is critical that the area is only determined Clear when it is truly clear to avoid a Movement Authority into an Occupied Track Status Area, that could lead to a collision.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[UCA-OP-1], [SDR-1], [SDR-3].</td></tr></table>

<div style="text-align: center;">Table 35 – 4.1.1 Dispatcher interaction in L3 Trackside initialisation</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.1.2 Using invalid/outdated stored information for L3 Trackside initialisation</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Track Status Area erroneously cleared during L3 Trackside initialisation by system leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;At L3 Trackside initialisation, in addition to communicating trains there could be non-communicating trains (e.g. in modes SH, NP, etc.) or other obstructions such as vehicles not equipped with ETCS, work areas, etc.After initialisation (either in planned circumstances or as a consequence of a system fault) the Level 3 Trackside has to ascertain the Train Location of all vehicles in the Area.If the L3 Trackside utilises stored information to clear Track Status Areas, then it is critical that this information is correct to avoid a Movement Authority into an occupied area, that would lead to a collision.The information may no longer be correct and erroneously consider the track clear when it is still occupied.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>Depends on specific implementation (utilizing previously stored data after initialization) and this is out of scope at this state of analysis.</td></tr></table>

<div style="text-align: center;">Table 36 – 4.1.2 Using invalid/outdated stored information for L3 Trackside initialisation</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.1.3 Deactivating Temporary Shunting Area</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Track Status Area erroneously cleared after deactivation of a Temporary Shunting Area leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>The L3 Trackside considers the track status in an Active Shunting Area as Unknown Track Status Area, except for the Train Location of communicating trains. When deactivating a Shunting Area, responsible staff may have the possibility to clear any remaining Unknown Track Status Area. Doing this, an occupied area of track could be set to clear, leading to collision.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[out of scope]</td></tr></table>

<div style="text-align: center;">Table 37 – 4.1.3 Deactivating Temporary Shunting Area</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.1.4 Driver confirms train integrity</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Track Status Area erroneously cleared by driver confirming Train Integrity leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>In case a train driver confirms Train Integrity after a part of the train has been lost, the lost part will be not detected (unless there is TTD), which could lead to collision with other trains approaching the area where the lost part is. This situation could occur when operating trains without TIMS or for a train with a failed TIMS.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[H-1][SC-2.7][SC-6.1][ASM-3][ASM-6][ASM-8][SDR-12]The analysis considers in the unsafe control actions of the I_OBU interface different scenarios about unknown train position.</td></tr></table>

<div style="text-align: center;">Table 38 – 4.1.4 Driver confirms train integrity</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.1.5 Recovery of a failed train</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Track Status Area erroneously cleared by TIMS device not being able to detect loss of train integrity after coupling trains leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;When a train is coupled with another train they should be considered as one train with a common train integrity. However, this depends on if the TIMS devices in the coupled trains are compatible or if the TIMS in the rear part is operational. In case the driver updates the train length to that of the coupled trains without knowing the status of the TIMS device in the rear part, a loss of integrity in the rear part will not be detected and reported by the TIMS in the front part of the train. This could happen in a rescue situation when there is need to pull out a failed train and lead to a collision if the track is cleared based on information which is not valid for the complete train and a part of it is lost without being detected.&quot;</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="6">Trace to R2DATO</td><td style='text-align: center;'>[H-1]</td></tr><tr><td style='text-align: center;'>[SC-2.7]</td></tr><tr><td style='text-align: center;'>[SC-6.1]</td></tr><tr><td style='text-align: center;'>[ASM-3]</td></tr><tr><td style='text-align: center;'>[ASM-6]</td></tr><tr><td style='text-align: center;'>[ASM-8]</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>The analysis considers in the unsafe control actions of the I_OBU interface different scenarios about unknown train position.</td></tr></table>

<div style="text-align: center;">Table 39 – 4.1.5 Recovery of a failed train</div>


#### 7.2 4.2 ERROR IN TRAIN LOCATION

This section describes causes which result in the location of a train as recorded within the L3 Trackside being different from the true location of the train


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.2.1 Confidence interval reduced at End of Mission</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Error in Train Location from reduced confidence interval at End of Mission leads to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;The L3 Trackside needs to determine the area that could be occupied by a train performing End of Mission (EoM) in order to protect it. To that aim, the L3 Trackside is expected to use the location information received from the train. However, as part of the ERA CCM Process an ambiguity in the specifications has been identified which makes it unclear how the ETCS On-board calculates the confidence interval reported at EoM. This is because linking information, including balise location accuracy used in the confidence interval, is deleted when changing to SB mode. If the location accuracy of the LRBG has a larger value than the National Value (Q_NVLOCACC) and the ETCS On-board uses the National Value in the EoM Position Report, this could lead to a collision if the Unknown Track Status Area for protecting the train is unduly shortened, not covering the whole length of the train.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[not applicable - described hazard results from a specific implementation]</td></tr></table>

<div style="text-align: center;">Table 40 – 4.2.1 Confidence interval reduced at End of Mission</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.2.1 Lack of linking information</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Error in Train Location from lack of linking information leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>When relocation is done for a new balise group without linking information (Subset-026, 3.4.4 [BL3 R2]) the ETCS On-board uses the estimated distance travelled between the previous LRBG and the new LRBG. Next figure illustrates the potential issue that arises.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//3993a6d9-566d-46dc-ad5c-13a9e3c66de8/markdown_0/imgs/img_in_image_box_290_544_943_934.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A50%3A12Z%2F-1%2F%2F239f89a23ec55af3307b245726a395d97cdaa89ad0360b423d77eb8926349863" > Figure 1: On-board mSRE relocation in the absence of linking information At time T0 (i.e. the time when the train was last known to be integer), the LRBG was BG_A. At time T1, BG_B is encountered, the ETCS On-board then relocates the Min Safe Rear end at T0 to the new LRBG. If linking information is not available or not used, the ETCS On-board then sends a position report to the L3 Trackside using the estimated distance between BG_A and BG_B when calculating the safe train length. If this estimate is shorter than the real distance between BG_A and BG_B, the L3 Trackside believes that the confirmed rear end is closer to BG_A than it actually is. This means that in case the train has been broken between time T0 and T1, but not yet detected by the TIMS device, there could be a part of the train in the section of track that was just cleared, but the L3 Trackside is not aware of this.</td></tr></table>

<div style="text-align: center;">Table 41 – 4.2.1 Lack of linking information</div>

---

<div style="text-align: center;">7.3 4.3 ERROR IN TRAIN LENGTH</div>


This section describes causes which result in the Train Length of a train as recorded within the L3 Trackside being different than the true length of the train


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.3.1 Reported train length shorter than actual</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Train Length value shorter than the actual length leading to collision, derailment, or exceeding speed limits</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;In case the Train Length given in the Validated Train Data to the L3 Trackside is shorter than the physical train length, this could result in:  ·Another train being authorised beyond the rear of this train located in front, OR  ·Infrastructure released (points moved) under the train, OR  ·Train does not achieve calculated braking curves, OR  ·Train permitted to accelerate earlier after speed restrictions.The error in Train Length could be caused by:  ·Incorrect train length provided by an external system.  ·Incorrect train length entered by the Driver at Start of Mission.  ·Driver does not update the train length after joining.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>R2DATO assumes in the [ASM-8] and [ASM-9] the correct reporting of the correct train length and train integrity.To show why these assumptions are needed, the analysis considers in [S2-UCA-MBS-16] the safety implications of a reported train length shorter than physical reality. This also results in recommendations regarding expected splitting and joining operations ([SDR-11] and [SDR-12])</td></tr></table>

<div style="text-align: center;">Table 42 – 4.3.1 Reported train length shorter than actual</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.3.2 Reported train length longer than actual</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Train Length value longer than the actual length leading to collision or exceeding speed limits</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;In case the Train Length given in the Validated Train Data to the L3 Trackside is longer than the physical train length, this could result in a Track Status Area which is Occupied or Unknown being cleared while still occupied by another vehicle, or that the calculated braking curves are not met by the train. The error in Train Length could be caused by:  ·Incorrect train length provided by an external system.  ·Incorrect train length entered by the Driver at Start of Mission.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>☐ Driver does not update the train length after splitting.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>R2DATO assumes in the [ASM-8] and [ASM-9] the correct reporting of the correct train length and train integrity.To show why these assumptions are needed, the analysis considers in [S1-UCA-MBS-16] the safety implications of a reported train length longer than physical reality. This also results in recommendations regarding expected splitting and joining operations ([SDR-11] and [SDR-12])</td></tr></table>

<div style="text-align: center;">Table 43 – 4.3.2 Reported train length longer than actual</div>


#### 7.4 4.4 CMD ERRONEOUSLY VALIDATES POSITION


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">This section describes the result of a CMD system erroneously validating the location of a train</td></tr><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.4.1 Wrong side failure of CMD</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>CMD erroneously validates a position which is incorrect leading to collision or derailment</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;In case CMD validates the position of a train after being moved in NP mode, the L3 Trackside can give this train a Movement Authority based on the position at End of Mission while the train is now somewhere else. This may lead to derailment or collision.Note that some CMD equipment may allow for a short movement of a train whilst still reporting “no cold movement detected”.Potential mitigations:The following considerations could be taken as mitigation measures:• Hazardous failure rate for CMD to be considered.• Use linking reaction for the first expected Balise Group in the linking chain when authorising trains to move, which will brake the train if it is not found as expected.• Use TTD where trains start after NP mode. However, this is not enough on its own.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[S3-UCA-MBS-16][S4-UCA-MBS-16][mainly concerns the SIL classification of the CMD device]</td></tr></table>

<div style="text-align: center;">Table 44 – 4.4.1 Wrong side failure of CMD</div>

---

<div style="text-align: center;">7.5 4.5 UNDETECTED MOVEMENTS</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">This section describes causes which result in undetected movement of a train</td></tr><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.1 Rollback after standstill</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected backward movement after standstill leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>If a train moves backwards after reaching standstill, it could compromise the authorisation for another train. It can take some time before the L3 Trackside can react on this potentially hazardous situation and try to prevent a collision.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]</td></tr></table>

<div style="text-align: center;">Table 45 – 4.5.1 Rollback after standstill</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.2 Unreported Movement</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Unreported Train movement leading to collision or derailment</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;If a non-communicating train is moved, the movement is not reported to the trackside, and therefore, the L3 Trackside has no knowledge of the movement, and may authorise a conflicting train movement.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]</td></tr></table>

<div style="text-align: center;">Table 46 – 4.5.2 Unreported Movement</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.3 At entrance to Level 3 area</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected movement entering the L3 area leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>In degraded situations, it could occur that a train incorrectly enters the L3 Area when it is not authorised, and it is not detected by the L3 Trackside.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[ASM-4-v2]</td></tr></table>

<div style="text-align: center;">Table 47 – 4.5.3 At entrance to Level 3 area</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.4 After End of Mission</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected movement after End of Mission leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>If a train in SB mode rolls away, Standstill Supervision will result in a brake application once the train moves beyond the distance D_NVROLL. This results in the train being brought to a halt, after which the driver can acknowledge the standstill supervision, releasing the brake. There is no limit on the number of acknowledgements the driver is allowed to make, since this may inhibit Splitting operations. This functionality can enable the driver to use consecutive acknowledgements of the standstill supervision activation to move the train. Figure 3 illustrates the movement that could occur.</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>consecutive roll away movements.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[ASM-4-v2]</td></tr></table>

<div style="text-align: center;">Table 48 – 4.5.4 After End of Mission</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.5 Loss of Train Integrity</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected movement of a part of the train after loss of integrity leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>In case train integrity has been lost and part of the train rolls backwards due to the gradient profile, this may result in a collision with other vehicles. In case of derailment, collisions can also occur on adjacent tracks.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[S3-UCA-MBS-16] [S4-UCA-MBS-17] [S5-UCA-MBS-17]</td></tr></table>

<div style="text-align: center;">Table 49 – 4.5.5 Loss of Train Integrity</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.6 Propelling train</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected movement beyond the secured area for a propelling train leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;In case a train is pushing another train in front of it (propelling movement) there is a risk that the front of the propelled train overpasses the area reserved for this movement as the driver in the propelling train cannot see where the front is. This can happen if there is need to rescue a failed train from the rear. The rescue train will then be propelling a piece of rolling stock in front of it that cannot report its position.If the front of this movement overpasses the reserved area, a collision may occur as the L3 Trackside is not aware of the real &quot;&quot;front end&quot;&quot; (belonging to the failed train) and able to react on this situation to protect other movements. As mSFE and Train length doesn&#x27;t match with the real train this could lead to a wrong track status.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[rescue train out of scope]</td></tr></table>

<div style="text-align: center;">Table 50 – 4.5.6 Propelling train</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.5.7 Shunting train</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Undetected movement out of an Active Shunting Area leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>Shunting movements may unintentionally move beyond the border of an Active Shunting Area without the L3 Trackside being aware of this and therefore being unable to protect other movements in the vicinity of the Shunting Area.</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[shunting out of scope]</td></tr></table>

<div style="text-align: center;">Table 51 – 4.5.7 Shunting train</div>


#### 7.6 4.6 TTD ERRONEOUSLY INDICATES TRACK CLEAR


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">This section describes the result of a TTD which erroneously indicates a section of track as Clear Track Status Area</td></tr><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.6.1 Wrong side failure of TTD</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>TTD erroneously indicates a Clear Track Status Area leading to collision or derailment</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;If TTD is used to clear track irrespective of Train Locations, then:  ◦ An Unknown Track Status Area could be cleared without being swept,  ◦ Infrastructure could be released or moved under a train,  ◦ Erroneously updating the CRE of the train in front, and consequently providing an MA to a following train that could result in a collision.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[according to assumption ASM-13 TTD is considered a SIL4 function]</td></tr></table>

<div style="text-align: center;">Table 52 – 4.6.1 Wrong side failure of TTD</div>


#### 7.7 4.7 Points Moved under train

This section describes the result of moving a point after communications failure


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.7.1 Points Moved After Communications failure</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>A point is moved in an Unknown/Occupied/Reserved Track Status Area with a train over it, or when it is about to pass over it, leading to derailment</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;The Dispatcher needs to move a train inside an Unknown, Occupied or Reserved Track Status Area to a new location. Figure 4 illustrates the situation with a train approaching a set of points inside an Unknown Track Status Area.<img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f04b7177-981d-497c-99d9-fbd52aac24a1/markdown_0/imgs/img_in_image_box_293_339_756_465.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A50%3A38Z%2F-1%2F%2Ff92b07a8cf185062c9990980f89101dbaf5fe50274db52b26ac2f0d73f3a149b" > Figure 4: Unknown Track Status Area due a Communication failureThe Dispatcher would need to move points so that the train can be moved to a siding. In the absence of TTD, moving a point could cause a derailment if moved when a train is over or about to pass it.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[ASM-4-v2]</td></tr></table>

<div style="text-align: center;">Table 53 – 4.7.1 Points Moved After Communications failure</div>


#### 7.8 4.8 HAZARDS IDENTIFIED BUT PRESENT ALREADY IN ETCS L2

The hazards in this section were also identified by the work on ETCS Level 3, but after examination, were found to be already present in L2.

In some cases, there are additional mitigations possible in ETCS Level 3, which are given in the proposed mitigations.


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.8.1 Mixed traffic</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Non-ETCS train erroneously enters a route for an ETCS L3 train leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;Drivers that operate both ETCS and non-ETCS fitted trains may mistakenly use a &#x27;proceed for ETCS&#x27; aspect when operating a non-ETCS train due to confusion of ETCS and non-ETCS experience. Such a situation may result in a SPAD (Signal Passed At Danger) and a collision. This could happen at borders to the L3 Area but also inside an area with mixed traffic where L3 is used as an overlay to a conventional system with optical signals. This hazard is the same as in Level 2. It is the same situation as a non-ETCS train erroneously entering a route set for a Level 2 train in a mixed traffic area.&quot;</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[assumption [ASM-3] – there are no non-ETCS trains with regular movements]</td></tr></table>

<div style="text-align: center;">Table 54 – 4.8.1 Mixed traffic</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.8.2 Reversing</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Train moves backwards after loss of train integrity leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;In case a train needs to reverse after a loss of train integrity it may collide with the part of the train that was lost:<img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e2052ef6-1cdd-4ba3-92b7-9a4f8f811bac/markdown_0/imgs/img_in_image_box_276_612_804_749.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T22%3A50%3A41Z%2F-1%2F%2F0bf81630d0398c13e1e740b6fc70e1fead055d501f393e65ee7352f1642a41cc" >Figure 5: Train reversing after loss of integrityFigure 5: Train reversing after loss of integrityThis hazard is the same as in Level 2, and in conventional signalling.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[reversing out of scope]</td></tr></table>

<div style="text-align: center;">Table 55 – 4.8.2 Reversing</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Hazard</td><td style='text-align: center;'>4.8.3 Loss of train integrity</td></tr><tr><td style='text-align: center;'>Hazard headline</td><td style='text-align: center;'>Derailment after loss of train integrity causes obstruction in adjacent tracks leading to collision</td></tr><tr><td style='text-align: center;'>Hazard description</td><td style='text-align: center;'>&quot;After a loss of train integrity, the lost part of the train could derail causing an obstruction in the adjacent track resulting in a collision. This hazard is the same as in Level 2, and in traditional signalling.&quot;</td></tr><tr><td style='text-align: center;'>Trace to R2DATO</td><td style='text-align: center;'>[S3-UCA-MBS-16][S4-UCA-MBS-17][S5-UCA-MBS-17]</td></tr></table>

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