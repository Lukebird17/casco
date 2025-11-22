# 中国城市轨道交通协会团体标准

T/CAMET 04012.1—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范 第1部分：CBTC部分测试及验证

# Urban rail transit — Test specification for interoperability of communication based train control system Part 1: Test and verification of CBTC part

2018-09-10 发布

2018-12-31 实施

---

## 目次

前言 …… VII    
引言 …… VIII    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 3    
3.1 术语 …… 3    
3.2 缩略语 …… 6    
4 互联互通产品测试生命周期划分及验证活动 …… 7    
4.1 测试阶段生命周期划分及验证活动 …… 7    
4.2 测试阶段内容及依据 …… 8    
5 测试环境 …… 8    
5.1 互联互通产品供应商测试及验证平台需求 …… 8    
5.2 互联互通系统集成实验室测试及验证平台需求 …… 8    
5.3 互联互通试验线测试及验证平台需求 …… 9    
6 测试需求 …… 10    
6.1 互联互通产品测试验证活动的划分原则 …… 10    
6.2 互联互通总体功能及接口功能分配 …… 12    
6.3 互联互通测试需求 …… 47    
6.4 互联互通计算机联锁（CI）间接口测试需求 …… 99    
6.5 互联互通区域控制器（ZC）间跨线接口测试需求 …… 109    
6.6 互联互通跨线 ATS 间接口测试需求 …… 117    
6.7 互联互通车地通信接口（VOBC 和 CI）测试需求 …… 126    
6.8 互联互通车地通信接口（VOBC 和 ATS）测试需求 …… 136

---

6.9 互联互通车地通信接口 (VOBC 和 ZC) 测试需求 …… 147  
7 测试案例要求 …… 161  
7.1 总体要求 …… 161  
7.2 具体要求 …… 161  
参考文献 …… 162

---

## 前言

T/CAMET 04012《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》分为以下两个部分：

——第1部分：CBTC部分测试及验证；

——第2部分：点式部分测试及验证。

本部分是 T/CAMET 04012 的第 1 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：中国铁道科学研究院集团有限公司通信信号研究所、交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、浙江众合科技股份有限公司、北京交通大学、株洲中车时代电气股份有限公司。

本部分主要起草人：编写组：李亮、史宁娟、许硕、娄玥童、徐文升、刘鲁鹏、杨鹏、方发根、周在福、黄友能、刘宏杰、王奇、王丽丽。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、王道敏、张良、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、徐鼎。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车 运行控制系统(CBTC)互联互通测试规范 第1部分:CBTC部分测试及验证

## 1 范围

T/CAMET 04012 的本部分规定了基于通信的列车运行控制系统（CBTC）互联互通其 CBTC 部分功能验证测试以及接口验证测试。

本部分适用于满足互联互通要求的 CBTC 系统其 CBTC 部分验证测试应包含的各个阶段，按照阶段定义和互联互通需求特点对需求验证进行分配，并作为后续互联互通测试案例编写的依据，对案例的编写具有指导作用。

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡注日期的引用文件，仅注日期的版本适用于本部分。凡不注日期的引用文件，其最新版本（包括所有修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB/T 21562—2008 轨道交通可靠性、可用性、可维护性和安全性规范及示例（IEC 62278:2002，IDT）

GB/T 22239—2008 信息安全技术-信息系统安全等级保护基本要求

GB/T 28808—2012 轨道交通通信、信号和处理系统控制和防护系统软件（IEC 62279:2002, IDT）

GB/T 28809—2012 轨道交通通信、信号和处理系统信号用安全相关电子系统（IEC 62425:2007, IDT）

---

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第1部分：系统总体要求

T/CAMET 04010.3 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第3部分：车载电子地图

T/CAMET 04011.1 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第1部分：应答器报文

T/CAMET 04011.2 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第2部分：CBTC系统车地连续通信协议

T/CAMET 04011.3 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）与车辆的接口

T/CAMET 04011.4 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通接口规范 第 4 部分: 区域控制器 (ZC) 间接口

T/CAMET 04011.5 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通接口规范 第 5 部分: 计算机联锁 (CI) 间接口

T/CAMET 04011.6 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第6部分：列车自动监控系统（ATS）间接口

EN 50159:2010 铁路应用-通信、信号和处理系统-信号的安全相关的电子系统（Railway Applications-Communication, Signaling and Processing System-Safety-Related Communication in Transmission Systems）

IEEE Std 1474.1—2004 IEEE 基于通信的列车控制（CBTC）系统的性能和功能要求（IEEE Standard for Communications-Based Train Control (CBTC) Performance and Functional Requirements）

IEEE Std 1474.4—2011 IEEE 基于通信的列车控制（CBTC）系统的系统功能测试推荐实践（IEEE Recommended Practice for Functional

---

Testing of a Communications Based Train Control (CBTC) System)

## 3 术语和缩略语

GB 50157—2013、CJ/T 407—2012 和 T/CAMET 04010.1 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术，连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.2 

## 正线 main line

载客列车运营的贯穿全程的线路。

[GB 50157—2013, 定义 2.0.11]

#### 3.1.3 

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.37]

#### 3.1.4 

列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路，指挥行车，实施列车运行管理等技术的总称。

[GB 50157—2013, 定义 2.0.38]

#### 3.1.5 

## 列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

---

[GB 50157—2013, 定义 2.0.39]

#### 3.1.6 

列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

[GB 50157—2013, 定义 2.0.40]

#### 3.1.7 

计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.8 

## 维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护。

[T/CAMET 04010.1,术语3.1.8]

#### 3.1.9 

## 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点。

[T/CAMET 04010.1,术语3.1.10]

#### 3.1.10 

## 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T 407—2012, 定义 3.1.7]

#### 3.1.11 

装备列车 CBTC-equipped trains

装备了 CBTC 系统车载设备且设备处于工作状态的列车。

[T/CAMET 04010.1,术语3.1.11]

#### 3.1.12 

非装备列车 Non-CBTC-equipped trains

没有装备 CBTC 系统车载设备或者 CBTC 系统车载设备处于不工作

---

状态的列车。

[T/CAMET 04010.1,术语 3.1.12]

#### 3.1.13 

## 转换轨 transfer track

指车辆段/停车场与正线的连接轨，运营列车在驶入/驶出转换轨过程中，当条件具备时，进行列车运行控制级别及驾驶模式转换。

[T/CAMET 04010.1,术语 3.1.13]

#### 3.1.14 

跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式

[T/CAMET 04010.1, 术语 3.1.14]

#### 3.1.15 

平均故障间隔时间（平均无故障时间）mean time between failures

指设备连续发生两次故障之间的平均间隔时间

#### 3.1.16 

列车自动驾驶模式 automatic manual train operation

在司机监控下，CBTC系统自动控制列车运行，并进行安全防护的列车驾驶模式。

#### 3.1.17 

列车自动防护模式 coded train operating mode

在列车自动防护设备防护下，司机驾驶列车运行的列车驾驶模式。

#### 3.1.18 

限制人工驾驶模式 restricted train operating mode

司机按规定的目视行车限速控车运行，列车自动防护设备进行超速防护的列车驾驶模式。

#### 3.1.19 

非限制人工驾驶模式 emergency unrestricted train operating mode

ATP 自动防护设备已被切除，车载设备不对列车运行进行监控，司机按操作规程驾驶列车的列车驾驶模式。

---

#### 3.1.20 

## 移交重叠区 handover overlap region

为使列车在相邻区域控制器（ZC）间平滑移交，在 ZC 管辖范围交界处设置的用于列车移交控制的区域。

[T/CAMET 04010.1,术语 3.1.15]

#### 3.1.21 

## 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1,术语 3.1.16]

### 3.2 缩略语

AM: 列车自动驾驶模式 (Automatic Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO: 列车自动运行(Automatic Train Operation)

ATP: 列车自动防护(Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

BTM: 应答器传输模块 (Balise Transfer Module)

CBTC:基于通信的列车控制(Communication Based Train Control)

CI: 计算机联锁 (Computerized Interlocking)

CTC: 连续式等级 (Continuous Train Control)

DCS: 数据通信系统 (Data Communication System)

ITC: 点式运行级别 (Intermittent Train Control)

LEU:轨旁电子单元(Lineside Electronic Unit)

MSS: 维护支持系统 (Maintenance Support System)

MTBF: 平均故障间隔时间 (Mean Time Between Failures)

MTTR: 平均修复时间 (Mean Time To Repair)

PIS:乘客信息系统(Passenger Information System)

PSD:站台门(Platform Screen Door)

---

RAMS: 可靠性、可用性、可维修性和安全性（Reliability, Availability, Maintainability and Safety）

SIL: 安全完整性等级 (Safety Integrity Level)

TMS: 列车管理系统 (Train Management System)

TSR: 临时限速 (Temporary Speed Restriction)

UPS: 不间断电源 (Uninterruptible Power System)

V0BC: 车载控制器 (Vehicle On-Board Controller)

WCS:无线通信系统(Wireless Communication System)

ZC: 区域控制器 (Zone Controller)

## 4 互联互通产品测试生命周期划分及验证活动

### 4.1 测试阶段生命周期划分及验证活动

## a）互联互通产品供应商测试及验证阶段。

本阶段的测试与验证任务由各互联互通产品供应商进行。各互联互通产品供货商需要按照互联互通技术规范的要求，对各子系统产品进行设计与实现，并对互联互通总体要求和功能分配中要求的互联互通功能进行测试与验证。

b）互联互通产品的实验室验证平台测试及验证阶段。

本阶段的测试与验证任务由互联互通产品第三方验证机构进行。各互联互通产品供货商依据实验室测试环境要求提供被测产品，在专用的测试与验证平台进行测试与验证；对互联互通产品进行功能测试。实验室互联互通测试将按照子系统进行，CBTC互联互通功能测试将由VOBC、CI、ATS、ZC子系统4个部分构成。

## c）互联互通产品的试验线测试及验证阶段。

本阶段的测试与验证任务由互联互通产品第三方验证机构进行。各互联互通产品供货商依据试验线测试环境要求提供被测产品，在专用的试验线进行实车测试与验证；对于实验室验证与测试平台无法完全验证的功能进行测试与验证。试验线互联互通测试将按照子系统进行，CBTC互联互通功能测试将由V0BC、CI、ATS、ZC子系统4个部分构成。

---

### 4.2 测试阶段内容及依据

互联互通测试及验证技术规范依据系统规范和接口规范文件编写，主要对系统规范和接口规范中的互联互通功能、接口等进行测试和验证，本规范对系统性能的测试和验证不做要求。

## 5 测试环境

### 5.1 互联互通产品供应商测试及验证平台需求

互联互通产品供应商测试及验证平台由各厂商自己搭建，并对各自产品进行测试和验证，保证产品的设计和实现满足互联互通要求。

### 5.2 互联互通系统集成实验室测试及验证平台需求

#### 5.2.1 测试及验证平台设备构成

实验室验证与测试平台需要由存在互联互通连接的2条实验线路的若干车站构成，可以在2条线路上采用不同厂家的互联互通产品，并验证2条线路之间的地面设备之间以及车地之间的互联互通跨线运行功能，且列车在正常的运营模式下通过跨线接口线路并在正线完成正常的互联互通功能。

室内验证平台测试环境的每条线路选取车站规模为2个控区5个车站，如图1所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e6d22e56-7893-4dab-adfc-7edf68b8dc5c/markdown_0/imgs/img_in_image_box_81_824_824_1055.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A25%3A23Z%2F-1%2F%2Fc9ec28dc492bf447353c66aaaa3890b195ffe9505ac929e5e7fd27f65f2c3d68" alt="Image" width="88%" /></div>


<div style="text-align: center;">图 1 互联互通实验线路构成示意图</div>

---

#### 5.2.2 验证对象与信息流

室内验证平台用于在室内验证跨线 CBTC 互联互通接口及功能。

a）验证对象包括：

——互联互通产品——车载 VOBC 设备；

——互联互通产品——联锁系统设备；

——互联互通产品——ATS 系统设备；

——互联互通产品——轨旁 ATP 系统设备。

b) 验证的内容包括：

——T/CAMET 04010.1 中要求的功能；

——T/CAMET 04011.4 中规定的接口内容；

——T/CAMET 04011.5 中规定的接口内容

——T/CAMET 04011.6 中规定的接口内容

——T/CAMET 0401.3 中规定的内容：

——T/CAMET 04010.3 中规定的内容；

——T/CAMET 04011.2 中规定的(V0BC 与 01部分)内容；

——T/CAMET 0401.2 中规定的(VOBC 与 ATS 部分)内容；

——T/CAMET 040112 中规定的(VOBC)与ZC部分)内容。

#### 5.2.3 验证方法

## 轨道

在实验室验证平台搭建测试环境，通过仿真列车（使用计算机软件仿真的具备 VOBC 逻辑功能的列车）进行本线、跨线接口线路、其他互联互通线路上的 CBTC 运行测试，对互联互通功能进行验证。

### 5.3 互联互通试验线测试及验证平台需求

#### 5.3.1 试验线设备构成

试验线完成 CBTC 系统产品的互联互通测试。试验线设备至少包括：

——试验线路；

——试验列车；

——信号系统设备(ATP、ATO、ATS、联锁、DCS、ZC等):

——信号系统无线通信网络及沿线接入点（LTE 或 Wi-Fi）。

---

#### 5.3.2 试验线条件要求

为了满足在试验线路完成互联互通功能的验证和测试，试验线路选取应具备以下条件：

——跨控区条件；

——站前/站后折返条件；

——设置区间信号机的长大区间（需要设置信号机的区间）。

试验线应设置至少2个控区，5个车站以及4个区间；车站对应设置有站台门相关设备等。

此外，试验列车应兼容互联互通产品供应商信号系统接口。

#### 5.3.3 验证方法

在试验线上，每个控区安装不同供应商的地面设备，利用安装不同供应商的车载信号设备，按照互联互通相关测试规范的要求，列车完成并通过互联互通系统接口以及功能的测试和验证，如图2所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4f3760c7-2318-483a-ab83-27de961d8ae6/markdown_0/imgs/img_in_image_box_85_583_804_675.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A25%3A32Z%2F-1%2F%2F016fed30e295e0f5657720dc5721ce217c27e29f95745f19964f8e37ba38929c" alt="Image" width="85%" /></div>


<div style="text-align: center;">图 2 互联互通试验线示意图</div>


## 6 测试需求

### 6.1 互联互通产品测试验证活动的划分原则

对 CBTC 互联互通系统进行验证首先要根据功能分配进行测试需求的划分，根据测试需求的可执行性，将测试需求划分为可测性需求和不可测需求。可测性需求可通过产品或系统测试的方式进行覆盖和验证，而不可测需求则需要针对具体的要求通过一定方式进行覆盖和验证。

对 CBTC 互联互通系统进行验证，根据测试验证的生命周期将其划分为产品供应商测试及验证阶段、实验室验证平台测试和试验线测试阶段。

---

#### 6.1.1 互联互通产品供应商测试及验证阶段

##### 6.1.1.1 互联互通产品供应商测试及验证阶段的工作内容

本阶段主要是对互联互通产品进行测试，主要工作是各供应商对自己的产品，按照互联互通标准的要求，进行与自己产品相关的全覆盖式测试。

##### 6.1.1.2 互联互通产品供应商测试及验证阶段的测试方法

对于不具备可测性的需求，包括系统结构描述、物理接口等需求，只在本阶段进行覆盖，可参考各产品的设计文件以及相应的实现报告。

对于可测试的需求，供应商依据互联互通系统需求编写对应的测试需求，采用功能测试的方法，对产品需求进行验证和覆盖。

#### 6.1.2 互联互通系统集成实验室验证平台测试阶段

##### 6.1.2.1 互联互通系统集成实验室验证平台测试的工作内容

本阶段属于互联互通系统的集成测试的范围。主要工作为集成各供货商的被测设备，搭建专用的系统测试验证平台，对互联互通系统进行功能测试。系统测试验证平台为半实物的仿真测试平台，即部分设备是实物，部分设备为仿真。实验室测试验证平台测试阶段，对互联互通共线和跨线相关内容进行测试和验证，其中测试与验证的部分分为以下几个部分：

a）与功能相关的测试内容，在此阶段进行测试，如点式功能、CBTC 功能等；

b) 与数据相关的测试内容，在此阶段进行测试，如遍历站台门数据、精确停车数据、列车折返数据等；

c）与接口相关的测试内容，在此阶段进行测试，如与CI-CI接口、ZC-ZC接口、ATS-ATS接口、V0BC-ZC接口等。

##### 6.1.2.2 互联互通系统集成实验室验证平台测试的测试方法

本阶段主要测试目的是对可测需求进行功能验证，采用黑盒测试的方法进行测试。

#### 6.1.3 互联互通试验线测试阶段

##### 6.1.3.1 互联互通试验线测试的工作内容

本阶段与实验室验证平台同属系统集成测试的范围。在试验线集成

---

各系统供应商的被测设备，车辆在真实的线路上运行，所有互联互通设备均采用实物设备来进行测试和验证。

实验室验证平台测试由于部分为仿真环境，诸如列车动力学模型、车辆、线路等等，对系统功能的验证，不能做到完全真实和充分，所以在试验线测试与验证阶段，结合运营方面的要求，测试和验证的内容分为以下几个部分：

a）与设备安装相关的测试内容，在此阶段进行测试，如应答器定位、轮径校正等；

b) 与车辆接口相关功能测试，在该阶段进行，如列车牵引、制动接口等；

c）与线路相关的列车运行相关功能的测试内容，如车辆运行曲线、列车停车位置等；

d）与继电接口相关的功能，如联锁控制道岔、信号机等功能；

e）与网络环境相关的功能，诸如网络的稳定性测试等；

f）与运营相关的功能，诸如按照运行计划跑图功能等。

完成了产品设计与实现的测试、室内验证平台测试、试验线测试后，可对CBTC互联互通系统进行全覆盖的测试和验证。

根据系统测试验证活动的划分原则，对后续章节中的测试需求进行验证和测试的阶段划分。

##### 6.1.3.2 互联互通试验线测试的工作方法

对于试验线可测试的功能，依据互联互通系统测试规范的要求，采用功能测试的方法，对功能项进行验证和覆盖。

### 6.2 互联互通总体功能及接口功能分配

#### 6.2.1 互联互通系统架构和功能分配技术要求中功能分配

对总体要求定义的所有功能点（共73条）进行识别，按照T/CAMET04010.1功能分配的定义将其分配到各相关子系统，并根据其功能属性确定测试验证的阶段，详见表1。

---

<div style="text-align: center;">表 1 功能分配表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">1</td><td rowspan="3">初始化CBTC列车位置</td><td style='text-align: center;'>进入CBTC区域的CBTC列车位置初始化，并自动检测每列符合装备CBTC设备的列车，进入CBTC区域无需手动输入列车位置或列车长度的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>从设备故障中恢复的CBTC列车完成CBTC列车位置初始化，并应自动检测每列装备CBTC设备的列车，从CBTC设备故障中恢复的列车无需手动输入列车位置或列车长度的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车升级至CBTC级别，当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，至少应满足如下转换条件：1) ATP车载设备无故障，且完成列车定位；2) ATP车载设备收到ATP轨旁设备发送的有效MA信息</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="5">2</td><td rowspan="5">确定CBTC列车位置</td><td style='text-align: center;'>确定列车长度 CBTC应能确定列车长度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>确定CBTC列车位置 CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>位置误差校正 CBTC列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车完整性检测 CBTC系统应能实现列车的完整性检测 当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车轮径校正 CBTC系统应能实现列车轮径校正功能，系统宜在列车进入转换轨前设置轮径自动补偿设备，并在出段/场前完成自动轮径补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">2</td><td rowspan="2">确定CBTC列车位置</td><td style='text-align: center;'>确定列车停站位置。CBTC系统应根据不同的列车长度，确定列车的停站位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>退行防护。ATP车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">3</td><td rowspan="2">确定轨道区段占用状态</td><td style='text-align: center;'>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>前方轨道区段占用状态。当CBTC列车前方区段被故障列车或者非CBTC装备列车占用时，CBTC系统应根据前方区段占用状态确定CBTC列车的安全边界</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>防护列车丢失位置报告</td><td style='text-align: center;'>防护列车丢失位置报告 当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">5</td><td rowspan="2">防护列车完整性丢失</td><td style='text-align: center;'>列车完整性检测 CBTC系统应能实现列车的完整性检测 当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>与功能点“确定CBTC列车位置”中“列车完整性检测”重复</td><td style='text-align: center;'>与功能点“确定CBTC列车位置”中“列车完整性检测”重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车完整性丢失防护 在检测到列车完整性丢失时，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>确定前方CBTC列车位置</td><td style='text-align: center;'>CBTC列车前方位置 对于每辆CBTC列车，应确定列车前方的CBTC列车位置</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>确定前方安全进路限制</td><td style='text-align: center;'>前方安全进路限制 对于每辆CBTC列车，系统应确定列车的安全进路位置</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">8</td><td rowspan="3">确定移动授权</td><td style='text-align: center;'>列车完整性检测、CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>与功能点“确定CBTC列车位置”中“列有完整性检测”重复</td><td style='text-align: center;'>与功能点“确定CBTC列车位置”中“列车完整性检测”重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车升级至CBTC级别。当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，至少应满足如下转换条件：1) ATP车载设备无故障且完成列车定位；2) ATP车载设备收到ATP服务设备发送的有效MA信息</td><td style='text-align: center;'>与功能点“初始化CBTC列车位置”中子功能点重复</td><td style='text-align: center;'>与功能点“初始化CBTC列车位置”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>移动授权的确定。为对列车进行合适的移动防护限制，CBTC系统应估算最大移动授权限制位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>确定目标点</td><td style='text-align: center;'>确定目标点。为了确保列车不超过移动授权，CBTC系统应确定一个目标点</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>响应站台紧急关闭按钮</td><td style='text-align: center;'>响应站台紧急关闭按钮的按下。当ATP轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>道岔状态防护</td><td style='text-align: center;'>道岔状态防护。CBTC系统应控制区域内道岔状态进行防护，当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>故障处理</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">13</td><td rowspan="2">固定速度限制防护</td><td style='text-align: center;'>固定线路速度限制。CBTC应提供固定线路限速的限制防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车构造速度限制。系统应提供列车构造速度的防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>临时限速限制防护</td><td style='text-align: center;'>临时限制速度限制。CBTC应按照系统设置的临时限速，为列车计算移动授权，对临时限速进行防护</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="3">15</td><td rowspan="3">确定制动曲线</td><td style='text-align: center;'>目标点的制动曲线</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>考虑最不利情况下的影响。CBTC的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>防止制动曲线超过速度限制。CBTC应保证制动曲线在超过固定或临时限速之前减速</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="3">16</td><td rowspan="3">列车超速防护</td><td style='text-align: center;'>确定授权速度。CBTC应基于ATP曲线，确定列车当前位置的限制速度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>ATP曲线。CBTC应为每辆列车计算完整的ATP曲线</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>速度监督和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>列车超速防护</td><td style='text-align: center;'>移动授权更新时的速度防护。移动授权更新时，如果列车的实际运行速度超过移动授权更新后的紧急制动触发速度，系统应实施紧急制动</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>列车速度测定</td><td style='text-align: center;'>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>测速误差补偿</td><td style='text-align: center;'>测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>零速状态确定</td><td style='text-align: center;'>零速状态确定。CBTC应确定零速度状态</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>列车运行方向确定</td><td style='text-align: center;'>确定CBTC列车运行方向。CBTC系统应确定每辆CBTC列车的实际运行方向</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>列车运行方向防护</td><td style='text-align: center;'>监督/防护运行方向。如果列车实际运行方向与授权的列车运行方向不一致，CBTC应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>退行防护</td><td style='text-align: center;'>退行防护。ATP车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>越过移动授权终点防护</td><td style='text-align: center;'>越过移动授权终点的响应。列车越过移动授权终点时，系统应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'></td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>移动授权更新超时防护</td><td style='text-align: center;'>移动授权更新超时的防护。移动授权更新超时，系统应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'></td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>紧急制动缓解</td><td style='text-align: center;'>紧急制动缓解。在保重安全的条件下，系统可以缓解已施加的紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>车门允许</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>车门允许</td><td style='text-align: center;'>4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>站台门控制</td><td style='text-align: center;'>站台门控制：CBTC应在打开站台门之前，检查是否满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">28</td><td rowspan="2">车门防护</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>车门状态丢失防护。列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1) 切除牵引但不实施制动；2) 不切除牵引，也不实施制动，列车运行至下一座车站；3) 实施紧急制动；4) 实施全常用制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">29</td><td rowspan="2">车门防护切除</td><td style='text-align: center;'>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>车门操作切除。车辆可以提供单个车门切除功能，切除后的车门不响应列车开门命令</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">30</td><td rowspan="2">站台门防护</td><td style='text-align: center;'>站台门锁闭状态防护。仅在站台门处于“关闭且锁闭”状态时，系统方允许列车移动。CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；已进站未停稳以及正在出站的列车应立即紧急制动；已完全出站的列车不受影响</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>站台门状态丢失的响应。当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>列车折返</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>车载ATP界面功能</td><td style='text-align: center;'>CBTC车载ATP显示数据。CBTC车载显示屏落显示ATP数据应包括：1)列车运行模式；2)CBTC运行状态；3)当前列车速度；4)当前最大允许CBTC速度；5)超速报警</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>车载 ATP 界面功能</td><td style='text-align: center;'>CBTC 车载 ATP 输入数据。用户 ATP 信息输入到 CBTC 应包括：1) 运行模式选择；2) 超速报警情况确认</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>ATP 自诊断、故障报警及数据记录</td><td style='text-align: center;'>白诊断、故障报警及数据记录。ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存 7 d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>模式转换</td><td style='text-align: center;'>列车驾驶模式。列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）、列车自动防护模式（CM）为列车正常运行模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>模式转换</td><td style='text-align: center;'>驾驶模式转换：列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>ZC间移交</td><td style='text-align: center;'>ZC切换。两条连续式列车控制级别线路间应设置移交边界和移交重叠区：列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交、接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>电子地图存储</td><td style='text-align: center;'>电子地图存储：CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>停稳停准判断</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td><td style='text-align: center;'>与功能点“车门允许”中子功能点重复</td><td style='text-align: center;'>与功能点“车门允许”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>确定ATO曲线</td><td style='text-align: center;'>确定ATO曲线、CBTC系统应为列车确定ATO曲线。ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制。ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>精确停车</td><td style='text-align: center;'>列车进站精确停车。ATO子系统应具备列车进站自动精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>根据ATO曲线调整列车速度</td><td style='text-align: center;'>列车调速、CBTC系统应根据。ATO曲线调整列车速度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>ATO能够响应ATS系统设置的跳停命令</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>运营调整</td><td style='text-align: center;'>在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="4">43</td><td rowspan="4">开关车门</td><td style='text-align: center;'>开列车门 在 AM 驾驶模式下，在 ATP 的防护下可提供自动开门或者人工开门两种开门方式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>开站台门 CBTC 系统应能自动开启站台门</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>关闭列车门 在 AM 驾驶模式下，可提供自动关门或者人工关门两种关门方式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>关闭站台门 CBTC 系统应能自动关闭站台门</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>ATO 界面显示</td><td style='text-align: center;'>CBTC 车载 ATO 显示数据。在列车显示屏上显示的 CBTC 车载 ATO 数据应由授权管理部门规定</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>ATO 自诊断、故障报警及数据记录</td><td style='text-align: center;'>自诊断、故障报警及数据记录。ATO 子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心 ATS</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>ATO 发送列车运行信息</td><td style='text-align: center;'>ATO 子系统向 ATS 子系统发送列车运行信息，以便 ATS 子系统能对在线列车进行监控</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>ATO发送旅客信息</td><td style='text-align: center;'>车载旅客信息数据。ATO车载设备应向TMS提供有关车载旅客信息的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">48</td><td rowspan="2">确定列车识别号</td><td style='text-align: center;'>CBTC的运行列车识别号。每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车标识号。列车识别号应由列车号、车次号、车组号、目的地号组成</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车-地双向通信传输信息恢复</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>ATS列车追踪</td><td style='text-align: center;'>ATS列车追踪。ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他的相关信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>--</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">50</td><td rowspan="3">列车进路办理</td><td style='text-align: center;'>列车进路办理——自动 ATS 系统应该具有列车自动办理进路的功能。ATS 系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>列车进路办理——人工 ATS 系统应该具有手动办理进路的功能</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>列车进路办理——冲突检查。当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">51</td><td rowspan="3">列车自动调整</td><td style='text-align: center;'>自动调度。ATS 系统可包括自动调度功能</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车时刻表/发车（运行）间隔调整。ATS 系统可具有监视与自动调整的功能</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>冲突自动调整。在 CBTC 列车位置报告的基础上，ATS 系统应包括基于列车位置报告的列车自动调整功能，来处理列车冲突，以把整个系统的延迟减少到最小</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>节能运行</td><td style='text-align: center;'>节能运行. ATS系统可具有通过实时控制及协调列车加速、列车滑行、列车制动来实施能源优化的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>扣车. ATS系统应具有在车站扣车能力</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>提前发车</td><td style='text-align: center;'>提前发车. ATS系统应具有设置站台提前发车的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>跳停车站. ATS系统应具有设置一个或多个装备CBTC的列车经过下一个或下几个车站而不停车的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>设置/取消临时限速</td><td style='text-align: center;'>临时限速. ATS系统应具有在CBTC区域内任何轨道区段，设置（与取消）临时限速的能力</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>时刻表编制管理</td><td style='text-align: center;'>ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>模拟培训</td><td style='text-align: center;'>ATS应具备模拟演示及培训系统，实现对调度员的培训</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">59</td><td rowspan="3">ATS界面功能</td><td style='text-align: center;'>在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的</td><td style='text-align: center;'>与功能点“运营调整”中子功能点重复</td><td style='text-align: center;'>与功能点“运营调整”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>ATS列车追踪，ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他相关的信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td><td style='text-align: center;'>与功能点“ATS列车追踪”中子功能点重复</td><td style='text-align: center;'>与功能点“ATS列车追踪”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>ATS显示数据，CBTC的ATS显示应能够表示以下信息：1)精确的和区域相关的信息；2)列车状态相关信息；3)列车移动授权/进路信息；4)和被控列车运行相关的信息如防护区段信息、锁闭的进路/区段，以及临时限速极限和限速值；5)其他</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>ATS界面功能</td><td style='text-align: center;'>CBTC输入数据。CBTC的ATS用户界面显示应能够接收以下ATS用户输入：
1)办理和取消进路输入；
2)建立和取消防护区段，锁闭进路/区段，以及临时限速输入；
3)其他</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>--</td></tr><tr><td rowspan="2">60</td><td rowspan="2">ATS数据记录</td><td style='text-align: center;'>发送报警数据。ATS子系统可将自身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>--</td></tr><tr><td style='text-align: center;'>数据记录及回放。系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放的功能。综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30d</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>--</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>中控/站控转换</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">62</td><td rowspan="2">进路办理</td><td style='text-align: center;'>列车进路办理——自动。ATS系统应该具有列车自动办理进路的功能。ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>列车进路办理——人工。ATS系统应该具有手动办理进路的功能</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">62</td><td rowspan="3">进路办理</td><td style='text-align: center;'>列车进路办理——冲突检查。当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>与功能点“列车进路办理”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>进路办理。联锁应具备进路办理功能，包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>装有无效CBTC装备的列车进路办理。对于设备故障的CBTC列车或无装备的列车，在前方进路出清并重新开放后，装有无效CBTC装备的列车方可驶入</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>保护区段建立</td><td style='text-align: center;'>保护区段。联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>进路/区段锁闭</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭(并随后解锁)CBTC区域内的道岔、信号机、或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>65</td><td style='text-align: center;'>道岔单操、单锁</td><td style='text-align: center;'>道岔单操、单锁。联锁具备道岔单独操纵及锁闭的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>66</td><td style='text-align: center;'>车站/区间封锁</td><td style='text-align: center;'>封锁。系统应具有车站封锁、区间封锁的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">67</td><td rowspan="2">站台紧急关闭按钮</td><td style='text-align: center;'>响应站台紧急关闭按钮的按下。当ATP轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td><td style='text-align: center;'>与功能点“响应站台紧急关闭按钮”子功能点重复</td><td style='text-align: center;'>与功能点“响应站台紧急关闭按钮”子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>站台紧急关闭按钮。联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">68</td><td rowspan="2">CI自检、故障报警及数据记录</td><td style='text-align: center;'>故障监测：CI子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>监视和记录工作状态：CI子系统能监视和记录自身的工作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯丝状态监测及断丝报警、转辙机动作状态</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>69</td><td style='text-align: center;'>进路解锁及取消</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机、或轨道区段的能力：CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td><td style='text-align: center;'>与功能点“进路/区段锁闭”中子功能点重复</td><td style='text-align: center;'>与功能点“进路/区段锁闭”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>70</td><td style='text-align: center;'>计轴故障恢复</td><td style='text-align: center;'>计轴故障恢复。系统应具有计轴故障恢复的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>71</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>扣车。ATS系统应具有在车站扣车能力</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>72</td><td style='text-align: center;'>站控/遥控</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td><td style='text-align: center;'>与功能点“中控/站控转换”中子功能点重复</td><td style='text-align: center;'>与功能点“中控/站控转换”中子功能点重复</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>73</td><td style='text-align: center;'>CI权限设置</td><td style='text-align: center;'>操作权限设置。CI子系统能设置不同操作人员的权限，并有相应的安全操作手段</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td colspan="8">注1：表中的重复测试点表示该测试点在其他相应的功能点中已做要求。注2：表中功能点描述依据系统规范第2部分系统架构和功能分配技术要求。注3：“一”表示不适用。注4：“✓”表示适用。注5：“点式”表示在点式级别下测试。注6：“连续式”表示在连续式级别下测试。注7：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注8：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注9：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。</td></tr></table>

---

#### 6.2.2 互联互通 CI-CI 接口说明中功能分配

对 T/CAMET 04011.5 中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 2。

<div style="text-align: center;">表 2 互联互通计算机联锁(CI)间接口规范需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.4.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.4.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.4.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.4.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.4.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.4.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.4.7</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.4.8</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.4.9</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.4.10</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.4.11</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.4.12</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“—”表示不适用。注2：“✓”表示适用。注3：“点式”表示在点式模式下测试。注4：“连续式”表示在连续式模式下测试。注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。注8：表格中的章节号为T/CAMET 04011.5中章节号。</td></tr></table>

---

#### 6.2.3 互联互通跨线 ZC-ZC 接口说明中功能分配

对 T/CAMET 04011.4 中的跨线 ZC 与 ZC 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 3。

<div style="text-align: center;">表 3 跨线 ZC 与 ZC 接口规范部分需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.2.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.2.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.2.3</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.3.1.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.3.1.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.3.1.3</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.4.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.4.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.4.3</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.4.4</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.4.5</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.4.6</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.4.7</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.4.8</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“-”表示不适用。注2：“✓”表示适用。注3：“点式”表示在点式模式下测试。注4：“连续式”表示在连续式模式下测试。注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。注8：表格中的章节号为T/CAMET 04011.6中章节号。</td></tr></table>

---

#### 6.2.4 互联互通 ATS-ATS 接口说明中功能分配

对 T/CAMET 04011.6 中的需求进行识别，并根据其需求属性确定测试验证的阶段，如表 4 所示。

<div style="text-align: center;">表 4 互联互通 ATS 间接口规范需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.2.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.2.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.2.3.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.2.3.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.2.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.3.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.3.3</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.3.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.3.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.3.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.3.3.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.3.3.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.3.3.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.3.3.7</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>6.3.3.8</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1:“-”表示不适用。注2:“✓”表示适用。注3:“点式”表示在点式模式下测试。注4:“连续式”表示在连续式模式下测试。注5:“设计与实现”表示在互联互通第一阶段测试,由各厂家独立测试。注6:“室内平台”表示在互联互通第二阶段测试,由各厂家提供互联互通产品在互联互通实验室平台测试。注7:“试验线”表示在互联互通第三阶段测试,由各厂家提供互联互通产品在互联互通试验线测试。注8:表格中的章节号为T/CAMET 04011.6中章节号。</td></tr></table>

---

#### 6.2.5 互联互通 VOBC-ZC 接口说明中功能分配

对 T/CAMET 04011.2 中的 VOBC 与 ZC 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，如表 5 所示。

<div style="text-align: center;">表 5 CBTC 互联互通系统车地通信协议需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>5.1.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>5.1.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>5.1.3.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>5.1.3.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>5.1.3.3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>5.1.4</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>5.2.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>5.2.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>5.3.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>5.4.1.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>5.4.1.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>5.4.1.3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>5.4.1.4</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>5.4.1.5</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>5.4.1.6</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>5.4.2.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>5.4.2.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 5 CBTC 互联互通系统车地通信协议需求识别表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>5.4.2.3</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>5.4.2.4</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>5.5.1</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>5.5.2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“—”表示不适用。注2：“✓”表示适用。注3：“点式”表示在点式模式下测试。注4：“连续式”表示在连续式模式下测试。注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。注8：表格中的章节号为T/CAMET 04011.2中章节号。</td></tr></table>

#### 6.2.6 互联互通 VOBC-ATS 接口说明中功能分配

对 T/CAMET 04011.2 中的 VOBC 与 ZC 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，如表 6 所示。

<div style="text-align: center;">表 6 CBTC 互联互通系统车地通信协议需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.1.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.1.3.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.1.3.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 6 CBTC 互联互通系统车地通信协议需求识别表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.1.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.3.2.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.3.2.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.3.2.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.3.2.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.3.2.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.3.2.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.3.2.2.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>6.3.2.2.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>6.3.2.2.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>6.3.2.2.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>6.3.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>6.3.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“—”表示不适用。注2：“✓”表示适用。注3：“点式”表示在点式模式下测试。注4：“连续式”表示在连续式模式下测试。注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。注8：表格中的章节号为T/CAMET 04011.2中章节号。</td></tr></table>

---

#### 6.2.7 互联互通 VOBC-CI 接口说明中功能分配

对 T/CAMET 04011.2 中的 VOBC 与 CI 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，如表 7 所示。

<div style="text-align: center;">表 7 CBTC 互联互通系统车地通信协议需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>7.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>7.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>7.1.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>7.1.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>7.1.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>7.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>7.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>7.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>7.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>7.3.2.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>7.3.2.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>7.3.2.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>7.3.2.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>7.3.2.1.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>7.3.3.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>7.3.3.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>7.3.3.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 7 CBTC 互联互通系统车地通信协议需求识别表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>7.3.3.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>7.3.3.1.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td colspan="7">注1：“—”表示不适用。注2：“✓”表示适用。注3：“点式”表示在点式模式下测试。注4：“连续式”表示在连续式模式下测试。注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。注8：表格中的章节号为T/CAMET 04011.2中章节号。</td></tr></table>

### 6.3 互联互通测试需求

#### 6.3.1 定义测试需求的原则

定义测试需求应遵循以下原则：

## a） 可理解性

每一个测试需求应以易于理解的文字进行描述。对认证机构、用户、开发人员、测试人员而言，每一个测试需求都必须易于理解。在测试需求描述中，一些专业词汇要与文中术语、定义和缩略语中描述的内容一致，便于理解。

## b) 明确性

每一个测试需求必须具有唯一的编号。

## c）等级适用性

必须标明每一个测试需求适用于的运行等级。因为每一个测试需求

---

不一定适用于所有的运行等级。

## d）可追溯性

所有测试需求应明确的指向某一个或多个功能点或接口需求。

#### 6.3.2 测试需求编号命名原则

为满足测试需求定义的各种原则，测试需求的编号命名应遵循以下原则：

## a）包含功能点或接口编号

为便于追溯和理解，测试需求编号中需要包含功能点或接口编号。对于 T/CAMET 04010.1、T/CAMET 04010.2 因描述的是功能点，测试需求编号中体现功能点的编号，如“CBTC-F-ATP-1-CTC-1”。对于描述系统间接口的接口规范，如 T/CAMET 04011.1、T/CAMET 04011.4 等，测试需求编号中体现设备间接口，如“CBTC-IF-CI/CI-MSG-CTC-I”。

## b) 包含运行等级

为满足测试需求等级适用性的要求，测试需求编号中需要包含运行等级。点式部分以“ITC”进行描述，CBTC部分以“CTC”进行描述。

## c）包含唯一标识的序号

为满足测试需求唯一性的要求，对每个功能点中的测试需求进行编号，从1开始，相同运行等级的，顺序号不可以重复（如删除后的编号将不再使用）。

测试需求编号举例：CBTC-F-ATP-1-CTC-1。

#### 6.3.3 互联互通系统测试需求

6.2 节中描述了 T/CAMET 04010.2 中所有的互联互通相关的功能点，并对其进行了 ITC 点式和 CTC 连续式的划分。下面对 CTC 连续式部分的功能点进行测试和验证方法进行描述。

#### 6.3.4 初始化 CBTC 列车位置

初始化 CBTC 列车位置功能的测试和验证方法详见表 8～表 10。

---

<div style="text-align: center;">表 8 初始化 CBTC 列车位置(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-1-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>从设备故障中恢复的 CBTC 列车完成位置初始化。CBTC 列车位置初始化，并应自动检测每列装备 CBTC 设备的列车，从 CBTC 设备故障中恢复的列车无需手动输入列车位置或列车长度的数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于 CTC 控制级别的列车，ATP 故障，列车丢失定位，降级为 RM 模式；2) ATP 故障恢复后，经过两连续应答器，系统自动获得列车位置和运行方向</td></tr><tr><td colspan="2">注：表中功能内容是功能分配的原文描述（下同）。</td></tr></table>

<div style="text-align: center;">表 9 初始化 CBTC 列车位置(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-1-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车升级至 CBTC 级别。系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，至少应满足如下转换条件：1) ATP 车载设备无故障，且完成列车定位；2) ATP 车载设备收到 ATP 轨旁设备发送的有效 MA 信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备，处于 RM 控制等级的列车，无故障完成定位，呼叫响应 ZC 并建立连接；2) 列车收到 ZC 发送的有效 MA 信息后，具备升级条件，升级为 CBTC 级别</td></tr></table>

<div style="text-align: center;">表 10 初始化 CBTC 列车位置(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-1-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车升级至 CBTC 级别。系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，至少应满足如下转换条件：1) ATP 车载设备无故障，且完成列车定位；2) ATP 车载设备收到 ATP 轨旁设备发送的有效 MA 信息</td></tr></table>

---

<div style="text-align: center;">表 10 初始化 CBTC 列车位置(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于点式控制等级的列车，呼叫响应 ZC 并建立连接；2) 列车收到 ZC 发送的有效 MA 信息后，具备升级条件，升级为 CBTC 级别</td></tr></table>

#### 6.3.5 确定 CBTC 列车位置

确定 CBTC 列车位置功能的测试和验证方法详见表 11 ~ 表 16。

<div style="text-align: center;">表 11 确定 CBTC 列车位置(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定列车长度。CBTC 应能确定列车长度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 与 ATS 建立连接的连续级列车，向 ATS 报告列车位置；2) 与 ZC 建立连接的连续级列车，向 ZC 报告列车长度</td></tr></table>

<div style="text-align: center;">表 12 确定 CBTC 列车位置(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定 CBTC 列车位置。CBTC 列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 通过列车位置检测设备完成连续式列车的列车位置的安全和精确定位（包括列车的正反向运行）；2) 连续等级列车通过车地通信向轨旁 ZC 和 ATS 系统发送列车位置信息，包括列车车头、车尾以及位置的不确定性等内容</td></tr></table>

<div style="text-align: center;">表 13 确定 CBTC 列车位置(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>位置误差校正。CBTC 列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td></tr></table>

---

<div style="text-align: center;">表 13 确定 CBTC 列车位置(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 系统，处于连续式控制级别的车载 ATP 设备，在向 ATS 以及 ZC 汇报列车位置的同时，也汇报车载 ATP 系统考虑到安全因素而计算的位置不确定性（包括列车的正反向运行）。2) ATS 系统显示列车位置考虑列车位置的不确定性，ZC 系统计算列车移动授权考虑列车位置的不确定性</td></tr></table>

<div style="text-align: center;">表 14 确定 CBTC 列车位置(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车完整性检测、CBTC 系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)处于连续式控制级别的车载 ATP 设备，检测到本车的完整性丢失，列车实施紧急制动，并丢失定位；2)列车位置丢失后，联锁和 ATS 按照物理区段占用进行显示；3)列车降级后（丢定位），ZC 通过判断超时后，不再给列车发送移动授权。若后车 MA 位于丢失完整性列车车尾，则 CBTC 系统对后车进行安全防护</td></tr></table>

<div style="text-align: center;">表 15 确定 CBTC 列车位置(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定CBTC列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定列车停站位置.CBTC系统应根据不同的列车长度,确定列 车的停站位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车,在停站时,根据本 身的编组和列车长度,以及电子地图中存储的针对不同编组的停车 点位置,进行停车(包括正反向进站)</td></tr></table>

---

<div style="text-align: center;">表 16 确定 CBTC 列车位置(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>退行防护。ATP 车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于连续式控制级别的列车，当退行速度超过允许值时，列车紧急制动；ZC 向后车发送安全间隔防护的移动授权；2) 装备 CBTC 设备、处于连续式控制级别的列车，当退行距离超过允许值时，列车紧急制动；ZC 向后车发送安全间隔防护的移动授权</td></tr></table>

#### 6.3.6 确定轨道区段占用状态

确定轨道区段占用状态功能的测试和验证方法详见表 17～表 20。

<div style="text-align: center;">表 17 确定轨道区段占用状态(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>轨道区段的占用状态：CBTC系统可根据轨旁次级占用检测设备提供的信息、结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于连续式控制级别的列车占用某轨道区段；2) 轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给地面ATP设备；3) 地面ATP设备根据列车位置和联锁报告的区段占用信息，确定轨道区段的占用状态，发送给联锁</td></tr></table>

---

<div style="text-align: center;">表 18 确定轨道区段占用状态(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1）某轨道区段上有两辆以上的处于连续式控制等级的列车；2）轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给地面ATP设备；3）地面ATP设备根据列车位置和联锁报告的区段占用信息，确定轨道区段的占用状态，发送给联锁</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//424456b3-b5fa-43ec-b79f-de94cf2b5321/markdown_0/imgs/img_in_image_box_255_567_595_639.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A28%3A11Z%2F-1%2F%2F935ed0577cc1005c7d450996cdab7eef63083a3f8377960ce5c5bd1ee3aadabd" alt="Image" width="40%" /></div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-OTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1）某轨道区段上有两辆列车，一辆由连续等级降级到非连续式控制等级的列车，一辆处于连续式控制等级；2）轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给地面ATP设备；3）地面ATP设备根据列车位置和联锁报告的区段占用信息，确定轨道区段的占用状态，发送给联锁</td></tr></table>

---

<div style="text-align: center;">表 20 确定轨道区段占用状态(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>前方轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>前方轨道区段占用状态。当CBTC列车前方区段被故障列车或者非CBTC装备列车占用时，CBTC系统应根据前方区段占用状态确定CBTC列车的安全边界</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)某轨道区段上有两辆列车，后车为连续级列车；2)前车是由连续等级降级到非连续式控制等级的列车，确定后车连续级列车的情况</td></tr></table>

#### 6.3.7 防护列车丢失位置报告

防护列车丢失位置报告功能的测试和验证方法详见表21。

<div style="text-align: center;">表 21 防护列车丢失位置报告</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>防护列车丢失位置报告</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-4-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>防护列车丢失位置报告，当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)车载ATP检测到位置丢失，列车紧急制动；2)地面ATP设备接收到联锁通过检测到的区段占用情况，结合本身的列车管理中无车汇报占用该区段的信息，向后车发送的移动授权均不会延伸到该无位置汇报的列车占用区段</td></tr></table>

#### 6.3.8 防护列车完整性丢失

防护列车完整性丢失功能的测试和验证方法详见表22。

<div style="text-align: center;">表 22 防护列车完整性丢失</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>防护列车完整性丢失</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-5-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车完整性丢失防护。在检测到列车完整性丢失时，CBTC系统 将提供移动授权防护，避免其他列车进入无位置汇报列车占用的 区段</td></tr></table>

---

<div style="text-align: center;">表 22 防护列车完整性丢失(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>防护列车完整性丢失</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)车载ATP检测到列车完整性丢失，列车紧急制动并丢失定位；2)地面ATP设备接收到联锁通过检测到的区段占用情况，结合本身的列车管理中无车汇报占用该区段的信息，向后车发送的移动授权均不会延伸到该无位置汇报的列车占用区段</td></tr></table>

#### 6.3.9 确定前方 CBTC 列车位置

确定前方 CBTC 列车位置功能的测试和验证方法详见表 23。

<div style="text-align: center;">表 23 确定前方 CBTC 列车位置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定前方 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-6-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 列车前方位置对于每辆 CBTC 列车，应确定列车前方的 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 所有与地面 ATP 设备建立连接的列车，运行模式有 RM 有位置、点式、连续式控制等级的列车，均向地面 ATP 设备报告列车位置；2) 地面 ATP 设备为当前列车计算移动授权时，移动授权终点不会越过前方列车</td></tr></table>

#### 6.3.10 确定前方安全进路限制

确定前方安全进路限制功能的测试和验证方法详见表24。

<div style="text-align: center;">表 24 确定前方安全进路限制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定前方安全进路限制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-7-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>前方安全进路限制。对于每辆CBTC列车，系统应确定列车的安全进路位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，前方进路锁闭并开放，地面ATP设备将移动授权延伸至进路内方</td></tr></table>

---

#### 6.3.11 确定移动授权

确定移动授权功能的测试和验证方法详见表25。

<div style="text-align: center;">表 25 确定移动授权</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定移动授权</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-8-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移动授权的确定。为对列车进行合适的移动防护限制，CBTC系统应估算最大移动授权限制位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>地面ATP设备根据前行列车位置以及联锁向其发送的列车占用检测设备状态信息，计算危险点，地面ATP设备提供给列车的最大移动授权限制位置不能越过任何危险点，并且向车载ATP发送移动授权范围内的临时限速信息，车载ATP根据接收到的移动授权结合本身电子地图的限速信息进行防护</td></tr></table>

#### 6.3.12 确定目标点

确定目标点功能的测试和验证方法详见表26。

<div style="text-align: center;">表 26 确定目标点</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定目标点</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-9-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定目标点为了确保列车不超过移动授权，CBTC系统应确定一个目标点</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于连续式控制级别的列车不能越过移动授权终点</td></tr></table>

#### 6.3.13 响应紧急关闭按钮

响应紧急关闭按钮的测试和验证方法详见表27和表28。

<div style="text-align: center;">表 27 响应紧急关闭按钮(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-10-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>响应紧急关闭按钮的按下。当 ATP 轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td></tr></table>

---

<div style="text-align: center;">表 27 响应紧急关闭按钮(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 联锁检测到站台紧急关闭按钮被按下，将该按钮状态发送给地面ATP设备；2) 地面ATP设备根据列车位置报告判断列车未进入站台区域，则向车载ATP发送控制命令信息，信息中包括站台紧急关闭按钮被按下的信息，由车载ATP采取措施保证安全</td></tr></table>

<div style="text-align: center;">表 28 响应紧急关闭按钮(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-10-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>响应紧急关闭按钮的按下。当ATP轨旁设备接收到站台紧急关闭按钮被接下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 联锁检测到站台紧急关闭按钮被按下，将该按钮状态发送给地面ATP设备；2) 地面ATP设备根据列车位置报告判断列车已进入站台区域，则向车载ATP发送控制命令信息，信息中包括站台紧急关闭按钮被按下的信息，由车载ATP采取措施保证安全</td></tr></table>

#### 6.3.14 道岔状态防护

道岔状态防护功能的测试和验证方法详见表29和表30。

<div style="text-align: center;">表 29 道岔状态防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔状态防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-11-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>道岔状态防护：CBTC系统应控制区域内道岔状态进行防护，当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于连续式控制级别的列车，前方移动授权范围内有道岔；2) 列车未驶入道岔时，设置道岔状态丢失，验证移动授权回撤至道岔区域的边界位置</td></tr></table>

---

<div style="text-align: center;">表 30 道岔状态防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔状态防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-11-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>道岔状态防护。CBTC系统应控制区域内道岔状态进行防护，当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于连续式控制级别的列车，前方移动授权范围内有道岔；2) 列车驶入道岔，设置道岔状态丢失，验证列车实施紧急制动</td></tr></table>

#### 6.3.15 车载故障处理

车载故障处理功能的测试和验证方法详见表31～表34。

<div style="text-align: center;">表 31 车载故障处理（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理：列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车、ATP 检测到本车的非预期移动超过配置值后输出紧急制动，并给出报警提示（如果线路条件允许，需要线路具有一定的坡度）</td></tr></table>

<div style="text-align: center;">表 32 车载故障处理(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示、与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车，检测到车载设备故障，立即施加紧急制动，并给出报警提示</td></tr></table>

---

<div style="text-align: center;">表 33 车载故障处理(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车，检测到超过系统允许范围的车地通信中断，给出报警提示，立即施加紧急制动</td></tr></table>

<div style="text-align: center;">表 34 车载故障处理(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理 列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车、轨旁 ATP 故障，本控区列车紧急制动后降级运行</td></tr></table>

#### 6.3.16 固定速度限制防护

固定速度限制防护功能的测试和验证方法详见表35和表36.

<div style="text-align: center;">表 35 固定速度限制防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>固定速度限制防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-13-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>固定线路速度限制。CBTC 应提供固定线路限速的限制防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车，在运行时，利用自己电子地图中存储的线路限速，计算速度曲线，对线路上的固定限速进行防护</td></tr></table>

---

<div style="text-align: center;">表 36 固定速度限制防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>固定速度限制防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-13-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车构造速度限制。系统应提供列车构造速度的防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制级别的列车，在运行时，计算的可运行的最高速度不大于列车自身的构造速度，验证列车计算的速度曲线中最高速度不超过列车的构造速度</td></tr></table>

#### 6.3.17 临时限速限制防护

临时限速限制防护功能的测试和验证方法详见表37。

<div style="text-align: center;">表 37 临时限速限制防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>临时限速限制防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-14-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>临时限速限制防护.临时限制速度限制CBTC应按照系统设置的临时限速,为列车计算移动授权,对临时限速进行防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)ATS设备支持临时限速的设置并向轨旁ATP设备发送;2)轨旁ATP会将移动授权范围内的临时限速发送给车载ATP;3)车载ATP以低于临时限速值的速度,通过临时限速区段</td></tr></table>

#### 6.3.18 确定制动曲线

确定制动曲线功能的测试和验证方法详见表38～表40。

<div style="text-align: center;">表 38 确定制动曲线(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-15-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>目标点的制动曲线</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，根据轨旁ATP设备发送的移动授权，结合本身存储的和前方线路的限速情况，计算目标点的制动曲线</td></tr></table>

---

<div style="text-align: center;">表 39 确定制动曲线(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-15-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>考虑最不利情况下的影响。CBTC 的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于连续式控制等级的列车，在计算速度曲线时，要考虑最差情况下系统偏差、反应系数和反应时间的补偿</td></tr></table>

<div style="text-align: center;">表 40 确定制动曲线(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>核心控制曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-FATP-T5-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>防止制动曲线超过速度限制CBTC应保证制动曲线在超过固定或临时限速之前减速</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于连续式控制等级运行的列车，在经过固定限速区段，如道岔区段时，提前减速；2) 装备CBTC设备、处于连续式控制等级运行的列车，在经过临时限速区段前，提前减速</td></tr></table>

#### 6.3.19 列车超速防护

列车超速防护功能的测试和验证方法详见表41～表43。

<div style="text-align: center;">表 41 列车超速防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定授权速度。CBTC应基于ATP曲线，确定列车当前位置的限制速度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级运行的列车，根据移动授权和线路速度计算ATP曲线，并基于ATP曲线，确定列车当前位置的限制速度</td></tr></table>

---

<div style="text-align: center;">表 42 列车超速防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATP曲线。CBTC应为每辆列车计算完整的ATP曲线</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，根据移动授权和线路速度计算ATP曲线，并基于ATP曲线，确定列车当前位置的限制速度</td></tr></table>

<div style="text-align: center;">表 43 列车超速防护(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>速度监督和防护.如果列车实际速度超过限制速度,CBTC应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级运行的列车,当列车实际运行速度超过限制速度时,实施紧急制动</td></tr></table>

#### 6.3.20 列车速度测定

列车速度测定功能的测试和验证方法详见表44。

<div style="text-align: center;">表 44 列车速度测定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车速度测定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-17-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，利用测速测距设备测量并计算列车的实际速度，检查速度满足分辨率和精度的要求</td></tr></table>

---

#### 6.3.21 测速误差补偿

测速误差补偿功能的测试和验证方法详见表45。

<div style="text-align: center;">表 45 测速误差补偿</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>测速误差补偿</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-18-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>测速误差补偿.CBTC系统应能够补偿测速误差产生的影响,并对测速作出合适的补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车,在空转打滑时,应能够补偿测速误差产生的影响,并对测速作出合适的补偿</td></tr></table>

#### 6.3.22 零速状态确定

零速状态确定功能的测试和验证方法详见表46。

<div style="text-align: center;">表 46 零速状态确定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>零速状态确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-19-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>零速状态确定 CBTC 应确定零速度状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制等级的列车，可以进行零速状态确认</td></tr></table>

#### 6.3.23 列车运行方向确定

列车运行方向确定功能的测试和验证方法详见表47。

<div style="text-align: center;">表 47 列车运行方向确定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行方向确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-20-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车运行方向：CBTC系统应确定每辆CBTC列车的实际运行方向</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于连续式控制等级的列车，明确自己的运行方向；2) 此时列车与联锁和ATS建立连接，ATP会将运行方向发送给联锁和ATS设备；3) 此时列车与ZC建立连接，ATP会将运行方向发送给ZC设备</td></tr></table>

---

#### 6.3.24 列车运行方向防护

列车运行方向防护功能的测试和验证方法详见表48和表49。

<div style="text-align: center;">表 48 列车运行方向防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行方向防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-21-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>监督/防护运行方向。如果列车实际运行方向与授权的列车运行方向不一致，CBTC 应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于连续式控制等级的列车，列车实际运行方向与 ZC 发送的移动授权方向不一致，ATP 实施紧急制动（折返过程除外）；2) 此时列车与 ATS 建立连接，ATP 会将紧急制动状态发送给 ATS 设备；3) 此时列车与 ZC 建立连接，ATP 会将紧急制动状态发送给 ZC 设备</td></tr></table>

<div style="text-align: center;">表 49 列车运行方向防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行方向防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-21-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>监督/防护运行方向 如果列车实际运行方向与授权的列车运行方向不一致，CBTC应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于RM或点式控制等级的列车，列车实际运行方向与ZC发送的移动授权方向不一致，ATP是否会实施紧急制动因厂家而异，自行测试；2) 此时列车与ATS建立连接，ATP会将是否紧急制动的状态发送给ATS设备；3) 此时列车与ZC建立连接，ATP会将是否紧急制动的状态发送给ZC设备</td></tr></table>

#### 6.3.25 越过移动授权终点防护

越过移动授权终点防护功能的测试和验证方法详见表50。

---

<div style="text-align: center;">表 50 越过移动授权终点防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>越过移动授权终点防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-23-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>越过移动授权终点的响应。列车越过移动授权终点时，系统应实 施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)装备CBTC设备、处于连续式控制等级的列车，越过移动授权终 点，系统实施紧急制动； 2)此时列车与ATS建立连接，ATP会将紧急制动状态发送给ATS 设备</td></tr></table>

#### 6.3.26 退行防护

参考6.3.5中表16的内容CIATION

#### 6.3.27 移动授权更新超时防护

移动授权更新超时防护功能的测试和验证方法详见表 51 和表 52。

表 51 移动授权更新超时防护—


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-APP-24-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移动授权更新超时的防护移动授权更新超时，系统应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车、发生超过系统允许范围的车地通信中断时，车载设备的移动授权无法及时更新，车载ATP紧急制动</td></tr></table>

<div style="text-align: center;">表 52 移动授权更新超时防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-24-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移动授权更新超时的防护移动授权更新超时，系统应实施紧急 制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、点式控制等级的列车，与轨旁 ATP设备建立连接后，发生超过系统允许范围的车地通信中断时，车 载设备是否紧急制动根据各厂家不同面不同，根据具体情况测试</td></tr></table>

---

#### 6.3.28 紧急制动缓解

紧急制动缓解功能的测试和验证方法详见表 53。

<div style="text-align: center;">表 53 紧急制动缓解</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>紧急制动缓解</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-25-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>紧急制动缓解，在保证安全的条件下，系统可以缓解已施加的紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于连续式控制等级的列车，因某种原因施加了紧急制动，如退行防护、设备故障等，在施加EB的触发条件消失，可以缓解该紧急制动</td></tr></table>

#### 6.3.29 车门允许

车门允许功能的测试和验证方法详见表 54 ~ 表 58。

<div style="text-align: center;">表 54 车门允许（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1) 列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2) 开门侧与站台一致；3) 列车零速；4) 保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 54 车门允许(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，满足以下条件后，车载ATP允许打开对应侧车门和站台门。1) 停准在指定的停车点；2) 开门侧与站台一致；3) 列车零速；4) 保持制动已施加。在AM驾驶下，测试自开自关、自开人关、人开人关三种开门方式。针对反向进站进行相同的测试项</td></tr></table>

<div style="text-align: center;">表 55 车门允许(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前,应满足下列条件:
1)列车“正确对齐”在一个指定的停止点,停止点偏差在允许范围内;
2)开门侧与站台一致;
3)列车零速;
4)保持制动已施加.
列车在车站规定的位置停准停稳后,车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门,并可选择通过自开自关、自开人关、人开关三种方式,自动或者人工打开车门
在AM驾驶模式下,可提供三种开门方式,CM驾驶模式下,仅能实现人工开门
列车在车站停车超出停车窗范围,车载设备应不允许车门和站台门打开,司机可在车载设备防护条件下前进或后退,直至停车对位</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车、满足以下条件后,车载ATP允许打开对应侧车门和站台门或双侧车门和站台门.
1)停准在指定的停车点,且在停车窗内;
2)开门侧与站台一致;
3)列车零速;
4)保持制动已施加.
在CM驾驶下,只能人工打开车门</td></tr></table>

---

<div style="text-align: center;">表 56 车门允许(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前,应满足下列条件:1)列车“正确对齐”在一个指定的停止点,停止点偏差在允许范围内;2)开门侧与站台一致;3)列车零速;4)保持制动已施加.列车在车站规定的位置停准停稳后,车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门,并可选择通过自开自关、自开人关、人开人关三种方式,自动或者人工打开车门.在AM驾驶模式下,可提供三种开门方式,CM驾驶模式下,仅能实现人工开门.列车在车站停车超出停车窗范围,车载设备应不允许车门和站台门打开,司机可在车载设备防护条件下前进或后退,直至停车对位</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车,在车站停车时,未到停车窗,司机可控制列车继续前进,到停车窗后停车,确保满足以下条件后,车载ATP允许打开对应侧车门和站台门或双侧车门和站台门。1)开门侧与站台一致;2)列车零速;3)保持制动已施加</td></tr></table>

<div style="text-align: center;">表 57 车门允许（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；</td></tr></table>

---

<div style="text-align: center;">表 57 车门允许(四)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处门连片式控制等级的列车，在车站停车时，越过停车窗，司机可控制列车退行，在满足退行距离和退行速度下，在停车窗停车，确保满足以下条件后，车载ATP允许打开对应侧车门和站台门或双侧车门和站台门。1)开门时与站台一致；2)列车零速；3)保持制动已施加</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>市轨道车允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。</td></tr></table>

---

<div style="text-align: center;">表 58 车门允许(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，在车站停车时，以下任一条件不满足，车载ATP不给出开门允许。1)列车停准在指定的停车点，且在停车窗内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加</td></tr></table>

#### 6.3.30 站台门控制

站台门控制功能的测试和验证方法详见表59和表60。

<div style="text-align: center;">表 59 站台门控制(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门控制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-27-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门控制 CBTC 应打开站台门之前，应检查是否满足下列条件：1) 列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2) 站台门侧与车门侧一致；3) 列车零速；4) 保持制动已施加</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制等级的列车，在下列条件满足时提供门允许，并向联锁发送打开站台门的请求，打开站台门前，确认满足下速条件后，站台门打开。1) 列车停准在指定的停车点，且在停车窗内；2) 站台门侧与车门侧一致；3) 列车零速；4) 保持制动已施加</td></tr></table>

---

<div style="text-align: center;">表 60 站台门控制(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门控制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-27-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门控制。CBTC应打开站台门之前，应检查下列条件满足：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，有门允许，并向联锁发送打开站台门的请求；联锁在打开站台门前，如果出现以下任一情况，则车载系统不向联锁发送开门命令。1)列车不在停车窗内；2)站台门侧与车门侧不一致；3)列车未停稳；4)保持制动未施加</td></tr></table>

#### 6.3.31 车门防护

车门防护功能的测试和验证方法详见表61～表65。

<div style="text-align: center;">表 61 车门防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车 移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，车门未被旁路且车 门未处于“关闭且锁闭”状态时，系统不允许列车移动</td></tr></table>

<div style="text-align: center;">表 62 车门防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车 移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，车门被旁路且车门 未处于“关闭且锁闭”状态时，列车可以移动</td></tr></table>

---

<div style="text-align: center;">表 63 车门防护(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级列车，车门处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

<div style="text-align: center;">表 64 车门防护(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门状态丢失防护 列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1) 切除牵引但不实施制动；2) 不切除牵引，也不实施制动，列车运行至下一座车站；3) 实施紧急制动；4) 实施全常用制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制级别的列车，在运行过程中，车门未被旁路的情况下，监督到车门打开，可以采取下列措施之一：1) 切除牵引但不实施制动；2) 不切除牵引，也不实施制动，列车运行至下一座车站；3) 实施紧急制动；4) 实施全常用制动</td></tr></table>

<div style="text-align: center;">表 65 车门防护(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门状态丢失防护。列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1) 切除牵引但不实施制动；</td></tr></table>

---

<div style="text-align: center;">表 65 车门防护(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>2) 不切除牵引,也不实施制动,列车运行至下一座车站;3) 实施紧急制动;4) 实施全常用制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制级别的列车,在运行过程中,车门被旁路的情况下,监督到车门打开,不会采取下列任一种措施:1) 切除牵引但不实施制动;2) 实施紧急制动;3) 实施全常用制动</td></tr></table>

#### 6.3.32 车门防护切除

车门防护切除功能的测试和验证方法详见表66。

表 66 车门防护切除


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护切除</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-29-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护切除。系统在车门故障时可提供车门切除功能，此时ATP不再对车门状态进行防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTP设备、处于连续式控制等级的列车，车门故障时处于打开状态，司机操作使车门处于车门切除状态；2) 列车可以移动</td></tr></table>

#### 6.3.33 站台门防护

站台门防护功能的测试和验证方法详见表67和表68。

<div style="text-align: center;">表 67 站台门防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-30-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门状态丢失的响应。当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>一装备CBTC设备、处于连续式控制等级的列车，位于站台外或正在进入站台，进站进路已排列并开放，此时站台门关闭状态丢失，CBTC系统需对故障区域进行防护，避免列车进入故障区域</td></tr></table>

---

<div style="text-align: center;">表 68 站台门防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-30-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门状态丢失的响应。当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于连续式控制等级的列车，已进入站台，此时站台门关闭状态丢失，CBTC系统需禁止列车运行</td></tr></table>

#### 6.3.34 列车折返

列车折返功能的测试和验证方法详见表69～表71。

<div style="text-align: center;">表 69 列车折返(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATP监督下的人工折返模式，站后折返：列车处于连续式控制等级，司机人工驾驶列车由站台运行至折返区域，完成相应的确认操作，自动切换列车尾端驾驶，然后人工驾驶列车进入发车股道，定点停车后，打开车门和站台门</td></tr></table>

<div style="text-align: center;">表 70 列车折返(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATP监督下的人工折返模式，站前折返：列车处于连续式控制等级，当列车在折返站定点停车后，司机完成相应的确认操作，自动切换列车尾端驾驶，在此过程中司机根据上下客站台的设置打开或关闭车门和站台门</td></tr></table>

---

<div style="text-align: center;">表 71 列车折返(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATO无人自动折返模式，站后折返：列车处于连续式控制等级，AM驾驶模式，当列车在折返站规定的停车时间结束及旅客下车完毕，关闭车门和站台门，司机完成相应的确认操作后，列车可在无人驾驶的情况下，从到达站台自动驾驶进入和折出折返线，最后进入发车股道并定点停车，自动打开车门和站台门，司机开启反向驾驶端，完成无人自动折返2) ATO有人自动折返模式：列车处于连续式控制等级，AM驾驶模式，列车在折返站规定的站停时间结束及旅客下车完毕，关闭车门和站台门，司机完成相应的操作并确认发车后，列车自动驾驶进入折返线停稳后，司机进行相应的确认操作，开启反向驾驶端，按压发车或确认按钮，列车自动驾驶进入发车股道自动打开车门，完成有人自动折返</td></tr></table>

#### 6.3.35 车载 ATP 界面功能

车载 ATP 界面功能的测试和验证方法详见表 72 和表 73.

<div style="text-align: center;">表 72 车载 ATP 界面功能(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 显示数据 CBTC 车载显示屏 显示 ATP 数据应包括：1) 列车运行模式；2) CBTC 运行状态；3) 当前列车速度；4) 当前最大允许 CBTC 速度；5) 超速报警</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制等级的列车，人机界面上要显示：1) 列车运行模式；2) CBTC 运行状态；3) 当前列车速度；4) 当前最大允许 CBTC 速度；5) 超速报警</td></tr></table>

---

<div style="text-align: center;">表 73 车载 ATP 界面功能(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 输入数据。用户 ATP 信息输入到 CBTC 应包括：1) 运行模式选择；2) 超速报警情况确认</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于连续式控制等级的列车、ATP 设备的人机界面上支持的输入信息：1) 运行模式选择；2) 超速报警情况确认</td></tr></table>

#### 6.3.36 ATP 自诊断、故障报警及数据记录

ATP 白诊断、故障报警及数据记录功能的测试和验证方法详见表 74。

<div style="text-align: center;">表 74 ATP 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATP自诊断、故障报警及数据记录</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-33-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自诊断、故障报警及数据记录。ATP车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存7d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备的列车、处于连续式控制等级的列车，需具备自诊断、故障报警及数据记录的功能：1) ATP车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印；2) 记录的内容包括事件的时间和日期，并至少保存7d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr></table>

#### 6.3.37 模式转换

模式转换功能的测试和验证方法详见表 75 ~ 表 81。

---

<div style="text-align: center;">表 75 模式转换(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车驾驶模式。列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）、列车自动防护模式（CM）为列车正常运行模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备的列车，列车应具有的驾驶模式包括：1)列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）；2)列车自动运行模式（AM）、列车自动防护模式（CM）为列车正常运行模式</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATF-34-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车，驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的人工转换，CM→AM：1)列车处于连续式控制等级的CM模式，具备ATO启动条件时，司机点击ATO启动确认按钮，列车进入连续式控制等级的AM模式运行，同时验证了由低等级转为高等级时，不停车转换驾驶模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

---

<div style="text-align: center;">表 77 模式转换(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式。</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的自动转换，RM→CM；1)列车处于RM有位置模式，与轨旁ATP设备建立通信，并获得移动授权，验证列车升级为连续式控制等级的CM模式，同时验证了由低等级转为高等级时，不停车转换驾驶模式；2)对于模式转换，车载设备进行记录和显示。</td></tr></table>

<div style="text-align: center;">表 78 模式转换(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换：列车驾驶模式等级由高至低分别为：AM、CM、RM 各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM 转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的自动转换，点式控制等级CM→连续式控制等级CM：1)列车处于点式控制等级，驾驶模式为CM，与轨旁ATP设备建立通信，并获得移动授权，验证列车升级为连续式控制级别的CM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

---

<div style="text-align: center;">表 79 模式转换(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换.列车驾驶模式等级由高至低分别为：AM、CM、RM.各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车.驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的自动转换，点式控制等级AM→连续式控制等级AM：1)列车处于点式控制等级，驾驶模式为AM，与轨旁ATP设备建立通信，并获得移动授权，验证列车升级为连续式控制等级的AM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

<div style="text-align: center;">表 80 模式转换(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的转换，AM、CM转为RM时：1)列车处于连续式控制等级AM模式，进入转换轨，速度低于预定值，ATP人机界面提示要转换为RM，停车后，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

---

<div style="text-align: center;">表 81 模式转换(ヒ)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的转换，列车进入车辆段/停车场时，AM、CM转为RM时：1)列车处于连续式控制等级AM模式，进入进段转换轨，速度低于预定值，ATP人机界面提示要转换为RM，在不停车情况下，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

#### 6.3.38 ZC间移交

ZC间移交功能的测试和验证方法详见表82～表85

<div style="text-align: center;">表 82 ZC 间移交(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC间移交</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-35-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>两条连续式列车控制级别线路间应设置移交边界和移交重叠区：列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交、接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>列车未越过移交边界前的测试需求：列车进入移交重叠区后，未越过移交边界前，车载ATP设备同时与移交、接管线路的轨旁ATP设备建立通信，此时列车采用移交线路的轨旁ATP设备发送的MA；移交、接管线路上的轨旁ATP设备互传线路状态、列车位置等信息，移交、接管线路的轨旁ATP设备均向列车发送MA</td></tr></table>

---

<div style="text-align: center;">表 83 ZC 间移交(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC间移交</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-35-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>两条连续式列车控制级别线路间应设置移交边界和移交重叠区：列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交、接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>列车越过移交边界后的测试需求：列车越过移交边界后，车载ATP设备断开与移交线路的轨旁ATP设备的通信，只与接管线路的轨旁ATP设备通信，并采用其MA；移交线路的轨旁ATP设备不再向列车发送MA</td></tr></table>

---

<div style="text-align: center;">表 85 ZC 间移交(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC间移交</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-35-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>两条连续式列车控制级别线路间应设置移交边界和移交重叠区：列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交、接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>RM有位置列车和点式列车是否能够移交，因厂家而异，根据实际情况进行测试</td></tr></table>

#### 6.3.39 多车追踪防护功能

多车追踪防护功能的测试和验证方法详见表86和表87。

<div style="text-align: center;">表 86 多车追踪防护功能（·）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>多车追踪防护功能(两车)</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-76-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>系统应具备过车追踪防护功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)两列CTC车可以实现在同轴追踪防护；2)两列CTC车可以实现在相邻计轴追踪防护；3)两列CTC车可以实现在间隔计轴追踪防护；4)列车CTC车和一列非CTC车可以实现追踪防护</td></tr></table>

<div style="text-align: center;">表 87 多车追踪防护功能(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>多车追踪防护功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-76-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>系统应具备过车追踪防护功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 三列 CTC 车可以实现在同计轴追踪防护；2) 三列 CTC 车可以实现在相邻计轴追踪防护</td></tr><tr><td colspan="2">注：两列车以上的追踪防护测试按项目具体要求选测。</td></tr></table>

---

#### 6.3.40 电子地图存储

电子地图存储功能的测试和验证方法详见表88。

<div style="text-align: center;">表 88 电子地图存储</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-36-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备的车载ATP系统处于连续式控制等级的列车，为支持互联互通项目中多条线路的跨线运行，ATP车载设备需根据运行范围，存储相应的电子地图。为了实现列车的跨线运行，轨旁设备应获取相邻线路的部分线路信息，以支持列车移交的完成，因此要存储对应区域的电子地图</td></tr></table>

#### 6.3.41 停稳停准判断

参考6.3.29中对应的功能点，见表54～表58。

#### 6.3.42 确定 ATO 曲线

确定 ATO 曲线功能的测试和验证方法详见表 89。

<div style="text-align: center;">表 89 确定 ATO 曲线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 ATO 曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-38-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定 ATO 曲线 CBTC 系统应为列车确定 ATO 曲线。ATO 子系统在 ATP 子系统的保护下，根据 ATS 子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制。ATO 子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在 ATP 系统的监督下，处于自动驾驶模式下的连续式列车在线运行，系统自动计算 ATO 运行曲线，并控制列车按照 ATO 曲线运行，包括列车的加速、减速、惰行和巡航；
2) 自动驾驶列车通过车地通信接收 ATS 系统发送的站间走行时分和停站时间以及 ATP 提供的列车限制速度及距离等参数计算 ATO 控车曲线</td></tr></table>

---

#### 6.3.43 精确停车

精确停车功能的测试和验证方法详见表90。

<div style="text-align: center;">表 90 精确停车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>精确停车</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-39-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进站精确停车 ATO 子系统应具备列车进站精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 系统设置不同编组长度的列车；2) 处于自动驾驶模式下的连续式列车执行进站停车，并保证列车在指定位置精确停车</td></tr></table>

#### 6.3.44 根据 ATO 曲线调整列车速度

根据 ATO 曲线调整列车速度功能的测试和验证方法详见表 91。

<div style="text-align: center;">表 91 根据 ATO 曲线调整列车速度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>根据ATO曲线调整列车速度</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-40-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车调速 CBTC系统应根据ATO曲线调整列车速度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的连续式列车在线运行，ATO系统依据列车运行信息，包括运行时间、限速点、停车点等，控制列车速度，保证在正常运行</td></tr></table>

#### 6.3.45 开关车门

开关车门功能的测试和验证方法详见表92～表95。

<div style="text-align: center;">表 92 开关车门(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>开列车门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-43-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>开列车门。在 AM 驾驶模式下，在 ATP 的防护下可提供自动开门或者人工开门两种开门方式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的连续式列车到站停稳停准后，依据门控模式等条件自动或人工开启列车车门</td></tr></table>

---

<div style="text-align: center;">表 93 开关车门(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>开站台门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-43-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>开站台门。CBTC系统应能自动开启站台门</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)连续式列车到站停稳停准后，依据门控模式等条件自动发送开启站台门的联控命令；2)轨旁联锁系统接收联控命令并通过站台门接口控制站台门打开</td></tr></table>

<div style="text-align: center;">表 94 开关车门(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>关闭列车门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-FAO-43-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>关闭列车门。在AM驾驶模式下，可提供自动关门或者人工关门两种关门方式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的连续式列车到站并执行完成在站作业后，依据门控模式等条件自动或人工关闭列车车门</td></tr></table>

<div style="text-align: center;">表 95 开关车门(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>关闭站台门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-43-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>关闭站台门，CBTC系统应能自动关闭站台门</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 连续式列车到站并执行完成在站作业后，依据门控模式等条件自动发送关闭站台门的联控命令；2) 轨旁联锁系统接收联控命令并通过站台门接口控制站台门关闭</td></tr></table>

#### 6.3.46 ATO 界面显示

ATO 界面显示功能的测试和验证方法详见表 96。

---

<div style="text-align: center;">表 96 ATO 界面显示</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO界面显示</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-44-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC车载ATO显示数据。在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续式列车运行过程中，车载人机界面上的显示对应内容（依据授权管理部门规定）</td></tr></table>

#### 6.3.47 ATO 自诊断、故障报警及数据记录

ATO 自诊断、故障报警及数据记录功能的测试和验证方法详见表 97。

<div style="text-align: center;">表 97 ATO 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO自诊断、故障报警及数据记录</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-45-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自诊断、故障报警及数据记录ATO子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心ATS</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>模拟ATO设备故障，在车载人机界面上显示相应的报警信息，或者车载维护终端上对应相应的数据信息。此外，通过车地通信将故障信息发送到ATS系统</td></tr></table>

#### 6.3.48 车载旅客信息数据

车载旅客信息数据功能的测试和验证方法详见表98。

<div style="text-align: center;">表 98 车载旅客信息数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载旅客信息数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-47-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载旅客信息数据。ATO车载设备应向TMS提供有关车载旅客信息的数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 连续式列车通过数据接口向列车TMS系统发送运营相关数据（若有）；2) 连续式列车通过数据接口接收列车TMS系统发送列车相关数据（若有）</td></tr></table>

---

#### 6.3.49 确定列车识别号

确定列车识别号功能的测试和验证方法详见表99和表100。

<div style="text-align: center;">表 99 确定列车识别号(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CBTC的运行列车识别号</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-48-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC的运行列车识别号。每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车识别号。列车识别号应由列车号、车次号、车组号、目的地号组成</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续式列车在线运行，可以通过ATS系统人工或自动分配列车识别号，可以通过ATS终端修改列车号、车次号、车组号、目的地号</td></tr></table>

<div style="text-align: center;">表 100 确定列车识别号(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车识别号丢失处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-48-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车-地双向通信传输信息恢复</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续式列车在线运行，丢失识别号后，系统根据运行图、列车位置及时间自动推算并自动设置列车识别号</td></tr></table>

#### 6.3.50 ATS 列车追踪

ATS 列车追踪功能的测试和验证方法详见表 101 和表 102。

<div style="text-align: center;">表 101 ATS 列车追踪(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS列车追踪</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-49-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS列车追踪ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他相关的信息并保持这些信息的能力。 列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续式列车在线运行（包括跨线运行），在ATS中心或车站操作终端观察列车运行信息，包括位置、标识等</td></tr></table>

---

<div style="text-align: center;">表 102 ATS 列车追踪(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS列车追踪</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-49-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS列车追踪 ATS系统应该具有自动追踪,获取所有运行在CBTC区域的装备 CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表,及其他的相关信息并保持这些信息的能力。 列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续式列车进出段运行,在ATS中心或车站操作终端观察列车运行信息,包括车组号的跟踪、显示</td></tr></table>

#### 6.3.51 列车进路办理

列车进路办理功能的测试和验证方法详见表103～表105。

<div style="text-align: center;">表 103 列车进路办理（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——自动</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-50-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——自动，ATS系统应该具有列车自动办理进路的功能，ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS车站或中心操作终端设置并确认进路具备自动进路功能（包括跨线进路），连续式列车接近后自动触发前方进路</td></tr></table>

<div style="text-align: center;">表 104 列车进路办理（二）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——人工</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-50-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——人工。ATS系统应该具有手动办理进路的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS车站或中心操作终端人工办理进路（包括跨线进路）</td></tr></table>

---

<div style="text-align: center;">表 105 列车进路办理（三）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——冲突检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-50-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——冲突检查。当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS系统编制一个具有交路冲突的运行计划，并加载该运行计划对冲突检查功能进行检查</td></tr></table>

#### 6.3.52 列车自动调整

列车自动调整功能的测试和验证方法详见表 106～表 108。

表 106 列车自动调整


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车自动调整 — 自动调度</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-51-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自动调度。ATS系统可包括自动调度功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续等级列车在自动驾驶模式下，ATS系统通过设置列车运行图，对在线列车以及存车线、场段列车进行自动调度</td></tr></table>

<div style="text-align: center;">表 107 列车自动调整(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车自动调整——列车自动间隔调整</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-51-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车时刻表/发车(运行)间隔调整。ATS系统可具有监视与自动调整的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过操作终端修改列车运行间隔；2) 连续等级列车接收并执行列车间隔调整命令；3) ATS系统沟通过监视终端观察间隔调整结果</td></tr></table>

---

<div style="text-align: center;">表 108 列车自动调整(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车自动调整——冲突自动调整</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-51-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>冲突自动调整。在CBTC列车位置报告的基础上，ATS系统应包括基于列车位置报告的列车自动调整功能，来处理列车冲突，以把整个系统的延迟减少到最小</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 连续等级列车通过车地通信将列车实时位置信息发送给ATS 系统； 2) ATS系统参考列车位置信息排列列车进路，减小列车进路冲突 带来的早晚点状况</td></tr></table>

#### 6.3.53 节能运行

节能运行功能的测试和验证方法详见表 109。

<div style="text-align: center;">表 109 节能运行</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>节能运行</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-52-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>节能运行、ATS系统可具有通过实时控制及协调列车加速、列车滑行、列车制动来实施能源优化的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过终端选择节能曲线；2) 连续等级列车可以通过车地通信接收并执行节能曲线</td></tr></table>

#### 6.3.54 扣车

扣车功能的测试和验证方法详见表110。

<div style="text-align: center;">表 110 扣车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>扣车</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-53-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>扣车、ATS系统应具有在车站扣车能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过终端选择设置扣车功能；2) 轨旁联锁或ZC系统通过授权或进路控制方式执行扣车功能；3) 连续等级列车可以通过车地通信接收并执行在站台扣车</td></tr></table>

---

#### 6.3.55 提前发车

提前发车功能的测试和验证方法详见表111。

<div style="text-align: center;">表 111 提前发车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>提前发车</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-54-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>提前发车：ATS系统应具有设置站台提前发车的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过终端选择设置提前发车功能；2) 连续等级列车可以通过车地通信接收并执行在站台提前发车</td></tr></table>

#### 6.3.56 跳停

跳停功能的测试和验证方法详见表112。

<div style="text-align: center;">表 112 跳停</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>跳停</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-55-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>跳停车站、ATS系统应具有设置一个或多个装备CBTC的列车经过下一个或下几个车站而不停车的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过终端选择设置跳停功能；2) 连续等级列车可以通过车地通信接收并执行在站台跳停</td></tr></table>

#### 6.3.57 设置/取消临时限速

设置/取消临时限速功能的测试和验证方法详见表113。

<div style="text-align: center;">表 113 设置/取消临时限速</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>设置/取消临时限速</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-56-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>临时限速。ATS系统应具有在CBTC区域内任何轨道区段，设置（与取消）临时限速的能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统通过终端选择设置/取消临时限速；2) ZC接收并处理ATS发送的临时限速命令；3) 连续等级列车可以通过车地通信接收并执行在ZC提供的临时限速信息</td></tr></table>

---

#### 6.3.58 时刻表编制管理

时刻表编制管理功能的测试和验证方法详见表114。

<div style="text-align: center;">表 114 时刻表编制管理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>时刻表编制管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-57-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>依据时刻表输入数据，在ATS时刻表编辑终端编制新的时刻表或对既有时刻表进行变更</td></tr></table>

#### 6.3.59 时钟校核功能

时钟校核功能的测试和验证方法详见表115。

<div style="text-align: center;">表 115 时钟校核功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>时钟校核功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-57-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>系统具备与 ATS 之间进行时钟校核功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>列车可以实现与不同厂家 ATS 之间的时钟校核，实现系统时间的一致性</td></tr></table>

#### 6.3.60 模拟培训

模拟培训功能的测试和验证方法详见表116。

<div style="text-align: center;">表 116 模拟培训</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模拟培训</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-58-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS 应具备模拟演示及培训系统，实现对调度员的培训</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在 ATS 模拟系统上执行演示和培训内容</td></tr></table>

#### 6.3.61 ATS 界面功能

ATS 界面功能的测试和验证方法详见表 117 和表 118。

---

<div style="text-align: center;">表 117 ATS 界面功能(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS显示数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-59-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS显示数据。CBTC的ATS显示应能够表示以下信息：1)精确的和区域相关的信息；2)列车状态相关信息；3)列车移动授权/进路信息；4)和被控列车运行相关的信息如防护区段信息，锁闭的进路/区段，以及临时限速极限和限速值；5)其他</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>连续等级列车在线运行，在ATS中心或车站操作终端显示列车运行位置、状态及相关的进路信息</td></tr><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CBTC输入数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-59-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC输入数据：CBTC的ATS用户界面显示应能够接收以下ATS用户输入：1)办理和取消进路输入；2)建立和取消防护区段，锁闭进路/区段，以及临时限速输入；3)其他</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)连续式列车在线运行，在ATS中心或车站操作终端进行进路的办理和取消（包括跨线进路）；2)连续式列车在线运行，在ATS中心或车站操作终端进行建立和取消防护区段，锁闭进路/区段，以及临时限速输入（包括跨线进路）</td></tr></table>

#### 6.3.62 ATS 数据记录

ATS 数据记录功能的测试和验证方法详见表 119 和表 120。

---

<div style="text-align: center;">表 119 ATS 数据记录(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>发送报警数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-60-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>发送报警数据。ATS 子系统可将自身的报警信息、ATP 车载子系统、ATO 子系统、CI 子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在中心维护工作站、车站维护工作站以及维护中心的信号监测报警工作站上查询连续式列车相关运行信息，包括 ATS 子系统、车载子系统、ZC 子系统以及 CI 子系统等报警信息</td></tr></table>

<div style="text-align: center;">表 120 ATS 数据记录(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据记录及回放</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-60-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>数据记录及回放。系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能。综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30 d</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS车站或中心操作终端或信号监测报警工作站进行30 d前的数据的查询操作，包括操作信息以及设备运行状态等</td></tr></table>

#### 6.3.63 中控/站控转换

中控/站控转换功能的测试和验证方法详见表 121。

<div style="text-align: center;">表 121 中控/站控转换</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站控/遥控</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-61-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在 ATS 车站操作终端或中心操作终端可以通过申请和确认操作，进行站控和中心控的切换功能；2) 在车站操作终端支持强制获取控制权功能；3) 本地或中央自动控制模式时，进行人工进路的相关操作，系统支持人工控制优于自动控制</td></tr></table>

---

#### 6.3.64 进路办理

进路办理功能的测试和验证方法详见表122。

<div style="text-align: center;">表 122 进路办理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>进路办理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-62-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>进路办理。联锁应具备进路办理功能。包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)联锁系统支持人工排列并建立进路（包括跨线进路）功能；2)联锁系统支持为连续式列车设置进路为自动进路模式功能</td></tr></table>

#### 6.3.65 保护区段控制

保护区段控制功能的测试和验证方法详见表 123 和表 124。

<div style="text-align: center;">表 123 保护区段控制(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>保护区段建立</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-63-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>保护区段：联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>联锁系统支持终端办理进路（包括跨线进路），将触发保护区段并锁闭功能；且连续式列车通过进路，进路逐段自动解锁</td></tr></table>

<div style="text-align: center;">表 124 保护区段控制(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>保护区段解锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-63-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>系统支持 CTC 列车进路保护区段解锁功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>CTC 列车在具备保护区段的进路停车后，进路外方的保护区段满足解锁条件后解锁</td></tr></table>

---

#### 6.3.66 停车保证功能

停车保证功能的测试和验证方法详见表 125。

<div style="text-align: center;">表 125 停车保证功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>停车保证功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-77-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>系统支持CTC列车停车保证功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>CBTC列车运行在正线上，在联锁上操作取消列车前方接近锁闭进路，此时列车向ZC汇报能否在当前进路终点前停稳，ZC收到后向联锁汇报能否停车保证</td></tr></table>

#### 6.3.67 进路/区段锁闭

进路/区段锁闭功能的测试和验证方法详见表126。

<div style="text-align: center;">表 126 进路/区段锁闭</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-64-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机、或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>联锁系统支持在CBTC区域内选取一条含有道岔的的进路（包括跨线进路），并排并建立进路，且取消已建立的进路，进路关闭并解锁；此外，一连续式列车接近并完整通过开放的进路，进路将逐段顺序解锁</td></tr></table>

#### 6.3.68 道岔单操、单锁

道岔单操、单锁功能的测试和验证方法详见表127。

<div style="text-align: center;">表 127 道岔单操、单锁</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔单操、单锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-65-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>道岔单操、单锁。联锁具备道岔单独操纵及锁闭的能力</td></tr></table>

---

<div style="text-align: center;">表 127 道岔单操、单锁（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔单操、单锁</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>CI操作终端上执行道岔的单独锁闭、解锁以及总定、总反操作，操作可以正确执行</td></tr></table>

#### 6.3.69 车站/区间封锁

车站/区间封锁功能的测试和验证方法详见表128。

<div style="text-align: center;">表 128 车站/区间封锁</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车站/区间封锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-66-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>封锁。系统应具有车站封锁、区间封锁的能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)封锁进站信号或者站台股道区段后，不能建立进站的进路； 2)封锁出站信号或者出站离太区段后，不能建立进入区间的进路（包括路线区间）</td></tr></table>

#### 6.3.70 站台紧急关闭按钮

站台紧急关闭按钮功能的测试和验证方法详见表129。

<div style="text-align: center;">表 129 站台紧急关闭按钮</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台紧急关闭按钮</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-C1-67-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台紧急关闭按钮：联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在连续式控车模式下，排列并建立进站进路，激活对应站台的站台紧急关闭按钮，ZC将紧急关闭状态发送给列车，由车载控制列车无法进入站台</td></tr></table>

#### 6.3.71 CI 自检、故障报警及数据记录

CI 自检、故障报警及数据记录功能的测试和验证方法详见表 130 和表 131。

---

<div style="text-align: center;">表 130 CI 自检、故障报警及数据记录（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>故障监测</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-69-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障监测。CI子系统具有自检、自诊断和对信号机、转辙机等基 础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>设置设备报警条件（包括系统自身故障，信号机、转辙机等设备故 障），在联锁维护终端界面显示相应的设备故障提示</td></tr></table>

<div style="text-align: center;">表 131 CI 自检、故障报警及数据记录(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>监视和记录工作状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-69-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>监视和记录工作状态：CI子系统能监视和记录自身的工作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯丝状态监测及断丝报警，转辙机动作状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在联锁维护终端显示设备工作状态，包括系统自动工作状态以及轨旁设备工作状态；2)在联锁维护终端界面获取并检查日志记录信息</td></tr></table>

#### 6.3.72 计轴故障恢复

计轴故障恢复功能的测试和验证方法详见表132。

<div style="text-align: center;">表 132 计轴故障恢复</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>计轴故障恢复</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-71-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>计轴故障恢复。系统应具有计轴故障恢复的能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)计轴预复位操作和列车完整通过完成计轴的复位(若具备)；2)计轴直接复位操作完成计轴的立即复位(若具备)</td></tr></table>

---

#### 6.3.73 CI 权限设置

CI 权限设置功能的测试和验证方法详见表 133。

<div style="text-align: center;">表 133 CI 权限设置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI权限设置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-74-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>操作权限设置CI子系统能设置不同操作人员的权限，并有相应的安全操作手段</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>启动CI子系统，操作人员需要通过口令进行登录和初始化操作，且任何安全相关的操作需要输入口令执行</td></tr></table>

### 6.4 互联互通计算机联锁(CI)间接口测试需求

#### 6.4.1 CI 与 CI 接口概述

CI 与 CI 接口概述功能的测试和验证方法详见表 134。

<div style="text-align: center;">表 134 CI 与 CI 接口概述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口概述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与CI子系统的接口是基于RSSP-I协议，通过双冗余以太网通信</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.4.2 通信层次描述

通信层次描述功能的测试和验证方法详见表135。

<div style="text-align: center;">表 135 通信层次描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与相邻CI通信的层次划分详见T/CAMET 04011.5章节5.2.3图3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.4.3 物理层描述

物理层描述功能的测试和验证方法详见表136。

<div style="text-align: center;">表 136 物理层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。
两系统按照A网和B网相连，A网和B网相连接的方式，其连接方式详见T/CAMET 04011.5章节5.1.1图1</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试功能内容：
CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。
对应测试需求：
1）相邻CI间通过A网连接，B网中断，验证可以正常办理进路，操作道岔等；
2）相邻CI间通过A网中断，B网连接，验证可以正常办理进路，操作道岔等；
3）相邻CI间AB网同时连接，办理进路的同时（进路满足办理条件），断开任一网络，验证进路办理成功。
该功能内容中描述的其他内容的验证通过产品设计来覆盖</td></tr></table>

#### 6.4.4 数据链路层描述

数据链路层描述功能的测试和验证方法详见表137。

<div style="text-align: center;">表 137 数据链路层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据链路层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>MAC(Medium Access Control)子层基于IEEE 802.3标准。MAC头由14个字节组成，1个帧校验序列(4字节)将被加在Ethernet帧后面</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.4.5 网络层描述

网络层描述功能的测试和验证方法详见表138。

<div style="text-align: center;">表 138 网络层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>网络层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本接口使用 IPv4 协议作为网络层的协议</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.4.6 传输层描述

传输层描述功能的测试和验证方法详见表 139。

功能名称 传输层描述

测试需求编号 CBTC-IP-CI/CI-MSG-CTC-6

功能内容 本接口使用 UDP/IP 协议作为传输协议

测试需求 见各厂商设计文件

#### 6.4.7 安全通信协议层描述

安全通信协议层描述功能的测试和验证方法详见表 140。

<div style="text-align: center;">表 140 安全通信协议层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>采用RSSP-I标准协议，同时通过序列号对冗余网络数据进行过滤，不作为本文档描述</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.4.8 应用层描述

应用层描述功能的测试和验证方法详见表141。

---

<div style="text-align: center;">表 141 应用层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应用层遵守 T/CAMET 04011.5 规定的协议，详见 CI-CI 间接口描述</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.4.9 动态交互描述

动态交互描述功能的测试和验证方法详见表142。

<div style="text-align: center;">表 142 动态交互描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>动态交互描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI以300ms(周期根据各厂商配置)为周期向相邻的CI发送信息CI认为与邻站CI通信中断的超时时间定义为TCiTimeout(可配置,推荐值5s)1)CI没有接收到来自邻站CI的任何消息达到或超过TCiTimeout超时时间定义的时间窗口,则CI应认为与邻站CI通信中断;2)CI没有接收到来自邻站CI的任何消息达到或超过TCiTimeout超时时间定义的时间窗口,则CI应认为与邻站CI通信中断(指应用层根据CAL包头中字段进行判断,而非安全通信协议层进行的判断);3)若CI判断接收到邻站CI的应用信息延迟已经达到TCiTimeout时,CI应认为与邻站CI通信中断(指应用层根据CAL包头中字段进行判断,而非安全通信协议层进行的判断);4)CI与邻站CI间通信中断的情况下,本站CI无法收到邻站汇报的设备信息。CI应将邻站所有设备状态设置为安全侧,如将通往邻站进路的始端信号机置为禁止信号,对应来自邻站的区段设置为占用;5)CI与邻站CI间通信中断的情况下,若本站CI收到了合法的邻站CI信息,则本站CI应认为与邻站CI连接恢复;6)互联互通线网中,CI与邻站CI的通信超时时间应一致,消息有效期时间应一致;7)CI与邻站CI间通信中断的情况下,若本站CI收到了合法的邻站CI信息,则本站CI应认为与邻站CI连接恢复</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>断开相邻CI间通信,验证当断开时间超过系统定义的延时通信周期后,相邻CI认为通信中断</td></tr></table>

---

#### 6.4.10 通信故障处理

通信故障处理功能的测试和验证方法详见表143。

<div style="text-align: center;">表 143 通信故障处理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>通信中断后，本站CI无法收到邻站汇报的设备信息。CI将邻站所有设备状态设置为安全侧，如将通往邻站进路的始端信号机置为禁止信号，对应来自邻站的区段设置为占用</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)双通道全部断开后，接收端CI子系统认为通信中断，并有相应的报警提示；2)设备状态置为安全侧</td></tr></table>

#### 6.4.11 CI 间通信通用报文

CI间通信通用报文功能的测试和验证方法详见表144。

<div style="text-align: center;">表 144 CI 间通信通用报文</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI间通信通用报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL消息包中包含CI间传输的各条应用信息，每个GAL消息包总长不得超过1 000字节，格式定义详见T/CAMET 04011.5章节5.3.1.2表1。
CI与邻站CI传输分界线两边的设备信息，包括进路内物理区段、信号机、站台门、紧急关闭按钮、道岔及保护区段状态。双方CI向对方传输互联互通相关范围内的本联锁管辖范围的设备状态，接收对方CI发送的设备状态。
接口数据采用big-endian编码顺序</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.4.12 CI 与 CI 接口描述

CI 与 CI 接口描述功能的测试和验证方法详见表 145 ~ 表 158。

<div style="text-align: center;">表 145 CI 与 CI 接口描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-I2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应用层信息格式定义详见T/CAMET 04011.5章节5.3.1.2表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 146 CI 与 CI 接口描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>报文类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本节对CI间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.5章节5.3.2表3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 147 CI 与 CI 接口描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联锁管辖范围的道岔状态发送给邻站CI。相邻CI间进路索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.1表4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>依据接口数据中所包含的道岔，分别对道岔做引导总锁、单锁、封锁、单操定位、单操反位、道岔四开的操作，验证临站联锁显示同本站联锁一致；并验证未对道岔做任何设置时，临站联锁显示同本站联锁显示一致。通过对跨线进路中的相关道岔设置相应的状态，并验证不同的状态对跨线进路及跨线列车运行的影响</td></tr></table>

---

<div style="text-align: center;">表 148 CI 与 CI 接口描述(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理区段状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联锁管辖范围的物理区段状态发送给邻站CI。相邻CI间物理区段索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.2表5</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>通过相关操作使物理区段（如计轴区段）状态为占用、封锁、区段锁闭、防护锁闭、某一锁闭方向，验证临站联锁显示同本站联锁显示一致；并验证使物理区段（如计轴区段）处于空闲且未封锁且未锁闭状态时，临站联锁显示同本站联锁显示一致。通过对跨线进路中的相关物理区段设置相应的状态，并验证不同的状态对跨线进路的影响</td></tr></table>

表 149 CI 与 CI 接口描述


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>逻辑区段状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CZCI-MSG-CTC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联锁管辖范围的逻辑区段状态发送给邻站CI。相邻CI间逻辑区段索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.3表6</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>操作逻辑区段使其状态为CT车占用、UT车占用、设置/取消临时限速，区段封锁、区段进路锁闭、区段保护锁闭、某一锁闭方向等，验证临站联锁显示同本站联锁一致；并验证使逻辑区段处于空闲且未封锁和未锁闭状态时，临站联锁显示与本站联锁显示一致。通过对跨线进路中的相关逻辑区段设置相应的状态，并验证不同的状态对跨线进路的影响</td></tr></table>

---

<div style="text-align: center;">表 150 CI 与 CI 接口描述(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信号机状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联领管辖范围的信号机状态发送给邻站CI。联锁分界点处信号机属于接车方联锁管辖，若联锁分界点有外置保护区段，则发车方联锁也应向接车方联锁发送该信号机状态信息。若联锁分界点无外置保护区段，则发车方联锁不发该信号机状态信息。相邻CI间信号机索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.4表7</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>操作信号机使其状态分别为红灯、黄灯、绿灯、红黄灯、灯丝断丝、封锁、未封锁，验证临站联锁显示同本站联锁一致。通过对跨线进路中的相关信号机设置相应的状态，并验证不同的状态对跨线进路的影响</td></tr></table>

<div style="text-align: center;">表 151 CI 与 CI 接口描述(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将互联互通相关范围内的本联锁管辖范围的站台门状态信息发送给邻站CI，相邻CI间站台门索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.5表8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>操作站台门使其处于开门、关门、旁路、未旁路的状态，验证临站联锁显示同本站联锁一致；通过对跨线相关区域中的站台门设置相应的状态，并验证不同的状态对跨线列车运行的影响</td></tr></table>

<div style="text-align: center;">表 152 CI 与 CI 接口描述(八)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>照查状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将互联互通相关范围内的本联锁管辖范围的照查状态信息发送给邻站CI。相邻CI间照查索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.7表10</td></tr></table>

---

<div style="text-align: center;">表 152 CI 与 CI 接口描述（八）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>照查状态信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)操作使照查条件处于照查条件满足或照查条件不满足的状态，验证临站联锁显示与本站联锁一致；2)通过对跨线进路相关的照查条件设置相应的状态，并验证不同的状态对跨线进路及跨线列车运行的影响</td></tr></table>

<div style="text-align: center;">表 153 CI 与 CI 接口描述（九）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>防淹门状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-20</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将互联互通相关范围内的本联锁管辖范围的防淹门信息发送给邻站CI。相邻CI间防淹门索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.8表11</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)操作站台门使其处于开门、关门、开门允许/不允许、关门请求/未请求状态，验证临站联锁显示同本站联锁一致；2)通过对跨线相关区域中的防淹门设置相应的状态，并验证不同的状态对跨线列车运行的影响</td></tr></table>

<div style="text-align: center;">表 154 CI 与 CI 接口描述(十)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>上电锁闭状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-21</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将本站信息发送给邻站CI，详见T/CAMET 04011.5章节5.4.9表12</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>操作使联锁处于上电锁闭、上电解锁状态，验证临站联锁显示与本站联锁一致</td></tr></table>

<div style="text-align: center;">表 155 CI 与 CI 接口描述(十一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>临时限速信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-22</td></tr></table>

---

<div style="text-align: center;">表 155 CI 与 CI 接口描述(十一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>临时限速信息</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联锁管辖范围的临时限速区段状态发送给邻站CI。相邻CI间临时限速区段索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.10表13</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在跨线区域中设置对不同的区段设置临时限速，验证临站联锁显示同本站联锁一致；2) 通过对跨线相关区域中的区段设置相应的状态，并验证不同的状态对跨线列车运行的影响</td></tr></table>

<div style="text-align: center;">表 156 CI 与 CI 接口描述(十二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台紧急关闭按钮信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-23</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI应将互联互通相关范围内的本联锁管辖范围的站台紧急关闭信息发送给邻站CI。相邻CI间临时限速区段索引顺序应保持一致。详见T/CAMET 04011.5章节5.4.6表9</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在跨线区域中设置对不同的区段临时限速，验证临站联锁显示同本站联锁一致；2) 通过对跨线相关区域中的区段设置相应的状态，并验证不同的状态对跨线列车运行的影响</td></tr></table>

<div style="text-align: center;">表 157 CI 与 CI 接口描述(十三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>城市自定义包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-24</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将互联互通相关范围内的本联锁管辖范围的城市自定义信息发送给邻站CI,详见T/CAMET 04011.5章节5.4.11表14</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在工程中约定</td></tr></table>

---

<div style="text-align: center;">表 158 CI 与 CI 接口描述(十四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>厂商自定义包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-CTC-25</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本CI将互联互通相关范围内的本联锁管辖范围的厂商自定义信息发送给邻站CI，详见T/CAMET 04011.5章节5.4.12表15</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在工程中约定</td></tr></table>

### 6.5 互联互通区域控制器(ZC)间跨线接口测试需求

#### 6.5.1 通信模型描述

通信模型描述功能的测试和验证方法详见表 159。

<div style="text-align: center;">表 159C 通信模型描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信模型描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC_IF_ZC/ZC-MSG-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>安全功能模块和通信功能模块应由各厂家ZC子系统内部功能实现，分别用于实现安全功能和对外通信功能，ZC-ZC通信协议模型详见T/GAMET04011.4章节5.2.1图1</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂面设计文件</td></tr></table>

#### 6.5.2 通信机制

通信机制功能的测试和验证方法详见表160。

<div style="text-align: center;">表 160 通信机制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1) 邻站 ZC 间通信采用周期发送的方式进行通信；2) 通信双方均采用大端字节序进行数据传输</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.5.3 通信层次结构描述

通信层次结构描述功能的测试和验证方法详见表161。

---

<div style="text-align: center;">表 161 通信层次结构描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次结构描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC间通信层次结构划分详见T/CAMET 04011.4章节5.2.3图2。1)物理层:采用1EEE802.3标准协议。2)网络层:IPv4。3)传输层:UDP协议。4)安全通信协议层:采用RSSP-1铁路信号安全通信协议。5)应用层:参见T/CAMET 04011.4章节5.3.1详细定义</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.5.4 物理接口

物理接口功能的测试和验证方法详见表162～表165。

<div style="text-align: center;">表 162 物理接口(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>跨线ZC之间通过RJ45接口冗余接入信号安全数据网，ZC间通信的网络拓扑结构采用A网-A网，B网-B网两个链路</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 163 物理接口(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信应用层消息包定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>按照《RSSP-I 铁路信号安全通信协议》，将相邻 ZC 间每个周期需要交互的信息通过组成通用（GAL）消息包进行传输，详见 T/CAMET 04011.4 章节 5.3.1.1 图 3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 164 物理接口(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL包中包含ZC间传输的各条应用信息。格式定义详见T/CAMET 04011.4章节5.3.1.2表1和表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 165 物理接口(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态的监存和管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1. ZC 应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站 ZC 的应用信息，并记录报警信息。具体检查方式如下：1) 消息内容的一致性检查：包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性。若消息中存在字段的“非法”取值，应对本 GAL 包信息中所有进行丢弃处理；2) 通用应用（GAL）信息包消息所应包含的信息的完整性；3) 其他逻辑检查。2. ZC 应能对通信连接状态进行判断：1) ZC 认为与邻站 ZC 通信中断的超时时间定义为 TZcTimeout（1.5 s ~ 6 s，可配置）。2) 若 ZC 在 TZcTimeout 超时时间内，没有接收到来自邻站 ZC 的任何消息，则 ZC 应认为与邻站 ZC 通信中断。3) 若 ZC 判断接收到邻站 ZC 的 GAL 包延迟已经达到 TZcTimeout 时，ZC 应丢弃此 GAL 包，或认为与邻站 ZC 通信中断。4) 通信中断的情况下，应生成报警信息，并进行安全侧处理。5) ZC 与邻站 ZC 间通信中断的情况下，若本站 ZC 收到了合法的邻站 ZC 信息，则本站 ZC 应认为与邻站 ZC 连接恢复。6) 互联互通线网中，各厂商 ZC 间的通信超时时间应一致，消息有效期时间应一致</td></tr></table>

---

<div style="text-align: center;">表 165 物理接口(四)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态的监督和管理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)应用信息的合法性检查参见各厂商设计文件.2)通信连接状态:断开相邻ZC与ZC间通信,并超过系统定义的TZcTimeout,ZC系统判断为与相邻ZC通信超时</td></tr></table>

#### 6.5.5 数据类型定义

数据类型定义功能的测试和验证方法详见表166。

<div style="text-align: center;">表 166 数据类型定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本节对ZC之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.4章节5.3.2表3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.5.6 应用信息定义——道岔状态信息

应用信息定义——道岔状态信息功能的测试和验证方法详见表167。

<div style="text-align: center;">表 167 应用信息定义——道岔状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本ZC应将配置重叠区内所有道岔状态发送给邻站ZC相邻ZC间道岔索引顺序应保持一致 详见T/CAMET 04011.4章节5.4.2表4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)排列、取消跨ZC分界点的进路(遍历道岔的所有状态)；2)验证通信数据与接口协议定义一致性</td></tr></table>

#### 6.5.7 应用信息定义——物理区段状态信息

物理区段状态信息功能的测试和验证方法详见表168。

---

<div style="text-align: center;">表 168 应用信息定义——物理区段状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理区段状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本ZC将配置重叠区内本管辖区物理区段信息发送给邻站ZC。相邻ZC需对物理区段进行排序，并且同一物理区段在发送方的排序位置与接收方的排序位置相同。详见T/CAMET 04011.4章节5.4.3表5</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)验证ZC重叠区内物理区段空闲和占用时，相邻ZC交互的“物理区段占用状态”信息正确；2)验证物理区段未锁闭、被引导进路锁闭、被进路锁闭时，相邻ZC交互的“物理区段锁闭状态”和“物理区段锁闭方向”信息正确</td></tr></table>

#### 6.5.8 应用信息定义——移交状态信息

移交状态信息功能的测试和验证方法详见表169。

<div style="text-align: center;">表 169</div>


应用信息定义——移交状态信息（一）


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移交状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移交状态信息包用于ZC切换的管理，信息包含移交与接管ZC交互的各自边界点移交状态信息 详见T/CAMET 04011.4章节5.4.4表6</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)对于移交ZC，当移交列车最大安全前端在移交ZC的管辖区，MA到达边界点时开始针对该边界点发送列车移交状态，并在移交列车最小安全后端离开移交ZC后停止发送该列车的移交状态；2)对于接管ZC，当正在移交的列车最大安全前端或者最小安全后端在相邻ZC重叠区，接管ZC针对该边界点发送移交状态；3)非CTC车和CTC车，移动授权到达边界，验证边界点ID、接近列车ID、接近距离、接近列车运行等级、接近列车车载ATP当前模式、移交列车VID正确，移交ZC向接管ZC发送的列车移交接管状态字段为0x11，接管ZC向移交ZC发送的列车移交接管状态字段为0xFF；</td></tr></table>

---

<div style="text-align: center;">表 169 应用信息定义——移交状态信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移交状态信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>4) 非 CTC 车和 CTC 车, 移动授权越过边界, 验证边界点 ID、接近列车 ID、接近距离、接近列车运行等级、接近列车车载 ATP 当前模式、移交列车 VID 正确, 移交 ZC 向接管 ZC 发送的列车移交接管状态字段为 0x11, 接管 ZC 向移交 ZC 发送的列车移交接管状态字段为 0x22; 移动授权状态为 11b. 移动授权已进入接管管辖区, MA 是否有效字段为本车有在本 ZC 管辖范围内的 MA 为 0x55, 且“列车在本 ZC 管辖范围内的 MA 信息”正确; 5) 无车移交时, 则“接近列车 ID”“接近列车运行等级”“接近列车车载 ATP 当前模式”“接近列车距离”字段均填写默认值; 6) 对于主进路在移交 ZC 管辖区内, 保护区段在接管 ZC 管辖区内, 移交 ZC 判断 MA 到达移交边界时, 向接管 ZC 发送的“移交状态信息”包中的 MA 信息中, 障碍点为默认值, 安全防护点为移交边界点, 保护区段有效性为“无效”; 接管 ZC 向移交 ZC 发送的“移交状态信息”包中的 MA 信息中, 障碍点、起点位置均为移交边界点, 安全防护点为保护区段末端回退安全余量, 保护区段有效性为“有效”</td></tr></table>

#### 6.5.9 应用信息定义——移交列车信息

移交列车信息功能的测试和验证方法详见表 170。

<div style="text-align: center;">表 170 应用信息定义——移交列车信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移交列车信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移交列车信息包用于列车相关的功能，ZC 将所有最大安全前端或最小安全后端位于重叠区本管辖区范围的列车（含非 CBTC 列车）的信息发送给相邻 ZC，详见 T/CAMET 04011.4 章节 5.4.5 表 7</td></tr></table>

---

<div style="text-align: center;">表 170 应用信息定义——移交列车信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移交列车信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)非 CTC 车和 CTC 列车通过跨线移交重叠区，并对以下时机数据进行验证：列车最大前端进入移交重叠区开始发送移交列车信息，列车最小安全后端通过重叠区后，不再发送移交列车信息；2)遍历“信息单元状态”字段中每个字段的不同值</td></tr></table>

#### 6.5.10 应用信息定义——城市自定义包信息

城市自定义包信息功能的测试和验证方法详见表171。

<div style="text-align: center;">表 171 应用信息定义——城市自定义包信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>城市自定义包信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在工程中约定</td></tr></table>

#### 6.5.11 应用信息定义——厂商自定义包信息

厂商自定义包信息功能的测试和验证方法详见表172。

<div style="text-align: center;">表 172 应用信息定义——厂商自定义包信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>厂商自定义包信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，ZC收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在工程中约定</td></tr></table>

#### 6.5.12 应用信息定义——站场信息延时包

站场信息延时包信息功能的测试和验证方法详见表173。

---

<div style="text-align: center;">表 173 应用信息定义——站场信息延时包(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站场信息延时包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>用于表明GAL包内站场信息的最大已存在时间。站场信息的最大已存在时间指来自CI的站场信息在发送方ZC发出该信息前已存在的时间。涉及站场信息包括：道岔状态信息包、物理区段状态信息包、移交状态信息包中的距边界点最近的列车信息、轨道区段列车排序信息包。ZC判断相邻ZC发送的GAL包中站场信息的可用性时，应考虑站场信息已存在时间。详见T/CAMET 04011.4章节5.4.8表10</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)站场信息延时包中的数据已超过站场信息的可用时间，验证移交ZC不会使用该信息；2)站场信息延时包中的数据未超过站场信息的可用时间，验证移交ZC使用该信息</td></tr></table>

#### 6.5.13 应用信息定义——轨道区段列车排序信息

轨道区段列车排序信息功能的测试和验证方法详见表174。

<div style="text-align: center;">表 174 应用信息定义——轨道区段列车排序信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>轨道区段列车排序信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ZC/ZC-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本ZC应将配置重叠区内本ZC管辖范围内所有轨道区段上的列车顺序信息发送给邻站ZC相邻ZC间轨道区段索引顺序应保持一致。详见T/CAMET04011.4章节5.4.9表11. 轨道区段内列车排序原则为：1)通信列车排序按照V0BC发送的原始位置报告进行；2)若发送方ZC发送的轨道区段上无列车序列，且在“物理区段状态信息”包中，该轨道区段所在物理区段的“物理区段占用状态”取值为“占用”，则发送方ZC应保证该轨道区段上无非通信车；3)轨道区段上的列车应按照从边界点向远离边界点的方向排序；4)轨道区段内相邻的非通信车可合并为一列非通信车</td></tr></table>

---

<div style="text-align: center;">表 174 应用信息定义——轨道区段列车排序信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>轨道区段列车排序信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ZC 重叠区内全为完成头尾筛选的连续级列车，验证移交 ZC 向接管 ZC 发送的轨道区段内列车排序信息正确；2) ZC 重叠区内一轨道区段上两连续级列车降级为非连续级列车，验证移交 ZC 向接管 ZC 发送的轨道区段内列车排序信息中该轨道区段内的两列车变为一列车；3) ZC 重叠区内一轨道区段上存在两连续级列车，后车降级为非连续级列车，前车丢失尾端筛选，验证移交 ZC 向接管 ZC 发送的轨道区段内列车排序信息中该轨道区段内的两列车变为一列车。</td></tr></table>

### 6.6 互联互通跨线 ATS 间接口测试需求

#### 6.6.1 ATS 与 ATS 通信机制

ATS 和 ATS 通信机制功能的测试和验证方法详见表 175。

<div style="text-align: center;">表 175 ATS 与 ATS 通信机制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>市轨道通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)相邻ATS间通信采用周期与非周期发送的方式进行通信。2)通信双方均采用大端字节序进行数据传输</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr><tr><td colspan="2">注:表中功能内容是ATS接口规范的原文描述(下同)。</td></tr></table>

#### 6.6.2 ATS 与 ATS 接口概述

ATS 与 ATS 接口概述功能的测试和验证方法详见表 176。

---

<div style="text-align: center;">表 176 ATS 与 ATS 接口概述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次结构描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS间通信层次结构划分详见T/CAMET 04011.6章节5.2.1图1。物理层：采用IEEE802.3标准协议；数据链路层：采用IEEE802.3标准协议；网络层：IPv4；传输层：TCP协议；应用层：参见T/CAMET 04011.6章节5.2.3详细定义</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.3 物理接口描述

物理接口描述功能的测试和验证方法详见表177。

<div style="text-align: center;">表 177 物理接口描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS冗余接入通信网络，网络拓扑结构为A网-A网，B网-B网，接口间宜通过防火墙进行隔离</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.4 通信层次描述

通信层次描述功能的测试和验证方法详见表178。

<div style="text-align: center;">表 178 通信层次描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-4</td></tr></table>

---

<div style="text-align: center;">表 178 通信层次描述(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次描述</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与ATS间建立对等的逻辑连接，如图7所示（箭头指向表示服务端，双线表示双网逻辑连接）：第一组通道，线路一ATS的主机作为客户端同时与线路二ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。第二组通道，线路二ATS的主机作为客户端同时与线路一ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。服务端侦听端口为9900</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.5 信息帧格式定义

信息帧格式定义功能的测试和验证方法详见表179。

<div style="text-align: center;">表 179 信息帧格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息帧格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>相邻ATS间每个周期需要交互的信息通过组成通用的(GAL)消息包(以下简称GAL包),进行传输,详见T/CAMET 04011.6章节5.2.2.3图3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.6 动态交互描述

动态交互描述功能的测试和验证方法详见表180～表182。

<div style="text-align: center;">表 180 动态交互描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-6</td></tr></table>

---

<div style="text-align: center;">表 180 动态交互描述(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS间通信的GAL包中包含ATS间传输的各条应用信息，每个GAL消息包总长不得超过65 000字节，每个GAL只包含一类应用数据。详见T/CAMET 04011.6章节5.2.2.3.2表1和表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 181 动态交互描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——合法性检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站ATS的应用信息，并记录报警信息。具体检查方式如下：1)消息内容的一致性检查包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性检查；2)通用应用(GAL)信息包消息所应包含的信息的完整性；3)其他逻辑检查</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 182 动态交互描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS和V0BC应能分别对通信连接状态进行判断：1) ATS认为与邻站ATS通信中断的超时时间定义为TATTimeout(3 s~9 s,可配置)；2) 若ATS在TATTimeout超时时间内,没有接收到来自邻站ATS的任何消息,则ATS应认为与邻站ATS通信中断；3) 若ATS判断接收到邻站ATS的周期性应用信息延迟已经达到TATTimeout时,ATS可丢弃此信息包,ATS应认为与邻站ATS通信中断或发生丢包；4) 通信中断的情况下,应生成报警信息；</td></tr></table>

---

<div style="text-align: center;">表 182 动态交互描述(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>5) 连接断开时立即重连；6) 互联互通线网中，各厂商的 ATS 间的通信超时时间应一致，消息有效期时间应一致；7) 通信中断的倒机切换逻辑：ATS 和相邻 ATS 的备机只有在完成了与各自系统主机的同步，真正进入备机状态以后才应与对方进行通信联系；8) ATS 和相邻 ATS 在通信中断后应首先尝试重新建立连接，只有在重建连接仍不成功后，才应进行倒机切换逻辑判断；9) ATS 备机之间相邻 ATS 主备机之间应通过其他的物理连接相互沟通各自系统主备机之间的通信连接状态，为倒机切换提供准确、可靠的判断依据；10) ATS 和相邻 ATS 只有在主机之间的通信连接发生故障以后才应进行倒机切换。备机与备机之间、主机与备机之间的通信中断后只报警而不倒机；11) ATS 和相邻 ATS 主机通讯中断且持续一段时间（该时间应可配置，范围 2 s~4 s）内不能恢复，且在判断 ATS 备机与相邻 ATS 主机通信正常的情况下，ATS 分机才应进行倒机切换</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 断开相邻 ATS 与 ATS 间通信，并超过系统定义的 TATTimeout，ATS 系统判断为与相邻 ATS 通信超时；2) 断开 ATS 和相邻 ATS 主机之间的通信连接持续一段时间未恢复，进行倒机切换；3) 断开 ATS 与相邻 ATS 备机与备机之间的通信连接，只报警而不倒机；4) 断开 ATS 与相邻 ATS 主机与备机之间的通信连接，只报警而不倒机</td></tr></table>

#### 6.6.7 接口数据描述

接口数据描述功能的测试和验证方法详见表 183 和表 184。

---

<div style="text-align: center;">表 183 接口数据描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.6章节5.2.3.1表3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 184 接口数据描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据交互方式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS之间数据交互方式详见T/CAMET 04011.6章节 5.2.3.2图4,表明了两个线路ATS间互传的数据流(箭头方向表示数据流向),具体定义如下: 1)本线路的列车运行调整信息; 2)本线路的站场显示信息、列车信息、接入站跳停命令及回执; 3)心跳信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.8 应用信息定义

应用信息定义功能的测试和验证方法详见表 185。

<div style="text-align: center;">表 185 应用信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本章节中的“无效”值：正常通信时发送方不可能发送的非法取值。接收方收到GAL包中的应用信息包中存在“无效”值时，应对GAL包应用信息包中无效字段进行错误处理。本章节中的“默认”值：</td></tr></table>

---

<div style="text-align: center;">表 185 应用信息定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1）针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；2）设备在初始化完成前，无法确定状态时，相关字段取值发送“默认”值。接收方收到“默认”值后，应认为信息有效，不进行处理。本章节中涉及“上行”“下行”的方向定义，均采用运营方向规定的上下行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.9 心跳信息包

心跳信息包功能的测试和验证方法详见表 186.

<div style="text-align: center;">表 186 心跳信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>心跳报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS 应周期性发送心跳信息，具体格式同应用信息包为 0 的 GAL 包</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送心跳报文</td></tr></table>

#### 6.6.10 站场显示信息包

站场显示信息包功能的测试和验证方法详见表187。

<div style="text-align: center;">表 187 站场显示信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站场显示信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应周期性将复视车站的所有站场表示信息发送给相邻线ATS。详见T/CAMET 04011.6章节5.2.3.3.3表4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS系统周期向相邻ATS发送跨线显示区域的站场信息</td></tr></table>

---

#### 6.6.11 列车信息包

列车信息包功能的测试和验证方法详见表188。

<div style="text-align: center;">表 188 列车信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应周期性将复视车站的所有列车状态信息发送给相邻线ATS，详见T/CAMET 04011.6章节5.2.3.3.4表5</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS系统周期向相邻ATS发送跨线显示区域的列车信息</td></tr></table>

#### 6.6.12 列车运行调整信息包

列车运行调整信息包功能的测试和验证方法详见表189。

<div style="text-align: center;">表 189 列车运行调整信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行调整信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对于跨线列车，线路 ATS 应应周期性互传各自线路内跨线运营分界处交出车站的计划运行图/时刻表、实迹运行图/时刻表和计划调整信息。详见 T/CAMET 04011.6 章节 5.2.3.3.5 表 6</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送跨线显示区域的列车运行调整相关信息</td></tr></table>

#### 6.6.13 列车接入站跳停命令信息包

列车接入站跳停命令信息包功能的测试和验证方法详见表190。

<div style="text-align: center;">表 190 列车接入站跳停命令信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停命令信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-16</td></tr></table>

---

<div style="text-align: center;">表 190 列车接入站跳停命令信息包(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停命令信息包</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对跨线列车，当在接入线接入站（人工或自动）设置跳停时，由接入线ATS发送站台跳停命令至交出线ATS，交出线ATS收到跳停命令后，发送接收回执给接入站ATS，由交出站ATS负责管理接入站台的跳停命令，确定将命令发送至列车的时机，回执超时时重发N次后报错，并停止发送（重发次数、超时时间可配置）。详见T/CAMET 04011.6章节5.2.3.3.6表7</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>接入线ATS系统周期向移交ATS发送跨线区域的列车跳停信息</td></tr></table>

#### 6.6.14 列车接入站跳停回执信息包

列车接入站跳停回执信息包功能的测试和验证方法详见表191。

<div style="text-align: center;">表 191 列车接入站跳停回执信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停回执信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对跨线列车，当接入线接入站站台设置跳停时，交出线ATS收到接入站发送的接入站站台跳停命令信息包后回复接收回执详见LT/CAMET 04011.6章节5.2.3.3.7表8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>移交线ATS系统向接入线ATS发送跨线区域的列车跳停信息包回执信息</td></tr></table>

#### 6.6.15 ATS 城市自定义帧

ATS 城市自定义帧功能的测试和验证方法详见表 192。

<div style="text-align: center;">表 192 ATS 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr></table>

---

<div style="text-align: center;">表 192 ATS 城市自定义帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统向相邻 ATS 发送城市自定义帧。2) 依据城市需求测试</td></tr></table>

#### 6.6.16 ATS厂商自定义帧

ATS厂商自定义帧功能的测试和验证方法详见表193。

<div style="text-align: center;">表 193 ATS 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能 各厂商分别定制，ATS收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统向相邻ATS发送厂商自定义帧. 2) 依据厂商功能定义测试</td></tr></table>

### 6.7 互联互通车地通信接口(VOBC 和 CI) 测试需求

#### 6.7.1 接口连接方式

接口连接方式描述功能的测试和验证方法详见表 194 和表 195。

<div style="text-align: center;">表 194 物理接口描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与CI之间采用冗余网络进行通信.CI与V0BC之间的网络拓扑结构采用A网-A网,B网-B网两个链路进行连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 195 安全通信协议</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-2</td></tr></table>

---

<div style="text-align: center;">表 195 安全通信协议(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与V0BC之间通信可采用RSSP-Ⅱ或RSSP-Ⅱ安全通信协议。RSSP-Ⅱ安全通信协议的具体要求参见《RSSP-Ⅱ铁路信号安全通信协议》（运基信号[2010]267号）；RSSP-Ⅰ安全通信协议的具体要求参见《RSSP-Ⅰ铁路信号安全通信协议》（运基信号[2010]267号）。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议架构详见T/CAMET04011.2章节7.1.2图10，其SAI/MASL/ALE三层，遵循RSSP-Ⅱ标准规定。1)TCP及IP层使用标准TCP/IP协议栈；2)MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE802.3）。RSSP-Ⅰ安全通信协议架构详见T/CAMET04011.2章节7.1.2图11，其RSSP-Ⅰ协议遵循RSSP-Ⅰ标准规定。1)UDP层使用标准UDP协议栈；2)MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE802.3）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.2 动态交互描述

动态交互描述功能的测试和验证方法详见表196～表198。

<div style="text-align: center;">表 196 动态交互描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-3</td></tr></table>

---

<div style="text-align: center;">表 196 动态交互描述(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI/V0BC 每周期最多允许发送 1 个消息包，包中包含 CI 与 V0BC 之间传输的应用信息，每个 GAL 消息包总长不得超过 1 000 字节，详见 T/CAMET 04011.2 章节 7.1.3.2 表 29 和表 30</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 197 动态交互描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——合法性检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI应对接收到的V0BC的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方的应用信息。具体检查方式如下：1)消息内容的一致性检查：包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性检查；2)消息所应包含的信息的完整性</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 198 动态交互描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI和V0BC应能分别对通信连接状态进行判断：
1) CI认为与V0BC通信中断的超时时间定义为TCiTimeout；
2) V0BC认为与CI通信中断的超时时间定义为TVobcTimeout；
3) 若CI在TCiTimeout超时时间内，没有接收到来自V0BC的任何消息，则CI应认为与V0BC的通信中断；
4) 若V0BC在TVobcTimeout超时时间内，没有接收到来自CI的任何消息，则V0BC应认为与CI的通信中断；</td></tr></table>

---

<div style="text-align: center;">表 198 动态交互描述(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>5) 若 CI 判断接收到 VOBC 的应用信息延迟已经达到 TCiTimeout 时，CI 应丢弃此信息包或认为与 VOBC 通信中断；6) 若 VOBC 判断接收到 CI 的应用信息延迟已经达到 TVobcTimeout 时，VOBC 应丢弃此信息包或认为与 CI 通信中断。    互联互通线网中，车载设备与各条线路上的联锁设备的通信超时时间应一致，消息有效期时间应一致。    VOBC 在与 CI 设备通信时，当判断与 CI 设备通信断开并且不再与对方建立连接后，应断开与 CI 设备的 TCP/IP 连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 断开相邻 VOBC 与 CI 间通信，并超过系统定义的 TCiTimeout，CI 系统判断为与 VOBC 通信超时；2) 断开相邻 VOBC 与 CI 间通信，并超过系统定义的 TVobcTimeout，VOBC 系统判断为与 CI 通信超时</td></tr></table>

#### 6.7.3 通信故障处理

通信故障处理功能的测试和验证方法详见表199。

表 199 通信故障处理


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>分 轨 道 通 信 故 障 处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。
车地无线通信双方（CI-V0BC）应用层的通信故障处理分为如下几种情况：
1) CI 和 V0BC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息；
2) 通信中断的情况下处理：若 CI/V0BC 认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理；
3) 其他风险由安全通信协议完成防护处理</td></tr></table>

---

<div style="text-align: center;">表 199 通信故障处理(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.4 通信体系结构

通信体系结构功能的测试和验证方法详见表200。

<div style="text-align: center;">表 200 通信体系结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次划分</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与CI通信协议模型详见T/CAMET 04011.2章节7.2.1图13</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.5 通信机制

通信机制功能的测试和验证方法详见表201。

<div style="text-align: center;">表 201 通信机制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)仅能由V0BC发起安全连接的建立过程；2)CI与V0BC采用周期发送和消息触发的方式进行通信；3)通信双方均采用大端字节序进行数据传输；4)CI与V0BC均应对接收的应用信息进行判断和逻辑运算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.6 应用信息定义

应用信息定义功能的测试和验证方法详见表202。

---

<div style="text-align: center;">表 202 应用信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC在列车进出站过程中，给CI发送信息控制站台门的打开和关闭。V0BC至CI的信息周期发送（发送周期按照各方发送方周期定义，对通信周期范围定义为200 ms~1 000 ms），CI接收到信息后向V0BC发送对应PSD的状态信息。对于可允许两侧开门的站台，系统将两侧的PSD当作两个不同的设备分别控制，为两侧的PSD分别分配全局唯一的标识（即整列的PSD当作一个设备，系统为其分配全局唯一的ID）。文中未做特殊说明的上下行定义，均为线路规定的运营上下行方向</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.7 数据类型定义

数据类型定义功能的测试和验证方法详见表203。

<div style="text-align: center;">表 203 数据类型定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对V0BC与CI之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义详见T/CAMET 04011.2章节7.3.1表31</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.8 VOBC 向 CI 发送心跳帧

V0BC 向 CI 发送心跳帧功能的测试和验证方法详见表 204。

---

<div style="text-align: center;">表 204 VOBC 向 CI 发送心跳帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC向CI发送心跳帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在列车车头最大安全前端进入CI通信区段前发送该信息包（具体时机各厂商自定义），用来维持V0BC设备和CI间通信链路的连续性。列车车头最大安全前端进入CI通信区段后，开始发送控制信息时不再发送心跳帧。V0BC向CI发送心跳帧信息详见T/CAMET 04011.2章节7.3.2.2.1表32</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.9 VOBC 向 CI 发送控制信息

V0BC 向 CI 发送控制信息功能的测试和验证方法详见表 205。

<div style="text-align: center;">表 205 VOBC 向 CI 发送控制信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC向CI发送控制信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>从列车车头最大安全前端进入CI通信区段开始，直至列车最大安全前端离开CI通信区段前，发送该信息包。本帧用于控制PSD的开关，VOBC至CI输出信息接口表详见T/CAMET04011.2章节7.3.2.2.2表33，应用层报文长度固定，全线站台门的编号方式应有共同的规则和相应的说明文件</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)站台区域具备连续通信条件；2)点式级别列车进站对标停车(跨线列车)；3)进行开关车门操作，站台门开关时机和一致性(包括方向和数量)符合设计要求</td></tr></table>

#### 6.7.10 VOBC 向 CI 发送城市自定义帧

VOBC 向 CI 发送城市自定义帧功能的测试和验证方法详见表 206。

---

<div style="text-align: center;">表 206 VOBC 向 CI 发送城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC向CI发送城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.11 VOBC 向 CI 发送厂商自定义帧

VOBC 向 CI 发送厂商自定义帧功能的测试和验证方法详见表 207。

<div style="text-align: center;">表 207 VOBC 向 CI 发送厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC向CI发送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-CTC-20</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同厂商时方可发送</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.12 VOBC 向 CI 发送注销请求帧

V0BC 向 CI 发送注销请求帧功能的测试和验证方法详见表 208。

<div style="text-align: center;">表 208 VOBC 向 CI 发送注销请求帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC向CI发送注销请求帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-21</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在列车判断需要与CI断开通信时，V0BC向CI发送注销信息，直至V0BC收到CI回复的注销信息，或者V0BC判断通信超时。 V0BC发送的“注销请求”包、“控制信息”包、“心跳”包在同一CAL包中不应同时存在，详见T/CAMET 04011.2章节7.3.2.2.5表37</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.7.13 CI 向 VOBC 发送心跳帧

CI 向 VOBC 发送心跳帧功能的测试和验证方法详见表 209。

<div style="text-align: center;">表 209 CI 向 VOBC 发送心跳帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送心跳帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-22</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>当CI与V0BC建立链接后，且尚未收到V0BC至CI控制信息之前，发送该信息包，用来维持V0BC设备和CI间通信链路的连续性</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.14 CI 向 VOBC 发送状态信息

CI 向 VOBC 发送状态信息功能的测试和验证方法详见表 210。

<div style="text-align: center;">表 210 CI 向 VOBC 发送状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-CTC-23</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>当CI收到V0BC的控制信息之后，发送该信息包。CI至V0BC输出信息接口表详见T/CAMET 04011.2章节7.3.3.2表32</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)站台区域具备连续通信条件；2)点式级别列车进站对标停车并结束停站作业且具备发车条件(跨线列车)；3)操作出站信号(关闭和开放)，列车具备红灯误出发防护功能；4)列车可以正确接收到站台门的状态信息(打开/关闭/互锁解除)</td></tr></table>

#### 6.7.15 CI 向 VOBC 发送城市自定义帧

CI 向 VOBC 发送城市自定义帧功能的测试和验证方法详见表 211。

---

<div style="text-align: center;">表 211 CI 向 VOBC 发送城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向VOBC发送城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-CTC-24</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.16 CI 向 VOBC 发送厂商自定义帧

Cl 向 VOBC 发送厂商自定义帧功能的测试和验证方法详见表 212。

<div style="text-align: center;">表 212 CI 向 VOBC 发送厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向VOBC发送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-CTC-25</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同一厂商时方可发送</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.17 CI 向 VOBC 发送注销回复帧

CI 向 VOBC 发送注销回复帧功能的测试和验证方法详见表 213。

<div style="text-align: center;">表 213 CI 向 VOBC 发送注销回复帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向VOBC发送注销回复帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-CTC-26</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在CI接收到VOBC的注销请求帧后，向VOBC回复注销回复帧。CI发送的“注销回复”包、“状态信息”包、“心跳”包在同一GAL包中不应同时存在</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

### 6.8 互联互通车地通信接口(VOBC 和 ATS) 测试需求

#### 6.8.1 接口连接方式

接口连接方式功能的测试和验证方法详见表 214 ~ 表 219。

<div style="text-align: center;">表 214 接口连接方式(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与ATS之间采用冗余网络进行通信。ATS与V0BC之间的网络拓扑结构采用A网-A网，B网-B网两个链路</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 215 接口连接方式(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与V0BC之间通信采用RSSP-Ⅱ安全通信协议。安全通信协议的具体要求参见《RSSP-Ⅱ铁路信号安全通信协议》（运基信号[2010]267号）。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议架构详见T/CAMET 04011.2章节6.1.2图6，其SAL/MASL/ALE三层，遵循RSSP-Ⅱ标准规定1) TCP及IP层使用标准TCP/IP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。RSSP-Ⅰ安全通信协议架构详见T/CAMET 04011.2章节6.1.2图7，RSSP-Ⅰ协议遵循RSSP-Ⅰ标准规定。1) UDP层使用标准UDP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 216 接口连接方式(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信应用层消息包定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>将 ATS-V0BC 间每个周期需要交互的应用信息通过组成 通用消息包进行传输，详见 T/CAMET 04011.2 章节 6.1.3 图 8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 217 接口连接方式（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IT-V0BC-ATS-MSG-CTG-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS/V0BC 每周期最多允许发送 1 个通用消息包，通用消息包中包含 ATS 与 V0BC 之间传输的各条应用信息。每个通用消息包总长不得超过 1 000 字节，详见 T/GAMET-04011.2 章节 6.1.3.2 表 15 和表 16</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试接口内容：电子地图版本控制信息。测试需求：1) 上电/进入线路时，在载设备默认采用版本较低的电子地图版本号；2) 车载设备与地面设备建立连接后，发送的通用消息包中为当前采用的电子地图版本号；3) 地面设备判断收到的通用信息包中车载电子地图版本号是否与地面一致，若一致，则进行正常通信；若不一致，则发送应用内容为空的通用消息包，通知车载设备地面电子地图版本号；4) 若车载设备收到空通用消息包，则判断本地是否存有与地面版本一致的电子地图，若有，则采用与地面版本一致的电子地图，继续与地面设备通信，通用消息包中的电子地图版本号与地面版本一致；否则，断开与地面设备的通信。其他见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 218 接口连接方式(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1. ATS及V0BC应分别对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方面的应用信息，并记录报警信息。具体检查方式如下：1)消息内容的一致性检查：包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性检查。2)通用应用(GAL)信息包消息所应包含的信息的完整性。3)其他逻辑检查2. ATS和V0BC应能分别对通信连接状态进行判断：1)ATS认为与V0BC通信中断的超时时间定义为TAtsTimeout(可配置，推荐值：6s)。2)V0BC认为与ATS通信中断的超时时间定义为TVobcTimeout(可配置，推荐值：6s)。3)若ATS在TAtsTimeout超时时间内，没有接收到来自V0BC的任何消息，则ATS应认为与V0BC的通信中断。4)若ATS判断收到V0BC的GAL包延迟已经达到TAtsTimeout，则ATS应丢弃此GAL包或认为与V0BC通信中断。5)若V0BC在TVobcTimeout超时时间内，没有接收到来自ATS的任何消息，则V0BC应认为与ATS的通信中断。6)若V0BC判断收到ATS的GAL包延迟已经达到TVobcTimeout，则V0BC应丢弃此GAL包或认为与ATS通信中断。7)通信中断的情况下，应生成报警信息。8)互联互通线网中，各厂商的V0BC与各条线路上的ATS的通信超时时间应一致，消息有效期时间应一致。3.列车在两ATS间移交时，V0BC判断列车最小安全后端越过ATS边界点后，应与移交ATS断开通信。4.V0BC判断与ATS断开通信，且不再与该ATS重新建立通信后，应断开与该ATS的TCP/IP连接</td></tr></table>

---

<div style="text-align: center;">表 218 接口连接方式(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>2. ~4. 测试需求如下： 断开 V0BC 与 ATS 的通信，观察通信中断时间 TAtsTimeout 和 TV0bcTimeout 是否正确，两子系统是否生成报警信息； 其余内容参见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 219 接口连接方式(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>EN50159:2010中提及的7种开放式网络存在的安全通信风险均由安全通信协议RSSP-Ⅱ安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。 
 军地无线通信双方（ATS-V0BC）应用层的通信故障处理分为如下几种情况： 
1) ATS和V0BC对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息； 
2) 通信中断的情况下处理：若ATS/V0BC认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.2 通信体系结构

通信体系结构功能的测试和验证方法详见表220和表221。

<div style="text-align: center;">表 220 通信体系结构(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信模型</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与V0BC通信协议模型详见T/CAMET 04011.2章节6.2.1图9</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 221 通信体系结构(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)仅能由V0BC发起安全连接的建立过程；2)ATS与V0BC采用周期发送和消息触发的方式进行通信；3)通信双方均采用大端字节序进行数据传输；4)ATS与V0BC均应对接收的应用信息进行判断和逻辑运算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.3 接口数据描述

接口数据描述功能的测试和验证方法详见表222。

<div style="text-align: center;">表 222 接口数据描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与V0BC之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.2章节6.3.1表17</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.4 ATS 向 VOBC 发送 ATS 心跳信息帧

ATS 心跳信息帧功能的测试和验证方法详见表 223。

<div style="text-align: center;">表 223 ATS 向 VOBC 发送 ATS 心跳信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS心跳信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>信息周期发送，用来维持ATS设备和V0BC间通信链路 的连续性。详见T/CAMET 04011.2章节6.3.2.2.I表18</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.8.5 ATS 向 VOBC 发送 ATO 命令信息帧

ATO 命令信息帧功能的测试和验证方法详见表 224。

<div style="text-align: center;">表 224 ATS 向 VOBC 发送 ATO 命令信息帧(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO命令信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>当ATS设备所管辖范围内有被控列车，ATS应周期向该V0BC发送ATO命令信息。详见T/CAMET 04011.2章节6.3.2.2.2表19</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 测试接口内容：下一ZC ID、下一CI ID、下一ATS ID。对应的测试需求如下：1) 对干计划列车ATS向列车发送下一ZC ID，在具备条件时，列车根据此ID呼叫响应的ZC；否则，发送默认值；2) 对于计划列车ATS向列车发送下一CI ID，在具备条件时，列车根据此ID呼叫响应的CI；否则，发送默认值；3) 对于计划列车ATS向列车发送下一ATS ID，在具备条件时，列车根据此ID呼叫响应的ATS；否则，发送默认值；4) 测试接口内容：服务号/表号、线路编号、车组所属线路号、车组号、源线路号、车次号、目的地线路号、目的地号、计划运行方向。对应的测试需求：一计划车/非计划车，检查ATS向ATO发送的命令信息帧中上述内容正确3. 测试接口内容：跳停站台ID、下一停车站台ID、下一站跳停命令。对应的测试需求如下：1) 设置跳停命令，列车位置在跳停命令接收范围内。列车将依据命令在跳停车站停车；2) 设置跳停命令，列车位置在跳停命令接收范围外。列车将继续在已设置跳停的站台执行停站操作；3) 取消跳停命令，列车位置在命令接收范围内。列车将依据命令在取消跳停车站停车；4) 取消跳停命令，列车位置在命令接收范围外。列车将继续跳停已设置取消跳停的站台。注：对于各厂家命令设置的范围依据协议中定义进行测试。</td></tr></table>

---

<div style="text-align: center;">表 224 ATS 向 VOBC 发送 ATO 命令信息帧(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO命令信息帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>4. 测试接口内容：站停时间、区间运行调整命令。对应的测试需求：列车进入站台，收到ATS发送的站停时间命令和区间运行调整命令，在站台停准停稳，打开车门，到达站停时间后，关闭车门，驶出站台，在区间按照收到的运行等级或区间运行时间行驶。5. 测试接口内容：扣车命令。对应的测试需求：列车最大安全前端所在站台有扣车命令，ATS发送“扣车有效”，列车执行扣车命令，否则发送“扣车取消，无扣车”6. 测试接口内容：折返命令。对应的测试需求如下：1) 对于计划列车，列车最大安全前端在站台内时，ATS按照列车运行计划判断列车是否要进行折返，并发送响应的站前折返、有人站后折返、无人自动折返命令；2) 对于非计划列车或与ATS无通信的列车，ATS向列车发送“不折返”命令，列车根据车载电子地图存储的区段属性显示折返提示。7. 测试接口内容：回段指示 对应的测试需求如下：V0BC与ATS通信正常：1) 当列车最大安全前端在转换轨内且列车为回段方向时，对于计划列车，ATS根据列车运行计划，向V0BC发送“回段”或“不回段”指示，列车在转换轨内进行相应的显示；对于非计划列车，ATS向V0BC发送默认值；2) 当列车最大安全前端不在转换轨内或列车不为回段方向时，ATS向V0BC发送的“回段指示”字段为默认值。V0BC与ATS断开：V0BC与ATS通信断开或收到的回段提示字段为默认值时，根据电子地图配置的区段属性，在转换轨内显示回段提示。8. 测试接口内容：门控策略。对应的测试需求如下：1) 站台为单侧门时，发送ATS中配置的默认值；2) 站台为双侧门时，发送相应的门控策略；同时开双侧门、先开左门再开右门、先开右门再开左门</td></tr></table>

---

#### 6.8.6 ATS 向 VOBC 发送 ATS 城市自定义帧

ATS 城市自定义帧功能的测试和验证方法详见表 225。

<div style="text-align: center;">表 225 ATS 向 VOBC 发送 ATS 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS 城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.7 ATS 向 VOBC 发送 ATS 厂商自定义帧

ATS厂商自定义帧功能的测试和验证方法详见表226。

<div style="text-align: center;">表 226 ATS 向 VOBC 发送 ATS 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能，各厂商分别定制。ATS判断通信的V0BC与自身属于同一厂商时，方可发送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.8 VOBC 向 ATS 发送 ATO 状态信息帧

ATO 状态信息帧功能的测试和验证方法详见表 227。

<div style="text-align: center;">表 227 VOBC 向 ATS 发送 ATO 状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO 状态信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-14</td></tr></table>

---

<div style="text-align: center;">表 227 VOBC 向 ATS 发送 ATO 状态信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO状态信息帧</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>若已建立ATO模式，V0BC应周期向ATS发送ATO状态信息。ATS需针对每列车的ATO状态信息进行超时判断，配置时间内未收到相应列车的ATO状态信息，则清除该车的ATO状态信息。未收到ATS发送的信息前，对应字段填写默认值。详见T/CAMET 04011.2章节6.3.2.3.1表22</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)测试接口内容：服务号/表号、线路编号、车组号所属线路号、车组号、源线路号、车次号、目的地号、司机号。测试需求：一计划车/非计划车，检查ATO向ATS发送的命令信息帧中上述内容正确。2)测试接口内容：ATO工作模式。测试需求：列车ATO未建立和AM自动驾驶时，向ATS发送的内容正确。3)测试接口内容：区间运行调整命令、跳停状态、扣车状态、下一停车站台ID。测试需求：列车ATO未建立和AM自动驾驶时，向ATS发送的内容正确</td></tr></table>

#### 6.8.9 VOBC 向 ATS 发送列车信息帧

列车信息帧功能的测试和验证方法详见表228。

<div style="text-align: center;">表 228 VOBC 向 ATS 发送列车信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本消息为周期信息，当V0BC与ATS之间的安全连接建立后，周期发送。详见T/CAMET 04011.2章节6.3.2.2.2表23</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)测试接口内容：列车识别号ID、线路编号、列车定位状态、运行方向、车轮方向、车头位置、车尾位置、过读测距误差、欠读测距误差、车载当前模式、车载工作模式、车载ATP</td></tr></table>

---

<div style="text-align: center;">表 228 VOBC 向 ATS 发送列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车信息帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>当前模式、列车速度信息、车门状态、停稳状态、预选模式、当前紧急制动触发速度、当前推荐速度、安全防护点位置、障碍点位置。测试需求：列车以某种工作模式（联锁控制级别、点式、CBTC）和驾驶模式（RM、CM、AM）（需遍历工作模式和驾驶模式的各种组合）运行，验证V0BC向ATS发送的列车识别号ID、线路编号、列车定位状态、运行方向、车轮方向、车头位置、车尾位置、过读测距误差、欠读测距误差、车载当前模式、车载工作模式、车载ATP当前模式、列车速度信息、车门状态、停稳状态、预选模式、当前紧急制动触发速度、当前推荐速度、安全防护点位置、障碍点位置数据正确。2）测试接口内容：列车完整性、测试需求：连续级列车，运行过程中完整性丢失，则向ATS报告“列车完整性”为完整，否则报告列车不完整。3）测试接口内容：紧急制动状态。测试需求：连续级列车，紧急制动时（如完整性丢失），向ZC发送紧急制动状态；否则发送无紧急制动状态。4）测试接口内容：无人折返状态。测试需求：当列车在无人自动折返中（从车载ATP接收到无人折返命令开始到换端前）、无人折返折返中，未进行无人自动折返几种状态时，向ATS发送响应的无人自动折入中、无人折返折出中、未进行无人自动折返状态。5）测试接口内容：列车AR状态。测试需求：列车折返时，向ATS发送处于AR状态，否者发送未处于AR状态；列车首端不会向ATS发送AR状态。6）测试接口内容：停车保证状态。测试需求：连续式控制等级列车，前方进路已开放，且列车接近锁闭，人解进路，ZC向列车发送停车保证请求信息；列车根据计算结果，向ZC和ATS发送可以停车、无法停车的状态</td></tr></table>

#### 6.8.10 VOBC 向 ATS 发送车载设备报警信息帧

车载设备报警信息帧功能的测试和验证方法详见表229。

---

<div style="text-align: center;">表 229 VOBC 向 ATS 发送车载设备报警信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载设备报警信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载设备报警信息帧详见 T/CAMET 04011.2 章节 6.3.2.3.3 表 25</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>遍历 ATO 故障、BTM 故障、车载人机界面故障、雷达故障、与列车信息管理系统通信故障、测速传感器故障、加速度计故障、ATP 故障（与 ATS 通信正常时），验证列车向 ATS 发送相应的故障信息</td></tr></table>

#### 6.8.11 VOBC 向 ATS 发送车载设备日检状态信息帧

车载设备日检状态信息帧功能的测试和验证方法详见表230。

<div style="text-align: center;">表 230 VOBC 向 ATS 发送车载设备日检状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载设备日检状态信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载设备日检状态信息帧详见 T/CAMET 04011.2 章节 6.3.2.3.4 表 26</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>当需要发送车载设备日检状态信息帧时，列车向 ATS 发送该信息，且列车识别号正确，日检状态根据定义进行检查</td></tr></table>

#### 6.8.12 VOBC 向 ATS 发送 VOBC 城市自定义帧

V0BC 城市自定义帧功能的测试和验证方法详见表 231。

<div style="text-align: center;">表 231 VOBC 向 ATS 发送 VOBC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能：具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.8.13 VOBC 向 ATS 发送 VOBC 厂商自定义帧

VOBC厂商自定义帧功能的测试和验证方法详见表232。

<div style="text-align: center;">表 232 VOBC 向 ATS 发送 VOBC 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制。VOBC判断通信的ATS与自身属于同一厂商时，方可发送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

### 6.9 互联互通车地通信接口(VOBC 和 ZC) 测试需求

#### 6.9.1 通信体系结构

通信体系结构功能的测试和验证方法详见表233和表234。

<div style="text-align: center;">表 233 通信体系结构(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信模型</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC与V0BC通信协议模型详见T/CAMET 04011.2章节5.2.1图4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 234 通信体系结构(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)仅能由V0BC发起安全连接的建立过程；2)ZC与V0BC采用周期发送和消息触发的方式进行通信；3)通信双方均采用大端字节序进行数据传输；4)ZC与V0BC均应对接收的应用信息进行判断和逻辑运算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.9.2 接口连接方式

接口连接方式功能的测试和验证方法详见表 235 和表 236。

<div style="text-align: center;">表 235 接口连接方式(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与ZC之间采用冗余网络进行通信(下文以A网,B网进行描述)ZC与V0BC之间的网络拓扑结构采用A网-A网,B网-B网两个链路</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 236 接口连接方式(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSC-CTC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC与V0BC之间通信可采用RSSP-Ⅱ或RSSP-Ⅰ安X全通信协议。RSSP-Ⅱ安全通信协议的具体要求参见《RSSP-Ⅱ铁路信号安全通信协议》（运基信号[2010]267号）；RSSP-Ⅰ安全通信协议的具体要求参见《RSSP-Ⅰ铁路信号安全通信协议》（运基信号[2010]267号）。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议架构详见T/CAMET 04011.2章节5.1.2图1，其SAI/MASL/ALE三层，遵循RSSP-Ⅱ标准规定。1) TCP及IP层使用标准TCP/IP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。RSSP-Ⅰ安全通信协议架构详见T/CAMET 040011.2章节5.1.2图2，其RSSP-Ⅰ协议遵循RSSP-Ⅰ标准规定。1) UDP层使用标准UDP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.9.3 动态交互描述

动态交互描述功能的测试和验证方法详见表 237 ~ 表 240。

<div style="text-align: center;">表 237 动态交互描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信应用层消息包定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>通信应用层消息包定义。将ZC-V0BC间每个周期需要交互的应用信息通过组成通用消息包进行传输，详见T/CAMET 04011.2章节5.1.3图3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

表 238 动态交互描述(三)


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-Y0BC/ZC-MSG-CTC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC/V0BC每周期最多允许发送1个通用消息包， 通用消息包中包含ZC与V0BC之间传输的各条应用 信息 每个通用信息包总长不得超过1 000字节，详见T/ CAMET 04011.2章节5.1.3.2表1和表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 239 动态交互描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1.ZC及V0BC应分别对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方的应用信息，并记录报警信息。具体检查方式如下：1)消息内容的一致性检查：包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性检查；</td></tr></table>

---

<div style="text-align: center;">表 239 动态交互描述(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>2) 通用应用 (GAL) 信息包消息所应包含的信息的完整性。2. ZC 和 VOBC 应能分别对通信连接状态进行判断:1) ZC 认为与 VOBC 通信中断的超时时间定义为 TZcTimeout (3 s ~ 9 s, 可配置);2) VOBC 认为与 ZC 通信中断的超时时间定义为 TVobcTimeout (3 s ~ 9 s, 可配置);3) 若 ZC 在 TZcTimeout 超时时间内, 没有接收到来自 VOBC 的任何消息, 则 ZC 应认为与 VOBC 的通信中断;4) 若 ZC 判断收到 VOBC 的 GAL 包延迟已经达到 TZcTimeout, 则 ZC 应丢弃此 GAL 包或认为与 VOBC 通信中断;5) 若 VOBC 在 TVobcTimeout 超时时间内, 没有接收到来自 ZC 的任何消息, 则 VOBC 应认为与 ZC 的通信中断;6) VOBC 判断收到 ZC 的 GAL 包延迟已经达到 TVobcTimeout, 则 VOBC 应丢弃此 GAL 包或认为与 ZC 通信中断;7) 互联互通线网中, 各厂商 VOBC 与各条线路上的 ZC 的通信超时时间应一致, 消息有效期时间应一致;8) 处于连续式列车控制级别的 VOBC 判断与 ZC 的通信中断后, 若列车未处于停稳状态, 则应输出紧急制动; 若列车处于停稳状态, 则可输出紧急制动。VOBC 在与 ZC 设备通信时, 当判断与 ZC 设备通信断开并且不再与对方建立连接后, 应断开与 ZC 设备的 TCP/CP 或 UDP 连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>功能内容 2. 中 1) ~ 7) 测试需求如下:断开 VOBC 与 ZC 的通信, 观察通信中断时间 TZcTimeout 和 TVobcTimeout 是否正确, 两子系统是否生成报警信息。功能内容 2. 中的 8) 测试需求如下:CTC 列车未停稳时, 断开 VOBC 与 ZC 的通信, 观察列车是否输出紧急制动; CTC 列车停稳时, 断开 VOBC 与 ZC 的通信, 观察列车是否输出紧急制动。其余内容参见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 240 动态交互描述(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议 RSSP-Ⅱ安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。 山地无线通信双方（ZC-V0BC）应用层的通信故障处理分为如下几种情况： ZC 和 V0BC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息。 通信中断的情况下处理：若 ZC/V0BC 认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.4 接口数据描述

接口数据描述功能的测试和验证方法详见表241。

<div style="text-align: center;">表 241 接口数据描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本节对ZC与V0BC之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.2章节5.3.1表3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.5 ZC 向 VOBC 发送列车控制信息

ZC 向 VOBC 发送列车控制信息功能的测试和验证方法详见表 242。

---

<div style="text-align: center;">表 242 ZC 向 VOBC 发送列车控制信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车控制信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ZC-MSG-CTC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC对满足MA发送条件的列车周期发送列车控制信息。详见T/CAMET 04011.2章节5.4.2.1表4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 测试接口内容: 下一ZC ID。对应的测试需求如下:1) 当MA终点未到达ZC边界时, ZC不向列车发送下一ZC ID的信息;2) 当MA终点到达ZC边界或者越过ZC边界时, 列车最大安全前端所在ZC向列车发送下一站ZC ID信息, 列车根据该ZC ID呼叫接管ZC并注册成功;3) RM和点式控制级别与ZC建立连接, ZC是否发送下一ZC ID, 因厂家而异, 按实际情况进行测试。2. 测试接口内容: MA信息中除停车保证外的内容。对应的测试需求如下:1) MA起点位置同列车位置报告的最小安全后端位置;2) 安全防护点和障碍点。保护区段有效的情况下: ZC发送的安全防护点位置为保护区段末端位置回退一定的安全余量(最不利情况下前车回退距离+列车悬垂+余量), 障碍点为保护区段起点位置。保护区段无效或者移动授权终点无保护区段的情况下, ZC发送的安全防护点位置不能越过进路的终端信号机; 障碍点为无效值。移动授权终点为前车车尾或除1)、2) 外的情况, ZC发送的安全防护点位置不能越过危险点; 障碍点为无效值。3. 测试接口内容: MA信息障碍点的内容。对应的测试需求如下:障碍点有效的情况下, 列车越过障碍点, 立即紧急制动。4. 测试接口内容: MA信息中停车保证。对应的测试需求如下:1) 有连续级列车占用前方开放进路的接近锁闭区段, 要取消或人解前方进路时, ZC向列车发送停车保证请求, 分能停车和不能停车两种情况;</td></tr></table>

---

<div style="text-align: center;">表 242 ZC 向 VOBC 发送列车控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车控制信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>2) 工程项目中能接受按停车保证要求停车后，会进入保护区段的情况；如被人解的进路的首区段为前一条进路的保护区段，且保护区段锁闭时，停车保证中的安全防护点和障碍点和保护区段有效性与移动授权信息中的安全防护点、障碍点及保护区段有效性一致；3) 工程项目中不能接受按停车保证要求停车，会进入保护区段的情况；停车保证中的安全防护点为要进行人解操作的信号机，障碍点和保护区段有效性同移动授权信息中一致；4) 列车收到停车保证请求后，计算是否能在对应的安全防护点前停下，分为3种可以停车、无法停车和无效3种情况。当收到可以停车时，进路立即解锁，否则进路不解锁；5) 无取消或人解前方进路信息时，ZC向列车发送的停车保证请求为无；列车向ZC发送的停车保证响应为无效。6) 测试接口内容：路径信息、对应的测试需求如下：1) 排列并开放线路中包含道岔最多的进路，部分道岔在定位，部分道岔在反置；2) ZC将该进路中的道岔信息，按照路径信息的要求发送给列车，列车按照ZC发送的道岔状态运行能运行至移动授权终点且未紧急制动，则验证该数据正确。6. 测试接口内容：PSD状态对应的测试需求如下：1) PSD未被互锁解除，当PSD处于非关闭且锁闭状态，验证已越过PSD区域的移动授权不回缩，ZC将MA范围内的PSD处于非关闭且锁闭的状态发送给列车，由列车进行控制，列车会在站台外停车；2) PSD未被互锁解除，当PSD处于关闭且锁闭状态，办理进站进路，进站进路开放灭灯允许信号，移动授权延伸过站台，验证ZC将MA信息中该PSD的关闭且锁闭状态发送给列车，列车可以进入站台；</td></tr></table>

---

<div style="text-align: center;">表 242 ZC 向 VOBC 发送列车控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车控制信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>3) PSD 被互锁解除, PSD 处于打开状态, 办理进站进路, 进站进路开放灭灯允许信号, 移动授权延伸过站台, 验证 ZC 将 MA 信息中该 PSD 的互锁解除状态发送给列车, 列车可以进入站台;4) PSD 被互锁解除, PSD 处于关闭状态, 办理进站进路, 进站进路开放灭灯允许信号, 移动授权延伸过站台, 验证 ZC 将 MA 信息中该 PSD 的互锁解除状态发送给列车, 列车可以进入站台7. 测试接口内容: ESB 状态 对应的测试需求如下:1) 移动授权已越过站台, 站台紧急关闭按钮被按下, 验证 ZC 将 MA 范围内的 ESB 被按下的状态发送给列车, 由列车进行控制, 列车会在站台外停车;2) 站台紧急关闭按钮未被按下, 办理进站进路, 移动授权延伸过站台, 验证 ZC 将 MA 范围内的 ESB 未被按下的状态发送给列车, 列车可以进入站台;3) 列车位于站台内, 此时 ESB 激活, 列车应该施加紧急制动8. 测试接口内容: 无人折返按钮状态 对应的测试需求如下:1) 连续式列车以 AM 模式行驶, 在站台停准停稳, 按压站台无人自动折返按钮, 验证 ZC 向列车转发无人自动折返按钮按下的信息, 列车进入无人折返模式;2) 连续式列车以 AM 模式行驶, 在站台停准停稳, 站台可以进行无人自动折返, 未按下无人自动折返按钮, 司机也未按压列车上的相关按钮, 验证 ZC 向列车转发无人自动折返按钮未按下的信息, 列车不会进入无人折返模式9. 测试接口内容: 临时限速信息, 在 ATS 上设置临时限速对应的测试需求如下:1) 当移动授权未覆盖至临时限速区段时, 验证 ZC 向列车发送的 MA 中无临时限速信息;2) 当移动授权覆盖至临时限速区段时, 验证 ZC 向列车发送区段的临时限速信息, 包括临时限速的始端和终端位置以及在轨道上的偏移量和限速值.</td></tr></table>

---

<div style="text-align: center;">表 242 ZC 向 VOBC 发送列车控制信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车控制信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>10. 测试接口内容：ZC-ZC 通信延时。对应的测试需求如下：1) MA 延伸过边界点时，移交 ZC 填写该信息，取值为计算当前 MA 时所使用的相邻 ZC 的信息包的延时，V0BC 在判断 MA 有效性时，扣除该延时；2) MA 未延伸过边界点时，填写默认值。11. 测试接口内容：运行目的地属性信息。对应的测试需求如下：1) MA 终点处目的地属性为通过、折返或回段时，则 ZC 向 ATP 发送通过、折返或回段的目的地属性信息；2) 若 ZC 无目的地属性信息，则发送默认值；3) 若 ATP 无相关功能，则接收到该信息时不处理</td></tr></table>

#### 6.9.6 ZC 向 VOBC 发送应用层安全连接——注册/注销响应

应用层安全连接注册/注销响应功能的测试和验证方法详见表243。

<div style="text-align: center;">表 243 ZC 向 VOBC 发送应用层安全连接——注册/注销响应</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用层安全连接——注册/注销响应</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC发送的注册/注销请求时，ZC返回该报文，详见T/CAMET 04011.2章节5.4.2.2表5</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>当列车已经定位，向ZC发送注册，ZC判断符合注册条件，ZC发送“注册/注销响应信息”为注册成功；否则发送注册失败，并将“注册失败原因”的错误代码发送给列车。如果列车始终未收到该信息，就一直发送注册请求，直到列车出清该ZC控制区域。列车具备发送注销请求的条件（如列车位置丢失、过移交边界等），向ZC发送注销请求，ZC判断符合注销条件，ZC发送“注册/注销响应信息”为注销成功。如果列车始终未收到该信息，就一直发送注销请求，直到列车出清该ZC控制区域</td></tr></table>

---

#### 6.9.7 ZC 向 VOBC 发送 ZC 主动注销请求

ZC 主动注销请求功能的测试和验证方法详见表 244。

<div style="text-align: center;">表 244 ZC 向 VOBC 发送 ZC 主动注销请求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC主动注销请求</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC的注销条件成立时，发送该信息。详见T/CAMET 04011.2章节5.4.2.3表6ZC发送“ZC主动注销请求”包后，应持续发送“ZC主动注销请求”包，不接受V0BC发送的除“注销信息包”外的其他信息。直至收到V0BC发送的“注销信息包”或判断通信超时。V0BC收到“ZC主动注销请求”包后，应向ZC发送“注销信息包”</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ZC的主动注销条件成立时（如列车越过移交边界），向列车发送该信息，包括注销命令和注销原因V0BC收到主动注销请求后，回复注销信息</td></tr></table>

#### 6.9.8 ZC 向 VOBC 发送特殊控制报文

特殊控制报文功能的测试和验证方法详见表245。

<div style="text-align: center;">表 245 ZC 向 VOBC 发送特殊控制报文</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>特殊控制报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ZC对于已经注册的列车，在满足下述条件之一时发送该信息帧：
1)列车已经定位（收到列车位置报告），但是不满足计算移动授权条件；
2)ZC判断列车应紧急制动；
3)非折返列车注册成功，但未收到列车的位置报告；
4)列车折返过程中，列车两端V0BC同时与ZC建立通信时，ZC可向其中一端发送特殊控制报文；
其他需要保持链路的情况。</td></tr></table>

---

<div style="text-align: center;">表 245 ZC 向 VOBC 发送特殊控制报文（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>特殊控制报文</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在列车折返过程中，当折出端与ZC注册后，ZC在收到折出端的位置报告之前不应发送特殊控制报文。列车当前级别为CBTC控制级别时，对特殊控制报文进行处理，否则特殊控制报文只用于维持安全连接。特殊控制命令详见表298</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 测试接口内容：紧急制动命令对立面测试需求如下：1) 连续级列车安全包络位于道岔上，道岔故障，验证ZC向列车发送特殊控制报文，报文中“紧急制动命令”为有命令，“链路保持命令”为无命令时，“链路保持命令”中应存在一个字段取值不为默认值；2) 非折返列车注册成功，但未收到列车的位置报告时，ZC向V0BC发送的“紧急制动命令”字段取值为“有命令”。2. 测试接口内容：链路保持命令。对应的测试需求如下：4) 列车已经定位（收到列车位置报告），但不满足计算移动比较条件（如列车未完成头部筛选或列车占压区段未锁闭等）验证ZC向列车发送特殊控制报文，报文中“链路保持命令”中其他需要保持链路的情况“为有；2) 列车（RM、点式、连续式）已经与接管ZC建立连接，但接管ZC无法为列车计算移动授权（如无锁闭的进路等），验证当前控制ZC向列车发送特殊控制报文，报文中“链路保持命令”中“接管ZC无法计算有效移动授权状态”为无法计算，否则为已计算。3. 测试接口内容：折返过程中尾端安全连接保持。对应的测试需求如下：1) 对于折返过程中不需要首尾V0BC同时与ZC建立通信的列车，“折返过程中尾端安全连接保持”发送内容为不保持；2) 对于折返过程中需要首尾V0BC同时与ZC建立通信的列车，ZC对尾端V0BC发送特殊控制报文；具体发送情况可参考相关工程文件；</td></tr></table>

---

<div style="text-align: center;">表 245 ZC 向 VOBC 发送特殊控制报文(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>特殊控制报文</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>3) 在列车折返过程中，如存在折出端 VOBC 重新与 ZC 建立通信的过程，当折出端与 ZC 注册后，ZC 在收到折出端的位置报告之前不发送特殊控制报文。4. 测试接口内容：列车运行等级。对应的测试需求如下：1) 列车处于连续式控制等级，需要对特殊控制报文进行相应处理；2) 列车处于 RM 或点式控制等级，不对特殊控制报文进行处理，只用于维持安全连接</td></tr></table>

#### 6.9.9 ZC 向 VOBC 发送 ZC 城市自定义帧

ZC城市自定义帧功能的测试和验证方法详见表246。

<div style="text-align: center;">表 246 ZC 向 VOBC 发送 ZC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能 具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>工程中约定</td></tr></table>

#### 6. 9. 10 ZC 向 VOBC 发送 ZC 厂商自定义帧

ZC 厂商自定义帧功能的测试和验证方法详见表 247。

<div style="text-align: center;">表 247 ZC 向 VOBC 发送 ZC 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ZC厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，V0BC收到本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>工程中约定</td></tr></table>

---

#### 6.9.11 VOBC 向 ZC 发送列车位置信息

列车位置信息功能的测试和验证方法详见表248。

<div style="text-align: center;">表 248 列车位置信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车位置信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>该信息周期发送，用来维持ZC设备和V0BC间安全通信的连续性。列车在ZC间移交过程中，V0BC与移交、接管ZC同时通信时，同一周期生成的向两个ZC发送的“列车位置信息包”内容应一致。详见T/CAMET 04011.2章节5.4.3.1表10</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)测试接口内容：运行方向、激活端、列车包络线、车载工作模式、车载驾驶模式、列车速度、停稳信息、受控ZC的ID。对应的测试需求：列车以某种工作模式（联锁控制级别、点式、CBTC）和驾驶模式（RM、CM、AM）（需遍历工作模式和驾驶模式的各种组合）运行，验证V0BC向ZC发送的运行方向、激活端、列车包络线，以及工作模式和驾驶模式、列车速度和停稳信息、受控ZC的ID正确。2)测试接口内容：车辆状态中的停车保证信息，与6.9.4中停车保证内容一起测试。3)测试接口内容：列车完整性、对应的测试需求：列车运行过程中完整性丢失，则向ZC报告“列车完整性”为不完整，否则报告列车完整。4)测试接口内容：无人折返指示灯。对应的测试需求：列车根据无人自动折返流程，向ZC分别发送“折返指示灯常亮”“折返指示灯常灭”“折返指示灯闪烁”。5)测试接口内容：紧急制动状态。对应的测试需求：列车紧急制动时（如完整性丢失），向ZC发送该状态。6)测试接口内容：退行距离。对应的测试需求：列车退行时，向ZC报告退行距离。7)测试接口内容：V0BC与ZC建立通信时无法确定准确位置。对应的测试需求：V0BC与ZC建立通信时无法确定</td></tr></table>

---

<div style="text-align: center;">表 248 列车位置信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车位置信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>准确位置则“运行方向”“车头估计位置所在轨道区段ID”“车头估计位置在轨道区段内偏移量”“车尾估计位置所在轨道区段ID”“车尾估计位置在轨道区段内偏移量”“过读误差”“欠读误差”均填写默认值；ZC收到默认值后，如果ZC之前无列车有效位置，向列车发送“紧急制动”的特殊控制报文。如果ZC之前有列车有效位置，可以丢弃此位置报告信息，采用之前的位置报告，继续与VOBC通信，直至通信超时断开</td></tr></table>

#### 6.9.12 VOBC 向 ZC 发送应用层注册/注销请求

应用层注册/注销请求功能的测试和验证方法详见表249。

<div style="text-align: center;">表 249 VOBC 向 ZC 发送应用层注册/注销请求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用层注册/注销请求</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC满足注册/注销条件时,应重复发送该信息。V0BC 的带有“应用层注册/注销请求”信息包的GAL包中,应不 带有“列车位置信息”包。详见T/CAMET 04011.2章节 5.4.3.2表12</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>同应用层安全连接注册/注销响应</td></tr></table>

#### 6. 9. 13 VOBC 向 ZC 发送 VOBC 城市自定义帧

V0BC 城市自定义帧功能的测试和验证方法详见表 250。

<div style="text-align: center;">表 250 VOBC 向 ZC 发送 VOBC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ZC-MSG-CTC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>工程中约定</td></tr></table>

---

#### 6. 9. 14 VOBC 向 ZC 发送 VOBC 厂商自定义帧

V0BC厂商自定义帧功能的测试和验证方法详见表251。

<div style="text-align: center;">表 251 VOBC 向 ZC 发送 VOBC 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ZC-MSG-CTC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，ZC收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>工程中约定</td></tr></table>

## 7 测试案例要求

### 7.1 总体要求

a) 互联互通测试案例编写需要依据本部分的测试需求进行，需要对测试需求中规定的功能点实现全覆盖。每个测试需求可以对应多个测试案例。

b）测试案例的编写以及测试过程需要遵循以下原则：

——测试过程中同时涉及车载和地面设备时，默认采用不同厂家设备；

——测试过程中涉及两个控区地面设备时，默认采用不同厂家设备；

——对于相同功能但正线和跨线接口实现方式不同的需求，需要在正线和跨线接口测试。

c）鉴于各厂家对故障的识别及处理原则存在较大差异，故障相关测试内容在互联互通产品供应商测试及验证阶段执行。

### 7.2 具体要求

测试案例中应至少描述以下内容：

——对应的测试需求：

——本规范中定义的测试阶段；

——测试条件（测试时应具备的前提条件）：

——测试环境（如时间、地点、人员）；

——被测设备的厂家编号等。

---

## 参考文献

[1]《RSSP-Ⅱ铁路信号安全通信协议》(运基信号[2010]267号)

[2] IEEE 802.3 系列标准

---

中国城市轨道交通协会团体标准

城市轨道交通

基于通信的列车运行控制系统（CBTC）

互联互通测试规范

第1部分：CBTC部分测试及验证

T/CAMET 04012.1—2018

中国铁道出版社有限公司出版发行

(100054, 北京市西城区右安门西街 8 号)

出版社网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm×1230 mm 1/32 印张：5.375 字数：151 千

2019 年 6 月第 1 版 2019 年 6 月第 1 次印刷

书号：15113·5690 定价：40.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本社发行部联系调换。发行部电话：路（021）73174，市（010）51873174