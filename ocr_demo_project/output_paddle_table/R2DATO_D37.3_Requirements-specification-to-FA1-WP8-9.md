# Rail to Digital automated up to autonomous train operation

### D37.3 – Requirements specification to FA1 WP8/9

Due date of deliverable: 31/07/2024

Actual submission date: 03/07/2024

Leader/Responsible of this Deliverable: Joelle Aoun, ProRail

Reviewed: Y/N


[
  {
    "Document status": "Description"
  },
  {
    "Document status": "First issue"
  },
  {
    "Document status": "Second issue"
  },
  {
    "Document status": "Third issue"
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
    "Project funded from the European Union&#x27;s Horizon Europe research and innovation programme": "Sensitiv - limited under the conditions of the Grant Agreement"
  }
]

Start date: 01/12/2022

Duration: 42 months

---

# Contract No. HE – 101102001

## ACKNOWLEDGEMENTS

[
  {
    "Name": "Joelle Aoun",
    "Company": "ProRail",
    "Details of Contribution": "Main structure, contributions to main sections, review, revision, quality check"
  },
  {
    "Name": "Alwin Pot",
    "Company": "ProRail",
    "Details of Contribution": "Main structure, general sections, Dutch case study and revision"
  },
  {
    "Name": "Patrick Looij",
    "Company": "NS Reizigers",
    "Details of Contribution": "Performance indicators, description of Dutch case study"
  },
  {
    "Name": "José A. Reyes",
    "Company": "CAF",
    "Details of Contribution": "ERTMS/ETCS Overview"
  },
  {
    "Name": "Miguel Letona Otaño",
    "Company": "ADIF",
    "Details of Contribution": "Spanish case studies"
  },
  {
    "Name": "Alfonso Martín Hernández",
    "Company": "ADIF",
    "Details of Contribution": "Spanish case studies"
  },
  {
    "Name": "Alfonso Martínez Sierra",
    "Company": "ADIF",
    "Details of Contribution": "ETCS HL3 system architecture and functionality"
  },
  {
    "Name": "Daniel Knutsen",
    "Company": "VTI (TRV)",
    "Details of Contribution": "Swedish case studies"
  },
  {
    "Name": "Augustin Arachtingi",
    "Company": "SNCF",
    "Details of Contribution": "French case studies"
  },
  {
    "Name": "ASTP",
    "Company": "Advanced Safe Train Positioning"
  },
  {
    "Name": "ATO",
    "Company": "Automatic Train Operation"
  },
  {
    "Name": "CCS",
    "Company": "Control Command and Signalling system"
  },
  {
    "Name": "DAC",
    "Company": "Digital Automatic Coupling"
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
    "Name": "EVC",
    "Company": "European Vital Computer"
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
    "Name": "GSM-R",
    "Company": "Global System for Mobile Communications for Railways"
  },
  {
    "Name": "HL3",
    "Company": "Hybrid Level 3"
  },
  {
    "Name": "HTD",
    "Company": "Hybrid Train Detection"
  },
  {
    "Name": "ICNG",
    "Company": "Intercity Nieuwe Generatie"
  },
  {
    "Name": "LZB",
    "Company": "Linienzugbeeinflussung (a cab signalling and train protection system used on selected German and Austrian railway lines as well as on the AVE and some commuter rail lines in Spain)."
  },
  {
    "Name": "MA",
    "Company": "Movement Authority"
  },
  {
    "Name": "OTI-I",
    "Company": "On-board Train Integrity Function"
  },
  {
    "Name": "OTI-L",
    "Company": "On-board Train Length Function"
  },
  {
    "Name": "PTD",
    "Company": "Positive Train Detection"
  },
  {
    "Name": "R2DATO",
    "Company": "Rail to Digital automated up to autonomous train operation"
  },
  {
    "Name": "RBC",
    "Company": "Radio Block Centre"
  },
  {
    "Name": "SNG",
    "Company": "Sprinter Nieuwe Generatie"
  },
  {
    "Name": "TCO",
    "Company": "Total Cost of Ownership"
  },
  {
    "Name": "TIM",
    "Company": "Train Integrity Monitor(ing)"
  },
  {
    "Name": "TSI",
    "Company": "Technical Specification for Interoperability"
  },
  {
    "Name": "TTD",
    "Company": "Trackside Train Detection"
  },
  {
    "Name": "VSS",
    "Company": "Virtual Sub-Section"
  },
  {
    "Name": "Performance indicator",
    "Company": "Unit",
    "Details of Contribution": "Explanation"
  },
  {
    "Name": "Headway",
    "Company": "Minutes and seconds",
    "Details of Contribution": "Minimal time between 2 trains with which the second can follow the first on the whole trajectory just without hindrance."
  },
  {
    "Name": "Relative capacity utilisation",
    "Company": "%(capacity utilisation / 60 min)",
    "Details of Contribution": "Timetable compression method according to UIC-406 leaflet, to be performed on one corridor at a time without merging traffic. Trains run the whole trajectory strictly unhindered."
  }
]

The scenarios of the Swedish southern mainline and the Dutch SAAL corridor will be assessed further for the aspect of robustness by letting a train block the other traffic for a set number of minutes. This gives the insight in how quickly the block layout given a particular traffic pattern helps to solve the congestion. The definitions of the performance indicators for scenarios with external delays are explained in Table 2.

---

[
  {
    "Performance indicator": "Recovery time",
    "Unit": "(Hours), minutes and seconds",
    "Explanation": "Time after which there are no trains running behind their schedule as in the unhindered simulation."
  },
  {
    "Performance indicator": "Number of affected trains",
    "Unit": "Trains",
    "Explanation": "Number of trains that have a changed running time due to the hindrance and congestion compared to the unhindered simulation."
  },
  {
    "Performance indicator": "Total delay",
    "Unit": "(Hours), minutes and seconds",
    "Explanation": "The additional running times compared to the unhindered simulation, summed up over the affected trains."
  }
]

### 4.2 SET-UP OF SCENARIOS AND VARIABLES

This section describes how the scenarios have been set-up to achieve the aim of this deliverable. Note that there are several benefits of HTD that will not be the focus of this deliverable. Only research related to capacity and robustness will be the focus of these case studies as stated in Section 4.1. For capacity, the headway between two following trains will be computed or the relative capacity utilisation of a full timetable will be calculated. For robustness calculations, some scenarios will be set up in which a train blocks the corridor for a set time period, where the aim is to study the recovery time, number of affected trains and total delay.

Simulation with stochastic disruptions will not be included in this stage, for several reasons. The input data of real disruptions is not available for future or hypothetical situations analysis, scenarios are harder to reproduce or compare and finally this method requires many runs which makes simulation and analysis more time consuming. Overcoming these issues does not outweigh the benefits, so stochastic analysis is not foreseen in this deliverable. Therefore, all simulations will be deterministic with no delays or fixed delays in the simulation.

In every scenario, we define a reference situation, using the current or future base information about the track and calculating the headway or relative capacity utilisation. After that, and through variations of the physical blocks and incorporating virtual blocks, according to what is proposed in each scenario, improvement in capacity will be sought in these cases where the capacity is the main objective. When the objective is cost reduction and only keeping equal capacity, we look for keeping the current headway but changing the physical blocks into VSSs.

These results are used not only in this work package in tasks T37.3 and T37.5, but also in FP2WP32.

Each case study described in Chapter 5 includes four parts:

- Infrastructure: a description of the part of the railway network used in the case studies, either the current infrastructure for existing lines or the planned infrastructure for a greenfield situation.

- Traffic: a description of the train services on the delimited network and possible alterations that could influence the scenario. The described traffic could be either current traffic (high flows

---

where HTD could help increase robustness), or future traffic flows demands that could only possibly be achieved with HTD.

• Assumptions: this section describes additional assumptions for the simulations, like timetable principles.

- Scenarios: a description of the different infrastructure and traffic scenarios. They always relate to reference scenario and then build up in order to make the results comparable with only one variable changed at a time. The variables are described below.

For our simulation studies of HTD there are three variables of interest: the lengths of the TTD blocks, the lengths of the VSSs and the availability of TIMs on trains. These variables are defined for each scenario and depend on the state and aim of each network.

- Size of the TTD blocks [m]: A benefit with HTD is the possibility to extend the current TTDs without affecting capacity negatively. This means that for some scenarios varying the size of TTD is of interest.

- Size of the VSS [m]: For creating additional capacity with additional blocks it is not necessary anymore to add axle counters or loops, but it can be done with adding VSSs. Therefore the size of VSSs is crucial for the capacity computation.

- Share of trains equipped with TIM [% or based on train type]: The availability of TIM equipped trains in the traffic pattern has impact on the capacity and robustness. This might be a percentage of the trains or defined as one train category to have a TIM and another to not have a TIM.

### 4.3 SIMULATION ENVIRONMENTS

Two simulation environments will be used in EU Rail FP1 WP9 for assessing the case studies of this work package: the tool of CAF for exploratory research based on the headway of two trains for the Spanish case studies and RailSys for the French, Swedish and Dutch case studies that involve a complete timetable and in some cases external delays. Both simulation environments are briefly described in Sections 4.3.1 and 4.3.2.

#### 4.3.1 CAF tool

The simulations for the Spanish cases will be performed in the CAF tool. It is focussed on calculating headways. Therefore the tool needs information about the rolling stock and about the technical and the physical characteristics of the track. The tool is limited to work with two trains at the same time: the predecessor and its follower. According to this information, it offers the headway between them as a solution.

#### 4.3.2 RailSys

The simulation software RailSys is an integrated microscopic planning tool, developed by RMCon. RailSys is widely used in the railway sector by infrastructure managers, railway undertakings consulting firms and research institutes  $ [4] $ . RailSys features native ERTMS/ETCS support and

---

detailed calculations of the ETCS braking curves. Infrastructure and rolling stock are modelled on a microscopic level, which provides sufficiently detailed settings for the modelling of HTD and analytical possibilities for the results.

Infrastructure models are needed for all scenarios which utilise RailSys. In case of current lines, existing models will be used as a basis of the studies. For some scenarios, ERTMS/ETCS will need to be implemented in the models. HTD needs to be designed and applied to all existing models for the relevant scenarios. It is important that relevant settings are correctly used to achieve a credible simulation result. Coordination between partners is necessary for this purpose.

For the evaluation of capacity utilisation, the UIC-406 compression method in RailSys will be used. In RailSys, the interpretation of UIC-406 is based on the compression of sequential timetable train paths within divided sections  $ [4] $ . According to the method, RailSys identifies conflicts in the timetable and moves affected trains exactly unhindered behind the conflicting train. The outcome from the RailSys computation is the capacity utilisation which will be generated from specific case studies as described in Chapter 5.

---

## 5 CASE STUDIES AND SCENARIOS

To fulfill the aims of developing migration and deployment strategies to accelerate the application of ETCS HTD, the several research scenarios have been defined according to the set-up described in the previous chapter. These scenarios are used for evaluating the requirements specification of HTD. The lines have been chosen where the main advantages of HTD can be found, both in terms of reduction of trackside implementation costs and improvement of capacity performance.

The general outline is that the Spanish cases and a Swedish case will be described and analysed based on headways. Thereafter, the French and Swedish cases will be assessed on capacity by relative capacity utilisation. Finally another Swedish case and the Dutch case are described and analysed for relative capacity utilisation and robustness aspects.

Since there are many case studies described in this chapter, Table 3 provides an overview of the locations, market segments, network length, reference signalling system and performance indicators. The explanation follows in the paragraphs of every separate case study.

[
  {
    "Nr": "Headway",
    "Country": "Relative capacity utilisation",
    "Location": "3 PI&#x27;s for external delays"
  },
  {
    "Nr": "5.1",
    "Country": "Spain",
    "Location": "Atocha commuter tunnels",
    "Market segment": "Urban",
    "Network length [km]": "7",
    "Reference signalling system": "L1",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.2",
    "Country": "Spain",
    "Location": "Madrid C-5 cercanías",
    "Market segment": "Sub-urban",
    "Network length [km]": "45",
    "Reference signalling system": "Class B",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.3",
    "Country": "Spain",
    "Location": "Madrid - Torrejón de Velasco",
    "Market segment": "High-speed",
    "Network length [km]": "36",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.4",
    "Country": "Spain",
    "Location": "Barcelona - Figueras",
    "Market segment": "Mainline",
    "Network length [km]": "130",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.5",
    "Country": "Spain",
    "Location": "León - Guardo",
    "Market segment": "Regional",
    "Network length [km]": "26",
    "Reference signalling system": "Class B",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.6",
    "Country": "Spain",
    "Location": "Lérida - Reus",
    "Market segment": "Freight",
    "Network length [km]": "64",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.7",
    "Country": "Spain",
    "Location": "Cercanías Barcelona",
    "Market segment": "Mainline",
    "Network length [km]": "8",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.8",
    "Country": "France",
    "Location": "Lille",
    "Market segment": "Sub-urban",
    "Network length [km]": "30",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.9",
    "Country": "France",
    "Location": "Bretagne pays de Loire (LNOBPL)",
    "Market segment": "Mainline",
    "Network length [km]": "250",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.10",
    "Country": "Sweden",
    "Location": "Stockholm Citybanan",
    "Market segment": "Urban",
    "Network length [km]": "6",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  }
]

---

[
  {
    "Nr": "Headway",
    "Country": "Relative capacity utilisation",
    "Location": "3 PI&#x27;s for external delays"
  },
  {
    "Nr": "5.11",
    "Country": "Sweden",
    "Location": "East link",
    "Market segment": "Mainline / High-speed",
    "Network length [km]": "160",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.12",
    "Country": "Sweden",
    "Location": "Southern mainline (Norrköping - Mjölby)",
    "Market segment": "Mainline",
    "Network length [km]": "79",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  },
  {
    "Nr": "5.13",
    "Country": "Netherlands",
    "Location": "SAAL-corridor: Schiphol - Amsterdam - Almere - Lelystad",
    "Market segment": "Mainline / (Sub)urban",
    "Network length [km]": "120",
    "Reference signalling system": "L2",
    "Performance indicators": "X"
  }
]

---

# Contract No. HE – 101102001

### 5.1 SPAIN: ATOCHA COMMUTER TUNNELS

#### 5.1.1 Infrastructure

This is a double-track ETCS Level 1 section for commuter trains between Chamartín and Atocha stations, with a length of 7.4 km, this section is selected for study as it is a central node where many lines come together, more specifically, almost all of Madrid's commuter lines.

There are two options for this route: through Recoletos tunnel stopping at Recoletos station (Chamartín-Nuevos Ministerios-Recoletos-Atocha) or through Sol tunnel stopping at Sol station (Chamartín-Nuevos Ministerios-Sol-Atocha). Figure 2 displays the schematic of the lines involved.

[
  {
    "Scenario": "Reference",
    "TTD": "Current (ETCS Level 1)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "Passenger trains with and without TIMs"
  },
  {
    "Scenario": "2",
    "TTD": "Reduction of TTD between stations",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "Passenger trains with and without TIMs"
  },
  {
    "Scenario": "3",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  },
  {
    "Scenario": "4",
    "TTD": "Reduction of TTD between stations",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

# Contract No. HE – 101102001

### 5.2 SPAIN: MADRID C-5 CERCANÍAS

#### 5.2.1 Infrastructure

This is a double-track commuter line between Mostoles-El Soto and Humanes with 21 stations in between them, with a length of 45.1 km. The used signalling system is Class B.

This line is selected for study as it is the only one in Spain working with automatic driving, where it is expected to eliminate this LZB and install ERTMS.

Figure 4 represents the scheme of the line where all the 21 stations appear. A fully technical description of this line is available at  $ [7] $ .

## Móstoles-El Soto - Atocha - Fuenlabrada - Humanes

[
  {
    "Scenario": "Reference",
    "TTD": "Current (LZB)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains without TIMs"
  },
  {
    "Scenario": "2",
    "TTD": "Reduction of TTD between stations",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains without TIMs"
  },
  {
    "Scenario": "3",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  },
  {
    "Scenario": "4",
    "TTD": "Reduction of TTD between stations",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

### 5.3 SPAIN: MADRID - TORREJÓN DE VELASCO

#### 5.3.1 Infrastructure

This is an ETCS L2 double-track high-speed line between Madrid and Torrejón de Velasco with a length of 35.85 km, this line goes through 8 different Madrid city stations: Madrid Chamartín, Concha Espina, Serrano, Madrid-Jardín Botánico, Entrevías, Abroñigal, Canal del Manzanares, Cerro de los Ángeles, Parla Norte, and Torrejón de Velasco.

Figure 5 provides the technical drawing of the line where all these stations can be found.

---

[
  {
    "Scenario": "Reference",
    "TTD": "Current (ETCS Level 2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  },
  {
    "Scenario": "2",
    "TTD": "Reduction of TTD between stations",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

# Contract No. HE – 101102001

### 5.4 SPAIN: BARCELONA - FIGUERAS

#### 5.4.1 Infrastructure

This is a double-track high-speed line between Barcelona and Figueras with a length of 130 km. It is equipped with ETCS L2. A full description of this line is available at  $ [8] $ . The stations are the following: Barcelona-Sants, Sant Andreu Comtal, Mollet, Llinars, Riells, Vilobi d'Onyar, Girona, Figueres.

#### 5.4.2 Traffic

The traffic of the line consists of mixed traffic: freight trains every 1.5 hours, regional trains (200-250 km/h) every 2 hours and high-speed trains (250-350 km/h) every 3 hours.

#### 5.4.3 General assumptions

Current trains are equipped with TIMs. For the simulations, passenger trains remain equipped with it and freight trains will not.

#### 5.4.4 Scenarios

The objective to reach by this simulating experiment is to get an increase in capacity. This is a mainline with high-speed and freight traffic between Madrid and Torrejón de Velasco.

Concerning rolling stock, passenger trains will remain all equipped with TIMs as it is more critical because of punctuality and other possible service problems. Freight trains will not be equipped with TIMs because it is deemed less critical than for passenger trains, primarily due to punctuality concerns and their associated impacts.

The TTDs remain as they are now in the reference scenario. However, VSSs are incorporated in order to get an increase in capacity. The VSS lengths will be the ones taken from the methodology for reaching optimal sizes through iterations by simulating this specific scenario taking into account the critical sections and the increase in capacity objective. The proposed scenarios for the Spanish case Barcelona-Figueras are displayed in Table 7.

[
  {
    "Scenario": "Reference",
    "TTD": "Current (ETCS Level 2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "Passenger trains with TIMs and freight trains without TIMs"
  }
]

---

# Contract No. HE – 101102001

### 5.5 SPAIN: LEÓN - GUARDO

#### 5.5.1 Infrastructure

This is a single Class B regional line from Asunción Universidad to with a length of 93,82 km. In this case, a 26 km section from Asunción Universidad to Matallana will be studied, the stations are the following: Asunción Universidad, San Feliz, La Robla and Matallana. There are sidings in some stations in between them where trains can overtake and come across each other.

It is expected to have demonstrators for ATO, ASTP, FRMCS in this line for the next Europe’s Rail call.

Figure 6 shows the technical drawing of the track layout where all the stations through where this line goes.

---

[
  {
    "Scenario": "Reference",
    "TTD": "Current (Class B)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Minimum (1 TTD between stations, 1 TTD in stations)",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "Passenger trains with TIMs"
  }
]

---

# Contract No. HE – 101102001

### 5.6 SPAIN: LÉRIDA-REUS

#### 5.6.1 Infrastructure

This is a single regional line with ETCS L2 from Lérida to Reus covering a length of 64 km. The study covers the following stations: Lleida Pirineus, Puigverd de Lleida, Juneda, Les Borges Blanques, Canal d'Urgell, Vinaixa, Riu Milans, L'Espluga de Francoli, Montblanc, Vilaverd, La Plana-Picamoixons, Base de Alcover, Alcover and Reus.

#### 5.6.2 Traffic

The traffic consists of mainly freight trains and 2 passenger trains per day, therefore it is considered as freight case study. These freight trains could typically be organized in batteries of trains that all the group runs towards the same direction in order to increase capacity.

The maximum speed of the trains is 140 km/h.

#### 5.6.3 General assumptions

All the trains are equipped with TIMs as in the current reference scenario.

#### 5.6.4 Scenarios

The objective set for this line is to improve capacity, for which rolling stock, TTD and VSS conditions are defined.

The TTDs remain as they are now in the reference scenario, however, VSSs are incorporated in order to get an increase in capacity. The VSS lengths will be the ones taken from the methodology for reaching optimal sizes through iterations by simulations. Table 9 displays the proposed scenarios for Lérida-Reus.

[
  {
    "Scenario": "Reference",
    "TTD": "Current (ETCS Level 2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

### 5.7 SPAIN: CERCANÍAS BARCELONA

#### 5.7.1 Infrastructure

For this case, one section of the Barcelona commuter network will be studied taken into account the following: El Prat de Llobregat-Paseo de Gracia (Paseo de Gracia tunnel), Hospitalet-Aragó (Plaza Cataluña tunnel) and Sagrera-Granollers (Montmeló tunnel). The reference signalling system is ETCS L2.

Figure 7 illustrates the track layout for the Hospitalet-Aragó section, a full description of this line and the others is available at  $ [7] $ .

[
  {
    "Scenario": "Reference",
    "TTD": "Current (ETCS Level 2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "Passenger trains with TIMs and freight trains without TIMs"
  },
  {
    "Scenario": "2",
    "TTD": "Current",
    "VSS": "From 25 m to max. TTD length",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

# Contract No. HE – 101102001

### 5.8 FRANCE: LILLE

#### 5.8.1 Infrastructure

This case study consists of a project for the development of the regional lines around Lille. The project is planned to be completed in 2040, and includes both capacity improvements of existing infrastructure and a new double-track line (Hénin-Beaumont – Lille) for high-speed regional trains. The new line is planned to be equipped with ETCS.

#### 5.8.2 Traffic

The traffic of the network includes regional and suburban trains. The aim of the project is to increase traffic on all routes to/from Lille, doubling the frequencies to four trains per hour. The new Hénin-Beaumont – Lille line has a target of 12 trains per hour in each direction. It is planned to have only suburban and regional trains on the new line that will be studied. The time-distance diagram for the Lille case study is shown in Figure 8.

[
  {
    "Scenario": "Reference",
    "TTD": "Current (with ETCS Level 2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "TBD",
    "Rolling Stock": "All trains with TIMs"
  }
]

---

### 5.9 FRANCE: BRETAGNE PAYS DE LOIRE (LNOBPL)

#### 5.9.1 Infrastructure

The LNOBPL is a new proposed high-speed line in France. The aim of the project is to improve the rail connection between Brittany and Pays de la Loire. Several infrastructure improvements are proposed, including a new high-speed line, capacity treatment of critical sections of the existing infrastructure, and implementation of ERTMS/ETCS on the existing lines. Implementing HTD on new lines or on an existing line is seen as an option.

As the new high-speed line will not have a high capacity requirement, the study will focus on the existing line that are planned to be equipped with ETCS. These lines have high capacity requirement as they support mixed traffic (regional, suburban, high-speed and freight trains) The exact relevant lines of the network where the study will be carried out are still to be determined.

#### 5.9.2 Traffic

The aim the project is to improve the frequency of the suburban, inter-regional, and high-speed links to/from Paris by increasing rail capacity and improving journey times, while supporting the development of rail freight. The traffic is mixed with high-speed train, regional trains, suburban trains and freight trains running on the same tracks. The planned timetable for the line Rennes – Brest is shown in Figure 9.

[
  {
    "Scenario": "Reference",
    "TTD": "Current design (with ETCS L2)",
    "VSS": "-",
    "Rolling Stock": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "TBD",
    "Rolling Stock": "Only suburban and regional trains with TIMs"
  },
  {
    "Scenario": "2",
    "TTD": "Current",
    "VSS": "TBD",
    "Rolling Stock": "Suburban, regional and high-speed trains with TIMs"
  }
]

---

### 5.10 SWEDEN: STOCKHOLM CITYBANAN

#### 5.10.1 Infrastructure

A 6 km long commuter line through the city centre of Stockholm. The line is doubletrack with two stations on the line (Stockholm City and Stockholm Odenplan), both with platforms on the main track. No shunting is allowed at Stockholm City or Stockholm Odenplan. The tunnel is deep which means that there are high gradients at the start and end of the line, which affects the braking curves depending on down- or uphill. Gradients could also limit the possibility of VSS deployments, as it should be possible to stop and accelerate at each VSS. The current line uses track circuit for TTD. However, there are plans to change the TTDs to axle counters. The timeline is not confirmed. For the simulation of the line, the length of model should be longer than the 6 km. This is because the traffic on the connected lines will limit the possible capacity on Citybanan. The infrastructure layouts of the Stockholm Citybanan case are shown in Figure 10 and Figure 11.

[
  {
    "Scenario": "Reference",
    "TTD": "Current block lengths with ETCS L2",
    "VSS": "no",
    "Traffic": "Current"
  },
  {
    "Scenario": "1",
    "TTD": "Track circuit (extended block length) / axle counters (minimal number)",
    "VSS": "25-100 m",
    "Traffic": "Current (0 % TIM equipped)"
  },
  {
    "Scenario": "2",
    "TTD": "Track circuit (extended block length) / axle counters (minimal number)",
    "VSS": "25-100 m",
    "Traffic": "Migration step (50% TIM equipped)"
  },
  {
    "Scenario": "3",
    "TTD": "Track circuit (extended block length) / axle counters (minimal number)",
    "VSS": "25-100 m",
    "Traffic": "Full deployment (100 % TIM equipped)"
  }
]

---

# Contract No. HE – 101102001

### 5.11 SWEDEN: EAST LINK

#### 5.11.1 Infrastructure

A greenfield railway project with aim of increasing capacity between Stockholm and Linköping. Connecting to the Western Main Line at the north and to the Southern Main Line in the south. The goal of the project is for the line to become operational in 2035. The planning process is currently ongoing, and the line is planned to be doubletrack with ERTMS/ETCS Level 2. The line will have five new stations (Vagnhärad, Nyköping, Skavsta, Norrköping and Linköping) and is planned to allow train speeds of 250 km/h. The line is part of a future high-speed line in Sweden, connecting Stockholm and Gothenburg/Malmö. Between Norrköping–Linköping, the line will run parallel with the current Southern Main Line (see Figure 13).

[
  {
    "Scenario": "Reference (ETCS L2)",
    "TTD": "Current",
    "VSS": "-",
    "TIMs": "-"
  },
  {
    "Scenario": "1",
    "TTD": "Current",
    "VSS": "TBD",
    "TIMs": "All trains with TIMs"
  }
]

---

### 5.12 SWEDEN: SOUTHERN MAINLINE (NORRKÖPING – MJÖLBY)

#### 5.12.1 Infrastructure

The section Norrköping–Mjölbyst is part of the Southern Mainline between Stockholm and Malmö, one of the most important railway connection in Sweden. The section between Norrköping–Mjölbyst is about 79 km long, double track and electrified. The Southern Mainline infrastructure is illustrated in Figure 14. The allowed speed on the section is between 110–200 km/h. The section consists of seven stations, where two stations (Linghem and Kimstad) have platforms on the main track and no possibility for overtaking.

---

[
  {
    "Trajectory": "Norrköping - Linköping",
    "Long-distance trains": "43",
    "Regional trains": "48",
    "Freight trains": "8"
  }
]

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>Linköping - Mjölby</td><td style='text-align: center;'>21</td><td style='text-align: center;'>48</td><td style='text-align: center;'>10</td></tr></table>

#### 5.12.3 General assumptions

Traffic is assumed to be the same as the current timetable.

#### 5.12.4 Scenarios

Performance indicators of specific interest for the Southern Mainline are headway, the UIC-406 compression method and recovery time. The reason is that capacity and robustness are important aspects of this line, as the capacity utilization is high, and the line is prone to disturbances. The signalling system ETCS L2 is used as benchmark, as there is an ongoing project to implement ERTMS on the line.

The traffic scenarios have been chosen from the assumption that different train types will be upgraded with train integrity in steps, from easy implementation to complex. For this reason, it is assumed that railcars will have working train integrity in a first step, followed by locomotive-hauled passenger, and lastly freight trains. The value for VSS lengths in this case study should be from the assumption of a simple deployment strategy. Meaning, that the VSS lengths have a standardized length. This is mainly because of two reasons: firstly, it simplifies the simulations in this first step of studying the deployment strategies; secondly, studying the effect of a standardized length could be of interest as it would save cost for the HTD deployment project. A standardized VSS length, in this step, should be in the range of 200 – 500 meters. The reason for this is that similar values have been used in earlier studies  $ [12] $ .

The total number of scenarios to be simulated for the Swedish Southern mainline is 16 (four train integrity scenarios per infrastructure scenario). The scenarios for the implementation of virtual blocks and the extension of current blocks are reported in Table 16.

[
  {
    "Scenario": "Reference",
    "TTD": "Current block lengths",
    "VSS": "no"
  },
  {
    "Scenario": "I-1",
    "TTD": "Current block lengths",
    "VSS": "200-500 m"
  },
  {
    "Scenario": "I-2",
    "TTD": "Track circuit (extended block length)/axle counters (minimal number)",
    "VSS": "no"
  },
  {
    "Scenario": "I-3",
    "TTD": "Track circuit (extended block length)/axle counters (minimal number)",
    "VSS": "200-500 m"
  }
]

The suggested scenarios regarding the implementation of train integrity are provided in Table 17.

---

[
  {
    "Scenario": "Reference",
    "Railcar": "No TIM",
    "Locomotive-hauled passenger trains": "No TIM",
    "Freight trains": "No TIM"
  },
  {
    "Scenario": "T-1",
    "Railcar": "TIM",
    "Locomotive-hauled passenger trains": "No TIM",
    "Freight trains": "No TIM"
  },
  {
    "Scenario": "T-2",
    "Railcar": "TIM",
    "Locomotive-hauled passenger trains": "TIM",
    "Freight trains": "No TIM"
  },
  {
    "Scenario": "T-3",
    "Railcar": "TIM",
    "Locomotive-hauled passenger trains": "TIM",
    "Freight trains": "TIM"
  }
]

---

### 5.13 THE NETHERLANDS: SAAL-CORRIDOR (SCHIPHOL AIRPORT, AMSTERDAM, ALMERE, LELYSTAD)

The SAAL-corridor is one of the busiest railway lines in the Netherlands on which a capacity increase is planned by implementing ETCS L2. From Schiphol airport, the line runs to the intercity station of Amsterdam Zuid, then via Weesp to Almere and ends in Lelystad. The line contains multiple locations where traffic merges and diverges to other corridors.

In this section, we describe the infrastructure scenarios and traffic scenarios for the SAAL corridor. Next, we elaborate on several assumptions that are relevant for the Netherlands. Finally, we describe which simulations are to be executed.

#### 5.13.1 Infrastructure

The infrastructure consists of several parts of 4-track. These sections lie between Hoofddorp, Schiphol and Amsterdam Zuid and around Weesp. Furthermore, the stations of Rai, Weesp, Almere Centrum, Almere Oostvaarders and Lelystad Centrum provide more than 2 platform tracks. The rest of the line is all double track.

The reference infrastructure scenario is the base infrastructure on which a Level 2 design from the real project is assigned according to design version 2.0 of February 2024. We will vary two infrastructure design parameters in order to find the ideal design principle under various conditions of usage. Propose 7 different infrastructure scenarios, based on variations around two parameters to find the proper design principles for various usage of the:

1. Number of axle counters

2. Distance of virtual blocks

3. Based on these two parameters we have created seven infrastructure design scenarios that will be described below.

The number of TTD blocks can be varied in 3 gradations:

1. The base infrastructure on which a Level 2 design from the real project according to design version 2.0 of February 2024. This is infra scenario I-0.

2. The first HTD design, numbered I-1, is based on the base L2 design of I-0 and assumes a headway of approximately 1 minute without buffer times still reachable on the TTD for degraded situations and behind trains without TIM. This leads to a reduction of 50 % axle counters as a result of the following assumptions:

- Physical blocks of  $ \sim $  2 km on tracks without regular freight traffic, given passenger trains running at 140 km/h

- Physical blocks of 0.5 – 1 km on tracks with regular freight traffic, given freight trains running at 100 km/h

• Some shorter physical blocks near stations

• No additional virtual blocks

3. The second HTD-design, numbered I-4, is the base infrastructure with only a minimum number of axle counters, always near other physical objects (switches and level crossings).

---

This leads in the worst case to trains running only at station distance in degraded situations or behind trains without TIM.

The distance of virtual blocks can be varied in 2 gradations:

- The base infrastructure from scenario I-1 or I-4 with additional virtual blocks to further optimise capacity. The virtual blocks are 200-250 meters apart (usually by splitting the designed TTD-blocks in 2 VSS). This fits to a headway of approximately the timetable resolution of 6 s for the shortest and fastest trains. These scenarios get the numbers I-2 and I-5.

- The infrastructure from scenarios I-2 and I-5 with additional virtual blocks to further optimise capacity. The virtual blocks are 100-125 meters apart. This fits to a headway of approximately half the timetable resolution of 3 s for the shortest and fastest trains. These scenarios get the numbers I-3 and I-6.

This leads to the total of 7 infrastructure scenarios, numbered I-0 to I-6, as shown in Table 18.

[
  {
    "Increasing number of virtual blocks →": "x"
  },
  {
    "Increasing number of virtual blocks →": "I-3 Medium number axle counters, virtual blocks every 100-125m"
  },
  {
    "Increasing number of virtual blocks →": "I-6 Minimum number axle counters, virtual blocks every 100-125m"
  },
  {
    "Increasing number of virtual blocks →": "Only “Flevo” line"
  }
]

In order to find a balance between workload and the demand for simulations we propose to simulate all scenarios in which the distance between virtual blocks are varied only on the "Flevo" line between Muiderberg Aansluiting and Lelystad (note that the Flevo Line is the northeastern part of the SAAL area). This leads to infra scenarios I-1 and I-4 having a version on the whole scope of SAAL and on the scope of only the Flevo line. These infra scenarios are marked with S and F respectively.

---

reference I-0 is only analysed for the whole SAAL area and the infra scenarios I-2, I-3, I-5 and I-6 are only analysed for the smaller Flevo area.

Direct comparison is possible between infra scenarios in every column [I-0, I-1S and I-4S], [I-1S and I-4S], [I-1F and I-4F], [I-2 and I-5] and [I-3 and I-6] and in every row [I-1F, I-2 and I-3] and [I-4F, I-5 and I-6], where within each group the geographical area is the same and is only varied in one layout setting, either the number of axle counters or the number of virtual blocks. The design of the Flevo Line for the infrastructure scenarios I-0 and I-1 are displayed in Figure 15 and Figure 16, respectively.

[
  {
    "Time": "29",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "28",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "27",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "26",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "25",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "24",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "23",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "22",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "21",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "20",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "19",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "18",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "17",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "16",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "15",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "14",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "13",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "12",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "11",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "10",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "9",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "8",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "7",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "6",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "5",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "4",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "3",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "2",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "1",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "0",
    "Wp (Vtbr)": "0.0",
    "Mbga (Vtbr)": "0.0",
    "Ampo (Vtbr)": "0.0",
    "Almm (Vtbr)": "0.0",
    "Almp (Vtbr)": "0.0",
    "Almb (Vtbr)": "0.0",
    "Almo (Vtbr)": "0.0",
    "LD20012 (Vtbr)": "0.0",
    "BD00012 (Vtbr)": "0.0"
  },
  {
    "Time": "Nr",
    "Wp (Vtbr)": "Infra scenarios",
    "Mbga (Vtbr)": "Description"
  },
  {
    "Time": "T-1",
    "Wp (Vtbr)": "All 7",
    "Mbga (Vtbr)": "Regular timetable without freight trains"
  },
  {
    "Time": "T-2",
    "Wp (Vtbr)": "I-0, I-1S, I-4S",
    "Mbga (Vtbr)": "Regular timetable including freight train paths numbered AB10 and KBG10"
  },
  {
    "Time": "T-3",
    "Wp (Vtbr)": "All 7",
    "Mbga (Vtbr)": "Sprinters that do not include a TIM. We choose Sprinters instead of intercities because Sprinters are more constricting in the timetable"
  },
  {
    "Time": "T-4",
    "Wp (Vtbr)": "I-1F, I-2, I-3, I-4F, I-5, I-6",
    "Mbga (Vtbr)": "Regular timetable including a freight train on a detour route"
  },
  {
    "Time": "T-5",
    "Wp (Vtbr)": "I-1F and I-4F",
    "Mbga (Vtbr)": "Regular timetable including a non integer train (i.e. an open access train) on detour route"
  },
  {
    "Time": "T-6",
    "Wp (Vtbr)": "I-1F, I-2, I-3 *",
    "Mbga (Vtbr)": "Regular timetable (without a freight train on a detour) in which 1 train has an unplanned stop for 15 minutes. **"
  },
  {
    "Time": "T-7",
    "Wp (Vtbr)": "I-1F, I-2, I-3 *",
    "Mbga (Vtbr)": "Regular timetable (with a freight train on a detour) in which 1 train has an unplanned stop for 15 minutes. **"
  },
  {
    "Time": "*) For these scenarios the three performance indicators for delayed situations will be used. **) 15 minutes, because of the 15-minute pattern of SAAL.",
    "Wp (Vtbr)": "*) For these scenarios the three performance indicators for delayed situations will be used. **) 15 minutes, because of the 15-minute pattern of SAAL.",
    "Mbga (Vtbr)": "*) For these scenarios the three performance indicators for delayed situations will be used. **) 15 minutes, because of the 15-minute pattern of SAAL."
  }
]

---

# Contract No. HE – 101102001

## 6 CONCLUSIONS

The goal of this deliverable is to describe the test specification requirements for ERTMS/ETCS Hybrid Level 3 (HL3), also known as Hybrid Train Detection (HTD), to be considered in EU Rail FP1 WP8 and of which the capacity and robustness effects according to the specified performance indicators will be calculated in EU Rail FP1 WP9. The methodology, case studies and scenarios have been reviewed by partners from EU Rail FP1 WP8, that are now making preparations to execute the required scenarios for WP9.

The scenarios are provided for seven Spanish case studies, two case studies in France, three in Sweden and one in the Netherlands. The Spanish cases cover all five market segments: high-speed, mainline (mixed traffic), (sub-)urban, regional and freight. They are exploratory of the headway performance indicator. The insights can be used further in the French, Swedish and Dutch cases, that cover the high-speed, mainline (mixed traffic) and (sub-)urban market segments. They use also relative capacity utilisation as a measure in order to evaluate the capacity from a line and network perspective. Finally, two cases from Sweden (Southern mainline) and the Netherlands (SAAL-corridor) will be used to evaluate HTD-designs for their robustness by adding a deterministic delay to a single train. This is measured by the performance indicators: recovery time, number of affected trains and total delay in the system.

The scenarios are built specifically around logical combinations of infrastructure and traffic. In the infrastructure, the variance lies in the number and positioning of trackside train detection and the virtual subsections in between. In the traffic the variance is possible in the share and types of trains that are equipped to fully utilise HTD by having a Train Integrity Monitor on board.

The results of the calculations of EU Rail FP1 WP9 will be used in the development and evaluation of the method for track layout with ETCS HTD, that will be described in deliverable 37.2 of this work package. Another evaluation of the results will be performed in EU Rail FP2 WP32, where different DATO-concepts are compared.

---

## REFERENCES

[1] ERTMS/ETCS Subset-026 4.0.0: System Requirements Specification.

[2] EEIG ERTMS Users Group, 2024, ERTMS/ETCS Hybrid Train Detection: Principles, Ref. 16E042 Version 1G, Brussels, Belgium.

[3] ERTMS/ETCS Subset-026: System Requirements Specification 3.6.0.

[4] RMCon Rail Management Consultants International GmbH, 2020, RailSys Manual, Hanover, Germany.

[5] www.renfe.com.

[6] Consigna Serie A-2890 Versión 34 de 04-09-2023. ADIF.

[7] Consigna Serie A-2904 Versión 19 de 04-08-2023. ADIF.

[8] Barcelona-Figueras. Esquema de vías y aparatosn Versión 4.7 de 11-01-2007. ADIF. Figueras.

[9] Consigna Serie A-3035 Versión 17 de 25-03-2024. ADIF.

[10] Consigna Serie A-2915 Versión 53 de 09-10-2023. ADIF.

[11] Trafikverket, 2024, RAPPORT Tågtrafik 2045 med fastställd plan 2022–2033.

[12] Jansen, J.M., 2019, ERTMS/ETCS Hybrid Level 3, a simulation-based impact assessment for the Dutch railway network, Delft University of Technology.