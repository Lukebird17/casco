# 中国城市轨道交通协会团体标准

T/CAMET 04011.2—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第2部分：CBTC系统车地连续通信协议

# Urban rail transit — Interface specification for interoperability of communication based train control system

# Part 2: Train-wayside communication protocol for CBTC system

2018-09-10 发布

2018-12-31 实施

---

## 目次

前言 …… VII    
引言 …… IX    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 2    
3.1 术语 …… 2    
3.2 缩略语 …… 5    
4 接口描述 …… 5    
5 VOBC-ZC 报文规范 …… 5    
5.1 接口连接方式 …… 5    
5.2 通信体系结构 …… 11    
5.3 接口数据描述 …… 12    
5.4 应用信息定义 …… 13    
5.5 折返流程说明 …… 32    
6 VOBC-ATS 报文规范 …… 35    
6.1 接口连接方式 …… 35    
6.2 通信体系结构 …… 41    
6.3 接口数据描述 …… 42    
7 VOBC-CI 报文规范 …… 61    
7.1 接口连接方式 …… 61    
7.2 通信体系结构 …… 67

---

7.3 接口数据描述……68  
附录 A（资料性附录） ATO 控制命令帧发送更新时机示例……78  
A.1 场景……78  
A.2 ATO 控制命令帧发送更新时机……78

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第4部分：区域控制器（ZC）间接口；

——第5部分：计算机联锁(CI)间接口；

——第6部分：列车自动监控系统（ATS）间接口；

——第7部分:信号各子系统与维护支持系统(MSS)间接口;

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 2 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京交通大学、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：王伟、刘超、李凯、黄友能、刘宏杰、王悉、张蕾、刘鲁鹏、马新成、刘剑、范楷、任颖、鲍旭红、严光明、胡顺定。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范 第2部分:CBTC系统车地连续通信协议

## 1 范围

本部分规定了 T/CAMET 04011 定义的互联互通的车地通信协议，包括互联互通下 CBTC 系统的车载信号设备 ZC、车载信号设备与 ATS、车载信号设备与 CI 的接口连接方式，接口数据描述等。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

市轨道交

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 1 部分: 系统总体要求

T/CAMET 04010.2 城市轨道交通 基于通信的列车运行控制系统

---

(CBTC)互联互通系统规范 第2部分：系统架构和功能分配

T/CAMET 04011.6 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第6部分：列车自动监控系统（ATS）间接口规范

运基信号 $$ 2010 $$ 267号文件 RSSP-I 铁路信号安全通信协议

运基信号 $$ 2010 $$ 267号文件 RSSP-Ⅱ铁路信号安全通信协议

# EN 50159:2010 欧洲铁路通信信号领域信息传输系统中安全通信标准(Secure Communication Standards for Information Transmission Systems in the Field of Railway Communication Signals in Europe)

IEEE 802.3 局域网协议(Ethernet LAN protocols as defined in IEEE 802.3 suite)

## 3 术语和缩略语

GB/T 12758—2004、GB 50157—2013、CJ/T 407—2012、T/CAMET 04010.1 和 T/CAMET 04010.2 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

## 城市轨道交通信号 urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T 12758—2004, 术语与定义 3.1]

#### 3.1.2 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

---

#### 3.1.3 

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.37]

#### 3.1.4 

## 列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB 50157—2013, 定义 2.0.38]

#### 3.1.5 

## 列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

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

[T/CAMET 04010.1,术语 3.1.8]

---

#### 3.1.9 

## 保护区段 overlap section

为实现超速防护，保证安全停车而延伸的闭塞区段。

[GB/T 12758—2004, 术语与定义 3.12]

#### 3.1.10 

## 目标速度 target speed

列车运行至前方目标地点应达到的允许速度。

[GB/T 12758—2004, 术语与定义 3.13]

#### 3.1.11 

目标距离 target distance

列车运行至前方目标地点的走行距离。

[GB/T 12758—2004, 术语与定义 3.14]

#### 3.1.12 

## 安全保护距离 safe protection distance

列车自动防护系统中，列车超速防护实施安全停车控制时，为防止停车位置离散性可能造成的危险，而设置的自预定停车位置至目标地点的安全距离。

[GB/T 12758—2004, 术语与定义 3.15]

#### 3.1.13 

## 互联互通 Interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1,术语3.1.16]

#### 3.1.14 

## 共线运行 mix operation

装备不同厂家车载信号设备的列车可以在装备同一厂家轨旁信号设备线路上支持以点式列车控制级别和连续式列车控制级别无缝安全可靠运营。

---

[T/CAMET 04010.2,术语3.1.18]

### 3.2 缩略语

AM:列车自动驾驶模式(Automatic Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO:列车自动运行(Automatic Train Operation)

ATP:列车自动防护(Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

CBTC: 基于通信的列车控制系统（Communication Based Train Control）

CM:受控人工驾驶(Code Train Operating Mode)

CI: 计算机联锁 (Computer Interlocking)

DCS: 数据通信系统 (Data Communication System)

PSD:站台门(Platform Screen Door)

RM:限制人工驾驶(Restricted Train Operating Mode)

V0BC: 车载控制器 (Vehicle On-Board Controller)

ZC: 区域控制器 (Zone Controller)

## 4 接口描述

## 轨道

本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对接口数据交互内容进行扩展。

## 5 VOBC - ZC 报文规范

### 5.1 接口连接方式

#### 5.1.1 物理接口

VOBC 与 ZC 之间采用冗余网络进行通信（下文以 A 网、B 网进行描述）ZC 与 VOBC 之间的网络拓扑结构采用 A 网 - A 网、B 网 - B 网两个链路。

#### 5.1.2 安全通信协议

ZC 与 VOBC 之间通信可采用 RSSP-Ⅱ 或 RSSP-Ⅰ 安全通信协议。

---

RSSP-Ⅱ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅱ铁路信号安全通信协议》；RSSP-Ⅰ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅰ铁路信号安全通信协议》。采用RSSP-Ⅰ安全通信协议的前提条件为使用LTE-M通信且LTE-M具备空口加密措施可防止伪装、CBTC信号系统符合三级等保要求。在此前提条件下，宜采用RSSP-Ⅰ安全通信协议。

如图 1 所示，其 SAI/MASL/ALE 三层，遵循 RSSP-Ⅱ标准规定。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7f539be5-61d1-44c6-8dd3-0ff21d758147/markdown_0/imgs/img_in_image_box_129_381_779_878.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A38%3A05Z%2F-1%2F%2F53d566e4181a89ad861e18437aecc8e6a738c9f57834f3a6c46c1f309c63ecdd" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 1 无线安全通信协议 RSSP-Ⅱ构架</div>


TCP 及 IP 层使用标准 TCP/IP 协议栈。

MAC 及 PHY 层取决于不同的网络种类, 无线网使用无线标准协议, 地面网使用以太网协议(IEEE 802.3)。

如图 2 所示, 其 RSSP-I 协议遵循 RSSP-I 标准规定。

UDP 层使用标准 UDP 协议栈。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c6c88915-3c17-4c77-90bb-79f248d207a0/markdown_0/imgs/img_in_image_box_100_128_747_587.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A38%3A14Z%2F-1%2F%2F7af42ae91723b0575039c1cda10064a6f70a1dd42efba42a67145d50302b6f58" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 2 无线安全通信协议 RSSP-I 构架</div>


MAC 及 PHY 层取决于不同的网络种类, 无线网使用无线标准协议, 地面网使用以太网协议(IEEE 802.3)。

#### 5.1.3 动态交互描述

##### 5.1.3.1 通信应用层消息包定义

将 ZC-VOBC 间每个周期需要交互的应用信息通过组成通用消息包进行传输，如图 3 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c6c88915-3c17-4c77-90bb-79f248d207a0/markdown_0/imgs/img_in_image_box_221_855_628_976.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A38%3A14Z%2F-1%2F%2F1e6b58b3c05df9ef2be0f7be0cb2d65301895f217c3bbdea3dc7e9b78708f5d7" alt="Image" width="48%" /></div>


<div style="text-align: center;">图 3 通用消息包和应用层信息包关系结构图</div>


##### 5.1.3.2 信息包格式定义

ZC/V0BC 每周期最多允许发送 1 个通用消息包，通用消息包中包含 ZC 与 V0BC 之间传输的各条应用信息。

---

每个通用消息包总长不得超过1 000字节，通用信息包格式定义见表1，应用层信息格式定义见表2。

<div style="text-align: center;">表 1 通用信息包格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">接口信息类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型高位</td><td rowspan="2">2字节</td><td rowspan="2">0x0102;ZC-V0BC接口</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td style='text-align: center;'>3</td><td rowspan="4">源ID</td><td rowspan="4">4字节</td><td rowspan="4">发送方设备ID</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>6</td></tr><tr><td rowspan="4">接收方标识信息</td><td style='text-align: center;'>7</td><td rowspan="4">目的ID</td><td rowspan="4">4字节</td><td rowspan="4">接收方设备ID</td></tr><tr><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>9</td></tr><tr><td style='text-align: center;'>10</td></tr><tr><td rowspan="4">数据版本校验信息</td><td style='text-align: center;'>11</td><td rowspan="4">ZC与V0BC之间的版本一致性信息</td><td rowspan="4">4字节</td><td rowspan="4">ZC管辖范围内,ZC与V0BC间的数据版本校验信息</td></tr><tr><td style='text-align: center;'>12</td></tr><tr><td style='text-align: center;'>13</td></tr><tr><td style='text-align: center;'>14</td></tr><tr><td rowspan="4">本方消息序列号</td><td style='text-align: center;'>15</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录发送本条消息时,本方的周期计数</td></tr><tr><td style='text-align: center;'>16</td></tr><tr><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>18</td></tr><tr><td rowspan="2">通信周期</td><td style='text-align: center;'>19</td><td rowspan="2">通信周期</td><td rowspan="2">2字节</td><td rowspan="2">设备通信周期,单位为毫秒(ms)</td></tr><tr><td style='text-align: center;'>20</td></tr></table>

---

<div style="text-align: center;">表 1 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="4">对方消息序列号b</td><td style='text-align: center;'>21</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息中的对方消息序列号默认值：0xFFFFFFF</td></tr><tr><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>24</td></tr><tr><td rowspan="4">收到上一条消息时本方序列号b</td><td style='text-align: center;'>25</td><td rowspan="4">协议版本号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息时，本方的周期计数默认值：0xFFFFFFF</td></tr><tr><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>协议版本号a</td><td style='text-align: center;'>29</td><td style='text-align: center;'>应用层数据长度</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>ZC/V0BC的协议版本，本规范定义为20</td></tr><tr><td style='text-align: center;'>应用层数据长度</td><td style='text-align: center;'>30</td><td rowspan="2">应用层数据长度</td><td rowspan="2">2字节</td><td rowspan="2">应用层数据“~报文结束的字节数</td></tr><tr><td rowspan="2">应用层数据</td><td style='text-align: center;'>31</td></tr><tr><td style='text-align: center;'>32~1000</td><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>参见表2格式定义</td></tr><tr><td colspan="5">注：1.数据版本校验计算范围为ZC管辖区域范围；2.ZC/V0BC判断“数据版本校验信息”或“协议版本号”字段校验不通过时，应进行丢包或断开通信处理。b序列号有效值为1~（21-1）。发送方应保证生成两包信息包时，两包信息报中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔“当未收到对方消息时，填写默认值。</td></tr></table>

---

<div style="text-align: center;">表 2 应用层信息格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>说 明</td></tr><tr><td rowspan="2">报文长度</td><td style='text-align: center;'>1</td><td rowspan="2">报文长度(报文类型~报文结束)</td><td rowspan="2">自定义,详细内容参见5.3节</td></tr><tr><td style='text-align: center;'>2</td></tr><tr><td rowspan="2">报文类型</td><td style='text-align: center;'>3</td><td rowspan="2">定义某一条应用信息的标识</td><td rowspan="2">自定义,详细内容参见5.3节</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td rowspan="2">预留</td><td style='text-align: center;'>5</td><td rowspan="2">预留</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>7~报文结束</td><td style='text-align: center;'>按照报文格式定义的报文具体内容</td><td style='text-align: center;'>自定义,详细内容参见5.3节</td></tr></table>

##### 5.1.3.3 通信状态管理

a）ZC 应对与接收到的 VOBC 的应用消息进行合法性检查，若检查未通过，认为本周期未收到对方的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

1）消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查以及信息完整性；

2）通用消息包消息所应包含的信息的完整性。

b) ZC 和 VOBC 应能分别对通信连接状态进行判断（指应用层根据 GAL 包头中字段进行判断，而非安全通信协议层进行的判断）：

1）ZC 认为与 VOBC 通信中断的超时时间定义为 TZcTimeout （3 s~9 s，可配置，推荐值：6 s）；

2）VOBC 认为与 ZC 通信中断的超时时间定义为 TVobcTimeout (3 s ~ 9 s, 可配置, 推荐值: 6 s);

3）若 ZC 在 TZcTimeout 超时时间内，没有接收到来自 VOBC 的任何消息，则 ZC 应认为与 VOBC 的通信中断；

4）若 ZC 判断收到 VOBC 的 GAL 包延迟已经达到 TZcTimeout，

---

则 ZC 应丢弃此 GAL 包或认为与 VOBC 通信中断；

5）若 VOBC 在 TVobcTimeout 超时时间内，没有接收到来自 ZC 的任何消息，则 VOBC 应认为与 ZC 的通信中断；

6) 若 VOBC 判断收到 ZC 的 GAL 包延迟已经达到 TVobcTimeout，则 VOBC 应丢弃此 GAL 包或认为与 ZC 通信中断；

7）互联互通线网中，各厂商 VOBC 与各条线路上的 ZC 的通信超时时间应一致，消息有效期时间应一致；

8）处于连续式列车控制级别的 VOBC 判断与 ZC 的通信中断后，若列车未处于停稳状态，则应输出紧急制动，若列车处于停稳状态，则可输出紧急制动。

c) 当使用安全通信协议 RSSP-Ⅱ时，VOBC 判断与 ZC 断开通信，且不再与该 ZC 重新建立通信后，应断开与该 ZC 的 TCP/IP 连接；



当使用安全通信协议 RSSP-I 时，VOBC 判断与 ZC 断开通信，且不再与该 ZC 重新建立通信后，应断开与该 ZC 的 UDP 连接。

#### 5.1.4 通信故障处理

EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。

车地无线通信双方（ZC-VOBC）应用层的通信故障处理分为以下两种情况：

a）ZC 和 VOBC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对方的应用信息；

b）通信中断的情况下处理：若ZC/V0BC认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理。

### 5.2 通信体系结构

#### 5.2.1 通信模型

ZC 与 VOBC 通信协议模型如图 4 所示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e3c3f8de-5776-4969-af19-3cc511ecce74/markdown_0/imgs/img_in_image_box_212_94_690_455.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A38%3A38Z%2F-1%2F%2F204d5a39f22b2cdff1ebe79ab3873b9b64637e3e4cb2b608a5367c520254f110" alt="Image" width="56%" /></div>


说明：

图中安全功能模块和通信功能模块属于各子系统内部功能实现，分别用于实现安全功能和对外通信功能。

<div style="text-align: center;">图 4 ZC 与 VOBC 通信协议模型</div>


#### 5.2.2 通信机制

a）仅能由 VOBC 发起安全连接的建立过程；

b）ZC 与 VOBC 采用周期发送和消息触发的方式进行通信；

c）通信双方均采用大端字节序进行数据传输；

d）ZC 与 VOBC 均应对接收的应用信息进行判断和逻辑运算。

### 5.3 接口数据描述

#### 5.3.1 数据类型定义

本节对 ZC 与 VOBC 之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，见表 3。

<div style="text-align: center;">表 3 ZC 与 VOBC 通信的应用层信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0201</td><td style='text-align: center;'>列车控制信息</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr></table>

---

<div style="text-align: center;">表 3 ZC 与 VOBC 通信的应用层信息定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0205</td><td style='text-align: center;'>应用层注册/注销响应</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x0207</td><td style='text-align: center;'>ZC主动注销请求</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x0209</td><td style='text-align: center;'>特殊控制报文</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x020B</td><td style='text-align: center;'>ZC城市自定义帧</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020D</td><td style='text-align: center;'>ZC厂商自定义帧</td><td style='text-align: center;'>ZC→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0202</td><td style='text-align: center;'>列车位置信息</td><td style='text-align: center;'>V0BC→ZC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0206</td><td style='text-align: center;'>应用层注册/注销请求</td><td style='text-align: center;'>V0BC→ZC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x0208</td><td style='text-align: center;'>V0BC城市自定义帧</td><td style='text-align: center;'>V0BC→ZC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020A</td><td style='text-align: center;'>V0BC厂商自定义帧</td><td style='text-align: center;'>V0BC→ZC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr></table>

### 5.4 应用信息定义

#### 5.4.1 概述

本节中的“非法”值，正常通信时发送方不可能发送的非法取值。接收方收到GAL包中的应用信息帧中存在“非法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认为本周期末收到数据。

## 本章节中的“默认”值：

(a) 针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值。

(b) 设备在初始化完成前，无法确定状态时，相关字段取值发送“默认值”。接收方收到“默认”值后，应认为信息有效，不进行处理。

本节中涉及“上行”、“下行”的方向定义，均采用运营方向规定的上下行。跨线时，两条线路上下行运营方向定义不一致时，发送上下行方向信息的规则确定为：除特殊说明外，发送方按照自身所属线路（ZC 指所属线路，VOBC 指最大安全前端所在线路）上下行定义进行发送，由接收方适配处理。

本节中的“预留”字段，发送方统一填0，接收方可不对预留字段进行

---

校验。

本节中的轨道区段内的偏移量，基准点均为车载电子地图中，该轨道区段沿车载电子地图上行方向的起点。

#### 5.4.2 ZC 向 VOBC 发送信息

##### 5.4.2.1 列车控制信息

ZC 对满足 MA 发送条件的列车周期发送列车控制信息见表 4。

<div style="text-align: center;">表 4 列车控制信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>是否安全信息</td></tr><tr><td style='text-align: center;'>下一ZC ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>ZC IDMA终点到ZC边界或者越过ZC边界时设定该信息默认值:0x00000000如到达线路终端,填写默认值</td><td style='text-align: center;'>非安全信息</td></tr><tr><td rowspan="4">MA信息</td><td style='text-align: center;'>2</td><td style='text-align: center;'>MA信息长度从“MA方向”位到“信号机状态”所有字节长度有效范围:49~429</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>MA方向在MA起点朝向MA终点的方向,以MA起点处的上下行方向定义确定上行:0x55,下行:0xAA其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>停车保证请求有:0x55,无:0xAA其他非法停车保证功能可选,根据工程项目需求确定,如无此功能则默认填写无停车保证请求</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证请求序列号有效范围:1~(2²⁻¹-1)默认值:0xFFFFFFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td colspan="4">14</td></tr></table>

---

<div style="text-align: center;">表 4 列车控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>是否安全信息</td></tr><tr><td rowspan="10">MA信息</td><td style='text-align: center;'>—</td><td style='text-align: center;'>MA起点位置b</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm有效范围:0x0~0xFFFFFFE</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>安全防护点位置c</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm有效范围:0x0~0xFFFFFFE</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>障碍点信息c</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID默认值:0x00000000</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm有效范围:0x0~0xFFFFFFE默认值:0xFFFFFFFF</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>保护区段有效性(保护区段建立时有效)有效:0x55无效:0xAA默认值:0xFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td rowspan="4">路径信息</td><td style='text-align: center;'>2</td><td style='text-align: center;'>道岔信息个数(MA内包含的道岔,个数为变量,有效范围:0~20)d</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>道岔(1)信息</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>道岔状态定位:0x55,反位:0xAA,其他非法</td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 4 列车控制信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>是否安全信息</td></tr><tr><td rowspan="2">路径信息</td><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>道岔(X)信息,X是道岔信息个数字段取值</td><td style='text-align: center;'>安全信息</td></tr><tr><td rowspan="6">PSD状态</td><td style='text-align: center;'>2</td><td style='text-align: center;'>PSD信息数(MA内包含的PSD,个数为变量,有效范围:0~10)</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>PSD(1)信息</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>PSD状态非关闭且锁闭:0x55关闭且锁闭:0xAA互锁解除:0xCC其他非法若ZC无互锁解除相关功能,可将互锁解除视为“关门”处理</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>PSD(Y)信息,Y是PSD信息个数字段取值</td><td style='text-align: center;'>安全信息</td></tr><tr><td rowspan="5">ESB状态</td><td style='text-align: center;'>2</td><td style='text-align: center;'>ESB信息个数(MA内包含的ESB,个数为变长,有效范围:0~10)</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>ESB(1)信息</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>ESB状态按下:0x55,未按下:0xAA其他:非法</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 4 列车控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>是否安全信息</td></tr><tr><td style='text-align: center;'>ESB状态*</td><td style='text-align: center;'>—</td><td style='text-align: center;'>ESB(Z)信息,Z是ESB信息个数字段取值</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>无人折返按钮状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>无人折返按钮状态(列车停靠无人折返站台时发送) 按下:0x55,未按下:0xAA(默认值)</td><td style='text-align: center;'>非安全信息</td></tr><tr><td rowspan="12">临时限速信息*</td><td style='text-align: center;'>2</td><td style='text-align: center;'>临时限速信息个数(个数为变长,有效范围:0~10)</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>临时限速(口信息)</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>终端位置</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区间中偏移量,单位:cm有效范围:0x0~0xFFFFFE</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>终端位置</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区间中偏移量,单位:cm有效范围:0x0~0xFFFFFE</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>预留</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>临时限速值:单位:km/h(0km/h~254km/h)0xFF;默认值</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>…</td><td style='text-align: center;'>…</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>临时限速(10)信息</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>ZC-ZC通信延迟</td><td style='text-align: center;'>2</td><td style='text-align: center;'>计算跨边界点MA时,ZC与相邻ZC的通信延时,单位:ms有效范围:0~10 000</td><td style='text-align: center;'>安全信息</td></tr></table>

---

<div style="text-align: center;">表 4 列车控制信息（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>是否安全信息</td></tr><tr><td style='text-align: center;'>紧急制动命令 $ ^{b} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>是否有紧急制动命令有:0x55无:0xAA</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>运行目的地属性信息</td><td style='text-align: center;'>1</td><td style='text-align: center;'>MA终点处目的地属性通过:0x55折返:0xAA回段:0xCC默认值:0xFF若ZC无相关功能,则发送默认值。若ATP无相关功能,则接收此信息时不进行处理</td><td style='text-align: center;'>非安全信息</td></tr><tr><td rowspan="2">信号机状态</td><td style='text-align: center;'>4</td><td style='text-align: center;'>信号机的IDZC接收到的V0BC发送的信号机ID</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>“信号机的ID”的信号机状态CBTC允许信号:0x55;CBTC禁止信号:0xAA、默认值0xFF(该方向无信号机时填“否”)</td><td style='text-align: center;'>安全信息</td></tr><tr><td colspan="4">1.当有停车保证请求时,停车保证请求对应位置即为安全防护点位置;2.被人解的进路的首区段为前一条进路的保护区段,且保护区段锁闭时,如列车能给出在保护区段内的停车保证,此时进路应立即解锁;3.ZC每次生成停车保证请求时,应更新停车保证请求序列号,无停车保证请求时,停车保证请求序列号应为默认值;4.停车保证的发起ZC应保证自身可区分不同的停车保证命令及响应。1.ZC发送MA时,MA起点位置应在最小安全后端至最小安全后端后延一个列车最不利情况下的最大回退距离范围之内(含此范围的两端端点)。2.列车移交时,若接管ZC发给列车的MA起点为最小安全后端向后延伸一定距离,若无移交ZC的MA,则此延伸距离应不超过ZC移交边界。3.V0BC允许列车退行时,应能允许退行过程中列车安全包络车尾部分区域不在MA范围内。</td></tr></table>

---

## 表 4 列车控制信息(续)

1. ZC 向 VOBC 发送的 MA 信息包括：

安全防护点：列车绝对不能突破的点；

障碍点：保护区段有效时，主进路内最后一个计轴区段的终点；

保护区段状态：有效、无效或默认。





2. 安全防护点位置和障碍点位置的发送规则为：如果 ZC 发送的“保护区段有效性”字段取值为“有效”，ZC 发送的安全防护点位置应确保列车可正常进站停车，同时应确保安全性，障碍点为保护区段起点位置；如果 ZC 发送的“保护区段有效性”字段取值为“无效”或默认值，则 ZC 发送的障碍点信息为无效值；当 MA 终点对应的防护点为红灯信号机，且该信号机防护进路的前一条进路无保护区段时，安全防护点不应越过该红灯信号机防护的进路起点；ZC 计算安全防护点信息时，应包含设备安装相关的安全余量

3. VOBC 接收移动授权的处理方法为：



(1) VOBC 接收到来自 ZC 的 MA 信息后：

按照安全防护点位置进行列车紧急制动曲线计算；

VOBC 实现列车进站停准功能，应不受 ZCMA 过长的影响。

(2) 在任何情况下，如果列车闯过障碍点，VOBC 应立即紧急制动。

 $ ^{4} $ ZC 发送道岔状态信息规则：MA 范围内若包含道岔岔尖位置，则应发送该道岔状态（适用于道岔三段式轨道区段描述方案）。

ZC 发送道岔信息的顺序应沿从 MA 起点向安全防护点方向排列

MA 范围内的 PSD/ESB 防护区域激活时，ZC 向 VOBC 发送的 MA 不应回缩，由 VOBC 根据 MA 范围内的 PSD/ESB 状态对列车进行控制。

 $ ^{1} $ 无临时限速的区域，不发送临时限速命令；

ZC 向 VOBC 发送的临时限速命令中，两个临时限速命令不应存在重叠区域；

ZC 向 VOBC 发送的临时限速命令范围不应超出 MA 范围（起点到安全防护点范围）；

临时限速命令顺序应沿从 MA 起点向安全防护点方向排列；

临时限速命令始端位置指向终端位置的方向应与 MA 起点指向终点的方向相同。

若 MA 跨过边界点，则填写计算该 MA 时所使用的相邻 ZC 的信息包的延时；若 MA 未跨过边界点，则填写 0。V0BC 判断 MA 的有效性时，应扣除该延时。

1. ZC 判断可为车载 VOBC 计算有效 MA，但需要 VOBC 输出紧急制动时，发送“有紧急制动命令”信息；

2. 若 ZC 无相关功能，“紧急制动命令”字段发送“无命令”；

---

<div style="text-align: center;">表 4 列车控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>3. VOBC收到受控ZC发送的“有紧急制动命令”信息后，应输出紧急制动，但不因为此信息导致列车驾驶模式降级；4. VOBC收到受控ZC发送的“有紧急制动命令”信息时，应不可缓解紧急制动。当允许列车MA越过以该信号机为始端的进路时，发送CBTC允许状态；当不允许列车MA越过以该信号机为始端的进路时，发送CBTC禁止状态。</td></tr></table>

##### 5.4.2.2 应用层安全连接 注册/注销响应

对于车载发送的注册/注销请求，ZC返回该报文见表5。

<div style="text-align: center;">表 5 注册/注销响应信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>注册/注销响应</td><td style='text-align: center;'>1</td><td style='text-align: center;'>注册成功:0x55,注册失败:0xAA注销成功:0xCC其他非法</td><td style='text-align: center;'>非安全信息</td></tr><tr><td style='text-align: center;'>注册失败原因</td><td style='text-align: center;'>1</td><td style='text-align: center;'>错误代码0x**:注册失败原因(根据业主要求定义)0xFF:默认值,注册成功或注销成功时填写</td><td style='text-align: center;'>非安全信息</td></tr><tr><td style='text-align: center;'>预留</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td></tr></table>

##### 5.4.2.3 ZC 主动注销请求

ZC 的注销条件成立时，该信息定义见表 6。

<div style="text-align: center;">表 6 注销命令</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>注销命令</td><td style='text-align: center;'>1</td><td style='text-align: center;'>注销请求:0x55 其他非法</td><td style='text-align: center;'>非安全信息</td></tr></table>

---

<div style="text-align: center;">表 6 注销命令(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>注销原因</td><td style='text-align: center;'>1</td><td style='text-align: center;'>错误代码：(根据业主要求定义)</td><td style='text-align: center;'>非安全信息</td></tr><tr><td style='text-align: center;'>预留</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td></tr><tr><td colspan="4">注1：“ZC主动注销请求”包与“列车控制信息”包、“特殊控制报文”包在同一GAL包中不应同时存在。注2：ZC发送“ZC主动注销请求”包后，应持续发送“ZC主动注销请求”包，不接受VOBC发送的除“注销信息包”外的其他信息，直至收到VOBC发送的“注销信息包”或判断通信超时。注3：VOBC收到“ZC主动注销请求”包后，应向ZC发送“注销信息包”。</td></tr></table>

##### 5.4.2.4 特殊控制命令

特殊控制报文定义见

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bf1f8793-943f-477a-9e8f-5526008ec0d2/markdown_0/imgs/img_in_seal_box_284_496_589_620.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A39%3A19Z%2F-1%2F%2Fb02e5e90b74788a826e45a07871e1fbfda1a4ade285d551cc136d5df822ac0c2" alt="Image" width="36%" /></div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td rowspan="2">特殊控制报文</td><td style='text-align: center;'>1</td><td style='text-align: center;'>紧急制动命令有命令:0x55无命令:0xAA其他:非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>特殊控制原因,工程约定</td><td style='text-align: center;'>非安全信息</td></tr><tr><td colspan="4">注1:“特殊控制报文”包与“列车控制信息”包在同一GAL包内不应同时存在。注2:非注销过程中,不满足发送“列车控制信息”的条件,应发送特殊控制报文包。注3:ZC判断不需列车紧急制动,但需保持链路时,发送特殊控制报文包,且“紧急制动命令”字段取值为“无命令”。注4:当V0BC收到的特殊控制报文中“紧急制动命令”字段为“无命令”时,应不因此原因发生紧急制动,并保持与ZC的安全连接。</td></tr></table>

---

##### 5.4.2.5 ZC城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。ZC城市自定义帧信息见表8。

<div style="text-align: center;">表 8 ZC 城市自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

##### 5.4.2.6 ZC厂商自定义帧

自定义信息，用于实现各厂商特有功能，各厂商分别定制。ZC 判断通信的 VOBC 与自身属于同一厂商时，方可发送厂商自定义帧。ZC 厂商自定义帧信息见表 9。

<div style="text-align: center;">表 9 ZC 厂商自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

#### 5.4.3 VOBC 向 ZC 发送信息

##### 5.4.3.1 列车位置信息

该信息周期发送，用来维持 ZC 设备和 VOBC 间安全通信的连续性。

列车在 ZC 间移交过程中，VOBC 与移交、接管 ZC 同时通信时，同一周期生成的向两个 ZC 发送的“列车位置信息包”内容应一致。

列车位置信息包内容见表10。

<div style="text-align: center;">表 10 列车位置信息内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>运行方向a</td><td style='text-align: center;'>1</td><td style='text-align: center;'>最小安全后端指向最大安全前端的方向，以最小安全后端处的上下行方向确定上行：0x55</td><td style='text-align: center;'>安全信息</td></tr></table>

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>运行方向*</td><td style='text-align: center;'>1</td><td style='text-align: center;'>下行:0xAA
默认:0xFF
其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>激活端</td><td style='text-align: center;'>1</td><td style='text-align: center;'>本V0BC是否为激活端(首尾冗余的V0BC统一发送是激活端)
激活端:0x55
非激活端:0xAA
其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td rowspan="10">列车包络线</td><td style='text-align: center;'>—</td><td style='text-align: center;'>列车最大安全前端位置</td><td rowspan="10">安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID*
默认值:0x00000000</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段内偏移量,单位:cm
有效范围:0x0~0xFFFFFFF
默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>列车最小安全前端位置</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID*
默认值:0x00000000</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm,有效范围:0x0~0xFFFFFFF*
默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>列车最大安全后端位置</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID*
默认值:0x00000000</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm,有效范围:0x0~0xFFFFFFF*
默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>列车最小安全后端位置</td></tr></table>

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td rowspan="4">列车包络线</td><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID $ ^{a} $ 默认值:0x00000000</td><td rowspan="4">安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>区段内偏移量,单位:cm,有效范围:0x0~0xFFFFFFE $ ^{a} $ 默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>列车长度,单位:cm,有效范围:1000~50000</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>列车车头第一轮对到车钩长度(单位:cm),有效范围:1~1000</td></tr><tr><td style='text-align: center;'>列车运行控制级别 $ ^{b} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x01:CBTC;0x02:点式;0x03:联锁控制级别;其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>列车驾驶模式 $ ^{b} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x01:AM;0x02:CM;0x03:RM;0x04:EUM;其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td rowspan="4">车辆状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>停车保证响应 $ ^{c} $ 0x55:可以停车;0xAA:无法停车;0xFF:默认值;其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证响应序列号 $ ^{c} $ 有效范围:1~(2 $ ^{31} $ -1)默认值:0xFFFFFFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证对应安全防护点轨道区段ID $ ^{c} $ 默认值:0x00000000</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证对应安全防护点区段内偏移量,单位:cm,有效范围:0x0~0xFFFFFFF $ ^{c} $ 默认值:0xFFFFFFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td colspan="4">24</td></tr></table>

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td rowspan="6">车辆状态</td><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证对应障碍点轨道区段ID $ ^{*} $ 
默认值:0x00000000</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>停车保证对应障碍点区段内偏移量,单位:cm,有效范围:0x0~0xFFFFFFF $ ^{*} $ 
默认值:0xFFFFFFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>停车保证对应保护区段有效性 $ ^{*} $ 
有效:0x5A
无效:0xAA
默认值:0xFF
其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>折返状态(AR状态,折返时车尾OBC注册后,到折返流程完成之前的状态)
0x55:AR状态;0xAA:非AR状态
其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>列车完整性
0x55:完整
0xAA:不完整
其他:非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>无人折返指示灯
0x55:折返指示灯常亮
0xAA:折返指示灯常灭
0xCC:折返指示灯闪烁
其他非法
若地面设备无折返指示灯闪烁功能,可将折返指示灯闪烁作为常亮处理;若车载设备无折返指示灯闪烁功能,可不发送折返指示灯闪烁信息</td><td style='text-align: center;'>非安全信息</td></tr></table>

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>车辆状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>紧急制动状态0x55:车载ATP采集到车辆反馈未实施紧急制动0xAA:车载ATP采集到车辆反馈已实施紧急制动其他:非法</td><td style='text-align: center;'>非安全信息</td></tr><tr><td rowspan="5">列车速度/距离信息</td><td style='text-align: center;'>2</td><td style='text-align: center;'>列车速度,单位:cm/s有效范围:0~15 000</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>速度方向(车轮旋转的方向)0x55:前(停车时是向前)0xAA:后其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>退行距离,单位:cm最不利情况下,列车从开始退行到停车的走行距离。有效范围:1~5 000默认值:0xFFFF</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>停准停稳信息0x55:停准且停稳0xAA:未停稳0xCC:停稳但未停准其他:非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>保护区段允许解锁0x55:允许解锁0xAA:不允许解锁其他非法</td><td style='text-align: center;'>安全信息</td></tr><tr><td style='text-align: center;'>受控ZCID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>受控ZC(列车采用MA/特殊控制报文的ZC)的ID默认值:0x00000000车载V0BC未采用MA和特殊控制报文时发送默认值</td><td style='text-align: center;'>安全信息</td></tr></table>

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>信号机 IDf</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0 为默认值V0BC 最大安全前端前方沿列车运行方向可搜索到的最近的同向信号机,V0BC 发送“保护区段允许解锁”字段为允许解锁时,该信号机 ID 应为有效值</td><td style='text-align: center;'>安全信息</td></tr><tr><td colspan="4">*1. 若 V0BC 与 ZC 建立通信时无法确定准确位置,则“运行方向”、“列车最大安全前端位置所在轨道区段 ID”、“列车最大安全前端位置在轨道区段内偏移量”、“列车最小安全前端位置所在轨道区段 ID”、“列车最小安全前端位置在轨道区段内偏移量”、“列车最大安全后端位置所在轨道区段内偏移量”、“列车最小安全后端位置所在轨道区段 ID”、“列车最小安全后端位置在轨道区段内偏移量”均填写默认值(列车安全位置示意如图 5 所示)。2. V0BC 应保证:若“运行方向”、“列车最大安全前端位置所在轨道区段 ID”、“列车最大安全前端位置在轨道区段内偏移量”、“列车最小安全前端位置所在轨道区段 ID”、“列车最小安全前端位置在轨道区段内偏移量”、“列车最大安全后端位置所在轨道区段 ID”、“列车最小安全后端位置在轨道区段内偏移量”、“列车最小安全后端位置所在轨道区段内偏移量”字段中,任一字段取值为默认值,则“运行方向”、“列车最大安全前端位置所在轨道区段 ID”、“列车最大安全前端位置在轨道区段内偏移量”、“列车最小安全前端位置所在轨道区段 ID”、“列车最小安全前端位置在轨道区段内偏移量”、“列车最大安全后端位置所在轨道区段 ID”、“列车最大安全后端位置在轨道区段内偏移量”、“列车最小安全后端位置所在轨道区段 ID”、“列车最小安全后端位置在轨道区段内偏移量”、“停车保证响应”、“停车保证响应序列号”、“停车保证对应安全防护点轨道区段 ID”、“停车保证对应安全防护点轨道区段内偏移量”、“停车保证对应障碍点轨道区段 ID”、“停车保证对应障碍点轨道区段偏移量”、“停车保证对应保护区段有效性”字段取值应都为默认值。3. ZC 收到位置报告默认值后,若之前无列车有效位置,可选择以下处理之一:(1) 发送主动注销请求;(2) 不向 V0BC 发送任何信息;(3) 保持通信,发送“紧急制动”的特殊控制报文包,但将列车作为非通信车处理。</td></tr></table>

---

## 表 10 列车位置信息内容(续)

若之前有列车有效位置，可选择以下处理之一：

(1) 发送主动注销请求；

(2) 不向 VOBC 发送任何信息；



(3) 丢弃此位置报告信息，采用之前的位置报告，继续与 VOBC 通信，直至通信超时断开。

4. 各家 VOBC 在发送位置报告默认值时，应能分别适配 ZC 上述处理。若 ZC 收到 VOBC 发送的位置报告，且判断列车位置报告不在本 ZC 线路数据（含本 ZC 管辖范围及其他 ZC 管辖范围内与本 ZC 的重叠区）范围内，可选择以下处理之一：



(1) 持续发送特殊控制报文；

(2) 发送 ZC 主动注销请求；

(3) 不向 VOBC 发送任何信息；



(4) 各家 VOBC 应能分别适配 ZC 上述处理。

1. “列车运行控制级别”与“列车驾驶模式”字段取值应满足表11的要求。

2. 列车折返过程中，若头端、尾端 VOBC 存在同时与 ZC 通信过程，则原尾端 VOBC 与 ZC 建立通信，且未收到 ZC 的有效列车控制信息时，向 ZC 发送的“列车运行控制级别”、“列车驾驶模式”字段，取值应为原头端的“列车运行控制级别”、“列车驾驶模式”字段取值。

1. VOBC仅根据“当前使用”的MA消息中是否有停车保证请求作出应答，不负责记忆之前是否有停车保证；



2.“停车保证响应序列号”字段，取值为V0BC采信的停车保证对应的“停车保证请求序列号”取值；

3. 当无停车保证请求时，“停车保证请求对应安全防护点轨道区段ID”、“停车保证请求对应安全防护点轨道区段偏移量”、“停车保证请求对应障碍点轨道区段ID”、“停车保证请求对应障碍点轨道区段偏移量”、“停车保证请求对应保护区段有效性”、“停车保证响应”、“停车保证响应序列号”字段发送默认值；

4. ZC 收到 VOBC 发送的停车保证响应时，应判断停车保证响应序列号、停车保证对应位置与自身发送的停车保证请求信息一致方可采信。

此处的最不利情况，指列车退行至最大允许距离时，

1. 速度为最大退行允许速度；

2. 加速度为最大值；









3. 列车位于最大坡度（退行方向为下坡），且列车切牵引生效时间、紧急制动生效时间等安全制动模型相关延时均为最大值。

---

<div style="text-align: center;">表 10 列车位置信息内容(续)</div>


1. VOBC 发送“允许解锁”信息后，应保证列车不会进入前方保护区段；

2. 地面设备收到“允许解锁”信息后，可解锁列车前方保护区段

地面设备收到“允许解锁”信息后，可按照以下两种方式之一解锁列车前方保护区段：

(1) 解锁列车最大安全前端所在进路对应的保护区段；

(2) 解锁 VOBC 发送的信号机 ID 对应的保护区段。

VOBC 判断满足下列条件时，应发送列车最大安全前端所在进路对应保护区段“允许解锁”信息（此外进路指列车最大安全前端所在进路）：

(1) 列车在进路终端信号机防护点前停稳

(2) 列车最大安全前端末越过估计位置所在进路末端位置

(3) 进路终端信号机未开放；具体判断原则如下：

CBTC级别下，V0BC通证障碍点及安全防护点位置与进路末端位置关系判断：(1)若MA信息内障碍点有效，比障碍点位置不在进路末端，则认为终端信号机开放；(2)若MA信息内障碍点有效，且障碍点位置在进路末端，则为终端信号机未开放；(3)若MA信息内障碍点无效，且安全防护点越过进路终点，则认为终端信号机开放；(4)若MA信息内障碍点无效，且安全防护点未越过进路终点，则认为终端信号机未开放。

点式级别下根据CI发送的信号机状态，判断信号机是否开放，且不再需要此进路的保护区段；列车在进路终端信号机上游且位于本进路内的停车窗停准且停稳时应认为不再需要；列车越过进路终端信号机上游且位于本进路内的停车窗停稳时可认为不再需要

V0BC 滑列车运行方向搜索最近的同向信号机时，搜索范围不能超过未知状态的道岔。

<div style="text-align: center;">表 11 控制级别与驾驶模式对应关系</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>EUM</td><td style='text-align: center;'>RM</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>AM</td></tr><tr><td style='text-align: center;'>连续式列车控制级别</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>○</td><td style='text-align: center;'>○</td></tr><tr><td style='text-align: center;'>点式列车控制级别</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td><td style='text-align: center;'>○</td><td style='text-align: center;'>○</td></tr><tr><td style='text-align: center;'>联锁控制级别</td><td style='text-align: center;'>○</td><td style='text-align: center;'>○</td><td style='text-align: center;'>×</td><td style='text-align: center;'>×</td></tr><tr><td colspan="5">注：×/○表示该控制级别下不具有/具有该驾驶模式。</td></tr></table>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//64a6c794-bf43-4d9d-bb00-bc11877efe48/markdown_0/imgs/img_in_image_box_93_123_814_388.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A39%3A53Z%2F-1%2F%2Fb41e4aea6cddc60b13cef3a3b5f91ff1ae00f975f34f52d691a95bd28a5d9f8c" alt="Image" width="85%" /></div>


<div style="text-align: center;">图 5 列车安全位置示意图</div>


##### 5.4.3.2 应用层注册/注销请求

V0BC 满足注册/注销条件时，应重复发送该信息。

VOBC 的带有“应用层注册/注销请求”信息包的 GAL 包中，应不带有“列车位置信息”包。

注册注销请求内容见表12。

<div style="text-align: center;">表 12 注册注销请求</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td><td style='text-align: center;'>使用方式</td></tr><tr><td style='text-align: center;'>注册/注销请求</td><td style='text-align: center;'>1</td><td style='text-align: center;'>注册请求:0x55;注销请求:0xCC其他非法</td><td style='text-align: center;'>非安全信息</td></tr><tr><td style='text-align: center;'>注销原因</td><td style='text-align: center;'>1</td><td style='text-align: center;'>切换注销:0x01*和所有连接ZC注销:0x02其他原因:0xFF其他取值非法注册请求时,填写0xFF</td><td style='text-align: center;'>非安全信息</td></tr><tr><td style='text-align: center;'>预留</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0</td><td style='text-align: center;'></td></tr><tr><td colspan="4">&quot;V0BC开始向ZC发送&quot;注册信息包&quot;时,由于此时V0BC未收到过ZC的信息,故&quot;注册信息包&quot;中,GAL包帧头中的&quot;对方消息序列号&quot;、&quot;收到上一条消息时本方序列号&quot;字段取值为默认值。ZC收到此类&quot;注册信息包&quot;后,无法判断该信息包是否超时,此时ZC应回复空GAL包(GAL包帧头中&quot;应用层数据长度&quot;为0,且无应用层数据),此空GAL包帧头中的&quot;对方消息序列号&quot;、&quot;收到</td></tr></table>

---

<div style="text-align: center;">表 12 注册注销请求(续)</div>


上一条消息时本方序列号"字段取值应根据收到的“注册信息包”填写有效值。

为提高系统可用性，ZC与V0BC建立安全连接后，ZC未收到V0BC发送的注册信息包前，可周期发送空GAL包（此功能不强制要求）。

VOBC 与 ZC 间的注册流程为：

a) VOBC 判断满足注册条件后，向 ZC 发送“应用层注册/注销”信息包，其中“注册/注销请求”字段取值为“注册请求”（下简称该包为“注册信息包”）；

b) VOBC 开始发送“注册信息包”后，应持续发送，直至收到 ZC 发送的“应用层注册/注销响应”信息包，且“注册/注销响应”字段的取值为“注册成功”（下简称该包为“注册成功响应包”）后，停止发送“注册信息包”，开始发送“列车位置信息”包；

c）ZC收到V0BC发送的“注册信息包”，且判断满足注册条件后，应持续发送“注册成功响应包”，直至收到V0BC发送的“列车位置信息”包，方可发送“特殊控制报文”或“列车控制信息”包。V0BC与ZC间的注销流程为：

a）VOBC 判断满足注销条件后，应向 ZC 发送“应用层注册/注销”信息包，其中“注册/注销请求”字段取值为“注销请求”（下简称该包为“注销信息包”）。

b）ZC收到VOBC发送的“注销信息包”，且判断满足注销条件后，应发送“应用层注册/注销响应”信息包，且“注册/注销响应”字段的取值为“注销成功”（下简称该包为“注销成功响应包”）。

c）ZC 开始发送“注销成功响应包”后，应持续发送，直至判断 VOBC 断开安全连接或判断通信超时。

d) VOBC 开始发送“注销信息包”后，应不接受 ZC 发送的“注销成功响应包”之外的其他信息，并持续发送“注销信息包”，直至收到 ZC 发送的“注销成功响应包”或判断通信超时。VOBC 收到 ZC 发送的“注销成功响应包”后应主动断开安全连接。

---

注：列车在 ZC 间切换过程中，完成切换后，V0BC 与接管 ZC 保持通信，与移交 ZC 断开通信时，向移交 ZC 发送的注销原因为“切换注销”；V0BC 判断与连接的所有 ZC 均需断开连接（含只与一个 ZC 连接的情况），则向所有 ZC 发送的注销原因均为“和所有连接 ZC 注销”；其他情况下的注销，V0BC 向注销 ZC 发送的注销原因为“其他原因”。

##### 5.4.3.3 VOBC 城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。VOBC城市自定义帧信息见表13。

<div style="text-align: center;">表 13 VOBC 城市自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

##### 5.4.3.4 VOBC 厂商自定义帧

自定义信息，用于实现各厂商特有功能，各厂商分别定制。V0BC 判断通信的 ZC 与自身属于同一厂商时，方可发送厂商自定义帧。V0BC 厂商自定义帧信息见表 14。

<div style="text-align: center;">表 14 VOBC 厂商自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

### 5.5 折返流程说明

折返流程分为首尾端 VOBC 共用安全连接与首尾端 VOBC 不共用安全连接两种情况。本节中 VOBC1 指换端前的车头 VOBC, VOBC2 指换端前的车尾 VOBC。

#### 5.5.1 首尾 VOBC 共用安全连接

此种情况下，VOBC 在红蓝网上分别与 ZC 建立安全连接，冗余消息在红蓝网上分别传输（红网 IP 对红网 IP，蓝网 IP 对蓝网 IP）。首尾 VOBC 共同使用这组安全连接，首尾 VOBC 共用一个 VID。ZC 不区分首

---

尾端 VOBC

折返过程如下：

a) VOBC 与 ZC 正常通信，向 ZC 发送 VOBC1 方向的“列车位置信息”包，ZC 向 VOBC 发送 VOBC1 方向的“列车控制信息”包；

b) 折返开始后，V0BC 应停止发送 V0BC1 方向的“列车位置信息”包，改为发送 V0BC2 方向的“列车位置信息”包，V0BC 应保证列车换端过程中，列车安全包络不超出折返轨范围；

(c) ZC 根据收到的 VOBC“列车位置信息”包判断列车方向发生改变且列车安全包络完全处于折返轨内，则认为列车换端，开始向 VOBC 发送 VOBC2 方向的“列车控制信息”包；

d) VOBC 收到 VOBC2 间的“列车控制信息”包后，开始据此控制列车，若移动授权终点超过换端后的最大安全前端一定距离（暂定 0.5 m 可配置，具体数值在工程中约定），则 VOBC 应能够保持 CBTC 等级，折返流程结束。

#### 5.5.2 首尾 VOBC 不共用安全连接

此种情况时车载首尾 VOBC 使用不同的 ID，首尾 VOBC 分别与 ZC 建立安全连接。在折返过程中，车尾 VOBC 与 ZC 新注册建立一条安全连接。此时 VOBC1、VOBC2 同时与 ZC 通信，分别维护安全连接。换端完成后，VOBC1 注销与 ZC 的连接，仅保留 VOBC2 的连接（与折返前相比，与 ZC 通信的车载设备的红蓝网 IP 地址发生了切换）。首尾 VOBC 采用不同的 VID。

折返流程如下：

a） VOBC1 与 ZC 正常通信，向 ZC 发送本端“列车位置信息”包，ZC 向 VOBC1 发送“列车控制信息”包。

b）折返开始后，VOBC2与ZC新建立安全连接，并发起注册，通信建立后，VOBC2判断列车停稳后向ZC发送本端“列车位置信息”包，其中“折返状态”内容应为“AR状态”，VOBC应保证列车换端过程中，列车安全包络不超出折返轨范围。

c） ZC 与 VOBC1、VOBC2 同时保持通信，向两 VOBC 发送的内

---

容为：

1）向两 VOBC 分别发送该端的“列车控制信息”包；

2）向一端 VOBC 发送该端的“列车控制信息”包，向另一端发送“特殊控制报文”包，其中“紧急制动命令”字段取值应为“无命令”。

ZC 根据两端 VOBC 发送的“列车位置信息”包中的“激活端”与

“AR 状态”字段判断向两端发送的信息内容。规则为：

- 若两端“列车位置信息”包中的“激活端”信息均为“非激活端”，则向两端同时发送“特殊控制报文”包。

若两端“列车位置信息”包中有且仅有一端的“激活端”信息为“激活端”，则向该端发送“列车控制信息”包，向另一端发送“特殊控制报文”包；

若两端“列车位置信息”包中的“激活端”信息均为“激活端”，则判断“AR状态”：若有且仅有一端的“AR状态”为“AR状态”，则向该端发送“列车控制信息”包，向另一端发送“特殊控制报文”包；若两端“AR状态”均为“AR状态”或“非AR状态”，则向两端同时发送“特殊控制报文”包。

1）车载方应确保 ZC 同时收到 VOBCI 端的“激活端”信息为“激活端”，VOBC2 的“激活端”信息为“激活端”，且 VOBC2 的“AR 状态”为“AR 状态”；之后 VOBCI 的“激活端”信息方可变为“非激活端”，并可开始注销，VOBCI 应在 VOBC2 的列车最大安全前端出清折返区域前向 ZC 发出注销请求。

2）VOBC2 收到 ZC 发送的 VOBC2 方向的“列车控制信息”包之前，车载方应保证 VOBC1、VOBC2 发送的列车安全包络偏差不超过 20 cm。

3）VOBC2 收到 VOBC2 方向的“列车控制信息”包后，开始据此控制列车，若移动授权终点超过换端后的最大安全前端

---

一定距离（暂定0.5 m，可配置，具体数值在工程中约定），则V0BC2应能够保持CBTC等级。

4）换端完成后，V0BC1向ZC发送注销请求，断开与ZC的连接。

5）车载方应确保，VOBC1与ZC注销完成或断开通信后，VOBC2向ZC发送的本端列车位置信息中“折返状态”内容方可改为“非AR状态”。

## 6 VOBC - ATS 报文规范

### 6.1 接口连接方式

#### 6.1.1 物理接口

VOBC 与 ATS 之间采用冗余网络进行通信。ATS 与 VOBC 之间的网络拓扑结构采用 A 网 - A 网、B 网 - B 网两个链路。

#### 6.1.2 安全通信协议

ATS 与 VOBC 之间通信可采用 RSSP-Ⅱ或 RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅱ铁路信号安全通信协议》；RSSP-Ⅰ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅰ铁路信号安全通信协议》。采用 RSSP-Ⅰ安全通信协议的前提条件为使用 LTE-M 通信且 LTE-M 具备空口加密措施可防止伪装、CBTC 信号系统符合三级等保要求。在此前提条件下，宜采用 RSSP-Ⅰ安全通信协议。

如图 6 所示，其 SAI/MASL/ALE 三层，遵循 RSSP-Ⅱ标准规定。

TCP 及 IP 层使用标准 TCP/IP 协议栈。

MAC 及 PHY 层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。

如图 7 所示, 其 RSSP-I 协议遵循 RSSP-I 标准规定。

UDP 层使用标准 UDP 协议栈。

MAC 及 PHY 层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//966231d9-b860-49ca-9556-bc5944fb0923/markdown_0/imgs/img_in_image_box_162_135_794_610.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A40%3A13Z%2F-1%2F%2F209f8c597bb79fad789b668bb03ce6072fe58fafacae02b0475419f0de5ce5b4" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 6 无线安全通信协议 RSSP - II 构架</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//966231d9-b860-49ca-9556-bc5944fb0923/markdown_0/imgs/img_in_image_box_133_679_794_1082.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A40%3A13Z%2F-1%2F%2F3ea3f709bceac471d91735d0d80759b65ad5f5987556b83a3afcf5fb7e6bdd5e" alt="Image" width="78%" /></div>


<div style="text-align: center;">图 7 无线安全通信协议 RSSP-I 构架</div>

---

#### 6.1.3 动态交互描述

##### 6.1.3.1 通信应用层消息包定义

将 ATS-VOBC 间每个周期需要交互的应用信息通过组成通用消息包进行传输，如图 8 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d225c60e-345a-4018-b8fa-5438dd151288/markdown_0/imgs/img_in_image_box_213_252_652_378.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A40%3A20Z%2F-1%2F%2Fd8873691d096e153000492da9814a0c3cd88161234ff4bc776f5f2859d36c6fe" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 8 通用消息包和应用层信息包关系结构图</div>


##### 6.1.3.2 信息包格式定义

ATS/V0BC 每周期最多允许发送 1 个通用消息包，通用消息包中包含 ATS 与 V0BC 之间传输的各条应用信息。

每个通用消息包总长不得超过1 000字节，格式定义见表15和表16。

表 15 通用信息包格式定义


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">接口信息类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型值位</td><td rowspan="2">数字</td><td rowspan="2">0x0204: ATS - VOBC 接口</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td style='text-align: center;'>3</td><td rowspan="4">源 ID</td><td rowspan="4">4 字节</td><td rowspan="4">发送方设备 ID</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>6</td></tr><tr><td rowspan="4">接收方标识信息</td><td style='text-align: center;'>7</td><td rowspan="4">目的 ID</td><td rowspan="4">4 字节</td><td rowspan="4">接收方设备 ID</td></tr><tr><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>9</td></tr><tr><td style='text-align: center;'>10</td></tr></table>

---

<div style="text-align: center;">表 15 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节
编号</td><td style='text-align: center;'>字    段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="4">数据版本校验
信息 $ ^{a} $</td><td style='text-align: center;'>11</td><td rowspan="4">ATS与V0BC
之间的版本
一致性信息</td><td rowspan="4">4字节</td><td rowspan="4">ATS管辖范围内,ATS与
V0BC间的数据版本校验信息</td></tr><tr><td style='text-align: center;'>12</td></tr><tr><td style='text-align: center;'>13</td></tr><tr><td style='text-align: center;'>14</td></tr><tr><td rowspan="4">本方消息
序列号 $ ^{b} $</td><td style='text-align: center;'>15</td><td rowspan="4"></td><td rowspan="4">4字节</td><td rowspan="4">记录发送本条消息时,本方
的周期计数</td></tr><tr><td style='text-align: center;'>16</td></tr><tr><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>18</td></tr><tr><td rowspan="2">通信周期</td><td style='text-align: center;'>19</td><td rowspan="2"></td><td rowspan="2">2字节</td><td rowspan="2">设备通信周期,单位:ms</td></tr><tr><td style='text-align: center;'>20</td></tr><tr><td rowspan="4">对方消息
序列号 $ ^{b} $</td><td style='text-align: center;'>21</td><td rowspan="4"></td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息中
的对方消息序列号
默认值:0xFFFFFFF $ ^{c} $</td></tr><tr><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>24</td></tr><tr><td rowspan="4">收到上一条
消息时本方
序列号 $ ^{b} $</td><td style='text-align: center;'>25</td><td rowspan="4"></td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息
时,本方的周期计数
默认值:0xFFFFFFF $ ^{c} $</td></tr><tr><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>协议版本号 $ ^{a} $</td><td style='text-align: center;'>29</td><td style='text-align: center;'>协议版本号</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>V0BC-ATS的协议版本,本
规范定义为20</td></tr><tr><td rowspan="2">应用层数据
长度</td><td style='text-align: center;'>30</td><td rowspan="2">应用层数据长度</td><td rowspan="2">2字节</td><td rowspan="2">“应用层数据”报文结束的字
节数</td></tr><tr><td style='text-align: center;'>31</td></tr></table>

---

<div style="text-align: center;">表 15 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>32~1000</td><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>参见表16格式定义</td></tr><tr><td colspan="5">*1.数据版本校验信息取值规则在工程阶段约定；2.ZC/ATS判断“数据版本校验信息”或“协议版本号”字段校验不通过时，应进行丢包或断开通信处理。*序列号有效值为1~(231-1)。发送方应保证生成两包信息包时，两包信息报中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔。*当未收到对方消息时，填写默认值。</td></tr></table>

<div style="text-align: center;">表 16 应用层信息格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="2">报文长度</td><td style='text-align: center;'>1</td><td rowspan="2">报文长度
(报文类型~报文结束)</td><td rowspan="2">自定义</td></tr><tr><td style='text-align: center;'>2</td></tr><tr><td rowspan="2">报文类型</td><td style='text-align: center;'>3</td><td rowspan="2">定义某一条应用
信息的标识</td><td rowspan="2">自定义</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td rowspan="2">预留</td><td style='text-align: center;'>5</td><td rowspan="2">预留</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>7~报文结束</td><td style='text-align: center;'>按照报文格式定义的
报文具体内容</td><td style='text-align: center;'>自定义</td></tr></table>

##### 6.1.3.3 通信状态管理

通信状态管理应包括如下内容：

a) ATS 应对接收到的 VOBC 的应用消息进行合法性检查，若检查未通过，认为本周期未收到对方的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

---

1）消息内容的一致性检查：包括信息的字段合法性检查，字段组合合法性检查，以及信息完整性检查；

2）通用消息包消息所应包含的信息的完整性；

3）其他逻辑检查。

b) ATS 和 VOBC 应能分别对通信连接状态进行判断（指应用层根据 GAL 包头中字段进行判断，而非安全通信协议层进行的判断）：

1）ATS 认为与 VOBC 通信中断的超时时间定义为 TAtTimeout，可配置，推荐值：6 s；

2）VOBC 认为与 ATS 通信中断的超时时间定义为 TVobcTimeout，可配置，推荐值：6 s；

3）若 ATS 在 TAtTimeout 超时时间内，没有接收到来自 VOBC 的任何消息，则 ATS 应认为与 VOBC 的通信中断；

4）若 ATS 判断收到 VOBC 的 GAL 包延迟已经达到 TAtTimeout，则 ATS 应丢弃此 GAL 包或认为与 VOBC 通信中断；

5）若 VOBC 在 TVobcTimeout 超时时间内，没有接收到来自 ATS 的任何消息，则 VOBC 应认为与 ATS 的通信中断；

6）若 VOBC 判断收到 ATS 的 GAL 包延迟已经达到 TVobcTimeout，则 VOBC 应丢弃此 GAL 包或认为与 ATS 通信中断；

7）通信中断的情况下，应生成报警信息；

8）互联互通线网中，各厂商的 VOBC 与各条线路上的 ATS 的通信超时时间应一致，消息有效期时间应一致。

c) 列车在两 ATS 间移交时，VOBC 判断列车最小安全后端越过 ATS 边界点后，应与移交 ATS 断开通信。

d) 当使用安全通信协议 RSSP-Ⅱ时，VOBC 判断与 ATS 断开通信，且不再与该 ATS 重新建立通信后，应断开与该 ATS 的 TCP/IP 连接；当使用安全通信协议 RSSP-I 时，VOBC 判断与 ATS 断开通信，且不再与该 ATS 重新建立通信后，应断开与该 ATS 的 UDP 连接。

---

#### 6.1.4 通信故障处理

EN50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。车地无线通信双方（ATS-VOBC）应用层的通信故障处理分为如下几种情况：

a) ATS 和 VOBC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息；

b）通信中断的情况下处理：若 ATS/V0BC 认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理。

### 6.2 通信体系结构

#### 6.2.1 通信模型

ATS 与 VOBC 通信协议模型如图 9 所示

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a41d1c98-86a4-41f6-8716-f0ccf3bcaace/markdown_0/imgs/img_in_image_box_178_446_681_937.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A40%3A31Z%2F-1%2F%2F480272d6989cad3d48d13611717330c22e922130904ebb51f50d150b09536379" alt="Image" width="59%" /></div>


<div style="text-align: center;">图 9 ATS 与 VOBC 通信协议模型</div>


#### 6.2.2 通信机制

通信机制包括如下内容：

a）仅能由 VOBC 发起安全连接的建立过程；

---

b) ATS 与 VOBC 采用周期发送和消息触发的方式进行通信；

c）通信双方均采用大端字节序进行数据传输；

d）ATS 与 VOBC 均应对接收的应用信息进行判断和逻辑运算。

### 6.3 接口数据描述

#### 6.3.1 数据类型定义

本节对 ATS 与 VOBC 之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，见表 17。

<div style="text-align: center;">表 17 ATS 与 VOBC 通信的应用层信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>总长度(字节)</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0201</td><td style='text-align: center;'>ATS心跳信息帧</td><td style='text-align: center;'>ATS→V0BC</td><td style='text-align: center;'>4 + 8</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0203</td><td style='text-align: center;'>ATO命令信息帧</td><td style='text-align: center;'>ATS→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0205</td><td style='text-align: center;'>ATS城市自定义帧</td><td style='text-align: center;'>ATS→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x0207</td><td style='text-align: center;'>ATS厂商自定义帧</td><td style='text-align: center;'>ATS→V0BC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x0202</td><td style='text-align: center;'>ATO状态信息帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0204</td><td style='text-align: center;'>列车信息帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0206</td><td style='text-align: center;'>车载设备报警信息帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0208</td><td style='text-align: center;'>车载设备日检状态信息帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x020A</td><td style='text-align: center;'>V0BC城市自定义帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x020C</td><td style='text-align: center;'>V0BC厂商自定义帧</td><td style='text-align: center;'>V0BC→ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>非周期</td></tr></table>

#### 6.3.2 应用信息定义

##### 6.3.2.1 概述

本节中的“非法”值：正常通信时发送方不可能发送的非法取值。接收方收到GAL包中的应用信息帧中存在“非法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认为本周期未收到数据。

本节中的“默认”值：

---

(a) 针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；

(b) 设备在初始化完成前，无法确定状态时，相关字段取值发送“默认值”。接收方收到“默认”值后，应认为信息有效，不进行处理。

本节中涉及“上行”、“下行”的方向定义，均采用运营方向规定的上下行。跨线时，两条线路上下行运营方向定义不一致时，发送上下行方向信息的规则确定为：发送方按照自身所属线路（ATS 指所属线路，VOBC 指最大安全前端所在线路）上下行定义进行发送，由接收方适配处理。

本节中的“预留”字段，发送方统一填0，接收方可不对预留字段进行校验。

本节中的轨道区段内的偏移量，基准点均为车载电子地图中，该轨道区段沿车载电子地图上行方向的起点。

##### 6.3.2.2 ATS 向 VOBC 发送数据

###### 6.3.2.2.1 ATS 心跳信息帧

信息周期发送，用来维持 ATS 设备和 VOBC 间通信链路的连续性。ATS 心跳信息帧见表 18。

<div style="text-align: center;">表 18 ATS 心跳信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>年</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围11~99（表示2011~2099年），超出范围无效</td></tr><tr><td style='text-align: center;'>月</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围1~12，超出范围无效</td></tr><tr><td style='text-align: center;'>日</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围1~31，超出范围无效</td></tr><tr><td style='text-align: center;'>小时</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围0~23，超出范围无效</td></tr><tr><td style='text-align: center;'>分钟</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围0~59，超出范围无效</td></tr><tr><td style='text-align: center;'>秒钟</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有效范围0~59，超出范围无效</td></tr><tr><td colspan="3">注：时钟信息定义为当地时间。</td></tr></table>

###### 6.3.2.2.2 ATO 命令信息帧

当 ATS 设备所管辖范围内有被控列车，ATS 应周期向该 VOBC 发送

---

ATO 命令信息, ATO 命令信息帧内容见表 19.

<div style="text-align: center;">表 19 ATO 命令信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>服务号/表号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>00~65 534 有效默认值:0xFFFF列车为非计划车时,发送默认值</td></tr><tr><td style='text-align: center;'>线路编号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>线路编号,全网统一标识</td></tr><tr><td style='text-align: center;'>下一ZC ID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC 最大安全前端所在 ZC 管辖区域的下一个 ZCID。“最大安全前端”的定义在具体工程项目中明确默认值为 0x00000000</td></tr><tr><td style='text-align: center;'>下一CI ID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC 最大安全前端所在 CI 管辖区域的下一个 CIID默认值为 0x00000000</td></tr><tr><td style='text-align: center;'>下一ATSID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC 最大安全前端所在 ATS 管辖区域的下一个 ATSID默认值为 0x00000000</td></tr><tr><td style='text-align: center;'>车组所属线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>车组所属线路编号,全网统一标识</td></tr><tr><td style='text-align: center;'>车组号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>001~999 有效,超出范围无效“车组所属线路号”+“车组号”在全线网内为唯一标识</td></tr><tr><td style='text-align: center;'>源线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>列车始发站线路编号,全网统一标识默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>车次号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0001~9999 有效,超出范围无效,0000 为默认值</td></tr><tr><td style='text-align: center;'>目的地线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>目的地线路编号,同线路编号默认值:0xFFFF列车无目的地号时,发送默认值</td></tr></table>

---

<div style="text-align: center;">表 19 ATO 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>目的地号</td><td style='text-align: center;'>4</td><td style='text-align: center;'>列车运行计划中列车运行的终点。用ASCII码表示，最多4个ASCII码，低于4个，高位使用空格补齐默认值：0xFFFFFFF列车为非计划车时，发送默认值具体定义方式在工程中明确</td></tr><tr><td style='text-align: center;'>计划运行方向</td><td style='text-align: center;'>1</td><td style='text-align: center;'>列车运行计划中，列车的运行方向上行：0x55；下行：0xAA；默认：0xFF；其他：非法</td></tr><tr><td style='text-align: center;'>跳停站台IDb</td><td style='text-align: center;'>4</td><td style='text-align: center;'>下一站跳停时，取值为站台ID，跳停站台只针对正常上下客站各设置。下一站不跳停时取值为0x00000000</td></tr><tr><td style='text-align: center;'>到站站台IDb</td><td style='text-align: center;'>4</td><td style='text-align: center;'>到达站站台ID；默认值：0x00000000</td></tr><tr><td style='text-align: center;'>下-停车站台IDb</td><td style='text-align: center;'>4</td><td style='text-align: center;'>前方最近的停车站台ID，定义同“跳停站台ID”，默认值为0x00000000</td></tr><tr><td style='text-align: center;'>站停时间</td><td style='text-align: center;'>2</td><td style='text-align: center;'>立即停车：0x50001站停时间：不小于0x0002，单位：s，有效范围：2~65534默认值：0xFFFF其他非法</td></tr><tr><td style='text-align: center;'>下一站跳停命令</td><td style='text-align: center;'>1</td><td style='text-align: center;'>下一站跳停：0x55下一站无跳停命令/取消下一站跳停：0xAA默认值：0xFF其他非法</td></tr><tr><td style='text-align: center;'>区间运行调整命令</td><td style='text-align: center;'>2</td><td style='text-align: center;'>运行等级或区间运行时间（发车到下一站停车），根据业主需求确定，在互联互通线网中应统一，如果区间运行调整命令为默认值，则按V0BC约定的默认运行曲线运行</td></tr></table>

---

<div style="text-align: center;">表 19 ATO 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>扣车命令 $ ^{e} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>扣车有效:0x55扣车取消,无扣车:0xAA默认值:0xFF其他非法</td></tr><tr><td style='text-align: center;'>扣车站台ID $ ^{f} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>扣车站台ID默认值:0x00000000若本站扣车,则发送本站ID;若本站不扣车或取消本站扣车,则发送默认值</td></tr><tr><td style='text-align: center;'>折返命令 $ ^{d} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>是否进行折返站前折返:0x55有人站后折返:0xCC无人自动折返:0xAA不折返:0x33默认值:0xFF</td></tr><tr><td style='text-align: center;'>回段指示 $ ^{e} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>是否进行回段。回段:0x55;不回段:0xAA;默认值:0xFF</td></tr><tr><td style='text-align: center;'>门控策略</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开关门策略开左门,之后关左门:0x55开右门,之后关右门:0xCC同时开双侧门,之后同时关双侧门:0xAA先开左门再开右门之后同时关双侧门:0x11(开门间隔在具体工程项目中确认 $ ^{f} $ )先开右门再开左门之后同时关双侧门:0x22关双侧门:0x88;先开左门再关左门再开右门再关右门:0x33;先开右门再关右门再开左门再关左门:0x44;默认值:0xFF站台为双侧门时,发送门控策略,单侧门时发送默认值;左右门定义为按照沿列车进站方向的左、右侧</td></tr></table>

---

<div style="text-align: center;">表 19 ATO 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>预留</td><td style='text-align: center;'>4</td><td style='text-align: center;'></td></tr><tr><td colspan="3">“下一ZC/CI/ATSID信息，对于计划列车，ATS按照列车运行计划查找列车最大安全前端所在ZC/CI/ATS的下一个ZC/CI/ATS，并向VOBC发送；对于非计划列车，ATS发送默认值。
“ATS向VOBC更新“到站站台ID”、“跳停站台ID”和“下一停车站台ID”、“下一站跳停命令”、“站停时间”、“区间运行调整命令”信息的规则为：
1.“到站站台ID”、“跳停站台ID”、“下一停车站台ID”、“下一站跳停命令”、“区间运行调整命令”字段，ATS收到VOBC在站台发送的“列车信息帧”中的“列车停准停稳状态”字段取值为“停稳且停准”（以下简称“停准停稳状态”）时，更新为下一站/下一区间信息，若ATS未收到VOBC在该站发出的“停准停稳状态”，则在ATS判断列车出站（ATS应保证：ATS判断列车出站的时刻应不早于VOBC判断列车最大安全前端离开站台轨道区段的时刻）时，更新为下一站/下一区间信息。
2.“站停时间”字段，ATS收到VOBC在站台发送的“列车信息帧”中的“列车停准停稳状态”字段取值为“停稳且停准”时，取值ATS期望列车在该站停车的总时间，如停站时间为30s，在列车停站期间ATS周期性发送30s；ATS收到VOBC发送的“列车信息帧”中的“列车停准停稳状态”字段取值不为“停稳且停准”时，取值为默认值。若列车非停准停稳期间，VOBC收到了“站停时间”字段取值为非默认值的ATO命令信息帧，则VOBC不响应该站停时间。
3.ATO判断满足跳停条件时，应响应区间ATO跳停命令或取消跳停命令。
4.到站站台是列车运行路径上的下一个站台，如果有跳停站台，则和跳停站台一致，否则和下一停站站台一致。
5.若列车跨线运行，未越过ATS边界，前方站台属于接管线路管辖范围时，ATO控制命令帧发送更新时机见附录A示例。
“1.ATS应提供设置/取消扣车命令的操作。
（1）对单个站台的设置/取消扣车；
（2）对全线站台的取消扣车；
（3）一次性对同方向多个站台的设置/取消扣车。
2.中心和车站均具备设置/取消扣车功能。ATS应区分显示中心、车站的设置的扣车命令。中心取消扣车操作只能取消由中心设置的扣车；车站取消扣车操作只能取消由车站设置的扣车；中心与车站通信故障时，车站可强制取消中心设置的扣车。</td></tr></table>

---

## 表 19 ATO 命令信息帧(续)

3. 当站台处于跳停状态时，对该站台设置扣车命令，则扣车命令有效，跳停命令自动停止。

4. 调度人员可随时设置/取消扣车。

5. 设置/取消扣车命令后，ATS 立即向 CI 发送扣车命令信息。CI 办理站台发车进路时，若站台设置扣车，则进路可锁闭，但不可开放，取消扣车后，信号自动开放。



6. 列车最大安全前端所在站台有扣车命令时，ATS 向 VOBC 发送“扣车有效”；若列车最大安全前端在站台，该站台无扣车命令，或列车最大安全前端不在站台，则 ATS 向 VOBC 发送“扣车取消，无扣车”

7. VOBC 收到 ATS 发送的“扣车有效”信息时，应在 HMI 上显示扣车有效图标。

8. VOBC 在站台停车，且收到本站台的扣车命令时，应不输出 ATO 发车指示。“折返命令”字段用于 VOBC 进行折返提示相关功能，应可按照具体项目需要配置此功能。若项目要求：根据线路情况，在可进行折返的位置，VOBC 均进行折返提示，则该项目中，此字段取值为默认值。若项目要求：VOBC 应按照列车计划，在计划要进行折返的位置方可提示折返，则此字段取值规则如下：



对于计划列车，列车最大安全前端在站台内时，ATS按照列车运行计划判断列车是否要进行折返：（1）若列车要进行站前折返，则ATS发送站前折返命令，V0BC收到后，列车在站台停稳后，显示换端提示；（2）若列车要进行有人站后折返，则ATS发送有人站后折返命令，当列车最大安全前端进入折返轨后，ATS发送换端命令，V0BC收到后，在运行至此站台后的站后折返轨停车后，显示换端提示；（3）若列车要进行无人自动折返，则ATS发送无人自动折返命令，V0BC收到后，列车在站台停稳后，显示无人自动折返提示，当列车最大安全前端进入站后折返轨后，ATS发送换端命令，V0BC收到后，在站后折返轨停车后，显示换端提示；（4）若列车不进行折返，则ATS发送不折返命令，V0BC收到后，不显示折返提示。

2. 对于非计划列车，列车最大安全前端在站台内时，ATS 发送默认值

3. 列车最大安全前端不在站台内，且不在折返轨内时，ATS 发送默认值

4. 对于与 ATS 无通信的列车，VOBC 根据车载电子地图存储区段属性显示折返提示。

VOBC 进入无人自动折返流程后，不应因与 ATS 的通信中断或 ATS 的信息内容而退出无人自动折返流程。

1. 当列车最大安全前端不在转换轨内或列车不为回段方向时，ATS 向 VOBC 发送的“回段指示”字段为默认值。

---

<div style="text-align: center;">表 19 ATO 命令信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">2. 当列车最大安全前端在转换轨内且列车为回段方向时，对于计划列车，ATS根据列车运行计划，向VOBC发送“回段”或“不回段”指示，对于非计划列车，ATS向VOBC发送默认值。</td></tr><tr><td colspan="2">3. VOBC与ATS通信正常且收到的回段提示字段非默认值时，根据ATS回段提示信息，判断在转换轨内是否显示回段提示；VOBC与ATS通信断开或收到的回段提示字段为默认值时，根据电子地图配置的区段属性，在转换轨内显示回段提示。</td></tr><tr><td colspan="2">本信息帧中涉及“站台ID”的字段，若命令对应位置两侧均为站台，则ATS可发送任意一侧站台ID。</td></tr><tr><td colspan="2">对双侧车门不同时开放的情况，开门间隔规则在线网内应一致。</td></tr></table>

###### 6.3.2.2.3 ATS城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。ATS城市自定义帧内容见表20。

表 20 ATS 城市自定义帧


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

## 轨道

###### 6.3.2.2.4 ATS厂商自定义帧

白定义信息，用于实现各厂商特有功能。各厂商分别定制。ATS 判断通信的 VOBC 与自身属于同一厂商时，方可发送厂商自定义帧。ATS 厂商自定义帧内容见表 21。

<div style="text-align: center;">表 21 ATS 厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

##### 6.3.2.3 VOBC 向 ATS 发送数据

###### 6.3.2.3.1 ATO 状态信息帧

若已建立 ATO 模式, VOBC 应周期向 ATS 发送 ATO 状态信息, ATO

---

状态信息帧详见表22。

ATS 应针对每列车的 ATO 状态信息进行超时判断，配置时间内未收到相应列车的 ATO 状态信息，则清除该车的 ATO 状态信息。

未收到 ATS 发送的信息前，对应字段填写默认值。

<div style="text-align: center;">表 22 ATO 状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>服务号/表号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>00~65 534 有效
默认值:0xFFFF
其他:非法
列车为非计划车时,发送默认值</td></tr><tr><td style='text-align: center;'>线路编号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>线路编号,全网统一标识,默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>车组号所属线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>车组号所属线路号,默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>车组号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>二进制码,001~999 有效,000 表示对所有列车的广播,其他非法
默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>源线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>列车始发站线路编号,默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>车次号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0000~9999 有效,超出范围无效,0000 表示车次号未设定
默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>目的地线路号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>目的地线路编号,默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>目的地号</td><td style='text-align: center;'>4</td><td style='text-align: center;'>用 ASCII 码表示,具体定义内容在工程项目中明确默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>司机号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>二进制码
1~65 534 有效,超出范围无效
默认值:0xFFFF</td></tr><tr><td style='text-align: center;'>ATO 工作模式</td><td style='text-align: center;'>1</td><td style='text-align: center;'>AM 自动驾驶:0x03
ATO 未建立:0x00
其他非法
默认值:0xFF</td></tr></table>

---

<div style="text-align: center;">表 22 ATO 状态信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>区间运行调整命令</td><td style='text-align: center;'>2</td><td style='text-align: center;'>V0BC收到的ATS发送的运行等级或区间运行时间（列车从前一站发车到下一站停车时间，单位：s），根据业主需求确定，默认值：0xFFFF</td></tr><tr><td style='text-align: center;'>跳停状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>V0BC收到的ATS发送的跳停命令跳停：0x55无跳停命令/取消跳停：0xAA默认值：0xFF其他非法</td></tr><tr><td style='text-align: center;'>扣车状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>V0BC收到的ATS发送的扣车命令扣车有效：0x55扣车取消，无扣车：0xAA默认值：0xFF其他非法</td></tr><tr><td style='text-align: center;'>下一停车站台ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC收到的ATS发送的下一停车站台ID，默认值：0x00000000</td></tr><tr><td style='text-align: center;'>跳停站台ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC收到的ATS发送的跳停站台ID默认值：0x00000000</td></tr><tr><td style='text-align: center;'>扣车站台ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>V0BC收到的ATS发送的扣车站台ID默认值：0x00000000</td></tr><tr><td style='text-align: center;'>站停时间</td><td style='text-align: center;'>2</td><td style='text-align: center;'>V0BC收到的ATS发送的站停时间默认值：0xFFFF</td></tr><tr><td style='text-align: center;'>门控策略</td><td style='text-align: center;'>1</td><td style='text-align: center;'>V0BC收到的ATS发送的门控策略默认值：0xFF</td></tr><tr><td style='text-align: center;'>预留</td><td style='text-align: center;'>4</td><td style='text-align: center;'>根据业主要求定义</td></tr><tr><td colspan="3">注：“车组号”、“车组号所属线路号”由V0BC通过“ATO状态信息帧”向ATS发送；ATS收到后，向车载发送的“ATO命令信息帧”中填写收到的“车组号”、“车组号所属线路号”，收到之前填写默认值；“ATO命令信息帧”中的其他信息由ATS通过“ATO命令信息帧”向V0BC发送；V0BC收到后，向ATS发送的“ATO状态信息帧”中填写已执行的对应信息值，收到之前填写默认值。当前ATO命令执行完成后，在新的命令到达之前，V0BC应持续向ATS反馈当前ATO命令的执行状态。</td></tr></table>

---

###### 6.3.2.3.2 列车信息帧

本消息为周期信息，当 VOBC 与 ATS 之间的安全连接建立后，周期发送，列车信息帧内容见表 23。

<div style="text-align: center;">表 23 列车信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>线路编号</td><td style='text-align: center;'>2</td><td style='text-align: center;'>线路编号，全网统一标识</td></tr><tr><td style='text-align: center;'>列车定位状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>有定位：0x55无定位：0xAA其他非法</td></tr><tr><td style='text-align: center;'>运行方向 $ ^{a} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>最小安全后端指向最大安全前端的方向，以最小安全后端处的上下行方向确定。上行：0x55下行：0xAA默认：0xFF其他：非法</td></tr><tr><td style='text-align: center;'>激活端</td><td style='text-align: center;'></td><td style='text-align: center;'>本V0BC是否为激活端（首尾冗余的V0BC统一发送是激活端）激活端：0x55非激活端：0xAA其他：非法</td></tr><tr><td style='text-align: center;'>车轮转向</td><td style='text-align: center;'>1</td><td style='text-align: center;'>车轮正转（前进）：0x55车轮反转（后退）：0xAA其他值无效车轮不转动时按正转发送</td></tr><tr><td style='text-align: center;'>列车最大安全前端位置所在轨道区段ID $ ^{a} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>列车最大安全前端位置所在轨道区段ID默认值：0x00000000</td></tr><tr><td style='text-align: center;'>列车最大安全前端位置在轨道区段内偏移量 $ ^{a} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>单位：cm，有效范围：0x0~0xFFFFFFF默认值：0xFFFFFFF</td></tr></table>

---

<div style="text-align: center;">表 23 列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>列车最小安全前端位置所在轨道区段ID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>列车最小安全前端位置所在轨道区段ID默认值:0x00000000</td></tr><tr><td style='text-align: center;'>列车最小安全前端位置在轨道区段内偏移量*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>单位:cm,有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>列车最大安全后端位置所在轨道区段ID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>列车最大安全后端位置所在轨道区段ID默认值:0x00000000</td></tr><tr><td style='text-align: center;'>列车最大安全后端位置在轨道区段内偏移量*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>单位:cm,有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>列车最小安全后端位置所在轨道区段ID*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>列车最小安全后端位置所在轨道区段ID默认值:0x00000000</td></tr><tr><td style='text-align: center;'>列车最小安全后端位置在轨道区段内偏移量*</td><td style='text-align: center;'>4</td><td style='text-align: center;'>单位:cm,有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFF</td></tr><tr><td style='text-align: center;'>列车驾驶模式*</td><td style='text-align: center;'>1</td><td style='text-align: center;'>AM模式:0x01CM模式:0x02RM模式:0x03EUM模式:0x04默认值:0xFF其他非法</td></tr><tr><td style='text-align: center;'>列车运行控制级别*</td><td style='text-align: center;'>1</td><td style='text-align: center;'>CBTC:0x01点式:0x02联锁:0x03默认值:0xFF其他非法</td></tr><tr><td style='text-align: center;'>列车完整性</td><td style='text-align: center;'>1</td><td style='text-align: center;'>完整:0x55不完整:0xAA其他非法</td></tr></table>

---

<div style="text-align: center;">表 23 列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>列车紧急制动状态 $ ^{4} $</td><td style='text-align: center;'>1</td><td style='text-align: center;'>无紧急制动:0x55紧急制动:0xAA其他非法</td></tr><tr><td style='text-align: center;'>列车AR状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>列车换端过程中,原尾端ATP与ZC建立通信后到升级之前的状态处于AR状态:0x55未处于AR状态:0xAA其他非法</td></tr><tr><td style='text-align: center;'>列车速度信息</td><td style='text-align: center;'>2</td><td style='text-align: center;'>单位:cm/s,有效范围:0~15 000</td></tr><tr><td style='text-align: center;'>车门状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开门:0x55关门:0xAA门旁路:0xFF其他非法若无门旁路功能则按照关门处理</td></tr><tr><td style='text-align: center;'>列车停稳状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>停稳且停准:0x55未停稳:0xAA停稳但未停准:0xCC其他:非法</td></tr><tr><td style='text-align: center;'>停车保证状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>停车保证响应可以停车:0x55无法停车:0xAA默认值:0xFF其他非法</td></tr><tr><td style='text-align: center;'>无人折返状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>无人折返折入中(从车载ATP接收到无人折返命令开始到换端前):0x55无人折返折出中:0xAA未在无人折返中:0x00默认值:0xFF其他非法若车载ATP无相关功能,则发送默认值;若ATS无相关功能,则可不处理此信息</td></tr></table>

---

<div style="text-align: center;">表 23 列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>预选模式</td><td style='text-align: center;'>1</td><td style='text-align: center;'>车载 ATP 允许到达的最高模式CBTC - AM: 0x01CBTC - CM: 0x02ITC - AM: 0x03ITC - CM: 0x04IL - RM: 0x05其他值非法</td></tr><tr><td style='text-align: center;'>紧急制动原因</td><td style='text-align: center;'>1</td><td style='text-align: center;'>根据业主要求定义</td></tr><tr><td style='text-align: center;'>当前紧急制动触发速度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>单位 cm/s, ATP 曲线对应的 EBI 速度,有效范围: 0x0~0xFFFE默认值: 0xFFFF。当 VOBC 无法发送此信息时, 发送默认值</td></tr><tr><td style='text-align: center;'>当前推荐速度</td><td style='text-align: center;'>2</td><td style='text-align: center;'>单位 cm/s, ATO 曲线对应的常用制动速度, 有效范围: 0x0~0xFFFE默认值: 0xFFFF。当 VOBC 无法发送此信息时, 发送默认值</td></tr><tr><td style='text-align: center;'>安全防护点轨道区段 ID $ ^{r} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC 采用的 ZC 的移动授权中的安全防护点轨道区段 ID默认值: 0x00000000</td></tr><tr><td style='text-align: center;'>安全防护点轨道区段偏移量 $ ^{r} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC 采用的 ZC 的移动授权中的安全防护点轨道区段偏移量。有效范围: 0x0~0xFFFFFFE默认值: 0xFFFFFFF</td></tr><tr><td style='text-align: center;'>障碍点轨道区段 ID $ ^{r} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC 采用的 ZC 的移动授权中的障碍点轨道区段 ID默认值: 0x00000000</td></tr><tr><td style='text-align: center;'>障碍点轨道区段内偏移量 $ ^{r} $</td><td style='text-align: center;'>4</td><td style='text-align: center;'>VOBC 采用的 ZC 的移动授权中的障碍点轨道区段偏移量。有效范围: 0x0~0xFFFFFFE默认值: 0xFFFFFFF</td></tr></table>

---

<div style="text-align: center;">表 23 列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="6">MA路径信息</td><td style='text-align: center;'>道岔信息个数</td><td style='text-align: center;'>2</td><td style='text-align: center;'>V0BC采信的ZC的移动授权内包含的道岔个数。有效范围：0~20</td></tr><tr><td style='text-align: center;'>道岔(1)ID</td><td style='text-align: center;'>4</td><td style='text-align: center;'>道岔ID</td></tr><tr><td style='text-align: center;'>道岔(1)状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>道岔状态定位：0x55反位：0xAA其他：非法</td></tr><tr><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td></tr><tr><td style='text-align: center;'>道岔(X)ID(X为“道岔信息个数”字段值)</td><td style='text-align: center;'>4</td><td style='text-align: center;'>道岔ID</td></tr><tr><td style='text-align: center;'>道岔(X)状态</td><td style='text-align: center;'>1</td><td style='text-align: center;'>道岔状态定位：0x55反位：0xAA其他：非法</td></tr><tr><td colspan="2">列车编组信息</td><td style='text-align: center;'>1</td><td style='text-align: center;'>列车编组数信息，取值范围：1~20</td></tr><tr><td colspan="2">预留</td><td style='text-align: center;'>4</td><td style='text-align: center;'>根据业主要求定义</td></tr><tr><td colspan="4">“若V0BC与ATS建立通信时无法确定准确位置，则“运行方向”、“列车最大安全前端位置所在轨道区段ID”、“列车最大安全前端位置在轨道区段内偏移量”、“列车最小安全前端位置所在轨道区段ID”、“列车最小安全前端位置在轨道区段内偏移量”、“列车最大安全后端位置所在轨道区段ID”、“列车最大安全后端位置在轨道区段内偏移量”、“列车最小安全后端位置所在轨道区段ID”、“列车最小安全后端位置在轨道区段内偏移量”均填写默认值。b“列车运行控制级别”与“列车驾驶模式”字段取值应满足下表对应关系，控制级别与驾驶模式对照见表24。若ATP采用ZC发送的MA，则安全防护点轨道区段ID、安全防护点轨道区段偏移量、障碍点轨道区段ID、障碍点轨道区段内偏移量取值均为采用的MA内容；</td></tr></table>

---

<div style="text-align: center;">表 23 列车信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>若 ATP 不采用 ZC 发送的 MA，则安全防护点轨道区段 ID、安全防护点轨道区段偏移量、障碍点轨道区段 ID、障碍点轨道区段内偏移量均发送默认值。停车保证的具体含义参见本规范 5.4.2 节 V0BC-ZC 列车信息帧中“停车保证响应”字段。</td></tr></table>

<div style="text-align: center;">表 24 控制级别与驾驶模式对照表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'></td><td style='text-align: center;'>EUM</td><td style='text-align: center;'>RM</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>AM</td></tr><tr><td style='text-align: center;'>连续式列车控制级别</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>○</td><td style='text-align: center;'>○</td></tr><tr><td style='text-align: center;'>点式列车控制级别</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>○</td><td style='text-align: center;'>○</td></tr><tr><td style='text-align: center;'>联锁控制级别</td><td colspan="4">注:✗/○表示该控制级别下不具有/具有该驾驶模式</td></tr></table>

###### 6.3.2.3.3 车载设备报警信息帧

车载设备报警信息帧详见表25。

表 25 车载设备报警信息锁


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td colspan="2">报警信息数量</td><td style='text-align: center;'>1</td><td style='text-align: center;'>报警信息总数(n)，有效范围：8~20*</td></tr><tr><td rowspan="2">列车报警信息</td><td style='text-align: center;'>信息1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ATO故障有故障：0x55无故障：0xAA默认值：0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>BTM故障有故障：0x55无故障：0xAA默认值：0xFF其他值无效</td></tr></table>

---

<div style="text-align: center;">表 25 车载设备报警信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="6">列车报警信息</td><td style='text-align: center;'>信息3</td><td style='text-align: center;'>1</td><td style='text-align: center;'>车载人机界面故障有故障:0x55无故障:0xAA默认值:0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息4</td><td style='text-align: center;'>1</td><td style='text-align: center;'>雷达故障(可选)有故障:0x55无故障:0xAA默认值:0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息5</td><td style='text-align: center;'>1</td><td style='text-align: center;'>与列车信息管理系统通信故障有故障:0x55无故障:0xAA默认值:0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息6</td><td style='text-align: center;'>1</td><td style='text-align: center;'>测速传感器故障有故障:0x55无故障:0xAA默认值:0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息7</td><td style='text-align: center;'>1</td><td style='text-align: center;'>加速度计故障(可选)有故障:0x55无故障:0xAA默认值:0xFF其他值无效</td></tr><tr><td style='text-align: center;'>信息8</td><td style='text-align: center;'>1</td><td style='text-align: center;'>ATP故障(与ATS通信正常时)有故障:0x55无故障:0xAA默认值:0xFF其他:非法</td></tr><tr><td colspan="4">58</td></tr></table>

---

<div style="text-align: center;">表 25 车载设备报警信息帧(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说 明</td></tr><tr><td rowspan="2">列车报警 信息</td><td style='text-align: center;'>…</td><td style='text-align: center;'>…</td><td style='text-align: center;'>…</td></tr><tr><td style='text-align: center;'>信息n</td><td style='text-align: center;'>1</td><td style='text-align: center;'>…</td></tr><tr><td colspan="2">板卡信息</td><td style='text-align: center;'>6</td><td style='text-align: center;'>自定义,在工程项目中具体明确</td></tr><tr><td colspan="4">“报警信息1~8为固定信息,其他报警信息可在具体工程中约定。</td></tr></table>

###### 6.3.2.3.4 车载设备日检状态信息帧

车载设备日检状态信息帧见表26。

<div style="text-align: center;">表 26 车载设备日检状态信息帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>日检状态</td><td style='text-align: center;'>6</td><td style='text-align: center;'>自定义</td></tr></table>

###### 6.3.2.3.5 VOBC 城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。VOBC城市自定义帧信息见表27。

<div style="text-align: center;">表 27 VOBC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

###### 6.3.2.3.6 VOBC 厂商自定义帧

自定义信息，用于实现各厂商特有功能。各厂商分别定制。V0BC 判断通信的 ATS 与自身属于同一厂商时，方可发送厂商自定义帧。V0BC 城市自定义帧信息见表 28。

---

<div style="text-align: center;">表 28 VOBC 城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

#### 6.3.3 列车折返过程通信说明

##### 6.3.3.1 概述

折返流程分为首尾端 VOBC 共用安全连接与首尾端 VOBC 不共用安全连接两种情况。本节中 VOBC1 指换端前的车头 VOBC、VOBC2 指换端前的车尾 VOBC。

##### 6.3.3.2 首尾 VOBC 共用安全连接

此种情况下，V0BC在红蓝网上分别与ATS建立安全连接，冗余消息在红蓝网上分别传输（红网IP对红网IP，蓝网IP对蓝网IP）。首尾V0BC共同使用这组安全连接，首尾V0BC共用一个VID。ATS不区分首尾端V0BC。

折返过程如下：

a）VOBC 与 ATS 正常通信，向 ATS 发送 VOBCI 方向的“列车信息帧”和“ATO 状态信息帧”，ATS 向 VOBC 发送 VOBCI 方向的“ATO 命令信息帧”；

b）折返开始后，VOBC应停止发送VOBC1方向的“列车信息帧”和“ATO状态信息帧”，改为发送VOBC2方向的“列车信息帧”和“ATO命令信息帧”；

c) ATS 根据收到的 VOBC“列车信息帧”和“ATO 状态信息帧”判断列车方向发生改变且列车安全包络完全位于折返轨内，则认为列车换端，开始向 VOBC 发送 VOBC2 方向的“ATO 命令信息帧”；

d）VOBC 收到 VOBC2 方向的“ATO 命令信息帧”，开始据此控制列车，折返流程结束。

##### 6.3.3.3 首尾 VOBC 不共用安全连接

此种情况时车载首尾 VOBC 使用不同的 ID，首尾 VOBC 分别与 ATS

---

建立安全连接。在折返过程中，车尾 VOBC2 与 ATS 新建立安全连接。此时 VOBC1、VOBC2 同时与 ATS 通信，分别维护安全连接。换端完成后，VOBC1 断开与 ATS 的连接，仅保留 VOBC2 的连接。

折返流程如下：

a） VOBC1 与 ATS 正常通信，向 ATS 发送本端“列车信息帧”和“ATO 状态信息帧”，ATS 向 VOBC1 发送“ATO 命令信息帧”；

b）折返开始后，VOBC2与ATS新建立安全连接，通信建立后，VOBC2向ATS发送本端“列车信息帧”和“ATO状态信息帧”，其中“列车AR状态”内容应为“处于AR状态”；

e) ATS 与 VOBC1、VOBC2 同时保持通信，向两 VOBC 发送相同的应用信息，帧头区分 VOBC1 和 VOBC2；

d) 换端完成后，VOBCI 停止向 ATS 发送信息，断开与 ATS 的连接；

e） VOBC1 与 ATS 断开连接后，VOBC2 向 ATS 发送的本端列车位置信息中“列车 AR 状态”内容改为“未处于 AR 状态”。

#### 6.3.4 列车跨线过程通信说明

列车跨线过程中与ATS的通信过程参见T/CAMET04011.6

#### 6.3.5 时钟同步说明

ATS 应具备 NTP 服务功能。YOBC 可使用 NTP 服务与 ATS 进行时钟同步，也可采用 6.3.2.1.1 ATS 心跳信息帧中的时间信息与 ATS 进行时钟同步

#### 6.3.6 ATO 控制命令帧发送更新时机说明

ATS 应具备 NTP 服务功能。VOBC 可使用 NTP 服务与 ATS 进行时钟同步，也可采用 6.3.2.1.1 ATS 心跳信息帧中的时间信息与 ATS 进行时钟同步。见附录 A。

## 7 VOBC - CI 报文规范

### 7.1 接口连接方式

#### 7.1.1 物理接口

V0BC 与 CI 之间采用冗余网络进行通信。CI 与 V0BC 之间的网络

---

拓扑结构采用 A 网 - A 网、B 网 - B 网两个链路进行连接。

#### 7.1.2 安全通信协议

CI 与 VOBC 之间通信可采用 RSSP-Ⅱ或 RSSP-Ⅰ安全通信协议。RSSP-Ⅱ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅱ铁路信号安全通信协议》；RSSP-Ⅰ安全通信协议的具体要求参见运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅰ铁路信号安全通信协议》。采用 RSSP-Ⅰ安全通信协议的前提条件为使用 LTE-M 通信且 LTE-M 具备空口加密措施可防止伪装、CBTC 信号系统符合三级等保要求。在此前提条件下，宜采用 RSSP-Ⅰ安全通信协议。

如图 10 所示, 其 SAL/MASL/ALE 三层, 遵循 RSSP-Ⅱ标准规定。

TCP 及 IP 层使用标准 TCP/IP 协议栈。

MAC 及 PHY 层取决于不同的网络种类, 无线网使用无线标准协议, 地面网使用以太网协议(IEEE 802.3)。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//76c2c0fd-39e2-4fdc-801f-27fde1161f7a/markdown_0/imgs/img_in_image_box_129_581_775_1087.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A41%3A45Z%2F-1%2F%2F13a1caec971d88425788b6d8cd47638edb4eb9ca148c1966075fcd774ce6849b" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 10 无线安全通信协议 RSSP-Ⅱ构架</div>

---

如图 11 所示, 其 RSSP-I 协议遵循 RSSP-I 标准规定。

UDP 层使用标准 UDP 协议栈。

MAC 及 PHY 层取决于不同的网络种类，无线网使用无线标准协议，地面网使用以太网协议（IEEE 802.3）。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//12b2a3d5-3b43-4ce7-85c4-02b89160d381/markdown_0/imgs/img_in_image_box_92_256_768_703.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A41%3A48Z%2F-1%2F%2F1d715a71b3bb5635e1a1b9f45cb6a3420fe0bcdc0efb0310d0a923195745b21b" alt="Image" width="80%" /></div>


<div style="text-align: center;">图 11 无线安全通信协议 RSSP-I 构架</div>


#### 7.1.3 动态交互描述

##### 7.1.3.1 通信应用层消息包定义

将 CI-VOBC 间每个周期需要交互的应用信息通过组成通用消息包进行传输，如图 12 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//12b2a3d5-3b43-4ce7-85c4-02b89160d381/markdown_0/imgs/img_in_image_box_205_931_658_1068.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A41%3A48Z%2F-1%2F%2F121d619386a8f907b95494b92415f9e165d162a22ed7912fbb6555177465b647" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 12 通用消息包和应用层信息包关系结构图</div>

---

##### 7.1.3.2 信息包格式定义

V0BC/CI 每周期最多允许发送 1 个 GAL 消息包，GAL 包中包含 V0BC 与 CI 之间传输的各条应用信息。每个 GAL 消息包总长不得超过 1000 字节，格式定义见表 29 和表 30。

<div style="text-align: center;">表 29 通用信息包格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">接口信息类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型高位</td><td rowspan="2">2字节</td><td rowspan="2">0x0206; VOBC-CI接口</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td style='text-align: center;'>3</td><td rowspan="4">源ID</td><td rowspan="4">4字节</td><td rowspan="4">通信双方的定义</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>6</td></tr><tr><td rowspan="4">接收方标识信息</td><td style='text-align: center;'>7</td><td rowspan="4">目的ID</td><td rowspan="4">4字节</td><td rowspan="4">通信双方的定义</td></tr><tr><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>9</td></tr><tr><td style='text-align: center;'>10</td></tr><tr><td rowspan="4">电子地图版本校验信息 $ ^{a} $</td><td style='text-align: center;'>11</td><td rowspan="4">CI、VOBC之间的版本一致性信息</td><td rowspan="4">4字节</td><td rowspan="4">CI管辖范围内, CI与VOBC间的数据版本校验信息</td></tr><tr><td style='text-align: center;'>12</td></tr><tr><td style='text-align: center;'>13</td></tr><tr><td style='text-align: center;'>14</td></tr><tr><td rowspan="4">本方消息序列号 $ ^{b} $</td><td style='text-align: center;'>15</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录发送本条消息时, 本方的周期计数</td></tr><tr><td style='text-align: center;'>16</td></tr><tr><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>18</td></tr></table>

---

<div style="text-align: center;">表 29 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">通信周期</td><td style='text-align: center;'>19</td><td rowspan="2">通信周期</td><td rowspan="2">2字节</td><td rowspan="2">设备通信周期,单位:ms</td></tr><tr><td style='text-align: center;'>20</td></tr><tr><td rowspan="4">对方消息序列号</td><td style='text-align: center;'>21</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息中的对方消息序列号</td></tr><tr><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>24</td></tr><tr><td rowspan="4">收到上一条消息时本方序列号</td><td style='text-align: center;'>25</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息时,本方的周期计数</td></tr><tr><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>协议版本号</td><td style='text-align: center;'>29</td><td style='text-align: center;'>协议版本号</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>CI-V0BC的协议版本,本规范定义为20</td></tr><tr><td style='text-align: center;'>应用层报文总长度</td><td style='text-align: center;'>3031</td><td style='text-align: center;'>应用报文总长度</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>后续报文长度的字节数,不含长度本身两字节</td></tr><tr><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>32~1000</td><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>参见表30格式定义</td></tr><tr><td colspan="5">“电子地图版本校验信息针对范围为CI管辖区域范围。
“序列号有效值为1~(211-1)。
“当未收到对方消息时,序列号约定为0xFFFFFFF。
““电子地图版本校验信息”、“协议版本号”需要进行校验,若校验不一致,则接收方进行丢包或断开安全连接处理。</td></tr></table>

---

<div style="text-align: center;">表 30 应用层信息格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="2">报文长度</td><td style='text-align: center;'>1</td><td rowspan="2">报文长度（报文类型~报文结束）</td><td rowspan="2"></td></tr><tr><td style='text-align: center;'>2</td></tr><tr><td rowspan="2">报文类型</td><td style='text-align: center;'>3</td><td rowspan="2">定义某一条应用信息的标识</td><td rowspan="2">详见具体接口文档4.2节</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td rowspan="2">预留</td><td style='text-align: center;'>5</td><td rowspan="2">预留</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>7~报文结束</td><td style='text-align: center;'>按照报文格式定义的报文具体内容</td><td style='text-align: center;'>详见具体接口文档</td></tr></table>

##### 7.1.3.3 通信状态管理

通信状态管理包括如下内容：

a）应对接收到的 VOBC 的应用消息进行合法性检查，若检查未通过，认为本周期未收到对方的应用信息或主动断开安全连接。具体检查方式如下：

1）消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查以及信息完整性检查；

2）消息所应包含的信息的完整性。

b) CI 和 VOBC 应能分别对通信连接状态进行判断：

1）CI 认为与 VOBC 通信中断的超时时间定义为 TCiTimeout （可配置，推荐值为 6 s）；

2）VOBC 认为与 CI 通信中断的超时时间定义为 TVobcTimeout （可配置，推荐值为 6 s）；

3）若 CI 在 TCiTimeout 超时时间内，没有接收到来自 VOBC 的任何消息，则 CI 应认为与 VOBC 的通信中断；

4）若 VOBC 在 TVobcTimeout 超时时间内，没有接收到来自 CI 的任何消息，则 VOBC 应认为与 CI 的通信中断。

---

5）若 CI 判断接收到 VOBC 的应用信息延迟已经达到 TC $ _i $ Timeout 时，CI 应丢弃此信息包或认为与 VOBC 通信中断；

6）若 VOBC 判断接收到 CI 的应用信息延迟已经达到 TVobcTimeout 时，VOBC 应丢弃此信息包或认为与 CI 通信中断。

c) 互联互通线网中，车载设备与各条线路上的联锁设备的通信超时时间应一致，消息有效期时间应一致：

1）当使用安全通信协议 RSSP-Ⅱ，VOBC 在与 CI 设备通信时，当判断与 CI 设备通信断开并且不再与对方建立连接后，应断开与该 CI 设备的 TCP/IP 连接；





2）当使用安全通信协议 RSSP-I，V0BC 在与 CI 设备通信时，当判断与 CI 设备通信断开并且不再与对方建立连接后，应断开与该 CI 设备的 UDP 链接。

d) EN 50159:2010 中提及的 7 种开放式网络存在的安全通信风险均由安全通信协议进行防护，风险包括：重复、删除、插入、重排序、损坏、伪装、延迟。

车地无线通信双方（CI-VOBC）应用层的通信故障处理分为如下几种情况：

1）CI 和 VOBC 对于接收到的重复、逆序的应用信息，采用直接丢弃的方式进行处理，并且认为本周期未收到对等方的应用信息；

2）通信中断的情况下，若CI/V0BC认为与对等方应用层通信超时中断，采取主动释放安全连接的方式进行处理；

3）其他风险由安全通信协议完成防护处理。

### 7.2 通信体系结构

#### 7.2.1 通信模型

CL 与 VOBC 通信协议模型如图 13 所示。

#### 7.2.2 通信机制

通信机制包括如下内容：

a）仅能由 VOBC 发起安全连接的建立过程；

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//58a80b07-49b3-42a1-8bef-5fcbb10aa41c/markdown_0/imgs/img_in_image_box_189_114_722_504.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A42%3A06Z%2F-1%2F%2Fe88202e9cda72b071ea91557d057441267eee4df2785ee30668795d70fed6808" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 13 CI 与 VOBC 通信协议模型</div>


b） CI 与 VOBC 采用周期发送和消息触发的方式进行通信；

c）通信双方均采用大端字节序进行数据传输；

d）CI 与 VOBC 均应对接收的应用信息进行判断和逻辑运算。

### 7.3 接口数据描述

#### 7.3.1 数据类型定义

本节对 VOBC 与 CI 之间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）进行定义，见表 31。

<div style="text-align: center;">表 31 CI 与 VOBC 通信的应用层信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0201</td><td style='text-align: center;'>V0BC→CI 控制信息</td><td style='text-align: center;'>V0BC→CI</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0202</td><td style='text-align: center;'>CI→V0BC 状态信息</td><td style='text-align: center;'>CI→V0BC</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0203</td><td style='text-align: center;'>V0BC→CI 心跳帧</td><td style='text-align: center;'>V0BC→CI</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0204</td><td style='text-align: center;'>CI→V0BC 心跳帧</td><td style='text-align: center;'>CI→V0BC</td><td style='text-align: center;'>周期</td></tr></table>

---

<div style="text-align: center;">表 31 CI 与 VOBC 通信的应用层信息定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0205</td><td style='text-align: center;'>V0BC→CI城市自定义帧</td><td style='text-align: center;'>V0BC→CI</td><td style='text-align: center;'>自定义</td></tr><tr><td style='text-align: center;'>0x0206</td><td style='text-align: center;'>CI→V0BC城市自定义帧</td><td style='text-align: center;'>CI→V0BC</td><td style='text-align: center;'>自定义</td></tr><tr><td style='text-align: center;'>0x0207</td><td style='text-align: center;'>V0BC→CI厂商自定义帧</td><td style='text-align: center;'>V0BC→CI</td><td style='text-align: center;'>自定义</td></tr><tr><td style='text-align: center;'>0x0208</td><td style='text-align: center;'>CI→V0BC厂商自定义帧</td><td style='text-align: center;'>CI→V0BC</td><td style='text-align: center;'>自定义</td></tr><tr><td style='text-align: center;'>0x0209</td><td style='text-align: center;'>V0BC→CI注销请求帧</td><td style='text-align: center;'>V0BC→CI</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020a</td><td style='text-align: center;'>CI→V0BC注销回复帧</td><td style='text-align: center;'>CI→V0BC</td><td style='text-align: center;'>周期</td></tr></table>

#### 7.3.2 应用信息定义

##### 7.3.2.1 概述

VOBC 在列车进出站过程中，给 CI 发送信息控制站台门的打开和关闭。VOBC 至 CI 的信息周期发送（发送周期按照各方发送方周期定义，对通信周期范围定义为  $ 300 \, ms \sim 1000 \, ms $ ），CI 接收到信息后向 VOBC 发送对应 PSD 的状态信息。

对于可允许两侧开门的站台系统将两侧的 PSD 当作两个不同的设备分别控制，为两侧的 PSD 分别分配全局唯一的标识（即整列的 PSD 当作一个设备，系统为其分配全局唯一的 ID）。

文中未做说明的上下行定义，均为线路规定的运营上下行方向。

##### 7.3.2.2 VOBC 向 CI 发送信息

###### 7.3.2.2.1 VOBC 向 CI 发送心跳帧

在列车车头最大安全前端进入 CI 通信区段前发送该信息包（具体时机各厂商自定义），用来维持 VOBC 设备和 CI 间通信链路的连续性。

列车车头最大安全前端进入 CI 通信区段后，开始发送控制信息时不再发送心跳帧。VOBC 向 CI 发送心跳帧信息见表 32。

---

<div style="text-align: center;">表 32 VOBC 向 CI 发送心跳帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>无</td><td style='text-align: center;'>0</td><td style='text-align: center;'>仅有报文帧头，详见应用层信息格式定义</td></tr></table>

###### 7.3.2.2.2 VOBC 向 CI 发送控制信息

从列车车头最大安全前端进入 CI 通信区段开始，直至列车最大安全前端离开 CI 通信区段前，发送该信息包。

VOBC 至 CI 输出信息接口见表 33，应用层报文长度固定，全线站台门的编号方式应有共同的规则和相应的说明文件。

<div style="text-align: center;">表 33 VOBC 向 CI 发送控制信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>DIR_TRAIN</td><td style='text-align: center;'>1</td><td style='text-align: center;'>列车运行方向（激活端车头最大安全前端对应方向）上行：0x55下行：0xAA默认：0xFF</td></tr><tr><td style='text-align: center;'>CMD_UNLOCKOVERLAP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>允许保护区段解锁命令允许解锁：0x55不允许解锁：0xAA其他非法列车在停车点停准停稳时（包含运营停车点，折返停车点，区间参考停车点），VOBC才可发出允许保护区段解锁命令</td></tr><tr><td style='text-align: center;'>NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>轨道区段ID1~0xFFFFFFFF，0为默认值VOBC最大安全前端所在CI通信区段的轨道区段ID</td></tr><tr><td style='text-align: center;'>N_PSD_CMD_CODE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>站台开门码，VOBC根据停准停稳时对应的停车点及列车编组信息向CI发送开门码，每个开门码对应CI需要开的一组站台门，站台开门码定义详见注4：默认值为0</td></tr></table>

---

<div style="text-align: center;">表 33 VOBC 向 CI 发送控制信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td colspan="2">N_PSD</td><td style='text-align: center;'>1</td><td style='text-align: center;'>需要控制的PSD的数量(定长),0、1或者2;为0时,PSD1和PSD2字段填写默认值;为1时,PSD2字段填写默认值</td></tr><tr><td rowspan="2">PSD_1控制信息</td><td style='text-align: center;'>NID_PSD_1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>PSD_1的ID1~0xFFFFFFFF0为默认值,表示当前通信位置不存在站台门</td></tr><tr><td style='text-align: center;'>NC_PSD_1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>对PSD_1的控制命令(对应命令为开门时,开门码参照N_PSD_CMD_CODE)开门:0x55关门:0xAA默认无效值:0xFF</td></tr><tr><td rowspan="2">PSD_2控制信息</td><td style='text-align: center;'>NID_PSD_2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>PSD_2的ID(用于实现不同侧的屏蔽门控制)1~0xFFFFFFFF0为默认值,表示当前通信位置不存在站台门</td></tr><tr><td style='text-align: center;'>NC_PSD_2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>对PSD_2的控制命令(对应编组信息参照N_PSD_TYPE)开门:0x55关门:0xAA默认无效值:0xFF</td></tr><tr><td style='text-align: center;'>NID_SIGNAL</td><td style='text-align: center;'>NID_SIGNAL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>信号机的ID1~0xFFFFFFFF,0为默认值V0BC最大安全前端前方沿列车运行方向可搜索到的最近的同向信号机</td></tr><tr><td colspan="4">注1:在本接口中,CI根据V0BC发送的信号机ID回复对应的信号机状态。注2:V0BC发出允许保护区段解锁信息后,在自动或人工确认前方信号开放前,车载ATP应禁止列车前向牵引</td></tr></table>

---

# 表 33 VOBC 向 CI 发送控制信息（续）

注 $ ^{3} $ ：站台门控制命令发送时机：

(1) 从列车进入站台轨至列车停准停稳之前控制命令发送默认值；

(2)列车停准停稳之后，未进行开关站台门操作之前，控制命令发送默认值；



(3) 开关站台门操作后，应持续发送有效控制命令（开门或关门），直至采集到 CI 发送的站台门状态与期望状态一致时，开始发送默认值；

(4) 列车折返过程中，换端之后，V0BC对CI发送的站台门开关命令发送默认值，进行开关门操作之后持续发送有效的控制命令，直至采集到CI发送的站台门状态与期望状态一致时，开始发送默认值；

(5) 列车非停准停稳状态下，控制命令发送默认值；

(6) 通信故障恢复后，未进行开关站台门操作之前，控制命令发送默认值。

注4：站台门开门码定义见表34（其中上行、下行为电子地图定义的上下行方向，停车点1、停车点2的定义参见T/CAMET04010.3—2018）：

(1) V0BC 发送的站台门命令中含有开门命令时，开门码应发送有效信息；若两侧均为关门命令或默认值，则开门码信息应发送默认值。









(2) 开门码信息只对开门命令有效。若两侧 PSD 同时发送开门命令，则开门码信息对两侧 PSD 均有效；若一侧 PSD 发送开门命令，一侧发送关门命令或默认值，则开门码信息对开门命令侧有效，对另一侧无效。

(3)关门命令对对应侧全部PSD有效。



注 $ ^{5} $ : VOBC 在发送 CI 控制信息包时, PSDID 在具备站台门的情况下始终填写有效值, 在不具备站台门的情况下填写默认值。

注6：若 VOBC 处于 CBTC 等级，则可不向 CI 发送“允许解锁”（其他 PSD、信号机等相关信息照常发送）。

注7：VOBC判断下列条件同时满足时，应发送保护区段允许解锁：



(1)列车停稳；

(2)列车最大安全前端未越过估计位置所在进路末端位置（进路末端位置指列车估计位置前方第一个同向信号机所在轨道区段终点）；



(3)估计位置所在进路的终端信号机未开放，具体判断规则为：点式级别下，根据CI发送的信号机状态，判断信号机是否开放；

(4) 不再需要此进路的保护区段：列车停准且停稳时应认为不再需要，列车越过停车窗停稳时可认为不再需要。

注8：CI收到VOBC发送的保护区段允许解锁命令为允许解锁时，CI可根据VOBC发送的轨道区段ID或信号机ID解锁对应保护区段。

---

<div style="text-align: center;">表 34 开门码定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>bit7</td><td style='text-align: center;'>bit6</td><td style='text-align: center;'>bit5</td><td style='text-align: center;'>bit4</td><td style='text-align: center;'>bit3</td><td style='text-align: center;'>bit2</td><td style='text-align: center;'>bit1</td><td style='text-align: center;'>bit0</td></tr><tr><td style='text-align: center;'>上下行停车点: 0:下行; 1:上行</td><td colspan="2">停车点定义 01b:停车点1 10b:停车点2</td><td colspan="5">列车实际编组数。有效值:00001b~11111b。 例如,6编组列车取值为00110b</td></tr></table>

###### 7.3.2.2.3 VOBC 向 CI 发送城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。V0BC向CI发送城市自定义帧信息见表35。

<div style="text-align: center;">表 35 YOBC向CI发送城市自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

###### 7.3.2.2.4 VOBC 向 CI 发送厂商自定义帧

自定义信息，用于实现各厂商特有功能，各厂商分别定制，VOBC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同一厂商时方可发送市OBC向发送厂商自定义帧信息见表36。

<div style="text-align: center;">表 36 VOBC 向 CI 发送厂商自定义帧</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

###### 7.3.2.2.5 VOBC 向 CI 发送注销请求帧

在列车判断需要与 CI 断开通信时，VOBC 向 CI 发送注销信息，直至 VOBC 收到 CI 回复的注销信息，或者 VOBC 判断通信超时。

VOBC 发送的“注销请求”包、“控制信息”包、“心跳”包在同一 GAL 包中不应同时存在。

注销请求帧见表37。

---

<div style="text-align: center;">表 37 注销请求帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>无</td><td style='text-align: center;'>0</td><td style='text-align: center;'>仅有报文帧头，详见应用层信息格式定义</td></tr><tr><td colspan="3">注1：V0BC带有“注销请求帧”的GAL包中，应不带有其他信息包。注2：注销请求帧交互过程如下：(1)V0BC判断满足发送“注销请求帧”的条件后，应持续周期发送“注销请求帧”，直至收到CI发送的“注销回复帧”；(2)CI收到V0BC发送的“注销请求帧”后，应持续周期发送“注销回复帧”，直至与V0BC的通信断开；(3)V0BC收到CI发送的“注销回复帧”后，应停止发送“注销请求帧”，并断开与CI的通信；(4)4IPv0BC列车折返时，尾端V0BC应在明确获取首端V0BC已与CI注销或经过一定延时（应不小于V0BC-CI通信中断时间）后，方可向CI发送控制信息包。</td></tr></table>

#### 7.3.3 CI 向 VOBC 发送信息

##### 7.3.3.1 CI 向 VOBC 发送心跳帧

当 CI 与 VOBC 建立链接后，且尚未收到 VOBC 向 CI 发送的控制信息之前，发送该信息包，用来维持 VOBC 设备和 CI 间通信链路的连续性。

CI 向 VOBC 发送心跳帧信息见表 38。

<div style="text-align: center;">表 38 CI 向 VOBC 发送心跳帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>无</td><td style='text-align: center;'>0</td><td style='text-align: center;'>仅有报文帧头，详见应用层信息格式定义</td></tr><tr><td colspan="3">注1:CI与V0BC建立安全连接后，CI未收到V0BC发送的信息前，可周期发 送心跳帧（此功能不强制要求）。V0BC应可兼容CI发送的心跳帧“对方 清息序列号”、“收到上一条消息时本方序列号”字段取值为默认值。 注2:CI收到V0BC发送的首包信息，无法判断有效性时，发送“CI向V0BC发 送心跳帧”</td></tr></table>

##### 7.3.3.2 CI 向 VOBC 发送状态信息

当 CI 收到 VOBC 的控制信息之后，发送该信息包。

---

CI 向 VOBC 输出信息接口见表 39。

<div style="text-align: center;">表 39 CI 向 VOBC 发送状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="3">接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td colspan="3">NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>CI接收到的VOBC发送的轨道区段ID</td></tr><tr><td colspan="3">N_PSD_CMD_CODE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>CI接收到的VOBC发送的站台开门码</td></tr><tr><td colspan="3">N_PSD</td><td style='text-align: center;'>1</td><td style='text-align: center;'>回复状态的PSD的数量</td></tr><tr><td rowspan="3">PSD_1信息</td><td colspan="2">NID_PSD_1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>PSD_1的ID,1~0xFFFFFFFF0为默认值,表示当前通信位置不存在站台门</td></tr><tr><td style='text-align: center;'>PSD_1状态</td><td style='text-align: center;'>Q_PSD_1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>PSD_1的状态开门:0x55关门:0xAA(互锁解除时按照关门发送)默认值:0xFF</td></tr><tr><td style='text-align: center;'>PSD_1控制命令</td><td style='text-align: center;'>R_NC_PSD_1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>CI接收到的VOBC对PSD_1的控制命令</td></tr><tr><td rowspan="3">PSD_2信息</td><td colspan="2">NID_PSD_2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>PSD_2的ID1~0xFFFFFFFF0为默认值,表示当前通信位置不存在站台门</td></tr><tr><td style='text-align: center;'>PSD_2状态</td><td style='text-align: center;'>Q_PSD_2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>PSD_2的状态开门:0x55关门:0xAA(互锁解除时按照关门发送)默认值:0xFF</td></tr><tr><td style='text-align: center;'>PSD_2控制命令</td><td style='text-align: center;'>R_NC_PSD_2</td><td style='text-align: center;'>1</td><td style='text-align: center;'>CI接收到的VOBC对PSD_2的控制命令</td></tr></table>

---

<div style="text-align: center;">表 39 CI 向 VOBC 发送状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节 长度</td><td style='text-align: center;'>说 明</td></tr><tr><td rowspan="2">Q_SIGNAL_ASPECT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>信号机的 ID CI接收到的 V0BC 发送的信号机 ID</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>“信号机的 ID”的信号机状态 点式允许信号:0x55 点式禁止信号:0xAA 默认值:0xFF(该方向无信号机时填写)</td></tr></table>

##### 7.3.3.3 CI 向 VOBC 发送城市自定义帧

自定义信息，用于实现各城市特有的互联互通相关功能。具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。CI向V0BC发送城市自定义帧信息见表40。

<div style="text-align: center;">表 40 CI 向 VOBC 发送城市自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

##### 7.3.3.4 CI 向 VOBC 发送厂商自定义帧

自定义信息，用于实现各厂商特有功能。各厂商分别定制，V0BC收到非本厂商的厂商自定义帧后，可不进行处理。发送方判断接收方与自己属于同一厂商时方可发送。CI向V0BC发送厂商自定义帧信息见表41。

<div style="text-align: center;">表 41 CI 向 VOBC 发送厂商自定义帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

##### 7.3.3.5 CI 向 VOBC 发送注销回复帧

在 CI 接收到 VOBC 的注销请求帧后，向 VOBC 回复注销回复帧。

---

CI 发送的“注销回复”包、“状态信息”包、“心跳”包在同一 GAL 包中不应同时存在。CI 向 VOBC 发送注销回复帧信息见表 42。

<div style="text-align: center;">表 42 CI 向 VOBC 发送注销回复帧信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>无</td><td style='text-align: center;'>0</td><td style='text-align: center;'>仅有报文帧头，详见应用层信息格式定义</td></tr></table>

#### 7.3.4 列车折返过程通信说明

折返流程分为首尾端 VOBC 共用安全连接与首尾端 VOBC 不共用安全连接两种情况。本节中 VOBCI 指换端前的车头 VOBC、VOBC2 指换端前的车尾 VOBC。

##### 7.3.4.1 首尾 VOBC 共用安全连接

此种情况下，VOBC 在红蓝网上分别与 CI 建立安全连接，冗余消息在红蓝网上分别传输红网 IP 对红网 IP，蓝网 IP 对蓝网 IP）。首尾 VOBC 共同使用这组安全连接，首尾 VOBC 共用一个 VID。CI 不区分首尾端 VOBC。折返过程中，VOBC 均向 CI 发送“控制信息帧”，但“控制信息帧”中列车运行方向相反。

##### 7.3.4.2 首尾 VOBC 不共用安全连接

此种情况时车载首尾 VOBC 使用不同的 ID，首尾 VOBC 分别与 CI 建立安全连接。在折返过程中，车尾 VOBC2 与 CI 新建立安全连接，新建安全连接的时机可选择以下处理之一：

a）VOBCI 与 CI 注销完成后，VOBC2 才开始与 CI 建立连接。

b) VOBC1 与 CI 未完成注销确认前，VOBC2 开始与 CI 建立连接发送心跳包；VOBC1 与 CI 完成注销确认后，尾端开始向 CI 发送控制信息。

---

## 附录 A

(资料性附录)

ATO 控制命令帧发送更新时机示例

### A. 1 场景

车从 A 站向 D 站运行，A 站正常停车，B 站 C 站跳停，D 站、E 站正常停车。

### A.2 ATO 控制命令帧发送更新时机

ATO 控制命令帧发送更新时机见表 A.1，各阶段定义见表 A.2。

<div style="text-align: center;">表 A.1 ATS 向 VOBC 发送 ATO 控制命令帧更新时机</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>列车位置及ATO控制命令帧发送更新时机</td><td style='text-align: center;'>到站站台ID</td><td style='text-align: center;'>跳停站台ID</td><td style='text-align: center;'>下一停车站台ID</td><td style='text-align: center;'>下一站跳停命令</td><td style='text-align: center;'>站停时间</td><td style='text-align: center;'>区间运行调整命令</td></tr><tr><td style='text-align: center;'>1.A进站</td><td style='text-align: center;'>A</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A</td><td style='text-align: center;'>0xaa</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A</td></tr><tr><td style='text-align: center;'>1-2</td><td style='text-align: center;'>A</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A</td><td style='text-align: center;'>0xaa</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A</td></tr><tr><td style='text-align: center;'>2.A停稳</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>2-3</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>A</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>3.A开车</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>3-4</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>4.A出站</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>4-5</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>5.B进站</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>5-6</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr><tr><td style='text-align: center;'>6.B越过停车点</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>-</td><td style='text-align: center;'>A-B</td></tr></table>

---

<div style="text-align: center;">表 A.1 ATS 向 VOBC 发送 ATO 控制命令帧更新时机（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>列车位置及ATO控制命令帧发送更新时机</td><td style='text-align: center;'>到站站台ID</td><td style='text-align: center;'>跳停站台ID</td><td style='text-align: center;'>下一停车站台ID</td><td style='text-align: center;'>下一站跳停命令</td><td style='text-align: center;'>站停时间</td><td style='text-align: center;'>区间运行调整命令</td></tr><tr><td style='text-align: center;'>6—7</td><td style='text-align: center;'>B</td><td style='text-align: center;'>B</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>A—B</td></tr><tr><td style='text-align: center;'>7.B出站</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>7—8</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>8.C进站</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>8—9</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>9.C越过停车点</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>9—10</td><td style='text-align: center;'>C</td><td style='text-align: center;'>C</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0x55</td><td style='text-align: center;'>—</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>10.C出站</td><td style='text-align: center;'>D</td><td style='text-align: center;'>—</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0xAA</td><td style='text-align: center;'>—</td><td style='text-align: center;'>C—D</td></tr><tr><td style='text-align: center;'>10—11</td><td style='text-align: center;'>D</td><td style='text-align: center;'>—</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0xAA</td><td style='text-align: center;'>—</td><td style='text-align: center;'>C—D</td></tr><tr><td style='text-align: center;'>11.D进站</td><td style='text-align: center;'>D</td><td style='text-align: center;'>—</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0xAA</td><td style='text-align: center;'>—</td><td style='text-align: center;'>C—D</td></tr><tr><td style='text-align: center;'>11—12</td><td style='text-align: center;'>D</td><td style='text-align: center;'>—</td><td style='text-align: center;'>D</td><td style='text-align: center;'>0xAA</td><td style='text-align: center;'>—</td><td style='text-align: center;'>C—D</td></tr><tr><td style='text-align: center;'>12.D停稳</td><td style='text-align: center;'>E</td><td style='text-align: center;'>—</td><td style='text-align: center;'>E</td><td style='text-align: center;'>0xAA</td><td style='text-align: center;'>D</td><td style='text-align: center;'>D—E</td></tr><tr><td colspan="7">注:表中,1、2……表示阶段定义中的各时刻,1—2、2—3……表示各时刻之间的时间段(不含两端的时刻),“—”表示该字段发送默认值。</td></tr></table>

<div style="text-align: center;">表 A.2 ATS 向 VOBC 发送 ATO 控制命令帧</div>


<div style="text-align: center;">更新时机的各阶段定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>列车位置及ATO 控制命令帧发送 更新时机各 阶段定义</td><td style='text-align: center;'>各阶段定义</td></tr><tr><td style='text-align: center;'>1.A进站</td><td style='text-align: center;'>ATS收到列车信息帧中的安全防护点轨道区段ID和偏移量， 即列车最大安全前端到达A站站台的时刻</td></tr></table>

---

<div style="text-align: center;">表 A.2 ATS 向 VOBC 发送 ATO 控制命令帧   更新时机的各阶段定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>列车位置及ATO控制命令帧发送更新时机各阶段定义</td><td style='text-align: center;'>各阶段定义</td></tr><tr><td style='text-align: center;'>2. A停稳</td><td style='text-align: center;'>ATS开始收到列车信息帧中的停稳状态字段内容为0x55的时刻</td></tr><tr><td style='text-align: center;'>3. A开车</td><td style='text-align: center;'>ATS开始收到列车信息帧中的停稳状态字段内容不为0x55的时刻</td></tr><tr><td style='text-align: center;'>4. A出站</td><td style='text-align: center;'>列车最大安全前端离开A站站台的时刻</td></tr><tr><td style='text-align: center;'>5. B进站</td><td style='text-align: center;'>列车最大安全前端到达B站站台的时刻</td></tr><tr><td style='text-align: center;'>6. B越过停车点</td><td style='text-align: center;'>列车最大安全前端越过B站停车点的时刻</td></tr><tr><td style='text-align: center;'>7. B出站</td><td style='text-align: center;'>列车最大安全前端离开B站站台的时刻</td></tr><tr><td style='text-align: center;'>8. C进站</td><td style='text-align: center;'>列车最大安全前端到达C站站台的时刻</td></tr><tr><td style='text-align: center;'>9. C越过停车点</td><td style='text-align: center;'>列车最大安全前端越过C站停车点的时刻</td></tr><tr><td style='text-align: center;'>10. C出站</td><td style='text-align: center;'>列车最大安全前端离开C站站台的时刻</td></tr><tr><td style='text-align: center;'>11. D进站</td><td style='text-align: center;'>ATS收到列车信息帧中的安全防护点轨道区段ID和偏移量，即列车最大安全前端到达D站站台的时刻</td></tr><tr><td style='text-align: center;'>12. D停稳</td><td style='text-align: center;'>ATS开始收到列车信息帧中的停稳状态字段内容为0x55的时刻</td></tr><tr><td colspan="2">注: 表中,1,2……表示阶段定义中的各时刻。</td></tr></table>

---

# 中国城市轨道交通协会团体标准   城市轨道交通 基于通信的列车运行   控制系统（CBTC）互联互通接口规范   第2部分：CBTC系统车地连续通信协议   T/CAMET 04011.2—2018

中国铁道出版社有限公司出版发行  

(100054, 北京市西城区右安门西街 8 号)  

公司网址：http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本：880 mm × 1230 mm 1/32 印张：2.875 字数：78 千  

2019 年 5 月第 1 版 2019 年 5 月第 1 次印刷

书号：15113·5729 定价：25.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174