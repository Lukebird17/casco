Effective from October 2023 exam

# Interfaces and Interactions between Railway Control & Communications and Related Systems

An introduction for candidates taking Module A of the IRSE Professional Examination

Kimberley Chang, February 2021

version 2 - April 2023

The railway system is made up of various subsystems which interact to deliver the required outputs, normally the movement of passengers and freight. The way these systems interact all have a role to play in the safe and efficient running of the overall railway. Railway control and communications systems are designed and operated whilst taking into account their interactions with related systems. This article gives an overview of the interfaces and interactions between railway control and communications systems and the related subsystems in the railway environment.

Prominent subsystems are:

• Signalling;

• Telecommunications;

• Operations, including control centres, passenger information and public address systems;

• Drivers:

• Rolling stock;

- Permanent way / track – including the rails, fasteners, sleepers and ballast / slab track as well as on-track train detection & monitoring systems;

• Civil Engineering structures, including bridges, tunnels and stations;

• Electric traction supply;

• Electric power systems;

• Evacuation systems.

During the life of a railway system, changes will be made either to enhance its capacity and capability, renew life expired assets or add new services. When making changes to one part of the system it is essential that the impacts of the change on other parts of the system are considered if the overall system is to continue to perform its functions safely and correctly.

## I nterfaces and Interactions with Operations

## Control Centres and Signallers

The railway is controlled by signallers at signalling control centres who input their instructions via a control device, such as a computer screen, control panel or lever frame into the interlocking. After checking the instructions are safe, the interlocking passes the instructions on to the trackside infrastructure. It is important that the state of the infrastructure is feed back to the signaller in the form of indications on the computer display screen, indications panel, positions of the levers or by simply looking out of the window!

The interfaces with the signaller are described in more detail in the Back to Basics Article “Operator Interfaces” (IRSE News, Issue 269, September 2020).

## Train Describers

To set the correct route for a train, the signaller needs to know the identities of the individual trains as they enter, pass through and leave the control area. Each train is allocated a train reporting

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

number, to identify the train. The train reporting number allocates each train a unique identity which may be based on a combination of the train type, destination, operating company and an identity number.

The train reporting numbers are initially entered into the system by the operator, which may be a signaller, or depot controller at the start of the train’s journey. The train described then uses information from the interlocking about the status of the signalling system to “step” the train through the control area. At the fringes of the control area, the information is passed to adjacent train describers via a telecoms link.

The train reporting numbers can be manually altered, or interposed by a signaller if required. This may occur when a train has reached the end of its timetabled service and needs to start a new one, when a train divides to form two separate services or two trains join to make one.

The train descriptor system is not safety critical, as the interlocking protects trains from unsafe movements if a train is misrouted.

## Passenger Information & Public Address Systems

A passenger information system delivers real-time information to passengers about the nature and state of the railway. The customer interface usually consists of:

- visual information display screens at stations and on trains;

• audio announcements at stations and on trains;

• mobile phone applications; and

- railway operator or travel planner websites.

Passenger information and automated public address systems usually take their inputs from the train described and the timetable information to create real-time data. More information on passenger information systems can be found in the Back to Basics article “Telecoms Part 2” (IRSE News, Issue 271, November 2020).

## I nterfaces and Interactions with Drivers

There are several train-borne systems that perform the role of interfacing between the signalling system and the train driver.

## Automatic Train Protection

Automatic train protection systems are designed to prevent or mitigate the consequences of trains passing signals at danger, over-speeding or overrunning buffer stops. Examples include: train stops on metro systems, the Automatic Warning System used in UK and Australia, or the European Train Control System.

An automatic train protection system take information about the status of the signalling system, such as signal aspects, issued movement authorities or permissible speed information. The system automatically intervenes if trains are travelling too quickly to safely stop at a signal at danger or buffer stop, or decelerate sufficiently for a speed restriction. The intervention may consist of an alarm and/or visual indication in the driver's cab, or go further and automatically apply the brakes until either the train has slowed sufficiently or stopped completely, depending on the system installed.

## Automatic Train Operation

Automatic Train Operation is used to help automate the operation of trains and can vary in the degree of automation offered. This varies from no automation at the lowest level, to full

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

automation, including starting and stopping of trains, operation of doors and handling of emergency situations. It is primarily in use in metro systems, but is becoming more widespread on mainline railways. Automatic Train Operation takes input from the signalling system to determine how far ahead the line is clear, and trackside beacons that transmit brake commands to the train. The train's on-board computer calculates the required the braking curve to bring the train to a stand at the correct position in platforms or at junctions. The braking calculations are updated frequently to ensure accuracy.

## Driver Advisory System

The driver advisory system aims to optimise the driving of the train, saving energy and improving performance. The system consists of a control centre subsystem that evaluates timetable information and routing strategies, and sends the processed information to the train. The train's onboard subsystem uses this information to calculate energy efficient speed profiles to achieve train timings and issues advice to the driver. Some of these systems are static, so the information is received by the on-board subsystem at the start of the journey, whilst others are connected to the control centre subsystem during the journey and updated dynamically via radio.

## Secure Train to Signal Box Radio

Secure train to signal box radio (including GSM-R) is used to communicate between the train and the control centre. The driver is provided with an in-cab terminal which can be used to display and send messages or voice communications between the driver and operational staff. More information on secure train to signal box radio systems can be found in the Back to Basics article “Telecoms Part 1” (IRSE News, Issue 270, October 2020).

## I nterfaces and Interactions with Rolling Stock

## Braking Characteristics

The braking characteristics of the rolling stock vary between train types, with some having much better braking performance, such as modern passenger trains, than others, such as heavy freight trains. Signals are required to be positioned such that the space between the first caution signal and a signal at danger is sufficient for all train types authorised to run that route, with sufficient warning to stop (plus a safety margin).

[
  {
    "Point": "Category",
    "#": "Value"
  },
  {
    "Point": "1",
    "#": "100"
  },
  {
    "Point": "2",
    "#": "80"
  },
  {
    "Point": "3",
    "#": "60"
  },
  {
    "Point": "4",
    "#": "40"
  },
  {
    "Point": "5",
    "#": "20"
  },
  {
    "Point": "6",
    "#": "10"
  },
  {
    "Point": "7",
    "#": "0"
  },
  {
    "Point": "Color",
    "#": "Light Blue"
  }
]

[
  {
    "Category": "1",
    "Value": "1"
  },
  {
    "Category": "2",
    "Value": "2"
  },
  {
    "Category": "3",
    "Value": "3"
  },
  {
    "Category": "4",
    "Value": "4"
  },
  {
    "Category": "5",
    "Value": "5"
  },
  {
    "Category": "6",
    "Value": "6"
  },
  {
    "Category": "7",
    "Value": "7"
  },
  {
    "Category": "8",
    "Value": "8"
  },
  {
    "Category": "9",
    "Value": "9"
  },
  {
    "Category": "10",
    "Value": "10"
  },
  {
    "Category": "11",
    "Value": "11"
  },
  {
    "Category": "12",
    "Value": "12"
  },
  {
    "Category": "13",
    "Value": "13"
  },
  {
    "Category": "14",
    "Value": "14"
  },
  {
    "Category": "15",
    "Value": "15"
  },
  {
    "Category": "16",
    "Value": "16"
  },
  {
    "Category": "17",
    "Value": "17"
  },
  {
    "Category": "18",
    "Value": "18"
  },
  {
    "Category": "19",
    "Value": "19"
  },
  {
    "Category": "20",
    "Value": "20"
  },
  {
    "Category": "21",
    "Value": "21"
  },
  {
    "Category": "22",
    "Value": "22"
  },
  {
    "Category": "23",
    "Value": "23"
  },
  {
    "Category": "24",
    "Value": "24"
  },
  {
    "Category": "25",
    "Value": "25"
  },
  {
    "Category": "26",
    "Value": "26"
  },
  {
    "Category": "27",
    "Value": "27"
  },
  {
    "Category": "28",
    "Value": "28"
  },
  {
    "Category": "29",
    "Value": "29"
  },
  {
    "Category": "30",
    "Value": "30"
  },
  {
    "Category": "31",
    "Value": "31"
  },
  {
    "Category": "32",
    "Value": "32"
  },
  {
    "Category": "33",
    "Value": "33"
  },
  {
    "Category": "34",
    "Value": "34"
  },
  {
    "Category": "35",
    "Value": "35"
  },
  {
    "Category": "36",
    "Value": "36"
  },
  {
    "Category": "37",
    "Value": "37"
  },
  {
    "Category": "38",
    "Value": "38"
  },
  {
    "Category": "39",
    "Value": "39"
  },
  {
    "Category": "40",
    "Value": "40"
  },
  {
    "Category": "41",
    "Value": "41"
  },
  {
    "Category": "42",
    "Value": "42"
  },
  {
    "Category": "43",
    "Value": "43"
  },
  {
    "Category": "44",
    "Value": "44"
  },
  {
    "Category": "45",
    "Value": "45"
  },
  {
    "Category": "46",
    "Value": "46"
  },
  {
    "Category": "47",
    "Value": "47"
  },
  {
    "Category": "48",
    "Value": "48"
  },
  {
    "Category": "49",
    "Value": "49"
  },
  {
    "Category": "50",
    "Value": "50"
  },
  {
    "Category": "51",
    "Value": "51"
  },
  {
    "Category": "52",
    "Value": "52"
  },
  {
    "Category": "53",
    "Value": "53"
  },
  {
    "Category": "54",
    "Value": "54"
  },
  {
    "Category": "55",
    "Value": "55"
  },
  {
    "Category": "56",
    "Value": "56"
  },
  {
    "Category": "57",
    "Value": "57"
  },
  {
    "Category": "58",
    "Value": "58"
  },
  {
    "Category": "59",
    "Value": "59"
  },
  {
    "Category": "60",
    "Value": "60"
  },
  {
    "Category": "61",
    "Value": "61"
  },
  {
    "Category": "62",
    "Value": "62"
  },
  {
    "Category": "63",
    "Value": "63"
  },
  {
    "Category": "64",
    "Value": "64"
  },
  {
    "Category": "65",
    "Value": "65"
  },
  {
    "Category": "66",
    "Value": "66"
  },
  {
    "Category": "67",
    "Value": "67"
  },
  {
    "Category": "68",
    "Value": "68"
  },
  {
    "Category": "69",
    "Value": "69"
  },
  {
    "Category": "70",
    "Value": "70"
  },
  {
    "Category": "71",
    "Value": "71"
  },
  {
    "Category": "72",
    "Value": "72"
  },
  {
    "Category": "73",
    "Value": "73"
  },
  {
    "Category": "74",
    "Value": "74"
  },
  {
    "Category": "75",
    "Value": "75"
  },
  {
    "Category": "76",
    "Value": "76"
  },
  {
    "Category": "77",
    "Value": "77"
  },
  {
    "Category": "78",
    "Value": "78"
  },
  {
    "Category": "79",
    "Value": "79"
  },
  {
    "Category": "80",
    "Value": "80"
  },
  {
    "Category": "81",
    "Value": "81"
  },
  {
    "Category": "82",
    "Value": "82"
  },
  {
    "Category": "83",
    "Value": "83"
  },
  {
    "Category": "84",
    "Value": "84"
  },
  {
    "Category": "85",
    "Value": "85"
  },
  {
    "Category": "86",
    "Value": "86"
  },
  {
    "Category": "87",
    "Value": "87"
  },
  {
    "Category": "88",
    "Value": "88"
  },
  {
    "Category": "89",
    "Value": "89"
  },
  {
    "Category": "90",
    "Value": "90"
  },
  {
    "Category": "91",
    "Value": "91"
  },
  {
    "Category": "92",
    "Value": "92"
  },
  {
    "Category": "93",
    "Value": "93"
  },
  {
    "Category": "94",
    "Value": "94"
  },
  {
    "Category": "95",
    "Value": "95"
  },
  {
    "Category": "96",
    "Value": "96"
  },
  {
    "Category": "97",
    "Value": "97"
  },
  {
    "Category": "98",
    "Value": "98"
  },
  {
    "Category": "99",
    "Value": "99"
  }
]

[
  {
    "Item": "Top",
    "Description": "The first row of the chart."
  },
  {
    "Item": "Bottom",
    "Description": "The last row of the chart."
  },
  {
    "Item": "Top",
    "Description": "The second row of the chart."
  },
  {
    "Item": "Bottom",
    "Description": "The first row of the chart."
  }
]

Single slip, where two tracks cross and it is possible to move from one line to the other. Double slips have a slip on each side.

## Point Machines

Points can be controlled by direct connection to a control lever, such as in a mechanical signal box or ground frame, where the movement of the points are under the direct control of a human.

More commonly, the points are driven by a point machine, powered by an electric motor or hydraulic system, with the movements controlled by the interlocking. In both cases, when the points are in use, they are required to be locked in position, so that the points cannot be moved by the signalling system or the vibration of the train. This is particularly important when they are facing points and helps to prevent derailment and damage to the points.

The interlocking must know the position of the point blades, to check that the points are in the correct position for the safe movement of trains and have not failed or become obstructed. An individual detector rod is attached between the point blades and point machine that proves the position of the point blades by making the appropriate contacts within the point machine. If the blades are out by as little as a few millimetres, the rods will not be in the correct position and will prevent the contacts operating. The state of the contacts is fed back to the interlocking so that the signalling system is aware of the lie of the points.

Other types of point machine exist that apply locking and prove point lie in different ways, but the requirement for locking and detection of points is essentially the same.

## Catch/Trap Points

It is sometimes necessary to derail a train deliberately to protect against potential collision with another train.

Catch points are designed to derail anything running against the normal direction of traffic, such as loose wagons that have no or ineffective brakes and have "run away". The spring catch point consists of one point blade, normally open in the derailing position. A train moving in the normal direction will push the point blade closed against a spring and continue unimpeded. A train moving in the wrong direction will derail at the spring catch. Another type of catch point is the wide-to-

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

gauge type, consisting of two switches that work in opposite directions with the switches either both open or both closed. These are operated by the signalling system and a train travelling over these points whilst in the open position will be derailed.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2e791348-0a04-44e2-9494-eb40aa4a9602/markdown_0/imgs/img_in_image_box_200_192_504_307.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A41%3A23Z%2F-1%2F%2F189b5da3bf0d14907e9d9192b1900af26e8448d8ab77d808e44a8b93da1d54e6" alt="Image" width="25%" /></div>


<div style="text-align: center;">Spring catch points</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2e791348-0a04-44e2-9494-eb40aa4a9602/markdown_0/imgs/img_in_image_box_611_212_992_326.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A41%3A23Z%2F-1%2F%2Ff1512f8a1dba4f7296a43b826cb8b946cd9d0d9eed549b16fed22d132611f423" alt="Image" width="31%" /></div>


<div style="text-align: center;">Wide-to-gauge catch points</div>


Trap points protect lines from trains on adjacent lines that have passed a signal at danger, typically at the exit from sidings or freight loop lines. They are controlled by the interlocking, with locking and detection of point lie fed back to the signalling system.

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2e791348-0a04-44e2-9494-eb40aa4a9602/markdown_0/imgs/img_in_image_box_355_507_843_662.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T23%3A41%3A23Z%2F-1%2F%2F23a1435b799cb460827b19ffaaa9cfaabe5910f0cae5d79f82ff42a8f6e81741" alt="Image" width="40%" /></div>


## Junctions

Where two railway lines meet, there is potential for conflict between trains. Signals, or limits of movement authority are required close to junctions to prevent trains traversing the junction when it is not safe to do so and to authorise trains to traverse the junction when it is safe.

Signals are usually placed with a safety margin (overlap) between the signal and any potential points of conflict to protect trains traversing the junction from a train overrunning one of the protecting signals due to an error in braking judgement. It is undesirable for signals to be placed at very long distances from the junctions because this would reduce the junction capacity due to the increased time required for a train to clear the junction after being given a movement authority.

## Track-Based Train Detection

Train detection systems are described in more detail in the Back to Basics Article "Train Detection—the Basics" (IRSE News, Issue 261, December 2019).

## Other Rail-Mounted Equipment

Other equipment than can be placed on the track/ between the rails includes:

- Axle counters. These count the number of axles passing over a given point. They are clamped to one of the rails and their location can be constrained by, for example, the presence of check rails or third rails for traction power.

- Train protection systems. There are many different systems, but all involve track mounted equipment sending information to the train by electrical, magnetic or physical means.

ETCS (European Train Control System), CBTC (Communications Based Train Control) and automatic driving systems. These typically require equipment fixed to the sleepers between the rails to transmit to or receive information from trains. The equipment can include beacons or transmitters (often known as balises or transponders) and loops of cable.

---

Interactions between Railway Control & Communications and Related Systems

- Hot axle box detectors. These consist of infrared scanners that measure the abnormal levels of heat generated by failing bearings in axle boxes. Failed bearings cause the axle to seize and can cause derailment, so early detection is essential.

Other items can be fitted to the sleepers rather than the rails such as beacons for on board train announcements or speed restrictions and loops of cable for coded track circuits.

## I nterfaces and Interactions with Civil Engineering Structures

There are many structures around a railway line, either forming part of the railway or forming the surrounding environment. Sometimes the position, size or nature of those structures impact on how the signalling system is designed, constructed, maintained or operated.

## Tunnels, Viaducts and Bridges

Tunnels impact greatly on the ability to position signalling and telecoms equipment. Sometimes this is unavoidable, such as with the underground metro systems found in many cities worldwide. It is preferable for trains not to stop within tunnels or on viaducts due to the risks associated with evacuating a train in these places. Where reasonably practical to do so, signals are placed so that no part of the train is within a tunnel, viaduct, or anywhere else with limited clearance.

Tunnels and viaducts also present a challenge for the installation and maintenance of equipment, due to difficult access for staff, particularly if the tunnel or viaduct is long.

Limited clearance within tunnels can make it very difficult to place signals clear of the train's kinematic envelope, and this is sometimes managed by using special, smaller tunnel signals.

The ability of a driver to see signals at the minimum reading distance can be adversely affected by the walls of the tunnels, particularly if clearance within the tunnel is tight, or the tunnel is curved. It can be difficult for a driver to see the aspect displayed by a signal against a sunlit background if it is placed close to the exit of a tunnel, especially if the tunnel is long or narrow.

Bridges can also affect the ability of drivers to see signals immediately beyond it, as they may be obscured by the walls or span of the bridge.

## Stations and Lineside Buildings

If a passenger train is stopped at a signal and any part of the train is within a station platform, passengers may attempt to board or alight the train. This is a particular problem if the train's doors are not centrally locked. For this reason, stop signals are generally either positioned at the end of platforms or at least a train length beyond the end of the platform. Signals placed at the platform ends are preferably 20-25m from the stopping position of the train so that they can easily be seen by the driver when the train is stationary.

A driver must be able to read, interpret and understand a signal aspect for a sufficient distance on the approach. However, buildings, platform furniture, waiting shelters, canopies and passenger standing on the platforms can adversely affect this, particularly if the platform is curved. To aid the driver, an additional signal can be provided on the approach to the station, or part-way along the platform to give the driver an early indication of the next signal aspect.

The proximity of platforms to the railway line can make installation, inspection and maintenance of lineside equipment difficult. Where practical to do to, equipment such as train detection equipment are placed clear of the platforms so that staff can work on equipment in a position of safety.

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

In built up residential areas, where noise may be a problem for residents nearby, unnecessary railway-related noise must be kept to a minimum. The audible alarms on level crossings may sound at a lower level at night, or restrictions on the use of train horns on the approach to footpath crossings may be imposed, enforced by signage or regional / national operating instructions.

## Other Limitations on Signalling Equipment

Other structures that can also impact on the sighting of lineside signals include electrification gantries, large signal gantries or pipe bridges.

Trains should not stop on level crossings unless it is unavoidable, so signals need to be positioned so that they would not cause a train to obstruct the crossing when standing at the signal. Vandalism is also a risk at level crossings, so all equipment should be a sufficient distance from the crossing, ideally placed beyond security gates and anti-trespass guards / devices.

## I nterfaces and Interactions with Electrification and Power Systems

## Traction Power Supplies

Traction power is delivered by means of an overhead wire or at ground level via a third (live) rail close to the running rails, and collected by the train by a roof-mounted pantograph or rail-level pickup shoe. To create a complete circuit, there is a traction return, which can take several forms.

## Third or Fourth Rail Electrification

Where traction power is delivered by a third rail, the return current is carried by the running rails, or alternatively via a fourth conducting rail. The latter mechanism can be seen in the London Underground or Milan Metro.

One of the difficulties with using one of the running rails for traction return is that the running rail may also form part of the signalling train detection circuits. In this case there is the need for the signalling equipment to be able to distinguish between the traction current and the track circuit current. Train detection boundaries must also allow the traction return current to flow past the boundary to the next track section, but prevent the flow of track circuit current across the boundary. For more information on how this is achieved, refer to the Back to Basics article “Train Detection – the Basics” (IRSE News, Issue 261, December 2019).

## Overhead Line Electrification

Early versions of overhead line electrification also used the running rails to carry the traction return current. A major issue with this is that any conductor carrying a current generates a magnetic field that can induce a voltage in nearby cables, particularly if they run alongside the conductor for great distances, as is often the case with signalling and telecoms cables. To overcome this, the running rails can be electrically bonded so that the return current is shared amongst all running rails in the vicinity, reducing the current in each individual rail. This reduces the level of electromagnetic interference in the signalling and telecoms cables. An advantage of this is that traction current takes multiple paths so, in the event of a rail break, the traction return can return to its source by an alternative path.

To reduce the amount of electromagnetic interference, a dedicated return conductor wire is provided, running parallel to the overhead line at approximately the same height. The return conductor is bonded to the running rails so that it carries some of the traction return current. The current in the return conductor flows in the opposite direction to the overhead line, so the electromagnetic fields generated by the return conductor partially cancels that generated by the

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

overhead line. The current carried by the return conductor is weaker than the overhead lines, so there is still potential for interference in the lineside signalling and telecoms cables.

Electromagnetic interference in lineside cables can be reduced further by using booster transformers, which force nearly all of the traction return current from the rails to the return conductor. This increases the distance between potential sources of electromagnetic interference and other lineside cables, and consequently reduces the level of interference between them.

## Neutral Sections

Sources of traction power (feeder stations) need to be electrically insulated from one another, so a neutral section is provided where no traction power is supplied. This is sufficiently long to ensure that no train can be electrically connected to two separate supplies simultaneously, but not so long that a train will not have enough energy to reach the next live section.

It is important that the signalling system is designed such that no train ever comes to a stand within a neutral section, as any electric train would not be able to accelerate away again.

## I mmunisation

The effects of induction in signalling circuits can be limited by designing the signalling circuits and equipment to be immune from the unwanted currents. This is particularly important in the design of train detection systems where track circuits are used. In areas of AC electrification, DC track circuits may be used, and vice versa. Alternatively, AC track circuits can be used that have no harmonics in common with the traction current, enabling the track circuit receiver to distinguish between the track circuit current and any traction current that may be present in the rails.

## Signal Sighting

Overhead line equipment can affect the ability of a train driver to read and interpret lineside signals and signs when they are obscured by equipment, even if just momentarily. This is a particular problem where overhead line masts are on the inside of curves and may be overcome with the use of cantilever structures for the overhead line masts or alterations to the positions of signals and lineside signs.

## Equipotential Bonding and Earthing

To protect lineside signalling equipment against contact with the traction supply, either directly, such as when overhead wires come down, or indirectly, such as when other equipment is made live by an electrical fault, signalling equipment is bonded to earth.

In areas electrified by overhead line, any metal equipment beneath or near the overhead line is bonded to a running rail carrying traction return current so that if the wires carrying the traction current were to fall, the equipment is earthed via the running rail, protecting the equipment from damage and staff and public from electric shock.

In third/fourth rail electrified and non-electrified areas it is not usual practice to bond all metal structures to the traction return rail.

## Signalling & Telecoms Power Supplies

Signalling and telecoms power supplies must provide a constant, stable supply for the correct operation of equipment. It must also be safe for the staff to work on, with measures in place to protect staff and the public from electric shock under fault conditions.

Signalling equipment within apparatus cases must be earthed to protect staff and equipment from electric shock from contact with exposed conductive parts, such as circuitry, and other conductive

---

Interfaces and Interactions between Railway Control & Communications and Related Systems

parts that could be made live by an electrical fault. Other protective measures include enclosing high voltage equipment in insulated units, providing insulated covers for live parts or insulating conductors.

Signalling and telecoms equipment is commonly powered by a dedicated supply, and may be backed up by an uninterruptible power supply in case of failure of the supply point, to allow time to change to an alternative supply.

## I nterfaces and Interactions with Evacuation Systems

Signalling systems must be designed to minimise the risks associated with emergency evacuation of trains or railway infrastructure. The system should be designed to minimise the risk that an evacuation takes place in an area where it is difficult for passengers to exit a stricken train. It is also important that access to the site is possible for emergency services and rescue teams to provide assistance. For this reason, signals within tunnels, viaducts or steep cuttings are avoided if practical to do so.

The signalling system may also be required to respond quickly to protect a hazard, such as a train crash or fire. In many cases, trains involved in an incident may already be protected by the signalling system. However, there may be a requirement for passengers to exit the train in a hazardous area (or indeed they may do it contrary to instructions) and the signalling will require a mechanism for protecting the site – by replacing all signals in the area to danger or sending an "all trains stop" command via the radio, for example. Emergency communication and signalling intervention is essential to prevent further problems or disaster.