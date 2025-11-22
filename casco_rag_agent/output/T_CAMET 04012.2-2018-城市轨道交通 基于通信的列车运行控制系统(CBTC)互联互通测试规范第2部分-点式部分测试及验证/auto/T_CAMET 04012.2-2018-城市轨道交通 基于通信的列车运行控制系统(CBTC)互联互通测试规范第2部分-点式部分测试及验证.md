# 中国城市轨道交通协会团体标准

T/CAMET 04012.2—2018

城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范

# 第2部分：点式部分测试及验证

Urban rail transit — Test specification for interoperability of communication based train control system Part 2: Test and verification of intermittent train control part

# 目 次

前言 VI

引言 Ⅲ

1范围·  
2规范性引用文件  
3术语和缩略语 3  
3.1术语… 3  
3.2缩略语

4互联互通产品测试生命周期划分及验证活动

4.1测试阶段生命周期划分及验证活动  
4.2测试阶段内容及依据 8

# 5测试环境 8

5.1互联互通系统供应商测试及验证平台需求 8  
5.2互联互通系统集成实验室测试及验证平台需求 8  
5.3互联互通试验线测试及验证平台需求… 10

# 6测试需求· 10

6.1互联互通系统测试验证活动的划分原则 10  
6.2互联互通总体功能及接口功能分配. 12  
6.3 互联互通测试需求… 43  
6.4 互联互通系统测试需求… 44  
6.5 互联互通应答器接口需求… 93  
6.6 互联互通计算机联锁（CI）间接口测试需求 109  
6.7互联互通跨线ATS 间接口测试需求… 116  
6.8互联互通车地通信接口（VOBC和ATS）测试需求 125

6.9互联互通车地通信接口（VOBC和CI）测试需求… 136

7测试案例要求 146  
7.1总体要求 146  
7.2具体要求 146

参考文献…… 148

# 前 言

T/CAMET04012《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范》分为以下两个部分：

-第1部分：CBTC部分测试及验证；  
-第2部分：点式部分测试及验证。

本部分是T/CAMET04012的第2部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：中国铁道科学研究院集团有限公司通信信号研究所、交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、浙江众合科技股份有限公司、北京交通大学、株洲中车时代电气股份有限公司。

本部分主要起草人：编写组：李亮、史宁娟、王鲲、杜恒、刘合叶、刘鲁鹏、卢然、方发根、周在福、黄友能、王悉、吕浩炯、张大涛。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、张琼燕、段晨宁、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、王道敏、徐鼎。

# 引 言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的日标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准

该系列规范包括《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通基于通信的列年运行控制系统（CBTC）互联互通测试规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通T程规范》4个规范（17个部分）

# 城市轨道交通

基于通信的列车运行控制系统(CBTC)

互联互通测试规范

# 第2部分：点式部分测试及验证

# 1范围

# IATIO

T/C\MIT04012的本部分规定子基于通信的列车运行控制（CBTC）1联 $1 \dot { \jmath } .$

试应包含的各个阶 行分配，并作为后续工联互通测试案例编写的依据对案例的编写具有指导作川。

# 2规范性引用文件

# 轨道

下列文件对于本部分的应用是必不可少的。凡注日期的引用文件，仅注日期的版本适用于本部分。凡不注日期的引用文件，其最新版本（包括所有修改单）适川于本部分。

GB/T12758—2004城市轨道交通信号系统通用技术条件

GB/T21562—2008轨道交通可靠性、可用性、可维护性和安全性规范及示例（IEC62278：2002，IDT）

GB/T22239—2008信息安全技术信息系统安全等级保护基本要求

GB/T28808—2012轨道交通通信、信号和处理系统控制和防护系统软件（IEC62279：2002，IDT）

GB/T28809—2012轨道交通通信、信号和处理系统信号用安全相

关电了系统（IEC62425：2007,IDT）

GB50157—2013地铁设计规范

CJ/T407—2012城市轨道交通基于通信的列车白动控制系统技术要求

T/CAMET04010.1城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范第1部分：系统总体要求

T/CAMET04010.3城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范第3部分：车载电子地图

T/CAMET04011.1城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第1部分：应答器报文

T/CAMET04011.2城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第2部分：CBTC系统车地连续通信协议

T/CAMET04011.3城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）与车辆的接口

T/CAMET04011.4城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第4部分：区域控制器（ZC）间接口

T/CAMET04011.5城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第5部分：计算机联锁（CI）间接口

T/CAMET04011.6城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第6部分：列车自动监控系统（ATS）间接口

T/CAMET04012.1城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范第1部分：CBTC部分测试及验证

EN50159:2010铁路应用通信、信号和处理系统信号的安全相 关的电子系统（Railway applications—Communication,Signaling and Processing System——Safety-related Communication in Transmission Systems)

IEEEStd1474.1-2004IEEE基于通信的列车控制（CBTC）系统的性能和功能要求（IEEEStandard forCommunications-Based TrainControl

(CBTC) Performance and Functional Requirements)

IEEEStd1474.4-2011IEEE基于通信的列车控制（CBTC）系统的系统功能测试推荐实践（IEEERecominendedPractice forFunctionalTesting of a Communications Based Train Control (CBTC) System)

# 3术语和缩略语

GB 50157——2013、CJ/T 407—2012、T/CAMET 04010.1以及T/CAMET04012.1界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1术语

3.1.1

基于通信的列车控制communication based train control(CBTC）

通过不依赖轨旁列车占用检测设备的列车主动定位技术，连续车一地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车白动控制系统。

[CJ/T407—2012，定义3.1.1]

# 3.1.2

正线 main line 载客列车运营的贯穿全程的线路。 [GB50157—2013，定义2.0.11]

3.1.3

列车自动控制automatic train control  
信号系统自动实现列车监控、安全防护和运行控制等技术的总称。[GB50157—2013，定义2.0.37]

3.1.4

列车自动监控automatic train supervision

根据列车时刻表为列车运行自动设定进路，指挥行车，实施列车运行管理等技术的总称。

[GB 50157—2013,定义2.0.38]

# 3.1.5

列车自动防护automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称：

[GB50157—2013，定义2.0.39]

3.1.6

列车自动运行automatic train operation

自动实现列车加速、调速、停年和车门开闭、提示等控制技术的总称。

[GB 50157—2013，定义2.0.40]

3.1.7

计算机联锁computer interlocking  
以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称.[CJ/T407——2012，定义3.1.6]

3.1.8

维护支持系统maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统口常运营维护。

[T/CAMET04010.1,术语3.1.8]

3.1.9

危险点danger point   
列车运行前方不允许列乍任何部位越过的特定点。 [T/CAMET04010.1，术语3.1.10]

3.1.10

移动授权movement authority   
列车沿给定的行驶方向进人并在某一特定轨道区段内行车的许可。 [CJ/T407—2012，定义3.1.7]

3.1.11

装备列车CBTC-equipped trains

装备了CBTC系统车载设备且设备处于工作状态的列车。

[T/CAMET04010.1，术语3.1.11]

3.1.12

非装备列车Non-CBTC-equipped trains

没有装备CBTC系统车载设备或者CBTC系统车载设备处于不T作状态的列车。

[T/CAMET04010.1,术语3.1.12]

3.1.13

转换轨 transfer track

指车辆段/停车场与正线的连接轨，运营列车在驶入/驶出转换轨过程中，当条件具备时，进行列车运行控制级别及驾驶模式转换。

[T/CAMET 04010.1术3Y139W

3.1.14

跨线运 overline pperation

运营列车在两条或两条以上制式相同或兼容的线路中，出一条线路进入另外一条线路进行共线运行的方式。 会

[T/CAMET 04010.A术语3.1.14]

3.1.15

平均故障间隔时间（平均洗间mean time between filures指设备连续发生两次故障之间的平均间隔时间。

[T/CAMET04012.1,术语3.1.15]

3.1.16

列车自动驾驶模式automatic train operating mode

在司机监控下，CBTC系统白动控制列车运行，并进行安全防护的列车驾驶模式。

[T/CAMET 04012.1,术语3.1.16]

3.1.17

列车自动防护模式coded train operating mode

在列车自动防护设备防护下，司机驾驶列车运行的列车驾驶模式。

[T/CAMET 04012.1,术语3.1.17]

3.1.18

限制人工驾驶模式restricted train operating mode

司机按规定的目视行车限速控车运行，列车自动防护设备进行超速防护的列车驾驶模式。

[T/CAMET 04012.1,术语3.1.18]

3.1.19

非限制人工驾驶模式emergency unrestricted train operating mode

ATP自动防护设备已被切除，车载设备不对列车运行进行监控，司机按操作规程驾驶列车的列车驾驶模式。

[T/CAMET 04012.1,术语3.1.19]

3.1.20

移交重叠区handover overlap region

为使列车在相邻区域控制器（ZC）间平滑移交，在ZC管辖范用交界处设置的用于列车移交控制的区域。

[T/CAMET04010.1,术语3.1.15]

3.1.21

互联互通interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1,术语3.1.16]

# 3.2缩略语

AM:列车自动驾驶模式（Automatic Train OperatingMode）  
ATC：列车自动控制（AutomaticTrainControl）  
ATO:列车自动运行（AutomaticTrainOperation）  
ATP:列车自动防护（AutomaticTrain Protection）  
ATS:列车自动监控(Automatic Train Supervision)  
BTM:应答器传输模块（BaliseTransferModule）  
CBTC：基于通信的列车控制（CommunicationBased TrainControl）

CI:计算机联锁（Computerized Interlocking）CTC:连续式等级(Continuous Train Control）DCS:数据通信系统（Data CommunicationSystem)ITC:点式运行级别（Intermittent TrainControl）LEU：轨旁电子单元（LinesideElectronicUnit）MSS:维护支持系统（Maintenance Support System)MTBF:平均故障问隔时间（Mean TimeBetween Failures)MTTR:平均修复时间(Mean Time To Repair)PIS:乘客信息系统(Passenger Information System)PSD:站台门(Platform Screen Door)RAMS：可靠性、可用性、可维修性和安全性（Reliability，Availability，Maintainability and Safety)SIL:安全完整性等级（Safety Integrity Level)TMS:列车管理系统（Train Management System)TSR :临时限速（Temporary Speed Restriction)UPS:不间断电源（Uninterruptible Power System）VOBC：车载控制器（VehicleOn-Board Controller）WCS:无线通信系统(Wireless Communication System)ZC:区域控制器（ZoneController）

# 4互联互通产品测试生命周期划分及验证活动

# 4.1测试阶段生命周期划分及验证活动

a）互联互通产品供应商测试及验证阶段。

本阶段的测试与验证任务由各互联互通产品供应商进行。各互联互通产品供应商需要按照互联互通技术规范的要求，对各子系统产品进行设计与实现，并对互联互通总体要求和功能分配中要求的互联互通功能进行测试与验证。

b）互联互通系统集成实验室测试及验证阶段。

本阶段的测试与验证任务由互联互通系统集成第三方验证机构进行。各互联互通系统集成供应商依据实验室测试环境要求提供被测系统，在专用的测试与验证平台进行测试与验证；对互联互通系统进行功能测试。实验室互联互通测试将按照子系统进行，互联互通点式功能测试将由VOBC、CI、ATS、应答器子系统4个部分构成。

c）互联互通系统集成试验线测试及验证阶段。

本阶段的测试与验证任务由互联互通系统第三方验证机构进行。各互联互通系统供应商依据试验线测试环境要求提供被测系统，在专用的试验线进行实车测试与验证；对于实验室验证与测试平台无法完全验证的功能进行测试与验证，试验线互联互通测试将按照子系统进行，互联互通点式功能测试将由VOBC、CI、ATS、应答器子系统4个部分构成。

# 4.2测试阶段内容及依据

互联互通测试及验证技术规范依据系统规范和接口规范文件编写，主要对系统规范和接门规范中的互联互通功能、接口等进行测试和验证，本规范对系统性能的测试和验证不做要求。

# 5测试环境

# 5.1互联互通系统供应商测试及验证平台需求

互联互通系统供应商测试及验证平台由各厂商门已搭建，并对各白系统进行测试和验证，保证系统的设计和实现满足互联互通要求，

# 5.2互联互通系统集成实验室测试及验证平台需求

# 5.2.1测试及验证平台设备构成

5.2.1.1实验室验证与测试平台需要由存在互联互通连接的2条实验线路的若干车站构成，可以在2条线路上采用不同厂家的互联互通系统，并验证2条线路之间的地面设备之间以及车地之间的互联互通跨线运行功能，且列车在正常的运营模式下通过跨线接口线路并在正线完成正常的互联互通功能。

5.2.1.2实验室验证平台测试环境的每条线路选取车站规模为2个控区5个车站，如图1所示

![](images/ecf2a260de92bd7cc997b1114dd3f424ad96f71b794808fa602b06c92dbfef60.jpg)  
图1互联互通实验线路构成示意图

# 5.2.2验证对象与信息流

实验室验证平台用 跨线点式互联互通接口及功能 M

a) 验证对象包   
互联互通系 5车载VOBC设备，  
互联互通系 关 充设备$1 1$   
互联互通系统-应答器系统设备（包括车载和轨旁设备）

()验证的内容包轨道交-T/CAMET04011.4中规定的接口内容；-T/CAMET04011.5中规定的接口内容；-T/CAMET04011.6中规定的接口内容；T/CAMET04011.3中规定的内容；T/CAMET04010.3中规定的内容；T/CAMET04011.2中规定的（VOBC与CI部分）内容；-T/CAMET04011.2中规定的（VOBC与ATS部分）内容。

# 5.2.3验证方法

在实验室验证平台搭建测试环境，通过仿真列车进行本线、跨线接口线路、其他互联互通线路上的点式运行测试，对互联互通功能进行验证。

# 5.3互联互通试验线测试及验证平台需求

# 5.3.1试验线设备构成

试验线完成CBTC系统的互联互通测试。试验线设备至少包括：

试验线路；  
试验列车；  
信号系统设备（ATP、ATO、ATS、联锁、DCS、应答器等）；  
信号系统无线通信网络及沿线接入点（LTE或Wi-Fi）。

# 5.3.2试验线条件要求

5.3.2.1为了满足在试验线路完成互联互通功能的验证和测试，试验线路选取应具备以下条件：

跨控区条件；  
站前/站后折返条件；  
设置区间信号机的长大区间（需要设置信号机的区间）。

5.3.2.2试验线应设置至少3个控区，5个车站以及4个区间；车站对应设置有站台门相关设备等。此外，试验列车应兼容互联互通产品供应商信号系统接口。

# 5.3.3验证方法

在试验线上，每个控区安装不同供应商的地面设备，利用安装不同供应商的车载信号设备，列车完成互联互通系统接口及功能的测试和验证，如图2所示。

![](images/068c71b2dd487a45fde77f5647809dacdfe98389cdd9485df3ca87449c6b26a7.jpg)  
图2互联互通试验线示意图

# 6测试需求

# 6.1互联互通系统测试验证活动的划分原则

6.1.1概述

6.1.1.1对CBTC互联互通系统进行验证首先要根据功能分配进行测10

试需求的划分，根据测试需求的可执行性，将测试需求划分为可测性需求和不可测需求，可测性需求可通过产品或系统测试的方式进行覆盖和验证，而不可测需求则需要针对具体的要求通过一定方式进行覆盖和验证。6.1.1.2对CBTC互联互通系统进行验证，根据测试验证的生命周期将其划分为3个阶段，分别为供应商测试与验证阶段、实验室平台测试与验证阶段，以及试验线测试与验证阶段。

# 6.1.2互联互通系统供应商测试及验证阶段

# 6.1.2.1互联互通产品供应商测试及验证阶段的工作内容

本阶段主要是对互联互通系统进行测试，主要工作是各供应商对自已的系统，按照互联互通标准的要求，进行与自已系统相关的全覆盖式测试。

# 6.1.2.2互联互通系统供应商测试及验证阶段的测试方法

6.1.2.2.1对于不具备可测性的需求，包括系统结构描述、物理接口等需求，只在本阶段进行覆盖，可参考各产品的设计文件以及相应的实验报告。

6.1.2.2.2对于可测试的需求，供应商依据互联互通系统需求编写对应的测试需求，采用功能测试的方法，对产品需求进行验证和覆盖。

# 6.1.3互联互通系统集成实验室平台测试及验证阶段

# 6.1.3.1互联互通系统集成实验室平台测试及验证阶段的工作内容

本阶段属于互联互通系统的集成测试的范围。主要工作为集成各供应商的被测设备，搭建专用的系统测试验证平台，对互联互通系统进行功能测试。系统测试验证平台为半实物的仿真测试平台，即部分设备为实物、部分设备为仿真。实验室测试验证平台测试阶段，对互联互通共线和跨线相关内容进行测试和验证，其中测试与验证的部分分为以下几个部分：

a) 与功能相关的测试内容，在此阶段进行测试，如点式功能、CBTC功能等；  
b) 与数据相关的测试内容，在此阶段进行测试，如遍历站台门数据、精确停车数据、列车折返数据等；  
c ) 与接口相关的测试内容，在此阶段进行测试，如与CI-CI接口、ZC-ZC接口、ATS-ATS接口、VOBC-ZC接口等。

# 6.1.3.2互联互通系统集成实验室平台验证与测试阶段的工作方法

本阶段主要测试日的是对可测性需求进行功能验证，采用黑盒测试的方法进行测试：

# 6.1.4互联互通试验线测试及验证阶段

# 6.1.4.1互联互通试验线测试及验证的工作内容

本阶段与实验室验证平台同属系统集成测试的范围。在试验线集成各系统供应商的被测设备，车辆在真实的线路上运行，所有互联互通设备均采用实物设备来进行测试和验证：实验室验证平台测试由于部分为仿真环境，诸如列车动力学模型、车辆、线路等等，对系统功能的验证，不能做到完全真实和充分，所以在试验线测试与验证阶段，结合运营方面的要求，测试和验证的内容分为以下几个部分：

a) 与设备安装相关的测试内容，在此阶段进行测试，如应答器定位、轮径校正等；  
b) ) 与车辆接口相关功能测试，在该阶段进行，如列车牵引、制动接口等；  
(:) 与线路相关的列车运行相关功能的测试内容，如车辆运行曲线、列车停车位置等；  
d) 与继电接口相关的功能，如联锁控制道岔、信号机等功能；  
e) 与网络环境相关的功能，如网路的稳定性等；  
f) 与运营相关的功能，如按照运行计划跑图功能等。

# 6.1.4.2互联互通试验线验证与测试的工作方法

完成了产品设计与实现的测试、室内验证平台测试、试验线测试后，可对CBTC互联互通系统进行全覆盖的测试和验证。根据系统测试验证活动的划分原则，对后续章节中的测试需求进行验证和测试的阶段划分。

# 6.2互联互通总体功能及接口功能分配

# 6.2.1互联互通系统架构和功能分配技术要求中功能分配

对总体要求定义的所有功能点（共73条）进行识别，按照T/CAMET04010.1功能分配的定义将其分配到各相关子系统，并根据其功能属性确定测试验证的阶段，详见表1。

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>于功能点描述</td><td rowspan=1 colspan=1>点式</td><td rowspan=1 colspan=1>连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=3 colspan=1>1</td><td rowspan=3 colspan=1>初始化CBTC列车位置</td><td rowspan=1 colspan=1>进人CBTC区域的CBTC列车位置初始化CBTC列车位置初始化，并自动检测每列符合装备CBTC设备的列车.进人CBTCK域无需手动输人列车位置或列车长度的</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>元成位初始化CBTC列车位车长度的数据</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>列车升级至CBTO车控制级别或联锁控制              续车控制级别时，应满足如下1)ATP车载设备无故障，且完成列车定位；2)ATP车载设备收到ATP轨旁设备发送的有效MA信息</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>确定CBTC列车位置</td><td rowspan=1 colspan=1>确定列乍长度CBTC应能确定列车长度</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td></tr></table>

表1功能分配表（一)（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">点式 连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="5">2</td><td colspan="1" rowspan="5">确定CBTC列车位置</td><td colspan="1" rowspan="1">确定CBTC列车位置CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">位置误差校正CBTC列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">列乍完整性检测CBTC系统应能实现列车的完整性检测 车载设备检测到列车完整性信息玉失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安企运行</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">列车轮径校正CBTC系统应能实现列车轮径校正功能，系统宜在列车进入转换轨前设置轮径自动补偿设备，并在出段/场前完成自动轮径补偿</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">确定列车停站位置：CBTC系统应根据不同的列车长度，确定列车的停站位置</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">确定CBTC列车位置</td><td colspan="1" rowspan="1">退行防护、ATP车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全问隔防护</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="2">3</td><td colspan="1" rowspan="2">确定轨道X段占用状态</td><td colspan="1" rowspan="1">轨道区段的占用状态：CBTC系统可根据轨旁次级占用检测设备提供的信息.结合CBTC列车汇报的位置信息，确定轨道区段的占用状态[有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车]</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">前方轨道区段占用状态，当CBTC列车前方区段被故障列车或者非CBTC 装备列车占用时，CBTC系统应根据前方区段占用状态确定CBTC列车的安全边界</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">防护列车丢失位置报告</td><td colspan="1" rowspan="1">防护列车丢失位置报告。当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">点式连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="2">5</td><td colspan="1" rowspan="2">防护列车完整性丢失</td><td colspan="1" rowspan="1">列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">—</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">列车完整性丢失防护。在检测到列车完整性丢失时，CBTC系统将提供移动授权防护，避免其他列车进人无位置汇报列车占用的区段</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">确定前方CBTC列车位置</td><td colspan="1" rowspan="1">CBTC列车前方位置。对于每辆CBTC列车，应确定列车前方的CBTC列车位置</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">确定前方安全进路限制</td><td colspan="1" rowspan="1">前方安全进路限制。对于每辆CBTC列车，系统应确定列车的安全进路位置</td><td colspan="1" rowspan="1">—</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">确定移动授权</td><td colspan="1" rowspan="1">列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="2">8</td><td colspan="1" rowspan="2">确定移动授权</td><td colspan="1" rowspan="1">列车升级至CBTC级别当系统由点式列年控制级别或联锁控制级别升级为连续式列乍控制级别时，应满足如下转换条件：1)ATP车载设备无故障，且完成2)ATP车载设备收到A有效MA信息</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">移动授权的确定动防护限制，CBTC    应估算最大移动授权限制位置</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">确定日标点</td><td colspan="1" rowspan="1">确定日标点  为权，CBTC系统应确</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">响应站台紧急关闭按钮</td><td colspan="1" rowspan="1">的荡响应站台紧息关闭按       ATP劳设备接收到站台紧急关息时，应通过车也通信设备向列车发送相应的列车控制命令信息</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">道岔状态防护</td><td colspan="1" rowspan="1">道岔状态防护CBTC系统应控制区域内道岔状态进行防护：当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶人丢失状态的道岔区域时，列车应实施紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">点式 连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">车载故障处理</td><td colspan="1" rowspan="1">故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范用的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="2">13</td><td colspan="1" rowspan="2">固定速度限制防护</td><td colspan="1" rowspan="1">固定线路速度限制CBTC应提供固定线路限速的限制防护</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">列车构造速度限制系统应提供列车构造速度的防护</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">/</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">临时限速限制防护</td><td colspan="1" rowspan="1">临时限制速度限制，CBTC 应按照系统设置的临时限速，为列车计算移动授权，对临时限速进行防护</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="3">15</td><td colspan="1" rowspan="3">确定制动曲线</td><td colspan="1" rowspan="1">目标点的制动曲线</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">考虑最不利情况下的影响，CBTC的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">防止制动曲线超过速度限制。CBTC 应保证制动曲线在超过固定或临时限速之前减速</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">列车超速防护</td><td colspan="1" rowspan="1">确定授权速度，CBTC 应基于ATP 曲线，确定列车当前位置的限制速度</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="3">16</td><td colspan="1" rowspan="3">列车超速防护</td><td colspan="1" rowspan="1">ATP曲线。CBTC应为每辆列车计算完整的ATP曲线</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">速度监督和防护。如果列车实际速度超过限制速度，CBTC 应实施紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">移动授权更新时的速度防护。移动授权更新时，如果列车的实际运行速度超过移动授权更新后的紧急制动触发速度，系统应实施紧急制动</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">列车速度测定</td><td colspan="1" rowspan="1">确定CBTC列车实际速度：CBTC应确定每辆CBTC 装备列车的实际速度，速度满足分辨率和精度的要求</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">测速误差补偿</td><td colspan="1" rowspan="1">测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">零速状态确定</td><td colspan="1" rowspan="1">零速状态确定。CBTC应确定零速度状态</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">列车运行方向确定</td><td colspan="1" rowspan="1">确定CBTC列车运行方向。CBTC 系统应确定每辆CBTC列车的实际运行方向</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr></table>

表1功能分配表(一)（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">列车运行方向防护</td><td colspan="1" rowspan="1">监怪/防护运行方向如果列车实际运行方向与授权的列车运行方向不一致，CBTC应实施紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">退行防护</td><td colspan="1" rowspan="1">退行防护ATP车载设备应具有退行防护功能，以满足列车定位的需求，当退行距离和退行速度超过允许值时，系统应立即采取紧急制动 在列乍退行过程中，系统应对追踪运行的列车提供安全间隔防护</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">越过移动授权终点防护</td><td colspan="1" rowspan="1">越过移动授权终点的响应 列车越过移动授权终点时，系统应实施紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">24</td><td colspan="1" rowspan="1">移动授权更新超时防护</td><td colspan="1" rowspan="1">移动授权更新超时的防护如果移动授权更新超时，系统应实施紧急制动</td><td colspan="1" rowspan="1">L</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="1">紧急制动缓解</td><td colspan="1" rowspan="1">紧急制动缓解在保证安全的条件下，系统可以缓解已施加的紧急制动</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">26</td><td colspan="1" rowspan="1">车门允诈</td><td colspan="1" rowspan="1">CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范周内2）开门侧与站台一致。3)列车零速                  中4）保持制动已施加。     国列车在车站规定的     准停     车载ATP应允许打开对      门及站车门及站台门，可    通过自        自人关、人开人关三种    ，自动或       打车门在AM驾驶     下，可损        开方式；CM驾驶模式            现应不允许车门和站台        司机     车设备防护条件下前进或后</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">27</td><td colspan="1" rowspan="1">站台门控制</td><td colspan="1" rowspan="1">站台门控制、CBTC在打开站台门之前，应检查是否满足下列条件：1）列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内2)站台门侧与车门侧-致3)列车零速4)保持制动已施加</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>子功能点描述</td><td rowspan=1 colspan=1>点式</td><td rowspan=1 colspan=1>连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=2 colspan=1>28</td><td rowspan=2 colspan=1>车门防护</td><td rowspan=1 colspan=1>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>车门状态丢失防护：列车在运行过程中，车载设备应实时监控列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引.也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=2 colspan=1>29</td><td rowspan=2 colspan=1>车门防护切除</td><td rowspan=1 colspan=1>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>车门操作切除。车辆可以提供单个车门切除功能，切除后的车门不响应列车开门命令</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>子功能点描述</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>点式连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=2 colspan=1>30</td><td rowspan=2 colspan=1>站台门防护</td><td rowspan=1 colspan=1>站台门锁闭状态防护仅在站台门处于“关闭且锁闭”状态时，系统方允许列车移动CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；已进站未停稳以及正在出站的列车应立即紧急制动；已完全出站的列车不受影响</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>站台门状态丢失的响应。当列车靠近车站或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>31</td><td rowspan=1 colspan=1>列车折返</td><td rowspan=1 colspan=1>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>车载ATP界面功能</td><td rowspan=1 colspan=1>CBTC车载ATP显示数据。CBTC 车载显示屏幕显示ATP数据应包括：1)列车运行模式；2)CBTC运行状态；3)当前列车速度；4）当前最大允许CBTC速度；5)超速报警</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td></tr></table>

表1功能分配表（一)（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">32</td><td colspan="1" rowspan="1">车载ATP界面功能</td><td colspan="1" rowspan="1">CBTC车载ATP 输入数据·用户ATP信息输人到CBTC应包括：1)运行模式选择；2)超速报警情况确认</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">33</td><td colspan="1" rowspan="1">ATP自诊断、故障报警及数据记录</td><td colspan="1" rowspan="1">自诊断、故障报警及数据记录ATP车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印 记录的内容包括事件的时间和日期，并至少保存7d，保存的数据可实现上传。并宜实现自动转存记录内容包括：设备运行状况、行乍里程、控制情况、驾驶模式、速度、列车日检数据</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">34</td><td colspan="1" rowspan="1">模式转换</td><td colspan="1" rowspan="1">列车驾驶模式列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RV）、非限制人工驾驶模式（EUM）列车自动运行模式（AM）、列乍自动防护模式（CM）为列车正常运行模式</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">34</td><td colspan="1" rowspan="1">模式转换</td><td colspan="1" rowspan="1">驾驶模式转换：列车驾驶模式等级由高至低分别为：AM、CM、RM、各驾驶模式满足转换条作可由人工转换，也可白动转换，车载设备应予以记录和显示。为保证停车。驾驶模式由低等列车宜不停车转换驾</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">35</td><td colspan="1" rowspan="1">ZC间移交</td><td colspan="1" rowspan="1">ZC切换。两条连交重叠列车进移交重叠区后，车载列车是否越过移交边界线路的轨旁ATP设备发送线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">36</td><td colspan="1" rowspan="1">电子地图存储</td><td colspan="1" rowspan="1">电子地图存储。CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>子功能点描述</td><td rowspan=1 colspan=1>点式</td><td rowspan=1 colspan=1>连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=1 colspan=1>37</td><td rowspan=1 colspan=1>停稳停准判断</td><td rowspan=1 colspan=1>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点。停止点偏差在允许范围内。2)开门侧与站台一致。3)列车零速..4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、白开人关、人开人关三种方式，白动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式。CM驾驶模式下，仅能实现人T开门.列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td><td rowspan=1 colspan=1>亚复测试点</td><td rowspan=1 colspan=1>重复测试点</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>38</td><td rowspan=1 colspan=1>确定ATO曲线</td><td rowspan=1 colspan=1>确定ATO曲线，CBTC系统应为列车确定ATO出线，ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制，ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>子功能点描述</td><td rowspan=1 colspan=1>点式</td><td rowspan=1 colspan=1>连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=1 colspan=1>39</td><td rowspan=1 colspan=1>精确停车</td><td rowspan=1 colspan=1>列车进站精确停车。ATO子系统应具备列车进站精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>根据ATO曲线调整列车速度</td><td rowspan=1 colspan=1>列车调速。CBTC系统应根据ATO曲线调整列车速度</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>41</td><td rowspan=1 colspan=1>跳停</td><td rowspan=1 colspan=1>ATO 能够响应ATS系统设置的跳停命令</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>42</td><td rowspan=1 colspan=1>运营调整</td><td rowspan=1 colspan=1>在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=4 colspan=1>43</td><td rowspan=4 colspan=1>开关车门</td><td rowspan=1 colspan=1>开列车门：在AM驾驶模式和ATP的防护下，可提供白动开门或者人工开门两种开门方式</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>开站台门。CBTC 系统应能自动开启站台门</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>关闭列车门。在AM驾驶模式下，可提供自动关门或者人工关门两种关门方式</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>关闭站台门：CBTC 系统应能自动关闭站台门</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">44</td><td colspan="1" rowspan="1">ATO界面显示</td><td colspan="1" rowspan="1">CBTC车载ATO显示数据在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td></tr><tr><td colspan="1" rowspan="1">45</td><td colspan="1" rowspan="1">ATO白诊断、故障报警及数据记录</td><td colspan="1" rowspan="1">白诊断、故障报警及数据记录：ATO子系统应具有白诊断功能，记求和分析故障报警信息，并能将报警信息传至中心ATS</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">46</td><td colspan="1" rowspan="1">ATO发送列车运行信息</td><td colspan="1" rowspan="1">ATO子系统向ATS子系统发送列车运行信息，以便 ATS 子系统能对在线列车进行监控</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">47</td><td colspan="1" rowspan="1">ATO发送旅客信息</td><td colspan="1" rowspan="1">车载旅客信息数据。ATO车载设备应向TMS 提供有关车载旅客信息的数据</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="2">48</td><td colspan="1" rowspan="2">确定列车识别号</td><td colspan="1" rowspan="1">CBTC 的运行列车识别号：每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车识别号：列车识别号应由列车号、车次号、车组号、目的地号组成</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车一地双向通信传输信息恢复</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">49</td><td colspan="1" rowspan="1">ATS列车追踪</td><td colspan="1" rowspan="1">ATS列车追踪：ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他的相关的信息并ATS用户界面上。运行时应具有车组</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="3">50</td><td colspan="1" rowspan="3">列车进路办理</td><td colspan="1" rowspan="1">列车进路办理      动。ATS系统应该具有列车自动办理进                系统依行信息站联锁表自动设置发        指挥在线列运行                            会</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">列车进路办理—人I、ATS系统应该具有手动办理进路的功能</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">列车进路办理—冲突检查、当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr></table>

表1功能分配表（一)（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="3">51</td><td colspan="1" rowspan="3">列车自动调整</td><td colspan="1" rowspan="1">自动调度。ATS系统可包括自动调度功能</td><td colspan="1" rowspan="1">—</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">列车时刻表/发车（运行)间隔调整，ATS系统可具有监视与自动调整的功能。</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">冲突自动调整：在CBTC列车位置报告的基础上，ATS系统应包括基于列车位置报告的列车自动调整功能，来处理列车冲突，以把整个系统的延迟减少到最小</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">52</td><td colspan="1" rowspan="1">节能运行</td><td colspan="1" rowspan="1">节能运行、ATS系统可具有通过实时控制及协调列车加速、列车滑行、列车制动米实施能源优化的功能</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">53</td><td colspan="1" rowspan="1">扣车</td><td colspan="1" rowspan="1">扣车，ATS系统应具有在车站扣车能力</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">54</td><td colspan="1" rowspan="1">提前发车</td><td colspan="1" rowspan="1">提前发车、ATS 系统应具有设置站台提前发车的功能</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">55</td><td colspan="1" rowspan="1">跳停</td><td colspan="1" rowspan="1">跳停车站：ATS系统应具有设置一个或多个装备CBTC的列车经过下一个或下几个车站而不停车的功能</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">56</td><td colspan="1" rowspan="1">设置/取消临时限速</td><td colspan="1" rowspan="1">临时限速、ATS系统应具有在CBTC区域内任何轨道区段，设置（与取消）临时限速的能力</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点措述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">57</td><td colspan="1" rowspan="1">时刻表编制管理</td><td colspan="1" rowspan="1">ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">58</td><td colspan="1" rowspan="1">模拟培训</td><td colspan="1" rowspan="1">ATS应具备模拟演示及培训系统，实现对调度员的培训</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="3">59</td><td colspan="1" rowspan="3">ATS界面功能</td><td colspan="1" rowspan="1">在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的日的</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">ATS 列车追踪ATS 系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表,及其他的相关的信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上，列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">ATS显示数据：CBTC的ATS显示应能够表示以下信息：1)精确的和区域相关的信息：2)列车状态相关信息；</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td></tr></table>

表1功能分配表（一）（续）  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="2">59</td><td colspan="1" rowspan="2">ATS界面功能</td><td colspan="1" rowspan="1">3)列车移动授权/进路信息；4)和被控列车运行相关的信息如防护区段信息，锁闭的进路/区段，以及临时限速极限和限速值；5)其他</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td></tr><tr><td colspan="1" rowspan="1">CBTC输入数据。CBTC的ATS用户界面显示应能够接收以下ATS用户输入：1)办理和取消进路输入；2)建立和取消防护区段，锁闭进路/区段，以及临时限速输入；3）其他</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">60</td><td colspan="1" rowspan="2">ATS数据记录</td><td colspan="1" rowspan="1">发送报数据，ATS子系统可将自身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">数据记录及回放系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程同放功能综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30d</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">61</td><td colspan="1" rowspan="1">中控/站控转换</td><td colspan="1" rowspan="1">在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号：列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或    控制CHINA时，人工控制优先于自动控</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="4">62</td><td colspan="1" rowspan="4">进路办理</td><td colspan="1" rowspan="1">列车进路办理有列车门动办理进路、车站联指挥在线列车运行</td><td colspan="1" rowspan="1">测点</td><td colspan="1" rowspan="1">重复试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">列车进路办理                   统应该具有手动办理进路的功</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">列车进路办理  冲突偏离计划，不同运行交路的列车经过同 地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">进路办理联锁应具备进路办理功能，包括人工办理列车进路、设置自动进路和白动折返进路、联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">功能点</td><td colspan="1" rowspan="1">子功能点描述</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">点式连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">62</td><td colspan="1" rowspan="1">进路办理</td><td colspan="1" rowspan="1">装有无效CBTC装备的列车进路办理。对于设备故障的CBTC列车或无装备的列车，在前方进路出清并重新开放后，装有无效 CBTC装备的列车方可驶入</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td></tr><tr><td colspan="1" rowspan="1">63</td><td colspan="1" rowspan="1">保护区段建立</td><td colspan="1" rowspan="1">保护区段。联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">64</td><td colspan="1" rowspan="1">进路/区段锁闭</td><td colspan="1" rowspan="1">进路/区段锁闭、系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行白动分段解锁</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">65</td><td colspan="1" rowspan="1">道岔单操、单锁</td><td colspan="1" rowspan="1">道岔单操、单锁：联锁具备道岔单独操纵及锁闭的能力</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">66</td><td colspan="1" rowspan="1">车站/区间封锁</td><td colspan="1" rowspan="1">封锁：系统应具有车站封锁、区间封锁的能力</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">67</td><td colspan="1" rowspan="1">站台紧急关闭按钮</td><td colspan="1" rowspan="1">响应站台紧急关闭按钮的按下，当ATP 轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">67</td><td colspan="1" rowspan="1">站台紧急关闭按钮</td><td colspan="1" rowspan="1">站台紧急关闭按钮联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="2">68</td><td colspan="1" rowspan="2">CI自检、故障报警及数据记录</td><td colspan="1" rowspan="1">故障监测．CI子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">监视和记录工作状态：CI子系统能监视和记录白身的下作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯丝状态监测及断丝报警，转辙机动作状态</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">69</td><td colspan="1" rowspan="1">进路解锁及取消</td><td colspan="1" rowspan="1">进路/区段锁闭：系统应具有锁闭（并随后解锁)CBTCX域内的道岔、信号机或轨道区段的能力，CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1">重复测试点</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">70</td><td colspan="1" rowspan="1">计轴故障恢复</td><td colspan="1" rowspan="1">计轴故障恢复，系统应具有计轴故障恢复的能力</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>功能点</td><td rowspan=1 colspan=1>子功能点描述</td><td rowspan=1 colspan=1>点式</td><td rowspan=1 colspan=1>连续式</td><td rowspan=1 colspan=1>设计与实现</td><td rowspan=1 colspan=1>室内平台</td><td rowspan=1 colspan=1>试验线</td></tr><tr><td rowspan=1 colspan=1>71</td><td rowspan=1 colspan=1>扣车</td><td rowspan=1 colspan=1>扣车。ATS 系统应具有在车站扣车的能力</td><td rowspan=1 colspan=1>重复测试点</td><td rowspan=1 colspan=1>重复测试点</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>72</td><td rowspan=1 colspan=1>站控/遥控</td><td rowspan=1 colspan=1>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td><td rowspan=1 colspan=1>重复测试点</td><td rowspan=1 colspan=1>重复测试点</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>73</td><td rowspan=1 colspan=1>CI权限设置</td><td rowspan=1 colspan=1>操作权限设置。CI子系统能设置不同操作人员的权限，并有相应的安全操作手段</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td></tr></table>

# 6.2.2互联互通应答器报文说明中功能分配

对T/CAMET04011.1中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表2。

表2互联互通应答器报文规范表  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">4.1.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">4.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">4.1.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">−</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">4.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">ATIO</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">−</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">4.1.5</td><td colspan="1" rowspan="1">SSO</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">4.1.6</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">4.1.7</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">4.2.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">4.2.2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">4.2.3</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">4.3.1.1</td><td colspan="1" rowspan="1">市</td><td colspan="1" rowspan="1">轨道</td><td colspan="1" rowspan="1">交</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">4.3.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">4.3.1.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">4.3.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">4.3.1.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">4.3.2.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">—</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">4.3.2.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">4.3.2.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">4.3.2.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">4.3.2.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">4.3.2.3.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">22</td><td colspan="1" rowspan="1">4.3.2.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">23</td><td colspan="1" rowspan="1">4.4.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

# 6.2.3互联互通CI-CI接口说明中功能分配

对T/CAMET04011.5中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表3。

表3互联互通计算机联锁（CI）间接口规范识别表  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">6.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">6.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">6.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">6.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">6.4.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6.4.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">6.4.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">6.4.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">6.4.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">6.4.6</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">6.4.7</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">6.4.8</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">6.4.9</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">6.4.10</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">6.4.11</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">6.4.12</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="7" rowspan="1">注1:“—”表示不适用；注2：“√”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8：表格中的章节号为T/CAMET04011.5中章节号。</td></tr></table>

# 6.2.4互联互通跨线ATS-ATS接口说明中功能分配

对T/CAMET04011.6中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表4。

表4互联互通ATS间接口规范识别表  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">6.1</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">/</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">6.2.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">6.2.2</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">6.2.3.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">6.2.3.2</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">/</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6.2.3.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">6.3.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">6.3.2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">6.3.3</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">6.3.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">6.3.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">6.3.3.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">6.3.3.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">6.3.3.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">6.3.3.6</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">6.3.3.7</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">6.3.3.8</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr></table>

注1:“—”表示不适用；

注2：“√”表示适用；

注3：“点式”表示在点式模式下测试；

注4：“连续式”表示在连续式模式下测试；

注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；

注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；

注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；

注8：表格中的章节号为T/CAMET04011.6中章节号。

# 6.2.5互联互通VOBC-ATS接口说明中功能分配

对T/CAMET04011.2中的VOBC与ATS接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，详见表5。

表5车地通信协议需求识别表  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="2" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">6.1.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">6.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">6.1.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">6.1.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">6.1.3.3</td><td colspan="1" rowspan="1">SSO</td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">6.1.4</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">6.2.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">6.2.2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">6.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">-</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">6.3.2.1.1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="2" rowspan="1"></td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">6.3.2.1.2</td><td colspan="1" rowspan="1">市</td><td colspan="1" rowspan="1">轨道</td><td colspan="2" rowspan="1">交</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">6.3.2.1.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">V</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">6.3.2.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">6.3.2.2.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">6.3.2.2.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">6.3.2.2.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">6.3.2.2.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">6.3.2.2.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">6.3.2.2.6</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">20</td><td colspan="1" rowspan="1">6.3.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="2" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="1">6.3.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="2" rowspan="1">√</td></tr></table>

# 6.2.6互联互通VOBC-CI接口说明中功能分配

对T/CAMET04011.2中的V0BC与CI接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，详见表6。

表6车地通信协议需求识别表  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">章节号</td><td colspan="1" rowspan="1">点式</td><td colspan="1" rowspan="1">连续式</td><td colspan="1" rowspan="1">设计与实现</td><td colspan="1" rowspan="1">室内平台</td><td colspan="1" rowspan="1">试验线</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">7.1.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">7.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">7.1.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">7.1.3.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">二</td><td colspan="1" rowspan="1">一</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">7.1.3.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">7.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">一</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">7.2.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">7.2.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1">7.3.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">7.3.2.1.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">二</td></tr><tr><td colspan="1" rowspan="1">11</td><td colspan="1" rowspan="1">7.3.2.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">12</td><td colspan="1" rowspan="1">7.3.2.1.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">13</td><td colspan="1" rowspan="1">7.3.2.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">14</td><td colspan="1" rowspan="1">7.3.2.1.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="1">7.3.3.1.1</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">16</td><td colspan="1" rowspan="1">7.3.3.1.2</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">17</td><td colspan="1" rowspan="1">7.3.3.1.3</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">18</td><td colspan="1" rowspan="1">7.3.3.1.4</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="1">7.3.3.1.5</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1">√</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="7" rowspan="1">注1：“—”表示不适用；注2：“√”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，山各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在联互通第三阶段测试，由各厂家提供互联互通产品在互联耳通试验线测试；注8：表格中的章节号为T/CAMET04011.2中章节号。</td></tr></table>

# 6.3互联互通测试需求

# 6.3.1定义测试需求的原则

定义测试需求应遵循以下原则。

a）可理解性

每一个测试需求应以易于理解的文字进行描述。对认证机构、用户、开发人员、测试人员而言，每一个测试需求都必须易于理解。在测试需求描述中，一些专业词汇要与文中术语、定义和缩略语中描述的内容一致，便于理解。

b）明确性

每一个测试需求必须具有唯一的编号。

c ) 等级适用性

必须标明每一个测试需求适用于的CBTC等级。因为每一个测试需求不一定适用于所有的运行等级。

d）可追溯性

所有测试需求应明确的指向某一个或多个功能点或接口需求。

# 6.3.2测试需求编号命名原则

为满足测试需求定义的各种原则，测试需求的命名应遵循以下原则。

a）包含功能点或接口编号

为便于追溯和理解，测试需求编号中需要包含功能点或接口编号。对于T/CAMET04010.1、T/CAMET04010.2因描述的是功能点，测试需求编号中体现功能点的编号，如“CBTC-F-ATP-1-ITC-1”。对于描述系统间接口的接口规范，如T/CAMET04011.1、T/CAMET04011.4等，测试需求编号中体现设备间接口,如“CBTC-IF-BALISE-MSG-ITC-1”或“CBTC-IF-CI/CI-MSG-ITC-1”。

# b）包含运行等级

为满足测试需求等级适用性的要求，测试需求编号中需要包含运行等级。点式部分以“ITC”进行描述。CBTC部分以“CTC”进行描述。

c）包含唯一标识的序号

为满足测试需求唯一性的要求，对每个功能点中的测试需求进行编号，从1开始，相同运行等级的，顺序号不可以重复（如删除后的编号将不再使用）。

# 6.4互联互通系统测试需求

# 6.4.1概述

6.2条中描述了T/CAMET04010.2中所有的互联互通相关的功能点，并对其进行了点式和连续式的划分。下面对点式部分的功能点进行测试和验证方法进行描述。

# 6.4.2初始化CBTC列车位置

初始化CBTC列车位置功能的测试和验证方法详见表7和表8。

# 表7初始化CBTC列车位置(一）

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">初始化CBTC列车位置</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-ATP-1-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">进入CBTC区域的CBTC列车位置初始化。CBTC列车位置初始化，并自动检测每列符合装备CBTC设备的列车，进入CBTC区域无需手动输入列车位置或列车长度的数据</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">装备CBTC设备、处于RM无位置报告模式的列车从非CBTC区域进人CBTC区域，经过具备定位条件两个连续应答器，系统自动获得列车位置和运行方向</td></tr><tr><td colspan="2" rowspan="1">注：表中功能内容是功能分配的原文描述（下同）。</td></tr></table>

# 表8初始化CBTC列车位置（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>初始化CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障中恢复的CBT      完成位置初始化。CBTC列装备CBTC设备的列无需手动输人列车位置车长度的数据</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>级别的列车，ATP故障，列      失定位，降级为RM定位条件的两个连续应答</td></tr></table>

# 6.4.3确定CBTC列车位置

确定CBTC列车位置功能的测试和验证方法详见表9～表19。

# 表9确定CBTC列车位置（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定列车长度。CBTC应能确定列车长度</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>与ATS建立连接的RM列车，向ATS报告列车长度</td></tr></table>

# 表10确定CBTC列车位置（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定列车长度。CBTC应能确定列车长度</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>与ATS建立连接的点式控制级别的列车，向ATS报告列车长度</td></tr></table>

# 表11确定CBTC列车位置（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定CBTC列车位置。CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>通过列车位置检测设备完成点式或RM列车的列车位置的安全和精确定位（包括列车的正反向运行）</td></tr></table>

表12确定CBTC列车位置（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>位置误差校正。CBTC列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC系统、处于RM控制级别的车载ATP设备，在向ATS汇报列车位置的同时，也汇报车载ATP系统考虑到安全因素而计算的位置不确定性（包括列车的正反向运行）</td></tr></table>

表13确定CBTC列车位置（五）  

<table><tr><td>功能名称</td><td>确定CBTC列车位置</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-2-ITC-5</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">位置误差校正。CBTC列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">1）车载ATP判断接收到的应答器报文有效的条件之一是应答器的位置在合理的范围之内；2）处于点式控制级别的车载ATP设备，在向ATS汇报列车位置的同时，也汇报车载ATP系统考虑到安全因素而计算的位置不确定性</td></tr></table>

表14确定CBTC列车位置（六）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列乍位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-6</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列乍完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)处于RM控制级别的车载ATP设备，检测到本车的完整性丢失，列车实施紧急制动，并丢失定位；2)列车位置丢失后，联锁和ATS按照物理区段占用进行显示。</td></tr></table>

表15确定CBTC列车位置（七）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">确定CBTC列车位置</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-ATP-2-ITC-7</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td></tr><tr><td>测试需求</td><td>1)处于点式控制级别的车载ATP设备，检测到本车的完 整性丢失，列车实施紧急制动，并丢失定位，降级为RM无 定位模式；</td></tr></table>

表16确定CBTC列车位置（八）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-8</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车轮径校正CBTC系统应能实现列车轮径校正功能，系统宜在列车进人转换轨前设置轮径门动补偿设备，并在出段/场前完成自动轮径补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式或RM列车执行从场段进入转换轨操作，列车将完成轮径的门动补偿（若具备该功能）</td></tr></table>

表17确定CBTC列车位置（儿）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定CBTC列车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-2-ITC-9</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定列车停站位置，CBTC系统应根据不同的列车长度，确定列车的停站位置</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备，处于点式控制等级的列车，在停站时，根据本身的编组和列车长度，以及电子地图中存储的针对不同的停车点位置，进行停车（包括正反向进站）</td></tr></table>

表18确定CBTC列车位置（十）  

<table><tr><td>功能名称</td><td>确定CBTC列车位置</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-2-ITC-10</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">退行防护、ATP车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">1）装备CBTC设备、处于RM控制级别，有位置报告的列车，当退行速度超过允许值时，列车紧急制动；2）装备CBTC设备、处于RM控制级别，有位置报告的列车，当退行距离超过允许值时，列车紧急制动</td></tr></table>

表19 确定CBTD列车位置（十一)  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>行防护。ATP车载设备厅       退行防护功能，以满足列车年定位的需求。当退行距离    行速度超过允许值时，退行过程中，系统应对</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>制级别的列车，当退行速2)装备CBTE        于点式控制级别的列车，当退行距离超过允许值时，列车紧急制动</td></tr></table>

# 6.4.4确定轨道区段占用状态

确定轨道区段占用状态功能的测试和验证方法详见表20和表21。

# 表20确定轨道区段占用状态（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定轨道区段占用状态</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-3-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和/或装有无效的CBTC车载设备的列车）</td></tr></table>

# 表20确定轨道区段占用状态（一）（续）

<table><tr><td>功能名称</td><td>确定轨道区段占用状态</td></tr><tr><td>测试需求</td><td>1）装备CBTC设备、无位置报告、处于RM控制级别的列 车占用某轨道区段； 2)轨旁次级占用检测设备检测到该轨道区段的占用信 息，发送给联锁，联锁将该信息发送给ATS设备进行显示</td></tr></table>

# 表21确定轨道区段占用状态（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定轨道区段占用状态</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-3-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>轨道区段的占川状态·CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和/或装有无效的CBTC车载设备的列车）</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制级别的列车占用某轨道区段；2)轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给ATS设备进行显示</td></tr></table>

# 6.4.5确定目标点

确定目标点功能的测试和验证方法详见表22。

表22确定目标点  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定目标点</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-9-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定日标点。为了确保列车不超过移动授权，CBTC系统应确定一个日标点</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制级别的列车不能越过点式移动授权中的进路的终点</td></tr></table>

# 6.4.6道岔状态防护

道岔状态防护功能的测试和验证方法详见表23。

表23道岔状态防护  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>道岔状态防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-11-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>道岔状态防护。CBTC系统应控制区域内道岔状态进行防护。当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制级别的列车，前方进路包含道岔且信号开放，点式移动授权延伸至进路内方；2)设置道岔状态丢失，验证始端信号机关闭；3）如果点式列车通过预告应答器接收到信号关闭信息，列车依据授权在信号机前正常停车；否则列车越过已关闭的信号机后紧急制动停车</td></tr></table>

# 6.4.7车载故障处理

车载故障处理功能的测试和验证方法详见表24\~表27。

表24车载故障处理（一)  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载故障处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-12-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制级别、有位置报告的列车，检测到本车的非预期移动，ATP设备会立即施加紧急制动，并给出报警提示</td></tr></table>

# 表25车载故障处理（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载故障处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-12-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制级别的列车，检测到本车的非预期移动，ATP设备会立即施加紧急制动，并给出报警提示</td></tr></table>

表26车载故障处理（三）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载故障处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-12-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障管理、列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制级别、有位置报告的列车，检测到车载设备故障，立即施加紧急制动，并给出报警提示</td></tr></table>

表27车载故障处理（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载故障处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-12-ITC4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制级别的列车，检测到车载设备故障，立即施加紧急制动，并给出报警提示</td></tr></table>

# 6.4.8固定速度限制防护

固定速度限制防护功能的测试和验证方法详见表28和表29。

表28固定速度限制防护（一）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>固定速度限制防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-13-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>固定线路速度限制。CBTC应提供固定线路限速的限制防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制级别的列车，在运行时，利用自已电子地图中存储的线路限速，计算速度曲线，对线路上的固定限速进行防护</td></tr></table>

表29固定速度限制防护（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车构造速度限制。                车构造速度的防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>利的列车，在运行时，计可运行的最高速度不大于列车自身的构造速度，验证超过列车的构造速度</td></tr></table>

# 6.4.9确定制动曲线

市

# 轨道

确定制动曲线功能的测试和验证方法详见表30\~表32。

# 表30确定制动曲线（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定制动曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-15-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>目标点的制动曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，经过主应答器或者预告应答器时，获得前方信号机的状态，计算目标点的制动曲线</td></tr></table>

# 表31确定制动曲线（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定制动曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-15-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>考虑最不利情况下的影响。CBTC的速度监/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，在计算速度曲线时，要考虑最差情况下系统偏差、反应次数和反应时间的补偿</td></tr></table>

表32确定制动曲线（三)  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定制动曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-15-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>防止制动曲线超过速度限制．CBTC应保证制动曲线在超过固定或临时限速之前减速</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级运行的列车，在经过固定限速区段，如道岔区段时，提前减速</td></tr></table>

# 6.4.10列车超速防护

列车超速防护功能的测试和验证方法详见表 $3 3 \sim$ 表36。

# 表33列车超速防护（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车超速防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-16-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定授权速度。CBTC应基于ATP曲线，确定列车当前位置的限制速度</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级运行的列车，根据点式移动授权和线路速度计算ATP曲线，并基于ATP曲线，确定列车当前位置的限制速度</td></tr></table>

表34列车超速防护（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车超速防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-16-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATP曲线。CBTC应为每辆列车计算完整的ATP曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级运行的列车，根据点式移动授权和线路计算ATP曲线，并基于ATP曲线，确定列车当前位置的限制速度</td></tr></table>

# 表35列车超速防护（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车超速防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-16-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>速度监和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级运行的列车，当列车实际运行速度超过限制速度时，实施紧急制动</td></tr></table>

表36列车超速防护（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车超速防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-16-ITC-4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>速度监和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级运行的列车，当列车实际运行速度超过RM限制速度时，实施紧急制动</td></tr></table>

# 6.4.11列车速度测定

列车速度测定功能的测试和验证方法详见表37和表38。

# 表37列车速度测定（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车速度测定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-17-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，利用测速测距功能测量并计算列车的实际速度，检查速度满足分辨率和精度的要求</td></tr></table>

# 表38列车速度测定（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车速度测定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-17-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，利用测速测距功能测量并计算列车的实际速度，检查速度满足分辨率和精度的要求</td></tr></table>

# 6.4.12测速误差补偿

测速误差补偿功能的测试和验证方法详见表39和表40。

# 表39测速误差补偿（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>测速误差补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-18-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，在空转打滑时，应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr></table>

表40测速误差补偿（二)  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>测速误差补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-18-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，在空转打滑时，应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr></table>

# 6.4.13 零速状态确定

零速状态确定功能的测试和验证为法详见表41和表42。

表41零速状态确定  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>E</td><td rowspan=1 colspan=1>零速状态确定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>+r$        P-19-ITC-1</td><td rowspan=1 colspan=1>化</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=2>速度状态</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=2>等级、行位置报告的列车，</td></tr></table>

表42零速状态确定（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>零速状态确定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-19-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>零速状态确定：CBTC应确定零速度状态</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级运行的列车，可以进行零速状态确认</td></tr></table>

# 6.4.14列车运行方向确定

列车运行方向确定功能的测试和验证方法详见表43和表44。

# 表43列车运行方向确定（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车运行方向确定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-20-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定CBTC列车运行方向。CBTC系统应确定每辆CBTC列车的实际运行方向</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1）装备CBTC设备、处于RM控制等级、有位置报告的列车，明确自已的运行方向；2)此时列车与联锁和ATS建立连接，ATP会将运行方向发送给联锁和ATS设备</td></tr></table>

表44列车运行方向确定（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车运行方向确定</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-20-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定CBTC列车运行方向CBTC系统应确定每辆CBTC列车的实际运行方向</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制等级的列年，明确门已的运行方向；2)此时列车与联锁和ATS建立连接，ATP会将运行方向发送给联锁和ATS设备</td></tr></table>

# 6.4.15越过移动授权终点防护

越过移动授权终点防护功能的测试和验证方法详见表45。

表45越过移动授权终点防护  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">越过移动授权终点防护</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-ATP-23-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">越过移动授权终点的响应。列车越过移动授权终点时，系统应实施紧急制动</td></tr><tr><td>测试需求</td><td>1)装备CBTC设备、处于点式控制等级的列车，越过移动 授权终点，系统实施紧急制动；</td></tr></table>

# 6.4.16移动授权更新超时防护（若有）

移动授权更新超时防护（若有）功能的测试和验证方法详见表46。

表46移动授权更新超时防护（若有）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>移动授权更新超时防护（若有）</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-24-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>移动授权更新超时的防护，移动授权更新超时，系统应实施紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制等级的列车，越过主信号应答器，且正确接收到点式移动授权；2)列车完全越过信号机后停车，且停车时间超过点式移动授权的有效时间，列车将施加紧急制动并提示降级</td></tr></table>

# 6.4.17紧急制动缓解

紧急制动缓解功能的测试和验证方法详见表47和表48。

# 表47紧急制动缓解(一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>紧急制动缓解</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-25-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>紧急制动缓解：在保证安金的条件下，系统可以缓解已施加的紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，因某种原因施加了紧急制动，如退行防护、设备故障等，在施加EB的触发条件消失且司机或调度员确认安全的情况下，可以缓解该紧急制动</td></tr></table>

# 表48紧急制动缓解（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>紧急制动缓解</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-25-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>紧急制动缓解。在保证安全的条件下，系统可以缓解已施加的紧急制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，因某种原因施加了紧急制动，如退行防护、设备故障等，在施加EB的触发条件消失且司机或调度员确认安全的情况下，可以缓解该紧急制动</td></tr></table>

# 6.4.18车门允许

车门允许功能的测试和验证方法详见表49～表53。

# 表49车门允许（—)

<table><tr><td>功能名称</td><td>车门允许</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-26-1TC-1 CBTC在开车门之前，应满足下列条件：</td></tr><tr><td>功能内容</td><td>1)列车“正确对齐”在一个指定的停止点，停止点偏差在 允许范周内； 2）开门侧与站台-致； 3)列车零速； 4)保持制动已施加， 列车在车站规定的位置停准停稳后，车载ATP应允许打 开对应侧车门及站台门或双侧车门及站台门、并可选择通 过自开自关、自开人关、人开人关三种方式，白动或者人工 打开车门。 在AM驾驶模式下，可提供三种开门方式，CM驾驶模式 下，仅能实现人工开门， 列车在车站停车超出停车窗范围，车载设备应不允许车 门和站台门打开，司机可在车载设备防护条件下前进或后</td></tr><tr><td>测试需求</td><td>1)停准在指定的停车点； 2)开门侧与站台一致； 3)列车零速；</td></tr></table>

表50车门允许（  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=2>车门</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CCBTC-F-ATP-26-HTC-2</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td></td><td></td></tr></table>

表50车门允许（二)（续）  

<table><tr><td>功能名称</td><td>车门允许</td></tr><tr><td>测试需求</td><td>件后，车载ATP允许打开对应侧车门和站台门或双侧车门 1）停准在指定的停车点，且在停车窗内； 2)开门侧与站台一致；</td></tr></table>

# 表51车门允许（三）

<table><tr><td>功能名称</td><td>乍门允许</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-26-ITC-3</td></tr><tr><td>功能内容</td><td>CBTC在开车门之前，应满足下列条件： 1）列车“正确对齐”在一个指定的停止点，停止点偏差在 允许范围内； 2)开门侧与站台一致； 3)列车零速； 4)保持制动已施加。. 列车在车站规定的位置停准停稳厅，车载ATP应允许打 开对应侧车门及站台门或双侧车门及站台门、并可选择通 过自开自关、自开人关、人开人关三种方式，自动或者人工 打开车门。 在AM驾驶模式下，可提供三种开门方式，CM驾驶模式 下，仅能实现人工开门。 列车在车站停车超出停车窗范围，车载设备应不允许车 门和站台门打开，司机可在车载设备防护条件下前进或后 退，直至停车对位</td></tr><tr><td>功能名称</td><td>车门允许</td></tr><tr><td>测试需求</td><td>车，确保满足以下条件后，车载ATP允许打开对应侧车门和</td></tr></table>

表52车门允许（四）  

<table><tr><td>功能名称</td><td>车门允许</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-26-ITC4 CBTC在开车门之前，应满足下列条件：</td></tr><tr><td>功能内容</td><td>1）列车“正确对齐”在一个指定的停止点，停止点偏差在 允许范围内； 2)开门侧与站台一致； 3)列车零速； 4)保持制动已施加 列车在车站规定的位置停准停稳后，车载ATP应允许打 开对应侧车门及站台门或双侧车门及站台门，并可选择通 过白开自关、自开人关、人开人关三种方式，自动或者人工 打开车门： 在AM驾驶模式下，可提供三种开门方式，CM驾驶模式 下，仅能实现人工开门。 列车在车站停车超出停车窗范围，车载设备应不允许车 门和站台门打开，司机可在车载设备防护条件下前进或后 退，直至停车对位</td></tr><tr><td>功能名称</td><td>车门允诈</td></tr><tr><td>测试需求</td><td>件后，车载ATP允许打开对应侧车门和站台门或双侧车</td></tr></table>

表53车门允许（五）  

<table><tr><td>功能名称</td><td>车门允许</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-26-ITC-5</td></tr><tr><td>功能内容</td><td>CBTC在开车门之前，应满足下列条件： 1)列车“正确对齐”在一个指定的停止点，停止点偏差在 允许范周内； 2）开门侧与站台一致； 3)列车零速； 4）保持制动已施加， 列车在车站规定的位置停准停稳后、车载ATP应允诈打 开对应侧车门及站台门或双侧车门及站台门，并可选择通 过白开自关、白开人关、人开人关三种方式，自动或者人工 打开车门。 在AM驾驶模式下，可提供三种开门方式，CM驾驶模式 下，仅能实现人工开门。 列车在车站停车超出停车窗范围，车载设备应不允许车 门和站台门打开，司机可在车载设备防护条件下前进或后 退，直至停车对位</td></tr><tr><td>测试需求</td><td>1）列车停准在指定的停车点，且在停车窗内；</td></tr></table>

# 6.4.19 点式开口功能

点式开口功能的测试和验证方法详见表5

![](images/425759d8de54ddcfd89ea7156751a88219fc55192fad425f0b053633a17df927.jpg)

表54点式开口功能  

<table><tr><td>功能名称</td><td>G 点式开口功能</td></tr><tr><td>测试需求编号</td><td></td></tr><tr><td>功能内容</td><td>功能</td></tr><tr><td>测试需求</td><td>停车，并可以通过开口确认</td></tr></table>

# 6.4.20点式红灯误出发防护功能

点式红灯误出发防护功能的测试和验证方法详见表55。

# 表55点式红灯误出发防护功能

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>点式红灯误出发防护功能</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-76-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>点式模式下，列车应具备点式红灯误出发防护功能</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>列车ITC-CM级别在站台出站信号前方停车，若前方信号为禁止信号，系统将不给出开口确认提示</td></tr></table>

# 6.4.21站台门控制

站台门控制功能的测试和验证方法详见表56和表57。

# 表56站台门控制（一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>站台门控制</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-27-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>站台门控制。CBTC应打开站台门之前，应检查是否满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3）列车尽速；4)保持制动已施加</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车、在下列条件满足时提供开门允许，并向联锁发送打开站台门的请求，打开站台门前，确认：1)列车停准在指定的停车点，且在停车商内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加：满足上述条件后，站台门打开</td></tr></table>

# 表57站台门控制（二）

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">站台门控制</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-ATP-27-ITC-2</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">站台门控制，CBTC应打开站台门之前，应检查下列条件满足：1）列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3)列车零速；4）保持制动已施加</td></tr><tr><td>测试需求</td><td>出现以下任一情况，则车载系统不向联锁发送开门命令。 1)列车不在停车窗内；</td></tr></table>

# 6.4.22车门防护

车门防护功能的测试和验证方法详见表 $5 8 \sim$ 表67

# 表58车门防护（一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护、仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级，有位置报告的列车，车门未被旁路且车门未处于“关闭且锁闭”状态，系统不允许列车移动</td></tr></table>

表59车门防护（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护：仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，车门被旁路且车门未处于“关闭且锁闭”状态时，列车可以移动</td></tr></table>

# 表60车门防护（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，车门处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

表61车门防护（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护，仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，车门未被旁路，且车门未处于“关闭且锁闭”状态，系统不允许列车移动</td></tr></table>

表62车门防护（五）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>年门防护。仪在车门处于“关闭且锁闭”状态时，系统方允许列乍移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，车门被旁路，且车门未处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

表63车门防护（六）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-ITC-6</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，车门处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

表64车门防护（七）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-1TC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门状态丢失防护。列车在运行过程当中，车载设备应实时监列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备处于RM控制等级、有位置报告的列车，路的情况下，监到车门打开，可以来列车运行至下一座车站；实施紧急制动；            S4 实施全常用制动</td></tr></table>

表65 车门防护（八  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>福                  防</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-VAT1-8-8交</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门状态丢失防护。列车在运行过程当中，车载设备应实时监列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级、有位置报告的列车，在运行过程中，车门被旁路的情况下，监督到车门打开，不会采取下列任一种措施：1）切除牵引但不实施制动；2）实施紧急制动；3）实施全常用制动</td></tr></table>

表66车门防护（九）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-28-1TC-9</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门状态丢失防护。列车在运行过程当巾，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制级别的列车，在运行过程中，车门未被旁路的情况下，监怪到车门打开，可以采取下列措施之：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列乍运行至下一座乍站；3）实施紧急制动；4）实施全常用制动</td></tr></table>

表67车门防护（十）  

<table><tr><td>功能名称</td><td>车门防护</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-28-ITC-10</td></tr><tr><td>功能内容</td><td>车门状态丢失防护。列车在运行过程当中，车载设备应 实时监怪列车车门状态，当检测到车门不为关门且锁闭状 态时，系统宜采取下列措施之一： 1）切除牵引但不实施制动； 2）不切除牵引，也不实施制动，列车运行至下一座车站； 3）实施紧急制动； 4）实施全常用制动</td></tr><tr><td>测试需求</td><td>装备CBTC设备、处于点式控制级别的列车，在运行过程 中，车门被旁路的情况下，监坚到车门打开，不会采取下列 任一种措施： 1）切除牵引但不实施制动； 2）实施紧急制动；</td></tr></table>

# 6.4.23车门防护切除

车门防护切除功能的测试和验证方法详见表68和表69。

# 表68车门防护切除（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护切除</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-29-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于RM控制等级、有位置报告的列车，车门故障时处于打开状态，司机操作使车门处于“车门切除”状态；2）列车可以移动</td></tr></table>

表69车门防护切除（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车门防护切除</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-29-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制等级的列车，车门故障时处于打开状态，司机操作使车门处于“车门切除”状态；2)列车可以移动</td></tr></table>

# 6.4.24站台门防护

站台门防护功能的测试和验证方法详见表70。

# 表70站台门防护

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>站台门防护</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-30-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>站台门状态丢失的响应。当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)装备CBTC设备、处于点式控制等级的列车，位于站台外，进站进路已排列并开放，此时站台门关闭状态丢失，验证进站进路始端信号机关闭；2)装备CBTC设备、处于点式控制等级的列车，位于站台内，出站进路已排列并开放，此时站台门关闭状态玉失，验证出站进路始端信号机关闭</td></tr></table>

# 6.4.25列车折返

列车折返功能的测试和验证方法详见表71\~表73。

# 表71列车折返（一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车折返</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-31-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车折返方式应包括ATO无人自动折返模式、ATO有人白动折返模式、ATP监督下的人T折返模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>ATP监督下的人T折返模式，站后折返：司机人T驾驶列车由站台运行至折返区域，完成相应的确认操作，自动切换列车首尾驾驶端，然后人工驾驶列车进入发车股道，定点停车后，打开车门和站台门</td></tr></table>

# 表72列车折返（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车折返</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-31-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监将下的人工折返模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>ATP监督下的人T折返模式，站前折返：当列车在折返站定点停车后，司机完成相应的确认操作，门动切换列车首尾驾驶端，在此过程中司机根据上下客站台的设置打开和关闭车门和站台门</td></tr></table>

# 表73C列车折返

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>C-F-ATP-31-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>动折返模式、ATO有人ATP监权监督下的人     返模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>监督下的人工折返模       ：列车在ATP监怪下的</td></tr></table>

# 6.4.26车载ATP界面功能轨道

![](images/7bdd1249b985c068a6caeacef65ee3fa20eb6d357889c35459db28f56422eb8c.jpg)

车载ATP界面功能的测试和验证方法详见表74\~表77。

# 表74车载ATP界面功能(—)

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">车载ATP界面功能</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-ATP-32-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CBTC车载ATP显示数据，CBTC车载显示屏幕显示ATP数据应包括：1）列车运行模式；2)CBTC运行状态；3)当前列车速度；4）当前最大允许CBTC速度；5)超速报警</td></tr><tr><td>要显示： 测试需求 5)超速报</td><td>装备CBTC设备、处于RM控制等级的列车，人机界面上 1）列车运行模式； 2)CBTC运行状态； 3）当前列车速度； 4）当前最大允许CBTC速度；</td></tr></table>

# 表75车载ATP界面功能（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载ATP界面功能</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-32-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC车载ATP显示数据。CBTC车载显示屏幕显示ATP数据应包括：1)列车运行模式；2)CBTC运行状态；3)当前列车速度；4）当前最大允许CBTC速度；5)超速报警</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，人机界面上要显示：1)列车运行模式；2)CBTC运行状态；3)当前列车速度；4）当前最大允许CBTC速度；5)超速报警</td></tr></table>

# 表76车载ATP界面功能（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载ATP界面功能</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-32-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC车载ATP输入数据。用户ATP信息输入到CBTC应包括：1)运行模式选择；2)超速报警情况确认</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于RM控制等级的列车，ATP设备的人机界面上支持的输人信息：1)运行模式选择；2)超速报警情况确认；</td></tr></table>

# 表77车载ATP界面功能（四）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载ATP界面功能</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-32-ITC4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC车载ATP输入数据。用户ATP信息输入到CBTC应包括：1)运行模式选择；2)超速报警情况确认</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备、处于点式控制等级的列车，ATP设备的人机界面上支持的输入信息：1)运行模式选择；2)超速报警情况确认</td></tr></table>

# 6.4.27ATP自诊断、故障报警及数据记录

ATP自诊断、故障报警及数据记录功能的测试和验证方法详见表78。

表78ATP自诊断、故障报警及数据记录  

<table><tr><td>功能名称</td><td>ATP白诊断、故障报警及数据记录</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATP-33-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">ATP自诊断、故障报警及数据记录</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">自诊断、故障报警及数据记录。ATP车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存7d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">装备CBTC设备的列车，需具备白诊断、故障报警及数据记录的功能：ATP车载设备具备门诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括非件的时间和口期，并至少保存7d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr></table>

# 6.4.28模式转换

模式转换功能的测试和验证方法详见表79\~表83。

# 表79模式转换（一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>模式转换</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-34-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车驾驶模式。列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车白动防护模式（CM）、限制人T驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）和列车白动防护模式（CM）为列车正常运行模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>装备CBTC设备的列车，列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM），列车自动运行模式（AM）和列车自动防护模式（CM）为列车正常运行模式</td></tr></table>

# 表80模式转换（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>模式转换</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-34-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>CM模</td></tr></table>

![](images/82c4e1751d5abc688b94cfff0b28ec2516b8c400fc16610664e250ede0f93b9e.jpg)

表81模式转换（三）  

<table><tr><td>功能名称</td><td>模示</td><td></td></tr><tr><td>测试需求编号</td><td></td><td rowspan="3"></td></tr><tr><td>功能内容</td><td>可自动转换，车载设备应予以记录和显示。为保证行车安</td></tr><tr><td>测试需求</td><td>允许报文，列车升级为点式列车，驾驶模式自动转换为 CM，同时验证了由低等级转为高等级时，不停车转换驾驶</td></tr></table>

表82模式转换（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>模式转换</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-34-ITC4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>驾驶模式的转换，AM、CM转为RM时：1)列车处于点式AM或CM模式，进入转换轨，速度低于预定值，ATP人机界面提示要转换为RM，停车后，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

表83模式转换(T）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>模式转换</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-34-ITC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>驾驶模式转换列车驾驶模式等级由高至低分别为：AM、CM、RM各驾驶模式满足转换条件可山人T转换，也可自动转换，车载设备应予以记录和显示为保证行车安全，列车驾驶模式山AM、CM转换为RM时，列车应停车驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>驾驶模式的转换，列车进入车辆段/停车场时，AM、CM转为RM时：1)列车处于点式AM或CM模式，进入进段转换轨，速度低于预定值，ATP人机界面提示要转换为RM，在不停车情况下，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

# 6.4.29电子地图存储

电子地图存储功能的测试和验证方法详见表84。

表84电子地图存储  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>电子地图存储</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-36-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>电子地图存储。CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>车载电子地图．装备CBTC系统的车载设备，应根据运行范用的不同，存储相关范同的电子地图，如在某条线路AL运行，则电子地图包含整条线路上的数据</td></tr></table>

# 6.4.30确定ATO曲线

确定ATO曲线功能的测试和验证方法详见表85。

# 表85确定ATO曲线

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>确定ATO曲线</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATO-38-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>确定ATO曲线。CBTC系统应为列车确定ATO曲线ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的白动驾驶、列车在区间运行的白动调整，并可实现列车的节能运行控制。ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在ATP系统的监督下，处于自动驾驶模式下的点式列车在线运行，系统自动计算ATO运行曲线，并控制列车按照ATO曲线运行，包括列车的加速、减速、惰行和巡航</td></tr></table>

# 6.4.31精确停车

精确停车功能的测试和验证方法详见表86。

表86精准停车  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>精确停车</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATO-39-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车进站精确停车。ATO子系统应具备列车进站精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)系统设置不同编组长度的列车；2)处于白动驾驶模式下的点式列车执行进站停车，并保证列车在指定位置精确停车</td></tr></table>

# 6.4.32根据AT0曲线调整列车速度

根据ATO曲线调整列车速度功能的测试和验证方法详见表87。

表87根据AT0曲线调整列车速度  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>根据ATO曲线调整列车速度</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-AT0-40-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车调速：CBTC系统应根据ATO曲线调整列车速度</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>处于自动驾驶模式下的点式列车作线运行，ATO系统依据列车运行信息，包括限速点、停车点等，控制列车速度，保证在正常运行</td></tr></table>

# 6.4.33开关车门

开关车门功能的测试和验证方法详见表88和表91。

# 表88开关车门(一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>开列车门</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATO-43-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>开列车门：在AM驾驶模式和ATP的防护下可提供自动开门或者人工开门两种开门方式</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>处于自动驾驶模式下的点式列车到站停稳停准后，依据门控模式等条件自动或人工开启列车车门</td></tr></table>

# 表89开关车门（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>开站台门</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATO-43-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>开站台门。CBTC系统应能自动开启站台门</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式列车到站停稳停准后，依据门控模式等条件自动发送开启站台门的联控命令</td></tr></table>

# 表90开关车门（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>关闭列车门</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>在AM          下，可提供白动关门或者</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>到站并执行完成在站作业后，依据门控模式等条件自动或人工关闭列车车门</td></tr></table>

表91开关车门（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>警                  闭站</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>关闭站台门：CBTC系统应能自动关闭站台门</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式列车到站并执行完成在站作业后，依据门控模式等条件自动发送关闭站台门的联控命令</td></tr></table>

# 6.4.34ATO界面显示

ATO界面显示功能的测试和验证方法详见表92。

表92AT0界面显示  

<table><tr><td>功能名称</td><td>ATO界面显示</td></tr><tr><td>测试需求编号</td><td>CBTC-F-AT0-44-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">ATO界而显示</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CBTC车载ATO显示数据：在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">点式列车运行过程中，车载人机界面上的显示对应内容（依据授权管理部门规定）</td></tr></table>

# 6.4.35AT0自诊断、故障报警及数据记录

ATO自诊断、故障报警及数据记录功能的测试和验证方法详见表93。

表93ATO自诊断、故障报警及数据记录  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATO自诊断、故障报警及数据记录</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-AT0-45-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自诊断、故障报及数据记录：ATO子系统应具行门诊断功能，记求和分析故障报警信息，并能将报警信息传至中心ATS</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>模拟ATO设备故障：在车载人机界面上显示相应的报信息，或者车载维护终端上对应相应的数据信息，此外，在ATS中心显示终端查询相关报警信息</td></tr></table>

# 6.4.36车载旅客信息数据

车载旅客信息数据功能的测试和验证方法详见表94。

表94车载旅客信息数据  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载旅客信息数据</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATO-47-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车载旅客信息数据。ATO车载设备应向TMS提供有关车载旅客信息的数据</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式或RM列车通过数据接口向列车TMS系统发送运营相关数据（若有）</td></tr></table>

# 6.4.37确定列车识别号

确定列车识别号功能的测试和验证方法详见表95和表96。

# 表95确定列车识别号（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>CBTC的运行列车识别号</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-48-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC的运行列车识别号．每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车识别号：列车识别号应由列车号、车次号、车组号、目的地号组成</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式或RM列车在线运行，ATS系统可实现对列车识别号的追踪，并可以通过ATS操作终端人工设置或修改列车号、车次号、车组号、门的地号</td></tr></table>

# 表96确定列车识别号（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车识别号丢失处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS48-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间白动推算并自动设置列车识别号，且能通过乍-地双向通信传输信息恢复</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式或RM列车在线运行，丢失识别号后，系统根据运行图、列车位置及时间自动推算并门动设置列车识别号</td></tr></table>

# 6.4.38 ATS列车追踪

ATS列车追踪功能的测试和验证方法详见表97。

表97ATS列车追踪  

<table><tr><td>功能名称</td><td>ATS列车追踪</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATS-49-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">ATS列车追踪。ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，以及其他的相关信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位咒报告来进行追踪并显示在ATS用户界面上，列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">1）点式或RM列车在线运行（包括跨线运行），ATS系统可以实现列车识别号的追踪功能，并在ATS中心或乍站操作终端观察列乍运行信息，包括位置、标识等2）点式或RM列车进出段运行，ATS系统可以实现列车识别号的追踪功能，在ATS中心或车站操作终端观察列车运行信息，包括车组号的跟踪、显示</td></tr></table>

# 6.4.39列车进路办理

列车进路办理功能的测试和验证方法详见表98～表100

# 表98列车进路办理（)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车进路办理——自动</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-50-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车进路办理—自动ATS系统应该具有列车自动办理进路的功能。ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在ATS车站或中心操作终端设置并确认进路具备自动进路功能（包括跨线进路），点式列车接近后自动触发前方进路</td></tr></table>

# 表99列车进路办理（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车进路办理-—人工</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-50-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>列车进路办理—人工。ATS系统应该具有手动办理进路的功能</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在ATS车站或中心操作的终端人T办理进路（包括跨线进路）</td></tr></table>

表100列车进路办理（三）  

<table><tr><td>功能名称</td><td colspan="2">川车进路办理 冲突检查</td></tr><tr><td>测试需求编号</td><td></td><td>列乍运行偏离计划，不</td></tr><tr><td>功能内容</td><td>计划冲突，并提示调度员采取列车计</td><td>系统应能检测到列车 划冲突干预方案</td></tr><tr><td>测试需求</td><td>运计划对冲突检查功能进行检查</td><td>的运行计划，并加载该</td></tr></table>

# 6.4.40时刻表编制管理

# 劲道

时刻表编制管理功能的测试和验证法详见表101。

表101时刻表编制管理  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>时刻表编制管理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-57-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>依据时刻表输入数据，在ATS时刻表编辑终端编制新的时刻表或对既有时刻表进行变更</td></tr></table>

# 6.4.41模拟培训

模拟培训功能的测试和验证方法详见表102。

表102模拟培训  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>模拟培训</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-58-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS应具备模拟演示及培训系统，实现对调度员的培训</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在ATS模拟系统上执行演示和培训内容</td></tr></table>

# 6.4.42 ATS界面功能

ATS界面功能的测试和验证方法详见表103和表104。

# 表103ATS界面功能（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATS显示数据</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-59-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS显示数据，CBTC的ATS显示应能够表示以下信息：1)精确的和区域机关的信息；2)列车状态相关信息；3)列车移动授权/进路信息；4）和被控列车运行相关的信息如防护区段信息，锁闭的进路/区段，以及临时限速极限和限速值；5）其他</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>点式或RM列车在线运行，在ATS中心或乍站操作终端显示列车运行位置、状态及相关的进路信息（包括保护区段、进路锁闭等)</td></tr></table>

# 表104ATS界面功能（二）

<table><tr><td>功能名称</td><td>CBTC输入数据</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATS-59-ITC-2</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CBTC输人数据。CBTC的ATS用户界面显示应能够接收以下ATS用户输入：1）办理和取消进路输入；2)建立和取消防护区段，锁闭进路/区段，以及临时限速输入；3）其他</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">点式列车在线运行，在ATS中心或车站操作终端进行进路的办理和取消（包括跨线进路）</td></tr></table>

# 6.4.43ATS数据记录

ATS数据记录功能的测试和验证方法详见表105和表106。

# 表105ATS数据记录（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>发送报警数据</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-60-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>发送报警数据，ATS子系统可将门身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在中心维护工作站、车站维护工作站以及维护中心的信号监测报警工作站上查询点式或RM列车相关运行信息，包括ATS子系统以及CI子系统报警信息</td></tr></table>

表106ATS数据记录（二）  

<table><tr><td>功能名称</td><td>数据记录及回放</td></tr><tr><td>测试需求编号</td><td>CBTC-F-ATS-60-ITC-2</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">数据记录及回放。系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能。综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30d</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">在ATS车站或中心操作终端或信号监测报警工作站进行30d前的数据的查询操作，包括操作信息以及设备运行状态等</td></tr></table>

# 6.4.44中控/站控转换

中控/站控转换功能的测试和验证方法详见表107。

# 表107中控/站控转换

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>站控/遥控</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATS-61-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>在紧急情况下，车站值班员可在挖制工作站上强行取得控制权，控制乍站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在ATS车站操作终端或中心操作终端通过申请和确认操作，进行站控和中心控的切换；2)在车站操作终端强制获取控制权；3）本地或中央自动控制模式时，进行人工进路的相关操作，确认人工控制优于白动控制</td></tr></table>

# 6.4.45进路办理

进路办理功能的测试和验证方法详见表108和表109。

表108进路办理（一)  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>进路办理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-62-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>进路办理。联锁应具备进路办理功能。包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)联锁支持人工排列并建立进路（包括跨线进路）功能；2)联锁支持为点式列车设置进路为自动进路模式功能</td></tr></table>

表109进路办理（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>aaSC装有元效TG装备的列车进路办理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>F-CI-62-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>办理、对于设备故障的  进路出清斥重新开放中装有CBTC装务备的列车驶入</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>博进路（包括跨线进路） 4列车通过进路，进路正常逐段解锁</td></tr></table>

# 6.4.46 保护区段控制

# 轨道

保护区段控制功能的测试和验证方法详见表110和表111。

表110保护区段控制（一）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>保护区段建立</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-63-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>保护区段，联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)CI终端办理进路（包括跨线进路），将触发保护区段并锁闭；2)点式或RM列车通过进路，进路逐段自动解锁</td></tr></table>

表111保护区段控制（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>保护区段解锁</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-63-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>点式或RM列车进站停稳后，保护区段应自动解锁（延时或立即）</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>驾驶ITC-CM列车在站台停车点处对位停车，列车停稳后，站台外方保护区段满足解锁条件后解锁</td></tr></table>

# 6.4.47进路/区段锁闭

进路/区段锁闭功能的测试和验证方法详见表112。

表112进路/区段锁闭  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>进路/区段锁闭</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-64-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>进路/区段锁闭、系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行白动分段解锁</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1）在CBTC区域内选取一条含有道岔的进路（包括跨线进路），排列并建立进路；2)取消已建立的进路，进路关闭并解锁；3)一点式或RM列车接近并完整通过开放的进路，进路将逐段顺序解锁</td></tr></table>

# 6.4.48道岔单操、单锁

道岔单操、单锁功能的测试和验证方法详见表113。

表113道岔单操、单锁  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">道岔单操、单锁</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-F-CI-65-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">道岔单操、单锁。联锁具备道岔单独操纵及锁闭的能力</td></tr><tr><td>测试需求</td><td>CI操作终端上执行道岔的单独锁闭、解锁及总定、总反操 作，操作可以正确执行</td></tr></table>

# 6.4.49车站/区间封锁

车站/区间封锁功能的测试和验证方法详见表114。

表114车站/区间锁闭  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车站/区间封锁</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-66-ITC-I</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>封锁．系统应具有车站封锁、区间封锁的能力</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)封锁进站信号或者站台股道区段后，不能建立进站的进路；2)封锁出站信号或者出站离去区段后，不能建立进入区间的进路（包括跨线区间)</td></tr></table>

# 6.4.50站台紧急关闭按钮

站台紧急关闭按钮功能的测试和验证方法详见表115。

表115站台紧急关闭按钮  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>站台紧急关闭按钮</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-67-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>站台紧急关闭按钮，联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在点式控车模式下，排列并建立进站进路，激活对应站台的站台紧急关闭按钮，联锁将关闭进站进路；2)在点式控车模式下，排列并建立出站进路，激活对应站台的站台紧急关闭按钮，联锁将关闭出站进路</td></tr></table>

# 6.4.51CI自检、故障报警及数据记录

CI自检、故障报警及数据记录功能的测试和验证方法详见表116和表117。

# 表116CI自检、故障报警及数据记录（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>故障监测</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-69-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>故障监测，CI子系统具有自检、白诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>设置设备报警条件（包括系统自身故障，信号机、转辙机等设备故障），在联锁维护终端界面显示相应的设备故障提示</td></tr></table>

# 表117CI自检、故障报警及数据记录（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>监视和记录工作状态</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-ATP-69-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>监视和记录工作状态。CI子系统能监视和记录自身的工作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯丝状态监测及断丝报警、转辙机动作状态</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在联锁维护终端显示设备工作状态，包括系统自动T作状态以及轨旁设备工作状态；2)在联锁维护终端界面获取并检查日志记录信息</td></tr></table>

# 6.4.52计轴故障恢复

计轴故障恢复功能的测试和验证方法详见表118。

表118计轴故障恢复  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>计轴故障恢复</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-F-CI-71-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>计轴故障恢复。系统应具有计轴故障恢复的能力</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)计轴预复位操作和列车完整通过完成计轴的复位（若具备）；2)计轴直接复位操作完成计轴的立即复位（若具备）</td></tr></table>

# 6.4.53 CI权限设置

CI权限设置功能的测试和验证方法详见表119。

# 表919CI权限设置

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>作权限设置。                   不同操作人员的权限，相应的安全操作码</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>通过口令进行登录和初始</td></tr></table>

# 轨道

# 6.5互联互通应答器接口需求

# 6.5.1概述

本章节的需求依据T/CAMET04011.1编写，文中所描述的章节号引用自T/CAMET04011.1。

# 6.5.2通信配置及控制功能

通信配置及控制功能的测试和验证方法详见表120～表129。

# 表120通信配置及控制功能（一）

<table><tr><td>功能名称</td><td>点式通信结构配置</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BALISE-MSG-ITC-1</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CBTC系统巾，车载ATP应通过车载BTM实现与应答器的通信。当列车经过地面应答器时，车载应答器天线激活地面应答器，并接收应答器循环发送的应答器报文</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

表121通信配置及控制功能（二）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>点式通信结构配置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC系统应通过车载BTM和应答器传输报文实现如下功能：1)建立列车定位；2)校正列车位置；3)传输点式移动授权；4）监控应答器通信状态</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1）列车定位功能测试需求：装备CBTC设备、RM控制等级、无位置报告的列车，经过两个连续具备定位条作的应答器，获得列车位置和方向，完成定位；2）校正列车位置，RM下测试需求：装备CBTC设备、RM控制等级、有位置报告的列车，在经过应答器前观察列车包络，经过应答器后，检查列车位置更新，包络缩小；3）校正列车位置，点式下测试需求：装备CBTC设备、点式控制等级、在经过应答器前观察列车包络，经过应答器后，检查列车位置更新，包络缩小；4）传输点式移动授权，RM下测试需求：装备CBTC设备、RM控制等级、有位置报告的列车，前方进路开放允许信号，列车经过主应答器，获得点式移动授权，升级为点式模式；5）传输点式移动授权，点式下测试需求：装备CBTC设备、点式控制等级，前方进路开放允许信号，列车经过主应答器，点式移动授权更新；6）监控应答器通信状态：当应答器故障时，车载ATP收不到应答器报文，当连续收不到应答器报文的应答器个数不超过系统设计值时，列车定位保持；超过系统设计值时，列车丢失定位</td></tr></table>

# 表122通信配置及控制功能（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>点式通信结构配置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC的点式后备系统或主用系统为点式的信号系统应满足T/CAMET04011.1章节5.1.3图1定义的结构。LEU可通过联锁设备或信号机点灯电路控制，如采用信号机点灯电路控制，应考虑是否能够满足线路拓扑要求</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表123通信配置及控制功能（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器功能分配</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CBTC的点式后备系统或主用系统为点式的信号系统基本功能分配如下：1）信号机由联锁设备控制；2)联锁或信号机点灯电路通过LEU控制有源应答器报文；3）年载设备通过应答器天线获取应答器信息，根据点式移动授权，生成制动曲线并进行相应的防护</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表124通信配置及控制功能（五）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器通信制式</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>地而应答器采用无线通信方式向车载应答器单方向循环传送报文</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表125通信配置及控制功能（六）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器类型及配置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-6</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>应答器按照报文是否可变，可分为无源应答器和有源应答器。其中无源应答器又称固定应答器，有源应答器可分为主应答器和填充应答器两种，周定应答器报文不可变，主应答器与填充应答器报文可变，主应答器布置在信号机处，填充应答器布置在主应答器外方，填充应答器与主应答器的距离宜保证列车不至降速时收到填充应答器报文，填充应答器与主应答器报文中信号状态和移动授权信息一致</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1．固定应答器测试需求：在线路上选择同定应答器，检查报文周定不变。2.填充应答器测试需求，在线路上选择填充应答器，检在内容如下：1)检查填充应答器布置企主应答器外方；2)填充应答器对应的主应答器的始端信号机开放允许信号，驾驶点式列乍经过填充应答器，检查列车不降速；3）填充应答器和主应签器报文一致；4)选择包含道岔的进路，检查道岔开往不同方向时，填充应答器的报文会发生变化.3.主应答器测试需求，在线路上选择主应答器，检查内容如下：1）主应答器布置在信号机处；2)选择包含道岔的进路，检查道岔开往不同方向时，主应答器的报文会发生变化</td></tr></table>

表126通信配置及控制功能（七）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器类型及配置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>在无点式后备模式时，系统只需要配置固定应答器</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表127通信配置及控制功能（八）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>物理接口</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-8</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>物理接口应满足如下要求：地面有源应答器应采用LEU进行编码，应采用专用电缆连接。车载应答器天线与BTM应通过专用馈缆连接</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表128通信配置及控制功能（元）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>类型及配置</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>面应答器与车载应答器天    的信息传输接口（也称应答器编码与解码应满足 应答器传输系统技术B/T3485)的要求     体</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见 商设计文件         场</td></tr></table>

表129通信配置及控制功能（十）  

<table><tr><td>功能名称</td><td>通信故障处理</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BALISE-MSG-ITC-10</td></tr><tr><td>功能内容</td><td>通信故障处理，应符合以下要求： 1）如遇BTM无法解码、应答器天线无法激活应答器、 传输错误等原因导致车载设备无法接收应答器报文，车 载设备应按照应答器丢失处理，应满足故障导向安全的 原则； 2）有源应答器与LEU通信故障时，应答器应发送应答器 默认报文（灭灯情况下也发送默认报文）；LEU与联锁通信 中断时，LEU向应答器发送LEU默认报文，并经应答器发送 至车载设备</td></tr><tr><td>测试需求</td><td>应答器报文的应答器个数超过系统设计值时，列车丢失</td></tr></table>

# 6.5.3报文标识及格式信息

报文标识及格式信息功能的测试和验证方法详见表 $1 3 0 \sim$ 表137。

# 表130报文识别及格式信息（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文长度要求</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-11</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>应答器报文采用830位长报文结构，用户信息包中不足的位以1补齐</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 表131报文识别及格式信息（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文结构定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-12</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>应答器报文结构定义详见T/CAMET04011.1章节5.3.1表1</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>因Q_UPDOWN、M_VERSION、Q_MEDIA、N_PIG、N_TOTAL、M_DUP在本协议中为定值，检查应答器报文中上述变量是否分别对应为1、0010000、0、000、000、00即可</td></tr></table>

表132报文识别及格式信息（三）  

<table><tr><td>功能名称</td><td>应答器报文结构定义——报文计数器</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BAlISE-MSG-ITC-13</td></tr><tr><td>功能内容</td><td>报文计数器对应变量名为M_MCOUNT，采用8位表示。 单个应答器会对应多条报文，本变量表示本报文在这些报 文中的序号固定应答器只包含一条报文，M_MCOUNT设 为255。有源应答器默认报文，M_MCOUNT设为252。LEU 默认报文，M_MCOUNT设为0M_MCOUNT值禁用253和 254 其他报文M_MCOUNT厂商自定</td></tr><tr><td>测试需求</td><td>检查固定应答器中M_MCOUNT=255</td></tr></table>

表133报文识别及格式信息（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文结构定义—报文计数器</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-14</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>报文计数器对应变量名为M_MCOUNT，采用8位表示，单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号，固定应答器具包含一条报文，M_MCOUNT设为255行源应答器默认报文，M_MC0UNT设为252LEU默认报文，M_MCOUNT设为0M_MCOUNT值禁用253和254.其他报文M_MCOUNT山厂商门定</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查行源应答器默认报文M_MCOUNT=252</td></tr></table>

表134报文识别及格式信息（五）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">应答器报文结构定义——报文计数器</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-BALISE-MSG-ITC-15</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">报文计数器对应变量名为M_MCOUNT，采用8位表示：单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号：周定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252：LEU默认报文，M_MCOUNT设为0.M_MCOUNT值禁用253和254：其他报文M_MCOUNT由厂商自定</td></tr><tr><td>测试需求</td><td>检查LEU默认报文M_MCOUNT=0</td></tr></table>

表135报文识别及格式信息（六）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文结构定义——报文计数器</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BAIISE-MSG-ITC-16</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>报文计数器对应变量名为M_MCOUNT，采用8位表示。单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号．同定应答器只包含一条报文，M_MCOUNT设为255行源应答器默认报文，M_MC0UNT设为252LEU默认报文，M_MCOUNT设为0M_MCOUNT值禁用253和254其他报文M_MCOUNT由厂商门定</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查有源应答器除有源应答器默认报文、LEU默认报文外其他的报文，M_MCOUNT数值参号厂商门定</td></tr></table>

# 表136报文识别及格式信息（七）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文结构定义——线路编号</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-17</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>线路编号对应变量名为NID_L，采用10位表示线路编号采川区域内统一编号的方式，可在区域线路规划时统·分配</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查应答器报文中NID_L等于线路编号</td></tr></table>

表137报文识别及格式信息（八）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应答器报文结构定义—应答器（组)编号</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-18</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>应答器（组）编号对应变量名为NID_BG，采用14位表示。用于在一条线路内，唯一识别的ID，由5位十进制数表示，最大值为16383</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查应答器报文中NID_BG等于应答器编号</td></tr></table>

# 6.5.4用户信息包

用户信息包功能的测试和验证方法详见表138～表149

# 表138用户信息包（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ETCS-44包定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-19</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>每个ETCS44包应只包含一个子包，一个应答器报文中可包含多个ETCS-44包，ETCS-44包定义详见T/CAMET04011.1节5.3.2.1表2</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>选择线路设计中有效方向分别为反向有效、正向有效、双向有                     金查Q_DIR中足否分别为00、OFM01</td></tr></table>

表139用户信息包（  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>202子但）</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=2>/CAMET04011.1节5.         3</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=2>检查报所管辖范围内的地图版本</td></tr></table>

表140用户信息包（三）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">公共信息包定义（203子包）</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-BALISE-MSG-ITC-21</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">公共信息包定义详见T/CAMET04011.1章节5.3.2.3表4</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">1）检查报文中NID_XUSER=203；2)C_CI_IEU的值：联锁与LEU通信正常该值取为O，联锁与LEU通信中断该值取为I；3）C_LEU_BALISE的值：检查LEU与应答器通信正常时该值取为0、LEU与应答器通信中断时该值取为1；</td></tr><tr><td>测试需求</td><td>SWITCH1,S_SWITCH1_STATE, NID_SWITCH2、S_SWITCH2</td></tr></table>

表141用户信息包（四）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">公共信息包——Q_SIGNAI_ASPECT取值</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-BALISE-MSG-ITC-22</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">公共信息包——QSIGNAL_ASPECT取值详见T/CAMET04011.1章节5.3.2.3表5黄灯序号的确认原则为：对于Q_SIGNAL_ASPECT中ABCDEFGHIJKLMNPOQ，从第3位（P）开始，每一位表示对向道岔（不包含顺向道岔）的状态，对向道岔定位为0，对向道岔反位为1，川最多表示15个对向道岔，不足15个对向道岔，为0．第Ⅰ位（Q）表示是否有保护区段，0表示无保护区段，1表示有保护区段，例如前方进路存在3个对向道岔，第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位，详见T/CAMET04011.1章节5.3.2.3表6由于道岔之前的走向关系，有可能出现黄灯序号不连续的情况</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">测试填充应答器：1)选择线路上任一条进路，分别办理进路始端信号机为红灯，引导、灭灯或故障情况下，检查Q_S1GNAL_ASPECT的值为1；2)选择线路上无保护区段的进路，主进路锁闭完整，始端信号机点亮绿灯，检查QSIGNAL_ASPECT的值为2；3）选择线路上有保护区段的进路，主进路和保护进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值为3；</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">公共信息包——Q_SIGNAL_ASPECT取值</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">4)选择线路上包含对向道岔最多的进路，检查Q_SIGNAL_ASPECT的取值满足要求：ABCDEFGHIJKLMNPOQ，从第3位(P)开始，每一位表示对向道岔（不包含顺向道岔）“的状态，对向道岔定位为0，对向道岔反位为1，可最多表示15个对向道岔，不足15个对向道岔为0。第1位（Q）表示是否有保护区段，0表示无保护区段，1表示有保护区段。第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位</td></tr><tr><td colspan="2" rowspan="1">区分对向道岔和顺向道岔的方式：1)从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔前区域，后搜索到该道岔的岔后区域，则该道岔为该方向上的对向道岔。2)从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔后区域，后搜索到该道岔的岔前区域，则该道岔为该方向上的顺向道岔，</td></tr></table>

表142用户信息包（五）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">Q_SIGNAL_ASPECT取值</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-BALISE-MSG-ITC-23</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">Q_SIGNAL_ASPECT所表示的范围为主应答器对应的信号机所防护的进路的情况（即使该主应答器兼具预告应答器功能，Q_SIGNAL_ASPECT也不报告前方预告进路的情况）。QSIGNAL_ASPECT所表示的道岔不包含保护区段的道岔</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">测试填充应答器：1)选择线路上任一条进路，分别办理进路始端信号机为红灯，引导、灭灯或故障情况下，检查Q_SIGNAL_ASPECT的值=1；2)选择线路上无保护区段的进路，主进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值=2；</td></tr><tr><td></td><td>4）选择线路上包含对向道岔最多的进路，检查Q_SIGNAL</td></tr></table>

表143用户信息包（六）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">公共信息包——Q_SIGNAL_ASPECT_PRE取值</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-BALISE-MSG-ITC-24</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">Q_SIGNAL_ASPECT_PRE 取值 : Q_SIGNAL_ASPECT_PRE的定义方式与Q_SIGNAL_APSECT完全相同，范围为兼预告的主应答器所预告的第二架信号机处开始至第二架信号防护的进路末端，如果Q_SIGNAL_APSECT为红灯，则Q–SIGNAL_ASPECT_PRE取值为0</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">测试填充应答器：1）选择线路上任条进路、分别办理进路始端信号机为红灯，引导、灭灯或故障情况下，检查Q_SIGNAL_ASPECT的值为1；2)选择线路上无保护区段的进路，主进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值为2；3)选择线路上有保护区段的进路，主进路和保护进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值为3；4)选择线路上包含对向道岔最多的进路，检查Q_SIGNAL_ASPECT的取值满足要求：ABCDEFGHIJKLMNPOQ，从第3</td></tr><tr><td>测试需求</td><td>位(P)开始，每一位表示对向道岔（不包含顺向道岔）的状态， 对向道岔定位为0，对向道岔反位为1，可最多表示15个对向 道岔，不足15个对向道岔为0。第1位（Q）表示是否有保护 区段，0表示无保护区段，1表示有保护区段。第1个对向道 岔反位，第2个对向道岔定位，第3个对向道岔反位</td></tr></table>

表144用户信息包（七）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">公共信息包一—D_DIS取值</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">取值。主应答器       终点距离，至多160km分辨率）。应的主应答器至MA终点距离。放置在保护区段的末点位于进路最后一个区段 则         应不越过车挡的末端：如果没有保护区段，则该距离填充至当前进路末端对于兼预告的主应答器，则该距离与预告进路是否开放相关如果预告进路未开放，则该距离遵从上述原则；如果预告进路开放，则该距离为兼预告主应答器至第二架信号机防护进路的终点的距离，保护区段处理方式相同默认报文中，D_DIS填0</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">测试填充应答器分以下几种情况：1）始端信号机开放的是允许信号，且进路有保护区段，DDIS为进路长度加保护区段长度（主信号应答器到MA终点）；</td></tr><tr><td>功能名称</td><td>公共信息包——D_DIS取值</td></tr><tr><td>测试需求 D_DIS为列车至当前进路末端的距离（主信号应答器到MA 终点）；</td><td>3)始端信号机开放的是允许信号，进路有车挡，D_DIS为 主信号应答器到车挡； 4)始端信号机为红灯，列车所占当前进路有保护区段，则 D_DIS为列车至保护区段末端的距离（主信号应答器到MA 终点）； 5）始端信号机为红灯，列车所占当前进路无保护区段，则</td></tr></table>

表145用户信息包（八）  

<table><tr><td>功能名称</td><td>公共信息包——D_DIS_OVERLAP取值</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BALISE-MSG-ITC-26</td></tr><tr><td>功能内容</td><td>D_DIS_OVERLAP取值。主应答器至进路保护区段起点 的距离，至多160km（1cm分辨率）。 如果该应答器为填充应答器，则该距离为填充应答器对 应的主应答器至主应答器对应的信号机防护进路末端的保 护区段起点距离。 如果进路无保护区段，D_DIS_OVERLAP填0。 默认报文中，D_DIS_OVERLAP填0。 对于兼预告的主应答器，则该距离与预告进路是否开放相 关。如果预告进路未开放，则该距离遵从上述原则；如果预 告进路开放，则该距离为兼预告主应答器至第二架信号机防 护进路末端的保护区段起点距离，保护区段处理方式相同</td></tr><tr><td>测试需求</td><td>2)始端信号机开放的是允许信号，进路无保护区段，D_ 3)始端信号机为红灯，列车所占当前进路有保护区段，则</td></tr></table>

表146用户信息包（儿）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>公共信息包——NID_SWITCH取值</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSG-ITC-27</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>NID_SWITCH取值，线路内统一编号，且唯-一</td></tr><tr><td rowspan=1 colspan=1>验证阶段</td><td rowspan=1 colspan=1>产品设计与实现、验证平台测试</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查进路中道岔编号NID_SWITCH是否存在</td></tr></table>

表147用户信息包（十)  

<table><tr><td>功能名称</td><td>公共信息包——N_SWITCH 取值</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BALISE-MSG-ITC-28</td></tr><tr><td>功能内容</td><td>于15，该包根据不同的道岔数量是变长的。道岔数量不足15</td></tr><tr><td>测试需求</td><td>段包含多个道岔的场景，检查N_SWITCH的值等于进路中 道岔的数量加保护区段中道岔的数量； 2）进路无保护区段，检查N_SWITCH的值等于进路中道</td></tr></table>

表148用户信息包（十一）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>自定义包定义（204子包）</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-BALISE-MSC-ITC-29</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>白定义包定义详见T/CAMET04011.1章节5.3.3表7和表8</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>检查NID_XUSER=204，NID_PROVIDER为厂商标识，DRESERVED为厂商自定义内容及格式</td></tr></table>

表149用户信息包（十二）  

<table><tr><td>功能名称</td><td>应答器发包原则</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-BALISE-MSG-ITC-30</td></tr><tr><td>功能内容</td><td>应答器发包原则详见T/CAMET04011.1章节5.4表9</td></tr><tr><td>测试需求</td><td>I)选择无源应答器，ETCS44包中只包含地图版本信息 包，即202子包； 2)选择有源应答器，亮灯时有源应答器发送地图版本信 息包（202子包）、公共信息包（203子包）、厂商自定义信息 包（204子包，可选）、城市自定义信息包（205子包，可选）； 3)选择有源应答器，有源应答器与LEU通信中断，地图 版本信息包（202子包）、公共信息包（203子包），C_LEU_</td></tr><tr><td>测试需求</td><td>BALISE为1; 4)选择有源应答器，联锁与LEU通信中断，地图版本信息</td></tr></table>

# 6.6互联互通计算机联锁（CI）间接口测试需求

# 6.6.1 CI与CI接口概述

CI与CI接口概述功能的测试和验证方法详见表150。

<table><tr><td rowspan=1 colspan=2>表150  CI与CI接口概述</td></tr><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>与CI子系统的接口是基   SSP-Ⅰ协议，通过双冗余网通信</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>各厂商设计文件           体</td></tr></table>

# 6.6.2通信层次描述

通信层次描述功能的测试和验证直法详见表151。

表151通信层次描述  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信层次描述</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-2</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>T/CAMET04011.5章节5.2.1图2为CI与相邻CI通信的通信协议模型，CI间层次结构详见T/CAMET04011.5章节5.2.3图3</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.3物理层描述

物理层描述功能的测试和验证方法详见表152。

表152物理层描述  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>物理层描述</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/C1-MSG-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何—个单网的故障都不会对系统的正常使用产生影响：两系统按照A网和A网相连，B网和B网相连接的方式，其连接方式详见T/CAMET04011.5节5.1.1图1</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>测试功能内容：CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A[网和B网）以提高系统的可靠性，任何一·个单网的故障都不会对系统的正常使用产生影响，对应测试需求：1）相邻CI间通过A网连接，B网中断，验证可以正常办理进路，操作道岔等；2)相邻（I间通过A网中断，B网连接，验证可以正常办理进路，操作道岔等；3）相邻CI间AB网同时连接，办理进路的同时（进路满足办理条件），断开任-网络，验证进路办理成功.该功能内容中描述的其他内容的验证通过产品设计米覆盖</td></tr></table>

# 6.6.4数据链路层描述

数据链路层描述功能的测试和验证方法详见表153。

表153数据链路层描述  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>数据链路层</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>MAC(Medium Access Control）子层基于 IEEE 802.3标准MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.5络层描述

网络层描述功能的测试和验证方法详见表154。

表154网络层描述  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>网络层</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>本接口使用IPv4协议作为网络层的协议</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.6传输层

传输层功能的测试和验证方法详见表155。

表155传输层  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>传输层</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-6</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>本接口使用UDP/IP协议作为传输协议</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.7安全通信协议层

安全通信协议层功能的测试和验证方法详见表156。

# 表156安全通信协议层

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>安全通信协议层</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>采用RSSP-I标准协议，同时通过序列号对冗余网络数据进行过滤，不作为本文档描述</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.8应用层

应用层功能的测试和验证方法详见表157。

# 表157应用层

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应用层</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-CI/CI-MSG-ITC-8</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>应用层遵守T/CAMET04011.5规定的协议，详见CI-CI间接口描述</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.6.9动态交互描述

动态交互描述功能的测试和验证方法详见表158

表158动态交互描述  

<table><tr><td>功能名称</td><td>动态交描述</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-CI/CI-MSG-ITC-9</td></tr><tr><td>功能内容</td><td>CI以300ms（周期根据各厂商配置）为周期向相邻的CI 发送信息 CI认为与邻站CI通信中断的超时时间定义为TCiTimeout （可配置，推荐值5s） G没有接收到米自邻站CI的作何消息达到或超过 TCiTimeOut超时时间定义的时间窗Ⅱ，则CI应认为与邻站 CI通信中断（指应川层根据GAL包头中字段进行判断，而 非安全通信协议层进行的判断）；若CI判断接收到邻站CI 的应川信息延迟已经达到TCiTimeOut时，CI应认为与邻站 CI通信中断（指应用层根据GAL包头中字段进行判断，而 非安全通信协议层进行的判断） CI与邻站CI间通信中断的情况下，本站CI无法收到邻 站汇报的设备信息．CI应将邻站所有设备状态设置为安全 侧.如将通往邻站进路的始端信号机置为禁止信号，对应来 自邻站的区段设置为占用：CI与邻站CI间通信中断的情况 下，若本站CI收到了合法的邻站CI信息，则本站CI应认为 与邻站CI连接恢复： 互联互通线网中，CI与邻站CI的通信超时时间应一致， 消息有效期时间应一致。</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">动态交互描述</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CI与邻站CI间通信中断的情况下，若本站CI收到了合法的邻站CI信息，则本站CI应认为与邻站CI连接恢复</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">断开相邻CI间通信，验证3个通信周期后，相邻CI认为通信中断</td></tr></table>

# 6.6.10通信故障处理

通信故障处理功能的测试和验证方法详见表159。

表159通信故障处理  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>站汇报的设备信息，CI将邻邦站所有设备状态设置为安      置为0），如将通往邻对应来自邻站的区段</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>CI子系统认为通信中断，并有相应的报提查2)设备状态         侧，设备包含：道岔（四开）、逻辑区段（占川）、物理区段（占用）、信号机（关闭）、站台门（开启且末旁路）、紧停按钮（按下）、照查（照查不满足）、进路（接近锁闭）、保护区段（未请求）、联锁系统（上电锁闭）</td></tr></table>

# 6.6.11CI间通信通用报文

CI间通信通用报文功能的测试和验证方法详见表160。

# 表160CI间通信通用报文

<table><tr><td>功能名称</td><td>CI间通信通用报文</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-CI/CI-MSG-ITC-11</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CI间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL消息包中包含CI间传输的各条应用信息，每个GAL消息包总长不得超过1000字节。信息包格式定义详见T/CAMET040I1.5章节5.3.1.2的表1和表2</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

# 6.6.12 CI与CI接口描述

CI与CI接口描述功能的测试和验证方法详见表161。

# 表161CI与CI接口描述

<table><tr><td>功能名称</td><td>CI与CI接描述</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-CI/CI-MSG-ITC-12 1)CI间通信的所有应用信息类型及其含义、发送方向、长</td></tr><tr><td>功能内容</td><td>度范围、发送方式（周期/非周期）的内容详见T/CAMET 04011.5章节5.3.2的表3； 2）本CI应将互联互通相关范围内的本联锁管辖范围的 道岔状态发送给邻站CI．相邻CI间道岔索引顺序应保持 一致，详见T/CAMET04011.5章节5.4.1的表4； 3）本CI应将互联互通相关范围内的本联锁区管辖范围 内的物理区段状态发送给邻站CI。相邻CI间物理区段索 引顺序应保持一致，详见T/CAMET04011.5章节5.4.2的 表5； 4）本CI应将互联互通相关范围内的本联锁区管辖范围 的逻辑区段状态发送给邻站CI，相邻CI间逻辑区段索引 顺序应保持一致，详见T/CAMET04011.5章节5.4.3的 表6； 5）本CI应将互联互通相关范围内的本联锁区管辖范围 内的信号机状态发送给邻站CI，联锁分界点处信号机属于</td></tr><tr><td>功能名称</td><td>CI与CI接口描述</td></tr><tr><td>功能内容</td><td>序应保持一致，详见T/CAMET04011.5章节5.4.5的表8； 7)本CI将互联互通相关范围内的本联锁区管辖范围的 站台紧急关闭信息发送给邻站CI：相邻CI间站台紧急关 闭索引顺序应保持一致，详见T/CAMET04011.5章节</td></tr><tr><td>测试需求</td><td>1）分别对道岔做引导总锁、单锁、封锁、单操定位、单操反 位、道岔四开的操作，验证临站联锁显示同本站联锁一致； 并验证未对道岔做任何设置时，临站联锁显示同本站联锁</td></tr></table>

# 表161CI与CI接口描述(续）

<table><tr><td>功能名称</td><td>CI与CI接口描述</td></tr><tr><td>测试需求</td><td>联锁显示与本站联锁显示·致； 4）操作信号机使其状态分别为红灯、黄灯、绿灯、红黄灯、 灯丝断丝、封锁、末封锁、验证临站联锁显示同本站联锁</td></tr></table>

# 6.7互联互通跨线ATS间接口测试需求

# 6.7.1 ATS与ATS通信机制

ATS与ATS通信机制功能的测试和验证方法详见表162。

# 表162ATS与ATS通信机制

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信机制</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>1)相邻ATS间通信采用周期与非周期发送的方式进行通信。2)通信双方均采用大端字节序进行数据传输</td></tr><tr><td rowspan=1 colspan=1>测试雷求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.7.2 ATS与ATS接口概述

ATS与ATS接描述功能的测试和验证法详见表163。

# 表163VATS与ATS接口

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>&#x27;SS间通信层次结构划分详      CAMET04011.6章节图1。物理层采用IEEE80     标准协议，数据链路层采川IPV4协议，传输层协议，应用层见       ET04011.6章节5.2.3</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1></td></tr></table>

# 6.7.3物理接口

物理接口功能的测试和验证方法详见表164。

# 表164物理接口

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>物理接1</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS通过RJ45接口冗余接入通信网络，网络拓扑结构为A网-A网，B网-B网，接口间宜通过防火墙进行隔离</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.7.4通信层次描述

通信层次描述功能的测试和验证方法详见表165。

# 表165通信层次描述

<table><tr><td>功能名称</td><td>通信层次描述</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-ATS/ATS-MSG-ITC4 ATS与ATS间建立对等的逻辑连接，详见T/CAMET</td></tr><tr><td>功能内容</td><td>04011.6章节5.2.2.2图2（箭头指向表示服务端，双线表示 双网逻辑连接）： 1)第--组通道，线路一ATS的主机作为客户端同时与线 路二ATS的主机和备机建立双网连接，用于传送本线路内 产生的信息。 2)第二组通道，线路二ATS的主机作为客户端同时与线 路一ATS的主机和备机建立双网连接，用于传送本线路内 产生的信息。</td></tr><tr><td>测试需求</td><td>服务端侦听端口为9900 见各厂商设计文件</td></tr></table>

# 6.7.5信息帧格式定义

信息帧格式定义功能的测试和验证方法详见表166。

表166信息帧格式定义  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>信息帧格式定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>相邻ATS间每个周期需要交互的信息通过组成通用（GAL）消息包（以下简称GAL包），进行传输，详见T/CAMET04011.6章节5.2.2.3图3</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.7.6信息包格式定义

信息包格式定义功能的测试和验证方法详见表167～表171。

# 表167信息包格式定义（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>信息包格式定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-6</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS间通信的GAL包中包含ATS间传输的各条应用信息，每个GAL消息包总长不得超过65000字节，每个GAL只包含一类应用数据。GAL包格式定义详见T/CAMET04011.6章节5.2.2.3.2表1和表2</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 表168信息包格式定义（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信状态管理  一合法性检查</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站ATS的应用信息，并记录报警信息。具体检查方式如下：消息内容的一致性检查包括：信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。通用应用（GAL）信息包消息所应包含的信息的完整性。其他逻辑检查</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表169信息包格式定义（三）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">通信状态管理一 超时检查</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-1F-ATS/ATS-MSG-ITC-8</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">ATS和VOBC应能分别对通信连接状态进行判断：ATS认为与邻站ATS通信中断的超时时间定义为TATSTimeout(3s~9s,可配置）。若ATS在TATSTimeout超时时间内，没有接收到来自邻站ATS的任何消息，则ATS应认为与邻站ATS通信中断。</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">通信状态管理——超时检查</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">若ATS判断接收到邻站ATS的周期性应用信息延迟已经达到TATSTimeout时，ATS可丢弃此信息包，ATS应认为与邻站ATS通信中断或发生丢包。通信中断的情况下，应生成报警信息。连接断开时立即重连.联互通线网中，各厂商的ATS间的通信超时时间应一致，消息有效期时间应一致</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">断开相邻ATS与ATS间通信，并超过系统定义的TATSTimeout，ATS系统判断为与相邻ATS通信超时；断开ATS和相邻ATS主机之间的通信连接持续一段时间未恢复，进行倒机切换；断开ATS与相邻ATS备机与备机之间的通信连接，只报而不倒机；断开ATS与相邻ATS主机与备机之间的通信连接，只报而不倒机</td></tr></table>

表170信息包格式定义（四）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>数据类型定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-9</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.6章节5.2.3.1表3</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表171数据交互方式定义（五）  

<table><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">数据交互方式定义</td></tr><tr><td colspan="1" rowspan="1">测试需求编号</td><td colspan="1" rowspan="1">CBTC-IF-ATS/ATS-MSG-IrC-10</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">T/CAMET04011.6章节5.2.3.2图4表明了两个线路ATS间互传的数据流（箭头方向表示数据流向），具体定义如下：</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">1)A为本线路的列车运行调整信息；2）B为本线路的站场显示信息、列车信息、接入站跳停命令及回执；3)C为心跳信息</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

# 6.7.7应用信息定义

应用信息定义功能的测试和验证方法详见表172。

表172C\应用信息定义  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>送方不可能发送的非法取值                                  息包中存在“无效”值字段进行错误处理.程中不实现的功能，通信字段取值发送“默认”值；设备在初始化完前道法确定状态时，相关字段取值发送“默认”值。接收方收到“默认”值后，应认为信息有效，不进行处理.协议中涉及“上行”“下行”的方向定义，均采用运营方向规定的上下行</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见备厂商设计文件</td></tr></table>

# 6.7.8心跳信息包

心跳信息包功能的测试和验证方法详见表173。

表173心跳信息包  

<table><tr><td>功能名称</td><td>心跳报文</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-ATS/ATS-MSG-ITC-12</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">ATS应周期性发送心跳信息，具体格式同应用信息包为0的GAL包</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">ATS系统周期向相邻ATS发送心跳报文</td></tr></table>

# 6.7.9站场显示信息包

站场显示信息包功能的测试和验证方法详见表174。

表174站场显示信息包  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>站场显示信息包</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-13</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS应周期性将复视车站的所有站场表示信息发送给相邻线ATS.站场显示信息包详见T/CAMET04011.6章节5.2.3.3.3表4</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>ATS系统周期向相邻ATS发送跨线显示区域的站场信息</td></tr></table>

# 6.7.10列车信息包

列车信息包功能的测试和验证方法详见表175。

# 表175列车信息包

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车信息包</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-14</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS应周期性将复视车站的所有列车状态信息发送给相邻线 ATS，详见T/CAMET04011.6章节5.2.3.3.4表5</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>ATS系统周期向相邻ATS发送跨线显示区域的列车信息</td></tr></table>

# 6.7.11列车运行调整信息包

列车运行调整信息包功能的测试和验证方法详见表176。

表176列车运行调整信息包  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车运行调整信息包</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-15</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>对于跨线列车，线路ATS间应周期性互传各自线路内跨线运营分界处交出车站的计划运行图/时刻表、实迹运行图/时刻表和计划调整信息。列车运行调整信息包定义详见T/CAMET04011.6章节5.2.3.3.5表6</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>ATS系统周期向相邻ATS发送跨线显示区域的列车运行调整相关信息</td></tr></table>

# 6.7.12列车接入站跳停命令信息包

列车接人站跳停命令信息包功能的测试和验证方法详见表177。

# 表177列车接入站跳停命令信息包（一）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车接入站跳停命令信息包</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-1F-ATS/ATS-MSG-1TC-16</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>对跨线列车，当在接人线接入站（人工或自动）设置跳停时，由接人线ATS发送站台跳停命令至交出线ATS，交出线ATS收到跳停命令后，发送接收回执给接入站ATS，由交出站ATS负贞管理接入站台的跳停命令，确定将命令发送至列车的时机，回执超时时重发N次后报错，并停止发送（重发次数、超时时间可配置）。列车接人站跳停命令信息包定义详见T/CAMET04011.6章节5.2.3.3.6表7</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>接入线ATS系统周期向移交ATS发送跨线区域的列车跳停信息</td></tr></table>

# 6.7.13列车接入站跳停回执信息包

列车接人站跳停回执信息包功能的测试和验证方法详见表178。

表178列车接入站跳停回执信息包  

<table><tr><td>功能名称</td><td>列车接入站跳停回执信息包</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-ATS/ ATS-MSG-ITC-17</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">对跨线列车，当接人线接入站站台设置跳停时，交出线ATS收到接入站发送的接入站站台跳停命令信息包后回复接收回执。列车接入站跳停回执信息包的定义详见T/CAMET04011.6章节5.2.3.3.7表8</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">移交线ATS系统向接入线ATS发送跨线区域的列车跳停信息包回执信息</td></tr></table>

# 6.7.14ATS城市自定义帧

ATS城市白定义帧功能的测试和验证方法详见表179。

# 表179ATS城市自定义帧

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATS城市门定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSC-ITC-18</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各城市特有的互联互通相关功能，具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1）ATS系统向相邻ATS发送城市自定义帧；2)依据城市需求测试</td></tr></table>

# 6.7.15ATS厂商自定义帧

ATS厂商自定义帧功能的测试和验证方法详见表180。

表180ATS厂商自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATS厂商自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-ATS/ATS-MSG-ITC-19</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各厂商特有功能。各厂商分别定制，ATS收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1）ATS系统向相邻ATS发送厂商自定义帧；2)依据厂商功能定义测试</td></tr></table>

# 6.8互联互通车地通信接口（VOBC和ATS）测试需求

# 6.8.1概述

VOBC与ATS之间采用冗余网络进行通信。ATS与VOBC之间的网络拓扑结构采用A网-A网，B网-B网两个链路。VOBC和ATS的通信主要用于列车的运行调整控制（在点式级别下不对基于VOBC-ATS通信的运行调整功能做强制要求，各供应商依据各自系统功能进行测试和验证）。

# 6.8.2物理接口

物理接口功能的测试和验证方法详见表181。

# 表181A物理接口

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>C-IF-VOBC/ATS-MSG-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>OBC与ATS之间采用元     络进行通信ATS与VOBC之间的网络拓扑结构采      冈-A网，B网-B网两个正链路</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>国   商设计文件</td></tr></table>

# 6.8.3安全通信协议

![](images/b2fcdf5c6f133008a8d932ffe252bd6762d2b5278c6644fe52be023fb53e5fe3.jpg)

# 轨道

![](images/e47ef600f97cfc2b8acdfebdb851a93e4050f6ede1dcbd3638a5d66561c5ae62.jpg)

安全通信协议功能的测试和验证方法详见表182。

表182安全通信协议  

<table><tr><td>功能名称</td><td>安全通信协议</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/ATS-MSG-ITC-2</td></tr><tr><td>功能内容</td><td>议》（运基信号[2010]267号）。 采用RSSP-I安全通信协议的前提条件为使用LTE-M通 信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统</td></tr><tr><td>功能内容</td><td>规定。 1）TCP及IP层使用标准TCP/IP协议栈； 2）MAC及PHY层取决于不同的网络种类，无线网使用无 线标准协议，地面网使用以太网协议（IEEE802.3）. RSSP-I安全通信协议架构详见T/CAMET04011.2章节</td></tr><tr><td>测试需求</td><td>线标准协议，地面网使用以太网协议(IEEE802.3)</td></tr></table>

# 6.8.4动态交互描述

动态交互描述功能的测试和验证方法详见表183～表186。

表183动态交互描述（一）  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>消息定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-3</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>将ATS-VOBC间每个周期需要交互的应用信息通过组成通用消息包进行传输详见T/CAMET04011.2章节6.1.3图8</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表184动态交互描述（二）  

<table><tr><td>功能名称</td><td>信息包格式定义</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/ATS-MSG-ITC4</td></tr><tr><td>功能内容</td><td>ATS/VOBC每周期最多允许发送1个通用消息包，通用 消息包中包含ATS与VOBC之间传输的各条应用信息。每 个通用消息包总长不得超过1000字节，格式的定义详见 T/CAMET04011.2章节6.1.3.2表15和表16</td></tr><tr><td>测试需求</td><td>测试接口内容：电子地图版本控制信息。对应的测试需 求如下： 1）上电/进人线路时，车载设备默认采用版本较低的电子 地图版本号； 2)车载设备与地面设备建立连接后，发送的通用消息包 中为当前采用的电子地图版本号； 3）地面设备判断收到的通用信息包中车载电子地图版本 号是否与地面一致，若一致，则进行正常通信，若不一致，则 发送应用内容为空的通用消息包，通知车载设备地面电子 地图版本号； 4)若车载设备收到空通用消息包，则判断本地是否存有 与地面版本一致的电子地图，若有，则采用与地面版本一致 的电子地图，继续与地面设备通信，通用消息包中的电子地 图版本号与地面版本一致；否则，断开与地面设备的通信； 5)其他见各厂商设计文件</td></tr></table>

# 表185动态交互描述（三）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信状态管理   -合法性检查</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-1TC-5</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>ATS及VOBC应分别对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方的应用信息，并记录报警信息。具体检查方式如下：消息内容的一致性检查包括：信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。通用应用（GAL）信息包消息所应包含的信息的完整性。其他逻辑检查</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表186动态交互描述（四）  

<table><tr><td>功能名称</td><td>通信状态管理- 超时检查</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/ATS-MSG-ITC-6</td></tr><tr><td>功能内容</td><td>1．ATS和VOBC应能分别对通信连接状态进行判断： 1）ATS认为与VOBC通信中断的超时时间定义为 TAtsTimeout（可配置，推荐值：6s）； 2）VOBC认为与ATS通信中断的超时时间定义为 TVobcTimeout(可配咒，推荐值：6s)； 3）若ATS在TAtsTimeout超时时间内，没有接收到来自 VOBC的任何消息，则ATS应认为与VOBC的通信中断； 4）若ATS判断收到VOBC的GAL包延迟已经达到 TAtsTimeout，则ATS应丢弃此GAL包或认为与VOBC通信 中断； 5)若VOBC在TVobeTimeout超时时间内，没有接收到 来自ATS的任何消息，则VOBC应认为与ATS的通信 中断； 6）若VOBC判断收到ATS的GAL包延迟已经达到 TVobeTimcout，则VOBC应丢弃此GAL包或认为与ATS通 信中断； 7)通信中断的情况下，应生成报警信息； 8)互联互通线网中，各厂商的VOBC与各条线路上的 ATS的通信超时时间应一致，消息有效期时间应一致， 2.列车在两ATS间移交时，VOBC判断列车最小安全后 端越过ATS边界点后，应与移交ATS断开通信 3.VOBC判断与ATS断开通信，且不再与该ATS重新建 立通信后，应断开与该ATS的TCP/IP或UDP连接</td></tr><tr><td>测试需求</td><td>1）断开相邻VOBC与ATS间通信，并超过系统定义的 TAtsTimeout，ATS系统判断为与VOBC通信超时； 2）断开相邻VOBC与ATS间通信，并超过系统定义的 TVobeTimeout，VOBC系统判断为与ATS通信超时</td></tr></table>

# 6.8.5通信故障处理

通信故障处理功能的测试和验证方法详见表187。

表187通信故障处理  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信故障处理</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>EN50159：2010中提及的7种开放式网络存在的安全通信风险均由安全通信协议RSSP-Ⅱ安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。车地无线通信双方（ATS-VOBC）应用层的通信故障处理分为如下儿种情况：ATS和VOBC对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息TS/VOBC认为与对等方应用全连接的方式进行处理</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>无餐厂商设计文件</td></tr></table>

# 6.8.6数据类型定义

数据类型定义功能的测试和验证方法详见表188

装188数据类型定义  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>市              据类 定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>熟道CBTC-IF-VATS-MSG-ITC-8</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>本条对ATS与VOBC之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET04011.2章节6.3.1表17</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.8.7应用信息定义

应用信息定义功能的测试和验证方法详见表189。

表189应用信息定义  

<table><tr><td>功能名称</td><td>应用信息定义</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/ATS-MSG-ITC-9</td></tr><tr><td>功能内容</td><td>协议中的“非法”值：正常通信时发送方不可能发送的非 法取值。接收方收到GAL包中的应用信息帧中存在“非 法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认 为本周期未收到数据。 协议中的“默认”值：（1）针对具体工程中不实现的功能， 通信双方可在具体T程中约定，相关字段取值发送“默认” 值；（2）设备在初始化完成前，无法确定状态时，相关字段取 值发送“默认值”。接收方收到“默认”值后，应认为信息有 效，不进行处理。 协议中涉及“上行”“下行”的方向定义，均采用运营方向</td></tr><tr><td>测试需求</td><td>规定的上行和下行 见各厂商设计文件</td></tr></table>

# 6.8.8ATS至VOBC心跳报文

ATS至VOBC心跳报文功能的测试和验证方法详见表190。

表190ATS至VOBC心跳报文  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATS至VOBC心跳报文</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG;-ITC-10</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>周期发送，用来维持ATS设备和VOBC间通信链路的连续性：ATS至VOBC心跳帧详见T/CAMET04011.2章节6.3.2.2.1表18</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在具备连续通信通道的前提下，ATS系统周期向点式列车发送心跳报文</td></tr></table>

# 6.8.9ATS至VOBC命令信息帧

ATS至VOBC命令信息帧功能的测试和验证方法详见表191。

表191ATS至VOBC命令信息帧  

<table><tr><td>功能名称</td><td>ATS至VOBC命令信息帧</td></tr><tr><td>测试需求编号</td><td>CBTC-1F-VOBC/ATS-MSG-ITC-11</td></tr><tr><td>功能内容</td><td>各厂商ATS各自按照自身时机向VOBC发送ATO命令 信息帧，由VOBC适配。可能的发送时机包括： 1）当ATS设备所管辖范围内有被控列车，且列车最大安 全前端处于站台区域、转换轨或折返轨时，ATS应周期向该 VOBC发送ATO命令信息； 2)通信过程中，周期发送。 ATS至VOBC命令信息帧定义详见T/CAMET04011.2章 节6.3.2.2.2表19</td></tr><tr><td>测试需求</td><td>1.测试接口内容：下一ZCID、下一CI ID、下一ATSID。 对应的测试需求如下： 1）对于计划列车ATS向列车发送下一ZCID，在具备条件 时，列车根据此ID呼叫相应的ZC；否则，发送默认值； 2）对于计划列车ATS向列车发送下一CIID，在具备条件 时，列车根据此ID呼叫相应的CI;否则，发送默认值； 3）对于计划列车ATS向列车发送下一ATSID，在具备条 件时，列车根据此ID呼叫相应的ATS；否则，发送默认值。 2.测试接口内容：服务号/表号、线路编号、车组所属线路 号、车组号、源线路号、车次号、目的地线路号、目的地号、计 划运行方向。对应的测试需求：计划车/非计划车，检查 ATS向ATO发送的命令信息帧中上述内容正确。 3.测试接口内容：跳停站台ID、下一停车站台ID、下一站 跳停命令。对应的测试需求如下： 1)设置跳停命令，列车位置在跳停命令接收范围内。列 车将依据命令在跳停车站停车； 2）设置跳停命令，列车位置在跳停命令接收范围外；列车 将继续在已设置跳停的站台执行停站操作； 3)取消跳停命令，列车位置在命令接收范围内。列车将 依据命令在取消跳停车站停车； 4)取消跳停命令，列车位置在命令接收范围外。列车将 继续跳停已设置取消跳停的站台。 注：对于各厂家命令设置的范围依据协议中定义进行 测试。</td></tr></table>

<table><tr><td colspan="2">表191ATS至V0BC命令信息帧（续）</td></tr><tr><td>功能名称</td><td>ATS至VOBC命令信息帧</td></tr><tr><td>测试需求</td><td>4．测试接口内容：站停时间、区间运行调整命令。对应的 测试需求：列车进人站台，收到ATS发送的站停时间命令和 区间运行调整命令，在站台停准停稳，打开车门，到达站停 时间后，关闭车门，驶出站台，在区间按照收到的运行等级 或区间运行时间行驶。 5．测试接口内容：扣车命令.对应的测试需求：列车最大 安全前端所在站台有扣车命令，ATS发送“扣车有效”，列车 执行扣车命令，否则发送“扣车取消，无扣车” 6．测试接门内容：折返命令．对应的测试需求：对于计划 列车，列车最大安全前端在站台内时，ATS按照列车运行计 划判断列车是否要进行折返，并发送响应的站前折返、有人 站后折返、无人自动折返命令；对于非计划列车或与ATS无 通信的列车，ATS向列车发送“不折返”命令，列车根据车载 电了地图存储的区段届性显示折返提示.. 7.测试接口内容：同段指示。对应的测试需求如下： 1）VOBC与ATS通信正常： 当列车最大安全前端在转换轨内且列车为回段方向时， 对于计划列车，ATS根据列车运行计划，向VOBC发送“回 段”或“不回段”指示，列车在转换轨内进行相应的显示；对 于非计划列车，ATS向VOBC发送默认值。 当列车最大安全前端不在转换轨内或列车不为回段方向 时，ATS向VOBC发送的“回段指示”字段为默认值。 2）VOBC与ATS断开： VOBC与ATS通信断开或收到的回段提示字段为默认值 时，根据电子地图配的区段属性，在转换轨内显示回段 提示。 8.测试接口内容：门控策略。对应的测试需求如下： 1）站台为单侧门时，发送ATS中配置的默认值； 2)站台为双侧门时，发送相应的门控策略：同时开双侧 门、先开左门再开右门、先开右门再开左门；</td></tr></table>

# 6.8.10ATS城市自定义帧

ATS城市自定义帧功能的测试和验证方法详见表192。

# 表192ATS城市自定义帧

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATS城市自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-12</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>白定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>据城市需求测试</td></tr></table>

# 6.8.11 ATS厂商自定

ATS厂商自定义帧功能的测试和验证法详见表193。

表193ATS厂商自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>市轨道TS商自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-14</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各厂商特有功能，各厂商分别定制，VOBC收到非本厂商的厂商门定义帧后，可不进行处理</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在具备连续通信通道的前提下，ATS系统周期向点式列车发送厂商自定义帧；2）点式列车不做强制要求；3)依据厂商功能定义测试</td></tr></table>

# 6.8.12ATO状态信息帧

ATO状态信息帧功能的测试和验证方法详见表194。

表194AT0状态信息帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>ATO状态信息帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-15</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>若已建立ATO模式，VOBC应周期向ATS发送ATO状态信息。ATS需针对每列车的ATO状态信息进行超时判断，配置时间内未收到相应列车的ATO状态信息，则清除该车的ATO状态信息，ATO状态信息帧定义详见T/CAMET04011.2章节6.3.2.3.1表22</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在具备连续通信通道的前提下，ATO系统周期向ATS发送状态信息帧（点式列车不做强制要求）</td></tr></table>

# 6.8.13列车信息帧

列车信息帧功能的测试和验证方法详见表195。

# 表195列车信息帧(一)

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>列车信息帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-IrC-16</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>本消息为周期信息，当VOBC与ATS之间的安全连接建立后，周期发送，列车信息帧定义详见T/CAMET04011.2章节6.3.2.3.2表23和表24</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在具备连续通信通道的前提下，VOBC周期向ATS发送列车信息帧（点式列车不做强制要求）</td></tr></table>

# 6.8.14车载设备报警信息帧

车载设备报警信息帧功能的测试和验证方法详见表196。

# 表196车载设备报警信息帧

<table><tr><td>功能名称</td><td>车载设备报警信息帧</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/ATS-MSG-ITC-17</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">车载设备报警信息帧定义详见T/CAMET04011.2章节6.3.2.3.3表25</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">在具备连续通信通道的前提下，VOBC周期向ATS发送车载报警信息帧（点式列车不做强制要求）</td></tr></table>

# 6.8.15车载设备日检信息帧

车载设备日检信息帧功能的测试和验证方法详见表197。

表197车载设备日检信息帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>车载设备H检信息帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-18</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>车载设备口检信息帧定义详见T/CAMET04011.2章节6.3.2.3.4表26</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>在具备连续通信通道的前提下，VOBC向ATS发送车载H检信息帧（点式列车不做强制要求）</td></tr></table>

# 6.8.16VOBC城市自定义帧

VOBC城市自定义帧功能的测试和验证方法详见表198。

表198VOBC城市自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC城市自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-19</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在具备连续通信通道的前提下，VOBC向ATS发送城市自定义帧；2)点式列车不做强制要求；3)依据城市需求测试</td></tr></table>

# 6.8.17VOBC厂商自定义帧

VOBC厂商白定义帧功能的测试和验证方法详见表199。

表199VOBC厂商自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC厂商自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/ATS-MSG-ITC-20</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各厂商特有功能，各厂商分别定制，ATS收到非本厂商的厂商门定义帧后，可不进行处理</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)在具备连续通信通道的前提下，VOBC向ATS发送厂商门定义帧；2)点式列车不做强制要求；3）依据厂商功能定义测试</td></tr></table>

# 6.9互联互通车地通信接口（VOBC和CI）测试需求

6.9.1概述

6.9.1.1VOBC和CI是通过双路冗余的无线网络，基于TCP/IP协议（传输层）进行通信的：VOBC和CI的通信主要用于站台安全门PSD的控制。

6.9.1.2CI将VOBC所在站台的出站信号机状态发送给乍载VOBC，如出站信号机为红灯，则车载应提供闯红灯防护功能。

# 6.9.2接口连接方式

接口连接方式描述功能的测试和验证方法详见表200和表201，

# 表200物理接口

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>物理接口</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-1</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>VOBC与CI之间采用冗余网络进行通信．CI与VOBC之间的网络拓扑结构采用A网-A网和B网-B网两个链路进行连接</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表201安全通信协议  

<table><tr><td>功能名称</td><td>安全通信协议</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/CI-MSG-ITC-2 CI与VOBC之间通信可采用RSSP-Ⅱ或RSSP-I安全通</td></tr><tr><td>功能内容</td><td>信协议。 RSSP-Ⅱ安全通信协议的具体要求参见《RSSP-Ⅱ铁路 信号安全通信协议》（运基信号[20I0]267号）；RSSP-I 安全通信协议的具体要求参见《RSSP-I铁路信号安全 通信协议》（运基信号[20I0】267号）采川RSSP-I安 全通信协议的前提条件为使用LTE-M通信ITE-M具 备空口 装、CBTC信号系统符合一级 等保 安全通信协议 T/CAMET040I1.2章节 层，遵循RSSP-Ⅱ标准 规定 通信协议架构详见T/CAMET04011.2章节 7.1.2图1 1)UDP层使用标准UDP协议栈； 2）MAC及PHY层取决于不同的网络种类，无线网使用无</td></tr><tr><td>测试需求</td><td>线标准协议，地面网使用以太网协议（IEEE802.3) 见各厂商设计文件</td></tr></table>

# 6.9.3动态交互描述

动态交互描述功能的测试和验证方法详见表202～表204。

# 表202动态交互描述(一)

<table><tr><td>功能名称</td><td>信息包格式定义</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/CI-MSG-ITC-3</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">CI/VOBC每周期最多允许发送1个消息包，包中包含CI与VOBC之间传输的应用信息，每个GAL消息包总长不得超过1000字节，格式定义详见T/CAMET04011.2章节7.1.3.2表29和表30</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

# 表203动态交互描述（二）

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信状态管理   合法性检查</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-1F-VOBC/CI-MSG-ITC4</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>CI应对接收到的VOBC的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方的应用信息。具体检在方式如下：消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。消息所应包含的信息的完整性</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

表204动态交互描述（三）  

<table><tr><td>功能名称</td><td>通信状态管理 超时检查</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/CI-MSG-ITC-5</td></tr><tr><td>功能内容</td><td>CI和VOBC应能分别对通信连接状态进行判断： I）CI认为与VOBC通信中断的超时时间定义为 TCiTimeout（可配置，推荐值为6s）； 2）VOBC认为与CI通信中断的超时时间定义为 TVobeTimeout（可配置，推荐值为6s）； 3）若CI在TCiTimeout超时时间内，没有接收到来自 VOBC的任何消息，则CI应认为与VOBC的通信中断； 4）若VOBC在TVobeTimeout超时时间内，没有接收到来 白CI的任何消息，则VOBC应认为与CI的通信中断；</td></tr><tr><td colspan="1" rowspan="1">功能名称</td><td colspan="1" rowspan="1">通信状态管理一   超时检查</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">5）若CI判断接收到VOBC的应用信息延迟已经达到TCiTimeout时，CI应丢弃此信息包或认为与VOBC通信中断；6）若VOBC判断接收到CI的应用信息延迟已经达到TVobcTimeout时，VOBC应丢弃此信息包或认为与Cl通信中断互联互通线网中，车载设备与各条线路上的联锁设备的通信超时时间应一致，消息有效期时间应一致：VOBC在与CI设备通信时，当判断与CI设备通信断开并且不再与对方建立连接后，应断开与CI设备的TCP/IP连接</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">1)断开相邻VOBC与CI间通信，并超过系统定义的TCiTimcout，CI系统判断为与VOBC通信超时；2)断开相邻VOBC与CI间通信，并超过系统定义的TVobeTimeout，VOBC系统判断为与CI通信超时</td></tr></table>

# 6.9.4通信故障处理

通信故障处理功能的测试和验证方法详见表205。

表205通信故障处理  

<table><tr><td>功能名称</td><td>通信故障处理</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-VOBC/C1-MSG-ITC-6</td></tr><tr><td>功能内容</td><td>EN50159：2010中提及的7种开放式网络存在的安全通 信风险均由安全通信协议进行防护，风险包括：重复、删除、 插入、重排序、损坏、伪装、延迟。 车地无线通信双方（CI-VOBC）应用层的通信故障处理分 为如下儿种情况： 1)CI和VOBC对于接收到的重复、逆序的应用信息，采用 直接丢弃的方式进行处理，并且认为本周期未收到对等方 的应用信息；</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">2)通信中断的情况下处理：若CI/VOBC认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理；3)其他风险由安全通信协议完成防护处理</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

# 6.9.5通信体系结构

通信体系结构功能的测试和验证方法详见表206。

表206通信体系结构  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信层次划分</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-1F-VOBC/CI-MSG-ITC-7</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>VOBC与CI通信协议模型详见T/CAMET04011.2章节7.2.1图13</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.6通信机制

通信机制功能的测试和验证方法详见表207。

表207通信机制  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>通信机制</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-14</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>1）仅能由VOBC发起安全连接的建立过程；2）CI与VOBC采用周期发送和消息触发的方式进行通信；3)通信双方均采用大端字节序进行数据传输；4）CI与VOBC均应对接收的应用信息进行判断和逻辑运算</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.7应用信息定义

应用信息定义功能的测试和验证方法详见表208。

表208应用信息定义  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>应用信息定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-18</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td></td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>[商计件</td></tr></table>

![](images/bf0a635317fa4e395b9c7169e97186e1d4f7f8a869b4a2b7853b18fe43866244.jpg)

# 轨道

# 6.9.8数据类型定义

数据类型定义功能的测试和验证方法详见表209。

表209数据类型定义  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>数据类型定义</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-19</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>对VOBC与CI之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET04011.2章节7.3.1表31</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.9 VOBC向CI发送心跳帧

VOBC向CI发送心跳帧功能的测试和验证方法详见表210。

表210VOBC向CI发送心跳帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC向CI发送心跳帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-20</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>在列车车头最大安全前端进人CI通信区段前发送该信息包（具体时机各厂商自定义），用来维持VOBC设备和CI间通信链路的连续性列车车头最大安全前端进人CI通信区段后，开始发送控制信息时不再发送心跳帧VOBC向CI发送心跳帧定义详见T/CAMET04011.2学节7.3.2.2.1表32</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.10VOBC向CI发送控制信息

VOBC向CI发送控制信息功能的测试和验证方法详见表211。

表211VOBC向CI发送控制信息  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC向CI发送控制信息</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-21</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>从列车车头最大安全前端进人CI通信区段开始，直至列车最大安全前端离开CI通信区段前，发送该信息包VOBC至CI输出信息接口長详见T/CAMET04011.2章节7.3.2.2.2表33，应用层报文长度固定，全线站台门的编号方式应有共同的规则和相应的说明文件</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>1)站台区域具备连续通信条件；2)点式级别列车进站对标停车（跨线列车）；3)进行开关车门操作，站台门开关时机和一致性（包括方向和数量）符合设计要求</td></tr></table>

# 6.9.11VOBC向CI发送城市自定义帧

VOBC向CI城市发送白定义帧功能的测试和验证方法详见表212。

表212VOBC向CI发送城市自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC向CI发送城市自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-22</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>白定义信息，用于实现各城市特有的互联互通相关功能：具体内容在工程中根据实际需求约定，各厂商均应实现相应功能，详见T/CAMET04011.2章节7.3.2.2.3表35</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.12VOBC向CI发送厂商自定义帧

VOBC向CI发送厂商白定义帧功能的测试和验证方法详见表213。

表213VOBC向CI发送厂商自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>VOBC向CI向送厂商自定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-23</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>白定义信息，用于实现各厂商特有功能。各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与门已属于同一厂商时方可发送，详见T/CAMET04011.2章节7.3.2.2.4表36</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.13VOBC向CI发送注销请求帧

VOBC向CI发送注销请求帧功能的测试和验证方法详见表214。

表214VOBC向CI发送注销请求帧  

<table><tr><td>功能名称</td><td>VOBC向CI发送注销请求帧</td></tr><tr><td>测试需求编号</td><td>CBTC-IF-V0BC/CI-MSG-ITC-24</td></tr><tr><td colspan="1" rowspan="1">功能内容</td><td colspan="1" rowspan="1">在列车判断需要与CI断开通信时，VOBC向CI发送注销信息，直至VOBC收到CI同复的注销信息，或者VOBC判断通信超时。VOBC发送的“注销请求”包、“控制信息”包、“心跳”包在同一GAL包中不应同时存在。VOBC向CI注销请求帧定义详见T/CAMET04011.2章背7.3.2.2.5表37</td></tr><tr><td colspan="1" rowspan="1">测试需求</td><td colspan="1" rowspan="1">见各厂商设计文件</td></tr></table>

# 6.9.14CI向VOBC发送心跳帧

CI向VOBC发送心跳帧功能的测试和验证方法详见表215。

表215CI向VOBC发送心跳帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>CI向VOBC发送心跳帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-25</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>当CI与VOBC建立链接后，H尚未收到VOBC=&gt;CI控制信息之前，发送该信息包，用来维持VOBC设备和CI间通信链路的连续性，CI向VOBC发送心跳帧的定义详见T/CAMET04011.2章节7.3.3.1表38</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.15CI向VOBC发送状态信息

CI向VOBC发送状态信息功能的测试和验证方法详见表216。

表216CI向VOBC发送状态信息  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>CI向VOBC发送状态信息</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-26</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>当CI收到VOBC的控制信息之后，发送该信息包：CI至VOBC输出信息接口表详见T/CAMET04011.2章节7.3.3.2表39</td></tr></table>

# 表216CI向VOBC发送状态信息（续）

<table><tr><td>功能名称</td><td>CI向VOBC发送状态信息</td></tr><tr><td>测试需求</td><td>2)点式级别列车进站对标停车并结束停站作业且具备发 车条件（跨线列车）；</td></tr></table>

# 6.9.16CI向V0BC发送城市自定义帧

CI向VOBC发送城市自定义帧功能的测试和验证方法详见表217。

表217CI向VOBC发送城市自定义帧  

<table><tr><td>功能名称</td><td></td><td>CI向VOBC发送城市自定义帧</td></tr><tr><td>测试需求编号</td><td></td><td></td></tr><tr><td>功能内容</td><td></td><td>的互联互通相关功能。 内定，各厂商均应实现相</td></tr><tr><td>测试需求</td><td></td><td>节7.3.3.3表40</td></tr></table>

# 6.9.17CI向VOBC发送厂商自定义帧

CI向VOBC发送厂商白定义帧功能的测试和验证方法详见表218。

表218CI向VOBC发送厂商自定义帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>CI向VOBC发送厂商白定义帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-28</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>自定义信息，用于实现各厂商特有功能。各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自已屈于同一厂商时方可发送，详见T/CAMET04011.2章节7.3.3.4表41</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 6.9.18CI向VOBC发送注销回复帧

CI向VOBC发送注销回复帧功能的测试和验证方法详见表219。

表219CI向VOBC发送注销回复帧  

<table><tr><td rowspan=1 colspan=1>功能名称</td><td rowspan=1 colspan=1>CI向VOBC发送注销回复帧</td></tr><tr><td rowspan=1 colspan=1>测试需求编号</td><td rowspan=1 colspan=1>CBTC-IF-VOBC/CI-MSG-ITC-29</td></tr><tr><td rowspan=1 colspan=1>功能内容</td><td rowspan=1 colspan=1>在CI接收到VOBC的注销请求帧后，向VOBC回复注销回复帧。CI发送的“注销回复”包、“状态信息”包、“心跳”包在同一GAL包巾不应同时存在。CI向VOBC输出信息接口表详见T/CAMET04011.2章节7.3.3.5表42</td></tr><tr><td rowspan=1 colspan=1>测试需求</td><td rowspan=1 colspan=1>见各厂商设计文件</td></tr></table>

# 7测试案例要求

# 7.1总体要求

a) 互联互通测试案例编写需要依据本部分的测试需求进行，需要对测试需求中规定的功能点实现全覆盖。每个测试需求可以对应多个测试案例。

b）测试案例的编写及测试过程需要遵循以下原则：

1) 测试过程中同时涉及车载和地面设备时，默认采用不同厂家设备；  
2) 测试过程中涉及两个控区地面设备时，默认采用不同厂家设备；  
3) 对于相同功能但正线和跨线接口实现方式不同的需求，需要在正线和跨线接口测试。

c）鉴于各厂家对故障的识别及处理原则存在较大差异，故障相关测试内容在互联互通产品供应商测试及验证阶段执行。

# 7.2具体要求

测试案例中应至少描述以下内容：

a) 对应的测试需求；  
b) 本规范中定义的测试阶段；  
c ) 测试条件（测试时应具备的前提条件）；  
d) 测试环境（如时间、地点、人员）；  
e) 被测设备的厂家编号等。

# 参考文献

[1]《RSSP-Ⅱ铁路信号安全通信协议》（运基信号[2010]267号）[2]IEEE802.3系列标准

# 城市轨道交通基于通信的列车运行控制系统（CBTC）

互联互通测试规范

# 第2部分：点式部分测试及验证

T/CAMET 04012.2—2018

\*

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门西街8号）出版社网址：http：//www.tdpress.com

开本： $8 8 0 \ \mathrm { m m } \times 1 \ 2 3 0 \ \mathrm { m m }$ 1/32印张：5字数：138千2019年6月第1版2019年6月第1次印刷

书号：15113·5715定价：40.00元

# 版权所有侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174