# 中国城市轨道交通协会团体标准

T/CAMET 04012.2—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范 第2部分：点式部分测试及验证

# Urban rail transit — Test specification for interoperability of communication based train control system

# Part 2: Test and verification of intermittent train control part

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
5.1 互联互通系统供应商测试及验证平台需求 …… 8    
5.2 互联互通系统集成实验室测试及验证平台需求 …… 8    
5.3 互联互通试验线测试及验证平台需求 …… 10    
6 测试需求 …… 10    
6.1 互联互通系统测试验证活动的划分原则 …… 10    
6.2 互联互通总体功能及接口功能分配 …… 12    
6.3 互联互通测试需求 …… 43    
6.4 互联互通系统测试需求 …… 44    
6.5 互联互通应答器接口需求 …… 93    
6.6 互联互通计算机联锁（CI）间接口测试需求 …… 109    
6.7 互联互通跨线 ATS 间接口测试需求 …… 116    
6.8 互联互通车地通信接口（VOBC 和 ATS）测试需求 …… 125

---

6.9 互联互通车地通信接口 (VOBC 和 CI) 测试需求 ..... 136  
7 测试案例要求 ..... 146  
7.1 总体要求 ..... 146  
7.2 具体要求 ..... 146  
参考文献 ..... 148

---

## 前言

T/CAMET 04012《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》分为以下两个部分：

——第1部分：CBTC部分测试及验证；

——第2部分：点式部分测试及验证。

本部分是 T/CAMET 04012 的第 2 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：中国铁道科学研究院集团有限公司通信信号研究所、交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、浙江众合科技股份有限公司、北京交通大学、株洲中车时代电气股份有限公司。

本部分主要起草人：编写组：李亮、史宁娟、王鲲、杜恒、刘合叶、刘鲁鹏、卢然、方发根、周在福、黄友能、王悉、吕浩炯、张大涛。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、张琼燕、段晨宁、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、王道敏、徐鼎。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC) 互联互通测试规范 第2部分:点式部分测试及验证

## 1 范围

T/CAMET 04012 的本部分规定了基于通信的列车运行控制（CBTC）互联互通系统共点式部分功能验证测试以及接口验证测试。

本部分适用于满足互联互通要求的 CBTC 系统，其点式部分验证测试应包含的各个阶段，按照阶段定义和互联互通需求特点对需求验证进行分配，并作为后续互联互通测试案例编写的依据，对案例的编写具有指导作用。

## 2 规范性引用文件

## 轨道交

下列文件对于本部分的应用是必不可少的。凡注日期的引用文件，仅注日期的版本适用于本部分。凡不注日期的引用文件，其最新版本（包括所有修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB/T 21562—2008 轨道交通可靠性、可用性、可维护性和安全性规范及示例(IEC 62278:2002, IDT)

GB/T 22239—2008 信息安全技术 信息系统安全等级保护基本要求

GB/T 28808—2012 轨道交通通信、信号和处理系统控制和防护系统软件（IEC 62279:2002, IDT）

GB/T 28809—2012 轨道交通通信、信号和处理系统信号用安全相

---

关电子系统（IEC 62425:2007, IDT）

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第1部分：系统总体要求

T/CAMET 04010.3 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第3部分：车载电子地图

T/CAMET 04011.1 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第1部分：应答器报文

T/CAMET 04011.2 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第2部分：CBTC系统车地连续通信协议

T/CAMET 04011.3 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）与车辆的接口

T/CAMET 04011.4 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通接口规范 第 4 部分: 区域控制器 (ZC) 间接口

T/CAMET 04011.5 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通接口规范 第 5 部分: 计算机联锁 (CI) 间接口

(CBTC)互联互通接口规范 第6部分:列车自动监控系统(ATS)间接口

T/CAMET 04012.1 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通测试规范 第 1 部分: CBTC 部分测试及验证

EN 50159:2010 铁路应用 通信、信号和处理系统 信号的安全相关的电子系统(Railway applications—Communication, Signaling and Processing System—Safety-related Communication in Transmission Systems)

IEEE Std 1474.1-2004 IEEE 基于通信的列车控制（CBTC）系统的性能和功能要求（IEEE Standard for Communications-Based Train Control）

---

(CBTC) Performance and Functional Requirements)

IEEE Std 1474.4-2011 IEEE 基于通信的列车控制（CBTC）系统的系统功能测试推荐实践（IEEE Recommended Practice for Functional Testing of a Communications Based Train Control (CBTC) System）

## 3 术语和缩略语

GB 50157—2013、CJ/T 407—2012、T/CAMET 04010.1 以及 T/CAMET 04012.1 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control(CBTC)

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

---

#### 3.1.5 

## 列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB 50157—2013, 定义 2.0.39]

#### 3.1.6 

## 列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

[GB 50157—2013, 定义 2.0.40]

#### 3.1.7 

## 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.8 

## 维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护。

[T/CAMET 04010.1,术语3.1.8]

#### 3.1.9 

## 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点

[T/CAMET 04010.1,术语3.1.10]

#### 3.1.10 

## 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T 407—2012, 定义 3.1.7]

#### 3.1.11 

## 装备列车 CBTC-equipped trains

装备了 CBTC 系统车载设备且设备处于工作状态的列车。

---

$$ \left[T/CAMET04010.1,术语3.1.11\right] $$ 

#### 3.1.12 

非装备列车 Non-CBTC-equipped trains

没有装备 CBTC 系统车载设备或者 CBTC 系统车载设备处于不工作状态的列车。

[T/CAMET 04010.1,术语3.1.12]

#### 3.1.13 

## 转换轨 transfer track

指车辆段/停车场与正线的连接轨，运营列车在驶入/驶出转换轨过程中，当条件具备时，进行列车运行控制级别及驾驶模式转换。

[T/CAMET 04010.1.术语3.1.13]

#### 3.1.14 

跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 040101.1.14]

#### 3.1.15 

平均故障间隔时间（平均无故障时间）mean time between failures

指设备连续发生两次故障之间的平均间隔时间。

[T/CAMET04012.1,术语3.1.15]

#### 3.1.16 

列车自动驾驶模式 automatic train operating mode

在司机监控下，CBTC系统自动控制列车运行，并进行安全防护的列车驾驶模式。

[T/CAMET04012.1,术语3.1.16]

#### 3.1.17 

列车自动防护模式 coded train operating mode

在列车自动防护设备防护下，司机驾驶列车运行的列车驾驶模式。



[T/CAMET 04012.1,术语3.1.17]

---

#### 3.1.18 

## 限制人工驾驶模式 restricted train operating mode

司机按规定的日视行车限速控车运行，列车自动防护设备进行超速防护的列车驾驶模式。

[T/CAMET 04012.1,术语 3.1.18]

#### 3.1.19 

非限制人工驾驶模式 emergency unrestricted train operating mode

ATP 自动防护设备已被切除，车载设备不对列车运行进行监控，司机按操作规程驾驶列车的列车驾驶模式。

[T/CAMET 04012.1,术语3.1.19]

#### 3.1.20 

## 移交重叠区 handover overlap region

为使列车在相邻区域控制器（ZC）间平滑移交，在 ZC 管辖范围交界处设置的用于列车移交控制的区域。

[T/CAMET 04010.1,术语 3.1.15]

#### 3.1.21 

## 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1,术语3.1.16]

### 3.2 缩略语

AM: 列车自动驾驶模式 (Automatic Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO: 列车自动运行 (Automatic Train Operation)

ATP: 列车自动防护 (Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

BTM: 应答器传输模块 (Balise Transfer Module)

CBTC: 基于通信的列车控制 (Communication Based Train Control)

---

CI: 计算机联锁 (Computerized Interlocking)

CTC: 连续式等级 (Continuous Train Control)

DCS: 数据通信系统 (Data Communication System)

ITC: 点式运行级别 (Intermittent Train Control)

LEU: 轨旁电子单元 (Lineside Electronic Unit)

MSS: 维护支持系统 (Maintenance Support System)

MTBF: 平均故障间隔时间 (Mean Time Between Failures)

MTTR: 平均修复时间 (Mean Time To Repair)

PIS:乘客信息系统(Passenger Information System)

PSD: 站台门 (Platform Screen Door)

RAMS: 可靠性、可用性、可维修性和安全性（Reliability, Availability, Maintainability and Safety）

SIL: 安全完整性等级 (Safety Integrity Level)

TMS: 列车管理系统 (Train Management System)

TSR: 临时限速 (Temporary Speed Restriction)

UPS:不间断电源(Uninterruptible Power System)

V0BC: 车载控制器 (Vehicle On-Board Controller)

WCS: 无线通信系统 (Wireless Communication System)

ZC: 区域控制器 (Zone Controller)

## 4 互联互通产品测试生命周期划分及验证活动

### 4.1 测试阶段生命周期划分及验证活动

## a）互联互通产品供应商测试及验证阶段。

本阶段的测试与验证任务由各互联互通产品供应商进行。各互联互通产品供应商需要按照互联互通技术规范的要求，对各子系统产品进行设计与实现，并对互联互通总体要求和功能分配中要求的互联互通功能进行测试与验证。

## b）互联互通系统集成实验室测试及验证阶段。

本阶段的测试与验证任务由互联互通系统集成第三方验证机构进

---

行。各互联互通系统集成供应商依据实验室测试环境要求提供被测系统，在专用的测试与验证平台进行测试与验证；对互联互通系统进行功能测试。实验室互联互通测试将按照子系统进行，互联互通点式功能测试将由VOBC、CI、ATS、应答器子系统4个部分构成。

## c）互联互通系统集成试验线测试及验证阶段。

本阶段的测试与验证任务由互联互通系统第三方验证机构进行。各互联互通系统供应商依据试验线测试环境要求提供被测系统，在专用的试验线进行实车测试与验证；对于实验室验证与测试平台无法完全验证的功能进行测试与验证。试验线互联互通测试将按照子系统进行，互联互通点式功能测试将由V0BC、CI、ATS、应答器子系统4个部分构成。

### 4.2 测试阶段内容及依据

互联互通测试及验证技术规范依据系统规范和接口规范文件编写，主要对系统规范和接口规范中的互联互通功能、接口等进行测试和验证，本规范对系统性能的测试和验证不做要求。

## 5 测试环境

### 5.1 互联互通系统供应商测试及验证平台需求

互联互通系统供应商测试及验证平台由各厂商自己搭建，并对各自系统进行测试和验证，保证系统的设计和实现满足互联互通要求。

### 5.2 互联互通系统集成实验室测试及验证平台需求

#### 5.2.1 测试及验证平台设备构成

5.2.1.1 实验室验证与测试平台需要由存在互联互通连接的2条实验线路的若干车站构成，可以在2条线路上采用不同厂家的互联互通系统，并验证2条线路之间的地面设备之间以及车地之间的互联互通跨线运行功能，且列车在正常的运营模式下通过跨线接口线路并在正线完成正常的互联互通功能。

5.2.1.2 实验室验证平台测试环境的每条线路选取车站规模为2个控区5个车站，如图1所示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a944e917-5352-43e6-9749-c7acd55959c6/markdown_0/imgs/img_in_image_box_79_108_790_318.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A12%3A12Z%2F-1%2F%2F456d64c4a561cd715af75a602cf721a86421a428e0e23f98043bface8ff449d2" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 1 互联互通实验线路构成示意图</div>


#### 5.2.2 验证对象与信息流

实验室验证平台用于在实验室内验证跨线点式互联互通接口及功能。

a）验证对象包括

——互联互通系统车载V0BC设备；

——互联互通系统-联锁系统设备：

—— 互联互通系统-ATS 系统设备；

——互联互通系统-应答器系统设备(包括车载和轨旁设备)

b) 验证的内容包括：为轨道交

——T/CAMET 04010.1 中要求的功能；

——T/CAMET 04011.4 中规定的接口内容；

——T/CAMET 04011.5 中规定的接口内容；

——T/CAMET 04011.6 中规定的接口内容；

——T/CAMET 04011.3 中规定的内容；

——T/CAMET 04010.3 中规定的内容；

——T/CAMET 04011.2 中规定的(VOBC 与 CI 部分)内容；

——T/CAMET 04011.2 中规定的(VOBC 与 ATS 部分)内容。

#### 5.2.3 验证方法

在实验室验证平台搭建测试环境，通过仿真列车进行本线、跨线接口线路、其他互联互通线路上的点式运行测试，对互联互通功能进行验证。

---

### 5.3 互联互通试验线测试及验证平台需求

#### 5.3.1 试验线设备构成

试验线完成 CBTC 系统的互联互通测试。试验线设备至少包括：

——试验线路；

——试验列车；

——信号系统设备（ATP、ATO、ATS、联锁、DCS、应答器等）；

——信号系统无线通信网络及沿线接入点(LTE 或 Wi-Fi)。

#### 5.3.2 试验线条件要求

5.3.2.1 为了满足在试验线路完成互联互通功能的验证和测试，试验线路选取应具备以下条件：

——跨控区条件：

——站前/站后折返条件：

——设置区间信号机的长大区间（需要设置信号机的区间）。

5.3.2.2 试验线应设置至少3个控区，5个车站以及4个区间；车站对应设置有站台门相关设备等。此外，试验列车应兼容互联互通产品供应商信号系统接口。

#### 5.3.3 验证方法

在试验线上，每个控区安装不同供应商的地面设备，利用安装不同供应商的车载信号设备，列车完成互联互通系统接口及功能的测试和验证，如图2所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c382bcf8-a023-492a-8532-3661b43ebf35/markdown_0/imgs/img_in_image_box_82_807_791_892.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A12%3A16Z%2F-1%2F%2F8b73c8c5e9387e487d55fee1ddec4d298432aa21700f46b305e1acec820ed058" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 2 互联互通试验线示意图</div>


## 6 测试需求

### 6.1 互联互通系统测试验证活动的划分原则

#### 6.1.1 概述

6.1.1.1 对 CBTC 互联互通系统进行验证首先要根据功能分配进行测

10

---

试需求的划分，根据测试需求的可执行性，将测试需求划分为可测性需求和不可测需求。可测性需求可通过产品或系统测试的方式进行覆盖和验证，而不可测需求则需要针对具体的要求通过一定方式进行覆盖和验证。

6.1.1.2 对 CBTC 互联互通系统进行验证，根据测试验证的生命周期将其划分为 3 个阶段，分别为供应商测试与验证阶段、实验室平台测试与验证阶段，以及试验线测试与验证阶段。

#### 6.1.2 互联互通系统供应商测试及验证阶段

##### 6.1.2.1 互联互通产品供应商测试及验证阶段的工作内容

本阶段主要是对互联互通系统进行测试，主要工作是各供应商对自己的系统，按照互联互通标准的要求，进行与自己系统相关的全覆盖式测试。

##### 6.1.2.2 互联互通系统供应商测试及验证阶段的测试方法

6.1.2.2.1 对于不具备可测性的需求，包括系统结构描述、物理接口等需求，只在本阶段进行覆盖，可参考各产品的设计文件以及相应的实验报告。

6.1.2.2.2 对于可测试的需求，供应商依据互联互通系统需求编写对应的测试需求，采用功能测试的方法，对产品需求进行验证和覆盖。

#### 6.1.3 互联互通系统集成实验室平台测试及验证阶段

##### 6.1.3.1 互联互通系统集成实验室平台测试及验证阶段的工作内容

本阶段属于互联互通系统的集成测试的范围。主要工作为集成各供应商的被测设备，搭建专用的系统测试验证平台，对互联互通系统进行功能测试。系统测试验证平台为半实物的仿真测试平台，即部分设备为实物、部分设备为仿真。实验室测试验证平台测试阶段，对互联互通共线和跨线相关内容进行测试和验证，其中测试与验证的部分分为以下几个部分：

a）与功能相关的测试内容，在此阶段进行测试，如点式功能、CBTC 功能等；

b) 与数据相关的测试内容，在此阶段进行测试，如遍历站台门数据、精确停车数据、列车折返数据等；

c）与接口相关的测试内容，在此阶段进行测试，如与CI-CI接口、ZC-ZC接口、ATS-ATS接口、V0BC-ZC接口等。

---

##### 6.1.3.2 互联互通系统集成实验室平台验证与测试阶段的工作方法

本阶段主要测试目的是对可测性需求进行功能验证，采用黑盒测试的方法进行测试。

#### 6.1.4 互联互通试验线测试及验证阶段

##### 6.1.4.1 互联互通试验线测试及验证的工作内容

本阶段与实验室验证平台同属系统集成测试的范围。在试验线集成各系统供应商的被测设备，车辆在真实的线路上运行，所有互联互通设备均采用实物设备来进行测试和验证。实验室验证平台测试由于部分为仿真环境，诸如列车动力学模型、车辆、线路等等，对系统功能的验证，不能做到完全真实和充分，所以在试验线测试与验证阶段，结合运营方面的要求，测试和验证的内容分为以下几个部分：

a）与设备安装相关的测试内容，在此阶段进行测试，如应答器定位、轮径校正等；

b) 与车辆接口相关功能测试，在该阶段进行，如列车牵引、制动接口等；

c) 与线路相关的列车运行相关功能的测试内容，如车辆运行曲线、列车停车位置等；

d）与继电接口相关的功能，如联锁控制道岔、信号机等功能；

e）与网络环境相关的功能，如网路的稳定性等；

f) 与运营相关的功能，如按照运行计划跑图功能等。

##### 6.1.4.2 互联互通试验线验证与测试的工作方法

完成了产品设计与实现的测试、室内验证平台测试、试验线测试后，可对CBTC互联互通系统进行全覆盖的测试和验证。根据系统测试验证活动的划分原则，对后续章节中的测试需求进行验证和测试的阶段划分。

### 6.2 互联互通总体功能及接口功能分配

#### 6.2.1 互联互通系统架构和功能分配技术要求中功能分配

对总体要求定义的所有功能点（共73条）进行识别，按照T/CAMET04010.1功能分配的定义将其分配到各相关子系统，并根据其功能属性确定测试验证的阶段，详见表1。

---

<div style="text-align: center;">表 1 功能分配表(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">1</td><td rowspan="3">初始化CBTC列车位置</td><td style='text-align: center;'>进入CBTC区域的CBTC列车位置初始化CBTC列车位置初始化，并自动检测每列符合装备CBTC设备的列车，进入CBTC区域无需手动输入列车位置或列车长度的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>从设备故障中恢复的CBTC列车完成位置初始化CBTC列车位置初始化，并应自动检测每列装备CBTC设备的列车，从CBTC设备故障中恢复的列车无需手动输入列车位置或列车长度的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车升级至CBTC级别，当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，应满足如下转换条件：1) ATP车载设备无故障，且完成列车定位；2) ATP车载设备收到ATP轨旁设备发送的有效MA信息</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>确定CBTC列车位置</td><td style='text-align: center;'>确定列车长度CBTC应能确定列车长度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="5">2</td><td rowspan="5">确定CBTC列车位置</td><td style='text-align: center;'>确定CBTC列车位置CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>位置误差校正CBTC列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车完整性检测CBTC系统应能实现列车的完整性检测车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车轮径校正CBTC系统应能实现列车轮径校正功能，系统宜在列车进入转换轨前设置轮径自动补偿设备，并在出段/场前完成自动轮径补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>确定列车停站位置CBTC系统应根据不同的列车长度，确定列车的停站位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>确定CBTC列车位置</td><td style='text-align: center;'>退行防护、ATP车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">3</td><td rowspan="2">确定轨道区段占用状态</td><td style='text-align: center;'>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态[有一辆或多辆车占用区段，包括CBTC列车和（或）装有无效的CBTC车载设备的列车]</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>前方轨道区段占用状态。当CBTC列车前方区段被故障列车或者非CBTC装备列车占用时，CBTC系统应根据前方区段占用状态确定CBTC列车的安全边界</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>防护列车丢失位置报告</td><td style='text-align: center;'>防护列车丢失位置报告。当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">5</td><td rowspan="2">防护列车完整性丢失</td><td style='text-align: center;'>列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车完整性丢失防护。在检测到列车完整性丢失时，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>确定前方CBTC列车位置</td><td style='text-align: center;'>CBTC列车前方位置。对于每辆CBTC列车，应确定列车前方的CBTC列车位置</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>确定前方安全进路限制</td><td style='text-align: center;'>前方安全进路限制。对于每辆CBTC列车，系统应确定列车的安全进路位置</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>确定移动授权</td><td style='text-align: center;'>列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">8</td><td rowspan="2">确定移动授权</td><td style='text-align: center;'>列车升级至CBTC级别 当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，应满足如下转换条件：1) ATP车载设备无故障，且完成列车定位；2) ATP车载设备收到ATP轨旁设备发放的有效MA信息</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>移动授权的确定 为列车进行合适的移动防护限制，CBTC系统应估算最大移动授权限制位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>确定目标点</td><td style='text-align: center;'>确定目标点 为了确保列车不超过移动授权，CBTC系统应确定一个目标点</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>响应站台紧急关闭按钮</td><td style='text-align: center;'>响应站台紧急关闭按钮的按下当ATP轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>道岔状态防护</td><td style='text-align: center;'>道岔状态防护 CBTC系统应控制区域内道岔状态进行防护：当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>车载故障处理</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">13</td><td rowspan="2">固定速度限制防护</td><td style='text-align: center;'>固定线路速度限制 CBTC应提供固定线路限速的限制防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车构造速度限制 系统应提供列车构造速度的防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>临时限速限制防护</td><td style='text-align: center;'>临时限制速度限制。CBTC应按照系统设置的临时限速，为列车计算移动授权，对临时限速进行防护</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="3">15</td><td rowspan="3">确定制动曲线</td><td style='text-align: center;'>目标点的制动曲线</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>考虑最不利情况下的影响。CBTC的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>防止制动曲线超过速度限制。CBTC应保证制动曲线在超过固定或临时限速之前减速</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>列车超速防护</td><td style='text-align: center;'>确定授权速度。CBTC应基于ATP曲线，确定列车当前位置的限制速度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">16</td><td rowspan="3">列车超速防护</td><td style='text-align: center;'>ATP曲线。CBTC应为每辆列车计算完整的ATP曲线</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>速度监督和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>移动授权更新时的速度防护。移动授权更新时，如果列车的实际运行速度超过移动授权更新后的紧急制动触发速度，系统应实施紧急制动</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>列车速度测定</td><td style='text-align: center;'>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>测速误差补偿</td><td style='text-align: center;'>测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>零速状态确定</td><td style='text-align: center;'>零速状态确定。CBTC应确定零速度状态</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>列车运行方向确定</td><td style='text-align: center;'>确定CBTC列车运行方向。CBTC系统应确定每辆CBTC列车的实际运行方向</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>列车运行方向防护</td><td style='text-align: center;'>监督/防护运行方向 如果列车实际运行方向与授权的列车运行方向不一致，CBTC应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>退行防护</td><td style='text-align: center;'>退行防护 ATP车载设备应具有退行防护功能，以满足列车定位的需求 当退行距离和退行速度超过允许值时，系统应立即采取紧急制动 在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>越过移动授权终点防护</td><td style='text-align: center;'>越过移动授权终点的响应 列车越过移动授权终点时，系统应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>移动授权 更新超时防护</td><td style='text-align: center;'>移动授权更新超时的防护 如果移动授权更新超时，系统应实施紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>紧急制动缓解</td><td style='text-align: center;'>紧急制动缓解 在保证安全的条件下，系统可以缓解已施加的紧急制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>车门允许</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内2)开门侧与站台一致。3)列车零速4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自评自关、自开人关、人开关三种方式，自动或人工打开车门。在AM驾驶模式下，可提供三种开门方式：CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门分开，司机可在车载设备防护条件下前进或后退，直至停车时止</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>站台门控制</td><td style='text-align: center;'>站台门控制：CBTC在打开站台门之前，应检查是否满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内2)站台门侧与车门侧一致3)列车零速4)保持制动已施加</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">28</td><td rowspan="2">车门防护</td><td style='text-align: center;'>车门防护，仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>车门状态丢失防护：列车在运行过程中，车载设备应实时监控列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">29</td><td rowspan="2">车门防护切除</td><td style='text-align: center;'>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>车门操作切除。车辆可以提供单个车门切除功能，切除后的车门不响应列车开门命令</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">30</td><td rowspan="2">站台门防护</td><td style='text-align: center;'>站台门锁闭状态防护 仅在站台门处于“关闭且锁闭”状态时，系统方允许列车移动CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；已进站未停稳以及正在出站的列车应立即紧急制动；已完全出站的列车不受影响</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>站台门状态丢失的响应。当列车靠近车站或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>列车折返</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>车载ATP界面功能</td><td style='text-align: center;'>CBTC车载ATP显示数据。CBTC车载显示屏靠显示ATP数据应包括：1)列车运行模式；2)CBTC运行状态；3)当前列车速度；4)当前最大允许CBTC速度；5)超速报警</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>车载 ATP 界面功能</td><td style='text-align: center;'>CBTC 车载 ATP 输入数据：用户 ATP 信息输入到 CBTC 应包括：1) 运行模式选择；2) 超速报警情况确认</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>ATP 自诊断、故障报警及数据记录</td><td style='text-align: center;'>自诊断、故障报警及数据记录。ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存 7 d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>模式转换</td><td style='text-align: center;'>列车驾驶模式。列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）、列车自动防护模式（CM）为列车正常运行模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>模式转换</td><td style='text-align: center;'>驾驶模式转换：列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>ZC间移交</td><td style='text-align: center;'>ZC切换。两条连续式列车控制级别线路间应设置移交边界和移交重叠区。列车进入移交重叠区后，车载ATP设备应同时与移交、接管线路的轨旁ATP设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁ATP设备发送的MA；移交接管线路的轨旁ATP设备间应互传线路状态、列车位置等信息，并向车载ATP设备发送MA信息</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>电子地图存储</td><td style='text-align: center;'>电子地图存储。CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>停稳停准判断</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内。2)开门侧与站台一致。3)列车零速。4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式。CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>确定ATO曲线</td><td style='text-align: center;'>确定ATO曲线。CBTC系统应为列车确定ATO曲线。ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制。ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>精确停车</td><td style='text-align: center;'>列车进站精确停车。ATO子系统应具备列车进站精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>根据ATO曲线调整列车速度</td><td style='text-align: center;'>列车调速。CBTC系统应根据ATO曲线调整列车速度</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>ATO能够响应ATS系统设置的跳停命令</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>运营调整</td><td style='text-align: center;'>在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="4">43</td><td rowspan="4">开关车门</td><td style='text-align: center;'>开列车门。在AM驾驶模式和ATP的防护下，可提供自动开门或者人工开门两种开门方式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>开站台门。CBTC系统应能自动开启站台门</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>关闭列车门。在AM驾驶模式下，可提供自动关门或者人工关门两种关门方式</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>关闭站台门。CBTC系统应能自动关闭站台门</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>ATO界面显示</td><td style='text-align: center;'>CBTC车载ATO显示数据 在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>ATO自诊断、故障报警及数据记录</td><td style='text-align: center;'>自诊断、故障报警及数据记录：ATO子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心ATS</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>ATO发送列车运行信息</td><td style='text-align: center;'>ATO子系统向ATS子系统发送列车运行信息，以便ATS子系统能对在线列车进行监控</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>ATO发送旅客信息</td><td style='text-align: center;'>车载旅客信息数据。ATO车载设备应向TMS提供有关车载旅客信息的数据</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">48</td><td rowspan="2">确定列车识别号</td><td style='text-align: center;'>CBTC的运行列车识别号。每一个运行在CBTC区域内的装备CBTC的列车都应该分配一个运行列车识别号。列车识别号应由列车号、车次号、车组号、目的地号组成</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车—地双向通信传输信息恢复</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>ATS列车追踪</td><td style='text-align: center;'>ATS列车追踪：ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他相关的信息并保持这些信息的能力。列车的前后位置应该根据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">50</td><td rowspan="3">列车进路办理</td><td style='text-align: center;'>列车进路办理——启动。ATS系统应该具有列车自动办理进路的功能。ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车进路办理——人工、ATS系统应该具有手动办理进路的功能</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车进路办理——冲突检查。当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="3">51</td><td rowspan="3">列车自动调整</td><td style='text-align: center;'>自动调度、ATS系统可包括自动调度功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>列车时刻表/发车(运行)间隔调整、ATS系统可具有监视与自动调整的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>冲突自动调整。在CBTC列车位置报告的基础上,ATS系统应包括基于列车位置报告的列车自动调整功能,来处理列车冲突,以把整个系统的延迟减少到最小</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>节能运行</td><td style='text-align: center;'>节能运行、ATS系统可具有通过实时控制及协调列车加速、列车滑行、列车制动来实施能源优化的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>扣车、ATS系统应具有在车站扣车能力</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>提前发车</td><td style='text-align: center;'>提前发车、ATS系统应具有设置站台提前发车的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>跳停车站、ATS系统应具有设置一个或多个装备CBTC的列车经过下一个或下几个车站而不停车的功能</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>设置/取消临时限速</td><td style='text-align: center;'>临时限速、ATS系统应具有在CBTC区域内任何轨道区段,设置(与取消)临时限速的能力</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>时刻表编制管理</td><td style='text-align: center;'>ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>模拟培训</td><td style='text-align: center;'>ATS应具备模拟演示及培训系统，实现对调度员的培训</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">59</td><td rowspan="3">ATS界面功能</td><td style='text-align: center;'>在AM模式下，ATO子系统可根据ATS的调整指令控制区间走行时分，达到列车运行自动调整的目的</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>ATS列车追踪ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，及其他相关的信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>ATS显示数据：CBTC的ATS显示应能够表示以下信息：1)精确的和区域相关的信息；2)列车状态相关信息；</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td rowspan="2">59</td><td rowspan="2">ATS界面功能</td><td style='text-align: center;'>3)列车移动授权/进路信息；4)和被控列车运行相关的信息如防护区段信息，领闭的进路/区段，以及临时限速极限和限速值；5)其他</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>CBTC输入数据。CBTC的ATS用户界面显示应能够接收以下ATS用户输入：1)办理和取消进路输入；2)建立和取消防护区段，锁闭进路/区段，以及临时限速输入；3)其他</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">60</td><td rowspan="2">ATS数据记录</td><td style='text-align: center;'>发送报警数据。ATS子系统可将自身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>数据记录及回放。系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能。综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30d</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>中控/站控转换</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="4">62</td><td rowspan="4">进路办理</td><td style='text-align: center;'>列车进路办理——自动、ATS系统应该具有列车自动办理进路的功能。ATS系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车进路办理——人工、ATS系统应该具有手动办理进路的功能</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车进路办理——冲突检查。当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>进路办理 联锁应具备进路办理功能，包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>进路办理</td><td style='text-align: center;'>装有无效CBTC装备的列车进路办理。对于设备故障的CBTC列车或无装备的列车，在前方进路出清并重新开放后，装有无效CBTC装备的列车方可驶入</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>保护区段建立</td><td style='text-align: center;'>保护区段。联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>进路/区段锁闭</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>65</td><td style='text-align: center;'>道岔单操、单锁</td><td style='text-align: center;'>道岔单操、单锁。联锁具备道岔单独操纵及锁闭的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>66</td><td style='text-align: center;'>车站/区间封锁</td><td style='text-align: center;'>封锁。系统应具有车站封锁、区间封锁的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>67</td><td style='text-align: center;'>站台紧急关闭按钮</td><td style='text-align: center;'>响应站台紧急关闭按钮的按下当ATP轨旁设备接收到站台紧急关闭按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>67</td><td style='text-align: center;'>站台紧急关闭按钮</td><td style='text-align: center;'>站台紧急关闭按钮 联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td rowspan="2">68</td><td rowspan="2">CI自检、故障报警及数据记录</td><td style='text-align: center;'>故障监测 CI子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>监视和记录工作状态 CI子系统能监视和记录自身的工作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯经状态监测及断丝报警，转辙机动作状态</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>69</td><td style='text-align: center;'>进路解锁及取消</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力。CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>70</td><td style='text-align: center;'>计轴故障恢复</td><td style='text-align: center;'>计轴故障恢复 系统应具有计轴故障恢复的能力</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 1 功能分配表(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>功能点</td><td style='text-align: center;'>子功能点描述</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>71</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>扣车。ATS系统应具有在车站扣车的能力</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>72</td><td style='text-align: center;'>站控/遥控</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>重复测试点</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>73</td><td style='text-align: center;'>CI权限设置</td><td style='text-align: center;'>操作权限设置。CI子系统能设置不同操作人员的权限，并有相应的安全操作手段</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td></tr><tr><td colspan="8">注1：表中的“重复测试点”表示该测试点在其他相应的功能点中已做要求。注2：表中“功能点描述”依据系统规范第2部分系统架构和功能分配技术要求。注3：“-”表示不适用。注4：“✓”表示适用。注5：“点式”表示在点式级别下测试。注6：“连续式”表示在连续式级别下测试。注7：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试。注8：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试。注9：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试。</td></tr></table>

---

#### 6.2.2 互联互通应答器报文说明中功能分配

对 T/CAMET 04011.1 中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 2。

<div style="text-align: center;">表 2 互联互通应答器报文规范表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>4.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>4.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>4.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>4.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>4.1.5</td><td style='text-align: center;'>CHINA ASSOCIATION OF METROSPORTS</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>4.1.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>4.1.7</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>4.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>4.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>4.2.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>4.3.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>轨道交通</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>4.3.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>4.3.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>4.3.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>4.3.1.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>4.3.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>4.3.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>4.3.2.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>4.3.2.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>4.3.2.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 2 互联互通应答器报文规范表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>4.3.2.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>4.3.2.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>4.4.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“—”表示不适用；注2：“✓”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8：表格中的章节号为T/CAMET 04011.1中章节号。</td></tr></table>

#### 6.2.3 互联互通 CI-CI 接口说明中功能分配

对 T/CAMET 04011.5 中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 3。

<div style="text-align: center;">表 3 互联互通计算机联锁(CI)间接口规范识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.3.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.4.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.4.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.4.3</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td></tr></table>

---

<div style="text-align: center;">表 3 互联互通计算机联锁（CI）间接口规范识别表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.4.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.4.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.4.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.4.7</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.4.8</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.4.9</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.4.10</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.4.11</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.4.12</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1:“—”表示不适用；注2:“✓”表示适用；注3:“点式”表示在点式模式下测试；注4:“连续式”表示在连续式模式下测试；注5:“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6:“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7:“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8:表格中的章节号为T/CAMET 04011.5中章节号。</td></tr></table>

#### 6.2.4 互联互通跨线 ATS-ATS 接口说明中功能分配

对 T/CAMET 04011.6 中的需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 4。

<div style="text-align: center;">表 4 互联互通 ATS 间接口规范识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>√</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.2.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>√</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通 ATS 间接口规范识别表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.2.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.2.3.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.2.3.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.2.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.3.2</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.3.3</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.3.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.3.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.3.3.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.3.3.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.3.3.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.3.3.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.3.3.7</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>6.3.3.8</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“-”表示不适用；注2：“✓”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8：表格中的章节号为T/CAMET 04011.6中章节号。</td></tr></table>

---

#### 6.2.5 互联互通 VOBC-ATS 接口说明中功能分配

对 T/CAMET 04011.2 中的 VOBC 与 ATS 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 5。

<div style="text-align: center;">表 5 车地通信协议需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>6.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>6.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>6.1.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>6.1.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>6.1.3.3</td><td style='text-align: center;'>ASSOCIATION OF METRO</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>6.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>6.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>6.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>6.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>6.3.2.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>6.3.2.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>6.3.2.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>6.3.2.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>6.3.2.2.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>6.3.2.2.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>6.3.2.2.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>6.3.2.2.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>6.3.2.2.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>6.3.2.2.6</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>6.3.3.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr></table>

---

<div style="text-align: center;">表 5 车地通信协议需求识别表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>6.3.3.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td></tr><tr><td colspan="7">注1：“—”表示不适用；注2：“✓”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8：表格中的章节号为T/CAMET 04011.2中章节号。</td></tr></table>

#### 6.2.6 互联互通 VOBC-CI 接口说明中功能分配

对 T/CAMET 04011.2 中的 VOBC 与 CI 接口规范部分需求进行识别，并根据其需求属性确定测试验证的阶段，详见表 6。

<div style="text-align: center;">表 6 车地通信协议需求识别表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>7.1.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>7.1.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>7.1.3.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>7.1.3.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>7.1.3.3</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>7.1.4</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>7.2.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>7.2.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>7.3.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>7.3.2.1.1</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>7.3.2.1.2</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>7.3.2.1.3</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>√</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 6 车地通信协议需求识别表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>章节号</td><td style='text-align: center;'>点式</td><td style='text-align: center;'>连续式</td><td style='text-align: center;'>设计与实现</td><td style='text-align: center;'>室内平台</td><td style='text-align: center;'>试验线</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>7.3.2.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>7.3.2.1.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>7.3.3.1.1</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>7.3.3.1.2</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>7.3.3.1.3</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>7.3.3.1.4</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>7.3.3.1.5</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>✓</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td></tr><tr><td colspan="7">注1：“—”表示不适用；注2：“✓”表示适用；注3：“点式”表示在点式模式下测试；注4：“连续式”表示在连续式模式下测试；注5：“设计与实现”表示在互联互通第一阶段测试，由各厂家独立测试；注6：“室内平台”表示在互联互通第二阶段测试，由各厂家提供互联互通产品在互联互通实验室平台测试；注7：“试验线”表示在互联互通第三阶段测试，由各厂家提供互联互通产品在互联互通试验线测试；注8：表格中的章节号为T/CAMET 04011.2中章节号。</td></tr></table>

### 6.3 互联互通测试需求

#### 6.3.1 定义测试需求的原则

定义测试需求应遵循以下原则。

## a） 司理解性

每一个测试需求应以易于理解的文字进行描述。对认证机构、用户、开发人员、测试人员而言，每一个测试需求都必须易于理解。在测试需求描述中，一些专业词汇要与文中术语、定义和缩略语中描述的内容一致，便于理解。

## b) 明确性

每一个测试需求必须具有唯一的编号。

## c）等级适用性

必须标明每一个测试需求适用于的 CBTC 等级。因为每一个测试需求不一定适用于所有的运行等级。

---

## d）可追溯性

所有测试需求应明确的指向某一个或多个功能点或接口需求。

#### 6.3.2 测试需求编号命名原则

为满足测试需求定义的各种原则，测试需求的命名应遵循以下原则。

## a）包含功能点或接口编号

为便于追溯和理解，测试需求编号中需要包含功能点或接口编号。对于T/CAMET04010.1、T/CAMET04010.2因描述的是功能点，测试需求编号中体现功能点的编号，如“CBTC-F-ATP-1-ITC-1”。对于描述系统间接口的接口规范，如T/CAMET04011.1、T/CAMET04011.4等，测试需求编号中体现设备间接口，如“CBTC-IF-BALISE-MSG-ITC-1”或“CBTC-IF-CI/CI-MSG-ITC-1”。

## b）包含运行等级

为满足测试需求等级适用性的要求，测试需求编号中需要包含运行等级。点式部分以“ITC”进行描述。CBTC部分以“CTC”进行描述。

## c）包含唯一标识的序号

为满足测试需求唯一性的要求，对每个功能点中的测试需求进行编号，从1开始，相同运行等级的，顺序号不可以重复（如删除后的编号将不再使用）。

### 6.4 互联互通系统测试需求

#### 6.4.1 概述

6.2 条中描述了 T/CAMET 04010.2 中所有的互联互通相关的功能点，并对其进行了点式和连续式的划分。下面对点式部分的功能点进行测试和验证方法进行描述。

#### 6.4.2 初始化 CBTC 列车位置

初始化 CBTC 列车位置功能的测试和验证方法详见表 7 和表 8。

<div style="text-align: center;">表 7 初始化 CBTC 列车位置(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-1-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>进入 CBTC 区域的 CBTC 列车位置初始化。CBTC 列车位置初始化，并自动检测每列符合装备 CBTC 设备的列车，进入 CBTC 区域无需手动输入列车位置或列车长度的数据</td></tr></table>

---

<div style="text-align: center;">表 7 初始化 CBTC 列车位置(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于 RM 无位置报告模式的列车从非 CBTC 区域进入 CBTC 区域，经过具备定位条件两个连续应答器，系统自动获得列车位置和运行方向</td></tr><tr><td colspan="2">注：表中功能内容是功能分配的原文描述（下同）。</td></tr></table>

<div style="text-align: center;">表 8 初始化 CBTC 列车位置(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>初始化 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-FATATC0A</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>从设备故障中恢复的 CBTC 列车完成位置初始化。CBTC 列车位置初始化，并应自动检测每列装备 CBTC 设备的列车从 CBTC 设备故障中恢复的列车无需手动输入列车位置或列车长度的数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于点式控制级别的列车，ATP 故障，列车丢失定位，降级为 RM 模式；2) ATP 故障恢复后，经过装备定位条件的两个连续应答器，系统自动获得列车位置和运行方向</td></tr></table>

#### 6.4.3 确定 CBTC 列车位置

确定 CBTC 列车位置功能的测试和验证方法详见表 9～表 19。

<div style="text-align: center;">表 9 确定 CBTC 列车位置(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定列车长度。CBTC 应能确定列车长度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>与 ATS 建立连接的 RM 列车，向 ATS 报告列车长度</td></tr></table>

---

<div style="text-align: center;">表 10 确定 CBTC 列车位置(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定列车长度。CBTC 应能确定列车长度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>与 ATS 建立连接的点式控制级别的列车，向 ATS 报告列车长度</td></tr></table>

<div style="text-align: center;">表 11 确定 CBTC 列车位置(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定 CBTC 列车位置。CBTC 列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>通过列车位置检测设备完成点式或 RM 列车的列车位置的安全和精确定位（包括列车的正反向运行）</td></tr></table>

<div style="text-align: center;">表 12 确定 CBTC 列车位置(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>位置误差校正。CBTC 列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 系统、处于 RM 控制级别的车载 ATP 设备，在向 ATS 汇报列车位置的同时，也汇报车载 ATP 系统考虑到安全因素而计算的位置不确定性（包括列车的正反向运行）</td></tr></table>

<div style="text-align: center;">表 13 确定 CBTC 列车位置(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-5</td></tr></table>

---

<div style="text-align: center;">表 13 确定 CBTC 列车位置(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>位置误差校正。CBTC 列车位置的确定应考虑测距误差的影响，并对位置误差考虑合适的余量</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 车载 ATP 判断接收到的应答器报文有效的条件之一是应答器的位置在合理的范围之内；2) 处于点式控制级别的车载 ATP 设备，在向 ATS 汇报列车位置的同时，也汇报车载 ATP 系统考虑到安全因素而计算的位置不确定性</td></tr></table>

<div style="text-align: center;">表 14 确定 CBTC 列车位置(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车完整性检测。CBTC 系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)处于 RM 控制级别的车载 ATP 设备，检测到本车的完整性丢失，列车实施紧急制动，并丢失定位；2)列车位置丢失后，联锁和 ATS 按照物理区段占用进行显示。</td></tr></table>

<div style="text-align: center;">表 15 确定 CBTC 列车位置(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定CBTC列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车完整性检测。CBTC系统应能实现列车的完整性检测。当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行</td></tr></table>

---

<div style="text-align: center;">表 15 确定 CBTC 列车位置(七)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定CBTC列车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)处于点式控制级别的车载ATP设备，检测到本车的完整性丢失，列车实施紧急制动，并丢失定位，降级为RM无定位模式；2)列车位置丢失后，联锁和ATS按照物理区段占用进行显示</td></tr></table>

<div style="text-align: center;">表 16 确定 CBTC 列车位置(八)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车轮径校正 CBTC 系统应能实现列车轮径校正功能， 系统宜在列车进入转换轨前设置轮径自动补偿设备，并在 出段/场前完成自动轮径补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式或 RM 列车执行从场段进入转换轨操作，列车将完 成轮径的自动补偿（若具备该功能）</td></tr></table>

<div style="text-align: center;">表 17 确定 CBTC 列车位置(儿)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定CBTC列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定列车停站位置.CBTC系统应根据不同的列车长度， 确定列车的停站位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于点式控制等级的列车，在停站时，根据本身的编组和列车长度，以及电子地图中存储的针对不 同的停车点位置，进行停车（包括正反向进站）</td></tr></table>

<div style="text-align: center;">表 18 确定 CBTC 列车位置(十)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-10</td></tr></table>

---

<div style="text-align: center;">表 18 确定 CBTC 列车位置(十)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>退行防护、ATP 车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于 RM 控制级别，有位置报告的列车，当退行速度超过允许值时，列车紧急制动；2) 装备 CBTC 设备、处于 RM 控制级别，有位置报告的列车，当退行距离超过允许值时，列车紧急制动</td></tr></table>

<div style="text-align: center;">表 19 确定 CBTC 列车位置(十一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 CBTC 列车位置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-2-ITC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>退行防护。ATP 车载设备应具有退行防护功能，以满足列车定位的需求。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对退行运行的列车提供安全间隔防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于点式控制级别的列车，当退行速度超过允许值时，列车紧急制动；2) 装备 CBTC 设备、处于点式控制级别的列车，当退行距离超过允许值时，列车紧急制动</td></tr></table>

#### 6.4.4 确定轨道区段占用状态

确定轨道区段占用状态功能的测试和验证方法详见表20和表21。

<div style="text-align: center;">表 20 确定轨道区段占用状态(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>轨道区段的占用状态。CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和/或装有无效的CBTC车载设备的列车）</td></tr></table>

---

<div style="text-align: center;">表 20 确定轨道区段占用状态(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、无位置报告、处于 RM 控制级别的列车占用某轨道区段；2) 轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给 ATS 设备进行显示</td></tr></table>

<div style="text-align: center;">表 21 确定轨道区段占用状态(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定轨道区段占用状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-3-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>轨道区段的占用状态：CBTC系统可根据轨旁次级占用检测设备提供的信息，结合CBTC列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括CBTC列车和/或装有无效的CBTC车载设备的列车）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于点式控制级别的列车占用某轨道区段；2) 轨旁次级占用检测设备检测到该轨道区段的占用信息，发送给联锁，联锁将该信息发送给ATS设备进行显示</td></tr></table>

#### 6.4.5 确定目标点

确定目标点功能的测试和验证方法详见表22。

<div style="text-align: center;">表 22 确定目标点</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定目标点</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-9-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定目标点。为了确保列车不超过移动授权，CBTC系统 应确定一个目标点</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制级别的列车不能越过点式 移动授权中的进路的终点</td></tr></table>

---

#### 6.4.6 道岔状态防护

道岔状态防护功能的测试和验证方法详见表23。

<div style="text-align: center;">表 23 道岔状态防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔状态防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-11-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>道岔状态防护。CBTC系统应控制区域内道岔状态进行防护。当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔区域时，列车应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于点式控制级别的列车，前方进路包含道岔且信号开放，点式移动授权延伸至进路内方；2) 设置道岔状态丢失，验证始端信号机关闭；3) 如果点式列车通过预告应答器接收到信号关闭信息，列车依据授权在信号机前正常停车；否则列车越过已关闭的信号机后紧急制动停车</td></tr></table>

#### 6.4.7 车载故障处理

车载故障处理功能的测试和验证方法详见表24～表27。

<div style="text-align: center;">表 24 车载故障处理（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理、列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于 RM 控制级别、有位置报告的列车，检测到本车的非预期移动、ATP 设备会立即施加紧急制动，并给出报警提示</td></tr></table>

---

<div style="text-align: center;">表 25 车载故障处理(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制级别的列车，检测到本车的非预期移动，ATP设备会立即施加紧急制动，并给出报警提示</td></tr></table>

<div style="text-align: center;">表 26 车载故障处理（三）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-12-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理、列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于 RM 控制级别、有位置报告的列车，检测到车载设备故障，立即施加紧急制动，并给出报警提示</td></tr></table>

<div style="text-align: center;">表 27 车载故障处理（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-I2-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障管理。列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制级别的列车，检测到车载设备故障，立即施加紧急制动，并给出报警提示</td></tr></table>

#### 6.4.8 固定速度限制防护

固定速度限制防护功能的测试和验证方法详见表28和表29。

---

<div style="text-align: center;">表 28 固定速度限制防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>固定速度限制防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-13-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>固定线路速度限制。CBTC 应提供固定线路限速的限制防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制级别的列车，在运行时，利用自己电子地图中存储的线路限速，计算速度曲线，对线路上的固定限速进行防护</td></tr></table>

<div style="text-align: center;">表 29 固定速度限制防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>固定速度限制防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-13-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车构造速度限制。系统应提供列车构造速度的防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于点式控制级别的列车，在运行时，计算的可运行的最高速度不大于列车自身的构造速度，验证列车计算的速度曲线中最高速度不超过列车的构造速度</td></tr></table>

#### 6.4.9 确定制动曲线

确定制动曲线功能的测试和验证方法详见表30～表32。

<div style="text-align: center;">表 30 确定制动曲线(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-15-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>目标点的制动曲线</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，经过主应答器或者预告应答器时，获得前方信号机的状态，计算目标点的制动曲线</td></tr></table>

---

<div style="text-align: center;">表 31 确定制动曲线(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-15-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>考虑最不利情况下的影响。CBTC 的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制等级的列车，在计算速度曲线时，要考虑最差情况下系统偏差、反应次数和反应时间的补偿</td></tr></table>

<div style="text-align: center;">表 32 确定制动曲线(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-15-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>防止制动曲线超过速度限制.CBTC应保证制动曲线在超过固定或临时限速之前减速</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备,处于点式控制等级运行的列车,在经过固定限速区段,如道岔区段时,提前减速</td></tr></table>

#### 6.4.10 列车超速防护

列车超速防护功能的测试和验证方法详见表33～表36。

<div style="text-align: center;">表 33 列车超速防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定授权速度。CBTC 应基于 ATP 曲线，确定列车当前位置的限制速度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制等级运行的列车，根据点式移动授权和线路速度计算 ATP 曲线，并基于 ATP 曲线，确定列车当前位置的限制速度</td></tr></table>

---

<div style="text-align: center;">表 34 列车超速防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATP 曲线。CBTC 应为每辆列车计算完整的 ATP 曲线</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制等级运行的列车，根据点式移动授权和线路计算 ATP 曲线，并基于 ATP 曲线，确定列车当前位置的限制速度</td></tr></table>

<div style="text-align: center;">表 35 列车超速防护(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>速度监督和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级运行的列车，当列车实际运行速度超过限制速度时，实施紧急制动</td></tr></table>

<div style="text-align: center;">表 36 列车超速防护(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车超速防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-16-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>速度监督和防护。如果列车实际速度超过限制速度，CBTC应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级运行的列车，当列车实际运行速度超过RM限制速度时，实施紧急制动</td></tr></table>

#### 6.4.11 列车速度测定

列车速度测定功能的测试和验证方法详见表37和表38。

---

<div style="text-align: center;">表 37 列车速度测定(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车速度测定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-17-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车，利用测速测距功能测量并计算列车的实际速度，检查速度满足分辨率和精度的要求</td></tr></table>

<div style="text-align: center;">表 38 列车速度测定(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车速度测定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-17-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车实际速度。CBTC应确定每辆CBTC装备列车的实际速度，速度满足分辨率和精度的要求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，利用测速测距功能测量并计算列车的实际速度，检查速度满足分辨率和精度的要求</td></tr></table>

#### 6.4.12 测速误差补偿

测速误差补偿功能的测试和验证方法详见表39和表40。

<div style="text-align: center;">表 39 测速误差补偿(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>测速误差补偿</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-18-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>测速误差补偿。CBTC系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车，在空转打滑时，应能够补偿测速误差产生的影响，并对测速作出合适的补偿</td></tr></table>

---

<div style="text-align: center;">表 40 测速误差补偿(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>测速误差补偿</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-18-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>测速误差补偿。CBTC系统应能够补偿测速误差产生的 影 响，并对测速作出合适的补偿</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，在空转打滑 时，应能够补偿测速误差产生的影响，并对测速作出合适的 补偿</td></tr></table>

#### 6.4.13 零速状态确定

零速状态确定功能的测试和验证方法详见表41和表42。


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>零速状态确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-ATP-19-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>零速状态确定。CBTC 应确定零速度状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车，可以进行零速状态确认</td></tr></table>

<div style="text-align: center;">表 42 零速状态确定(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>零速状态确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-19-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>零速状态确定：CBTC应确定零速度状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级运行的列车，可以进行零速状态确认</td></tr></table>

#### 6.4.14 列车运行方向确定

列车运行方向确定功能的测试和验证方法详见表43和表44。

---

<div style="text-align: center;">表 43 列车运行方向确定(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行方向确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-20-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车运行方向。CBTC系统应确定每辆CBTC 列车的实际运行方向</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)装备CBTC设备、处于RM控制等级、有位置报告的列车，明确自己的运行方向； 2)此时列车与联锁和ATS建立连接，ATP会将运行方向发送给联锁和ATS设备</td></tr></table>

<div style="text-align: center;">表 44 列车运行方向确定(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行方向确定</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-20-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定CBTC列车运行方向 CBTC系统应确定每辆CBTC 列车的实际运行方向</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于点式控制等级的列车，明确自己的运行方向； 2) 此时列车与联锁和ATS建立连接，ATP会将运行方向发送给联锁和ATS设备</td></tr></table>

#### 6.4.15 越过移动授权终点防护

越过移动授权终点防护功能的测试和验证方法详见表45。

<div style="text-align: center;">表 45 越过移动授权终点防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>越过移动授权终点防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-23-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>越过移动授权终点的响应。列车越过移动授权终点时，系统应实施紧急制动</td></tr></table>

---

<div style="text-align: center;">表 45 越过移动授权终点防护(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>越过移动授权终点防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备 CBTC 设备、处于点式控制等级的列车，越过移动授权终点，系统实施紧急制动；2) 此时列车与 ATS 建立连接，ATP 会将紧急制动状态发送给 ATS 设备</td></tr></table>

#### 6.4.16 移动授权更新超时防护(若有)

移动授权更新超时防护(若有)功能的测试和验证方法详见表46。

<div style="text-align: center;">表 46 移动授权更新超时防护(若有)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>移动授权更新超时防护(若有)</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-24-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>移动授权更新超时的防护.移动授权更新超时,系统应实施紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)装备CBTC设备、处于点式控制等级的列车,越过主信号应答器,且正确接收到点式移动授权;2)列车完全越过信号机后停车,且停车时间超过点式移动授权的有效时间,列车将施加紧急制动并提示降级</td></tr></table>

#### 6.4.17 紧急制动缓解

紧急制动缓解功能的测试和验证方法详见表47和表48。

<div style="text-align: center;">表 47 紧急制动缓解（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>紧急制动缓解</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-25-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>紧急制动缓解。在保证安全的条件下，系统可以缓解已 施加的紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车， 因某种原因施加了紧急制动，如退行防护、设备故障等，在 施加EB的触发条件消失且司机或调度员确认安全的情况 下，可以缓解该紧急制动</td></tr></table>

---

<div style="text-align: center;">表 48 紧急制动缓解(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>紧急制动缓解</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-25-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>紧急制动缓解。在保证安全的条件下，系统可以缓解已 施加的紧急制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，因某种原因 施加了紧急制动，如退行防护、设备故障等，在施加EB的触 发条件消失且司机或调度员确认安全的情况下，可以缓解 该紧急制动</td></tr></table>

#### 6.4.18 车门允许

车门允许功能的测试和验证方法详见表49～表53。

<div style="text-align: center;">表 49 车门允许(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 49 车门允许（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 装备 CBTC 设备、处于点式控制等级的列车，满足以下条件后，车载 ATP 允许打开对应侧车门和站台门。1) 停准在指定的停车点；2) 开门侧与站台一致；3) 列车零速；4) 保持制动已施加。在 AM 驾驶模式下，测试自开自关、自开人关、人开人关三种开门方式。2. 针对反向进站进行相同的测试项</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1.列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2.开门侧与站台一致；3.列车零速；4.保持制动已施加列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 50 车门允许(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，满足以下条件后，车载ATP允许打开对应侧车门和站台门或双侧车门和站台门。1)停准在指定的停车点，且在停车窗内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加。在CM驾驶模式下，只能人工打开车门</td></tr></table>

<div style="text-align: center;">表 51 车门允许(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 在开车门之前，应满足下列条件：1) 列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2) 开门侧与站台一致；3) 列车零速；4) 保持制动已施加。列车在车站规定的位置停准停稳后，车载 ATP 应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在 AM 驾驶模式下，可提供三种开门方式，CM 驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 51 车门允许(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，在车站停车时，未到停车窗，司机可控制列车继续前进，到停车窗后停车，确保满足以下条件后，车载ATP允许打开对应侧车门和站台门或双侧车门和站台门。 1)开门侧与站台一致； 2)列车零速； 3)保持制动已施加</td></tr></table>

<div style="text-align: center;">表 52 车门允许(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 52 车门允许(四)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，在车站停车时，越过停车窗，司机可控制列车退行，在满足退行距离和退行速度的情况下，在停车窗停车，确保满足下列条件后，车载ATP允许打开对应侧车门和站台门或双侧车门和站台门。 1)开门侧与站台一致； 2)列车零速； 3)保持制动已施加</td></tr></table>

<div style="text-align: center;">表 53 车门允许(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-26-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC在开车门之前，应满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加。列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人开人关三种方式，自动或者人工打开车门。在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位</td></tr></table>

---

<div style="text-align: center;">表 53 车门允许(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门允许</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，在车站停车时，以下条件任一条不满足，车载ATP不给出开门允许（开门使能）。1)列车停准在指定的停车点，且在停车窗内；2)开门侧与站台一致；3)列车零速；4)保持制动已施加</td></tr></table>

#### 6.4.19 点式开口功能

点式开口功能的测试和验证方法详见表54

<div style="text-align: center;">表 54 点式开口功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式开口功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-75-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>点式模式下，列车应具备点式开口功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>列车TC-CM级别在信号前方停车，并可以通过开口确认操作，确认后驾驶列车</td></tr></table>

#### 6.4.20 点式红灯误出发防护功能

点式红灯误出发防护功能的测试和验证方法详见表55。

<div style="text-align: center;">表 55 点式红灯误出发防护功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式红灯误出发防护功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-76-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>点式模式下，列车应具备点式红灯误出发防护功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>列车ITC-CM级别在站台出站信号前方停车，若前方信号为禁止信号，系统将不给出开口确认提示</td></tr></table>

---

#### 6.4.21 站台门控制

站台门控制功能的测试和验证方法详见表56和表57。

<div style="text-align: center;">表 56 站台门控制(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门控制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-27-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门控制。CBTC应打开站台门之前，应检查是否满足下列条件：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，在下列条件满足时提供开门允许，并向联锁发送打开站台门的请求，打开站台门前，确认：1)列车停准在指定的停车点，且在停车窗内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加满足上述条件后，站台门打开</td></tr></table>

<div style="text-align: center;">表 57 站台门控制(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门控制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-27-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门控制。CBTC应打开站台门之前，应检查下列条件满足：1)列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；2)站台门侧与车门侧一致；3)列车零速；4)保持制动已施加</td></tr></table>

---

<div style="text-align: center;">表 57 站台门控制(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门控制</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，有门允许，并向联锁发送打开站台门的请求；联锁在打开站台门前，如果出现以下任一情况，则车载系统不向联锁发送开门命令。1)列车不在停车窗内；2)站台门侧与车门侧不一致；3)列车未停稳；4)保持制动未施加</td></tr></table>

#### 6.4.22 车门防护

车门防护功能的测试和验证方法详见表58～表67。

<div style="text-align: center;">表 58 车门防护(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护，仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备，处于RM控制等级，有位置报告的列车， 车门未被旁路且车门未处于“关闭且锁闭”状态，系统不允 许列车移动</td></tr></table>

<div style="text-align: center;">表 59 车门防护(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护：仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车， 车门被旁路且车门未处于“关闭且锁闭”状态时，列车可以 移动</td></tr></table>

---

<div style="text-align: center;">表 60 车门防护(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车， 车门处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

<div style="text-align: center;">表 61 车门防护(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护，仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，车门未被旁 路，且车门未处于“关闭且锁闭”状态，系统不允许列车移动</td></tr></table>

<div style="text-align: center;">表 62 车门防护(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，车门被旁路， 且车门未处于“关闭且锁闭”状态，列车可以移动</td></tr></table>

<div style="text-align: center;">表 63 车门防护(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护。仅在车门处于“关闭且锁闭”状态时，系统方 允许列车移动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制等级的列车，车门处于 “关闭且锁闭”状态，列车可以移动</td></tr></table>

---

<div style="text-align: center;">表 64 车门防护(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门状态丢失防护。列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于RM控制等级、有位置报告的列车，在运行过程中，车门方被旁路的情况下，监督到车门打开，可以采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr></table>

---

<div style="text-align: center;">表 66 车门防护(九)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门状态丢失防护。列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制级别的列车，在运行过程中，车门未被旁路的情况下，监督到车门打开，可以采取下列措施之一：1）切除牵引但不实施制动；2）不切除牵引，也不实施制动，列车运行至下一座车站；3）实施紧急制动；4）实施全常用制动</td></tr></table>

<div style="text-align: center;">表 67 车门防护(十)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-28-ITC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门状态丢失防护。列车在运行过程当中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：
1）切除牵引但不实施制动；
2）不切除牵引，也不实施制动，列车运行至下一座车站；
3）实施紧急制动；
4）实施全常用制动</td></tr></table>

---

<div style="text-align: center;">表 67 车门防护(十)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备、处于点式控制级别的列车，在运行过程中，车门被旁路的情况下，监督到车门打开，不会采取下列任一种措施：1）切除牵引但不实施制动；2）实施紧急制动；3）实施全常用制动</td></tr></table>

#### 6.4.23 车门防护切除

车门防护切除功能的测试和验证方法详见表68和表69。

<div style="text-align: center;">表 68 车门防护切除（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护切除</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-29-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于RM控制等级、有位置报告的列车，车门故障时处于打开状态，司机操作使车门处于“车门切除”状态；2) 列车可以移动</td></tr></table>

<div style="text-align: center;">表 69 车门防护切除(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车门防护切除</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-29-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车门防护切除。系统在车门故障时，可提供车门切除功能，此时ATP不再对车门状态进行防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)装备CBTC设备，处于点式控制等级的列车，车门故障时处于打开状态，司机操作使车门处于“车门切除”状态；2)列车可以移动</td></tr></table>

---

#### 6.4.24 站台门防护

站台门防护功能的测试和验证方法详见表70。

<div style="text-align: center;">表 70 站台门防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-30-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台门状态丢失的响应。当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 装备CBTC设备、处于点式控制等级的列车，位于站台外，进站进路已排列并开放，此时站台门关闭状态丢失，验证进站进路始端信号机关闭；2) 装备CBTC设备、处于点式控制等级的列车，位于站台内，出站进路已排列并开放，此时站台门关闭状态丢失，验证出站进路始端信号机关闭</td></tr></table>

#### 6.4.25 列车折返

列车折返功能的测试和验证方法详见表71～表73。

<div style="text-align: center;">表 71 列车折返(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATP监督下的人工折返模式，站后折返：司机人工驾驶列车由站台运行至折返区域，完成相应的确认操作，自动切换列车首尾驾驶端，然后人工驾驶列车进入发车股道，定点停车后，打开车门和站台门</td></tr></table>

---

<div style="text-align: center;">表 72 列车折返(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATP监督下的人工折返模式，站前折返：当列车在折返站定点停车后，司机完成相应的确认操作，自动切换列车首尾驾驶端，在此过程中司机根据上下客站台的设置打开和关闭车门和站台门</td></tr></table>


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车折返</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-31-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车折返方式应包括ATO无人机自动折返模式、ATO有人自动折返模式、ATP监督下的人工折返模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATP监督下的人工折返模式失败；列车在ATP监督下的人工折返过程中，折返失败，列车进入RM模式</td></tr></table>

#### 6.4.26 车载 ATP 界面功能 轨道

车载 ATP 界面功能的测试和验证方法详见表 74 ~ 表 77。

<div style="text-align: center;">表 74 车载 ATP 界面功能(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 显示数据。CBTC 车载显示屏落显示 ATP 数据应包括：1)列车运行模式；2)CBTC 运行状态；3)当前列车速度；4)当前最大允许 CBTC 速度；5)超速报警</td></tr></table>

---

<div style="text-align: center;">表 74 车载 ATP 界面功能(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于 RM 控制等级的列车，人机界面上要显示：1)列车运行模式；2)CBTC 运行状态；3)当前列车速度；4)当前最大允许 CBTC 速度；5)超速报警</td></tr></table>

<div style="text-align: center;">表 75 车载 ATP 界面功能(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 显示数据。CBTC 车载显示屏将显示 ATP 数据应包括：1) 列车运行模式；2) CBTC 运行状态；3) 当前列车速度；4) 当前最大允许 CBTC 速度；5) 超速报警</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制等级的列车，人机界面上要显示：1) 列车运行模式；2) CBTC 运行状态；3) 当前列车速度；4) 当前最大允许 CBTC 速度；5) 超速报警</td></tr></table>

---

<div style="text-align: center;">表 76 车载 ATP 界面功能(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 输入数据。用户 ATP 信息输入到 CBTC 应包括：1) 运行模式选择；2) 超速报警情况确认</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于 RM 控制等级的列车、ATP 设备的人机界面上支持的输入信息：1) 运行模式选择；2) 超速报警情况确认；</td></tr></table>

<div style="text-align: center;">表 77 车载 ATP 界面功能（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载 ATP 界面功能</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-32-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC 车载 ATP 输入数据。用户 ATP 信息输入到 CBTC 应包括：1) 运行模式选择；2) 超速报警情况确认</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备、处于点式控制等级的列车、ATP 设备的人机界面上支持的输入信息：1) 运行模式选择；2) 超速报警情况确认</td></tr></table>

#### 6.4.27 ATP 自诊断、故障报警及数据记录

ATP 自诊断、故障报警及数据记录功能的测试和验证方法详见表 78。

<div style="text-align: center;">表 78 ATP 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATP 白诊断、故障报警及数据记录</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-33-ITC-1</td></tr></table>

---

<div style="text-align: center;">表 78 ATP 自诊断、故障报警及数据记录(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATP 自诊断、故障报警及数据记录</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自诊断、故障报警及数据记录。ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存7 d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备 CBTC 设备的列车，需具备自诊断、故障报警及数据记录的功能；ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并至少保存7 d，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据</td></tr></table>

#### 6.4.28 模式转换

模式转换功能的测试和验证方法详见表79～表83。

<div style="text-align: center;">表 79 模式转换(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车驾驶模式。列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）和列车自动防护模式（CM）为列车正常运行模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>装备CBTC设备的列车，列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）。列车自动运行模式（AM）和列车自动防护模式（CM）为列车正常运行模式</td></tr></table>

---

<div style="text-align: center;">表 80 模式转换(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的大小转换，CM转为AM时：1)列车处于CM模式，设备ATO启动条件时，司机点击ATO启动确认按钮，列车进入AM模式运行，同时验证了由低等级转为高等级时，不停车转换驾驶模式；2)对于模式转换，车载设备进行记录和显示</td></tr><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CDTC-F-ATP-34-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的自动转换，RM转为CM时：1)列车处于RM有位置模式，经过主应答器，获得点式允许报文，列车升级为点式列车，驾驶模式自动转换为CM，同时验证了由低等级转为高等级时，不停车转换驾驶模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

---

<div style="text-align: center;">表 82 模式转换(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换。列车驾驶模式等级由高至低分别为：AM、CM、RM。各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车。驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的转换，AM、CM转为RM时：1)列车处于点式AM或CM模式，进入转换轨，速度低于预定值，ATP人机界面提示要转换为RM，停车后，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

<div style="text-align: center;">表 83 模式转换(T)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-34-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>驾驶模式转换 列车驾驶模式等级由高至低分别为：AM、CM、RM 各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示 为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车驾驶模式由低等级向高等级转换时，列车宜不停车转换驾驶模式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶模式的转换，列车进入车辆段/停车场时，AM、CM转为RM时：1)列车处于点式AM或CM模式，进入进段转换轨，速度低于预定值，ATP人机界面提示要转换为RM，在不停车情况下，经司机确认可转换为RM模式；2)对于模式转换，车载设备进行记录和显示</td></tr></table>

---

#### 6.4.29 电子地图存储

电子地图存储功能的测试和验证方法详见表84。

<div style="text-align: center;">表 84 电子地图存储</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-36-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>电子地图存储，CBTC系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>车载电子地图 装备CBTC系统的车载设备，应根据运行范围的不同，存储相关范围的电子地图，如在某条线路A上运行，则电子地图包含整条线路上的数据</td></tr></table>

#### 6.4.30 确定 ATO 曲线

确定 ATO 曲线功能的测试和验证方法详见表 85。

<div style="text-align: center;">表 85 确定 ATO 曲线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>确定 ATO 曲线</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-38-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>确定 ATO 曲线。CBTC 系统应为列车确定 ATO 曲线。ATO 子系统在 ATP 子系统的保护下，根据 ATS 子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制。ATO 子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在 ATP 系统的监督下，处于自动驾驶模式下的点式列车在线运行，系统自动计算 ATO 运行曲线，并控制列车按照 ATO 曲线运行，包括列车的加速、减速、惰行和巡航</td></tr></table>

#### 6.4.31 精确停车

精确停车功能的测试和验证方法详见表86。

---

<div style="text-align: center;">表 86 精准停车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>精确停车</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-39-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进站精确停车。ATO子系统应具备列车进站精确停车功能，并支持不同编组的列车可以停靠的不同的停车位置</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)系统设置不同编组长度的列车；2)处于自动驾驶模式下的点式列车执行进站停车，并保证列车在指定位置精确停车</td></tr></table>

#### 6.4.32 根据 ATO 曲线调整列车速度

根据 ATO 曲线调整列车速度功能的测试和验证方法详见表 87.

<div style="text-align: center;">表 87 根据 ATO 曲线调整列车速度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>根据 ATO 曲线调整列车速度</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-40-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车调速 CBTC 系统应根据 ATO 曲线调整列车速度</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的点式列车在线运行，ATO 系统依据列车运行信息，包括限速点、停车点等，控制列车速度，保证在正常运行</td></tr></table>

#### 6.4.33 开关车门

开关车门功能的测试和验证方法详见表88和表91.

<div style="text-align: center;">表 88 开关车门(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>开列车门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-43-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>开列车门：在AM驾驶模式和ATP的防护下可提供自动开门或者人工开门两种开门方式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的点式列车到站停稳停准后，依据门控模式等条件自动或人工开启列车车门</td></tr></table>

---

<div style="text-align: center;">表 89 开关车门(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>开站台门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-43-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>开站台门。CBTC系统应能自动开启站台门</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式列车到站停稳停准后，依据门控模式等条件自动发 送开启站台门的联控命令</td></tr></table>

<div style="text-align: center;">表 90 开关车门(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>关闭列车门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-E-ATO-43-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>关闭列车门。在AM驾驶模式下，可提供自动关门或者人工关门两种关门方式</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>处于自动驾驶模式下的点式列车到站并执行完成在站作业后，依据门控模式等条件自动或人工关闭列车车门</td></tr></table>

<div style="text-align: center;">表 91 开关车门(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>关闭站台门</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-ATC-43-TC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>关闭站台门，CBTC系统应能自动关闭站台门</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式列车到站并执行完成在站作业后，依据门控模式等条件自动发送关闭站台门的联控命令</td></tr></table>

#### 6.4.34 ATO 界面显示

ATO 界面显示功能的测试和验证方法详见表 92。

<div style="text-align: center;">表 92 ATO 界面显示</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO 界面显示</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-44-ITC-1</td></tr></table>

---

<div style="text-align: center;">表 92 ATO 界面显示(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO界面显示</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC车载ATO显示数据：在列车显示屏上显示的CBTC车载ATO数据应由授权管理部门规定</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式列车运行过程中，车载人机界面上的显示对应内容（依据授权管理部门规定）</td></tr></table>

#### 6.4.35 ATO 自诊断、故障报警及数据记录

ATO 自诊断、故障报警及数据记录功能的测试和验证方法详见表 93。

<div style="text-align: center;">表 93 ATO 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO 自诊断、故障报警及数据记录</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-45-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自诊断、故障报警及数据记录。ATO 子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心 ATS</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>模拟 ATO 设备故障。在车载人机界面上显示相应的报警信息，或者车载维护终端上对应相应的数据信息。此外，在 ATS 中心显示终端查询相关报警信息</td></tr></table>

#### 6.4.36 车载旅客信息数据

车载旅客信息数据功能的测试和验证方法详见表94。

<div style="text-align: center;">表 94 车载旅客信息数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载旅客信息数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATO-47-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载旅客信息数据。ATO车载设备应向TMS提供有关车载旅客信息的数据</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式或RM列车通过数据接口向列车TMS系统发送运营相关数据（若有）</td></tr></table>

---

#### 6.4.37 确定列车识别号

确定列车识别号功能的测试和验证方法详见表95和表96。

<div style="text-align: center;">表 95 确定列车识别号（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CBTC的运行列车识别号</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-48-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC的运行列车识别号.每一个运行在CBTC区域 内的装备CBTC的列车都应该分配一个运行列车识别 号.列车识别号应由列车号、车次号、车组号、目的地号 组成</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式或RM列车在线运行,ATS系统可实现对列车识别号 的追踪,并可以通过ATS操作终端人工设置或修改列车号、 车次号、车组号、目的地号</td></tr></table>

<div style="text-align: center;">表 96 确定列车识别号(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车识别号丢失处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-48-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车识别号丢失处理。在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车-地双向通信传输信息恢复</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式或RM列车在线运行，丢失识别号后，系统根据运行图、列车位置及时间自动推算并自动设置列车识别号</td></tr></table>

#### 6.4.38 ATS 列车追踪

ATS 列车追踪功能的测试和验证方法详见表 97。

<div style="text-align: center;">表 97 ATS 列车追踪</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS 列车追踪</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-49-ITC-1</td></tr></table>

---

<div style="text-align: center;">表 97 ATS 列车追踪(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS列车追踪</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS列车追踪。ATS系统应该具有自动追踪，获取所有运行在CBTC区域的装备CBTC的列车记录并在ATS用户界面显示位置、标识、列车时刻表，以及其他的相关信息并保持这些信息的能力。列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上。列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 点式或RM列车在线运行（包括跨线运行），ATS系统可以实现列车识别号的追踪功能，并在ATS中心或车站操作终端观察列车运行信息，包括位置、标识等2) 点式或RM列车进出段运行，ATS系统可以实现列车识别号的追踪功能，在ATS中心或车站操作终端观察列车运行信息，包括车组号的跟踪、显示</td></tr></table>

#### 6.4.39 列车进路办理

列车进路办理功能的测试和验证方法详见表98～表100。

<div style="text-align: center;">表 98 列车进路办理（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——自动</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-50-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——自动 ATS 系统应该具有列车自动办理进路的功能。ATS 系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在 ATS 车站或中心操作终端设置并确认进路具备自动进路功能（包括跨线进路），点式列车接近后自动触发前方进路</td></tr></table>

---

<div style="text-align: center;">表 99 列车进路办理（二）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——人工</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-50-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——人工。ATS系统应该具有手动办理进路的功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS车站或中心操作的终端人工办理进路（包括跨线进路）</td></tr></table>

<div style="text-align: center;">表 100 列车进路办理（三）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车进路办理——冲突检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-DAT8-50-ITG-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>列车进路办理——冲突检查，当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS系统控制一个具有交路冲度的运行计划，并加载该运行计划对冲突检查功能进行检查</td></tr></table>

#### 6.4.40 时刻表编制管理

时刻表编制管理功能的测试和验证方法详见表101。

<div style="text-align: center;">表 101 时刻表编制管理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>时刻表编制管理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-57-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>依据时刻表输入数据，在ATS时刻表编辑终端编制新的时刻表或对既有时刻表进行变更</td></tr></table>

#### 6.4.41 模拟培训

模拟培训功能的测试和验证方法详见表102。

---

<div style="text-align: center;">表 102 模拟培训</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>模拟培训</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-58-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应具备模拟演示及培训系统，实现对调度员的培训</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS模拟系统上执行演示和培训内容</td></tr></table>

#### 6.4.42 ATS 界面功能

ATS 界面功能的测试和验证方法详见表 103 和表 104。

<div style="text-align: center;">表 103 ATS 界面功能(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS显示数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-59-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS显示数据，CBTC的ATS显示应能够表示以下信息：1)精确的和区域相关的信息；2)列车状态相关信息；3)列车移动授权/进路信息；4)和被控列车运行相关的信息如防护区段信息，锁闭的进路/区段，以及临时限速极限和限速值；5)其他</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式或RM列车在线运行，在ATS中心或车站操作终端显示列车运行位置、状态及相关的进路信息（包括保护区段、进路锁闭等）</td></tr></table>

<div style="text-align: center;">表 104 ATS 界面功能(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CBTC 输入数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-59-ITC-2</td></tr></table>

---

<div style="text-align: center;">表 104 ATS 界面功能(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CBTC输入数据</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC输入数据。CBTC的ATS用户界面显示应能够接收 以下ATS用户输入： 1)办理和取消进路输入； 2)建立和取消防护区段，锁闭进路/区段，以及临时限速 输入； 3)其他</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>点式列车在线运行，在ATS中心或车站操作终端进行进 路的办理和取消（包括跨线进路）</td></tr></table>

#### 6.4.43 ATS 数据记录

ATS 数据记录功能的测试和验证方法详见表 105 和表 106。

<div style="text-align: center;">表 105 ATS 数据记录(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>发送报警数据</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-60-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>发送报警数据。ATS子系统可将自身的报警信息、ATP 车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在中心维护工作站、车站维护工作站以及维护中心的信号监测报警工作站上查询点式或RM列车相关运行信息，包括ATS子系统以及CI子系统报警信息</td></tr></table>

<div style="text-align: center;">表 106 ATS 数据记录(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据记录及回放</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-60-ITC-2</td></tr></table>

---

<div style="text-align: center;">表 106 ATS 数据记录(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据记录及回放</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>数据记录及回放。系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能。综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记录应保存不少于30 d</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在ATS车站或中心操作终端或信号监测报警工作站进行30 d前的数据的查询操作，包括操作信息以及设备运行状态等</td></tr></table>

#### 6.4.44 中控/站控转换

中控/站控转换功能的测试和验证方法详见表107。

<div style="text-align: center;">表 107 中控/站控转换</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站控/遥控</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATS-61-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级原则为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在 ATS 车站操作终端或中心操作终端通过申请和确认操作，进行站控和中心控的切换；2) 在车站操作终端强制获取控制权；3) 本地或中央自动控制模式时，进行人工进路的相关操作，确认人工控制优于自动控制</td></tr></table>

#### 6.4.45 进路办理

进路办理功能的测试和验证方法详见表108和表109。

---

<div style="text-align: center;">表 108 进路办理(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>进路办理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-62-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>进路办理。联锁应具备进路办理功能。包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)联锁支持人工排列并建立进路（包括跨线进路）功能；2)联锁支持为点式列车设置进路为自动进路模式功能</td></tr></table>

<div style="text-align: center;">表 109 进路办理(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>具有无效CBTC装备的列车进路办理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-CI-62-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>装有无效CBTC装备的列车进路办理。对于设备故障的CBTC列车或无装备的列车，在前方进路出清片重新开放后装有无效CBTC装备的列车方可驶入</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>建立进路（包括跨线进路），联锁级列车通过进路，进路正常逐段解锁</td></tr></table>

#### 6.4.46 保护区段控制

保护区段控制功能的测试和验证方法详见表110和表111。

<div style="text-align: center;">表 110 保护区段控制（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>保护区段建立</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-63-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>保护区段. 联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) CI终端办理进路（包括跨线进路），将触发保护区段并锁闭；2) 点式或 RM列车通过进路，进路逐段自动解锁</td></tr></table>

---

<div style="text-align: center;">表 111 保护区段控制(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>保护区段解锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-63-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>点式或 RM 列车进站停稳后，保护区段应自动解锁（延时或立即）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>驾驶 ITC-CM 列车在站台停车点处对位停车，列车停稳后，站台外方保护区段满足解锁条件后解锁</td></tr></table>

#### 6.4.47 进路/区段锁闭

进路/区段锁闭功能的测试和验证方法详见表112。

<div style="text-align: center;">表 112 进路/区段锁闭</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-64-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>进路/区段锁闭。系统应具有锁闭（并随后解锁）CBTC 区域内的道岔、信号机或轨道区段的能力。CI 子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 在 CBTC 区域内选取一条含有道岔的进路（包括跨线进路），排列并建立进路；2) 取消已建立的进路，进路关闭并解锁；3) 一点式或 RM 列车接近并完整通过开放的进路，进路将逐段顺序解锁</td></tr></table>

#### 6.4.48 道岔单操、单锁

道岔单操、单锁功能的测试和验证方法详见表113。

<div style="text-align: center;">表 113 道岔单操、单锁</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔单操、单锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-65-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>道岔单操、单锁。联锁具备道岔单独操纵及锁闭的能力</td></tr></table>

---

<div style="text-align: center;">表 113 道岔单操、单锁（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>道岔单操、单锁</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>CI操作终端上执行道岔的单独锁闭、解锁及总定、总反操作，操作可以正确执行</td></tr></table>

#### 6.4.49 车站/区间封锁

车站/区间封锁功能的测试和验证方法详见表114。

<div style="text-align: center;">表 114 车站/区间锁闭</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车站/区间封锁</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-66-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>封锁：系统应具有车站封锁、区间封锁的能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)封锁进站信号或者站台股道区段后，不能建立进站的进路； 2)封锁出站信号或者出站离去区段后，不能建立进入区间的进路（包括跨线区间）</td></tr></table>

#### 6.4.50 站台紧急关闭按钮

站台紧急关闭按钮功能的测试和验证方法详见表115。

<div style="text-align: center;">表 115 站台紧急关闭按钮</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站台紧急关闭按钮</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-67-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>站台紧急关闭按钮：联锁子系统检查站台紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的进路或回缩相应列车的移动授权</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在点式控车模式下，排列并建立进站进路，激活对应站台的站台紧急关闭按钮，联锁将关闭进站进路；2)在点式控车模式下，排列并建立出站进路，激活对应站台的站台紧急关闭按钮，联锁将关闭出站进路</td></tr></table>

---

#### 6.4.51 CI 自检、故障报警及数据记录

CI 自检、故障报警及数据记录功能的测试和验证方法详见表 116 和表 117。

<div style="text-align: center;">表 116 CI 自检、故障报警及数据记录(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>故障监测</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-69-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>故障监测、CI子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>设置设备报警条件（包括系统自身故障，信号机、转辙机等设备故障），在联锁维护终端界面显示相应的设备故障提示</td></tr></table>

<div style="text-align: center;">表 117 CI 自检、故障报警及数据记录(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>监视和记录工作状态</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-ATP-69-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>监视和记录工作状态。CI子系统能监视和记录自身的工作状态和轨旁设备的状态，内容包括：进路状态、保护区段状态、轨道的占用/空闲、信号机显示、道岔位置、信号机主灯丝状态监测及断丝报警、转辙机动作状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在联锁维护终端显示设备工作状态，包括系统自动工作状态以及轨旁设备工作状态；2)在联锁维护终端界面获取并检查日志记录信息</td></tr></table>

#### 6.4.52 计轴故障恢复

计轴故障恢复功能的测试和验证方法详见表118。

---

<div style="text-align: center;">表 118 计轴故障恢复</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>计轴故障恢复</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-F-CI-71-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>计轴故障恢复。系统应具有计轴故障恢复的能力</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)计轴预复位操作和列车完整通过完成计轴的复位（若具备）；2)计轴直接复位操作完成计轴的立即复位（若具备）</td></tr></table>

#### 6.4.53 CI 权限设置

CI 权限设置功能的测试和验证方法详见表 119。

表 119 CI 权限设置


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI权限设置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-E-CI-74-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>操作权限设置：CI子系统能设置不同操作人员的权限， 并有相应的安全操作手段</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>启动CI子系统，操作人员需要通过口令进行登录和初始 化操作，且任何安全相关的操作需要输入口令执行</td></tr></table>

### 6.5 互联互通应答器接口需求

#### 6.5.1 概述

本章节的需求依据 T/CAMET 04011.1 编写，文中所描述的章节号引用自 T/CAMET 04011.1。

#### 6.5.2 通信配置及控制功能

通信配置及控制功能的测试和验证方法详见表 120 ~ 表 129。

<div style="text-align: center;">表 120 通信配置及控制功能(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式通信结构配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-1</td></tr></table>

---

<div style="text-align: center;">表 120 通信配置及控制功能（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式通信结构配置</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC系统中，车载ATP应通过车载BTM实现与应答器的通信。当列车经过地面应答器时，车载应答器天线激活地面应答器，并接收应答器循环发送的应答器报文</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 121 通信配置及控制功能(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式通信结构配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC系统应通过车载BTM和应答器传输报文实现如下功能：1)建立列车定位；2)校正列车位置；3)传输点式移动授权；4)监控应答器通信状态</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)列车定位功能测试需求：装备CBTC设备、RM控制等级、无位置报告的列车，经过两个连续具备定位条件的应答器，获得列车位置和方向，完成定位；2)校正列车位置，RM下测试需求：装备CBTC设备、RM控制等级、有位置报告的列车，在经过应答器前观察列车包络，经过应答器后，检查列车位置更新，包络缩小；3)校正列车位置，点式下测试需求：装备CBTC设备、点式控制等级、在经过应答器前观察列车包络，经过应答器后，检查列车位置更新，包络缩小；4)传输点式移动授权，RM下测试需求：装备CBTC设备、RM控制等级、有位置报告的列车，前方进路开放允许信号，列车经过主应答器，获得点式移动授权，升级为点式模式；5)传输点式移动授权，点式下测试需求：装备CBTC设备、点式控制等级，前方进路开放允许信号，列车经过主应答器，点式移动授权更新；6)监控应答器通信状态：当应答器故障时，车载ATP收不到应答器报文，当连续收不到应答器报文的应答器个数不超过系统设计值时，列车定位保持；超过系统设计值时，列车丢失定位</td></tr></table>

---

<div style="text-align: center;">表 122 通信配置及控制功能(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>点式通信结构配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC的点式后备系统或主用系统为点式的信号系统应满足T/CAMET 04011.1章节5.1.3图1定义的结构。LEU可通过联锁设备或信号机点灯电路控制，如采用信号机点灯电路控制。应考虑是否能够满足线路拓扑要求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 123 通信配置及控制功能(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器功能分配</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CBTC的点式后备系统或主用系统为点式的信号系统基本功能分配如下：1)信号机由联锁设备控制；2)联锁或信号机点灯电路通过LEU控制有源应答器报文；3)车载设备通过应答器天线获取应答器信息，根据点式移动授权，生成制动曲线并进行相应的防护</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 124 通信配置及控制功能（五）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器通信制式</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>地面应答器采用无线通信方式向车载应答器单方向循环传送报文</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 125 通信配置及控制功能（六）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器类型及配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应答器按照报文是否可变，可分为无源应答器和有源应答器。其中无源应答器又称固定应答器，有源应答器可分为主应答器和填充应答器两种。固定应答器报文不可变，主应答器与填充应答器报文可变，主应答器布置在信号机处，填充应答器布置在主应答器外方，填充应答器与主应答器的距离宜保证列车不至降速时收到填充应答器报文。填充应答器与主应答器报文中信号状态和移动授权信息一致</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 固定应答器测试需求：在线路上选择固定应答器，检查报文固定不变。2. 填充应答器测试需求：在线路上选择填充应答器，检查内容如下：1) 检查填充应答器布置在主应答器外方；2) 填充应答器对应的主应答器的始端信号机开放允许信号，驾驶点式列车经过填充应答器，检查列车不降速；3) 填充应答器和主应答器报文一致；4) 选择包含道岔的进路，检查道岔开往不同方向时，填充应答器的报文会发生变化。3. 主应答器测试需求：在线路上选择主应答器，检查内容如下：1) 主应答器布置在信号机处；2) 选择包含道岔的进路，检查道岔开往不同方向时，主应答器的报文会发生变化</td></tr></table>

<div style="text-align: center;">表 126 通信配置及控制功能(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器类型及配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在无点式后备模式时，系统只需要配置固定应答器</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 127 通信配置及控制功能(八)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>物理接口应满足如下要求：地面有源应答器应采用LEU进行编码，应采用专用电缆连接。车载应答器天线与BTM应通过专用馈缆连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 128 通信配置及控制功能（九）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>D1 容器类型及配置</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-FCO4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>地面应答器与车载应答器天线间的信息传输接口（也称接口 A），应答器编码与解码应满足《应答器传输系统技术条件》（TB/T 3485）的要求</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>应答厂商设计文件</td></tr></table>

<div style="text-align: center;">表 129 通信配置及控制功能(十)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>通信故障处理，应符合以下要求：
1）如遇BTM无法解码、应答器天线无法激活应答器、传输错误等原因导致车载设备无法接收应答器报文，车载设备应按照应答器丢失处理，应满足故障导向安全的原则；
2）有源应答器与LEU通信故障时，应答器应发送应答器默认报文（灭灯情况下也发送默认报文）；LEU与联锁通信中断时，LEU向应答器发送LEU默认报文，并经应答器发送至车载设备</td></tr></table>

---

<div style="text-align: center;">表 129 通信配置及控制功能(十)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)BTM无法解码、应答器天线无法激活应答器、传输错误等原因导致车载设备无法接收应答器报文，当连续收不到应答器报文的应答器个数超过系统设计值时，列车丢失定位；2)有源应答器与LEU通信故障时，应答器应发送应答器默认报文，报文中C_LEU_BALISE=1；LEU与联锁通信中断时，LEU向应答器发送LEU默认报文，报文中C_CI_LEU=1</td></tr></table>

#### 6.5.3 报文标识及格式信息

报文标识及格式信息功能的测试和验证方法详见表130～表137。

<div style="text-align: center;">表 130 报文识别及格式信息(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文长度要求</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-11</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应答器报文采用830位长报文结构，用户信息包中不足的位以1补齐</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 131 报文识别及格式信息(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应答器报文结构定义详见 T/CAMET 04011.1 章节 5.3.1 表1</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>因 Q_UPDOWN、M_VERSION、Q_MEDIA、N_PIG、N_TOTAL、M_DUP 在本协议中为定值，检查应答器报文中上述变量是否分别对应为 1、0010000、0、000、000、00 即可</td></tr></table>

---

<div style="text-align: center;">表 132 报文识别及格式信息（三）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——报文计数器</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>报文计数器对应变量名为M_MCOUNT，采用8位表示。单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号 固定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252。LEU默认报文，M_MCOUNT设为0。M_MCOUNT值禁用253和254。其他报文M_MCOUNT由厂商自定</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查固定应答器中M_MCOUNT=255</td></tr></table>

<div style="text-align: center;">表 133 报文识别及格式信息（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——报文计数器</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>报文计数器对应变量名为M_MCOUNT，采用8位表示。单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号。固定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252。LEU默认报文，M_MCOUNT设为0。M_MCOUNT值禁用253和254。其他报文M_MCOUNT由厂商自定</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查有源应答器默认报文M_MCOUNT=252</td></tr></table>

<div style="text-align: center;">表 134 报文识别及格式信息（五）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——报文计数器</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>报文计数器对应变量名为M_MCOUNT，采用8位表示。单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号。固定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252。LEU默认报文，M_MCOUNT设为0。M_MCOUNT值禁用253和254。其他报文M_MCOUNT由厂商自定</td></tr></table>

---

<div style="text-align: center;">表 134 报文识别及格式信息（五）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——报文计数器</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查 LEU 默认报文 M_MCOUNT = 0</td></tr></table>

<div style="text-align: center;">表 135 报文识别及格式信息（六）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——报文计数器</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>报文计数器对应变量名为M_MCOUNT，采用8位表示。单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号。固定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252。LEU默认报文，M_MCOUNT设为0。M_MCOUNT值禁用253和254。其他报文M_MCOUNT由厂商自定</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查有源应答器除有源应答器默认报文、LEU默认报文外其他的报文，M_MCOUNT数值参考厂商自定</td></tr></table>

<div style="text-align: center;">表 136 报文识别及格式信息(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——线路编号</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-17</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>线路编号对应变量名为NID_L，采用10位表示 线路编号采用区域内统一编号的方式，可在区域线路规划时统一分配</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查应答器报文中NID_L等于线路编号</td></tr></table>

<div style="text-align: center;">表 137 报文识别及格式信息（八）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器报文结构定义——应答器(组)编号</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应答器(组)编号对应变量名为NID_BG,采用14位表示。用于在一条线路内,唯一识别的ID,由5位十进制数表示,最大值为16383</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查应答器报文中NID_BG等于应答器编号</td></tr></table>

---

#### 6.5.4 用户信息包

用户信息包功能的测试和验证方法详见表 138 ~ 表 149

<div style="text-align: center;">表 138 用户信息包(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ETCS-44包定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>每个ETCS-44包应只包含一个子包，一个应答器报文中可包含多个ETCS-44包，ETCS-44包定义详见T/CAMET 04011.1章节5.3.2.1表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>选择线路设计中有效方向分别为反向有效、正向有效、双向有效的一个备器，检查Q_DIR中是否分别为00、01、10</td></tr></table>

表 139 用户信息包（二）


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>地图版本信息包定义(202 子包)</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>BTC-IF-BALSE-MSG-ITC-20</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>地图版本信息包定义详见 //CAMET 04011.1 章节 5.3.2.22 表 3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查报文中 MID_XUSER 为 202, M_EDITION 为本应答器所管辖范围内的地图版本</td></tr></table>

<div style="text-align: center;">表 140 用户信息包(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包定义(203 子包)</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-21</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>公共信息包定义详见 T/CAMET 04011.1 章节 5.3.2.3 表 4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 检查报文中 NID_XUSER = 203； 2) C_CI_LEU 的值：联锁与 LEU 通信正常该值取为 0，联锁与 LEU 通信中断该值取为 1； 3) C_LEU_BALISE 的值：检查 LEU 与应答器通信正常时该值取为 0，LEU 与应答器通信中断时该值取为 1；</td></tr></table>

---

<div style="text-align: center;">表 140 用户信息包(三)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包定义(203 子包)</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>4) Q_SIGNAL_ASPECT、D_DIS、N_SWITCH、NID_SWITCH1、S_SWITCH1_STATE、NID_SWITCH2、S_SWITCH2_STATE、……、NID_SWITCHN、S_SWITCHN_STATE 的值参见后续测试需求</td></tr></table>

<div style="text-align: center;">表 141 用户信息包(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——Q_SIGNAL_ASPECT取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-22</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>公共信息包——Q_SIGNAL_ASPECT取值详见T/CAMET 04011.1章节5.3.2.3表5. 黄灯序号的确认原则为：对于Q_SIGNAL_ASPECT中ABCDE FGHIJKLMNPOQ，从第3位（P）开始，每一位表示对向道岔（不包含顺向道岔）的状态，对向道岔定位为0，对向道岔反位为1，可最多表示15个对向道岔，不足15个对向道岔，为0。第1位（Q）表示是否有保护区段，0表示无保护区段，1表示有保护区段。例如前方进路存在3个对向道岔，第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位，详见T/CAMET 04011.1章节5.3.2.3表6. 由于道岔之前的走向关系，有可能出现黄灯序号不连续的情况</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试填充应答器：1）选择线路上任一条进路，分别办理进路始端信号机为红灯，引导、灭灯或故障情况下，检查Q_SIGNAL_ASPECT的值为1；2）选择线路上无保护区段的进路，主进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值为2；3）选择线路上有保护区段的进路，主进路和保护进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值为3；</td></tr></table>

---

<div style="text-align: center;">表 141 用户信息包(四)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——Q_SIGNAL_ASPECT 取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>4)选择线路上包含对向道岔最多的进路，检查Q_SIGNAL_ASPECT 的取值满足要求：A BCDE FGHI JKLM NP0Q，从第3位(P)开始，每一位表示对向道岔（不包含顺向道岔）的状态，对向道岔定位为0，对向道岔反位为1，可最多表示15个对向道岔，不足15个对向道岔为0。第1位(Q)表示是否有保护区段，0表示无保护区段，1表示有保护区段。第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位</td></tr><tr><td colspan="2">$ ^{*} $ 区分对向道岔和顺向道岔的方式：1)从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔前区域，后搜索到该道岔的岔后区域，则该道岔为该方向上的对向道岔。2)从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔后区域，后搜索到该道岔的岔前区域，则该道岔为该方向上的顺向道岔。</td></tr></table>

<div style="text-align: center;">表 142 用户信息包(五)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>Q_SIGNAL_ASPECT 取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-23</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>Q_SIGNAL_ASPECT 所表示的范围为主应答器对应的信号机所防护的进路的情况（即使该主应答器兼具预告应答器功能，Q_SIGNAL_ASPECT 也不报告前方预告进路的情况）。Q_SIGNAL_ASPECT 所表示的道岔不包含保护区段的道岔</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试填充应答器：1)选择线路上任一条进路，分别办理进路始端信号机为红灯，引导、灭灯或故障情况下，检查Q_SIGNAL_ASPECT 的值=1；2)选择线路上无保护区段的进路，主进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT 的值=2；</td></tr></table>

---

<div style="text-align: center;">表 142 用户信息包(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>Q_SIGNAL_ASPECT取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>3)选择线路上有保护区段的进路，主进路和保护进路锁闭完整，始端信号机点亮绿灯，检查Q_SIGNAL_ASPECT的值=3；4)选择线路上包含对向道岔最多的进路，检查Q_SIGNAL_ASPECT的取值满足要求：A BCDE FGHI JKLM NPOQ，从第3位(P)开始，每一位表示对向道岔(不包含顺向道岔)的状态，对向道岔定位为0，对向道岔反位为1，可最多表示15个对向道岔，不足15个对向道岔，为0。第1位(Q)表示是否有保护区段，0表示无保护区段，1表示有保护区段。第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位</td></tr></table>

<div style="text-align: center;">表 143 用户信息包(六)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——Q_SIGNAL_ASPECT_PRE 取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-24</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>Q_SIGNAL_ASPECT_PRE 取值: Q_SIGNAL_ASPECT_PRE 的定义方式与 Q_SIGNAL_APSECT 完全相同, 范围为兼预告的主应答器所预告的第二架信号机处开始至第二架信号防护的进路末端。如果 Q_SIGNAL_APSECT 为红灯, 则 Q_SIGNAL_ASPECT_PRE 取值为 0</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试填充应答器: 1) 选择线路上任一条进路, 分别办理进路始端信号机为红灯, 引导、灭灯或故障情况下, 检查 Q_SIGNAL_ASPECT 的值为 1; 2) 选择线路上无保护区段的进路, 主进路锁闭完整, 始端信号机点亮绿灯、检查 Q_SIGNAL_ASPECT 的值为 2; 3) 选择线路上有保护区段的进路, 主进路和保护进路锁闭完整, 始端信号机点亮绿灯、检查 Q_SIGNAL_ASPECT 的值为 3; 4) 选择线路上包含对向道岔最多的进路, 检查 Q_SIGNAL_ASPECT 的取值满足要求: A BCDE F GHI J K L M N P Q O, 从第 3</td></tr></table>

---

<div style="text-align: center;">表 143 用户信息包(六)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——Q_SIGNAL_ASPECT_PRE 取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>位(P)开始,每一位表示对向道岔(不包含顺向道岔)的状态, 对向道岔定位为0,对向道岔反位为1,可最多表示15个对向 道岔,不足15个对向道岔为0。第1位(Q)表示是否有保护 区段,0表示无保护区段,1表示有保护区段。第1个对向道 岔反位,第2个对向道岔定位,第3个对向道岔反位</td></tr></table>

<div style="text-align: center;">表 144 用户信息包(七)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——D_DIS取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-RAISE-MSG-ITG-25</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>D_DIS取值。主应答器至MA终点距离，至多160km（1m分辨率）。如果该应答器为填充应答器，则该距离为填充应答器对应的主送答器至MA终点距离。如果进路有保护区段，则MA终点放置在保护区段的末端，如果进路无保护区段，则MA终点位于进路最后一个区段的末端。若进路内有车挡，则MA终点应不超过车挡。红灯情况下，如果含保护区段，则该距离为前方保护区段的末端；如果没有保护区段，则该距离填充至当前进路末端。对于兼预告的主应答器，则该距离与预告进路是否开放相关。如果预告进路未开放，则该距离遵从上述原则；如果预告进路开放，则该距离为兼预告主应答器至第二架信号机防护进路的终点的距离，保护区段处理方式相同。默认报文中，D_DIS填0</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试填充应答器分以下几种情况：1) 始端信号机开放的是允许信号，且进路有保护区段，D_DIS为进路长度加保护区段长度（主信号应答器到MA终点）；</td></tr></table>

---

<div style="text-align: center;">表 144 用户信息包(七)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——D_DIS取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>2) 始端信号机开放的是允许信号，进路无保护区段，D_DIS为进路长度（主信号应答器到MA终点）；3) 始端信号机开放的是允许信号，进路有车挡，D_DIS为主信号应答器到车挡；4) 始端信号机为红灯，列车所占当前进路有保护区段，则D_DIS为列车至保护区段末端的距离（主信号应答器到MA终点）；5) 始端信号机为红灯，列车所占当前进路无保护区段，则D_DIS为列车至当前进路末端的距离（主信号应答器到MA终点）；6) 预告进路开放，列车所占当前进路有保护区段，则D_DIS为列车至保护区段末端的距离（主信号应答器到MA终点）；7) 预告进路开放，进路无保护区段，D_DIS为进路长度（主信号应答器到MA终点）；8) 预告进路开放，进路有车挡，D_DIS为主信号应答器到车挡；9) 如为默认报文，D_DIS=0</td></tr></table>

<div style="text-align: center;">表 145 用户信息包(八)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——D_DIS_OVERLAP 取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-26</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>D_DIS_OVERLAP 取值。主应答器至进路保护区段起点的距离，至多 160 km（1 cm 分辨率）。 如果该应答器为填充应答器，则该距离为填充应答器对应的主应答器至主应答器对应的信号机防护进路末端的保护区段起点距离。 如果进路无保护区段，D_DIS_OVERLAP 填 0。 默认报文中，D_DIS_OVERLAP 填 0。 对于兼预告的主应答器，则该距离与预告进路是否开放相关。如果预告进路未开放，则该距离遵从上述原则；如果预告进路开放，则该距离为兼预告主应答器至第二架信号机防护进路末端的保护区段起点距离，保护区段处理方式相同</td></tr></table>

---

<div style="text-align: center;">表 145 用户信息包(八)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——D_DIS_OVERLAP取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试主应答器分以下几种情况：1) 始端信号机开放的是允许信号，且进路有保护区段，D_DIS_OVERLAP为进路长度（主应答器至进路保护区段起点的距离）；2) 始端信号机开放的是允许信号，进路无保护区段，D_DIS_OVERLAP填0；3) 始端信号机为红灯，列车所占当前进路有保护区段，则D_DIS_OVERLAP为列车至保护区段起点的距离（主应答器至进路保护区段起点的距离）；4) 始端信号机为红灯，列车所占当前进路无保护区段，则D_DIS_OVERLAP为0；5) 如为默认报文，D_DIS_OVERLAP=0</td></tr></table>

<div style="text-align: center;">表 146 用户信息包（儿）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——NID_SWITCH 取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-27</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>NID_SWITCH 取值、线路内统一编号、且唯一</td></tr><tr><td style='text-align: center;'>验证阶段</td><td style='text-align: center;'>产品设计与实现、验证平台测试</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查进路中道岔编号 NID_SWITCH 是否存在</td></tr></table>

<div style="text-align: center;">表 147 用户信息包(十)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——N_SWITCH 取值</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-28</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>N_SWITCH 取值。MA 范围内道岔的数量，如果进路包含 保护区段，则保护区段内的道岔也包含在内。道岔数量应小于 15，该包根据不同的道岔数量是变长的。道岔数量不足 15 个，包的长度按照实际的道岔数量确定。如果 MA 范围内没有道岔，则 N_SWITCH 为 0，NID_SWITCH 和 S_SWITCH_STATE 位不存在。默认报文中认为 MA 范围内没有道岔</td></tr></table>

---

<div style="text-align: center;">表 147 用户信息包(十)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>公共信息包——N_SWITCH取值</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试分以下几种情况：1)进路有保护区段，且保护区段内有道岔，最好选保护区段包含多个道岔的场景，检查N_SWITCH的值等于进路中道岔的数量加保护区段中道岔的数量；2)进路无保护区段，检查N_SWITCH的值等于进路中道岔的数量；3)MA范围中无道岔，N_SWITCH为0，NID_SWITCH和S_SWITCH_STATE位不存在；4)默认报文N_SWITCH为0，NID_SWITCH和S_SWITCH_STATE位不存在</td></tr></table>

<div style="text-align: center;">表 148 用户信息包(十一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>自定义包定义(204 子包)</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-29</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义包定义详见 T/CAMET 04011.1 章节 5.3.3 表 7 和表 8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>检查 NID_XUSER = 204, NID_PROVIDER 为厂商标识, D_RESERVED 为厂商自定义内容及格式</td></tr></table>

<div style="text-align: center;">表 149 用户信息包(十二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器发包原则</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-BALISE-MSG-ITC-30</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应答器发包原则详见T/CAMET 04011.1章节5.4表9</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)选择无源应答器，ETCS-44包中只包含地图版本信息包，即202子包；2)选择有源应答器，亮灯时有源应答器发送地图版本信息包（202子包）、公共信息包（203子包）、厂商自定义信息包（204子包，可选）、城市自定义信息包（205子包，可选）；3)选择有源应答器，有源应答器与LEU通信中断，地图版本信息包（202子包）、公共信息包（203子包），C_LEU_</td></tr></table>

---

<div style="text-align: center;">表 149 用户信息包(十二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应答器发包原则</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>BALISE为1；4)选择有源应答器，联锁与LEU通信中断，地图版本信息包(202子包)、公共信息包(203子包)，C_CI_LEU为1</td></tr></table>

### 6.6 互联互通计算机联锁(CI)间接口测试需求

#### 6.6.1 CI 与 CI 接口概述

CI 与 CI 接口概述功能的测试和验证方法详见表 150。

<div style="text-align: center;">表 150 CI 与 CI 接口概述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口概述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与CI子系统的接口是基于BSSP-I协议，通过双冗余以太网通信</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.2 通信层次描述

通信层次描述功能的测试和验证方法详见表 151。

<div style="text-align: center;">表 151 通信层次描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>T/CAMET 04011.5 章节 5.2.1 图 2 为 CI 与相邻 CI 通信的通信协议模型，CI 间层次结构详见 T/CAMET 04011.5 章节 5.2.3 图 3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.3 物理层描述

物理层描述功能的测试和验证方法详见表 152。

---

<div style="text-align: center;">表 152 物理层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理层描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。两系统按照A网和A网相连，B网和B网相连接的方式，其连接方式详见T/CAMET 04011.5章节5.1.1图1</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试功能内容：CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。对应测试需求：1）相邻CI间通过A网连接，B网中断，验证可以正常办理进路，操作道岔等；2）相邻CI间通过A网中断，B网连接，验证可以正常办理进路，操作道岔等；3）相邻CI间AB网同时连接，办理进路的同时（进路满足办理条件），断开任一网络，验证进路办理成功。该功能内容中描述的其他内容的验证通过产品设计来覆盖</td></tr></table>

#### 6.6.4 数据链路层描述

数据链路层描述功能的测试和验证方法详见表 153。

<div style="text-align: center;">表 153 数据链路层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据链路层</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>MAC(Medium Access Control)子层基于IEEE 802.3标准 MAC头由14个字节组成,1个帧校验序列(4字节)将被加 在Ethernet帧后面</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.6.5 网络层描述

网络层描述功能的测试和验证方法详见表 154。

<div style="text-align: center;">表 154 网络层描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>网络层</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本接口使用IPv4协议作为网络层的协议</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.6 传输层

传输层功能的测试和验证方法详见表155。

<div style="text-align: center;">表 155 传输层</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>传输层</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本接口使用UDP/IP协议作为传输协议</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.7 安全通信协议层

安全通信协议层功能的测试和验证方法详见表156。

<div style="text-align: center;">表 156 安全通信协议层</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议层</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>采用 RSSP-1 标准协议，同时通过序列号对冗余网络数据进行过滤，不作为本文档描述</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.8 应用层

应用层功能的测试和验证方法详见表 157。

---

<div style="text-align: center;">表 157 应用层</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用层</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>应用层遵守 T/CAMET 04011.5 规定的协议，详见 CI-CI 间接口描述</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.9 动态交互描述

动态交互描述功能的测试和验证方法详见表 158.

<div style="text-align: center;">表 158 动态交互描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>动态交互描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI以300 ms(周期根据各厂商配置)为周期向相邻的CI发送信息CI认为与邻站CI通信中断的超时时间定义为TCiTimeout(可配置,推荐值5s)CI没有接收到来自邻站CI的任何消息达到或超过TCiTimeOut超时时间定义的时间窗口,则CI应认为与邻站CI通信中断(指应用层根据GAL包头中字段进行判断,而非安全通信协议层进行的判断);若CI判断接收到邻站CI的应用信息延迟已经达到TCiTimeOut时,CI应认为与邻站CI通信中断(指应用层根据GAL包头中字段进行判断,而非安全通信协议层进行的判断)CI与邻站CI间通信中断的情况下,本站CI无法收到邻站汇报的设备信息。CI应将邻站所有设备状态设置为安全侧,如将通往邻站进路的始端信号机置为禁止信号,对应来自邻站的区段设置为占用;CI与邻站CI间通信中断的情况下,若本站CI收到了合法的邻站CI信息,则本站CI应认为与邻站CI连接恢复。互联互通线网中,CI与邻站CI的通信超时时间应一致,消息有效期时间应一致。</td></tr></table>

---

<div style="text-align: center;">表 158 动态交互描述(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>动态交互描述</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与邻站CI间通信中断的情况下，若本站CI收到了合法的邻站CI信息，则本站CI应认为与邻站CI连接恢复</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>断开相邻CI间通信，验证3个通信周期后，相邻CI认为通信中断</td></tr></table>

#### 6.6.10 通信故障处理

通信故障处理功能的测试和验证方法详见表159。

<div style="text-align: center;">表 159 通信故障处理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>通信中断后，本站CI无法收到3站汇报的设备信息。CI将邻站所有设备状态设置为安全侧（置为0），如将通往邻站进路的命端信号机置为禁止信号。对应来自邻站的区段设置为占用</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)双通道全部断开后，接送端CI子系统认为通信中断，并有相应的报备提示。2)设备状态置为安全侧，设备包含：道岔（四开）、逻辑区段（占用）、物理区段（占用）、信号机（关闭）、站台门（开启且未旁路）、紧停按钮（按下）、照查（照查不满足）、进路（接近锁闭）、保护区段（未请求）、联锁系统（上电锁闭）</td></tr></table>

#### 6.6.11 CI 间通信通用报文

CI间通信通用报文功能的测试和验证方法详见表160。

<div style="text-align: center;">表 160 CI 间通信通用报文</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI 间通信通用报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-11</td></tr></table>

---

<div style="text-align: center;">表 160 CI 间通信通用报文(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI间通信通用报文</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL消息包中包含CI间传输的各条应用信息，每个GAL消息包总长不得超过1000字节。信息包格式定义详见T/CAMET 04011.5章节5.3.1.2的表1和表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.6.12 CI 与 CI 接口描述

CI 与 CI 接口描述功能的测试和验证方法详见表 161。

<div style="text-align: center;">表 161 CI 与 CI 接口描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-CI/CI-MSG-ITC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1) CI间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）的内容详见T/CAMET 04011.5章节5.3.2的表3；2) 本CI应将互联互通相关范围内的本联锁管辖范围的道岔状态发送给邻站CI，相邻CI间道岔索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.1的表4；3) 本CI应将互联互通相关范围内的本联锁区管辖范围内的物理区段状态发送给邻站CI。相邻CI间物理区段索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.2的表5；4) 本CI应将互联互通相关范围内的本联锁区管辖范围的逻辑区段状态发送给邻站CI，相邻CI间逻辑区段索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.3的表6；5) 本CI应将互联互通相关范围内的本联锁区管辖范围内的信号机状态发送给邻站CI，联锁分界点处信号机属于</td></tr></table>

---

<div style="text-align: center;">表 161 CI 与 CI 接口描述(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口描述</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>接车方联锁管辖，若联锁分界点有外置保护区段，则发车方联锁也应向接车方联锁发送该信号机状态信息。若联锁分界点无外置保护区段，则发车方联锁不发该信号机状态信息。相邻CI间信号机索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.4的表7；6)本CI将互联互通相关范围内的本联锁区管辖范围的站台门状态信息发送给邻站CI。相邻CI间站台门索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.5的表8；7)本CI将互联互通相关范围内的本联锁区管辖范围的站台紧急关闭信息发送给邻站CI。相邻CI间站台紧急关闭索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.6的表9；8)本CI将互联互通相关范围内的本联锁区管辖范围的照查状态信息发送给邻站CI。相邻CI间照查索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.7的表10；9)本CI将互联互通相关范围内的本联锁区管辖范围的防淹门信息发送给邻站CI。相邻CI间防淹门索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.8的表11；10)本CI将本站上电锁闭状态信息发送给邻站CI，详见T/CAMET 04011.5章节5.4.9的表12；11)本CI应将互联互通相关范围内的本联锁管辖范围的临时限速区段状态发送给邻站CI。相邻CI间临时限速区段索引顺序应保持一致，详见T/CAMET 04011.5章节5.4.10的表13</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>针对道岔的测试需求：1)分别对道岔做引导总锁、单锁、封锁、单操定位、单操反位、道岔四开的操作，验证临站联锁显示同本站联锁一致；并验证未对道岔做任何设置时，临站联锁显示同本站联锁显示一致；2)通过相关操作使计轴区段状态为占用、封锁、区段锁闭、防护锁闭、某一锁闭方向，验证临站联锁显示同本站联锁</td></tr></table>

---

<div style="text-align: center;">表 161 CI 与 CI 接口描述(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI与CI接口描述</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>显示一致；并验证使计轴区段处于空闲且未封锁和未锁闭状态时，临站联锁显示同本站联锁显示一致；3)操作逻辑区段使其状态为CT车占用、UT车占用、设置/取消临时限速，区段封锁、区段进路锁闭、区段保护锁闭、某一锁闭方向，验证临站联锁显示同本站联锁一致；并验证使逻辑区段处于空闲且未封锁和未锁闭状态时，临站联锁显示与本站联锁显示一致；4)操作信号机使其状态分别为红灯、黄灯、绿灯、红黄灯、灯丝断丝、封锁、未封锁，验证临站联锁显示同本站联锁一致；5)操作站台门使其处于开门或关门、旁路或未旁路的状态，验证临站联锁显示同本站联锁一致；6)操作站台紧急关闭按钮使其处于按下或未按下的状态，验证临站联锁显示同本站联锁一致；7)操作使照有条件处于照查条件满足或照查条件不满足的状态，验证临站联锁显示与本站联锁一致；8)进路：跨站进路在分界点处会设置虚拟或实体信号机，营造条件使接车站进路满足接近锁闭条件，验证发车站联锁会向接车站联锁发送接近锁闭信息；否则发送未接近锁闭信息；9)保护区段：当发车站最后一条主进路锁闭完成及保护区段建立的触发区段占用条件满足时，验证发车站联锁向接车站联锁发送保护区段请求，否则不发送；10)操作使联锁处于上电锁闭或上电解锁状态，验证临站联锁显示与本站联锁一致</td></tr></table>

### 6.7 互联互通跨线 ATS 间接口测试需求

#### 6.7.1 ATS 与 ATS 通信机制

ATS 与 ATS 通信机制功能的测试和验证方法详见表 162。

---

<div style="text-align: center;">表 162 ATS 与 ATS 通信机制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1) 相邻 ATS 间通信采用周期与非周期发送的方式进行通信。2) 通信双方均采用大端字节序进行数据传输</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.2 ATS 与 ATS 接口概述

ATS 与 ATS 接口描述功能的测试和验证方法详见表 163。

表 163 ATS 与 ATS 接口


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次结构描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS间通信层次结构划分详见TCAMET 04011.6章节5.2.1图1。物理层采用IEEE802.3标准协议，数据链路层采用IEEE802.3标准协议，网络层采用IPv4协议，传输层采用TCP协议，应用层见TCAMET 04011.6章节5.2.3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.3 物理接口

物理接口功能的测试和验证方法详见表 164。

<div style="text-align: center;">表 164 物理接口</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS通过RJ45接口冗余接入通信网络，网络拓扑结构为A网-A网，B网-B网，接口间宜通过防火墙进行隔离</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.7.4 通信层次描述

通信层次描述功能的测试和验证方法详见表 165。

<div style="text-align: center;">表 165 通信层次描述</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次描述</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与ATS间建立对等的逻辑连接，详见T/CAMET 04011.6章节5.2.2.2图2（箭头指向表示服务端，双线表示双网逻辑连接）：1)第一组通道，线路一ATS的主机作为客户端同时与线路二ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。2)第二组通道，线路二ATS的主机作为客户端同时与线路一ATS的主机和备机建立双网连接，用于传送本线路内产生的信息。服务端侦听端口为9900</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.5 信息帧格式定义

信息帧格式定义功能的测试和验证方法详见表166。

<div style="text-align: center;">表 166 信息帧格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息帧格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>相邻 ATS 间每个周期需要交互的信息通过组成通用（GAL）消息包（以下简称 GAL 包），进行传输，详见 T/CAMET 04011.6 章节 5.2.2.3 图 3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.6 信息包格式定义

信息包格式定义功能的测试和验证方法详见表 167 ~ 表 171。

---

<div style="text-align: center;">表 167 信息包格式定义（一）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS间通信的GAL包中包含ATS间传输的各条应用信息，每个GAL消息包总长不得超过65000字节，每个GAL只包含一类应用数据。GAL包格式定义详见T/CAMET 04011.6章节5.2.2.3.2表1和表2</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 168 信息包格式定义(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——合法性检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站ATS的应用信息，并记录报警信息。具体检查方式如下：消息内容的一致性检查包括：信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。通用应用(GAL)信息包消息所应包含的信息的完整性。其他逻辑检查</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 169 信息包格式定义（三）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS和V0BC应能分别对通信连接状态进行判断： ATS认为与邻站ATS通信中断的超时时间定义为 TATSTimeout(3s~9s,可配置)。 若ATS在TATSTimeout超时时间内,没有接收到来自邻站ATS的任何消息,则ATS应认为与邻站ATS通信中断。</td></tr></table>

---

<div style="text-align: center;">表 169 信息包格式定义（一）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>若 ATS 判断接收到邻站 ATS 的周期性应用信息延迟已经达到 TATSTimeout 时，ATS 可丢弃此信息包，ATS 应认为与邻站 ATS 通信中断或发生丢包。通信中断的情况下，应生成报警信息。连接断开时立即重连。联互通线网中，各厂商的 ATS 间的通信超时时间应一致，消息有效期时间应一致</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>断开相邻 ATS 与 ATS 间通信，并超过系统定义的 TATSTimeout，ATS 系统判断为与相邻 ATS 通信超时；断开 ATS 和相邻 ATS 主机之间的通信连接持续一段时间未恢复，进行倒机切换；断开 ATS 与相邻 ATS 备机与备机之间的通信连接，只报警而不倒机；断开 ATS 与相邻 ATS 主机与备机之间的通信连接，只报警而不倒机</td></tr></table>

<div style="text-align: center;">表 170 信息包格式定义（四）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-9</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET 04011.6章节5.2.3.1表3</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 171 数据交互方式定义（五）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据交互方式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>T/CAMET 04011.6 章节 5.2.3.2 图 4 表明了两个线路 ATS 间互传的数据流（箭头方向表示数据流向），具体定义如下：</td></tr></table>

---

<div style="text-align: center;">表 171 数据交互方式定义(五)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据交互方式定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)A为本线路的列车运行调整信息；2)B为本线路的站场显示信息、列车信息、接入站跳停命令及回执；3)C为心跳信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.7 应用信息定义

应用信息定义功能的测试和验证方法详见表 172。


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>BTC-IF-ATS/ATS-MSC-ITC-IT</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>协议中的“无效”值：正常通信时发送方不可能发送的非法取值。接收方收到GAL包中的应用信息包中存在“无效”值时，应对GAL包应用信息包中无效字段进行错误处理。协议中的“默认”值：针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；设备在初始化完成前，无法确定状态时，相关字段取值发送“默认”值。接收方收到“默认”值后，应认为信息有效，不进行处理。协议中涉及“上行”“下行”的方向定义，均采用运营方向规定的上下行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.7.8 心跳信息包

心跳信息包功能的测试和验证方法详见表 173。

<div style="text-align: center;">表 173 心跳信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>心跳报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-12</td></tr></table>

---

<div style="text-align: center;">表 173 心跳信息包(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>心跳报文</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS 应周期性发送心跳信息，具体格式同应用信息包为0 的 GAL包</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送心跳报文</td></tr></table>

#### 6.7.9 站场显示信息包

站场显示信息包功能的测试和验证方法详见表174。

<div style="text-align: center;">表 174 站场显示信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>站场显示信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-13</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS 应周期性将复视车站的所有站场表示信息发送给相邻线 ATS。站场显示信息包详见 T/CAMET 04011.6 章节 5.2.3.3.3 表 4</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送跨线显示区域的站场信息</td></tr></table>

#### 6.7.10 列车信息包

列车信息包功能的测试和验证方法详见表175。

<div style="text-align: center;">表 175 列车信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS 应周期性将复视车站的所有列车状态信息发送给相邻线 ATS，详见 T/CAMET 04011.6 章节 5.2.3.3.4 表 5</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送跨线显示区域的列车信息</td></tr></table>

#### 6.7.11 列车运行调整信息包

列车运行调整信息包功能的测试和验证方法详见表176。

---

<div style="text-align: center;">表 176 列车运行调整信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车运行调整信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对于跨线列车，线路 ATS 间应周期性互传各自线路内跨线运营分界处交出车站的计划运行图/时刻表、实迹运行图/时刻表和计划调整信息。列车运行调整信息包定义详见 T/CAMET 04011.6 章节 5.2.3.3.5 表 6</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>ATS 系统周期向相邻 ATS 发送跨线显示区域的列车运行调整相关信息</td></tr></table>

#### 6.7.12 列车接入站跳停命令信息包

列车接入站跳停命令信息包功能的测试和验证方法详见表177。

<div style="text-align: center;">表 177 列车接入站跳停命令信息包(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停命令信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对跨线列车，当在接入线接入站（人工或自动）设置跳停时，由接入线ATS发送站台跳停命令至交出线ATS，交出线ATS收到跳停命令后，发送接收回执给接入站ATS，由交出站ATS负责管理接入站台的跳停命令，确定将命令发送至列车的时机，回执超时时重发N次后报错，并停止发送（重发次数、超时时间可配置）。列车接入站跳停命令信息包定义详见T/CAMET 04011.6章节5.2.3.3.6表7</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>接入线ATS系统周期向移交ATS发送跨线区域的列车跳停信息</td></tr></table>

#### 6.7.13 列车接入站跳停回执信息包

列车接入站跳停回执信息包功能的测试和验证方法详见表178。

<div style="text-align: center;">表 178 列车接入站跳停回执信息包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停回执信息包</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-17</td></tr></table>

---

<div style="text-align: center;">表 178 列车接入站跳停回执信息包(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车接入站跳停回执信息包</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对跨线列车，当接入线接入站站台设置跳停时，交出线 ATS 收到接入站发送的接入站站台跳停命令信息包后回复接收回执。列车接入站跳停回执信息包的定义详见 T/CAMET 04011.6 章节 5.2.3.3.7 表 8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>移交线 ATS 系统向接入线 ATS 发送跨线区域的列车跳停信息包回执信息</td></tr></table>

#### 6.7.14 ATS 城市自定义帧

ATS 城市自定义帧功能的测试和验证方法详见表 179。

<div style="text-align: center;">表 179 ATS 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能，具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统向相邻ATS发送城市自定义帧；2) 依据城市需求测试</td></tr></table>

#### 6.7.15 ATS厂商自定义帧

ATS 厂商自定义帧功能的测试和验证方法详见表 180。

<div style="text-align: center;">表 180 ATS 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-ATS/ATS-MSG-ITC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，ATS收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) ATS系统向相邻ATS发送厂商自定义帧；2) 依据厂商功能定义测试</td></tr></table>

---

### 6.8 互联互通车地通信接口(VOBC 和 ATS) 测试需求

#### 6.8.1 概述

VOBC 与 ATS 之间采用冗余网络进行通信。ATS 与 VOBC 之间的网络拓扑结构采用 A 网-A 网，B 网-B 网两个链路。VOBC 和 ATS 的通信主要用于列车的运行调整控制（在点式级别下不对基于 VOBC-ATS 通信的运行调整功能做强制要求，各供应商依据各自系统功能进行测试和验证）。

#### 6.8.2 物理接口

物理接口功能的测试和验证方法详见表181。

<div style="text-align: center;">表 18.1 物理接口</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITG-1</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与ATS之间采用冗余网络进行通信。ATS与V0BC之间的网络拓扑结构采用A网-A网，B网-B网两个链路</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.3 安全通信协议

安全通信协议功能的测试和验证方法详见表182。

<div style="text-align: center;">表 182 安全通信协议</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS与V0BC之间通信采用RSSP-Ⅱ安全通信协议。安全通信协议的具体要求参见《RSSP-Ⅱ铁路信号安全通信协议》(运基信号[2010]267号)。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。</td></tr></table>

---

<div style="text-align: center;">表 182 安全通信协议(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>RSSP-Ⅱ安全通信协议架构详见T/CAMET 04011.2章节6.1.2图6，其SAI/MASL/ALE三层，遵循RSSP-Ⅱ标准规定。1) TCP及IP层使用标准TCP/IP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。RSSP-Ⅰ安全通信协议架构详见T/CAMET 04011.2章节6.1.2图7，协议遵循RSSP-Ⅰ标准规定。1) UDP层使用标准UDP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.4 动态交互描述

动态交互描述功能的测试和验证方法详见表183～表186。

<div style="text-align: center;">表 183 动态交互描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>消息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-3</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>将ATS-V0BC间每个周期需要交互的应用信息通过组成通用消息包进行传输详见T/CAMET 04011.2章节6.1.3图8</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 184 动态交互描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-4</td></tr></table>

---

<div style="text-align: center;">表 184 动态交互描述(二)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS/V0BC 每周期最多允许发送 1 个通用消息包，通用消息包中包含 ATS 与 V0BC 之间传输的各条应用信息。每个通用消息包总长不得超过 1000 字节，格式的定义详见 T/CAMET 04011.2 章节 6.1.3.2 表 15 和表 16</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>测试接口内容：电子地图版本控制信息。对应的测试需求如下：1) 上电/进入线路时，车载设备默认采用版本较低的电子地图版本号；2) 车载设备与地面设备建立连接后，发送的通用消息包中为当前采用的电子地图版本号；3) 地面设备判断收到的通用信息包中车载电子地图版本号是否与地面一致，若一致，则进行正常通信，若不一致，则发送应用内容为空的通用消息包，通知车载设备地面电子地图版本号；4) 若车载设备收到空通用消息包，则判断本地是否存有与地面版本一致的电子地图，若有，则采用与地面版本一致的电子地图，继续与地面设备通信，通用消息包中的电子地图版本号与地面版本一致；否则，断开与地面设备的通信；5) 其他见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 185 动态交互描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——合法性检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>ATS及V0BC应分别对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方面的应用信息，并记录报警信息。具体检查方式如下：消息内容的一致性检查包括：信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。通用应用(GAL)信息包消息所应包含的信息的完整性。其他逻辑检查</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 186 动态交互描述(四)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1. ATS 和 V0BC 应能分别对通信连接状态进行判断：1) ATS 认为与 V0BC 通信中断的超时时间定义为 TAtsTimeout（可配置，推荐值：6 s）；2) V0BC 认为与 ATS 通信中断的超时时间定义为 TVobcTimeout（可配置，推荐值：6 s）；3) 若 ATS 在 TAtsTimeout 超时时间内，没有接收到来自 V0BC 的任何消息，则 ATS 应认为与 V0BC 的通信中断；4) 若 ATS 判断收到 V0BC 的 GAL 包延迟已经达到 TAtsTimeout，则 ATS 应丢弃此 GAL 包或认为与 V0BC 通信中断；5) 若 V0BC 在 TVobcTimeout 超时时间内，没有接收到来自 ATS 的任何消息，则 V0BC 应认为与 ATS 的通信中断；6) 若 V0BC 判断收到 ATS 的 GAL 包延迟已经达到 TVobcTimeout，则 V0BC 应丢弃此 GAL 包或认为与 ATS 通信中断；7) 通信中断的情况下，应生成报警信息；8) 互联互通线网中，各厂商的 V0BC 与各条线路上的 ATS 的通信超时时间应一致，消息有效期时间应一致。2. 列车在两 ATS 间移交时，V0BC 判断列车最小安全后端越过 ATS 边界点后，应与移交 ATS 断开通信。3. V0BC 判断与 ATS 断开通信，且不再与该 ATS 重新建立通信后，应断开与该 ATS 的 TCP/IP 或 UDP 连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 断开相邻 V0BC 与 ATS 间通信，并超过系统定义的 TAtsTimeout，ATS 系统判断为与 V0BC 通信超时；2) 断开相邻 V0BC 与 ATS 间通信，并超过系统定义的 TVobcTimeout，V0BC 系统判断为与 ATS 通信超时</td></tr></table>

#### 6.8.5 通信故障处理

通信故障处理功能的测试和验证方法详见表187。

---

<div style="text-align: center;">表 187 通信故障处理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议 RSSP-Ⅱ 安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。车地无线通信双方（ATS-V0BC）应用层的通信故障处理分为如下几种情况：ATS 和 V0BC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息。通信中断的情况下处理，若 ATS/V0BC 认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>设备厂商设计文件</td></tr></table>

#### 6.8.6 数据类型定义

数据类型定义功能的测试和验证方法详见表188。

<div style="text-align: center;">表 188 数据类型定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-8</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本条对ATS与V0BC之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，详见T/CAMET04011.2章节6.3.1表17</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.7 应用信息定义

应用信息定义功能的测试和验证方法详见表189

<div style="text-align: center;">表 189 应用信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-9</td></tr></table>

---

<div style="text-align: center;">表 189 应用信息定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>协议中的“非法”值：正常通信时发送方不可能发送的非法取值。接收方收到GAL包中的应用信息帧中存在“非法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认为本周期未收到数据。 协议中的“默认”值：(1)针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；(2)设备在初始化完成前，无法确定状态时，相关字段取值发送“默认值”。接收方收到“默认”值后，应认为信息有效，不进行处理。 协议中涉及“上行”“下行”的方向定义，均采用运营方向规定的上行和下行</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.8.8 ATS 至 VOBC 心跳报文

ATS 至 VOBC 心跳报文功能的测试和验证方法详见表 190.

<div style="text-align: center;">表 190 ATS 至 VOBC 心跳报文</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS至VOBC心跳报文</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-ITC-10</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>周期发送，用来维持ATS设备和VOBC间通信链路的连续性。ATS至VOBC心跳帧详见T/CAMET 04011.2章节6.3.2.2.1表18</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在具备连续通信通道的前提下，ATS系统周期向点式列车发送心跳报文</td></tr></table>

#### 6.8.9 ATS 至 VOBC 命令信息帧

ATS 至 VOBC 命令信息帧功能的测试和验证方法详见表 191。

<div style="text-align: center;">表 191 ATS 至 VOBC 命令信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS 至 VOBC 命令信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-ITC-11</td></tr></table>

---

<div style="text-align: center;">表 191 ATS 至 VOBC 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS至V0BC命令信息帧</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>各厂商ATS各自按照自身时机向V0BC发送ATO命令信息帧，由V0BC适配。可能的发送时机包括：1)当ATS设备所管辖范围内有被控列车，且列车最大安全前端处于站台区域、转换轨或折返轨时，ATS应周期向该V0BC发送ATO命令信息；2)通信过程中，周期发送。ATS至V0BC命令信息帧定义详见T/CAMET 04011.2章节6.3.2.2.2表19</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1. 测试接口内容：下一ZC ID、下一CI ID、下一ATS ID。对应的测试需求如下：1)对于计划列车ATS向列车发送下一ZC ID，在具备条件时，列车根据此ID呼叫相应的ZC；否则，发送默认值；2)对于计划列车ATS向列车发送下一CI ID，在具备条件时，列车根据此ID呼叫相应的CI；否则，发送默认值；3)对于计划列车ATS向列车发送下一ATS ID，在具备条件时，列车根据此ID呼叫相应的ATS；否则，发送默认值。2. 测试接口内容：服务号/表号、线路编号、车组所属线路号、车组号、源线路号、车次号、目的地线路号、目的地号、计划运行方向。对应的测试需求：计划车/非计划车，检查ATS向ATO发送的命令信息帧中上述内容正确。3. 测试接口内容：跳停站台ID、下一停车站台ID、下一站跳停命令。对应的测试需求如下：1)设置跳停命令，列车位置在跳停命令接收范围内。列车将依据命令在跳停车站停车；2)设置跳停命令，列车位置在跳停命令接收范围外；列车将继续在已设置跳停的站台执行停站操作；3)取消跳停命令，列车位置在命令接收范围内。列车将依据命令在取消跳停车站停车；4)取消跳停命令，列车位置在命令接收范围外。列车将继续跳停已设置取消跳停的站台。注：对于各厂家命令设置的范围依据协议中定义进行测试。</td></tr></table>

---

<div style="text-align: center;">表 191 ATS 至 VOBC 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS至VOBC命令信息帧</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>4. 测试接口内容：站停时间、区间运行调整命令。对应的测试需求：列车进入站台，收到ATS发送的站停时间命令和区间运行调整命令，在站台停准停稳，打开车门，到达站停时间后，关闭车门，驶出站台，在区间按照收到的运行等级或区间运行时间行驶。5. 测试接口内容：扣车命令。对应的测试需求：列车最大安全前端所在站台有扣车命令，ATS发送“扣车有效”，列车执行扣车命令，否则发送“扣车取消，无扣车”。6. 测试接口内容：折返命令。对应的测试需求：对于计划列车，列车最大安全前端在站台内时，ATS按照列车运行计划判断列车是否要进行折返，并发送响应的站前折返、有人站后折返、无人自动折返命令；对于非计划列车或与ATS无通信的列车，ATS向列车发送“不折返”命令，列车根据车载电子地图存储的区段属性显示折返提示。7. 测试接口内容：回段指示。对应的测试需求如下：1) VOBC与ATS通信正常：当列车最大安全前端在转换轨内且列车为回段方向时，对于计划列车，ATS根据列车运行计划，向VOBC发送“回段”或“不回段”指示，列车在转换轨内进行相应的显示；对于非计划列车，ATS向VOBC发送默认值。当列车最大安全前端不在转换轨内或列车不为回段方向时，ATS向VOBC发送的“回段指示”字段为默认值。2) VOBC与ATS断开：VOBC与ATS通信断开或收到的回段提示字段为默认值时，根据电子地图配置的区段属性，在转换轨内显示回段提示。8. 测试接口内容：门控策略。对应的测试需求如下：1) 站台为单侧门时，发送ATS中配置的默认值；2) 站台为双侧门时，发送相应的门控策略；同时开双侧门、先开左门再开右门、先开右门再开左门；</td></tr></table>

---

#### 6.8.10 ATS 城市自定义帧

ATS 城市自定义帧功能的测试和验证方法详见表 192。

<div style="text-align: center;">表 192 ATS 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATS城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-12</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在具备连续通信通道的前提下，ATS系统周期向点式列车发送城市自定义帧；2)点式列车不做强制要求；3)依据城市需求测试</td></tr></table>

#### 6.8.11 ATS厂商自定义帧

ATS厂商自定义帧功能的测试和验证方法详见表193。

193 ATS厂商自定义帧


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>市轨道ATS厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-14</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能，各厂商分别定制，V0BC收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在具备连续通信通道的前提下，ATS系统周期向点式列车发送厂商自定义帧；2)点式列车不做强制要求；3)依据厂商功能定义测试</td></tr></table>

#### 6.8.12 ATO 状态信息帧

ATO 状态信息帧功能的测试和验证方法详见表 194。

---

<div style="text-align: center;">表 194 ATO 状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>ATO状态信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-15</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>若已建立ATO模式，V0BC应周期向ATS发送ATO状态信息。ATS需针对每列车的ATO状态信息进行超时判断，配置时间内未收到相应列车的ATO状态信息，则清除该车的ATO状态信息。ATO状态信息帧定义详见T/CAMET 04011.2章节6.3.2.3.1表22</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在具备连续通信通道的前提下，ATO系统周期向ATS发送状态信息帧（点式列车不做强制要求）</td></tr></table>

#### 6.8.13 列车信息帧

列车信息帧功能的测试和验证方法详见表195。

<div style="text-align: center;">表 195 列车信息帧(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>列车信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-16</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>本消息为周期信息，当V0BC与ATS之间的安全连接建立后，周期发送。列车信息帧定义详见T/CAMET 04011.2章节6.3.2.3.2表23和表24</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在具备连续通信通道的前提下，V0BC周期向ATS发送列车信息帧（点式列车不做强制要求）</td></tr></table>

#### 6.8.14 车载设备报警信息帧

车载设备报警信息帧功能的测试和验证方法详见表196。

<div style="text-align: center;">表 196 车载设备报警信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载设备报警信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-17</td></tr></table>

---

<div style="text-align: center;">表 196 车载设备报警信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载设备报警信息帧</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载设备报警信息帧定义详见 T/CAMET 04011.2 章节 6.3.2.3.3 表 25</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在具备连续通信通道的前提下，V0BC 周期向 ATS 发送车载报警信息帧（点式列车不做强制要求）</td></tr></table>

#### 6.8.15 车载设备日检信息帧

车载设备日检信息帧功能的测试和验证方法详见表197。

<div style="text-align: center;">表 197 车载设备日检信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>车载设备日检信息帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/ATS-MSG-ITC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>车载设备日检信息帧定义详见T/CAMET 04011.2章节 6.3.2.3.4表26</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>在具备连续通信通道的前提下，V0BC向ATS发送车载日检信息帧（点式列车不做强制要求）</td></tr></table>

#### 6.8.16 VOBC 城市自定义帧

V0BC 城市自定义帧功能的测试和验证方法详见表 198。

<div style="text-align: center;">表 198 VOBC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-ITC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在具备连续通信通道的前提下，VOBC向ATS发送城市自定义帧；2)点式列车不做强制要求；3)依据城市需求测试</td></tr></table>

---

#### 6.8.17 VOBC 厂商自定义帧

V0BC厂商自定义帧功能的测试和验证方法详见表199。

<div style="text-align: center;">表 199 VOBC 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/ATS-MSG-ITC-20</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，ATS收到非本厂商的厂商自定义帧后，可不进行处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)在具备连续通信通道的前提下，VOBC向ATS发送厂商自定义帧；2)点式列车不做强制要求；3)依据厂商功能定义测试</td></tr></table>

### 6.9 互联互通车地通信接口(VOBC 和 CI) 测试需求

#### 6.9.1 概述

6.9.1.1 VOBC 和 CI 是通过双路冗余的无线网络，基于 TCP/IP 协议（传输层）进行通信的。VOBC 和 CI 的通信主要用于站台安全门 PSD 的控制。

6.9.1.2 CI 将 VOBC 所在站台的出站信号机状态发送给车载 VOBC，如出站信号机为红灯，则车载应提供闯红灯防护功能。

#### 6.9.2 接口连接方式

接口连接方式描述功能的测试和验证方法详见表200和表201。

<div style="text-align: center;">表 200 物理接口</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>物理接口</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-I</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>VOBC与CI之间采用冗余网络进行通信.CI与VOBC之间的网络拓扑结构采用A网-A网和B网-B网两个链路进行连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

<div style="text-align: center;">表 201 安全通信协议</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>安全通信协议</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-2</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI与V0BC之间通信可采用RSSP-Ⅱ或RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议的具体要求参见《RSSP-Ⅱ铁路信号安全通信协议》（运基信号[2010]267号）；RSSP-Ⅰ安全通信协议的具体要求参见《RSSP-Ⅰ铁路信号安全通信协议》（运基信号[2010]267号）。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信口LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议架构详见T/CAMET04011.2章节7.1.2图10，其SAL/MASL/ALE三层，遵循RSSP-Ⅱ标准规定。1) TCP层使用标准TCP/IP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。RSSP-Ⅰ安全通信协议架构详见T/CAMET04011.2章节7.1.2图11，其RSSP-Ⅰ协议遵循RSSP-Ⅰ标准规定。1) UDP层使用标准UDP协议栈；2) MAC及PHY层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.3 动态交互描述

动态交互描述功能的测试和验证方法详见表202～表204。

<div style="text-align: center;">表 202 动态交互描述(一)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-3</td></tr></table>

---

<div style="text-align: center;">表 202 动态交互描述(一)(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>信息包格式定义</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI/V0BC每周期最多允许发送1个消息包，包中包含CI 与V0BC之间传输的应用信息，每个GAL消息包总长不得 超过1000字节，格式定义详见T/CAMET 04011.2章节 7.1.3.2表29和表30</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 203 动态交互描述(二)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——合法性检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI应对接收到的V0BC的应用消息进行合法性检查，若检查未通过，认为本周期未收到对等方面的应用信息。具体检查方式如下：消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。消息所应包含的信息的完整性</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

<div style="text-align: center;">表 204 动态交互描述(三)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-5</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>CI和V0BC应能分别对通信连接状态进行判断：1)CI认为与V0BC通信中断的超时时间定义为TCiTimeout(可配置，推荐值为6s)；2)V0BC认为与CI通信中断的超时时间定义为TVobcTimeout(可配置，推荐值为6s)；3)若CI在TCiTimeout超时时间内，没有接收到来自V0BC的任何消息，则CI应认为与V0BC的通信中断；4)若V0BC在TVobcTimeout超时时间内，没有接收到来自CI的任何消息，则V0BC应认为与CI的通信中断；</td></tr></table>

---

<div style="text-align: center;">表 204 动态交互描述（三）（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信状态管理——超时检查</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>5) 若 CI 判断接收到 VOBC 的应用信息延迟已经达到 TC\Timeout 时，CI 应丢弃此信息包或认为与 VOBC 通信中断；6) 若 VOBC 判断接收到 CI 的应用信息延迟已经达到 TVobc\Timeout 时，VOBC 应丢弃此信息包或认为与 CI 通信中断。互联互通线网中，车载设备与各条线路上的联锁设备的通信超时时间应一致，消息有效期时间应一致。VOBC 在与 CI 设备通信时，当判断与 CI 设备通信断开并且不再与对方建立连接后，应断开与 CI 设备的 TCP/IP 连接</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1) 断开相邻 VOBC 与 CI 间通信，并超过系统定义的 TC\Timeout，CI 系统判断为与 VOBC 通信超时；2) 断开相邻 VOBC 与 CI 间通信，并超过系统定义的 TVobc\Timeout，VOBC 系统判断为与 CI 通信超时</td></tr></table>

#### 6.9.4 通信故障处理

通信故障处理功能的测试和验证方法详见表205。

<div style="text-align: center;">表 205 通信故障处理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-6</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。 
 山地无线通信双方（CI-V0BC）应用层的通信故障处理分为如下几种情况： 
 1) CI 和 V0BC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息；</td></tr></table>

---

<div style="text-align: center;">表 205 通信故障处理(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信故障处理</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>2)通信中断的情况下处理:若CI/V0BC认为与对等方 应用层通信超时中断,采取主动释放安全连接的方式进行 处理; 3)其他风险由安全通信协议完成防护处理</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.5 通信体系结构

通信体系结构功能的测试和验证方法详见表206。

<div style="text-align: center;">表 206 通信体系结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信层次划分</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-7</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>V0BC与CI通信协议模型详见T/CAMET 04011.2章节7.2.1图13</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.6 通信机制

通信机制功能的测试和验证方法详见表207。

<div style="text-align: center;">表 207 通信机制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>通信机制</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-I4</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>1)仅能由V0BC发起安全连接的建立过程；2)CI与V0BC采用周期发送和消息触发的方式进行通信；3)通信双方均采用大端字节序进行数据传输；4)CI与V0BC均应对接收的应用信息进行判断和逻辑运算</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.9.7 应用信息定义

应用信息定义功能的测试和验证方法详见表 208。

<div style="text-align: center;">表 208 应用信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>应用信息定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-18</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>VOBC在列车进出站过程中，给CI发送信息控制站台门的打开和关闭 VOBC至CI的信息周期发送（发送周期按照各方发送方周期定义，对通信周期范围定义为200ms~1000ms），CI接收到信息后向VOBC发送对应PSD的状态信息。对于每列允许两侧开门的站台，系统将两侧的PSD当作两个不同的设备分别控制，为两侧的PSD分别分配全局唯一的标识（即整列的PSD当作一个设备，系统为其分配全局唯一的ID）。文中未做特殊说明的上下行定义均为线路规定的运营上下行方向</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>具备厂商设计文件</td></tr></table>

#### 6.9.8 数据类型定义

数据类型定义功能的测试和验证方法详见表209。

<div style="text-align: center;">表 209 数据类型定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>数据类型定义</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-19</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>对 V0BC 与 CI 之间通信的所有应用信息类型及其含义、 发送方向、长度范围、发送方式（周期/非周期）进行定义，详 见 T/CAMET 04011.2 章节 7.3.1 表 31</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.9.9 VOBC 向 CI 发送心跳帧

V0BC 向 CI 发送心跳帧功能的测试和验证方法详见表 210。

<div style="text-align: center;">表 210 VOBC 向 CI 发送心跳帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC向CI发送心跳帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-20</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在列车车头最大安全前端进入CI通信区段前发送该信息包（具体时机各厂商自定义），用来维持VOBC设备和CI间通信链路的连续性。列车车头最大安全前端进入CI通信区段后，开始发送控制信息时不再发送心跳帧。VOBC向CI发送心跳帧定义详见T/CAMET 04011.2章节7.3.2.2.1表32</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.10 VOBC 向 CI 发送控制信息

V0BC 向 CI 发送控制信息功能的测试和验证方法详见表 211。

<div style="text-align: center;">表 211 VOBC 向 CI 发送控制信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC向CI发送控制信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-21</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>从列车车头最大安全前端进入CI通信区段开始，直至列车最大安全前端离开CI通信区段前，发送该信息包V0BC至CI输出信息接口表详见T/CAMET 04011.2章节7.3.2.2.2表33，应用层报文长度固定，全线站台门的编号方式应有共同的规则和相应的说明文件</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)站台区域具备连续通信条件；2)点式级别列车进站对标停车（跨线列车）；3)进行开关车门操作，站台门开关时机和一致性（包括方向和数量）符合设计要求</td></tr></table>

---

#### 6.9.11 VOBC 向 CI 发送城市自定义帧

V0BC 向 CI 城市发送自定义帧功能的测试和验证方法详见表 212。

<div style="text-align: center;">表 212 VOBC 向 CI 发送城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC向CI发送城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-22</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各城市特有的互联互通相关功能：具体内容在工程中根据实际需求约定，各厂商均应实现相应功能，详见T/CAMET 04011.2章节7.3.2.2.3表35</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.12 VOBC 向 CI 发送厂商自定义帧

VOBC 向 CI 发送厂商自定义帧功能的测试和验证方法详见表 213。

<div style="text-align: center;">表 213 VOBC 向 CI 发送厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>VOBC向CI向送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-23</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同一厂商时方可发送，详见T/CAMET 04011.2章节7.3.2.2.4表36</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.13 VOBC 向 CI 发送注销请求帧

V0BC 向 CI 发送注销请求帧功能的测试和验证方法详见表 214。

<div style="text-align: center;">表 214 VOBC 向 CI 发送注销请求帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC 向 CI 发送注销请求帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-24</td></tr></table>

---

<div style="text-align: center;">表 214 VOBC 向 CI 发送注销请求帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>V0BC向CI发送注销请求帧</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在列车判断需要与CI断开通信时，V0BC向CI发送注销信息，直至V0BC收到CI回复的注销信息，或者V0BC判断通信超时。V0BC发送的“注销请求”包、“控制信息”包、“心跳”包在同一GAL包中不应同时存在。V0BC向CI注销请求帧定义详见T/CAMET 04011.2章节7.3.2.2.5表37</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.14 CI 向 VOBC 发送心跳帧

CI 向 VOBC 发送心跳帧功能的测试和验证方法详见表 215.

<div style="text-align: center;">表 215 CI 向 VOBC 发送心跳帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向VOBC发送心跳帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-VOBC/CI-MSG-ITC-25</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>当CI与VOBC建立链接后，且尚未收到VOBC=&gt;CI控制信息之前，发送该信息包，用来维持VOBC设备和CI间通信链路的连续性。CI向VOBC发送心跳帧的定义详见T/CAMET 04011.2章节7.3.3.1表38</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.15 CI 向 VOBC 发送状态信息

CI 向 VOBC 发送状态信息功能的测试和验证方法详见表 216。

<div style="text-align: center;">表 216 CI 向 VOBC 发送状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送状态信息</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-26</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>当CI收到V0BC的控制信息之后，发送该信息包：CI至V0BC输出信息接口表详见T/CAMET 04011.2章节7.3.3.2表39</td></tr></table>

---

<div style="text-align: center;">表 216 CI 向 VOBC 发送状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送状态信息</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>1)站台区域具备连续通信条件；2)点式级别列车进站对标停车并结束停站作业且具备发车条件（跨线列车）；3)操作出站信号（关闭和开放），列车具备红灯误出发防护功能；4)列车可以正确接收到站台门的状态信息（打开/关闭/互锁解除）</td></tr></table>

#### 6.9.16 CI 向 VOBC 发送城市自定义帧

CI 向 VOBC 发送城市自定义帧功能的测试和验证方法详见表 217。

<div style="text-align: center;">表 217 CI 向 VOBC 发送城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送城市自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-JE-V0BC/CI-MSG-ITC-27</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息用于实现各城市现有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能，详见T/CAMET 04014.2章节7.3.3.3表40</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

#### 6.9.17 CI 向 VOBC 发送厂商自定义帧

CI 向 VOBC 发送厂商自定义帧功能的测试和验证方法详见表 218。

<div style="text-align: center;">表 218 CI 向 VOBC 发送厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送厂商自定义帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-28</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>自定义信息，用于实现各厂商特有功能。各厂商分别定制，V0BC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同一厂商时方可发送，详见T/CAMET 04011.2章节7.3.3.4表41</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

---

#### 6.9.18 CI 向 VOBC 发送注销回复帧

CI 向 VOBC 发送注销回复帧功能的测试和验证方法详见表 219。

<div style="text-align: center;">表 219 CI 向 VOBC 发送注销回复帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能名称</td><td style='text-align: center;'>CI向V0BC发送注销回复帧</td></tr><tr><td style='text-align: center;'>测试需求编号</td><td style='text-align: center;'>CBTC-IF-V0BC/CI-MSG-ITC-29</td></tr><tr><td style='text-align: center;'>功能内容</td><td style='text-align: center;'>在CI接收到V0BC的注销请求帧后，向V0BC回复注销回复帧。CI发送的“注销回复”包、“状态信息”包、“心跳”包在同一GAL包中不应同时存在。CI向V0BC输出信息接口表详见T/CAMET 04011.2章节7.3.3.5表42</td></tr><tr><td style='text-align: center;'>测试需求</td><td style='text-align: center;'>见各厂商设计文件</td></tr></table>

## 7 测试案例要求

### 7.1 总体要求

a）互联互通测试案例编写需要依据本部分的测试需求进行，需要对测试需求中规定的功能点实现全覆盖。每个测试需求可以对应多个测试案例。

b) 测试案例的编写及测试过程需要遵循以下原则：

1）测试过程中同时涉及车载和地面设备时，默认采用不同厂家设备；

2）测试过程中涉及两个控区地面设备时，默认采用不同厂家设备；

3）对于相同功能但正线和跨线接口实现方式不同的需求，需要在正线和跨线接口测试。

c) 鉴于各厂家对故障的识别及处理原则存在较大差异，故障相关测试内容在互联互通产品供应商测试及验证阶段执行。

### 7.2 具体要求

测试案例中应至少描述以下内容：

---

a）对应的测试需求；

b）本规范中定义的测试阶段；

c）测试条件（测试时应具备的前提条件）；

d）测试环境（如时间、地点、人员）；

e）被测设备的厂家编号等。

---

## 参考文献

[1]《RSSP-Ⅱ铁路信号安全通信协议》(运基信号 $$ 2010 $$ 267号)

[2] IEEE 802.3 系列标准

---

中国城市轨道交通协会团体标准

城市轨道交通基于通信的列车运行控制系统（CBTC）

互联互通测试规范

第2部分：点式部分测试及验证

T/CAMET 04012.2—2018

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门西街8号）

出版社网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm×1230 mm 1/32 印张：5 字数：138千

2019年6月第1版 2019年6月第1次印刷

书号：15113·5715 定价：40.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174