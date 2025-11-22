# Back to basics: Operator interfaces

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//094021ee-24a6-4fc9-b2b4-d4dc7e113d1d/markdown_0/imgs/img_in_image_box_2_418_154_579.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A37%3A44Z%2F-1%2F%2Facad59176754aded0d283c4a0d392a3f349537fdde0ebc090576184939b21a65" alt="Image" width="12%" /></div>


Example of a mechanical lever frame. Note the indicators on the front of the shelf over the levers, showing the status of points and signals.

Ian Mitchell

This article in the 'Back to basics' series covers the subject of the interface between the signalling system and a human operator in a signalbox or control centre. The technology of these systems varies from mechanical levers and control panels with switches or buttons to computer workstations, but they all provide controls, which enable the operator to manage train movements and indications, which provide the operator with information about the status of the signalling equipment and position of trains.

As with other 'back to basics' articles, the intention is to provide an overview for IRSE members new to the industry who do not have experience of working in this specific area. The aim is to describe the systems in a generic manner, but using examples based mainly on UK main line railway practice. The scope is limited to the core signalling functions and excludes voice communications, which is of course also a key element of any operator interface.



<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//094021ee-24a6-4fc9-b2b4-d4dc7e113d1d/markdown_0/imgs/img_in_image_box_663_238_1148_533.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A37%3A44Z%2F-1%2F%2Fdbec3de102bb26f622a22a8ffdd37c09f15a1496a95e2eb8dbb935a463e524a9" alt="Image" width="40%" /></div>


## Evolution of the interface

In the mechanical signalling era, the operator interface and the interlocking were combined, the controls were levers above the floor of the signalbox that directly interacted with the mechanical interlocking in the locking room below, and via rods and wires to the points and signals on the railway outside.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//094021ee-24a6-4fc9-b2b4-d4dc7e113d1d/markdown_0/imgs/img_in_image_box_0_1052_1190_1681.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A37%3A44Z%2F-1%2F%2F09208fc76558f96ad4fea9dd587a475cd95e7ea6c3d294ba5e3ddbf5079d408e" alt="Image" width="99%" /></div>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//16fe0847-42d9-4372-8193-edbf4c12dee3/markdown_0/imgs/img_in_image_box_0_24_1188_636.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A37%3A41Z%2F-1%2F%2F79a34aa7a7d6397f55c17ce68a3ea20f9a696f1c1c51143028521c7b975fd0d5" alt="Image" width="99%" /></div>


Example of a first generation computer workstation with screens and a trackerball. This is the workstation controlling Liverpool Street terminus in London at the first Integrated Electronic Control Centre (IECC) commissioned by British Rail in 1989 – still in service in 2020 but due to be upgraded in the near future.

“The operator interface in a modern control centre is now usually a computer workstation with multiple screens”

locked. The progress of a train then appears as the white route lights changing to red in sequence along the route.



The NX controls and indications can either be combined on a single panel, or split with controls on a desk immediately in front of the operator and indications on a separate panel (often wall mounted) behind the desk – the latter arrangement is more common for large control centres with multiple operators.

## Computer workstations

The operator interface in a modern control centre is now usually a computer workstation, with multiple screens to display a schematic track diagram of the railway under control. The indications of signalling equipment status, route setting and track occupation are provided by colour coding of the symbols on the schematic track diagram, following the conventions that were originally established for lights on panels.

The operator interacts with the system via a computer keyboard and a mouse or trackerball, with a mode of operation mimicking an OCS or NX panel, e.g. click on route entrance symbol and select a route from a drop down list, or click on entrance symbol and then exit symbol in sequence.

One significant difference between computer workstations and the older technologies is in the method by which an operator applies a 'reminder' to prevent themselves from operating a control; for instance to prevent points being moved when maintenance is being undertaken. With levers or a panel, the reminder is simply a physical device that the operator attaches to the control that prevents it being operated – a collar on a lever, or a cap over a button or switch. On a computer workstation, the reminder is a software function that needs to be designed into the signalling system. A reminder is displayed on the workstation screen as highlighting of the symbol for the signalling object to which it applies, and the interlocking must reject any attempt to operate a control with a reminder applied (this check may be within the computer workstation interface where an older interlocking without this facility is recontrolled).



The number of screens is determined by the size and complexity of the area under control. It is usually a requirement that an overview of the whole of the controlled area must be visible at any time, and this is sometimes achieved on an upper row of screens displaying fixed areas, while the operator interacts with a lower row of screens on the desk where a selected area can be displayed in more detail, and to view the status of alarms and other information from the system.

The overview displays may be shared between multiple workstations – sometimes this is a very large wall mounted display covering the whole control centre area. This may be provided mainly for the benefit of managers or other staff in the room; an alternative to this is a 'supervisors workstation' where any of the signalling screens can be selected to be displayed on a 'view only' basis. Some control centres now cover very large areas, with tens of workstations controlling several hundred route kilometres of railway.

Computer workstations often provide additional functionality beyond the standard controls and indications, such as automatic route setting (ARS) or overrun management. Some of these are described later in the article.

## Technology and safety

In the mechanical and early relay interlocking era, the technology for the operator interface was simply a direct mechanical or electrical interface between levers, switches, lamps and relays. The concept of the signalling control system as a separate entity from the interlocking appeared

---

interfaces to the interlockings and the area-wide functions such as automatic route setting and train describer (see below) from the operator interfaces. This allows the areas controlled by the workstations to be dynamically reconfigured, for instance to reduce the number of workstations that need to be staffed in quiet periods. A further extension of this concept is to allow dynamic reconfiguration between control centres – for instance to provide a backup disaster recovery facility to maintain train operations when the primary control centre building has to be evacuated as a result of a terrorist attack or a natural disaster.

## Train describer

The track occupation indications on a panel or workstation show where there are trains in the controlled area, but the operator (or ARS) also needs to know the identity of each train so that it can be routed correctly. Each train will be allocated a number or alphanumeric code (sometimes called a 'headcode') and these are displayed to the operator by a system known as a 'train describer'. Train describers were one of the earliest applications of computer technology in signalling, and with a control panel the train describer is a dedicated processor interfaced to small alphanumeric displays set into the indications panel, or a separate computer screen. On a computer workstation the train describer is simply a software function within the system, with the train numbers displayed at the appropriate locations on the main screens. In either case a user interface to the train describer is required to allow an operator to enter (sometimes referred to as 'interposing'), delete and amend train numbers or enter other codes such as line blocked.

As conventional lineside signalling does not provide a data path for a train to report its identity to the control centre, the train described requires the train number to be entered manually by an operator or automatically from the timetable at the start of the train's journey, and it then tracks the train through the controlled area by monitoring the sequence of route setting and track section occupation. The train described logic is based on the concept that trains move between 'berths' – when a train is in the berth associated with a signal, it means this is the next signal it will encounter in its journey. Additional berths are provided at locations where trains may reverse, or where permissive working allows more than one train in a section.

When a train passes from one control area to another, the train number is transmitted as a data message between the train descriptors for the two areas. Similar data messages reporting every train step are also sent from each train descriptor to a national train running information system, which provides the data source for real-time customer and staff information displays, automated public address announcements, and recording systems for performance monitoring.

## Alarms and overrun management

Whatever the technology, the interface will provide a number of alerts and alarms. Some of these relate to equipment failures, and others to events that the operator needs to be aware of. A typical example will be a train descriptor alarm when a track section becomes unexpectedly occupied.

A specific alarm for signal passed at danger (SPAD) was introduced in the UK as a result of the public inquiry recommendations following the Ladbroke Grove accident in 1999. When a track section occupation sequence occurs at a red signal which may be as a result of a SPAD, a distinctive (and loud) alarm sounds and the area of overrun at the signal is highlighted on the workstation screens.

On some recent installations with computer workstations this facility has been further enhanced with an automated response to the SPAD event to stop other trains in the area. The processor in the interface system sends requests to the interlocking to replace other signals on the approach to the SPAD area. This is known as a 'predefined operational protection' (POP) control. Providing this capability in the SIL 2 interface system can allow simplification of logic in the SIL 4 interlocking.

## Automatic Route Setting

Modern control centres with computer workstations often include an automatic route setting (ARS) facility. This reduces the operator workload linked to routine train movements, allowing them to focus on problem areas and tasks that require voice communications with staff and the public.

ARS is usually a separate processor within the operator interface system that monitors the movement of trains as reported by the train descriptor, and uses an electronic version of the timetable for the day to identify which routes should be set to allow each train to run through the controlled area on its planned path and timings. Where possible the objective is to set routes sufficiently far ahead of the train so the driver always sees green signals, although there are exceptions to this, e.g. where departure from a station needs to wait for a 'train ready to start' message from platform staff.

An important principle is that ARS should not 'challenge' the interlocking by requesting a route that is not available to be set. This requires the ARS to be programmed with a copy of the interlocking route availability logic and to monitor the signalling states such as track occupancy, route locking and reminders.

When trains are running late, it is very likely that conflicts will arise where two trains require to run over the same section of track at the same time. This can arise when routes converge or cross, and at crossing points on single lines (see the article by John Francis in the June 2020 IRSE News for some examples). ARS requires an

---

algorithm to decide which train to give priority in these circumstances – this might be to keep the trains in timetable order, 'first come first served' or a comparison of the predicted train delays for the alternative options. At the design stage for a new installation, workshops with operators who are experienced with the train service in the area are a valuable source of information to tailor the algorithms for each potential area of conflict.

The operator retains the capability to set routes manually at any time, and where this is necessary the operator can switch off ARS for an individual train, or for an 'ARS sub-area', typically a single junction or running line between stations. ARS sub-areas will also be automatically switched off if an operator cancels a route that has been set by ARS, a SPAD is detected, or a signal group replacement control is operated.

## Traffic management

Traditionally the timetable used by ARS was updated on a daily basis from the national train planning systems. Since ARS can only set routes for trains according to the timetable, additional trains and those required to deviate from the timetable have to be routed manually by the operator. This can be avoided if ARS can be provided with a dynamic timetable, updated throughout the day with changes to the plan. This is the concept behind 'traffic management' which aims to move away from operators making train routing decisions in real time, to a process where issues are identified well in advance, and solutions are identified and incorporated into the dynamic timetable so that all trains can be routed by ARS.

Traffic management systems are another layer of functionality that sit above the primary operator interfaces described in this article. The interface with the signalling is via timetable updates to ARS, so there is minimal safety impact (i.e., SIL 0). They may also be used by operators who have strategic responsibility for a whole route, a 'controller' or 'despatcher' rather than a 'signaller'. The user interface is usually in the form of a train graph or a platform occupation chart, which shows the planned, actual and predicted movement of each train and highlights trains that are deviating from the plan and the consequential conflicts with other trains and with planned line blockages. Edit facilities allow trains to be rescheduled, rerouted or cancelled, and additional trains to be inserted into the timetable. There may also be a 'what if' facility to allow an operator to try out alternative options for rescheduling, evaluate the impact on train delays and other key performance indicators for the train service, and then deploy the chosen option into the dynamic timetable.

## Train protection and ERTMS/ETCS

Train protection systems overlaid onto conventional lineside signalling using track mounted equipment to communicate with the train (e.g. TPWS in the UK) have little impact on the operator interface, other than perhaps an indication to warn of equipment failure.

ETCS level 2 introduces a communication link between the train and a radio block centre (RBC), and this may require an operator interface, to provide information on the ETCS mode of operation of each train, and to allow updating of temporary speed restrictions. In early applications these functions have not been integrated into the primary operator interface system (which is only linked to the interlocking), and a separate stand-alone terminal from the ETCS supplier provides an operator interface to the RBC. As ETCS becomes more widespread, more integrated solutions are likely to evolve.



## Metros

On modern metros with CBTC signalling, the system architecture generally includes a component known as 'automatic train supervision' (ATS), and this incorporates the operator interface, including automatic route setting and traffic management functions. ATS interfaces with automatic train operation (ATO) so that decisions made in the control centre can directly influence movement of trains without involvement of a human driver.

For most metros the key parameter being managed is not the adherence to the timetable, but the regularity of trains, and the operator interface allows this to be monitored and managed. If two trains are running close together, ATS can delay the departure of the second train from a station to even out the gaps in the service, or instruct the ATO to run at reduced speeds between stations to save energy.

## I ntegration of systems

This article has described the operator interface for the core signalling functions, but in a modern control centre the person at a control panel or computer workstation will also have to interact with a number of other systems. Examples of this can include voice communications with train drivers and track workers, closed circuit television (CCTV) monitoring of level crossings and stations, monitoring systems for vehicle or infrastructure faults, passenger and staff information systems, supervisory control and data acquisition (SCADA) systems for electric traction power supply, and even corporate information technology (IT) applications such as emails and timesheets.

Traditionally there has been little integration of the operator interfaces for these systems – a typical computer workstation will have a separate terminal on the desk for voice communications, an office type personal computer for the corporate IT network, and dedicated screens for CCTV monitoring. The technology exists to integrate all of these into a single interface, but there are practical, commercial and safety assurance obstacles to integrating systems from different suppliers when there are no standard interface specifications, and differing system architectures, SIL requirements and system lifecycles. An integrated solution is most likely to be seen on a turnkey project to build a new metro or high speed line.

---

## Human factors

It goes without saying that an effective operator interface to the signalling system must be designed with the operator in mind, and human factors specialists have played an increasingly important role in design of modern control centres. This starts with workload analysis to determine how large an area of railway can be effectively managed by an individual operator, is this will determine the number of workstations and hence the size of the control room. The constraining factor will be determined by the level of automation in the system; for instance where ARS is provided, the workload during busy periods of train operations may be less than at night when the operator has to manage line blockages for work on the track.

At a more detailed level, the size of text and symbols on the screens, the number of screens and their location on the desk, the height of the desk and even the type of chair all need consideration to ensure the operator remains alert and comfortable.

## Conclusion

As with other areas of signalling technology, the evolution from levers to computer mouse has been dramatic, but the fundamental principles of controls and indications remain. What has changed the most is the level of automation; modern systems now require little human intervention when the railway is running to plan, but an experienced operator and a well-designed human interface are still crucial in dealing with failures and unexpected scenarios.

One of the lectures later in this year's Presidential Programme will specifically explore the issue of automation in control centres – what are the strengths and weaknesses of existing systems, what further tasks could be automated, and how to we ensure the human and computer work together most effectively?

/vancouver's Canada Line was equipped from opening with an integrated control centre, bringing a range of signalling, station and communication functions together at one workstation.

photo Siemens Mobility.

## About the author 

Ian Mitchell has 45 years' experience in the rail industry, in British Rail Research and its post-privatisation successor companies – AEA Technology Rail, DeltaRail and Resonate. He retired as professional head of signalling in 2011, but still does some consultancy for his previous employers as well as acting as one of editors of IRSE News and as a member of the International Technical Committee. He presented a Presidential Paper on the topic "Signalling Control Centres Today and Tomorrow" in 2003, and is due to deliver another in 2021 jointly with Nora Balfe, who is a human factors specialist with Irish Rail.

## “Back to basics” and the IRSE Exam

We hope that our "Back to basics" articles are particularly interesting to those of you who are new to the industry and are working to build up your knowledge. For those considering taking the IRSE exam, these articles should be particularly relevant for your studies.

As an example, why not think about how you would answer this question from the 2015 Module 5 of the exam, based on what you've learnt from the article?

Describe, with the aid of a drawing, the layout of either a mimic panel or a signaller's VDU display control system. You should include details of how each of the following are dealt with:

i) Route Setting and cancellation [4 marks].

ii) Manual movement of points [3 marks].

iii) Train detection status during normal and failure conditions [4 marks].

iv) Protection of different types of engineering work [3 marks].

v) How a major failure of the display would be managed [4 marks].

vi) Signals Passed at Danger [2 marks].

vii) Train identification [3 marks].

viii) Adjacent signal box alarms [2 marks].

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e7de24ee-ad6d-4153-9ef8-53cc62ff03a9/markdown_0/imgs/img_in_image_box_0_1120_1191_1677.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A38%3A05Z%2F-1%2F%2F038718649d063b7039c7bdb4afacbe2a64f3ae17350835876418b0fc2886b03c" alt="Image" width="100%" /></div>