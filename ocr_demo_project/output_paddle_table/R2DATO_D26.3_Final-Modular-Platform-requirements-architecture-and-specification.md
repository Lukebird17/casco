# Rail to Digital automated up to autonomous train operation

# D26.3 – Final Modular Platform requirements, architecture and specification

Due date of deliverable: 31/10/2024

First submission date: 30/09/2024

Final submission date: 25/07/2025

Leader/Responsible of this Deliverable: Maik Fox, Oliver Mayer-Buschmann / DB InfraGO AG

Reviewed: Y


[
  {
    "Document status": "Description"
  },
  {
    "Document status": "First issue for internal Review"
  },
  {
    "Document status": "Second issue for internal Review"
  },
  {
    "Document status": "Issue for TMT Review"
  },
  {
    "Document status": "Resolved review comments from JU"
  },
  {
    "Document status": "Resolved review comments from MCP"
  },
  {
    "Document status": "Resolved final comments from MCP"
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

Duration: 42 months

[
  {
    "Name": "Maik Fox",
    "Company": "DB InfraGO AG",
    "Details of Contribution": "Deliverable Lead, Executive Summary, Chapters 3, 4, 5, 8, 9, Appendix A, Appendix F"
  },
  {
    "Name": "Oliver Mayer-Buschmann",
    "Company": "DB InfraGO AG",
    "Details of Contribution": "Chapter 8"
  },
  {
    "Name": "Patrick Marsch",
    "Company": "DB InfraGO AG",
    "Details of Contribution": "Chapters 5, 8, Appendix D"
  },
  {
    "Name": "Julian Wissmann",
    "Company": "DB InfraGO AG",
    "Details of Contribution": "Chapter 8"
  },
  {
    "Name": "Nikolaus König",
    "Company": "Hitachi Rail GTS",
    "Details of Contribution": "Chapter 6"
  },
  {
    "Name": "Ignacio Alguacil Ventas",
    "Company": "INECO",
    "Details of Contribution": "Chapter 3.12"
  },
  {
    "Name": "Giovanni Venturi",
    "Company": "MER MEC",
    "Details of Contribution": "Chapters 7, Appendix C"
  },
  {
    "Name": "Francesco Inzirillo",
    "Company": "MER MEC",
    "Details of Contribution": "Chapters 1, 2, 7, Appendix C"
  },
  {
    "Name": "Patrick Rozijn",
    "Company": "NS",
    "Details of Contribution": "Chapters 3.8.2, 6 and 8"
  },
  {
    "Name": "Thomas Martin",
    "Company": "SBB",
    "Details of Contribution": "Chapter 3.7.2"
  },
  {
    "Name": "Sonja Steffens",
    "Company": "Siemens Mobility",
    "Details of Contribution": "Chapter 6, Appendix B, Appendix E"
  },
  {
    "Name": "Thomas Bernburg",
    "Company": "Siemens Mobility",
    "Details of Contribution": "Chapter 6"
  },
  {
    "Name": "Note: A glossary for ERJU terms can be found in chapter 3.7.2, a local glossary in Appendix F.",
    "Company": "Note: A glossary for ERJU terms can be found in chapter 3.7.2, a local glossary in Appendix F."
  },
  {
    "Name": "ALPI",
    "Company": "Application-level Platform Independence"
  },
  {
    "Name": "ATO",
    "Company": "Automatic Train Operation"
  },
  {
    "Name": "BTM",
    "Company": "Balise Transmission Module"
  },
  {
    "Name": "COTS",
    "Company": "Commercial Off The Shelf"
  },
  {
    "Name": "CCS",
    "Company": "Command, Control and Signalling"
  },
  {
    "Name": "CPI",
    "Company": "Compatible Platform Implementation"
  },
  {
    "Name": "DDP",
    "Company": "Deliverable Development Plan"
  },
  {
    "Name": "DMI",
    "Company": "Driver Machine Interface"
  },
  {
    "Name": "ERTMS",
    "Company": "European Rail Traffic Management System"
  },
  {
    "Name": "ETCS",
    "Company": "European Train Control System"
  },
  {
    "Name": "FRMCS",
    "Company": "Future Railway Mobile Communication System"
  },
  {
    "Name": "GoA",
    "Company": "Grade of Automation"
  },
  {
    "Name": "HLPI",
    "Company": "Hardware-level Platform Independence"
  },
  {
    "Name": "HW",
    "Company": "Hardware"
  },
  {
    "Name": "ICT",
    "Company": "Information and Communications Technology"
  },
  {
    "Name": "OCORA",
    "Company": "Open CSS On-Board Reference Architecture"
  },
  {
    "Name": "OT",
    "Company": "Operational Technology"
  },
  {
    "Name": "PI API",
    "Company": "Platform-Independent Application Programming Interface"
  },
  {
    "Name": "POSIX",
    "Company": "Portable Operating System Interface"
  },
  {
    "Name": "R2DATO",
    "Company": "Rail to digital automated up to autonomous train operation"
  },
  {
    "Name": "RBC",
    "Company": "Radio Block Centre"
  },
  {
    "Name": "RCA",
    "Company": "Reference CCS Architecture"
  },
  {
    "Name": "RTE",
    "Company": "Run Time Environment"
  },
  {
    "Name": "SCP",
    "Company": "Safe Computing Platform"
  },
  {
    "Name": "SRACs",
    "Company": "Safety Related Application Conditions"
  },
  {
    "Name": "SW",
    "Company": "Software"
  },
  {
    "Name": "TCMS",
    "Company": "Train Control Management System"
  },
  {
    "Name": "§",
    "Company": "Title",
    "Details of Contribution": "Description"
  },
  {
    "Name": "1",
    "Company": "Introduction",
    "Details of Contribution": "Provide an overview of the entire document."
  },
  {
    "Name": "2",
    "Company": "Development Methodology",
    "Details of Contribution": "Describe the activities performed for obtaining this document."
  },
  {
    "Name": "3",
    "Company": "Modular Platforms Concept (MPC)",
    "Details of Contribution": "Reports all the concepts that were discussed and agreed during the activities of WP26."
  },
  {
    "Name": "4",
    "Company": "Modular Platforms Requirements",
    "Details of Contribution": "Explains the sources and methodology of high-level requirements collection."
  },
  {
    "Name": "5",
    "Company": "Modular Platforms Architecture",
    "Details of Contribution": "Describes the architecture used as a basis for this document."
  },
  {
    "Name": "6",
    "Company": "Hardware-Level Platform Independence (HLPI)",
    "Details of Contribution": "This chapter describes the approach followed for obtaining a set of hardware platform independence principles, functions and their interfaces."
  },
  {
    "Name": "7",
    "Company": "Application-Level Platform Independence (ALPI)",
    "Details of Contribution": "This chapter describes the approach followed for obtaining a set of application platform independence principles, functions and their interfaces."
  },
  {
    "Name": "8",
    "Company": "Management, Diagnostics and Security related Interfaces",
    "Details of Contribution": "Explains the details of internal interfaces inside of the modular platform."
  },
  {
    "Name": "9",
    "Company": "Conclusions",
    "Details of Contribution": "In this chapter are summarised the achievements of the task 26.2 results and reported in the deliverable D26.3, as well as next steps."
  },
  {
    "Company": "References",
    "Details of Contribution": "Provides relevant references used throughout the document."
  },
  {
    "Name": "A",
    "Company": "MPC Requirements",
    "Details of Contribution": "Reports high-level requirements of the MPC."
  },
  {
    "Name": "B",
    "Company": "HLPI Requirements",
    "Details of Contribution": "Reports requirements of the HLPI."
  },
  {
    "Name": "C",
    "Company": "ALPI Requirements",
    "Details of Contribution": "Reports requirements of the ALPI."
  },
  {
    "Name": "D",
    "Company": "Management, Diagnostics and Security related Interface Requirements",
    "Details of Contribution": "Reports requirements of Management, Diagnostics and Security related interfaces."
  },
  {
    "Name": "E",
    "Company": "Collected Open Points for the MPC",
    "Details of Contribution": "Reports all open points collected for future work in the context of the Modular Platform Concept."
  },
  {
    "Name": "F",
    "Company": "MPC Glossary",
    "Details of Contribution": "Reports terms introduced in this document."
  },
  {
    "Name": "Term",
    "Company": "Abbreviation",
    "Details of Contribution": "Definition"
  },
  {
    "Name": "Application Execution Environment",
    "Company": "AAE",
    "Details of Contribution": "The Application Execution Environment refers to the combination of Runtime Environment and Safety Environment. Update Note: The SE is optional if it&#x27;s only a BIL application."
  },
  {
    "Name": "Application Layer",
    "Company": "AL",
    "Details of Contribution": "The Application Layer contains Functional Applications that constitute Functional Systems."
  },
  {
    "Name": "Basic Integrity Platform Independence Interface",
    "Company": "I4",
    "Details of Contribution": "The Basic Integrity Platform Independence Interface I4 (Interface 4) is used to perform a non-safety related platform independence with the applications. In other words, this API is an interface limited to non-safety functionalities between runtime environment and applications."
  },
  {
    "Name": "Compartment",
    "Company": "CP",
    "Details of Contribution": "A Compartment is a consistent, integrated entity comprising exactly one Runtime Environment Instance, Safety Environment Task Replicas of at most one Safety Environment, and Functional Application Task Replicas of its respective Functional Applications. It can be deployed on either a Physical or a Virtual Computing Element."
  },
  {
    "Name": "Compartment Execution Environment",
    "Company": "CEE",
    "Details of Contribution": "The Compartment Execution Environment refers to the combination of Physical Computing Element and Virtualization Environment."
  },
  {
    "Name": "Computing Element",
    "Company": "CE",
    "Details of Contribution": "The Computing Element provides physical or virtual compute resources."
  }
]

---

[
  {
    "Term": "External Diagnostic, Logging, Orchestration, and IT Security Interface(s)",
    "Abbreviation": "I1",
    "Definition": "The External Diagnostic, Configuration &amp; Orchestration, and IT Security Interface I1 (Interface 1) comprises communication-based interfaces between rail systems and central infrastructure components (Shared Services) such as diagnostics, IT-security services, and remote update."
  },
  {
    "Term": "Functional Application",
    "Abbreviation": "FA",
    "Definition": "A Functional Application is a comprehensive set of self-contained software functions, assumed to be provided as one product by a single vendor. Depending on its role in the overall function provided by the Functional System, it has a specific SIL (BIL up to SIL4) assigned (in-line with total FS SIL definition). Update Note: The technical definition of FA should not make assumptions on the sourcing (e.g., being a product of a vendor)."
  },
  {
    "Term": "Functional Application Task",
    "Abbreviation": "FAT",
    "Definition": "A Functional Application Task implements part of the functionality provided by a Functional Application. Depending on its role in the overall function provided by the Functional Application, it has a specific SIL assigned (in-line with total FA SIL definition). It may run replicated in multiple Compartments as FA Task Replicas."
  },
  {
    "Term": "Functional System",
    "Abbreviation": "FS",
    "Definition": "A Functional System is a comprehensive set of self-contained Compartments, assumed to be provided as one product by a single vendor. Depending on its overall function, it has a specific SIL assigned. Update Note: The technical definition of FA should not make assumptions on the sourcing (e.g., being a product of a vendor)."
  },
  {
    "Term": "FS Deployment Rules",
    "Abbreviation": "FSDR",
    "Definition": "The FS Deployment Rules comprises all necessary information for deploying the respective Functional System onto specific approved Compartment Execution Environment(s). These deployment rules are compiled as part of the FS integration process and are part of each integrated, tested and certified/approved Functional System along with its FS Compartments and all necessary approval documentation."
  },
  {
    "Term": "Hardware Abstraction Interface",
    "Abbreviation": "I2",
    "Definition": "The Hardware Abstraction Interface I2 (Interface 2) provides an abstraction of all technology layers above from the specific hardware used below, enabling easy replace ability of commercial of-the-shelf hardware procurable from a well-sized market of hardware vendors. Note: This is not really an interface, but rather a compatibility list of allowed hardware incl. CPU, memory, etc."
  },
  {
    "Term": "Hardware Layer",
    "Abbreviation": "HL",
    "Definition": "The Hardware Layer contains the actual Physical Computing Elements providing the compute resources to the platform."
  },
  {
    "Term": "Instance",
    "Abbreviation": "INS",
    "Definition": "An Instance is a specific realization of any entity. Update Note: “instantiation” could be used instead of “realization”."
  }
]

---

[
  {
    "Term": "Operational Interfaces",
    "Abbreviation": "IO",
    "Definition": "The IO is the sum of all operational interfaces used from Functional Systems (as e.g. an RBC) to communicate with other Functional Systems (as e.g. an IXL). Examples for these set of interfaces are the Eulynx Interfaces (SCI-xx) or interfaces like EuroRadio or TSI-standardized interfaces."
  },
  {
    "Term": "Orchestration Interface",
    "Abbreviation": "OI",
    "Definition": "This interface is used to manage (monitor, control, diagnose, configure) the virtual computing environments. It only exists if a Virtualisation Interface is present. OI is part of I1. Update Note: The Orchestration Interface as described here is not part of I1 in the way that MPC and Shared Services are using the term."
  },
  {
    "Term": "Physical Computing Element",
    "Abbreviation": "PCE",
    "Definition": "The Physical Computing Element refers to the physical device providing compute resources."
  },
  {
    "Term": "Replica",
    "Abbreviation": "REP",
    "Definition": "A Replica is a specific realization of any entity in a cluster of peers used for composite fail safety and/or availability. Replicas of the same entity always run in distinct Compartments deployed to distinct Computing Elements. Update Note: “instantiation” could be used instead of “realization”."
  },
  {
    "Term": "Runtime Environment",
    "Abbreviation": "RTE",
    "Definition": "The Runtime Environment refers to the software needed to provide the services of the Runtime Layer in a single Compartment."
  },
  {
    "Term": "Runtime Layer",
    "Abbreviation": "RL",
    "Definition": "The Runtime Layer refers to the system services (e.g., application and computing resource orchestration, monitoring of the Functional Applications and the Application Execution Environment, tracing and logging, communication services that are not related to safety, security means incl. authentication, encryption, key storage, etc.) and the communication stack for information exchange between Functional Applications running on the same Computing Environment and with external entities. It may also include an operating system."
  },
  {
    "Term": "Safety Environment",
    "Abbreviation": "SE",
    "Definition": "The Safety Environment refers to all Safety Environment Tasks needed for a Functional System."
  },
  {
    "Term": "Safety Environment Task",
    "Abbreviation": "SET",
    "Definition": "A Safety Environment Task implements part of the functionality provided by a Safety Environment. Depending on its role in the overall function provided, it has a specific SIL assigned (in-line with total SE SIL definition). It may run replicated in multiple Compartments as SE Task Replicas."
  },
  {
    "Term": "Safety Layer",
    "Abbreviation": "SL",
    "Definition": "The Safety Layer implements all the technical safety principles related to fulfilling the requirements of EN 50126, EN 50716, EN 50129, EN 50159 (e.g., composite fail safety, fault tolerance, voting mechanisms, redundancy mechanisms for availability, safety communication layers etc.) that are needed to enable the execution of Functional Applications up to SIL4."
  }
]

---

[
  {
    "Term": "Safety Platform Independence Interface",
    "Abbreviation": "I5",
    "Definition": "The aim of introducing Safety Platform Independence Interface I5 (Interface 5), is to be able to implement platform independent Safe Functional Applications (up to SIL4) i.e., applications, based on a generalized abstraction between the application logic and the system interfaces, will run unchanged on different platform implementations."
  },
  {
    "Term": "Virtual Computing Element",
    "Abbreviation": "VCE",
    "Definition": "The Virtual Computing Element refers to virtually provided compute resources with computing resource guarantees."
  },
  {
    "Term": "Virtualisation Environment",
    "Abbreviation": "VE",
    "Definition": "The Virtualisation Environment contains all software needed to provide (multiple) Virtual Computing Elements on a single Physical Computing Element."
  },
  {
    "Term": "Virtualisation Interface",
    "Abbreviation": "I3",
    "Definition": "The Virtualization Interface I3 (Interface 3) is used to provide a standardized interface above the virtualisation layer so that applications or higher platform layers are independent of a specific implementation of the computing hardware."
  },
  {
    "Term": "Virtualisation Layer",
    "Abbreviation": "VL",
    "Definition": "The Virtualisation Layer contains mechanisms that can provide Virtual Computing Elements needed to run multiple Compartments on a single physical hardware underneath. Update Note: FSDR for Compartment allocation to physical hardware have to be taken into account."
  },
  {
    "Term": "Virtual Machine Management",
    "Abbreviation": "VMM",
    "Definition": "Virtual Machine Management refers to the software and processes used to create, monitor, and manage virtual machines."
  }
]

[
  {
    "Project": "RCA/OCORA",
    "Discussion": "The RCA/OCORA initiative is a comprehensive source for the on-board computing platform requirements. In particular the document OCORA TWS03-020-&quot;Computing Platform Requirements&quot; v. 4.1 [6], part of the OCORA Release 4 (and later), notably all the &quot;approved&quot; requirements MSC-XX, with XX from 01 to 127 (including the optional ones), are suitable for the purpose of MPC."
  },
  {
    "Project": "EULYNX",
    "Discussion": "While EULYNX is looking at several aspects of distributed computing systems, its goal is not to define modular computing platforms. As such, EULYNX is only a source for indirect stakeholder requirements."
  },
  {
    "Project": "SIL 4 Data Center &amp; SIL 4 Cloud Reports",
    "Discussion": "The &quot;SIL4 Data Center&quot; report [4] and the &quot;SIL 4 Cloud&quot; [3] list several requirements in textual form."
  },
  {
    "Project": "ERJU SP CE domain",
    "Discussion": "The already discussed second deliverable of the ERJU SP CE domain (OAS, see chapter 3.7.3) provides several requirements based on the operational scenarios discussed."
  },
  {
    "Project": "MPC domain",
    "Discussion": "SP CE Interfaces"
  },
  {
    "Project": "Interfaces external to the platform",
    "Discussion": "• I1: External Diagnostics, Configuration &amp; Control Interface"
  },
  {
    "Project": "Hardware-Level Application Independence (HLPI)",
    "Discussion": "• I2: Hardware Abstraction Interface• I3: Virtualisation Interface"
  },
  {
    "Project": "Application-Level Platform Independence (ALPI)",
    "Discussion": "• I4: Basic Integrity Platform Independence Interface• I5: Safe Platform Independence Interface"
  },
  {
    "Project": "Term",
    "Discussion": "Definition in EN 50129:2018"
  },
  {
    "Project": "Fault",
    "Discussion": "Abnormal condition that could lead to an error in a system"
  },
  {
    "Project": "Term",
    "Discussion": "Definition in EN 50129:2018"
  },
  {
    "Project": "Error",
    "Discussion": "Discrepancy between a computed, observed or measured value or condition and the true, specified or theoretically correct value or condition"
  },
  {
    "Project": "Failure",
    "Discussion": "Loss of ability to perform as required"
  },
  {
    "Project": "Affected entity",
    "Discussion": "Actions"
  },
  {
    "Project": "Task replica",
    "Discussion": "• Restart the Task replica, recover its state and re-integrate it with its counterpart replicas.\n• Inform interested Tasks about the affected Task replica failure."
  },
  {
    "Project": "Computing Element",
    "Discussion": "• Restart the virtual/physical Computing Element and recover or restart all affected Runtime Environment instances and Task replicas, recover their state and re-integrate them with their counterpart replicas.\n• Inform interested Tasks about the affected Task replicas failure."
  },
  {
    "Project": "Entity",
    "Discussion": "Description"
  },
  {
    "Project": "CEME - Compartment Execution and Management Environment",
    "Discussion": "The Compartment Execution and Management Environment comprises the hardware and virtualisation environment along with related (proprietary)\n• Virtual Machine Management functions, and\n• Hardware and Virtualisation related Diagnostics Functions."
  }
]

---

[
  {
    "Description": "As shown in Figure 49, the CEME is expected to be 100% Commercial-of-the-shelf (COTS), except for the Native Hardware Access (NHA) function that may potentially not be COTS and that is required by the Safety Environments to support Functional Systems with a SIL level."
  },
  {
    "Entity": "Functional System(s)",
    "Description": "Functional System(s) are defined in chapters 3.7.2 and 5. In the context of the interfaces covered in this chapter, it is important to note that the Functional Systems(s) are expected to contain:  • FS Diagnostics Server: Entity running in a dedicated Compartment and/or together with a Functional Application in an FS Compartment, which provides diagnostics information to the Platform Management and to Shared Services  • FS Update Client: Entity running in a dedicated Compartment or together with a Functional Application in an FS Compartment, which responds to and executes update requests from the Platform Management or Shared Services"
  },
  {
    "Entity": "Shared Services",
    "Description": "Shared Services are standardized services related to IT security (e.g., authentication, certificate management), global time provisioning, diagnostics and configuration management / update that are located outside the platform."
  },
  {
    "Entity": "Platform Management",
    "Description": "This entity supervises the operation of the Functional Systems running on the Virtual Computing Elements in one (or multiple) location(s), e.g. data centre(s). It obtains diagnostics information from the FS Diagnostics Server within the Functional Systems and from the Hardware and Virtualisation related Diagnostics Functions within the CEME. It forwards the information, as appropriate, to the Shared Services via I1-DIAG and reacts by triggering appropriate actions, e.g., the creation of new Virtual Computing Elements inside the Virtualisation Environment or restarting Physical Computing Elements if needed.  Note: The Platform Management is not safety-relevant (but ensures the fulfilment of RAM requirements during operation), as the Functional Systems themselves (and the Safety Environments therein) always ensure a safe state and safe output. It is assumed that the Platform Management provides a highly standardized functionality in the way that it reacts to information arriving via CEME-DIAG and/or MGMT-DIAG by triggering actions via ORCH and/or FS-UPDATE in a standardized way, potentially involving FS-specific policies.  The Platform Management implements the MPC specific interfaces and abovementioned functionality, potentially utilising as much as feasible COTS solutions, e.g., OpenStack or other solutions."
  }
]

[
  {
    "Interface": "In D 26.1 [18]",
    "Description": "In SP CE domain [14]"
  },
  {
    "Interface": "CEME-DIAG (Compartment Execution and Management Environment related Diagnostics)",
    "Description": "Via this interface, diagnostics functions within the CEME provide diagnostics information related to the Hardware and Virtualization Environment to the Platform Management (such as the information that there is a HW failure, a VCE failure, etc.). The Platform Management reacts to this e.g., by triggering the (re-)creation of Virtual Computing Elements via ORCH and/or updates of Functional System Compartments via FS-UPDATE. It is assumed that this interface is specified by the chosen COTS CEME including Virtual Machine Management related functionality.",
    "Mapping to terminology": "IF-DIAGNOSTICS"
  },
  {
    "Interface": "ORCH",
    "Description": "Via this interface, the Platform Management triggers the Virtual Machine Management within the CEME to setup new Virtual Computing Elements etc. This interface is also used to setup FS Compartments to the extent that they form the endpoint of the FS-UPDATE interface. It is assumed that this interface is specified by the chosen COTS CEME solution, including Virtual Machine Management related functionality.",
    "Mapping to terminology": "IF-ORCHESTRATION"
  },
  {
    "Interface": "MGMT-DIAG",
    "Description": "Via this interface, the FS Diagnostics Server(s) in the Functional System(s) provide(s) diagnostics information strictly needed for the management of the FS Compartments and V(C)Es (such as information on failures of FS Compartments, etc.) to the Platform Management. The Platform Management reacts to this by triggering the (re-)creation of Virtual Computing Elements via ORCH and/or updates of Functional Systems (Compartments) via FS-UPDATE.",
    "Mapping to terminology": "IF-DIAGNOSTICS"
  },
  {
    "Interface": "Interface",
    "Description": "Description",
    "Mapping to terminology": "Mapping to terminology"
  },
  {
    "Interface": "Interface",
    "Description": "Description",
    "Mapping to terminology": "In SP CE domain [14]"
  },
  {
    "Interface": "FS-UPDATE",
    "Description": "Via this interface, the Platform Management supervises updates of the Functional Systems (Compartments).",
    "Mapping to terminology": "IF-ORCHESTRATION"
  },
  {
    "Interface": "I1-DIAG",
    "Description": "Via this interface, the FS Diagnostics Server in the Functional System(s) provides additional diagnostics information (beyond that strictly needed for the management of the FS Compartments and V(C)Es) towards Shared Services. Also, the interface can be used by the Platform Management to provide diagnostics information to Shared Services. Note: It is assumed that this interface is specified in the TCCS domain.",
    "Mapping to terminology": "IF-LOGGING"
  },
  {
    "Interface": "I1-UPDATE",
    "Description": "Via this interface, Shared Services trigger the update of Functional Systems (Compartments) toward the Platform Management and/or directly to the FS Update Client(s) within the Functional Systems (see Section 8.2 for further discussion on this). Note: It is assumed that this interface is specified in the TCCS domain.",
    "Mapping to terminology": "IF-ORCHESTRATION"
  },
  {
    "Interface": "I1-SEC",
    "Description": "Via this interface, the Virtualization Environment, the Platform Management, and the Functional System(s) access security and synchronization services provided by the Shared Services (see chapter 3.7.4). Note: It is assumed that this interface is specified in the TCCS domain.",
    "Mapping to terminology": "IF-IT-SEC"
  },
  {
    "Interface": "Column",
    "Description": "Meaning"
  },
  {
    "Interface": "Source",
    "Description": "O: OCORA Modular Platform Requirements [6]S: SP CE Domain OAS [15] (released to Mirror Group on 2024-05-07)+: new#: (heavily) modified or rewritten"
  },
  {
    "Interface": "Scope",
    "Description": "F: full (all target environments)OB: On-board required, trackside optionalTS: Trackside required, on-board optionalO: optional for all environmentsX: not in scope for work package 26"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R001",
    "Description": "O# MSCP-21",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R001",
    "Description": "O# MSCP-21",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R002",
    "Description": "O# MSCP-20",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R003",
    "Description": "O# MSCP-17",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R004",
    "Description": "O# MSCP-23",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R004",
    "Description": "O# MSCP-23",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R005",
    "Description": "OMSCP-18",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R005",
    "Description": "OMSCP-18",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R006",
    "Description": "OMSCP-29",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R007",
    "Description": "O# MSCP-89",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R008",
    "Description": "O# MSCP-28",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R009",
    "Description": "O# MSCP-30",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R010",
    "Description": "O MSCP-109",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R011",
    "Description": "O MSCP-36",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R012",
    "Description": "O# MSCP-38",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R013",
    "Description": "O# MSCP-33",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R014",
    "Description": "O MSCP-91",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R015",
    "Description": "OMSCP-37",
    "Mapping to terminology": "O"
  },
  {
    "Interface": "R016",
    "Description": "O# MSCP-94 &amp; 92",
    "Mapping to terminology": "TS"
  },
  {
    "Interface": "R017",
    "Description": "OMSCP-93",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R018",
    "Description": "OMSCP-41",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R019",
    "Description": "O# MSCP-39",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R020",
    "Description": "O# MSCP-97",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R021",
    "Description": "O# MSCP-96",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R022",
    "Description": "O# MSCP-40",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R023",
    "Description": "O MSCP-35",
    "Mapping to terminology": "O"
  },
  {
    "Interface": "R024",
    "Description": "O MSCP-108",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R025",
    "Description": "O MSCP-118",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R026",
    "Description": "OMSCP-119",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R027",
    "Description": "OMSCP-106",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R028",
    "Description": "O# MSCP-44",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R029",
    "Description": "OMSCP-49",
    "Mapping to terminology": "X"
  },
  {
    "Interface": "R030",
    "Description": "OMSCP-51",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R031",
    "Description": "OMSCP-55 &amp; 53",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R032",
    "Description": "OMSCP-60",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R033",
    "Description": "O#MSCP-59",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R034",
    "Description": "OMSCP-84",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R035",
    "Description": "OMSCP-67 &amp; 66",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R035",
    "Description": "OMSCP-67 &amp; 66",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R036",
    "Description": "OMSCP-68 &amp; 63",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R036",
    "Description": "OMSCP-68 &amp; 63",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R036",
    "Description": "OMSCP-68 &amp; 63",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R037",
    "Description": "OMSCP-69 &amp; 64",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R037",
    "Description": "OMSCP-69 &amp; 64",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R037",
    "Description": "OMSCP-69 &amp; 64",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R038",
    "Description": "O#MSCP-112",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R038",
    "Description": "O#MSCP-112",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R039",
    "Description": "O#MSCP-113",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R039",
    "Description": "O#MSCP-113",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R040",
    "Description": "O# MSCP-121",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R041",
    "Description": "O# MSCP-114",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R042",
    "Description": "O# MSCP-73",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R043",
    "Description": "O MSCP-54",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R044",
    "Description": "O MSCP-98",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R045",
    "Description": "O MSCP-102",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R046",
    "Description": "OMSCP-105",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R046",
    "Description": "OMSCP-105",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R047",
    "Description": "O# MSCP-76",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R047",
    "Description": "O# MSCP-76",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R048",
    "Description": "O# MSCP-116",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R048",
    "Description": "O# MSCP-116",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R049",
    "Description": "O# MSCP-115",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R049",
    "Description": "O# MSCP-115",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R050",
    "Description": "O# MSCP-123",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R050",
    "Description": "O# MSCP-123",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R051",
    "Description": "O# MSCP-101",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R051",
    "Description": "O# MSCP-101",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R052",
    "Description": "O# MSCP-81",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R052",
    "Description": "O# MSCP-81",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R053",
    "Description": "O MSCP-80",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R053",
    "Description": "O MSCP-80",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R053",
    "Description": "O MSCP-80",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R054",
    "Description": "O# MSCP-117",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R054",
    "Description": "O# MSCP-117",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R054",
    "Description": "O# MSCP-117",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R055",
    "Description": "O MSCP-111",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R055",
    "Description": "O MSCP-111",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Mapping to terminology": "Remark: Diagnostic information could for instance comprise the health status of the platform or a Functional System component."
  },
  {
    "Interface": "R056",
    "Description": "OMSCP-124",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R057",
    "Description": "O# MSCP-86 &amp; 87",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R058",
    "Description": "S SPT2CE-1520",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R059",
    "Description": "S# SPT2CE-1524",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R060",
    "Description": "S SPT2CE-1533",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R061",
    "Description": "S SPT2CE-1529",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R062",
    "Description": "S SPT2CE-1528",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R063",
    "Description": "S SPT2CE-1534",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R064",
    "Description": "S# SPT2CE-1546",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R065",
    "Description": "S# SPT2CE-1549",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R066",
    "Description": "S SPT2CE-1550",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R067",
    "Description": "S SPT2CE-1531",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R068",
    "Description": "S SPT2CE-1553",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R069",
    "Description": "S SPT2CE-1530",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R070",
    "Description": "S SPT2CE-1540",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R071",
    "Description": "S SPT2CE-1542",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R072",
    "Description": "S SPT2CE-1541",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R073",
    "Description": "S# SPT2CE-1537",
    "Mapping to terminology": "X"
  },
  {
    "Interface": "R074",
    "Description": "S SPT2CE-1536",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R075",
    "Description": "S SPT2CE-1545",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R076",
    "Description": "S SPT2CE-1544",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R077",
    "Description": "S SPT2CE-1543",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R078",
    "Description": "S SPT2CE-1535",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R079",
    "Description": "S SPT2CE-1551",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R080",
    "Description": "S# SPT2CE-1552",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Scope"
  },
  {
    "Interface": "R081",
    "Description": "SPT2CE-1547",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R082",
    "Description": "SPT2CE-1554",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R083",
    "Description": "SPT2CE-1548",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R084",
    "Description": "+",
    "Mapping to terminology": "F"
  },
  {
    "Interface": "R084",
    "Description": "+",
    "Mapping to terminology": "Satisfies: MPC-P02"
  },
  {
    "Interface": "Column",
    "Description": "Meaning"
  },
  {
    "Interface": "Source",
    "Description": "S: SP CE Domain OAS [15] (released to Mirror Group on 2024-05-07) +: new #: (heavily) modified or rewritten"
  },
  {
    "Interface": "Allocation",
    "Description": "FS: Functional SystemsVE: Virtualization environmentSE: Safety EnvironmentSS Diag: Shared Services for DiagnosisMPM: Modular Platform ManagementNetwork Diagnosis"
  },
  {
    "Interface": "Scope",
    "Description": "F: full (all target environments)OB: On-board required, trackside optionalTS: Trackside required, on-board optionalO: optional for all environmentsX: not in scope for work package 26"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-1",
    "Description": "+6.2.46.7.1",
    "Mapping to terminology": "Each solution of a Safety Environment shall define the own safety concept in a way which allows the usage of a non-safe VE.The SE itself must identify if the safety related parts of the FS are not running in the required time range or performance.Each miss-behaviour of the VE as e.g. wrong scheduling of the individual FS software parts may not have any impact onto the safety of the FS.The SE can&#x27;t rely on the behaviour of the VE, means the SE must identify each misbehaviour of VE and react safe.Information about misbehaviour of the VE must be provided as diagnosis by FS.Rationale: For aggregation of several FS compartments on a common non-safe VE its essential that the VE shall not have any dependency to safety."
  },
  {
    "Interface": "REQ-HLPI-2",
    "Description": "+6.3",
    "Mapping to terminology": "The VE shall provide the mapping of CPU cores exclusively to VCE.Rationale: For aggregation of several FS compartments on common VE on the same hardware its essential that the VE provides a stable runtime behaviour of each FS compartment by exclusive core usage."
  },
  {
    "Interface": "REQ-HLPI-3",
    "Description": "+6.3",
    "Mapping to terminology": "The CPU performance provided by the mapped CPU resources must be guaranteed for every timepoint during the runtime of an FS Compartment.Rationale: Variations or instabilities in the provided CPU performance will be identified by the SE and will directly lead to reduced availability as consequence of reactions by the SE.Example: If an individual application replica does not react in the required time then this will be evaluated as a misbehaviour of the application replica and this leads to reduced availability (as e.g. running mode reduced from 2oo3 to 2oo2)."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-4",
    "Description": "+6.3",
    "Mapping to terminology": "The installation of additional FS Compartments (of other FS) in additional VCEs on the same Virtualization Environment Instance must not have any impact on the guaranteed CPU performance (cores) for running FS Compartments. Rationale: The stability of the CPU resources is essential for independent handling of individual FS running aggregated in parallel on same VE."
  },
  {
    "Interface": "REQ-HLPI-5",
    "Description": "+6.4.1",
    "Mapping to terminology": "The individual VCE configurations of FS compartments shall be modular and independent. Each FS Compartment shall have its own configuration for the VCE. Adding or deleting of FS compartments onto the VE instance must not have any impact on the VCE configuration of the other FS compartments. Rationale: The independency of VCE configuration is essential for independent handling of individual FS running aggregated in parallel on same VE."
  },
  {
    "Interface": "REQ-HLPI-6",
    "Description": "+6.4.2",
    "Mapping to terminology": "The virtualization environment shall provide defined and stable user interfaces for the configuration of the usage by FS compartments. A new version of the VE may not have any impact onto the VE Configuration of the FS compartment. Each change in the user interface for the VE configuration shall be compatible in such a way that existing VE config (of already running system) can be used furthermore. Rationale: The independency of VCE configuration is essential for independent handling of individual FS running aggregated in parallel on same VE."
  },
  {
    "Interface": "REQ-HLPI-7",
    "Description": "+6.6",
    "Mapping to terminology": "Safety concept of each SE solution must be basically independent from the processor instruction set to be able to change the CPU architecture without impact to the safety concept. Rationale: For future proofness in context of usage of COTS hardware it&#x27;s essential to be able to change the processor instruction set without impact onto the basic safety concept."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-8",
    "Description": "+6.6",
    "Mapping to terminology": "The VE shall support “incompatibilities in detail” in context of hardware spare handling. The usage of a hardware spare part may not have any impact onto the FS compartments. Rationale: Ordering of the same hardware does not guarantee that the exact same hardware is delivered with 100% compatibility to the software. HW internal changes of details are possible."
  },
  {
    "Interface": "REQ-HLPI-9",
    "Description": "+6.6",
    "Mapping to terminology": "The VE shall support the usage of different variants of hardware - provided by different vendors - at in parallel at the same time. Needed adaptions within the VE for usage of a new hardware variant may not have any impact on the VE instances with already running FS compartments. Rationale: It’s essential for efficient handling of COTS hardware to avoid the impact on already running FS compartments."
  },
  {
    "Interface": "REQ-HLPI-10",
    "Description": "+6.7.1.x",
    "Mapping to terminology": "The virtualization environment shall provide a “native running hardware access” (NHA) functionality to provide needed information from the physical hardware in a reliable way to the SE. A first set of identified information is: - Unique identification of the physical hardware device - Core pinning - steady clock input source from the physical hardware - CPU and/or other temperature of the physical hardware - Voltage information Rationale: The details regarding the needed data depend on the SE solution. The “native running mode” of NHA is essential to achieve the needed reliability of the data required by SE solutions. Reliability in such a way that argumentation “data can’t be influenced systematically” can be done for up to SIL4."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-11",
    "Description": "+6.7.1.x",
    "Mapping to terminology": "The SE itself must ensure that the FS compartments are deployed in correct way running on different physical computing elements. In case of a false deployment (FS compartments running on the same physical computing element) the SE must identify the failure and react in a safe way. Rationale: Usage of non-safe SW as VE and for orchestration is not reliable. By this the SE must check the correct distribution on different physical computing elements."
  },
  {
    "Interface": "REQ-HLPI-12",
    "Description": "+6.7.2",
    "Mapping to terminology": "The SE shall realize safety mechanism to ensure the consistency of the safety related SW parts of an up to SIL4 FS. Rationale: by usage of non-safe SW for VE, operating system and orchestration software it&#x27;s not guaranteed that stopping, deleting and starting of safety related software is successful."
  },
  {
    "Interface": "REQ-HLPI-13",
    "Description": "+6.8",
    "Mapping to terminology": "3rd party supplier of VE has to consider IEC 62443 to provide certification as needed. Rationale: Fulfilment IEC 62443."
  },
  {
    "Interface": "REQ-HLPI-14",
    "Description": "+6.9.1",
    "Mapping to terminology": "The VE shall guarantee a perfect stable behaviour in context of runtime and reaction time of the SW parts within FS compartments. Rationale: Variations or instabilities in the provided CPU performance will be identified by the SE and will directly lead to reduced availability as consequence of reactions by the SE. Example: If an individual application replica does not react in the required time then this will be evaluated as a misbehaviour of the application replica and this leads to reduced availability (as e.g. running mode reduced from 2oo3 to 2oo2)."
  },
  {
    "Interface": "REQ-HLPI-15",
    "Description": "+6.9.2",
    "Mapping to terminology": "The SE shall support to repair a failed FS compartment during the operational phase of the FS, synchronization of the repaired FS compartment with the running FS compartments shall be done automatically by the SE to achieve full redundancy again. Rationale: Highest FS availability in context of SW maintenance: avoid stopping of the FS due to repair of an individual failure."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-16",
    "Description": "+6.9.3",
    "Mapping to terminology": "The VE shall support the mapping of VCEs to virtualized ethernet adapters and the alignment of virtualized Ethernet adapters to physical Ethernet cards of the PCE. Rationale: Flexible usage of Ethernet communication without dependency to FS internal configurations."
  },
  {
    "Interface": "REQ-HLPI-17",
    "Description": "+6.4.26.13.1",
    "Mapping to terminology": "The VE shall provide for new VE versions backwards compatibility of the VE configuration interface for FS configuration. Rationale: It must be avoided that a SW update of the VE leads to impact on the VCE Configs of the FS Compartments running above."
  },
  {
    "Interface": "REQ-HLPI-18",
    "Description": "+6.9.4",
    "Mapping to terminology": "The FS shall allow to update basic integrity SW parts as e.g. the IT security mechanism individually FS compartment-wise “one after the other” during operational phase of the FS. Rationale: Highest FS availability in context of SW maintenance: avoid stopping of the FS due to installation of an IT-security patch."
  },
  {
    "Interface": "REQ-HLPI-19",
    "Description": "+6.9.4",
    "Mapping to terminology": "The VE shall allow to update the VE software hardware-wise “one after the other” during operational phase of the FS running above. Rationale: Highest FS availability in context of SW maintenance: avoid stopping of the FS due to installation of an IT-security patch."
  },
  {
    "Interface": "REQ-HLPI-20",
    "Description": "+6.9.4",
    "Mapping to terminology": "The Platform Management must handle the dependency to update “one-after-the-other” during runtime of the FS. Rationale: Highest FS availability in context of SW maintenance: avoid stopping of the FS due to installation of an IT-security patch."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-21",
    "Description": "+6.11",
    "Mapping to terminology": "The Platform Management shall collect the diagnosis data of the VE and 3rd party SW (as e.g. for COTS hardware diagnosis) and provide this data via interface I1 to the Shared Services Diagnosis. Rationale: Standard solutions for VE / COTS diagnosis will not consider the interface I1 Diagnosis. By this a “protocol-conversion” is necessary to provide the diagnosis data in the required format."
  },
  {
    "Interface": "REQ-HLPI-22",
    "Description": "+6.11",
    "Mapping to terminology": "The Platform Management shall process a root cause analysis for the FS state and initiate necessary maintenance activities automatically. Rationale: It must be avoided that a SW update of the VE leads to impact on the VCE Configs of the FS Compartments running above."
  },
  {
    "Interface": "REQ-HLPI-23",
    "Description": "+6.11.2",
    "Mapping to terminology": "The FS shall provide diagnosis data about the own health state via the interface I1 FS Diagnosis to the Shared Services for diagnosis. Rationale: Shared Services for diagnosis are data sink for all kind of diagnosis data."
  },
  {
    "Interface": "REQ-HLPI-24",
    "Description": "+6.11.2",
    "Mapping to terminology": "The FS shall provide diagnosis data about the own health state via the interface I1 FS Diagnosis to the Platform Management. Rationale: Platform Management is the data sink for diagnosis data which is relevant for the handling of FS compartments running in VCEs on VPEs."
  },
  {
    "Interface": "REQ-HLPI-25",
    "Description": "+6.11.2",
    "Mapping to terminology": "The Platform Management must handle the relationship “one FS consists of several individual FS compartments which provide own diagnosis data”. Diagnosis data of the individual compartments must be aggregated to an overall state of the FS and this state must be provided via the interface I1 Diagnosis to the Shared Services Diagnosis. Rationale: Shared Services for diagnosis shall get a defined FS state (independent from details about the solution that the FS is running in several compartments)."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-HLPI-26",
    "Description": "+6.11.3",
    "Mapping to terminology": "The VE shall provide diagnosis date about the VE itself and about the underlying physical hardware to the PM. The data must be provided by the VE management tool to the Platform Management. Rationale: Platform Management is data sink for all diagnosis data relevant for the handling of the FS compartments within VCEs running on PCEs."
  },
  {
    "Interface": "REQ-HLPI-27",
    "Description": "+6.11.3",
    "Mapping to terminology": "The Platform Management must forward the diagnosis data about the VE and VCEs to the Shared Services for diagnosis. For this the interface I1 Diagnosis must be considered. Rationale: Shared Services for diagnosis are data sink for all kind of diagnosis data."
  },
  {
    "Interface": "REQ-HLPI-28",
    "Description": "+6.11.4",
    "Mapping to terminology": "Information about the health state of the virtual computing elements and physical computing elements shall be provided by the VE or even additional dedicated diagnosis software provided by 3rd party. Rationale: Platform Management is data sink for all diagnosis data relevant for the handling of the FS compartments within VCEs running on PCEs."
  },
  {
    "Interface": "REQ-HLPI-29",
    "Description": "+6.11.4",
    "Mapping to terminology": "A dedicated software for diagnosis of the physical computing elements shall provide diagnosis data to the Platform Management. Rationale: FS running in VCEs is not able to identify details about the detailed states of PCEs, FS only reacts in case of failures within the PCEs. By this a dedicated diagnosis software for the PCEs is necessary."
  },
  {
    "Interface": "REQ-HLPI-30",
    "Description": "+6.11.4",
    "Mapping to terminology": "The Platform Management must forward the diagnosis data about the physical computing elements to the Shared Services for diagnosis. For this the interface I1 Diagnosis must be considered. Rationale: Shared Services for diagnosis are data sink for all kind of diagnosis data."
  },
  {
    "Interface": "REQ-HLPI-31",
    "Description": "+6.11.5",
    "Mapping to terminology": "The Network Diagnosis shall provide the diagnosis data about the network to the Platform Management."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Mapping to terminology": "Rationale: Platform Management is data sink for all diagnosis data relevant for the handling of the FS compartments within VCEs running on PCEs. Network is relevant for the FS internal communication between the FS compartments. By this the network diagnosis is necessary for root cause analysis about FS state."
  },
  {
    "Interface": "REQ-HLPI-32",
    "Description": "+6.11.5",
    "Mapping to terminology": "The Platform Management must handle the relationship between FS compartments and the belonging network communication. Diagnosis data related to the network communication shall be evaluated with be belonging FS compartments in context of root cause analysis. Rationale: Platform Management is data sink for all diagnosis data relevant for the handling of the FS compartments within VCEs running on PCEs. Network is relevant for the FS internal communication between the FS compartments. By this the network diagnosis is necessary for root cause analysis about FS state."
  },
  {
    "Interface": "REQ-HLPI-33",
    "Description": "+6.12.1",
    "Mapping to terminology": "The SE shall support to update the own operating system (with IT-security layer) within the FS compartment compartment-wise “one after the other” to install IT-security patches during runtime of the FS. Rationale: IT-security patching during operational phase of the FS."
  },
  {
    "Interface": "REQ-HLPI-34",
    "Description": "+6.12.1",
    "Mapping to terminology": "The VE shall support to update the VE instances (with IT-security layer) hardware-wise “one after the other” with a new version of the VE instance SW to install IT-security patches during runtime of the FS. After the VE instance update the FS compartments shall be started automatically to achieve full redundancy, e.g., to achieve 2oo3 again. There must not be the dependency to install an update of the VE on all PCEs at same timepoint, because this would lead to stop of all FS compartments. Rationale: IT-security patching during operational phase of the FS."
  },
  {
    "Interface": "REQ-HLPI-35",
    "Description": "+6.12.1",
    "Mapping to terminology": "The VE shall allow to replace a physical computing element by another physical computing element without impact onto the running VE instances. Rationale: Replacing individual PCEs during operational phase of the FS."
  },
  {
    "Interface": "Column",
    "Description": "Meaning"
  },
  {
    "Interface": "Source",
    "Description": "S: SP CE Domain OAS [15] (released to Mirror Group on 2024-05-07)\n+: new\n#: (heavily) modified or rewritten"
  },
  {
    "Interface": "Allocation",
    "Description": "RT: runtime\nCF: configuration\nOP: offline process (data preparation, certification)"
  },
  {
    "Interface": "Scope",
    "Description": "F: full (all target environments)\nOB: On-board required, trackside optional\nTS: Trackside required, on-board optional\nO: optional for all environments\nX: not in scope for work package 26"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-ALPI-01",
    "Description": "7.3.2.1",
    "Mapping to terminology": "The ALPI shall provide an independent interface towards MPC. Rationale: The development of a Functional Application shall be independent from the MPC platform. ALPI&#x27;s interface shall be able to hide different MPC implementations based on different HW and SW. Independence shall be based on a common set of ALPI, based on a shared architecture and a common platform behaviour,"
  },
  {
    "Interface": "REQ-ALPI-01",
    "Description": "7.3.2.1",
    "Mapping to terminology": "Satisfies: MPC-P01, MPC-P02, MPC-A03, R17"
  },
  {
    "Interface": "REQ-ALPI-02",
    "Mapping to terminology": "The ALPI shall provide a standard interface. Rationale: The development of a Functional Application shall be based on a standard RTE interface. The standard interface should allow re-use and easy integration of the Functional Application in the case of different RTE suppliers. ALPI shall provide a standardised language to specify the application&#x27;s deployment-configuration. Satisfies: MPC-P01, MPC-P05, MPC-P07,"
  },
  {
    "Interface": "REQ-ALPI-03",
    "Mapping to terminology": "The ALPI shall provide a flexible interface. Rationale: The ALPI interface shall allow maximum flexibility in the use of all available RTE services and COTS SW, especially in the case of Non-Safety-Related Functional Applications that shall be developed with maximum flexibility to take full advantage of the evolution of ICT and OT technologies. Constraints that limit the use of products with new technologies developed in the COTS environment should be avoided. For Safety-Related Functional Applications ALPI shall provide implicit restrictions, selected via configuration, transparently implemented by runtime services, imposed through adoption of common standard models. Satisfies: MPC-P01, MPC-P05"
  },
  {
    "Interface": "REQ-ALPI-04",
    "Description": "7.1",
    "Mapping to terminology": "The ALPI shall reduce the complexity of Functional Application development. Rationale: The ALPI interface shall allow the development of Functional Application in which the complexity of the mechanisms needed to ensure communication, safety and security are not directly managed by Functional Engineer. ALPI shall minimize the number of services"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Mapping to terminology": "the number of differences in the interface specifications for on-board and trackside environments.Satisfies: MPC-P01, MPC-P03, R028, R039, R040, R041"
  },
  {
    "Interface": "REQ-ALPI-05",
    "Mapping to terminology": "The ALPI shall provide compatibility.Rationale: The ALPI interface shall be developed to assure backward compatibility during the future evolution of the ALPI interface.Satisfies: MPC-P04, MPC-P05, R40"
  },
  {
    "Interface": "REQ-ALPI-06",
    "Mapping to terminology": "The ALPI shall provide transparency.Rationale: The ALPI interface shall provide services that implement mechanisms/protocols/needed to achieve transparency of location, communication, safety, security.Satisfies: MPC-P01, MPC-P03, R004, R048, R049."
  },
  {
    "Interface": "REQ-ALPI-07",
    "Description": "7.3.2.1.1 7.3.2.2",
    "Mapping to terminology": "The ALPI shall provide a common standard development model.Rationale: The development of a Functional Application shall be based on the “Functional Application Task” concept. FAT is the basic component of a Functional Application. ALPI shall provide all services necessary to the creation, configuration, communication, scheduling, aggregation of FAT.Satisfies: MPC-P01, MPC-P03,"
  },
  {
    "Interface": "REQ-ALPI-08",
    "Mapping to terminology": "(removed)"
  },
  {
    "Interface": "REQ-ALPI-09",
    "Mapping to terminology": "The ALPI shall provide a configurable set of services to implement Non-Safe, Basic Safety Integrity and Safety Integrity Level SIL1-SIL4 Functional Application. ALPI shall allow restriction of the set by means of configuration.Rationale: ALPI shall provide a selected set of services depending on SIL of the Functional Application."
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Mapping to terminology": "Satisfies: MPC-P03"
  },
  {
    "Interface": "REQ-ALPI-010",
    "Mapping to terminology": "(removed)"
  },
  {
    "Interface": "REQ-ALPI-011",
    "Mapping to terminology": "The ALPI shall provide a restricted set of services to implement Basic Safe Functional Application. Rationale: Basic Integrity Level Functional Application shall be developed using services compliant with Basic Integrity Level requirements as specified in EN 50xxx. ALPI shall allow restriction of the set by means of configuration. Satisfies: MPC-P03, MPC-G02, R01"
  },
  {
    "Interface": "REQ-ALPI-012",
    "Mapping to terminology": "The ALPI shall provide a restricted set of services to implement SIL1,.. SIL4 Functional Application. Rationale: SIL1,.. SIL4 Functional Application shall be developed using ALPI services compliant with CENELEC standard as specified in EN 50xxx. In case of SIL4 FA, ALPI shall allow the implicit enabling of the transparent mechanisms that implement composite safety. ALPI shall allow restriction of the set of services by means of configuration. Satisfies: MPC-P03, R001, R061"
  },
  {
    "Interface": "REQ-ALPI-013",
    "Description": "7.3.2.1",
    "Mapping to terminology": "The ALPI shall allow the aggregation of Functional Applications with different SIL Rationale: aggregation of mixed SIL Functional Application. Satisfies: MPC-P03, R002, R061"
  },
  {
    "Interface": "REQ-ALPI-014",
    "Description": "7.3.1.3",
    "Mapping to terminology": "The ALPI shall provide runtime Security functions in the scope of the Functional Application Rationale: ALPI shall provide security services related to PKI management, authentication management, cryptographic verification/validation inside FAT. Security related to external communication is managed end-to-end with TLS at network level and it is not in scope of runtime services of ALPI. ALPI shall provide information of the Security level of network communication via configuration. Satisfies: R009, R010"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-ALPI-015",
    "Mapping to terminology": "(removed)"
  },
  {
    "Interface": "REQ-ALPI-016",
    "Description": "7.1",
    "Mapping to terminology": "The ALPI shall provide an offline Configuration data structure aimed to characterize the Functional ApplicationRationale: ALPI shall provide a configuration data structure for the purpose of characterizing ALPI services with respect to functionalities related to communication, safety, security, orchestration, logging of a Functional Application.Satisfies: R028, R036"
  },
  {
    "Interface": "REQ-ALPI-017",
    "Description": "7.3.2.4",
    "Mapping to terminology": "The ALPI shall provide Models for Functional Application life-cycle.Rationale: ALPI shall provide models to standardize life-cycle management; list to consider:• SW Architecture model: Functional Application is one or more processes• Life-Cycle safety assessment model: compliant with CENELEC• Process model: Task (UNIX process, ref. glossary)• Programming Model: Task, deterministic scheduling, RTC for Safety Related Functional Application• Executable generation model: validated compiler, linker, loader• Timing Model: timer-clock, execution deadline of FAT• Execution model: Start/Init, Operate, Stop/shutdown• Communication Model: MOM, standard P2P, publish/subscribe, transparent application of Gateway concept for external communication; use of OPC/UA, SNMP standard protocols• Configuration Model: Application Engineering Configuration data; Application-specific RTE data (for FA integration and runtime execution)• Security Model: compliant with IEC622443, EN50701, IEC 63452• Maintenance Model: provided by RTE; interoperable with external orchestration services IFORCH• Logging Model: provided by RTE SYSLOG services; interoperable with external services IF-DIAG• Error handling: according to CENELEC EN50129:2018• Diagnostics model: Collection of Functional Application analytics for KPIsSatisfies: R009, R010, R011, R019, R020, R021, R022, R023, R024, R028, R033, R047"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-ALPI-018",
    "Mapping to terminology": "The ALPI shall provide an offline Deployment data structure aimed to deploy or update Functional Application"
  },
  {
    "Interface": "REQ-ALPI-018",
    "Mapping to terminology": "Rationale: ALPI shall provide a data structure for the purpose of deploying a Functional Application. The data structure is transparently used for orchestration purposes. The deployment data structure shall be used to check FA configuration and FA executable integrity."
  },
  {
    "Interface": "REQ-ALPI-018",
    "Mapping to terminology": "Satisfies: R035, R036"
  },
  {
    "Interface": "REQ-ALPI-019",
    "Description": "7.3.1.3",
    "Mapping to terminology": "The ALPI shall provide resources/mechanism/services for Application Logging, Monitoring, Diagnostics."
  },
  {
    "Interface": "REQ-ALPI-019",
    "Description": "7.3.1.3",
    "Mapping to terminology": "Rationale: ALPI shall provide a data structure and services for the purpose of exporting Functional Application data to external entities. The data is selected through configuration, and it is transparently used for logging purposes. It shall be also possible direct logging, via SYSLOG (RTE) services"
  },
  {
    "Interface": "REQ-ALPI-019",
    "Description": "7.3.1.3",
    "Mapping to terminology": "Satisfies: R034, R056, R057"
  },
  {
    "Interface": "REQ-ALPI-020",
    "Description": "7.3.2.1",
    "Mapping to terminology": "The ALPI shall provide the SRAC to be fulfilled by a safety related Functional Application."
  },
  {
    "Interface": "REQ-ALPI-020",
    "Description": "7.3.2.3",
    "Mapping to terminology": "Rationale: ALPI shall provide a clear definition of SRAC to be fulfilled by the Functional Application. These SRAC are imposed by lower layer if necessary."
  },
  {
    "Interface": "REQ-ALPI-020",
    "Description": "7.3.2.3",
    "Mapping to terminology": "Satisfies: R008"
  },
  {
    "Interface": "REQ-ALPI-021",
    "Description": "7.3.2.3",
    "Mapping to terminology": "The ALPI shall provide the SRAC to be exported to installation, maintenance phases."
  },
  {
    "Interface": "REQ-ALPI-021",
    "Description": "7.3.2.3",
    "Mapping to terminology": "Rationale: ALPI shall provide a clear definition of SRAC to be exported to installation, maintenance phases."
  },
  {
    "Interface": "REQ-ALPI-021",
    "Description": "7.3.2.3",
    "Mapping to terminology": "Satisfies: R008"
  },
  {
    "Interface": "ID",
    "Description": "Source",
    "Mapping to terminology": "Requirement"
  },
  {
    "Interface": "REQ-ALPI-022",
    "Description": "7.3.1.1",
    "Mapping to terminology": "The ALPI shall provide a SW architecture model where a Functional Application SW is implemented through one or more process. A process is referred to as a &quot;UNIX process&quot; as specified in UNIX RTE environment. Rationale: ALPI shall provide standard SW architecture model for developing Functional Application."
  },
  {
    "Interface": "REQ-ALPI-023",
    "Mapping to terminology": "(removed)"
  },
  {
    "Interface": "REQ-ALPI-024",
    "Description": "7.3.1.1",
    "Mapping to terminology": "The ALPI shall provide services and functionalities compliant with the CENELEC life cycle. The related documentation shall be usable for modular certification. Rationale: ALPI shall provide standard life-cycle model for assessing a Functional Application. Satisfiies: R11"
  },
  {
    "Interface": "REQ-ALPI-025",
    "Description": "7.3.1.1",
    "Mapping to terminology": "The ALPI shall provide a standard POSIX interface. This interface is directly mappable on every POSIX compliant RTE. Rationale: ALPI shall provide a standard interface"
  },
  {
    "Interface": "REQ-ALPI-026",
    "Description": "7.3.1.1",
    "Mapping to terminology": "The ALPI shall provide a UNIX process model to develop Functional Application. ALPI interface should be POSIX. Rationale: ALPI shall provide a process model to develop Functional Application Process"
  },
  {
    "Interface": "REQ-ALPI-027",
    "Description": "7.3.1.1",
    "Mapping to terminology": "The ALPI shall provide a Programming Model in which process are realized with task; tasks are executed using deterministic behaviour. For deterministic, safety related task the RTC (Run To Completion) schema should be used. Rationale: ALPI shall provide a Programming Model to develop deterministic Functional Application Process"
  }
]

---

[
  {
    "ID": "REQ-ALPI-028",
    "Source": "7.4.6.3",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide an Execution Model of Functional Application Tasks. Task Execution shall be • timer-based, i.e., in configured regular intervals, or in the form of one-shot timers. • event-based, i.e., upon receipt of (certain types of messages). • timer- and event-based, i.e., the Task obtains execution time in regular intervals, or in the form of one-shot timers, only if (certain types of) messages have (or have not) been received. The specific execution modes are defined in the ALPI configuration Rationale: ALPI shall provide an Execution Model of a Functional Application Process. Satisfies:",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-029",
    "Source": "7.3.1.2",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide qualified tools (compiler, linker, loader, ...) for executable generations. Rationale: ALPI shall provide qualified tools for executable generations Satisfies:",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-030",
    "Source": "7.3.1.3",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide services for timer-clock, for defining and controlling execution deadline of task. Rationale: ALPI shall provide timing model to be used by Functional Application tasks Satisfies: R19, R020, R022, R025, R031",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-031",
    "Source": "7.3.1.4",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide services to Start/Init, Operate, Stop/shutdown a Functional Application task. Rationale: ALPI shall provide an Execution model to be used by Functional Application Satisfies: R016",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-032",
    "Source": "7.3.1.4",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide standard communication services. These services shall be based on MOM, P2P and publish/subscribe paradigms. ALPI services shall allow the use of OPC/UA, SNMP or other standard protocols (e.g., as defined in Subset 147). It should be possible to apply transparently the Gateway concept for external communication. Rationale: ALPI shall provide a Communication Model to be used by Functional Application Satisfies: R028, R30",
    "Scope": "F"
  }
]

---

[
  {
    "ID": "REQ-ALPI-033",
    "Source": "7.3.2.2",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide two types of configuration data: Application Engineering Configuration data and Application-Specific RTE data. AEC data for configuring application (i.e. IXL DB, data preparation, etc, communications IDs). ASRTE data for Functional Application integration and runtime execution. (i.e. cycle time, communication nodes, SIL of tasks, ...).",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-033",
    "Source": "7.3.2.2",
    "Allocation": "RT, CF",
    "Requirement": "Rationale: ALPI shall provide a Configuration Model to define the behaviour of a Functional Application.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-033",
    "Source": "7.3.2.2",
    "Allocation": "RT, CF",
    "Requirement": "Satisfies: R030",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-034",
    "Source": "7.4.9",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide security services compliant with IEC62443, EN50701, IEC 63452. Security on communication is transparent to ALPI and it is transparently managed end-to-end by lower layers. Specific security services such as cryptographic algorithm are provided by ALPI run time services. Specific requirement related to the use of PKI (Public key infrastructure) are defined via ALPI configuration and properly implemented by lower layers.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-034",
    "Source": "7.4.9",
    "Allocation": "RT, CF",
    "Requirement": "Rationale: ALPI shall provide a Security Model to be used by Functional Application.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-034",
    "Source": "7.4.9",
    "Allocation": "RT, CF",
    "Requirement": "Satisfies: R009",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-035",
    "Source": "7.4.11",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide maintenance services for Functional Application. These are provided by RTE and shall be interoperable with external orchestration services (IF-ORCH).",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-035",
    "Source": "7.4.11",
    "Allocation": "RT, CF",
    "Requirement": "Rationale: ALPI shall provide a Maintenance Model for a Functional Application.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-035",
    "Source": "7.4.11",
    "Allocation": "RT, CF",
    "Requirement": "Satisfies: MPC-P05",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-036",
    "Source": "7.3.1.3",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide Logging services for Functional Application. Run-time Logging will be provided by RTE through Syslog services. Implicit logging of specific application data is achieved through configuration, specifying data and frequency of logging. The logged data shall be interoperable with external services IF-DIAG.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-036",
    "Source": "7.3.1.3",
    "Allocation": "RT, CF",
    "Requirement": "Rationale: ALPI shall provide a Logging Model for a Functional Application.",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-036",
    "Source": "7.3.1.3",
    "Allocation": "RT, CF",
    "Requirement": "Satisfies: R032, R033, R057",
    "Scope": "F"
  }
]

---

[
  {
    "ID": "REQ-ALPI-037",
    "Source": "7.4.6.6",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide error handling services according to CENELEC EN50129:2018. Rationale: ALPI shall provide a standard Error Model for a Functional Application. Satisfies: R024",
    "Scope": "F"
  },
  {
    "ID": "REQ-ALPI-038",
    "Source": "7.3.1.3",
    "Allocation": "RT, CF",
    "Requirement": "The ALPI shall provide Diagnostics services. It will be possible the Collection of Functional Application analytics for KPIs. Rationale: ALPI shall provide a standard Diagnostics Model for a Functional Application. Satisfies: R033",
    "Scope": "F"
  }
]

---

# Contract No. HE – 101102001

## APPENDIX D MANAGEMENT, DIAGNOSTICS AND SECURITY RELATED INTERFACE REQUIREMENTS

This Appendix lists requirements for the interfaces as discussed in chapter 8, Management, Diagnostics and Security related Interfaces.


[
  {
    "Column": "Source",
    "Meaning": "S: SP CE Domain OAS [15] (released to Mirror Group on 2024-05-07) +: new #: (heavily) modified or rewritten"
  },
  {
    "Column": "Allocation",
    "Meaning": "VE: Virtualization environmentSS Diag: Shared Services for DiagnosisMPM: Modular Platform Management"
  },
  {
    "Column": "Scope",
    "Meaning": "F: full (all target environments)OB: On-board required, trackside optionalTS: Trackside required, on-board optionalO: optional for all environmentsX: not in scope for work package 26"
  }
]

---

[
  {
    "ID": "GEN-1",
    "Source": "EuroSpec, TCMS_DS",
    "Allocation (needed?)": "RE",
    "Requirement": "Data transfer shall have no influence on the operation of the overall system. Rationale: Separation and (de-) prioritization of the data transferred on networks, etc. needs to be guaranteed.",
    "Scope": "F"
  },
  {
    "ID": "GEN-2",
    "Source": "EuroSpec, TCMS_DS",
    "Allocation (needed?)": "RE",
    "Requirement": "All interfaces shall support means for authentication and encryption.",
    "Scope": "F"
  },
  {
    "ID": "GEN-3",
    "Source": "S SPT2CE-1421, Step 4",
    "Allocation (needed?)": "RE",
    "Requirement": "All interfaces shall provide means for the connected entities to check whether the interface is up and running.",
    "Scope": "F"
  }
]

EuroSpec [22] provides additional specifications on Software Updates [23] and Maintenance Software [24], which have not yet been considered in this deliverable but might be investigated in further work on the topic.

---

### D.2 REQUIREMENTS ON CEME-DIAG

[
  {
    "ID": "CEME DIAG-1",
    "Source": "+",
    "Allocation": "VE",
    "Requirement": "It shall be possible to configure the Virtual Machine Management w.r.t. which diagnostics information types are provided to the Platform Mgmt.",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-2",
    "Source": "+",
    "Allocation": "VE",
    "Requirement": "Diagnostics information provided by the Virtual Machine Management shall contain time stamps.",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-3",
    "Source": "+",
    "Allocation": "VE",
    "Requirement": "Diagnostics information exchanged shall be based on standardized naming convention for entities (CPUs, etc.).",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-4",
    "Source": "S# SPT2CE-1489 - SW Failure of one complete VE Instance",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of a complete Virtualization Environment instance has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-5",
    "Source": "S# SPT2CE-1489 - SW Failure of one complete VE Instance",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of a complete VE instance has been overcome.",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-6",
    "Source": "S# SPT2CE-1487 - SW Failure of all VE Instances",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all VE instances has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME -DIAG-7",
    "Source": "S# SPT2CE-1487 - SW Failure of all VE Instances",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all VE instances has been overcome.",
    "Scope": "TS"
  }
]

---

[
  {
    "ID": "CEME-DIAG-8",
    "Source": "S# SPT2CE-1496 - Individual HW failure within one physical Computing Element",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when an individual HW failure within one physical Computing Element has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-9",
    "Source": "S# SPT2CE-1496 - Individual HW failure within one physical Computing Element",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when an individual HW failure within one physical Computing Element has been overcome.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-10",
    "Source": "S# SPT2CE-1490 - Total HW failure of one complete physical computing element",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a total HW failure of one complete physical computing element has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-11",
    "Source": "S# SPT2CE-1490 - Total HW failure of one complete physical computing element",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a total HW failure of one complete physical computing element has been overcome.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-12",
    "Source": "S# SPT2CE-1492 - Disaster scenario - failure of all computing elements",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all computing elements has occurred.",
    "Scope": "TS"
  }
]

---

[
  {
    "ID": "CEME-DIAG-13",
    "Source": "S# SPT2CE-1492 - Disaster scenario - failure of all computing elements",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all computing elements has been overcome.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-14",
    "Source": "S# SPT2CE-1501 - Failure of one external communication channel regarding I0",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of one external communication channel regarding I0 has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-15",
    "Source": "S# SPT2CE-1501 - Failure of one external communication channel regarding I0",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of one external communication channel regarding I0 has been overcome.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-16",
    "Source": "S# SPT2CE-1499 - Failure of all external communication channels regarding I0",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all external communication channels regarding I0 has occurred.",
    "Scope": "TS"
  },
  {
    "ID": "CEME-DIAG-17",
    "Source": "S# SPT2CE-1499 - Failure of all external communication channels regarding I0",
    "Allocation": "VE",
    "Requirement": "The Virtual Machine Management shall issue a diagnostics information when a failure of all external communication channels regarding I0 has been overcome.",
    "Scope": "TS"
  }
]

---

## FP2R2DATO

### D.3 REQUIREMENTS ON ORCH

[
  {
    "ID": "ORCH-1",
    "Source": "SPT2CE-1421",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can verify that the deployment of the Virtualization Environment has been performed correctly by the Virtual Machine Management.Note: This requirement goes beyond those strictly derived from SPT2CE-1421.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-2",
    "Source": "SPT2CE-1428",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can verify whether a Virtualisation Environment of the designated Physical Computing Elements complies with the requirements as per the certified FS Deployment Rules of a Functional System to be deployed.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-3",
    "Source": "SPT2CE-1428",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can confirm whether sufficient resources can be allocated on the designated Physical Computing Element(s) in accordance with the FS.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-4",
    "Source": "SPT2CE-1428",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can create Virtual Computing Element(s) according to the FS Deployment Rules of a Functional System to be deployed.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-5",
    "Source": "SPT2CE-1428",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can verify that the correct Virtual Computing Element(s) have been created and that they are ready for FS Compartment deployment.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-6",
    "Source": "SPT2CE-1431 SPT2CE-1448",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can verify the correct mapping of FS Compartment and Virtual Computing Element.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-7",
    "Source": "SPT2CE-1439 SPT2CE-1602",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can request to release Virtual Computing Elements.",
    "Scope": "TS"
  }
]

---

[
  {
    "ID": "ORCH-8",
    "Source": "SPT2CE-1448 SPT2CE-1446 SPT2CE-1602 SPT2CE-1458",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can trigger a backup of the state of a FS compartment.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-9",
    "Source": "SPT2CE-1456 SPT2CE-1458",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can request to uninstall a Functional System Compartment.",
    "Scope": "TS"
  },
  {
    "ID": "ORCH-10",
    "Allocation (needed?)": "VE",
    "Requirement": "ORCH shall offer a function through which the Platform Management can setup the functions needed within a Virtual Computing Element for the subsequent usage of the I1-UPDATE interface to manage Functional System installations, updates, etc.",
    "Scope": "TS"
  }
]

---

### D.4 REQUIREMENTS ON MGMT-DIAG

[
  {
    "ID": "MGMT-DIAG-1",
    "Allocation (needed?)": "MPM",
    "Requirement": "It shall be possible to configure the FS Diagnostics Server w.r.t. which diagnostics information types are provided to the Platform Management.",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-2",
    "Allocation (needed?)": "MPM",
    "Requirement": "Diagnostics information provided by the FS Diagnostics Server shall contain time stamps.",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-3",
    "Allocation (needed?)": "MPM",
    "Requirement": "Diagnostics information exchanged shall be based on standardized naming convention for entities (CPUs, etc.).",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-4",
    "Source": "SPT2CE-1483 - Total SW Failure of one FS Compartment",
    "Allocation (needed?)": "MPM",
    "Requirement": "The FS Diagnostics Server shall issue a diagnostics information when an FS Compartment has failed.",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-5",
    "Source": "SPT2CE-1501 - Failure of one external communication channel regarding I0",
    "Allocation (needed?)": "MPM",
    "Requirement": "The FS Diagnostics Server shall issue a diagnostics information when a failure of one external communication channel regarding I0 has occurred.",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-6",
    "Source": "SPT2CE-1501 - Failure of one external communication channel regarding I0",
    "Allocation (needed?)": "MPM",
    "Requirement": "The FS Diagnostics Server shall issue a diagnostics information when a failure of one external communication channel regarding I0 has been overcome.",
    "Scope": "F"
  }
]

---

[
  {
    "ID": "MGMT-DIAG-7",
    "Source": "SPT2CE-1499 - Failure of all external communication channels regarding I0",
    "Allocation (needed?)": "MPM",
    "Requirement": "The FS Diagnostics Server shall issue a diagnostics information when a failure of all external communication channels regarding I0 has occurred.",
    "Scope": "F"
  },
  {
    "ID": "MGMT-DIAG-8",
    "Source": "SPT2CE-1499 - Failure of all external communication channels regarding I0",
    "Allocation (needed?)": "MPM",
    "Requirement": "The FS Diagnostics Server shall issue a diagnostics information when a failure of all external communication channels regarding I0 has been overcome.",
    "Scope": "F"
  }
]

---

### D.5 REQUIREMENTS ON FS-UPDATE

[
  {
    "ID": "FS-UPDATE-1",
    "Source": "SPT2CE-1431SPT2CE-1448SPT2CE-1446SPT2CE-1602SPT2CE-1456SPT2CE-1458",
    "Allocation": "MPM",
    "Requirement": "FS-UPDATE shall offer a function through which the Platform Management can request to install software / configurations within FS Compartments onto a corresponding Virtual Computing Element as per the FS Deployment Rules of the Functional System to be deployed.",
    "Scope": "F"
  },
  {
    "ID": "FS-UPDATE-2",
    "Source": "SPT2CE-1431SPT2CE-1456SPT2CE-1458",
    "Allocation": "MPM",
    "Requirement": "FS-UPDATE shall offer a function through which the Platform Management can request to start software / configuration within a Functional System Compartment.",
    "Scope": "F"
  },
  {
    "ID": "FS-UPDATE-3",
    "Source": "SPT2CE-1439SPT2CE-1446SPT2CE-1456SPT2CE-1602SPT2CE-1458",
    "Allocation": "MPM",
    "Requirement": "FS-UPDATE shall offer a function through which the Platform Management or potentially Shared Services can request to stop software / configuration within a Functional System Compartment.",
    "Scope": "F"
  },
  {
    "ID": "FS-UPDATE-4",
    "Source": "SPT2CE-1448SPT2CE-1446SPT2CE-1602SPT2CE-1458",
    "Allocation": "MPM",
    "Requirement": "FS-UPDATE shall offer a function through which the Platform Management or potentially Shared Services can test if software / configuration within a Functional System Compartment is up and running.",
    "Scope": "F"
  },
  {
    "ID": "FS-UPDATE-5",
    "Source": "SPT2CE-1456",
    "Allocation": "MPM",
    "Requirement": "FS-UPDATE shall offer a function through which the Platform Management or potentially Shared Services can check the version of a software / configuration within a Functional System Compartment.",
    "Scope": "F"
  }
]

---

## APPENDIX E COLLECTED OPEN POINTS FOR THE MPC

The following lists represents the collected opens for the Modular Platform Concept. They are meant for future work, e.g., in the ERJU SP CE domain, other domain, or future ERJU IP projects.


[
  {
    "ID": "Open-001",
    "Source Chapter": "6.3",
    "Open": "What kind of HW architecture aspects will be “bottle necks” in parallel usage by independent FS compartments running aggregated on same physical computing element?• Memory bandwidth?• Network bandwidth?How can this aspects be handled / defined FS compartment wise?"
  },
  {
    "ID": "Open-002",
    "Source Chapter": "6.5",
    "Open": "Architecture: how to handle the message-based interface of the NHA (see chapter 6.7) to FS Compartments above - is this interface a part of I3?"
  },
  {
    "ID": "Open-003",
    "Source Chapter": "6.6",
    "Open": "The details of the requirements towards the hardware (as e.g. hardware architecture, cores, performance, communication, MTBF, virtualization extension, ...) must be defined."
  },
  {
    "ID": "Open-004",
    "Source Chapter": "6.7.1.1",
    "Open": "What is the criteria for unique CPU identification? MAC address? TPM content?"
  },
  {
    "ID": "Open-005",
    "Source Chapter": "6.7.1.2",
    "Open": "How to solve the relationship of used CPU cores (used by the FS compartment within the VCE) and the information which shall be provided by the native running software as NHA?"
  },
  {
    "ID": "Open-006",
    "Source Chapter": "6.7.1.4",
    "Open": "The details regarding sensor information provided by NHA in context of temperature must be clarified."
  },
  {
    "ID": "Open-007",
    "Source Chapter": "6.7.1.5",
    "Open": "The details regarding sensor information provided by NHA in context of voltage must be clarified."
  },
  {
    "ID": "Open-008",
    "Source Chapter": "6.7.1.6",
    "Open": "It must be clarified, if the required information from the physical hardware can be provided via standardized interface I2 or if the NHA functionality must be adapted for different HW variants."
  },
  {
    "ID": "Open-009",
    "Source Chapter": "6.7.1.6",
    "Open": "The responsibility and technical handling (installation/update) of such a NHA software must be clarified."
  }
]

---

[
  {
    "ID": "Open-010",
    "Source Chapter": "6.7.2",
    "Open": "The safe handling of safety critical software in context of a non-safe VE with standard orchestration tools must be clarified, as e.g. to avoid unallowed installation and starting of FS duplicates"
  },
  {
    "ID": "Open-011",
    "Source Chapter": "5.4",
    "Open": "For the MPC Architecture, a combined modularization architecture proposal showing how the deeper levels of FS (e.g., compartments, RTE, Functional Applications, etc.) interact with the interfaces introduced in the service architecture, as well as with the Platform Management and/or Shared Services."
  },
  {
    "ID": "Open-012",
    "Source Chapter": "6.8",
    "Open": "Overall certification of the secure device needs to be clarified."
  },
  {
    "ID": "Open-013",
    "Source Chapter": "6.8",
    "Open": "The architecture for access to the TPM of the physical hardware must be clarified in context of - Access by several FS compartments provided by different suppliers- functionality secure boot- certification for IE 62443 SL3.Rationale: Access to physical hardware is not guaranteed for the IT-security mechanism running within a VCE."
  },
  {
    "ID": "Open-014",
    "Source Chapter": "6.9.4",
    "Open": "The overall architecture for the update of FS must be clarified.Which dependencies in context of “FS consists of several FS compartments” are handled on side of the Shared Services and on side of the Platform Management?"
  },
  {
    "ID": "Open-015",
    "Source Chapter": "6.9.5",
    "Open": "The safety related overall architecture for georedundant FS with safe handling of split-brain problem is not yet defined."
  },
  {
    "ID": "Open-016",
    "Source Chapter": "6.10",
    "Open": "Scalable handling of CPU resources: How to handle the scalable usage of CPU resources (cores, memory, network cards,) for flexible usage of independent FS compartments running on same PCE."
  },
  {
    "ID": "Open-017",
    "Source Chapter": "6.11",
    "Open": "The architectural details regarding “needed diagnosis data to do a root cause analysis and initiate automated repair activities” has to be clarified.Which data is relevant for Platform Management? Is a standardization of this senseful and possible or not?"
  }
]

---

[
  {
    "ID": "Open-018",
    "Source Chapter": "6.11.5",
    "Open": "Architecture for network diagnosis:·Which architecture element is responsible for network diagnosis?·Which architecture element is responsible to identify the root cause in case of network communication failures as e.g. regarding the FS internal communication between FS compartments?·Does this architecture element provide I1 Diagnosis to the Shared Services?"
  },
  {
    "ID": "Open-019",
    "Source Chapter": "6.11.4",
    "Open": "Architecture for network diagnosis: which architecture element is responsible to identify the root cause in case of network communication failures as e.g. regarding the FS internal communication between FS compartments?Does this architecture element provide I1 Diagnosis to the Shared Services?"
  },
  {
    "ID": "Open-020",
    "Source Chapter": "6.12.1",
    "Open": "Overall architecture in context of installation and update needs to be defined.·How to bring the individual FS Compartments onto the new VE instance on a new HW?·How to update FS Compartment versions?·What are the dependencies between Shared Services for Update and Platform Management?·How to differentiate between update of non-safe parts and safety related parts?·How to handle the NHA software in context of installation and update?"
  },
  {
    "ID": "Open-021",
    "Source Chapter": "6.13",
    "Open": "An automated installation of safety critical FS compartments by a basic integrity Platform Management must be evaluated from view of safety.The FS system keeps running as 2oo2 and ensures a safe synchronization of the newly started FS compartment. But duplication of safety related FS compartments has the potential to lead to the split-brain problem in context of a duplication of more than one FS compartment."
  },
  {
    "ID": "Open-022",
    "Source Chapter": "6.13.1",
    "Open": "What exactly is necessary in context hardening of the VE? What kind of VE functionalities must be deactivated or even removed to ensure that the handling of rail systems running on VE is possible in way as needed (efficient handling and available running FS)?"
  }
]

---

[
  {
    "ID": "Open-023",
    "Source Chapter": "6.13.1",
    "Open": "Is a kind of “generic” testing possible for performance and runtime behaviour of a new VE version to avoid the need for integration of each individual FS compartment version with new VE Version?"
  }
]

Table 11: Collected MPC Opens

---

[
  {
    "Term": "Application-Level Platform Independence",
    "Abbreviation": "ALPI",
    "Context Chapter": "7",
    "Definition": "Application-Level Platform Independence is achieved through the combination of the Runtime Layer and the Safety Layer providing all necessary safety-related and non-safety-related interfaces and resources for fulfilling an application&#x27;s functions. This includes diagnosis, logging, and monitoring. In addition, also the SRACs imposed on the application by the underlying platform must be fulfilled, ideally standardized."
  },
  {
    "Term": "Compartment Execution &amp; Management Environment",
    "Abbreviation": "CEME",
    "Context Chapter": "5",
    "Definition": "The CEME is following the definition of CEE (see chapter 3.7.2) and adds the management for PCE, VE and VCE."
  },
  {
    "Term": "Compatible Platform Implementation",
    "Abbreviation": "CPI",
    "Context Chapter": "3.11",
    "Definition": "An implementation of the Modular Platform Concept (MPC) as presented in this deliverable that is able to run Functional Systems."
  },
  {
    "Term": "Hardware-Level Platform Independence",
    "Abbreviation": "HLPI",
    "Context Chapter": "6",
    "Definition": "Hardware-Level Platform Independence is achieved through the combination of the Hardware Layer and the Virtualisation Layer providing all necessary interfaces to aggregate multiple Functional Systems with potentially different safety integrity levels on the same physical hardware."
  },
  {
    "Term": "Modular Platform Concept",
    "Abbreviation": "MPC",
    "Context Chapter": "3",
    "Definition": "A full concept showing how to develop, deploy and operate railway applications in a modular way on the trackside, data centres or on-board a train."
  },
  {
    "Term": "Native Hardware Access",
    "Abbreviation": "NHA",
    "Context Chapter": "6",
    "Definition": "The NHA enables access to hardware parameters and data from FS Compartments."
  },
  {
    "Term": "Platform Management",
    "Abbreviation": "PM",
    "Context Chapter": "5",
    "Definition": "Platform Management manages CEME and FS Compartments while providing interfaces to the outside."
  },
  {
    "Term": "Shared Services",
    "Abbreviation": "n/a",
    "Context Chapter": "3",
    "Definition": "The Shared Services represent a collection of overarching services (e.g., update and configuration) defined by the System Pillar TCCS domain."
  },
  {
    "Term": "Virtual Machine Management",
    "Abbreviation": "VMM",
    "Context Chapter": "8",
    "Definition": "Virtual Machine Management refers to the software and processes used to create, monitor, and manage virtual machines."
  }
]

<div style="text-align: center;">Table 12: MPC Glossary</div>