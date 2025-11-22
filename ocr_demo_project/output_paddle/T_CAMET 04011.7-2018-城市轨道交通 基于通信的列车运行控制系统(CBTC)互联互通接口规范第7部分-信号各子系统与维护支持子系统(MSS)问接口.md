# 中国城市轨道交通协会团体标准

T/CAMET 04011.7—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第7部分：信号各子系统与维护支持系统 (MSS) 间接口

## Urban rail transit — Interface specification for interoperability of communication based train control system Part 7: Interface between signal other subsystems and maintenance support system

2018-09-10 发布

2018-12-31 实施

---

## 目 次

前言 …… VII    
引言 …… VIII    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 2    
3.1 术语 …… 2    
3.2 缩略语 …… 3    
4 总则 …… 4    
5 接口描述 …… 5    
6 MSS-V0BC 报文规范 …… 6    
6.1 接口连接方式 …… 6    
6.2 通信层次结构描述 …… 6    
6.3 接口数据描述 …… 8    
7 MSS-ZC 报文规范 …… 13    
7.1 接口连接方式 …… 13    
7.2 通信层次结构描述 …… 14    
7.3 接口数据描述 …… 14    
8 MSS-DSU 报文规范（可选） …… 19    
8.1 接口连接方式 …… 19    
8.2 通信层次结构描述 …… 19    
8.3 接口数据描述 …… 19    
9 MSS-ATS 报文规范 …… 22    
9.1 接口连接方式 …… 22

---

9.2 通信层次结构描述 …… 23  
9.3 接口数据描述 …… 23  
10 MSS - CI 报文规范 …… 30  
10.1 接口连接方式 …… 30  
10.2 通信层次结构描述 …… 30  
10.3 接口数据描述 …… 31  
11 MSS - 计轴报文规范 …… 33  
11.1 接口连接方式 …… 33  
11.2 通信层次结构描述 …… 34  
11.3 接口数据描述 …… 34  
12 MSS - 电源报文规范 …… 36  
12.1 接口连接方式 …… 36  
12.2 通信层次结构描述 …… 37  
12.3 接口数据描述 …… 37  
13 MSS - LEU 报文规范 …… 45  
13.1 接口连接方式 …… 45  
13.2 通信层次结构描述 …… 46  
13.3 接口数据描述 …… 46  
14 MSS - 微机监测报文规范 …… 49  
14.1 接口连接方式 …… 49  
14.2 通信层次结构描述 …… 50  
14.3 接口数据描述 …… 50  
15 MSS - DCS 报文规范 …… 58  
15.1 接口连接方式 …… 58  
15.2 通信层次结构描述 …… 59  
15.3 接口数据描述 …… 59

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口；

——第4部分：区域控制器(ZC)间接口；

——第5部分：计算机联锁(CI)间接口；

——第6部分：列车自动监控系统（ATS）间接口；

——第7部分：信号各子系统与维护支持系统(MSS)间接口；

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 7 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京交通大学、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：黄友能、张瑞雪、张日新、智国盛、何丹、张尧、杨勇、李刚、章国林、胡顺定、韩琛、周晓。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、王道敏、张良、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、徐鼎。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第7部分：信号各子系统与维护支持 系统（MSS）间接口

## 1 范围

T/CAMET 04011 的本部分定义了中国城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通的各子系统与维护支持系统（MSS）间接口规范，包括互联互通下各系统与 MSS 的接口连接方式、接口数据描述等。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标工程建设。

## 轨道

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB/T 24339.1 轨道交通 通信、信号和处理系统 第1部分：封闭式传输系统中的安全相关通信（IEC 62280-1:2002, IDT）

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

---

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第1部分：系统总体要求

IEEE 802.3 以太网(Ethernet)

## 3 术语和缩略语

GB/T 12758—2004、GB 50157—2013、CJ/T 407—2012 和 T/CAMET 04010.1 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

城市轨道交通信号 urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T 12758—2004, 术语与定义 3.1]

#### 3.1.2 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.3 

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.37]

#### 3.1.4 

列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB 50157—2013, 定义 2.0.38]

---

#### 3.1.5 

列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB 50157—2013, 定义 2.0.39]

#### 3.1.6 

## 列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。 $$ GB 50157—2013, 定义 2.0.40 $$ 



#### 3.1.7 

计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[GB 50157—2013, 定义 2.0.40]

#### 3.1.8 

维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护。

[T/CAMET 04010.1, 术语 3.1.8]

### 3.2 缩略语

AM:列车自动驾驶模式(Automatic Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO: 列车自动运行 (Automatic Train Operation)

ATP: 列车自动防护 (Automatic Train Protection)

ATS: 列车自动监控 (Automatic Train Supervision)

BTM: 应答器传输模块 (Balise Transfer Module)

CBTC: 基于通信的列车控制 (Communication Based Train Control)

CI: 计算机联锁 (Computer Interlocking)

CM: 列车自动防护模式 (Coded Train Operating Mode)

---

CRC: 循环冗余校验 (Cyclic Redundancy Check)

DCS: 数据通信系统 (Data Communication System)

EUM: 非限制人工驾驶模式 (Emergency Unrestricted Train Operating Mode)

IP: 互联网协议地址 (Internet Protocol Address)

IPv4: 网际协议 (Internet Protocol, IP) 的第 4 版

LEU: 轨旁电子单元 (Lineside Electronic Unit)

MA: 移动授权 (Movement Authority)

MAC:媒体介入控制层(Media Access Control)

MSS:维护支持系统(Maintenance Support System)

MTBF: 平均故障间隔时间 (Mean Time Between Failures)

MTTR: 平均修复时间 (Mean Time To Repair)

PIS:乘客信息系统(Passenger Information System)

PSD: 站台门 (Platform Screen Door)

RM:限制人工驾驶模式(Restricted Train Operating Mode)

SIL: 安全完整性等级 (Safety Integrity Level)

TMS: 列车管理系统 (Train Management System)

TSR: 临时限速 (Temporary Speed Restriction)

UDP: 用户数据报协议 (User Datagram Protocol)

UPS:不间断电源(Uninterruptible Power System)

ZC: 区域控制器 (Zone Controller)

## 4 总则

4.1 信号系统互联互通是一项系统工程，涉及需求、产品、工程、运营、维护等各个方面，需要整体规划、点面结合、分步实施。

4.2 城市轨道交通 CBTC 系统互联互通是指装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

---

4.3 CBTC 系统互联互通的总体目标是支持轨道交通网络化运营，实现轨道交通线网建设和运营的资源共享。

4.4 互联互通的 CBTC 系统应采用安全可靠的产品，并应满足相关国产化政策要求。

4.5 在互联互通工程招标阶段，招标单位应在符合本规范的基础上，根据互联互通线路网络规划，补充信号系统其他相关功能、性能、接口、设计的具体需求，形成具体工程信号系统招标的技术要求。

4.6 CBTC 系统涉及互联互通的设备接口应符合国际/国内/行业标准的规定，对于无相关标准规定的接口，在满足系统安全、可靠、功能完整的前提下，接口定义应简单、清晰、层次合理。

4.7 采用本互联互通信号系统规范的工程实施应根据相关国际/国内/行业规范确定用户需求、系统构成、系统配置、工程布置以及特定工程须确定的系统/子系统间接口。

4.8 本规范基于国内各城市用户需求以及其所采用不同的具体实现方法的系统技术，制定合理的、满足国内用户需求的主要功能统一、系统架构统一的互联互通系统技术要求。

4.9 互联互通信号系统应采用可靠统一的无线通信系统（WCS）作为车-地信息传输的透明传输通道，采用满足 GB/T 24339.1 标准要求的网络传输安全防护技术。

4.10 信号系统互联互通除应遵守本规范规定外，还应符合国家现行相关规范的规定。

4.11 系统采用的设备和器材应符合有关现行国家标准和有关行业标准的规定。

## 5 接口描述

本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对接口数据交互内容进行扩展。

---

## 6 MSS - VOBC 报文规范

### 6.1 接口连接方式

#### 6.1.1 物理接口

MSS 子系统与 VOBC 子系统之间采用冗余网络进行数据通信，利用车－地无线传输系统完成交互信息发送与接收。

#### 6.1.2 动态交互描述

列车上电完成定位后，根据列车所处位置，确定信息上报所属的线路的 MSS 系统的 IP 地址，并周期性地向 MSS 系统发送状态信息。

列车进行转线作业时，当列车完全进入ZC共管区域后，需同时与两个线路的MSS系统进行周期性通信；当列车整体越过ZC共管区域边界后，V0BC系统仅与当前线路的MSS系统周期性通信。

#### 6.1.3 通信故障处理

MSS 如果连续超过额定时间都接收不到 VOBC 的任何数据，则 MSS 认为与 VOBC 通信中断，MSS 将 VOBC 设备状态设为未知。

### 6.2 通信层次结构描述

#### 6.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面。

#### 6.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 6.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 6.2.4 冗余层

V0BC 发送的内容(vobcmsg1)按照表1格式发送。

---

<div style="text-align: center;">表 1 VOBC 帧格式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>RP协议头</td><td style='text-align: center;'>num_msg¹</td><td style='text-align: center;'>msg1_id¹</td><td style='text-align: center;'>length_msg¹</td><td style='text-align: center;'>msg1</td><td style='text-align: center;'>msg_id_Pr²</td><td style='text-align: center;'>length_msg_Pr¹</td><td style='text-align: center;'>Msg_Pr²</td><td style='text-align: center;'>CRC</td></tr><tr><td style='text-align: center;'>15个字节</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>N个字节</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>N个字节</td><td style='text-align: center;'>4个字节</td></tr><tr><td colspan="9">a num_msg为本周期发送的消息个数,存在一个周期发送两种消息的可能,1个字节。</td></tr><tr><td colspan="9">b msg_id为消息的类型,msg_id=202代表本消息为告警信息。</td></tr><tr><td colspan="9">c length_msgN为消息的msgN的长度,2个字节。</td></tr><tr><td colspan="9">d msgN为具体的消息内容,详见6.3.1。</td></tr><tr><td colspan="9">e msg_id_Pr为用户自定义包消息类型。</td></tr><tr><td colspan="9">f length_msg_Pr为自定义包Msg_Pr的长度。</td></tr><tr><td colspan="9">g Msg_Pr为自定义包的内容。</td></tr></table>

<div style="text-align: center;">表 2 规定了 RP 协议头的内容。</div>


<div style="text-align: center;">表 2 RP 协议头</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>0xFF</td><td style='text-align: center;'>帧长度a</td><td style='text-align: center;'>发送方标识</td><td style='text-align: center;'>接收方标识</td><td style='text-align: center;'>序列号b</td></tr><tr><td style='text-align: center;'>1个字节</td><td style='text-align: center;'>2个字节</td><td style='text-align: center;'>4个字节</td><td style='text-align: center;'>4个字节</td><td style='text-align: center;'>4个字节</td></tr><tr><td colspan="5">a帧长度：从发送方标识至帧尾的字节长度。b序列号：本方的周期计数，发送方每周期将本计数加1，序列号有效值为1~ (21-1)。</td></tr></table>

表 3 规定了发送方和接收方标识信息的内容。

<div style="text-align: center;">表 3 发送方和接收方标识信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>内容</td></tr><tr><td rowspan="3">发送方标识信息</td><td rowspan="3">4字节</td><td style='text-align: center;'>V0BC:0x01,MSS:0x20</td></tr><tr><td style='text-align: center;'>厂商ID:对厂商统一编号</td></tr><tr><td style='text-align: center;'>当发送方为V0BC时,此编号为车载编号,编号(16bits):15~14bit,预留;13~2bit,列车编号;1~0bit,车端号</td></tr></table>

---

<div style="text-align: center;">表 3 发送方和接收方标识信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>内容</td></tr><tr><td rowspan="3">接收方标识信息</td><td rowspan="3">4字节</td><td style='text-align: center;'>V0BC:0x10,MSS:0x20</td></tr><tr><td style='text-align: center;'>厂商ID:对厂商统一编号</td></tr><tr><td style='text-align: center;'>当接收方为MSS时,此设备为MSS的ID</td></tr></table>

#### 6.2.5 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见6.3的规定。

### 6.3 接口数据描述

#### 6.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算：

 $$ \begin{aligned}G(x)=&\ x^{32}+x^{26}+x^{23}+x^{22}+x^{16}+x^{12}+x^{11}+x^{10}\\&+x^{8}+x^{7}+x^{5}+x^{4}+x^{2}+x+1\end{aligned} $$ 

式中：

 $ G(x) $  —— x 的 32 次幂生成多项式；

x——校验的二进制数；

余子式的初始值设为 0xFFFFFFF

#### 6.3.2 VOBC→MSS

表 4 规定了 VOBC 发送给 MSS 的内容。

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小 (Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>msg_id</td><td style='text-align: center;'>1</td><td style='text-align: center;'>202</td><td style='text-align: center;'>202</td><td style='text-align: center;'>202</td><td style='text-align: center;'>202</td><td style='text-align: center;'>消息 ID</td></tr><tr><td style='text-align: center;'>Version_No</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0x2001</td><td style='text-align: center;'>1</td><td style='text-align: center;'>65 535</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>应用层通信协议 版本号</td></tr></table>

---

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>Time</td><td style='text-align: center;'>6</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>DriverNo</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>65 535</td><td style='text-align: center;'>0 表示无效</td><td style='text-align: center;'>司机号</td></tr><tr><td style='text-align: center;'>ChoiceMode</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>1</td><td style='text-align: center;'>5</td><td style='text-align: center;'>1 = IL - RM, 2 = ITC - CM, 3 = ITC - AM, 4 = CBTC - CM, 5 = CBTC - AM</td><td style='text-align: center;'>最高驾驶模式</td></tr><tr><td style='text-align: center;'>CtrlLevel</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>1</td><td style='text-align: center;'>3</td><td style='text-align: center;'>1 = IL, 2 = ITC, 3 = CBTC</td><td style='text-align: center;'>当前控制级别</td></tr><tr><td style='text-align: center;'>DriveMode</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>3</td><td style='text-align: center;'>1 = RM, 2 = CM, 3 = AM</td><td style='text-align: center;'>当前驾驶模式</td></tr><tr><td style='text-align: center;'>Speed</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>列车当前速度(km/h)</td></tr><tr><td style='text-align: center;'>EbiSpeed</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>紧急制动触发速度(km/h)</td></tr><tr><td style='text-align: center;'>AtpDetailFault</td><td style='text-align: center;'>4</td><td style='text-align: center;'>N/A</td><td colspan="4">ATP 具体的板级故障报警,每一Bit代表一个故障</td></tr><tr><td style='text-align: center;'>AtpInitRst</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td colspan="4">ATP 设备自检结果,每一Bit代表一个结果,其中1表示故障,0表示正常</td></tr><tr><td style='text-align: center;'>DeviceFault</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td colspan="4">设备故障报警(非ATP、ATO设备),每一Bit代表一个故障</td></tr><tr><td style='text-align: center;'>AtoDetailFault</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td colspan="4">ATO 具体的板级故障报警,每一Bit代表一个故障,其中1表示故障,0表示正常</td></tr><tr><td style='text-align: center;'>PlatformId</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>站台号(列车在区间或站台停稳前发无效值,在站台停稳时站台号有效)</td></tr></table>

---

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>AtoOperationFault</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">ATO运行过程中的故障,每一个Bit代表一种故障</td></tr><tr><td style='text-align: center;'>AtpCutoffPropulsion</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>ATP切断牵引</td></tr><tr><td style='text-align: center;'>AtpCouffPropulsionReason</td><td style='text-align: center;'>8</td><td style='text-align: center;'>0</td><td colspan="4">列车切断牵引原因,每一个Bit代表一种原因,该Bit置1表示有效</td></tr><tr><td style='text-align: center;'>AtpEbA</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>ATP实施常用制动</td></tr><tr><td style='text-align: center;'>AtpEbAReason</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td colspan="4">列车常用制动原因,每一个Bit代表一种原因,该Bit置1表示有效</td></tr><tr><td style='text-align: center;'>AtpEb</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>ATP实施紧急制动</td></tr><tr><td style='text-align: center;'>AtpEbReason</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td colspan="4">列车紧急制动原因,每一个Bit代表一种原因,该Bit置1表示有效</td></tr><tr><td style='text-align: center;'>AtpLoseLoc</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>列车位置丢失</td></tr><tr><td style='text-align: center;'>AtpLoseLocReason</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td colspan="4">列车丢失位置原因,每一个Bit代表一种原因,该Bit置1表示有效</td></tr><tr><td style='text-align: center;'>TrainBrakeFault</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>列车制动力故障</td></tr><tr><td style='text-align: center;'>FullLoadRatio</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>255</td><td style='text-align: center;'>0~254表示百分比255为无效值</td><td style='text-align: center;'>乘客满载率(默认值为0,表示此时满载率为0或者未知)若本线无此功能,发送无效值</td></tr><tr><td style='text-align: center;'>电子地图版本</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>车载电子地图版本</td></tr></table>

---

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>ATP_Version</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td><td style='text-align: center;'>0 表示无效</td><td style='text-align: center;'>软件版本号</td></tr><tr><td style='text-align: center;'>ATO_Version</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td><td style='text-align: center;'>0 表示无效</td><td style='text-align: center;'>软件版本号</td></tr><tr><td style='text-align: center;'>MMI_Version</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td><td style='text-align: center;'>0 表示无效</td><td style='text-align: center;'>软件版本号</td></tr><tr><td style='text-align: center;'>Stopped_PrecisionATP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0山区</td><td style='text-align: center;'>列车停车精度数值(ATP)，发送-126~126之间的数值，代表停车精度数值，单位：cm。其中正数代表欠标，负数代表达标。超过[-126,126]的停车精度，发送-126或126的边界值。列车非停稳时该值无效，发送值为0x7f(127)</td><td style='text-align: center;'>列车的停车误差。列车非停稳时该值无效，发送值为0x7f</td></tr><tr><td style='text-align: center;'>Stopped_PrecisionATO</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0山区</td><td style='text-align: center;'>列车停车精度数值(ATO)，发送-126~126之间的数值，代表停车精度数值，单位：cm。其中正数代表欠标，负数代表达标。超过[-126,126]的停车精度，发送-126或126的边界值。列车非停稳时该值无效，发送值为0x7f(127)</td><td style='text-align: center;'>列车的停车误差。列车非停稳时该值无效，发送值为0x7f</td></tr></table>

---

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>Check_Result</td><td style='text-align: center;'>6</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0同一个比特</td><td style='text-align: center;'>0xFFFFFFF表示无效</td><td style='text-align: center;'>自定义</td></tr><tr><td style='text-align: center;'>VOBC_ZCID1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>移交ZC ID</td></tr><tr><td style='text-align: center;'>VOBC_ZCCOMFault1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">VOBC与ZC通信故障描述,0表示通信故障或未通信,1表示通信正常</td></tr><tr><td style='text-align: center;'>VOBC_ZCID2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>接管ZC ID,如无移交,取值0xFFFFFFF</td></tr><tr><td style='text-align: center;'>VOBC_ZCCOMFault2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">VOBC与ZC通信故障描述,0表示通信故障或未通信,1表示通信正常 无移交,取值0xFF</td></tr><tr><td style='text-align: center;'>VOBC_ATSID1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>移交ATS ID</td></tr><tr><td style='text-align: center;'>VOBC_ATSCOMFault1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">VOBC与ATS通信故障描述,0表示通信故障或未通信,1表示通信正常</td></tr><tr><td style='text-align: center;'>VOBC_ATSID2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>接管ATS ID,如无移交,取值0xFFFFFFF</td></tr><tr><td style='text-align: center;'>VOBC_ATSCOMFault2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">VOBC与移交ATS通信故障描述,0表示通信故障或未通信,1表示通信正常 无移交,取值0xFF</td></tr><tr><td style='text-align: center;'>VOBC_CIID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>CI ID填写最后连接的CI的ID</td></tr><tr><td style='text-align: center;'>VOBC_CICOMFault</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td colspan="4">VOBC与CI通信故障描述,0表示通信故障或未通信,1表示通信正常</td></tr><tr><td style='text-align: center;'>TrainComFault</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0=无效,1=有效</td><td style='text-align: center;'>ATP头尾通信故障,0代表头尾通信正常,1代表头尾通信故障</td></tr></table>

---

<div style="text-align: center;">表 4 VOBC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>缺省值</td><td style='text-align: center;'>最小值</td><td style='text-align: center;'>最大值</td><td style='text-align: center;'>枚举值</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>TmsComFault</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0 = 无效, 1 = 有效</td><td style='text-align: center;'>与 TMS 通信故障, 0 代表与 TMS 通信正常, 1 代表与 TMS 通信故障</td></tr><tr><td style='text-align: center;'>V0BC_HeadOrTail</td><td style='text-align: center;'>1</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>1</td><td style='text-align: center;'>2</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>激活段的序号: 01: TC1 (十进制); 02: TC2 (十进制); ff: 无效。备注: V0BC 头尾端信息, 01 为 TC1, 02 为 TC2, ff 为无效值, 即两端均不为激活端或者均为激活端。如 6 编组列车, 1 号车厢为 TC1, 6 号车厢为 TC2</td></tr><tr><td style='text-align: center;'>TrainReserve</td><td style='text-align: center;'>10</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>预留 10 个字节</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>CRC 校验, 计算范围从 msg_id 到 TrainReserve</td></tr></table>

## 7 MSS - ZC 报文规范

### 7.1 接口连接方式

#### 7.1.1 物理接口

MSS 子系统与 ZC 子系统的维护单元之间采用维护网进行数据通信。其中，ZC 子系统的维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

---

#### 7.1.2 动态交互描述

ZC 子系统维护单元周期性通过维护网向 MSS 子系统发送报警信息。

#### 7.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到 ZC 子系统维护单元的任何数据，则 MSS 子系统认为与 ZC 子系统通信中断；ZC 子系统维护单元如果超过额定时间收不到 MSS 子系统的应答数据，则认为 ZC 子系统与 MSS 子系统通信中断（可选功能），此时 ZC 子系统维护单元仍保持周期性给 MSS 发送数据不变。

### 7.2 通信层次结构描述

#### 7.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面。

#### 7.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 7.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 7.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见7.3的规定。

### 7.3 接口数据描述

#### 7.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF。

#### 7.3.2 ZC→MSS

表 5 规定了 ZC 发送给 MSS 的信息内容。

---

<div style="text-align: center;">表 5 ZC 发送给 MSS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值：0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值：0x20</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td style='text-align: center;'>ZC_INDEX</td><td style='text-align: center;'>4</td><td style='text-align: center;'>ZC的编号（十进制）ZC未开机或初始上电，ZC维护单元未收到平台发来的数据之前，ZC_INDEX=0</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号，初始值为1，每次报文依次累加，累计至0xFFFFFFF后，下一次重新回1，从1开始</td></tr><tr><td style='text-align: center;'>Device_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备包含固件数量</td></tr><tr><td style='text-align: center;'>Device(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备(1)状态0xAA：正常状态0xff：故障状态其他值，预留</td></tr><tr><td style='text-align: center;'>Device(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备(n)状态0xAA：正常状态0xff：故障状态其他值，预留</td></tr><tr><td style='text-align: center;'>HostStyle</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC主备状态0xAA：1系主用状态，2系备用状态0x55：1系备用状态，2系主用状态0x77：1系主用状态，2系故障0x99：1系故障，2系主用状态0xff：双机故障其他值，预留</td></tr></table>

---

<div style="text-align: center;">表 5 ZC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">ZC_DSU_COM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与DSU的通信状态0xAA:正常0x55:故障0x33:未知(ZC维护单元无法获取信息)0xff:无DSU设备时的默认值</td></tr><tr><td colspan="2">ZC_ATS_COM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与ATS的通信状态0xAA:正常0x55:故障0x33:未知(ZC维护单元无法获取信息)</td></tr><tr><td colspan="2">ZC_CI_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>与ZC通信的CI数量(十进制)</td></tr><tr><td rowspan="2">CI(1)信息</td><td style='text-align: center;'>ZC_CI_ID(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CI(1)的ID(十进制)</td></tr><tr><td style='text-align: center;'>ZC_CI_COM(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与CI(1)的通信状态0xAA:正常0x55:故障0x33:未知(ZCM无法获取信息)</td></tr><tr><td rowspan="2">CI(n)信息</td><td style='text-align: center;'>ZC_CI_ID(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>N/A</td></tr><tr><td style='text-align: center;'>ZC_CI_COM(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与CI(n)的通信状态0xAA:正常0x55:故障0x33:未知(ZCM无法获取信息)</td></tr><tr><td colspan="2">ZC_ZC_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>与ZC通信的相邻ZC数量(十进制)</td></tr><tr><td rowspan="2">相邻ZC(1)信息</td><td style='text-align: center;'>ZC_ZC_ID(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>相邻ZC(1)的ID(十进制)</td></tr><tr><td style='text-align: center;'>ZC_ZC_COM(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与相邻ZC(1)的通信状态0xAA:正常0x55:故障0x33:未知(ZCM无法获取信息)</td></tr></table>

---

<div style="text-align: center;">表 5 ZC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="2">相邻ZC(n)信息</td><td style='text-align: center;'>ZC_ZC_ID(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>相邻ZC(n)的ID(十进制)</td></tr><tr><td style='text-align: center;'>ZC_ZC_COM(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与相邻ZC(n)的通信状态
0xAA:正常
0x55:故障
0x33:未知(ZCM无法获取信息)</td></tr><tr><td colspan="2">NID_SOFT_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>包含软件数量</td></tr><tr><td colspan="2">NID_SOFT_Ver(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>软件版本号</td></tr><tr><td colspan="2">NID_SOFT_Ver(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>软件版本号</td></tr><tr><td colspan="2">ALXE_SEG_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>计轴区段数量</td></tr><tr><td rowspan="2">计轴区段(1)</td><td style='text-align: center;'>NID_ALXE_SEG</td><td style='text-align: center;'>4</td><td style='text-align: center;'>计轴区段(1)ID(十进制)</td></tr><tr><td style='text-align: center;'>Q_ALXE_SEG</td><td style='text-align: center;'>1</td><td style='text-align: center;'>计轴区段(1)状态
0x55:ARB
0xAA:正常</td></tr><tr><td rowspan="2">计轴区段(n)</td><td style='text-align: center;'>NID_ALXE_SEG</td><td style='text-align: center;'>4</td><td style='text-align: center;'>计轴区段(n)ID(十进制)</td></tr><tr><td style='text-align: center;'>Q_ALXE_SEG</td><td style='text-align: center;'>1</td><td style='text-align: center;'>计轴区段(n)状态
0x55:ARB
0xAA:正常</td></tr><tr><td colspan="2">Train_count</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC管辖范围内的列车数(此列车为ZC可识别的列车)</td></tr><tr><td rowspan="2">Train(1)</td><td style='text-align: center;'>VOBC_index</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC的唯一标识
0:未知列车设备ID(默认值)
其他:表示可识别列车ID(十进制)(车组号)</td></tr><tr><td style='text-align: center;'>ZC_VOBC_COM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与VOBC的通信状态
0xAA:正常
0x55:故障</td></tr></table>

---

<div style="text-align: center;">表 5 ZC 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="2">Train(n)</td><td style='text-align: center;'>VOBC_index</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC的唯一标识0:未知列车设备ID(默认值)其他:表示可识别列车ID(十进制)(车组号)</td></tr><tr><td style='text-align: center;'>ZC_VOBC_COM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC与VOBC的通信状态0xAA:正常0x55:故障</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从MSG_ID到END</td></tr></table>

#### 7.3.3 MSS→ZC

MSS 收到 ZC 的报文后，立即反馈应答。表 6 规定了 MSS 发送给 ZC 的信息内容。

<div style="text-align: center;">表 6 MSS 发送给 ZC 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志
默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息IP
默认值:0x21</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>RCV_SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>应答对应的ZC报文序列号</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识
默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

---

## 8 MSS - DSU 报文规范(可选)

### 8.1 接口连接方式

#### 8.1.1 物理接口

MSS 子系统与 DSU 子系统维护单元之间采用维护网进行数据通信。其中，DSU 子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 8.1.2 动态交互描述

DSU 子系统维护单元周期性通过维护网向 MSS 子系统发送报警信息。

#### 8.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到 DSU 子系统的任何数据，则 MSS 子系统认为与 DSU 子系统通信中断；DSU 子系统如果超过额定时间收不到 MSS 子系统的应答数据，则认为 DSU 子系统与 MSS 子系统通信中断（可选功能），此时 DSU 子系统仍保持周期给 MSS 发送数据不变。

### 8.2 通信层次结构描述

#### 8.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。

#### 8.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 8.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 8.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见8.3的规定。

### 8.3 接口数据描述

#### 8.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

---

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF。

#### 8. 3. 2 DSU→MSS

表 7 规定了 DSU 发送给 MSS 的信息内容。

<div style="text-align: center;">表 7 DSU 发送给 MSS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的开始标志
默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID
默认值:0x90</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>DSU_INDEX</td><td style='text-align: center;'>4</td><td style='text-align: center;'>DSU的编号(十进制)
DSU未开机或初始上电,DSU维护机未收到平台发来的数据之前,DSU_INDEX=0</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新回1,从1开始</td></tr><tr><td style='text-align: center;'>Device_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备包含固件数量</td></tr><tr><td style='text-align: center;'>Device(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备(1)状态
0xAA:正常状态
0xFF:故障状态
其他值,预留</td></tr><tr><td style='text-align: center;'>Device(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>设备(n)状态
0xAA:正常状态
0xFF:故障状态
其他值,预留</td></tr></table>

---

<div style="text-align: center;">表 7 DSU 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HostStyle</td><td style='text-align: center;'>1</td><td style='text-align: center;'>DSU 主备状态0xa:1 系主用状态,2 系备用状态0x55:1 系备用状态,2 系主用状态0x77:1 系主用状态,2 系故障0x99:1 系故障,2 系主用状态其他值,预留</td></tr><tr><td style='text-align: center;'>NID_SOFT_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>包含软件数量</td></tr><tr><td style='text-align: center;'>NID_SOFT_Ver(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>软件版本号</td></tr><tr><td style='text-align: center;'>NID_SOFT_Ver(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>软件版本号</td></tr><tr><td style='text-align: center;'>VOTE_STATUS_A</td><td style='text-align: center;'>CHINA ASSOCIATION</td><td style='text-align: center;'>DSU:A 系表及结果(主机1和主机2)0xa:一致0x55:不一致0x33:未知(DSU关切柜或初始上电)</td></tr><tr><td style='text-align: center;'>VOTE_STATUS_B</td><td style='text-align: center;'>CHINA ASSOCIATION</td><td style='text-align: center;'>DSU:B 系表及结果(主机3和主机4)0xa:一致0x55:不一致0x33:未知(DSU未开机或初始上电)</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>当定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识,默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验,计算范围从 MSG_ID 到 END</td></tr></table>

#### 8. 3. 3 MSS→DSU

表 8 规定了 MSS 发送给 DSU 内容。

<div style="text-align: center;">表 8 MSS 发送给 DSU 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从MSG_ID开始到CRC校验结束）</td></tr></table>

---

<div style="text-align: center;">表 8 MSS 发送给 DSU 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x91</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td style='text-align: center;'>RCV_SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>应答对应的DSU报文序列号</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验，计算范围从MSG_ID到END</td></tr></table>

## 9 MSS - ATS 报文规范

### 9.1 接口连接方式

#### 9.1.1 物理接口

MSS 子系统与 ATS 子系统维护单元之间采用维护网进行数据通信。其中，ATS 子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 9.1.2 动态交互描述

ATS 与 MSS 之间交互的数据包括心跳信息、ATS 报警信息、ATS 系统软件版本号、ATS 行车信息（含 CI 站场信息）、ATS 操作记录。在相同周期内，不同类型数据的 SN 顺序编写。同周期的相同类型数据的 SN 相同。

## a）心跳信息

心跳帧用于双方保持通信连接正常。MSS 周期性发送心跳帧给 ATS, ATS 周期性发送心跳帧给 MSS。

## b) ATS 报警信息

ATS 周期性向 MSS 发送当前全体 ATS 报警信息。

## c） ATS 系统软件版本号

---

首次连接、断链重连后或系统软件版本号发生变更后，ATS 向 MSS 发送一次全体 ATS 系统软件版本号。

## d）ATS 行车信息（含 CI 站场信息）

ATS 周期性实时向 MSS 传递站场状态数据、站场同步数据，数据以联锁集中区为划分单元。ATS 保证每次发送给 MSS 的一包数据中，不出现重复的信息。

ATS 周期性实时向 MSS 传递车次追踪数据等。

## e） ATS 操作记录

当发现有新的操作记录时，ATS 立即将操作记录发给 MSS。

#### 9.1.3 通信故障处理

如果 MSS 超过额定时间未收到心跳，认为双方连接出现故障，ATS 设备状态为未知，并向 ATS 发起重连申请；如果 ATS 超过额定时间未收到心跳，认为双方连接出现故障，此时 ATS 方重置通信链路，等待 MSS 重连。

### 9.2 通信层次结构描述

#### 9.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。

#### 9.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 9.2.3 传输层

本接口使用 UDP 协议作为传输协议。

#### 9.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见9.3的规定。

### 9.3 接口数据描述

#### 9.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

---

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF。

#### 9. 3. 2 ATS→MSS

##### 9.3.2.1 心跳信息

表 9 规定了 ATS 发送给 MSS 的心跳信息内容。

<div style="text-align: center;">表 9 ATS 发送给 MSS 的心跳信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x50</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>预留字节</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

##### 9.3.2.2 报警信息

表 10 规定了 ATS 发送给 MSS 的报警信息内容。

<div style="text-align: center;">表 10 ATS 发送给 MSS 的报警信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到 CRC校验结束)</td></tr></table>

---

<div style="text-align: center;">表 10 ATS 发送给 MSS 的报警信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x51</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加</td></tr><tr><td colspan="2">ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>报警总数</td></tr><tr><td rowspan="3">ALARM(1)</td><td style='text-align: center;'>ALARM_DEVICE_ID(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报警设备(1)编号</td></tr><tr><td style='text-align: center;'>ALARM_TYPE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警类型</td></tr><tr><td style='text-align: center;'>ALARM_PARA</td><td style='text-align: center;'>2</td><td style='text-align: center;'>报警参数</td></tr><tr><td rowspan="3">ALARM(n)</td><td style='text-align: center;'>ALARM_DEVICE_ID(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报警设备(n)编号</td></tr><tr><td style='text-align: center;'>ALARM_TYPE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警类型</td></tr><tr><td style='text-align: center;'>ALARM_PARA</td><td style='text-align: center;'>2</td><td style='text-align: center;'>报警参数</td></tr><tr><td colspan="3">Private</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

##### 9.3.2.3 版本信息

表 11 规定了 ATS 发送给 MSS 的版本信息内容。

<div style="text-align: center;">表 11 ATS 发送给 MSS 的版本信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr></table>

---

<div style="text-align: center;">表 11 ATS 发送给 MSS 的版本信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从 MSG_ID 开始到 CRC 校验结束）</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息 ID 默认值：0x52</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占 1 个字节（北京时间）</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号，初始值为 1，每次报文依次累加，累计至 0xFFFFFFF 后，下一次重新从 1 开始累加 重连后序列号继续累加，不置 1</td></tr><tr><td colspan="2">ATS_ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>ATS 设备编号</td></tr><tr><td colspan="2">VERSION_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>版本号总数</td></tr><tr><td rowspan="2">DEVICE (1)</td><td style='text-align: center;'>DEVICE_ID(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(1)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION (1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(1)版本号</td></tr><tr><td rowspan="2">DEVICE (n)</td><td style='text-align: center;'>DEVICE_ID(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(n)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION (n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(n)版本号</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值：0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验，校验范围从 LEN 到 END</td></tr></table>

9.3.2.4 站场信息

表 12 规定了 ATS 发送给 MSS 的站场信息内容。

---

<div style="text-align: center;">表 12 ATS 发送给 MSS 的站场信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x53</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新回0,从1开始</td></tr><tr><td style='text-align: center;'>站场状态数据长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述除长度本身的两个字节以外的站场状态数据长度</td></tr><tr><td style='text-align: center;'>站场状态数据</td><td style='text-align: center;'>N</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>站场同步数据长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述除长度本身的两个字节以外的站场同步数据长度</td></tr><tr><td style='text-align: center;'>站场同步数据</td><td style='text-align: center;'>N</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>车次追踪数据长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述除长度本身的两个字节以外的车次追踪数据长度</td></tr><tr><td style='text-align: center;'>车次追踪数据</td><td style='text-align: center;'>N</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>临时限速状态数据长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述除长度本身的两个字节以外的临时限速状态数据长度</td></tr><tr><td style='text-align: center;'>临时限速状态数据</td><td style='text-align: center;'>N</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>牵引供电信息长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述除长度本身的两个字节以外的牵引供电信息长度</td></tr><tr><td style='text-align: center;'>牵引供电信息</td><td style='text-align: center;'>N</td><td style='text-align: center;'>用户自定义</td></tr></table>

---

<div style="text-align: center;">表 12 ATS 发送给 MSS 的站场信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值：0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验，校验范围从 LEN 到 END</td></tr></table>

##### 9.3.2.5 操作信息

表 13 规定了 ATS 发送给 MSS 的操作信息内容。

<div style="text-align: center;">表 13 ATS 发送给 MSS 的操作信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x54</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新回0,从1开始</td></tr><tr><td colspan="2">RECORD_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>操作记录总数</td></tr><tr><td rowspan="4">RECORD(1)</td><td style='text-align: center;'>操作记录长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述本条操作的长度,表示从源机器ID到命令参数最后一个字节的字节数</td></tr><tr><td style='text-align: center;'>源机器ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备ID</td></tr><tr><td style='text-align: center;'>操作类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>操作参数</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>用户自定义</td></tr></table>

---

<div style="text-align: center;">表 13 ATS 发送给 MSS 的操作信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="4">RECORD(n)</td><td style='text-align: center;'>操作记录长度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>描述本条操作的长度，表示从源机器ID到命令参数最后一个字节的字节数</td></tr><tr><td style='text-align: center;'>源机器ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备ID</td></tr><tr><td style='text-align: center;'>操作类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>用户自定义</td></tr><tr><td style='text-align: center;'>操作参数</td><td style='text-align: center;'>不定长</td><td style='text-align: center;'>用户自定义</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验检验范围从LEN到END</td></tr></table>

#### 9.3.3 MSS→ATS

表 14 规定了 MSS 发送给 AIS 的操作信息内容

<div style="text-align: center;">表 14 MISS 发送给 ATS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>方轨道交描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志,默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID,默认值:0x57</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>预留字节</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

---

## 10 MSS - CI 报文规范

### 10.1 接口连接方式

#### 10.1.1 物理接口

MSS 子系统与联锁子系统维护单元之间采用维护网进行数据通信。其中，联锁子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 10.1.2 动态交互描述

联锁子系统周期性向 MSS 子系统发送全部信息，包括：联锁报警信息、联锁软件版本号、联锁设备状态信息。

MSS 子系统周期性发送一次心跳帧给联锁

#### 10.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到联锁子系统的任何数据，则 MSS 子系统认为与联锁子系统通信中断；联锁子系统如果超过额定时间收不到 MSS 子系统的应答数据，则认为联锁子系统与 MSS 子系统通信中断（可选功能），此时联锁子系统仍保持周期给 MSS 发送数据不变。

### 10.2 通信层次结构描述

#### 10.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面。

#### 10.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 10.2.3 传输层

本接口使用 UDP 协议作为传输协议。

#### 10.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见10.3的规定。

---

### 10.3 接口数据描述

#### 10.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFFF。

#### 10.3.2 联锁→MSS

##### 10.3.2.1 报警及设备信息

表 15 规定了联锁发送给 MSS 的报警及设备信息内容。

<div style="text-align: center;">表 15 联锁发送给 MSS 的报警及设备信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志
默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID
默认值:0x40</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加
重连后序列号继续累加,不置1</td></tr><tr><td style='text-align: center;'>CI_ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>联锁设备编号</td></tr><tr><td style='text-align: center;'>CI_INFO</td><td style='text-align: center;'>n</td><td style='text-align: center;'>联锁站场信息</td></tr><tr><td style='text-align: center;'>CI_IO</td><td style='text-align: center;'>n</td><td style='text-align: center;'>驱动采集数据</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识
默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

---

##### 10.3.2.2 软件版本信息

表 16 规定了联锁发送给 MSS 的版本信息内容。

<div style="text-align: center;">表 16 联锁发送给 MSS 的版本信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x41</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加重连后序列号继续累加,不置1</td></tr><tr><td colspan="2">CL_ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>联锁设备编号</td></tr><tr><td colspan="2">VERSION_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>版本号总数</td></tr><tr><td rowspan="2">DEVICE(1)</td><td style='text-align: center;'>DEVICE_ID(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(1)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(1)版本号</td></tr><tr><td rowspan="2">DEVICE(n)</td><td style='text-align: center;'>DEVICE_ID(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(n)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(n)版本号</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

---

#### 10.3.3 MSS→联锁

表 17 规定了 MSS 发送给联锁的信息内容

<div style="text-align: center;">表 17 MSS 发送给联锁的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(Byte)</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x42</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年月日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>预留字节默认值:0</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结果标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

### 11.1 接口连接方式

#### 11.1.1 物理接口

MSS 子系统与计轴子系统维护单元之间采用维护网进行数据通信。其中，计轴子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 11.1.2 动态交互描述

计轴子系统维护单元周期性通过维护网向 MSS 子系统发送报警信息。

#### 11.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到计轴子系统的任何数据，则

---

MSS 子系统认为与计轴子系统通信中断；计轴子系统如果超过额定时间收不到 MSS 子系统的应答数据，则认为计轴子系统与 MSS 子系统通信中断（可选功能），此时计轴子系统仍保持周期给 MSS 发送数据不变。

### 11.2 通信层次结构描述

#### 11.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面。

#### 11.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 11.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 11.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见11.3的规定。

### 11.3 接口数据描述

#### 11.3.1 数据存储方式

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

#### 11.3.2 计轴→MSS

表 18 规定了计轴发送给 MSS 的信息内容。

<div style="text-align: center;">表 18 计轴发送给 MSS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从帧头到帧尾)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID 默认值:0x70</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京 时间)</td></tr></table>

---

<div style="text-align: center;">表 18 计轴发送给 MSS 的信息帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号，初始值为1，每次报文依次累加，累计至0xFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td style='text-align: center;'>AXLE_INDEX</td><td style='text-align: center;'>2</td><td style='text-align: center;'>计轴子系统的车站编号</td></tr><tr><td style='text-align: center;'>AXLE_SECTION_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>计轴区段(1)状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_SECTION_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>计轴区段(n)状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_SENSOR_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>传感器(1)状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_SENSOR_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>传感器(n)状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_TYPE_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>设备种类</td></tr><tr><td style='text-align: center;'>AXLE_TYPE(1)_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>TYPE(1)类型设备编号(1)的状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_TYPE(1)_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>TYPE(1)类型设备编号(n)的状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_TYPE(n)_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>TYPE(n)类型设备编号(1)的状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>AXLE_TYPE(n)_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>TYPE(n)类型设备编号(n)的状态状态根据厂家信息进行约定</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值：0xAA</td></tr></table>

#### 11.3.3 MSS→计轴

表 19 规定了 MSS 发送给计轴的信息内容。

---

<div style="text-align: center;">表 19 MSS 发送给计轴的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x78</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>RCV_SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>对应计轴报警信息包中的帧序列号</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

## 12 MSS - 电源报文规范

### 12.1 接口连接方式

#### 12.1.1 物理接口

MSS 子系统与电源子系统维护单元之间采用维护网进行数据通信。其中，电源子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 12.1.2 动态交互描述

电源子系统维护单元周期性通过维护网向 MSS 子系统发送报警信息。

#### 12.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到电源子系统的任何数据，则 MSS 子系统认为与电源子系统通信中断；电源子系统如果超过额定时间收不到 MSS 子系统的应答数据，则认为电源子系统与 MSS 子系统通信中

---

断（可选功能），此时电源子系统仍保持周期给 MSS 发送数据不变。

### 12.2 通信层次结构描述

#### 12.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。

#### 12.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 12.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 12.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见12.3的规定。

### 12.3 接口数据描述

#### 12.3.1 数据存储方式和通信校验方法

接口数据存储方式采用Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）

生成多项式采用 CRC32(0x04e11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF。

#### 12.3.2 电源→MSS

模拟量数目/状态量数目/告警量数目：

按照实际值大小传输。如果某个量数目为 0，那么这个量的内容为空，其后紧接的是下一个量的数目。

模拟量：

a）电源屏模拟量按照字节（Byte）传输，1个模拟量占2个字节，模拟量数值放大100倍；

b) UPS 模拟量按照标准的浮点数传输，1 个模拟量站 4 个字节，模拟量数值不放大。

---

状态量：

a）电源屏状态量按照字节（Byte）传输，1个状态量占用1字节（Byte）；

b） UPS无状态量。

告警量：

a）电源屏及 UPS 告警量按照位（Bit）传输，1 个告警量占用 1 位（Bit），总共需要的占用的字节数如下：

1）如果告警量数量是8的整数倍，则告警量占用的字节数为：告警量数量/8；

2）如果告警量数量不是8的整数倍，则告警量占用的字节数为：告警量数量/8+1。

b) 电源屏及 UPS 告警量由每个字节低位（0 位）向高位（7 位）依次填充，如果当前的字节被填充完，则填充下一个字节。如果告警量不足 8 的整数倍，则剩余的位填充 0。

注：告警举例：假如有9个告警需要传输，则需要用2个字节传输。第一个字节

0~7位依次填充告警1~8，第二个字节0位填充告警9，第二个字节1~7位没有使用，填充0。见表20。

表 20 给出了电源告警实例。

<div style="text-align: center;">表 20 电源告警实例</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>告警序号</td><td style='text-align: center;'>告警1</td><td style='text-align: center;'>告警2</td><td style='text-align: center;'>告警3</td><td style='text-align: center;'>告警4</td><td style='text-align: center;'>告警5</td><td style='text-align: center;'>告警6</td><td style='text-align: center;'>告警7</td><td style='text-align: center;'>告警8</td><td style='text-align: center;'>告警9</td></tr><tr><td style='text-align: center;'>是否告警</td><td style='text-align: center;'>有</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td><td style='text-align: center;'>有</td><td style='text-align: center;'>有</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td><td style='text-align: center;'>有</td><td style='text-align: center;'>有</td></tr><tr><td style='text-align: center;'>位序号</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>2</td><td style='text-align: center;'>3</td><td style='text-align: center;'>4</td><td style='text-align: center;'>5</td><td style='text-align: center;'>6</td><td style='text-align: center;'>7</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>第一个字节</td><td style='text-align: center;'>1(告警1)</td><td style='text-align: center;'>0(告警2)</td><td style='text-align: center;'>0(告警3)</td><td style='text-align: center;'>1(告警4)</td><td style='text-align: center;'>1(告警5)</td><td style='text-align: center;'>0(告警6)</td><td style='text-align: center;'>0(告警7)</td><td style='text-align: center;'>1(告警8)</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>第二个字节</td><td style='text-align: center;'>1(告警9)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'>0(填充0)</td><td style='text-align: center;'></td></tr></table>

##### 12.3.2.1 电源报文

表 21 规定了电源发送给 MSS 的信息内容。

---

<div style="text-align: center;">表 21 电源发送给 MSS 的电源信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG ID开始到CRC校验结束)</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x30</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">STATION_INDEX</td><td style='text-align: center;'>1</td><td style='text-align: center;'>站点编号</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新回0,从1开始</td></tr><tr><td rowspan="3">PMS_INPUT_ANALOG</td><td style='text-align: center;'>INPUT_ANALOG_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>系统输入模拟量个数n</td></tr><tr><td style='text-align: center;'>INPUT_ANALOG(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>系统输入模拟量1</td></tr><tr><td style='text-align: center;'>INPUT_ANALOG(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>系统输入模拟量n</td></tr><tr><td rowspan="2">PMS_SWITCH_STATE</td><td style='text-align: center;'>SWITCH_STATE_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>开关状态量个数n</td></tr><tr><td style='text-align: center;'>SWITCH_STATE(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开关状态量10:断开;1:闭合</td></tr></table>

---

<div style="text-align: center;">表 21 电源发送给 MSS 的电源信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>PMS_SWITCH_STATE</td><td style='text-align: center;'>SWITCH_STATE(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开关状态量n0:断开;1:闭合</td></tr><tr><td rowspan="3">PMS_ALARM</td><td style='text-align: center;'>ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>输入输出告警个数n</td></tr><tr><td style='text-align: center;'>ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>输入输出告警10正常/1告警</td></tr><tr><td style='text-align: center;'>ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>输入输出告警n0正常/1告警</td></tr><tr><td rowspan="3">PMS_OUTPUT_ANALOG</td><td style='text-align: center;'>OUTPUT_ANALOG_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>输出模拟量数量n</td></tr><tr><td style='text-align: center;'>OUTPUT_ANALOG(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>输出模拟量1</td></tr><tr><td style='text-align: center;'>OUTPUT_ANALOG(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>输出模拟量n</td></tr><tr><td colspan="2">PWR_MODULE_TYPE_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块类型总数m</td></tr><tr><td colspan="2">PWR_MODULE_TYPE(1)_TYPE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型1的模块类型码</td></tr><tr><td colspan="2">PWR_MODULE_TYPE(1)_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型1的模块数量n</td></tr><tr><td rowspan="4">PWR_MODULE_TYPE(1)_1</td><td style='text-align: center;'>PWR_MODULE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块序号</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量个数n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_PUTPUT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量n</td></tr></table>

---

<div style="text-align: center;">表 21 电源发送给 MSS 的电源信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="6">PWR_MODULE_TYPE(1)_1</td><td style='text-align: center;'>PWR_MODULE_STATUS_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块状态量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块告警量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块状态量10正常/1告警</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块状态量n0正常/1告警</td></tr><tr><td rowspan="10">PWR_MODULE_TYPE(1)_n</td><td style='text-align: center;'>PWR_MODULE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块序号</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量个数n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_INPUT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块状态量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块告警量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警量10正常/1告警</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警量n0正常/1告警</td></tr></table>

---

<div style="text-align: center;">表 21 电源发送给 MSS 的电源信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">PWR_MODULE_TYPE(m)_TYPE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型m的模块类型码</td></tr><tr><td colspan="2">PWR_MODULE_TYPE(m)_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型m的模块数量n</td></tr><tr><td rowspan="10">PWR_MODULE_TYPE(m)_1</td><td style='text-align: center;'>PWR_MODULE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块序号</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量个数n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块状态量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块告警量数量</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警10正常/1告警</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警n0正常/1告警</td></tr><tr><td rowspan="3">PWR_MODULE_TYPE(m)_n</td><td style='text-align: center;'>PWR_MODULE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块序号</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量个数n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_OUTPUT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量1</td></tr></table>

---

<div style="text-align: center;">表 21 电源发送给 MSS 的电源信息帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="7">PWR_MODULE_TYPE(m)_n</td><td style='text-align: center;'>PWR_MODULE_OUTPUT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块输出模拟量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块状态量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量1</td></tr><tr><td style='text-align: center;'>PWR_MODULE_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>模块状态量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模块告警量数量n</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警量10正常/1告警</td></tr><tr><td style='text-align: center;'>PWR_MODULE_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>模块告警量n0正常/1告警</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

##### 12.3.2.2 UPS 报文

表 22 规定了电源发送给 MSS 的 UPS 信息内容。

<div style="text-align: center;">表 22 电源发送给 MSS 的 UPS 信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr></table>

---

<div style="text-align: center;">表 22 电源发送给 MSS 的 UPS 信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">名称</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x33</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">STATION_INDEX</td><td style='text-align: center;'>1</td><td style='text-align: center;'>站点编号</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新回0,从1开始</td></tr><tr><td colspan="2">UPS_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>UPS数目</td></tr><tr><td rowspan="7">UPS_1</td><td style='text-align: center;'>UPS_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>UPS的序号</td></tr><tr><td style='text-align: center;'>UPS_ANALOG_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>UPS模拟量数量n</td></tr><tr><td style='text-align: center;'>UPS_ANALOG(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>UPS模拟量1</td></tr><tr><td style='text-align: center;'>UPS_ANALOG(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>UPS模拟量n</td></tr><tr><td style='text-align: center;'>UPS_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>UPS告警量数量n</td></tr><tr><td style='text-align: center;'>UPS_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>UPS告警量10正常/1告警</td></tr><tr><td style='text-align: center;'>UPS_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>UPS告警量n0正常/1告警</td></tr><tr><td rowspan="7">UPS_n</td><td style='text-align: center;'>UPS_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>UPS的序号</td></tr><tr><td style='text-align: center;'>UPS_ANALOG_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>UPS模拟量数量n</td></tr><tr><td style='text-align: center;'>UPS_ANALOG(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>UPS模拟量1</td></tr><tr><td style='text-align: center;'>UPS_ANALOG(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>UPS模拟量n</td></tr><tr><td style='text-align: center;'>UPS_ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>UPS告警量数量n</td></tr><tr><td style='text-align: center;'>UPS_ALARM(1)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>UPS告警量10正常/1告警</td></tr><tr><td style='text-align: center;'>UPS_ALARM(n)</td><td style='text-align: center;'>1 Bit</td><td style='text-align: center;'>UPS告警量n0正常/1告警</td></tr></table>

---

<div style="text-align: center;">表 22 电源发送给 MSS 的 UPS 信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

#### 12.3.3 MSS→电源

表 23 规定了 MSS 发送给电源的信息内容。

<div style="text-align: center;">表 23 MSS 发送给电源的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>大小(BYTE)</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td rowspan="2">帧长度(从MSG_ID开始到CRC校验结束)消息ID:电源对应值0x36E85对应值0x39</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、秒、名占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>RCV_SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>应答对应的电源报文序列号</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

## 13 MSS - LEU 报文规范

### 13.1 接口连接方式

#### 13.1.1 物理接口

MSS 子系统与 LEU 子系统维护单元之间采用维护网进行数据通信。其中，LEU 子系统维护单元提供 1 路标准的以太网接口进行通信；MSS

---

子系统提供标准的以太网接口进行通信

#### 13.1.2 动态交互描述

LEU 子系统维护单元周期性通过维护网向 MSS 子系统发送报警信息。

#### 13.1.3 通信故障处理

MSS 子系统如果超过额定时间接收不到 LEU 子系统的任何数据，则 MSS 子系统认为与 LEU 子系统通信中断；LEU 子系统如果超过额定时间收不到 MSS 子系统的应答数据，则认为 LEU 子系统与 MSS 子系统通信中断（可选功能），此时 LEU 子系统仍保持周期给 MSS 发送数据不变。

### 13.2 通信层次结构描述

#### 13.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面

#### 13.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议

#### 13.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 13.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见

13.3 的规定

### 13.3 接口数据描述

#### 13.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF.

#### 13. 3. 2 LEU→MSS

表 24 规定了 LEU 发送给 MSS 的信息内容。

---

<div style="text-align: center;">表 24 LEU 发送给 MSS 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的开始标志默认值:0xAA</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x80</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2">STATION_INDEX</td><td style='text-align: center;'>1</td><td style='text-align: center;'>车站的编号</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>帧序列号，初始值为1，发送一次报警信息自动累加，累计至0xFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td colspan="2">LEU_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU数量</td></tr><tr><td rowspan="7">LEU(1)</td><td style='text-align: center;'>LEU_INDEX(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>LEU在所属车站的编号</td></tr><tr><td style='text-align: center;'>LEU(1)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(1)主机状态0x00无效表示LEU监测软件接收不到LEU的状态帧，主机状态未知0xAA:正常;0x55:故障</td></tr><tr><td style='text-align: center;'>LEU(1)_DEV(1)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(1)的DEV(1)状态</td></tr><tr><td style='text-align: center;'>LEU(1)_DEV(n)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(n)的DEV(1)状态</td></tr><tr><td style='text-align: center;'>NID_LEU_SW_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU软件数量</td></tr><tr><td style='text-align: center;'>NID_SW(1)_LEU(1)</td><td style='text-align: center;'>3</td><td style='text-align: center;'>LEU(1)的SW(1)软件版本号</td></tr><tr><td style='text-align: center;'>NID_SW(n)_LEU(1)</td><td style='text-align: center;'>3</td><td style='text-align: center;'>LEU(1)的SW(n)软件版本号</td></tr></table>

---

<div style="text-align: center;">表 24 LEU 发送给 MSS 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td rowspan="7">LEU(n)</td><td style='text-align: center;'>LEU_INDEX(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>LEU 在所属车站的编号</td></tr><tr><td style='text-align: center;'>LEU(1)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(1) 主机状态0x00 无效表示 LEU 监测软件接收不到 LEU 的状态帧，主机状态未知0xaa: 正常；0x55: 故障</td></tr><tr><td style='text-align: center;'>LEU(1)_DEV(1)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(1) 的 DEV(1) 状态</td></tr><tr><td style='text-align: center;'>LEU(1)_DEV(n)_STATUS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU(n) 的 DEV(1) 状态</td></tr><tr><td style='text-align: center;'>NID_LEU_SW_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU 软件数量</td></tr><tr><td style='text-align: center;'>NID_SW(1)_LEU(1)</td><td style='text-align: center;'>3</td><td style='text-align: center;'>LEU(1) 的 SW(1) 软件版本号</td></tr><tr><td style='text-align: center;'>NID_SW(n)_LEU(1)</td><td style='text-align: center;'>3</td><td style='text-align: center;'>LEU(1) 的 SW(n) 软件版本号</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值：0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验，计算范围从 MSG_ID 到 END</td></tr></table>

#### 13. 3. 3 MSS→LEU

表 25 规定了 LEU 发送给 MSS 的信息内容。

<div style="text-align: center;">表 25 MSS 发送给 LEU 的信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从MSG_ID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x88</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr></table>

---

<div style="text-align: center;">表 25 MSS 发送给 LEU 的信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节大小</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>RCV_SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>对应LEU报警信息包中的帧序列号</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,计算范围从MSG_ID到END</td></tr></table>

## 14 MSS - 微机监测报文规范

### 14.1 接口连接方式

#### 14.1.1 物理接口

## OCIATION

MSS 子系统与微机监测子系统维护单元之间采用维护网进行数据通信。其中，微机监测子系统维护单元提供 1 路标准的以太网接口进行通信；MSS 子系统提供标准的以太网接口进行通信。

#### 14.1.2 动态交互描述

微机监测与 MSS 之间交互的数据包括心跳信息、开关量报警信息及模拟量信息。

针对《铁路信号集中监测系统技术条件》（运基信号 $$ 2010 $$ 709号）要求的其余监测信息，如外电网综合质量监测、列车信号点灯回路电流监测、环境状态模拟量监测等信息，均作为互联互通自定义功能，下文不进行约束。

## a）心跳信息

心跳帧用于双方保持通信连接正常。MSS周期性发送心跳帧给微机监测，微机监测同时周期性发送心跳帧给MSS。

## b） 微机监测开关量报警信息

微机监测周期性 MSS 发送全体基础信号设备开关量报警信息。

## c） 微机监测模拟量信息

轨道电压周期性发送，道岔电流在道岔动作完后发送所有电流采集点，绝缘测试在测试完毕后发送测试结果。

---

## d）微机监测系统软件版本号

首次连接、断链重连后或系统软件版本号发生变更后，微机监测向MSS发送监测系统软件版本号。

#### 14.1.3 通信故障处理

如果 MSS 方超过额定时间未收到心跳，认为双方连接出现故障，微机监测设备状态为通信中断，并向微机监测发起重连申请；若微机监测超过额定时间未收到心跳，认为双方连接出现故障，此时微机监测方重置通信链路，等待 MSS 重连。

### 14.2 通信层次结构描述

#### 14.2.1 数据链路层

MAC 子层基于 IEEE 802.3 标准。

MAC 头由 14 个字节组成，1 个帧校验序列（4 字节）将被加在 Ethernet 帧后面。

#### 14.2.2 网络层

本接口使用 IPv4 协议作为网络层的协议。

#### 14.2.3 传输层

本接口实时传送的信息使用 UDP 协议作为传输协议。

#### 14.2.4 应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见14.3的规定。

### 14.3 接口数据描述

#### 14.3.1 数据存储方式和通信校验方法

接口数据存储方式采用 Big Endian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用 CRC32(0x04c11db7)，按公式(1)计算，余子式的初始值设为 0xFFFFFFF。

#### 14.3.2 微机监测→MSS

##### 14.3.2.1 心跳帧

表 26 规定了微机监测发送给 MSS 的心跳信息内容。

---

<div style="text-align: center;">表 26 微机监测发送给 MSS 的心跳信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从STATIONID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>STATIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID 默认值:0x10</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>预留字节</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

##### 14.3.2.2 开关量报警信息

开关量信息主要是轨道电压的超限报警。

表 27 规定了微机监测发送给 MSS 的轨道电压报警内容。

<div style="text-align: center;">表 27 微机监测发送给 MSS 的轨道电压报警信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从STATIONID开始到 CRC校验结束）</td></tr><tr><td style='text-align: center;'>STATIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID 默认值:0x20</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字 节（北京时间）</td></tr></table>

---

<div style="text-align: center;">表 27 微机监测发送给 MSS 的轨道电压报警信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号，初始值为1，每次报文依次累加，累计至0xFFFFFEF后，下一次重新从1开始累加（若数据帧长度大于1024字节，分包的各数据包的序列号保持一致）</td></tr><tr><td colspan="2">ALARM_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>报警总数</td></tr><tr><td rowspan="5">ALARM(1)</td><td style='text-align: center;'>ALARM_TYPE(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警(1)类型0x21：轨道电压超限报警</td></tr><tr><td style='text-align: center;'>ALARM_DEV(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警设备</td></tr><tr><td style='text-align: center;'>ALARM_STIME(1)</td><td style='text-align: center;'>6</td><td style='text-align: center;'>报警发生时间，格式同STAMP</td></tr><tr><td style='text-align: center;'>ALARM_NTIME(1)</td><td style='text-align: center;'>6</td><td style='text-align: center;'>报警恢复时间，格式同STAMP</td></tr><tr><td style='text-align: center;'>ALARM_STATUS(1)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警(1)状态0x00：正常0x55：故障</td></tr><tr><td rowspan="5">ALARM(n)</td><td style='text-align: center;'>ALARM_TYPE(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警(n)类型0x21：轨道电压超限报警</td></tr><tr><td style='text-align: center;'>ALARM_DEV(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警设备</td></tr><tr><td style='text-align: center;'>ALARM_STIME(n)</td><td style='text-align: center;'>6</td><td style='text-align: center;'>报警发生时间，格式同STAMP</td></tr><tr><td style='text-align: center;'>ALARM_NTIME(n)</td><td style='text-align: center;'>6</td><td style='text-align: center;'>报警恢复时间，格式同STAMP</td></tr><tr><td style='text-align: center;'>ALARM_STATUS(n)</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警(n)状态0x00：正常0x55：故障</td></tr><tr><td colspan="2">Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td colspan="2">END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值：0x55</td></tr><tr><td colspan="2">CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验，校验范围从LEN到END</td></tr></table>

---

##### 14.3.2.3 模拟量信息

模拟量信息的内容包括：绝缘、道岔电流曲线、轨道电压。其中绝缘、道岔电流曲线，当有数据产生时，监测自主发送数据至MSS。轨道电压值，监测周期性向MSS发送一次所有轨道电压的数据。

在 MSG_ID 下面定义 TYPE_ID，用于区分是哪个类型的数据。

表 28 规定了微机监测发送给 MSS 的模拟量内容。

<div style="text-align: center;">表 28 微机监测发送给 MSS 的模拟量类型</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>TYPE_ID</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>DLJY_INFO</td><td style='text-align: center;'>0x41</td><td style='text-align: center;'>电缆绝缘</td></tr><tr><td style='text-align: center;'>DCDL_INFO</td><td style='text-align: center;'>0x42</td><td style='text-align: center;'>道岔电流</td></tr><tr><td style='text-align: center;'>GDDY_INFO</td><td style='text-align: center;'>0x43</td><td style='text-align: center;'>轨道电压</td></tr></table>

由于绝缘、道岔电流曲线数据产生时发送，只能一个数据包发送一个设备的模拟量，所以在SN下面增加ITEM_NO内容，表示设备序号（例如道岔序号）。

对于道岔电流曲线，微机监测需要向MSS传送道岔动作次数，在ANALOG(n)下增加SWITCH，非道岔电流曲线的模拟量，该内容4个字节预留。

对于轨道电压模拟量监测，除电压值以外的信息，均作为自定义字段供厂家使用。

表 29 规定了微机监测发送的轨道电压模拟量包，格式如下。

<div style="text-align: center;">表 29 微机监测发送给 MSS 的轨道电压状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值：0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td style='text-align: center;'>STATIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr></table>

---

<div style="text-align: center;">表 29 微机监测发送给 MSS 的轨道电压状态信息帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID 默认值:0x30</td></tr><tr><td style='text-align: center;'>TYPE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>DATA TYPE</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加</td></tr><tr><td style='text-align: center;'>ANALOG_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模拟量总数</td></tr><tr><td style='text-align: center;'>ANALOG(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模拟量(1)算法是除以10,单位:V</td></tr><tr><td style='text-align: center;'>ANALOG(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>模拟量(n)</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC校验,校验范围从LEN到END</td></tr></table>

表 30 规定了微机监测发送的道岔电流模拟量包，格式如下。

<div style="text-align: center;">表 30 微机监测发送给 MSS 的道岔电流信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td style='text-align: center;'>STATIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID默认值:0x40</td></tr><tr><td style='text-align: center;'>TYPE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>DATA TYPE</td></tr></table>

---

<div style="text-align: center;">表 30 微机监测发送给 MSS 的道岔电流信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加</td></tr><tr><td colspan="2">ITEM_NO</td><td style='text-align: center;'>2</td><td style='text-align: center;'>设备编号,表示该数据包是第n个设备的内容(对于绝缘、漏流、道岔动作电流需要,其余模拟量可以不使用,按照配置表的顺序即可)</td></tr><tr><td colspan="2">START_TIME</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">DIRECTION</td><td style='text-align: center;'>1</td><td style='text-align: center;'>道岔转换方向0:定位到反位1:反位到定位2:定位到定位3:反位到反位4:定位到故障位5:反位到故障位</td></tr><tr><td colspan="2">CURVE_TYPR</td><td style='text-align: center;'>1</td><td style='text-align: center;'>曲线类型0:交流1:直流</td></tr><tr><td colspan="2">CURVE_NUM</td><td style='text-align: center;'>1</td><td style='text-align: center;'>曲线数量(如果是直流,则为1。如果是交流,则为3,依次是A、B、C三相)</td></tr><tr><td rowspan="3">CURVE(1)</td><td style='text-align: center;'>POINT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点数量(采集点的时间间隔:40ms)</td></tr><tr><td style='text-align: center;'>POINT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点(1)(算法是除以100,单位:A)</td></tr><tr><td style='text-align: center;'>POINT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点(n)(算法是除以100,单位:A)</td></tr><tr><td rowspan="3">CURVE(n)</td><td style='text-align: center;'>POINT_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点数量(采集点的时间间隔:40ms)</td></tr><tr><td style='text-align: center;'>POINT(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点(1)(算法是除以100,单位:A)</td></tr><tr><td style='text-align: center;'>POINT(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>采集点(n)(算法是除以100,单位:A)</td></tr></table>

---

<div style="text-align: center;">表 30 微机监测发送给 MSS 的道岔电流信息帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>SWITCH_CNT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>道岔动作次数</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验，校验范围从 LEN 到 SWITCH_CNT</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识 默认值:0x55</td></tr></table>

表 31 规定了微机监测发送的电缆绝缘模拟量包，格式如下。

<div style="text-align: center;">表 31 微机监测发送给 MSS 的电缆绝缘信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志
默认值:0xAA</td></tr><tr><td style='text-align: center;'>LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从STATIONID开始到CRC校验结束)</td></tr><tr><td style='text-align: center;'>STATIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr><tr><td style='text-align: center;'>MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID,默认值:0x40</td></tr><tr><td style='text-align: center;'>TYPE_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>DATA TYPE</td></tr><tr><td style='text-align: center;'>STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td style='text-align: center;'>SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFF后,下一次重新从1开始累加</td></tr><tr><td style='text-align: center;'>ITEM_NO</td><td style='text-align: center;'>2</td><td style='text-align: center;'>设备编号,表示该数据包是第n个设备的内容(对于绝缘、漏流、道岔动作电流需要,其余模拟量可以不使用,按照配置表的顺序即可)</td></tr><tr><td style='text-align: center;'>ANALOG</td><td style='text-align: center;'>2</td><td style='text-align: center;'>电缆绝缘,单位:MΩ,发实际值(算法是除以100).小于5说明线缆绝缘异常;大于等于20,表示绝缘良好</td></tr><tr><td style='text-align: center;'>Private</td><td style='text-align: center;'>N</td><td style='text-align: center;'>自定义字段</td></tr></table>

---

<div style="text-align: center;">表 31 微机监测发送给 MSS 的电缆绝缘信息帧（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td style='text-align: center;'>END</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧的结束标识默认值:0x55</td></tr><tr><td style='text-align: center;'>CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CRC 校验,校验范围从 LEN 到 END</td></tr></table>

##### 14.3.2.4 微机监测系统软件版本号

表 32 规定了微机监测发送的版本内容, 格式如下。

<div style="text-align: center;">表 32 微机监测发送给 MSS 的版本信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>描述</td></tr><tr><td colspan="2">HEADER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>帧开始标志 默认值:0xAA</td></tr><tr><td colspan="2">LEN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>帧长度(从STATIONID开始到CRC校验结束)</td></tr><tr><td colspan="2">STITIONID</td><td style='text-align: center;'>2</td><td style='text-align: center;'>站报码</td></tr><tr><td colspan="2">MSG_ID</td><td style='text-align: center;'>1</td><td style='text-align: center;'>消息ID 默认值:0x50</td></tr><tr><td colspan="2">STAMP</td><td style='text-align: center;'>6</td><td style='text-align: center;'>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2">SN</td><td style='text-align: center;'>4</td><td style='text-align: center;'>报文序列号,初始值为1,每次报文依次累加,累计至0xFFFFFFFF后,下一次重新从1开始累加</td></tr><tr><td colspan="2">VERSION_NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>版本号总数</td></tr><tr><td rowspan="2">DEVICE(1)</td><td style='text-align: center;'>DEVICE_ID(1)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>设备(1)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION(1)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(1)版本号</td></tr><tr><td rowspan="2">DEVICE(n)</td><td style='text-align: center;'>DEVICE_ID(n)</td><td style='text-align: center;'>2</td><td style='text-align: center;'>设备(n)编号</td></tr><tr><td style='text-align: center;'>DEVICE_VERSION(n)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>设备(n)版本号</td></tr></table>

---

# 中国城市轨道交通协会团体标准 城市轨道交通 基于通信的列车运行 控制系统（CBTC）互联互通接口规范 第7部分：信号各子系统与维护支持系统（MSS）间接口 T/CAMET 04011.7—2018

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门西街8号）

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm × 1230 mm 1/32 印张：2.25 字数：62 千  

2019 年 5 月第 1 版 2019 年 5 月第 1 次印刷

书号：15113·5733 定价：20.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174