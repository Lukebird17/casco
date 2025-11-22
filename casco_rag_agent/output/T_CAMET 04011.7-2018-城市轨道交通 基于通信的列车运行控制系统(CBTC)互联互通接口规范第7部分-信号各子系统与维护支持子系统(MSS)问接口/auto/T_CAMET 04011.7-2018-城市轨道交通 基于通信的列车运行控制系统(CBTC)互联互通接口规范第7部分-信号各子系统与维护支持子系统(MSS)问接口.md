# 中国城市轨道交通协会团体标准

T/CAMET 04011.7-2018

城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范第7部分：信号各子系统与维护支持系统（MSS）间接口

Urban rail transit — Interface specification for interoperability of communication based train control system Part 7: Interface between signal other subsystems and maintenance support system

# 目 次

前言 VI  
引言  
1范围 1  
2规范性引用文件 1  
3术语和缩略语 2  
3.1术语 2  
3.2缩略语 3  
4总则… 4  
5接口描述 5  
6MSS- VOBC报文规范 6  
6.1接口连接方式 6  
6.2通信层次结构描述 6  
6.3接口数据描述 8  
7MSS-ZC报文规范 13  
7.1接口连接方式… 13  
7.2通信层次结构描述· 14  
7.3接口数据描述… 14  
8MSS-DSU报文规范（可选） 19  
8.1接口连接方式… 19  
8.2通信层次结构描述 19  
8.3接口数据描述… 19  
9 MSS- ATS 报文规范 22  
91接口连接方式… 22

# V

9.3接口数据描述· 23  
10 MSS-CI报文规范 30  
10.1接口连接方式 30  
10.2通信层次结构描述 30  
10.3接口数据描述… 31  
11MSS-计轴报文规范 33  
11.1接口连接方式… 33  
11.2通信层次结构描述 34  
11.3接口数据描述… 34  
12MSS-电源报文规范 36  
12.1接口连接方式… 36  
12.2通信层次结构描述 37  
12.3接口数据描述. 37  
13 MSS-LEU报文规范 45  
13.1接口连接方式… 45  
13.2通信层次结构描述 46  
13.3 接口数据描述 46  
14MSS－微机监测报文规范 49  
14.1接口连接方式… 49  
14.2通信层次结构描述 50  
14.3接口数据描述 50  
15 MSS-DCS报文规范 58  
15.1接口连接方式… 58  
15.2通信层次结构描述 59  
15.3接口数据描述 59

# 前 言

T/CAMET04011《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

第1部分：应答器报文；  
第2部分：CBTC系统车地连续通信协议；  
第3部分：车载列车白动保护（ATP）/列车白动运行（ATO）系统与车辆的接口；  
第4部分：区域控制器（ZC）间接口；  
第5部分：计算机联锁（CI）间接口；  
第6部分：列车白动监控系统（ATS）间接口；  
第7部分：信号各子系统与维护支持系统（MSS）间接口；  
第8部分：车载人机界面。

本部分是T/CAMET04011的第7部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京交通大学、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：黄友能、张瑞雪、张日新、智国盛、何丹、张尧、杨勇、李刚、章国林、胡顺定、韩琛、周晓。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、王道敏、张良、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、徐鼎。

VI

# 引 言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的日标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

# 城市轨道交通基于通信的列车运行控制系统(CBTC)互联互通接口规范第7部分：信号各子系统与维护支持系统(MSS)间接口

# 1范围

# CIATIOA

接口规范，包括互联 各系统与MSS的接 接方式、接口数据描述等。

本部分适用于国菜用基于通信的列车运行制（CBTC）系统的新让、更新改监及扩建备招轨道交通线路建设期指导信号系统的系统

# 轨道

# 2规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T12758——2004城市轨道交通信号系统通用技术条件

GB/T24339.1轨道交通通信、信号和处理系统第1部分：封闭式传输系统中的安全相关通信（IEC62280-1：2002，IDT）

GB50157—2013地铁设计规范

CJ/T407—2012城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET04010.1城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范第1部分：系统总体要求

IEEE 802.3 以太网（Ethernet)

# 3术语和缩略语

GB/T12758—2004、GB 50157—2013、CJ/T407—2012和 T/CAMET04010.1界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1术语

3.1.1

# 城市轨道交通信号urban rail transit signal

应用于城市轨道交通系统中，人T或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称

[CB/T12758—2004，术语与定义3.1]

# 3.1.2

基于通信的列车控制communication based train control(CBTC）

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T407—2012，定义3.1.1]

# 3.1.3

列车自动控制automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB50157—2013，定义2.0.37]

3.1.4

列车自动监控automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB50157—2013，定义2.0.38]

3.1.5

列车自动防护automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB50157—2013，定义2.0.39]

3.1.6

列车自动运行automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

[GB 50157—2013，定义2.0.40]

3.1.7

计算机联锁computer interlocking

以计算机技术为核心，白动实现进路、道岔、信号机等防护技术的总称

[GB 50157—2013，定义2.0.40]

3.1.8

# 维护支持系统maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，川于系统日常运营维护。

[T/CAMET 04010.1,术语3.1.8]

# 3.2缩略语

AM:列车自动驾驶模式（Automatic Train Operating Mode)  
ATC：列车白动控制（Automatic Train Control）  
ATO:列车自动运行（AutomaticTrain Operation）  
ATP:列车白动防护（Automatic Train Protection）  
ATS:列车自动监控（Automatic Train Supervision）  
BTM:应答器传输模块（BaliseTransferModule）  
CBTC：基于通信的列车控制（Communication Based Train Control）  
CI:计算机联锁（Computer Interlocking)  
CM:列车自动防护模式（Coded Train OperatingMode）

CRC:循环冗余校验(Cyclic Redundancy Check)DCS:数据通信系统(Data Communication System)EUM：非限制人T.驾驶模式（Emergency Unrestricted Train OperatinMode)IP:互联网协议地址（InternetProtocolAddress）IPv4：网际协议（InternetProtocol, IP）的第4版LEU:轨旁电子单元（LinesideElectronicUnit）MA:移动授权（Movement Authority）MAC:媒体介入控制层（Media AccessControl）MSS:维护支持系统(Maintenance Support System)MTBF:平均故障间隔时 (Mean Time Between Failures)MTTR:平均修复时间（Mean Time ToRepair)PIS:乘客信息系统(Passenger Information System)PSD:站台门(Platform Screen Door)RM : 限制人工驾驶模式（Restricted Train Operating Mode）SIL:安全完整性等级（Safety Integrity Level)TMS:列车管理系统(Train Management System)TSR : 临时限速(Temporary Speed Restriction)UDP:用户数据报协议（UserDatagram Protocol）UPS:不间断电源（Uninterruptible Power System)ZC:区域控制器（ZoneController）

# 4总则

4.1信号系统互联互通是一项系统工程，涉及需求、产品、工程、运营、维护等各个方面，需要整体规划、点面结合、分步实施。

4.2城市轨道交通CBTC系统互联互通是指装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

4.3CBTC系统互联互通的总体目标是支持轨道交通网络化运营，实现轨道交通线网建设和运营的资源共享。  
4.4互联互通的CBTC系统应采用安全可靠的产品，并应满足相关国产化政策要求。  
4.5在互联互通工程招标阶段，招标单位应在符合本规范的基础上，根据互联互通线路网络规划，补充信号系统其他相关功能、性能、接口、设计的具体需求，形成具体工程信号系统招标的技术要求。  
4.6CBTC系统涉及互联互通的设备接口应符合国际/国内/行业标准的规定，对于无相关标准规定的接口在满足系统安全、可靠、功能完整的前提下，接口定义应简单 晰凄饮谷理。  
OF  
4.7采用本互联互通 立根据相关国际/国内/行业规范确定用户 置以及特定工程须不同的具体实现方法的系统技术，制定食 要功能统一、系统架车－地信息传输的透明传输通道，采用满足GB/T24339.1标准要求的网络传输安全防护技术。  
4.10信号系统互联互通除应遵守本规范规定外，还应符合国家现行相关规范的规定。  
4.11系统采用的设备和器材应符合有关现行国家标准和有关行业标准的规定。

# 5接口描述

本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对接口数据交互内容进行扩展。

# 6MSS-VOBC报文规范

# 6.1接口连接方式

# 6.1.1物理接口

MSS子系统与VOBC子系统之间采用冗余网络进行数据通信，利用车－地无线传输系统完成交互信息发送与接收。

# 6.1.2动态交互描述

列车上电完成定位后，根据列车所处位置，确定信息上报所属的线路的MSS系统的IP地址，并周期性地向MSS系统发送状态信息，

列车进行转线作业时，当列车完全进入ZC共管区域后，需同时与两个线路的MSS系统进行周期性通信；当列车整体越过ZC共管区域边界后，VOBC系统仪与当前线路的MSS系统周期性通信。

# 6.1.3通信故障处理

MSS如果连续超过额定时间都接收不到VOBC的任何数据，则MSS认为与VOBC通信中断，MSS将VOBC设备状态设为未知。

# 6.2通信层次结构描述

# 6.2.1数据链路层

MAC子层基于IEEE802.3标准。MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。

# 6.2.2网络层

本接口使川IPv4协议作为网络层的协议。

# 6.2.3传输层

本接口实时传送的信息使用UDP协议作为传输协议。

# 6.2.4冗余层

VOBC发送的内容（vobcmsgI）按照表1格式发送。

表1VOBC帧格式  

<table><tr><td rowspan=1 colspan=1>RP 协议头num_mg</td><td rowspan=1 colspan=1>RP 协议头num_mg</td><td rowspan=1 colspan=1>msg1 id length msg1</td><td rowspan=1 colspan=1>msg1 id length msg1</td><td rowspan=1 colspan=1>msg1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>msg_id_Pr length_msgPr[</td><td rowspan=1 colspan=1>Msg_Pr</td><td rowspan=1 colspan=1>CRC</td></tr><tr><td rowspan=1 colspan=1>15个字节1字节</td><td rowspan=1 colspan=1>15个字节1字节</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=1>2字节</td><td rowspan=1 colspan=1>N个字节1字节</td><td rowspan=1 colspan=1>N个字节1字节</td><td rowspan=1 colspan=1>2字节</td><td rowspan=1 colspan=1>N个字节4个字节</td><td rowspan=1 colspan=1>N个字节4个字节</td></tr></table>

表2规定了RP协议头的内容。

表2RP协议头  

<table><tr><td rowspan=1 colspan=1>OxFF</td><td rowspan=1 colspan=1>帧长度</td><td rowspan=1 colspan=1>发送方标识</td><td rowspan=1 colspan=1>接收方标识</td><td rowspan=1 colspan=1>序列号</td></tr><tr><td rowspan=1 colspan=1>1个字节</td><td rowspan=1 colspan=1>2个字节</td><td rowspan=1 colspan=1>4个字节</td><td rowspan=1 colspan=1>4个字节</td><td rowspan=1 colspan=1>4个字节</td></tr><tr><td rowspan=1 colspan=5>“帧长度：从发送方标识至帧尾的字节长度。序列号：本方的周期计数，发送方每周期将本计数加1，序列号有效值为1~(2^-1)</td></tr></table>

表3规定了发送方和接收方标识信息的内容。

表3发送方和接收方标识信息  

<table><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小</td><td colspan="1" rowspan="1">内容</td></tr><tr><td colspan="1" rowspan="3">发送方标识信息</td><td colspan="1" rowspan="3">4字节</td><td colspan="1" rowspan="1">VOBC:0x01,MSS:0x20</td></tr><tr><td colspan="1" rowspan="1">厂商ID：对厂商统一编号</td></tr><tr><td colspan="1" rowspan="1">当发送方为VOBC时，此编号为车载编号，编号(16 bits) :15~14bit,预留;13~2bit,列车编号；1~0bit,车端号</td></tr><tr><td rowspan="2">接收方标识信息</td><td rowspan="2">VOBC:0x10,MSS:0x20 4字节</td><td></td></tr><tr><td colspan="1">厂商ID：对厂商统一编号</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td></td></tr><tr><td colspan="1">当接收方为MSS时，此设备为MSS的ID</td></tr></table>

# 6.2.5应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见6.3的规定。

# 6.3接口数据描述

# 6.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验(CRC)。

生成多项式采用 $\mathrm { C R C 3 2 } \left( \mathrm { O x 0 4 c 1 1 d b 7 } \right)$ ，按公式（1）计算：

$$
\begin{array} { r c l } { { G ( x ) } } & { { = } } & { { x ^ { 3 2 } + x ^ { 2 6 } + x ^ { 2 3 } + x ^ { 2 2 } + x ^ { 1 6 } + x ^ { 1 2 } + x ^ { 1 1 } + x ^ { 1 0 } } } \\ { { } } & { { } } & { { } } \\ { { } } & { { + x ^ { 8 } + x ^ { 7 } + x ^ { 5 } + x ^ { 4 } + x ^ { 2 } + x + 1 } } \end{array}
$$

式中：

$G ( \ v { x } _ { } ) \stackrel { } { - } \ v { x } _ { } \cdot \ v { x } _ { }$ 的32次幂生成多项式；$x$ (id) 校验的二进制数；  
余子式的初始值设为OxFFFFFFFF。

6.3.2 VOBC MSS

表4规定了VOBC发送给MSS的内容。

表4VOBC发送给MSS的信息帧  

<table><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小(Byte))</td><td colspan="1" rowspan="1">缺省值</td><td colspan="1" rowspan="1">最小值</td><td colspan="1" rowspan="1">最大值</td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描</td></tr><tr><td colspan="1" rowspan="1">msg_id</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">202</td><td colspan="1" rowspan="1">202</td><td colspan="1" rowspan="1">202</td><td colspan="1" rowspan="1">202</td><td colspan="1" rowspan="1">消息ID</td></tr><tr><td colspan="1" rowspan="1">Version_No</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">0x2001</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">65 535</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">应用层通信协议版本号</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小(c e)d:)</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">Time</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占Ⅰ个字节(北京时间)</td></tr><tr><td colspan="1" rowspan="1">DriverNo</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">65535</td><td colspan="1" rowspan="1">0表示无效</td><td colspan="1" rowspan="1">司机号</td></tr><tr><td colspan="1" rowspan="1">ChoiceMode</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">1 = IL − RM,2 =ITC: − CM,3 = ITC –AM,4 =CBTC −CM ,-AM</td><td colspan="1" rowspan="1">最商驾驶模式</td></tr><tr><td colspan="1" rowspan="1">CtrILeyel</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">ITC,</td><td colspan="1" rowspan="1">当前控制级别</td></tr><tr><td colspan="1" rowspan="1">DriveMode</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">RCM</td><td colspan="1" rowspan="1">当前驾驶模式</td></tr><tr><td colspan="1" rowspan="1">Sped</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">Oxffe</td><td colspan="1" rowspan="1">0xff三</td><td colspan="1" rowspan="1">列车当前速度( km/h)</td></tr><tr><td colspan="1" rowspan="1">EbiSpeed</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">0xffff</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">轨道</td><td colspan="1" rowspan="1">示无效</td><td colspan="1" rowspan="1">紧急制动触发速度（km/h)</td></tr><tr><td colspan="1" rowspan="1">AtpIelailF ault</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">N/A</td><td colspan="4" rowspan="1">ATP具体的板级故障报警，每—Bit代表一个故障</td></tr><tr><td colspan="1" rowspan="1">AtpInitRst</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">N/A</td><td colspan="4" rowspan="1">ATP设备门检结果，每一Bit代表一个结果，其中1表示故障，0表示正常</td></tr><tr><td colspan="1" rowspan="1">DeviceFault</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">设备故障报警（非ATP、ATO设备），每一Bit代表一个故障</td></tr><tr><td colspan="1" rowspan="1">AtoDetailFault</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">ATO具体的板级故障报警，每一Bit代表一个故障，其中1表示故障，0表示正常</td></tr><tr><td colspan="1" rowspan="1">Platform1d</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">Oxfff表示无效</td><td colspan="1" rowspan="1">站台号（列车在区间或站台停稳前发无效值，在站台停稳时站台号有效）</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小( B e))</td><td colspan="1" rowspan="1">缺省值</td><td colspan="1" rowspan="1">最小值最大值</td><td colspan="1" rowspan="1">最小值最大值</td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">AtoOperationF ault</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">ATO运行过程中的故障，每一个Bit代表一种故障</td></tr><tr><td colspan="1" rowspan="1">AtpCutofffPropulsion</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=有效</td><td colspan="1" rowspan="1">ATP切断牵引</td></tr><tr><td colspan="1" rowspan="1">AtpCouoffPropulsionReason</td><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">列车切断牵引原因，每一个Bit代表一种原因，该Bit置1表示有效</td></tr><tr><td colspan="1" rowspan="1">AtpEbA</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=行效</td><td colspan="1" rowspan="1">ATP实施常用制动</td></tr><tr><td colspan="1" rowspan="1">AtpEbAReason</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">列车常用制动原因，每一个Bit代表一种原因，该Bit置1表示有效</td></tr><tr><td colspan="1" rowspan="1">AtpE1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=有效</td><td colspan="1" rowspan="1">ATP实施紧急制动</td></tr><tr><td colspan="1" rowspan="1">AtpEbReason</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">列车紧急制动原因，每一个Bit代表一种原因，该Bit置1長示有效</td></tr><tr><td colspan="1" rowspan="1">AtpLoseloc</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=效</td><td colspan="1" rowspan="1">列车位置丢失</td></tr><tr><td colspan="1" rowspan="1">AtpLoseLocReason</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">列车丢失位置原因，每一个Bit代表一种原因，该Bit置1表示有效</td></tr><tr><td colspan="1" rowspan="1">TrainBrakeF ault</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=有效</td><td colspan="1" rowspan="1">列车制动力故障</td></tr><tr><td colspan="1" rowspan="1">FulLoad_Ratio</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">255</td><td colspan="1" rowspan="1">0~254表示百分比255为无效值</td><td colspan="1" rowspan="1">乘客满载率（默认值为0，長示此时满载率为0或者未知）若本线无此功能，发送无效值</td></tr><tr><td colspan="1" rowspan="1">电子地图版本</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">车载电子地图版本</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小( Btc))</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">ATP_Version</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0表示无效</td><td colspan="1" rowspan="1">软件版本号</td></tr><tr><td colspan="1" rowspan="1">ATO_Version</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0表示无效</td><td colspan="1" rowspan="1">软件版本号</td></tr><tr><td colspan="1" rowspan="1">MMI_Version</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0表示无效</td><td colspan="1" rowspan="1">软件版本号</td></tr><tr><td colspan="1" rowspan="1">Stopped_PrecisionATP</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0xfe</td><td colspan="1" rowspan="1">列车停车精度数值（ATP），发送-126~126之间的数值，代表停车精度数值，单位：em，其中正数代表欠标，负数代長过标。超过[-126，126]的停车精度，发送-126或126的边界值.列车非停稳时该值无效，发送值为0x7f（127）</td><td colspan="1" rowspan="1">列车的停车误差列车非停稳时该值无效，发送值为0x7f</td></tr><tr><td colspan="1" rowspan="1">Stopped_PrecisionATO</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0xfe</td><td colspan="1" rowspan="1">列乍停车精度数值(ATO），发送-126~126之间的数值，代表停车精度数值，单位：cm。其中正数代表欠标,负数代表过标。超过[-126，126]的停车精度，发送- 126或126的边界值。列车非停稳时该值无效，发送值为0x7f(127）</td><td colspan="1" rowspan="1">列车的停车误差列车非停稳时该值无效，发送值为0x7f</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小(B te)</td><td colspan="1" rowspan="1">缺省值</td><td colspan="1" rowspan="1">最小值最大值</td><td colspan="1" rowspan="1">最小值最大值</td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">Check_Result</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0xffffe</td><td colspan="1" rowspan="1">DOxfff示无效</td><td colspan="1" rowspan="1">自定义</td></tr><tr><td colspan="1" rowspan="1">VOBC_ZCID1</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">移交ZC ID</td></tr><tr><td colspan="1" rowspan="1">VOBC_ZCCOMFault1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">VOBC与ZC通信故障描述，0長示通信故障或未通信，1表示通信正常</td></tr><tr><td colspan="1" rowspan="1">VOBC_ZCID2</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">接管ZC ID，如无移交，取值OxFFFFFFFF</td></tr><tr><td colspan="1" rowspan="1">VOBC_ZCCOMFault2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">VOBC与ZC通信故障描述、0表示通信故障或未通信，1表示通信正常，无移交，取值OxFF</td></tr><tr><td colspan="1" rowspan="1">VOBC_ATSID1</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">移交ATS ID</td></tr><tr><td colspan="1" rowspan="1">VOBC_ATSCOMFault1</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">VOBC与ATS通信故障描述，0表示通信故障或未通信，1表示通信正常</td></tr><tr><td colspan="1" rowspan="1">VOBC_ATSID2</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">接管ATS ID，如无移交，取值OxFFFFFFFF</td></tr><tr><td colspan="1" rowspan="1">VOBC_ATSCOMFault2</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">VOBC与移交ATS通信故障描述，0表示通信故障或未通信，1表示通信正常，无移交，取值OxFF</td></tr><tr><td colspan="1" rowspan="1">VOBC_CIID</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">CI ID填写最后连接的CI的ID</td></tr><tr><td colspan="1" rowspan="1">VOBC_CICOMFault</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="4" rowspan="1">VOBC与CI通信故障描述，O表示通信故障或未通信，1表示通信正常</td></tr><tr><td colspan="1" rowspan="1">TrainComF ault</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=有效</td><td colspan="1" rowspan="1">ATP头尾通信故障，0代表头尾通信正常，1代表头尾通信故障</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">大小( Bye)d)</td><td colspan="1" rowspan="1">缺省值</td><td colspan="1" rowspan="1">最小值</td><td colspan="1" rowspan="1">最大值</td><td colspan="1" rowspan="1">枚举值</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">TmsComFault</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">0=无效，1=有效</td><td colspan="1" rowspan="1">与TMS通信故障，0代表与TMS通信正常，！代表与TMS通信故障</td></tr><tr><td colspan="1" rowspan="1">VOBC_HeadOrTail</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">激活段的序号：01:TC1（十进制）；02:TC2（十进制）；ff：无效，备注：VOBC头尼端信息、01为TC1.02 为 TC2, ff为无效值，即两端均不为激活端或者均为激活端.如6编组列车，1号车厢为TC1，6号车厢为TC2</td></tr><tr><td colspan="1" rowspan="1">TrainReserve</td><td colspan="1" rowspan="1">10</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">轨道</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">预留10个字节</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">N/A</td><td colspan="1" rowspan="1">CRC校验，计算范围从 msg _ id到TrainReserve</td></tr></table>

# 7MSS-ZC报文规范

# 7.1接口连接方式

# 7.1.1物理接口

MSS子系统与ZC子系统的维护单元之间采用维护网进行数据通信。其中，ZC子系统的维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 7.1.2动态交互描述

ZC子系统维护单元周期性通过维护网向MSS子系统发送报警信息。

# 7.1.3通信故障处理

MSS子系统如果超过额定时间接收不到ZC子系统维护单元的任何数据，则MSS子系统认为与ZC子系统通信中断；ZC子系统维护单元如果超过额定时间收不到MSS子系统的应答数据，则认为ZC子系统与MSS子系统通信中断（可选功能），此时ZC子系统维护单元仍保持周期性给MSS发送数据不变。

# 7.2通信层次结构描述

# 7.2.1数据链路层

MAC子层堪于IEEE802.3标准MAC头由14个字节组成，I个帧校验序列（4宇节）将被加在Ethernet 帧后面，

# 7.2.2网络层

本接口使川IPv4协议作为网络层的协议。

# 7.2.3传输层

本接口实时传送的信息使用UDP协议作为传输协议。

# 7.2.4应用层

本接口实时传送的信息使用自定义的应用层协议，具体内容见7.3的规定。

# 7.3接口数据描述

# 7.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验。

生成多项式采用CRC32（0x04cI1db7），按公式（1）计算，余子式的初始值设为0xFFFFFFFF。

# 7.3.2 $\mathbf { Z } \mathbf { C } { \longrightarrow } \mathbf { M } \mathbf { S } \mathbf { S }$

表5规定了ZC发送给MSS的信息内容。

表5ZC发送给MSS的信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x20</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节(北京时间）</td></tr><tr><td colspan="2" rowspan="1">ZC_INDEX</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">ZC的编号（十进制）ZC未开机或初始上电，ZC维护单元术收到平台发来的数据之前，ZC_INDEX = 0</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新回1，从1开始</td></tr><tr><td colspan="2" rowspan="1">Device_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备包含固件数量</td></tr><tr><td colspan="2" rowspan="1">Device(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备(1)状态0xaa:正常状态0xff:故障状态其他值,预留</td></tr><tr><td colspan="2" rowspan="1">Device( n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备(n)状态0xaa:正常状态Oxff:故障状态其他值,预留</td></tr><tr><td colspan="2" rowspan="1">HostStyle</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ZC主备状态0xaa:1系主用状态，2系备用状态0x55：1系备用状态，2系主用状态0x77:1系主用状态，2系故障0x99:1系故障，2系主用状态Oxff：双机故障其他值,预留</td></tr><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">ZC_DSU_COM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与DSU的通信状态0xaa:正常0x55:故障0x33：未知（ZC维护单元无法获取信息）Oxff：无DSU设备时的默认值</td></tr><tr><td colspan="2" rowspan="1">ZC_ ATS_COM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">ZC与ATS的通信状态Oxaa:正常0x55：故障0x33：未知（ZC维护单元无法获取信息）</td></tr><tr><td colspan="2" rowspan="1">ZC_CI_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">与ZC通信的CI数量（十进制)</td></tr><tr><td colspan="1" rowspan="2">CI(1)信息</td><td colspan="1" rowspan="1">ZC_CI_ID(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CI(1)的ID(|进制)</td></tr><tr><td colspan="1" rowspan="1">ZC_CL_COM(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与CI(D)的通信状态Oxaa:正常0x55故障0x33：未知（ZCM无法获取信息）</td></tr><tr><td colspan="1" rowspan="2">CI(n)信息</td><td colspan="1" rowspan="1">ZC_CI_ID)(n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">N/A</td></tr><tr><td colspan="1" rowspan="1">ZC_CI_COM(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与CI(n)的通信状态0xaa;正常0x55：故障0x33：未知（ZCM无法获取信息）</td></tr><tr><td colspan="2" rowspan="1">ZC_ZC_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">与ZC通信的相邻ZC数量（十进制)</td></tr><tr><td colspan="1" rowspan="2">相邻ZC(1)信息</td><td colspan="1" rowspan="1">ZC_ZC_ID(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">相邻ZC(1)的ID(十进制）</td></tr><tr><td colspan="1" rowspan="1">ZC_ZC_COM(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与相邻ZC(1)的通信状态0xaa:正常0x55：故障0x33：未知（ZCM无法获取信息）</td></tr><tr><td colspan="1" rowspan="2">相邻ZC(n)信息</td><td colspan="1" rowspan="1">ZC_ZC_ID(n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">相邻ZC(n)的ID(十进制)</td></tr><tr><td colspan="1" rowspan="1">ZC_ZC_COM(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与相邻ZC(n)的通信状态0xaa:正常0x55:故障0x33：未知（ZCM无法获取信息）</td></tr><tr><td colspan="2" rowspan="1">NID_SOFT_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">包含软件数遣</td></tr><tr><td colspan="2" rowspan="1">NID_SOFT_Ver(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">软件版本号</td></tr><tr><td colspan="2" rowspan="1">NID_SOFT_Ver(n)</td><td colspan="1" rowspan="1">OCtATI0</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="2" rowspan="1">ALXE_SEG_NUM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="2">计轴区段(1）</td><td colspan="1" rowspan="1">NID_ALX</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">ID(十进制）</td></tr><tr><td colspan="1" rowspan="1">QALXE</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">轴区      状态0x55:A</td></tr><tr><td colspan="1" rowspan="2">计轴区段(n)</td><td colspan="1" rowspan="1">NID_ALXE</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">计        (n)ID(十进制)</td></tr><tr><td colspan="1" rowspan="1">Q_ALXE_SEG</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">0x55:ARB0xaa:正常</td></tr><tr><td colspan="2" rowspan="1">Train_count</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC管辖范围内的列车数（此列车为ZC可识别的列车）</td></tr><tr><td colspan="1" rowspan="2">Train(1)</td><td colspan="1" rowspan="1">VOBC_index</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">VOBC的唯一标识0：未知列车设备ID（默认值）其他：表示可识别列车ID（十进制）（车组号）</td></tr><tr><td colspan="1" rowspan="1">ZC_VOBC_COM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与VOBC的通信状态0xaa:正常0x55:故障</td></tr><tr><td colspan="1" rowspan="2">Train( n)</td><td colspan="1" rowspan="1">VOBC_index</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">VOBC的唯—标识0:未知列车设备ID（默认值）其他：表示可识别列车ID（十进制）（车组号）</td></tr><tr><td colspan="1" rowspan="1">ZC_VOBC_COM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">ZC与VOBC的通信状态Oxaa：正常0x55:故障</td></tr><tr><td colspan="2" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">白定义字段</td></tr><tr><td colspan="2" rowspan="1">END)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从MSGID到END</td></tr></table>

# 7.3.3 MSS→ZC

MSS收到ZC的报文后，立即反馈应答。表6规定了MSS发送给ZC的信息内容。

表6MSS发送给ZC的信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息IP默认值：0x21</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td rowspan=1 colspan=1>RCV_SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>应答对应的ZC报文序列号</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，计算范围从MSG_ID到END</td></tr></table>

# 8MSS-DSU报文规范（可选）

# 8.1接口连接方式

# 8.1.1物理接口

MSS子系统与DSU子系统维护单元之间采用维护网进行数据通信。其中，DSU子系统维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 8.1.2动态交互描述

DSU子系统维护单元周期性通过维护网向MSS子系统发送报警信息。

# 8.1.3通信故障处理

MSS子系统如果超过额定时间接收不到DSU子系统的任何数据，则MSS子系统认为与DSU子系统通信中断；DSU子系统如果超过额定时间收不到MSS子系统的应答数据，则认为DSU子系统与MSS子系统通信中1断（可选功能），此时DSU子系统仍保持周期给MSS发送数据不变。

# 8.2通信层次结构描述

# 8.2.1数据链路层

MAC子层基于IEEE802.3标准。MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面。

# 8.2.2网络层

本接口使用IPv4协议作为网络层的协议。

# 8.2.3传输层

本接口实时传送的信息使用UDP协议作为传输协议。

# 8.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见8.3的规定。

# 8.3接口数据描述

# 8.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用CRC32（0x04c11db7），按公式（I）计算，余子式的初始值设为OxFFFFFFFF。

# 8.3.2 DSU MSS

表7规定了DSU发送给MSS的信息内容。

表7DSU发送给MSS的信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的开始标志默认值：0xAA</td></tr><tr><td colspan="1" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID)默认值：0x90</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个定节（北京时间）</td></tr><tr><td colspan="1" rowspan="1">DSU_INDEX</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">DSU的编号（十进制)DSU未开机或初始上电，DSU维护机未收到平台发来的数据之前，DSU_INDEX= 0</td></tr><tr><td colspan="1" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新间1，从1开始</td></tr><tr><td colspan="1" rowspan="1">Device_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备包含固作数量</td></tr><tr><td colspan="1" rowspan="1">Device( I )</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备(1)状态Oxaa:正常状态Oxf ：故障状态其他值，预留</td></tr><tr><td colspan="1" rowspan="1">Device(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">设备(n)状态Oxaa:正常状态Oxff:故障状态其他值,预留</td></tr><tr><td colspan="1" rowspan="1">HostStyle</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DSU主备状态0xaa:1系主用状态，2系备用状态0x55：1系备用状态，2系主用状态0x77：1系主用状态，2系故障0x99：1系故障，2系主川状态其他值，预留</td></tr><tr><td colspan="1" rowspan="1">NID_SOFT_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">包含软件数量</td></tr><tr><td colspan="1" rowspan="1">NID_SOFT_Ver(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">软件版本号</td></tr><tr><td colspan="1" rowspan="1">NID_SOFT_Ver( n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1"></td></tr><tr><td colspan="1" rowspan="1">VOTE_STATUS_A</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">主机1和主机2）0xaa:一致0x55.不或初始上电）</td></tr><tr><td colspan="1" rowspan="1">VOTE_STATUS_B</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">机3和主机4）0xaa:一致0x55：不一致未开机或初始上电）</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">能道子</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识，默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范围从MSG_1D到END</td></tr></table>

# 8.3.3 MSS→DSU

表8规定了MSS发送给DSU内容。

表8MSS发送给DSU的信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的开始标志默认值：0xAA</td></tr><tr><td colspan="1" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x91</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、口、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="1" rowspan="1">RCV_SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">应答对应的DSU报文序列号</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范围从MSG_ID到END</td></tr></table>

# 9MSS-ATS报文规范

# 9.1接口连接方式

# 9.1.1物理接口

MSS子系统与ATS子系统维护单元之间采用维护网进行数据通信。其中，ATS子系统维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 9.1.2动态交互描述

ATS与MSS之间交互的数据包括心跳信息、ATS报警信息、ATS系统软件版本号、ATS行车信息（含CI站场信息）、ATS操作记录。在相同周期内，不同类型数据的SN顺序编写。同周期的相同类型数据的SN相同。

# a）心跳信息

心跳帧用于双方保持通信连接正常。MSS周期性发送心跳帧给ATS，ATS周期性发送心跳帧给MSS。

b）ATS报警信息  
ATS周期性向MSS发送当前全体ATS报警信息。c）ATS系统软件版本号

首次连接、断链重连后或系统软件版本号发生变更后，ATS向MSS发送一次全体ATS系统软件版本号。

d）ATS行车信息（含CI站场信息）

ATS周期性实时向MSS传递站场状态数据、站场同步数据，数据以联锁集中区为划分单元。ATS保证每次发送给MSS的一包数据中，不出现重复的信息。

ATS周期性实时向MSS传递车次追踪数据等。

e）ATS操作记录

当发现有新的操作记录时，ATS立即将操作记录发给MSS。

# 9.1.3通信故障处理

如果MSS超过额定时间未收到心跳，认为双方连接出现故障，ATS设备状态为末知，并向ATS发起重连申请；如果ATS超过额定时间未收到心跳，认为双方连接出现故障，此时ATS方重置通信链路，等待MSS重连。

# 9.2通信层次结构描述

# 9.2.1数据链路层

MAC 子层基于IEEE 802.3标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在thernet帧后面。

# 9.2.2网络层

本接口使用IPv4协议作为网络层的协议。

# 9.2.3传输层

本接口使用UDP协议作为传输协议。

# 9.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见9.3的规定。

# 9.3接口数据描述

# 9.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用CRC32（0x04c11db7），按公式（1）计算，余子式的初始值设为OxFFFFFFFF。

9.3.2 ATS $\longrightarrow$ MSS

9.3.2.1心跳信息

表9规定了ATS发送给MSS的心跳信息内容。

表9ATS发送给MSS的心跳信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>IEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值：0x50</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个宇节（北京时间）</td></tr><tr><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>预留字节</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从LEN到END</td></tr></table>

# 9.3.2.2报警信息

表10规定了ATS发送给MSS的报警信息内容。

表10ATS发送给MSS的报警信息帧  

<table><tr><td colspan="3" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="3" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="3" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="3" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="3" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x51</td></tr><tr><td colspan="3" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="3" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至0xFFFFFFFF后，下一次重新从1开始累加</td></tr><tr><td colspan="3" rowspan="1">ALARM_NUM</td><td colspan="1" rowspan="1">ATION</td><td colspan="1" rowspan="1">报警总数</td></tr><tr><td colspan="1" rowspan="3">ALARM(1)</td><td colspan="2" rowspan="1">ALARM_DEV</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">警设备（1）编号</td></tr><tr><td colspan="2" rowspan="1">ALARM_</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">类型</td></tr><tr><td colspan="1" rowspan="1">ALARM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">数</td></tr><tr><td colspan="1" rowspan="3">ALARM(n)</td><td colspan="1" rowspan="1">ALARM_</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">备(n)编号</td></tr><tr><td colspan="2" rowspan="1">ALARM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">类型</td></tr><tr><td colspan="2" rowspan="1">ALARM_PAI</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">参数</td></tr><tr><td colspan="3" rowspan="1">Private</td><td colspan="1" rowspan="1">九道交</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="3" rowspan="1">ENI</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">帧的结求标识默认值：0x55</td></tr><tr><td colspan="3" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从LEN到END</td></tr></table>

# 9.3.2.3版本信息

表11规定了ATS发送给MSS的版本信息内容。

表11ATS发送给MSS的版本信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">L.EN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束)</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x52</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、H、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新从1开始累加重连后序列号继续累加，不置1</td></tr><tr><td colspan="2" rowspan="1">ATS_ID</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">ATS设备编号</td></tr><tr><td colspan="2" rowspan="1">VERSION_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">版本号总数</td></tr><tr><td colspan="1" rowspan="2">DEVICE(1)</td><td colspan="1" rowspan="1">DEVICE_ID(1 )</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">设备(1)编号</td></tr><tr><td colspan="1" rowspan="1">DEVICE _VERSION(1)</td><td colspan="1" rowspan="1">+</td><td colspan="1" rowspan="1">设备(1)版本号</td></tr><tr><td colspan="1" rowspan="2">DEVICE (n)</td><td colspan="1" rowspan="1">DEVICE_ID( n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">设备(n)编号</td></tr><tr><td colspan="1" rowspan="1">DEVICE _VERSION (n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">设备(n)版本号</td></tr><tr><td colspan="2" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="2" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC 校验，校验范用从LEN到END</td></tr></table>

# 9.3.2.4站场信息

表12规定了ATS发送给MSS的站场信息内容。

表12ATS发送给MSS的站场信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值：0x53</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个宇节（北京时间）</td></tr><tr><td rowspan=1 colspan=1>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td rowspan=1 colspan=1>站场状态数据长度</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>描述除长度本身的两个字节以外的站场状态数据长度</td></tr><tr><td rowspan=1 colspan=1>站场状态数据</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>用户自定义</td></tr><tr><td rowspan=1 colspan=1>站场同步数据长度</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>描述除长度本身的两个字节以外的站场同步数据长度</td></tr><tr><td rowspan=1 colspan=1>站场同步数据</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>用户自定义</td></tr><tr><td rowspan=1 colspan=1>车次追踪数据长度</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>描述除长度本身的两个字节以外的车次追踪数据长度</td></tr><tr><td rowspan=1 colspan=1>车次追踪数据</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>用户自定义</td></tr><tr><td rowspan=1 colspan=1>临时限速状态数据长度</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>描述除长度本身的两个字节以外的临时限速状态数据长度</td></tr><tr><td rowspan=1 colspan=1>临时限速状态数据</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>用户自定义</td></tr><tr><td rowspan=1 colspan=1>牵引供电信息长度</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>描述除长度本身的两个字节以外的牵引供电信息长度</td></tr><tr><td rowspan=1 colspan=1>牵引供电信息</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>用户自定义</td></tr></table>

表12ATS发送给MSS的站场信息帧  

<table><tr><td rowspan=1 colspan=1>接1内容</td><td rowspan=1 colspan=1>宇节长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>Private</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>自定义字段</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范用从LEN到END</td></tr></table>

# 9.3.2.5操作信息

表13规定了ATS发送给MSS的操作信息内容。

表13ATS发送给MSS的操作信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x54</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、1、时、分、秒各占1个字节(北京时间）</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加、累计至OxFFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td colspan="2" rowspan="1">RECORD_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">操作记录总数</td></tr><tr><td colspan="1" rowspan="4">RECORD(1)</td><td colspan="1" rowspan="1">操作记录长度</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">描述本条操作的长度，表示从源机器ID到命令参数最后一个字节的字节数</td></tr><tr><td colspan="1" rowspan="1">源机器ID</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">设备ID</td></tr><tr><td colspan="1" rowspan="1">操作类型</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">用户自定义</td></tr><tr><td colspan="1" rowspan="1">操作参数</td><td colspan="1" rowspan="1">不定长</td><td colspan="1" rowspan="1">用户自定义</td></tr><tr><td colspan="1" rowspan="4">RECORD(n)</td><td colspan="1" rowspan="1">操作记录长度</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">描述本条操作的长度，表示从源机器ID到命令参数最后一个字节的字节数</td></tr><tr><td colspan="1" rowspan="1">源机器ID</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">设备ID</td></tr><tr><td colspan="1" rowspan="1">操作类型</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">用户自定义</td></tr><tr><td colspan="1" rowspan="1">操作参数</td><td colspan="1" rowspan="1">不定长</td><td colspan="1" rowspan="1">用户自定义</td></tr><tr><td colspan="2" rowspan="1">Private.</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="2" rowspan="1">END</td><td colspan="1" rowspan="1">SOCIATI7</td><td colspan="1" rowspan="1">55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC权    验范围从LEN到END</td></tr></table>

# 9.3.3 MSS ATS

表14MISS发送给ATS的信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度市</td><td rowspan=1 colspan=1>轨道交 描台述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志，默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID,默认值：0x57</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节(北京时问)</td></tr><tr><td rowspan=1 colspan=1>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>预留字节</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从LEN到END</td></tr></table>

# 10 MSS-CI报文规范

# 10.1接口连接方式

# 10.1.1物理接口

MSS子系统与联锁子系统维护单元之间采用维护网进行数据通信。其中，联锁子系统维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 10.1.2动态交互描述

联锁子系统周期性向MSS子系统发送全部信息，包括：联锁报警信息、联锁软件版本号、联锁设备状态信息。

MSS子系统周期性发送·次心跳帧给联锁

# 10.1.3通信故障处理

MSS子系统如果超过额定时间接收不到联锁子系统的任何数据，则MSS子系统认为与联锁子系统通信中断；联锁子系统如果超过额定时间收不到MSS子系统的应答数据，则认为联锁子系统与MSS子系统通信中断（可选功能），此时联锁子系统仍保持周期给MSS发送数据不变，

# 10.2通信层次结构描述

# 10.2.1数据链路层

MAC子层基于IEEE802.3标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面。

# 10.2.2络层

本接口使用IPv4协议作为网络层的协议。

# 10.2.3传输层

本接口使用UDP协议作为传输协议。

# 10.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见10.3的规定。

# 10.3 接口数据描述

# 10.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用CRC32（0x04c11db7），按公式（1）计算，余子式的初始值设为OxFFFFFFFF。

# 10.3.2联锁 MSS

10.3.2.1报警及设备信息

表15规定了联锁发送给MSS的报警及设备信息内容。

表15联锁发送给MSS的报警及设备信息帧  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>大小（Byte)</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值：0x40</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td rowspan=1 colspan=1>SN.</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新从1开始累加重连后序列号继续累加，不置1</td></tr><tr><td rowspan=1 colspan=1>CI_ID</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>联锁设备编号</td></tr><tr><td rowspan=1 colspan=1>CI_INFO</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>联锁站场信息</td></tr><tr><td rowspan=1 colspan=1>CI_IO</td><td rowspan=1 colspan=1>n</td><td rowspan=1 colspan=1>驱动采集数据</td></tr><tr><td rowspan=1 colspan=1>Private</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>自定义字段</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从LEN到END</td></tr></table>

# 10.3.2.2软件版本信息

表16规定了联锁发送给MSS的版本信息内容。

表16联锁发送给MSS的版本信息帧  

<table><tr><td rowspan=1 colspan=2>名称</td><td rowspan=1 colspan=1>大小(Byte)</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=2>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=2>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=2>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息I1)默认值：0x41</td></tr><tr><td rowspan=1 colspan=2>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td rowspan=1 colspan=2>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下次重新从1开始累加重连后序列号继续累加，不1</td></tr><tr><td rowspan=1 colspan=2>CL_I)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>联锁设备编号</td></tr><tr><td rowspan=1 colspan=2>VERSION_NUM</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>版本号总数</td></tr><tr><td rowspan=2 colspan=1>DEVICE(1)</td><td rowspan=1 colspan=1>DEVICE_ID(1)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备(1)编号</td></tr><tr><td rowspan=1 colspan=1>DEVICE _VERSION(1)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备(1)版本号</td></tr><tr><td rowspan=2 colspan=1>DEVICE(n)</td><td rowspan=1 colspan=1>DEVICE_ID(n)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备(n)编号</td></tr><tr><td rowspan=1 colspan=1>DEVICE _VERSION(n)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备(n)版本号</td></tr><tr><td rowspan=1 colspan=2>Private</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>自定义字段</td></tr><tr><td rowspan=1 colspan=2>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=2>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从LEN到END</td></tr></table>

# 10.3.3 MSS 联锁

表17规定了MSS发送给联锁的信息内容

表17MSS发送给联锁的信息帧  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>大小（Byte)</td><td rowspan=1 colspan=1>描   述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_ID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值:0x4</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>个字节(北京时间）</td></tr><tr><td rowspan=1 colspan=1>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>留字节默认值：0</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>束标识默认值：</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从到ENID</td></tr></table>

# 11 MSS-计轴报文规范

# 轨道

# 11.1接口连接方式

# 11.1.1物理接口

MSS子系统与计轴子系统维护单元之间采用维护网进行数据通信。其中，计轴子系统维护单元提供Ⅰ路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 11.1.2动态交互描述

计轴子系统维护单元周期性通过维护网向MSS子系统发送报警信息。

# 11.1.3通信故障处理

MSS子系统如果超过额定时间接收不到计轴子系统的任何数据，则

MSS子系统认为与计轴子系统通信中断；计轴子系统如果超过额定时间收不到MSS子系统的应答数据，则认为计轴子系统与MSS子系统通信中断（可选功能），此时计轴子系统仍保持周期给MSS发送数据不变。

# 11.2通信层次结构描述

# 11.2.1数据链路层

MAC子层基于IEEE802.3标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面.

# 11.2.2网络层

本接口使用IPv4协议作为网络层的协议。

# 11.2.3传输层

本接口实时传送的信息使用UDP协议作为传输协议。

# 11.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见11.3的规定.

# 11.3接口数据描述

# 11.3.1数据存储方式

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

# 11.3.2 计轴→MSS

表18规定了计轴发送给MSS的信息内容。

表18计轴发送给MSS的信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="1" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从帧头到帧尾）</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x70</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="1" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td colspan="1" rowspan="1">AXLE_INDEX</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">计轴子系统的车站编号</td></tr><tr><td colspan="1" rowspan="1">AXLE_SECTION _STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">计轴区段(1)状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE _SECTION _STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">计轴区段(n)状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE_ SENSOR_STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">传感器(1)状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE SENSORSTATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">传感器(n)状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE_TYPE_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">设备种类</td></tr><tr><td colspan="1" rowspan="1">AXLE_TYPE(1)_STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">TYPE(1)类型设备编号(1)的状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE_TYPE(1)_STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">TYPE(1）类型设备编号（n)的状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE_TYPE(n)_STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">TYPE(n)类型设备编号（1）的状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">AXLE_TYPE(n)_STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">TYPE（n)类型设备编号（n）的状态状态根据厂家信息进行约定</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0xAA</td></tr></table>

# 11.3.3 MSS 计轴

表19规定了MSS发送给计轴的信息内容。

表19MSS发送给计轴的信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节大小</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_I)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值：0x78</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节(北京时间)</td></tr><tr><td rowspan=1 colspan=1>RCV_SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>对应计轴报信息包中的帧序列号</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，计算范围从MSG_ID到END)</td></tr></table>

# 12MSS-电源报文规范

# 12.1接口连接方式

# 12.1.1物理接口

MSS子系统与电源子系统维护单元之间采用维护网进行数据通信。其中，电源子系统维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 12.1.2动态交互描述

电源子系统维护单元周期性通过维护网向MSS子系统发送报警信息。

# 12.1.3通信故障处理

MSS子系统如果超过额定时间接收不到电源子系统的任何数据，则MSS子系统认为与电源子系统通信中断；电源子系统如果超过额定时间收不到MSS子系统的应答数据，则认为电源子系统与MSS子系统通信中

断（可选功能），此时电源子系统仍保持周期给MSS发送数据不变。

# 12.2通信层次结构描述

# 12.2.1数据链路层

MAC子层基于IEEE802.3标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。

# 12.2.2 网络层

本接口使用IPv4协议作为网络层的协议。

# 12.2.3 传输层

本接口实时传送的信息使甩A协议作为传输协议。

# 12.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容见12.3的规定。

# 12.3 接口数据描述

12.3.1数据存储方式和通信校验方法

接口数据存储方式深用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC

生成多项式采用CRC32（0x046117），按公式（1）计算，余子式的初始值设为OxFFFFFFFF。

# 12.3.2电源 MSS

模拟量数目/状态量数目/告警量数目：

按照实际值大小传输。如果某个量数目为0，那么这个量的内容为空，其后紧接的是下一个量的数目。

模拟量：

a) 电源屏模拟量按照字节（Byte）传输，1个模拟量占2个字节，模拟量数值放大100倍；  
b) UPS模拟量按照标准的浮点数传输，1个模拟量站4个字节，模拟量数值不放大。

状态量：

a）电源屏状态量按照字节（Byte)传输，1个状态量占用1字节(Byte);

b)UPS无状态量。

告警量：

a) 电源屏及UPS告警量按照位（Bit）传输，1个告警量占用1位（Bit），总共需要的占用的字节数如下：1）如果告警量数量是8的整数倍，则告警量占用的字节数为：告警量数量/8；2) 如果告警量数量不是8的整数倍，则告警量占用的字节数为：告警量数量 $/ 8 + 1$

b）电源屏及UPS告警量由每个字节低位（0位）向高位（7位）依次填充，如果当前的字节被填充完，则填充下一个字节。如果告警量不足8的整数倍，则剩余的位填充0。

注：告警举例：假如有9个告警需要传输，则需要用2个字节传输。第一个字节0\~7位依次填充告警1\~8，第二个字节0位填充告警9，第二个字节1\~7位没有使用，填充0。见表20。

表20给出了电源告警实例。

表20电源告警实例  

<table><tr><td rowspan=1 colspan=1>告警序号</td><td rowspan=1 colspan=1>告警1</td><td rowspan=1 colspan=1>告警2</td><td rowspan=1 colspan=2>告警3</td><td rowspan=1 colspan=2>告警4</td><td rowspan=1 colspan=2>告警5</td><td rowspan=1 colspan=2>告警6</td><td rowspan=1 colspan=2>告警7</td><td rowspan=1 colspan=1>告警8</td><td rowspan=1 colspan=1>告警9</td></tr><tr><td rowspan=1 colspan=1>是否告警</td><td rowspan=1 colspan=1>有</td><td rowspan=1 colspan=1>无</td><td rowspan=1 colspan=2>无</td><td rowspan=1 colspan=2>有</td><td rowspan=1 colspan=2>有</td><td rowspan=1 colspan=2>无</td><td rowspan=1 colspan=2>无</td><td rowspan=1 colspan=1>有</td><td rowspan=1 colspan=1>有</td></tr><tr><td rowspan=1 colspan=1>位序号</td><td rowspan=1 colspan=1>0</td><td rowspan=1 colspan=1>1</td><td></td><td rowspan=1 colspan=2>2</td><td rowspan=1 colspan=2>3</td><td rowspan=1 colspan=2>4</td><td rowspan=1 colspan=2>5</td><td rowspan=1 colspan=2>6</td><td rowspan=1 colspan=1>7</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>1(告警1)</td><td rowspan=1 colspan=1>0(告警2)</td><td></td><td rowspan=1 colspan=2>0(告警3)</td><td rowspan=1 colspan=2>1(告警4)</td><td rowspan=1 colspan=2>1(告警5)</td><td rowspan=1 colspan=2>0(告警6)</td><td rowspan=1 colspan=2>0(告警7)</td><td rowspan=1 colspan=1>1(告警8)</td></tr><tr><td rowspan=1 colspan=1>第二个字节</td><td rowspan=1 colspan=1>1（告警9)</td><td rowspan=1 colspan=1>0(填充0)</td><td></td><td rowspan=1 colspan=2>0(填充0)</td><td rowspan=1 colspan=2>0(填充0)</td><td rowspan=1 colspan=2>0(填充0)</td><td rowspan=1 colspan=2>0(填充0)</td><td rowspan=1 colspan=2>0(填充0)</td><td rowspan=1 colspan=1>0(填充0)</td></tr></table>

# 12.3.2.1电源报文

表21规定了电源发送给MSS的信息内容。

表21电源发送给MSS的电源信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSGID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x30</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">STATION_INDEX</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">站点编号</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后,下一次重新回0，从1开始</td></tr><tr><td colspan="1" rowspan="3">PMS_INPUT_ANALOG</td><td colspan="1" rowspan="1">INPUT_ANALOG_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">系统输人模拟量个数n</td></tr><tr><td colspan="1" rowspan="1">INPUT_ANALOG(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">系统输人模拟量1</td></tr><tr><td colspan="1" rowspan="1">INPUT_ANALOG(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">系统输人模拟量n</td></tr><tr><td colspan="1" rowspan="2">PMS_SWITCH_STATE</td><td colspan="1" rowspan="1">SWITCH_STATE_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">开关状态量个数n</td></tr><tr><td colspan="1" rowspan="1">SWITCH_STATE(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">开关状态量10：断开；1：闭合</td></tr><tr><td colspan="2" rowspan="1">接1内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">PMS_SWITCH_STATE</td><td colspan="1" rowspan="1">SWITCH_STATE(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">开关状态量n0：断开；1：闭合</td></tr><tr><td colspan="1" rowspan="3">PMS_ALARM</td><td colspan="1" rowspan="1">ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">输入输出告警个数n</td></tr><tr><td colspan="1" rowspan="1">ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">输入输出告警10正常/1告</td></tr><tr><td colspan="1" rowspan="1">ALARM(n)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">输人输出告n0正常/1告警</td></tr><tr><td colspan="1" rowspan="3">PMS_OUTPUT_ ANALOG</td><td colspan="1" rowspan="1">OUTPUT_ ANALOG_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">输出模拟最数in</td></tr><tr><td colspan="1" rowspan="1">OUTPUT_ ANALOG(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">输出模拟量1</td></tr><tr><td colspan="1" rowspan="1">OUTPUT_ ANALOG(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">输出模拟量n</td></tr><tr><td colspan="2" rowspan="1">PWR_MODULE_ TYPE_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块类型总数m</td></tr><tr><td colspan="2" rowspan="1">PWR_MODULE_TYPE(1)_TYPE</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型1的模块类型码</td></tr><tr><td colspan="2" rowspan="1">PWR_MODULE_TYPE(1)_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型1的模块数量n</td></tr><tr><td colspan="1" rowspan="4">PWR_MODULE_TYPE(1)_1</td><td colspan="1" rowspan="1">PWR_MODULE_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块序号</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ OUTPUT_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量个数n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ OUTPUT(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量1</td></tr><tr><td colspan="1" rowspan="1">W_ MODULE _PUTPUT(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量n</td></tr><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="6">PWR_MODULE_TYPE(1)_1</td><td colspan="1" rowspan="1">PWR _ MODULE – STATUS.NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块状态量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量1</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块告警量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR MODULE   LARM（1</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块状态量10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">PWRMODULE ALARM</td><td colspan="1" rowspan="1">Bit</td><td colspan="1" rowspan="1">模块状态量n0正常/1告警</td></tr><tr><td colspan="1" rowspan="10">PWR _ MODULE _ TYPE(1)_n+</td><td colspan="1" rowspan="1">R_MODULFID</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">模块序号</td></tr><tr><td colspan="1" rowspan="1">MODULE _OUTIPUTUM</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">模块输出模拟量个数n</td></tr><tr><td colspan="1" rowspan="1">MODULE _OUTPUT</td><td colspan="1" rowspan="1">场</td><td colspan="1" rowspan="1">模块输出模拟量1</td></tr><tr><td colspan="1" rowspan="1">轨道(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量n</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULESTATUS_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块状态量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量1</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块告警量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警量10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ ALARM(n)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警量n0正常/1告警</td></tr><tr><td colspan="2" rowspan="1">PWR_MODULE_TYPE(m)_TYPE</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型m的模块类型码</td></tr><tr><td colspan="2" rowspan="1">PWR_MODULE_TYPE(m)_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型m的模块数量n</td></tr><tr><td colspan="1" rowspan="10">PWR _ MODULE _ TYPE(m)_1</td><td colspan="1" rowspan="1">PWR_MODULE_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块序号</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULE _OUTPUTNUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量个数n</td></tr><tr><td colspan="1" rowspan="1">PWRMODULE _OUTPUT(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量1</td></tr><tr><td colspan="1" rowspan="1">PWRMODULEOUTPUT(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量n</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULE _STATUSNUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块状态量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量1</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量n</td></tr><tr><td colspan="1" rowspan="1">PWRMODULEALARMNUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块告警量数量</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE –ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE –ALARM(n)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警n0正常/1告警</td></tr><tr><td colspan="1" rowspan="3">PWR _ MODULE – TYPE(m)_n</td><td colspan="1" rowspan="1">PWR_MODULE_D</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块序号</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULE_OUTPUT.NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量个数n</td></tr><tr><td colspan="1" rowspan="1">PWR — MODULE _OUTPUT(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量1</td></tr><tr><td colspan="1" rowspan="7">PWR _ MODULE _ TYPE(m)_n</td><td colspan="1" rowspan="1">PWR _ MODULE _ OUTPUT(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块输出模拟量n</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULE _STATUS–NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块状态量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ STATUS(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量1</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _STATUS(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">模块状态量n</td></tr><tr><td colspan="1" rowspan="1">PWR_MODULE _ALARMNUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模块告警量数量n</td></tr><tr><td colspan="1" rowspan="1">PWR _MODULE _ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警量10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">PWR _ MODULE _ ALARM(n)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">模块告警量n0正常/1告警</td></tr><tr><td colspan="2" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="2" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范围从MSG_ID到 END</td></tr></table>

# 12.3.2.2 UPS报文

表22规定了电源发送给MSS的UPS信息内容。

表22电源发送给MSS的UPS信息帧  

<table><tr><td colspan="2" rowspan="1">名称</td><td colspan="1" rowspan="1">大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">名称</td><td colspan="1" rowspan="1">大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">ci</td><td colspan="1" rowspan="1">消息ID默认值：0x33</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">STATION_INDEX</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">站点编号</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td colspan="2" rowspan="1">UPS_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">UPS数目</td></tr><tr><td colspan="1" rowspan="7">UPS_1</td><td colspan="1" rowspan="1">UPS_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">UPS的序号</td></tr><tr><td colspan="1" rowspan="1">UPS_ANALOG_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">UPS模拟量数量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ ANALOG(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">UPS模拟量1</td></tr><tr><td colspan="1" rowspan="1">UPS_ ANALOG(n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">UPS模拟量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">UPS告警量数量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">UPS告警量10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">UPS_ALARM(n)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">UPS告警量n0正常/1告警</td></tr><tr><td colspan="1" rowspan="7">UPS_n</td><td colspan="1" rowspan="1">UPS_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">UPS的序号</td></tr><tr><td colspan="1" rowspan="1">UPS_ ANALOG_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">UPS模拟量数量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ ANALOG(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">UPS模拟量1</td></tr><tr><td colspan="1" rowspan="1">UPS_ ANALOG(n)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">UPS模拟量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">UPS告警量数量n</td></tr><tr><td colspan="1" rowspan="1">UPS_ALARM(1)</td><td colspan="1" rowspan="1">1 Bit</td><td colspan="1" rowspan="1">UPS告警量10正常/1告警</td></tr><tr><td colspan="1" rowspan="1">UPS_ALARM(n)</td><td colspan="1" rowspan="1">1Bit</td><td colspan="1" rowspan="1">UPS告警量n0正常1告警</td></tr><tr><td colspan="1" rowspan="1">名称</td><td colspan="1" rowspan="1">火小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范I围从MSG_ID到END</td></tr></table>

# 12.3.3 MSS→电源

表23规定了MSS发送给电源的信息内容。

# 表23 MSS发详给电源的信息帧

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>大小（BYTE）</td><td rowspan=1 colspan=1>述</td></tr><tr><td rowspan=1 colspan=1>HEADER</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>贞     从MSG_ID开始到     校验结束）</td></tr><tr><td rowspan=1 colspan=1>MSG_I1)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID:国城源对应值0x36对应值0x39</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>饭日轨道秘年1个字节（北京时间）</td></tr><tr><td rowspan=1 colspan=1>RCV_SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>应答对应的电源报文序列号</td></tr><tr><td rowspan=1 colspan=1>ENI)</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结求标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，计3范围从MSG_ID到END</td></tr></table>

# 13 MSS-LEU报文规范

# 13.1接口连接方式

# 13.1.1物理接口

MSS子系统与LEU子系统维护单元之间采用维护网进行数据通信。其中，LEU子系统维护单元提供1路标准的以太网接口进行通信；MSS

子系统提供标准的以太网接口进行通信

# 13.1.2动态交互描述

LEU子系统维护单元周期性通过维护网向MSS子系统发送报警信息。

# 13.1.3通信故障处理

MSS子系统如果超过额定时间接收不到LEU子系统的任何数据，则MSS子系统认为与LEU子系统通信中断;LEU子系统如果超过额定时间收不到MSS子系统的应答数据，则认为LEU子系统与MSS子系统通信中断（可选功能），此时LEU子系统仍保持周期给MSS发送数据不变。

# 13.2通信层次结构描述

# 13.2.1数据链路层

MAC子层县丁IEEE802.3标准MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面

# 13.2.2网络层

本接1使用IPv4协议作为网络层的协议

# 13.2.3传输层

本接口实时传送的信息使用UDP协议作为传输协议。

# 13.2.4应用层

本接口实时传送的信息使用门定义的应用层协议，具体内容参见13.3的规定

# 13.3接口数据描述

# 13.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用CRC32（0x04c11db7），按公式（1）计算，余子式的初始值设为OxFFFFFFFF

# 13.3.2 LEU MSS

表24规定了LEU发送给MSS的信息内容。

表24LEU发送给MSS的信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息 ID默认值：0x80</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">STATION_INDEX</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">车站的编号</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">帧序列号，初始值为1，发送次报警信息自动累加，累计至OxFFFFFFFF后，下一次重新回0，从1开始</td></tr><tr><td colspan="2" rowspan="1">LEU_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU数量</td></tr><tr><td colspan="1" rowspan="7">LEU(1)</td><td colspan="1" rowspan="1">LEU_INDEX(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">LEU在所属车站的编号</td></tr><tr><td colspan="1" rowspan="1">LEU(1)_STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU（1）主机状态0x00无效表示LEU监测软件接收不到LEU的状态帧，主机状态未知0xaa:正常;0x55:故障</td></tr><tr><td colspan="1" rowspan="1">LEU(1) DEV(1)_STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU(1)的DEV(1)状态</td></tr><tr><td colspan="1" rowspan="1">LEU(1)_ DEV(n)_STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU（n)的DEV（1）状态</td></tr><tr><td colspan="1" rowspan="1">ND_LEU _SW_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU软件数量</td></tr><tr><td colspan="1" rowspan="1">NID_SW(1)LEU(1)</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">LEU(1）的SW（1）软件版本号</td></tr><tr><td colspan="1" rowspan="1">NID_SW(n)_LEU(1)</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">LEU(1）的SW(n)软件版本号</td></tr><tr><td colspan="1" rowspan="7">LEU(n)</td><td colspan="1" rowspan="1">LEU_INDEX(1)</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">LEU在所属车站的编号</td></tr><tr><td colspan="1" rowspan="1">LEU(1)_ STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU(1)主机状态0x00无效表示LEU监测软件接收不到LEU的状态帧，主机状态未知0xaa:正常;0x55：故障</td></tr><tr><td colspan="1" rowspan="1">LEU(1). DEV(1)_STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU(1)的DEV(1)状态</td></tr><tr><td colspan="1" rowspan="1">LEU(1)_ DEV(n)_STATUS</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU(n)的DEV(1)状态</td></tr><tr><td colspan="1" rowspan="1">NID_ LEU _SW_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">LEU软件数量</td></tr><tr><td colspan="1" rowspan="1">NID_SW(1)_IFU(1)</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">LEU(1）的SW（1）软件版本号</td></tr><tr><td colspan="1" rowspan="1">NID_SW(n)_LEU(1)</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">LEU(1）的SW(n)软件版本号</td></tr><tr><td colspan="2" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="2" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结求标识默认值：0x55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范同从MSG_ID)到END</td></tr></table>

# 13.3.3 MSS LEU

表25规定了LEU发送给MSS的信息内容。

表25MSS发送给LEU的信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节大小</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="1" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从MSG_ID开始到CRC校验结束）</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x88</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="1" rowspan="1">RCV_SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">对应LEU报警信息包中的帧序列号</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，计算范围从MSG_ID到END</td></tr></table>

# 14MSS-微机监测报文规范

# 14.1接口连接方式

# 14.1.1物理接口

CSOCIATIONOK

MSS子系统与微机监测子系统维护单元之间采月维护网进数据通信。其中，微机监测全系统维护单元提供1路标准的以太网接口进行通信；MSS子系统提供标准的以太网接口进行通信。

# 14.1.2动态交互描述

微机监测与MSS交互的数据包括心跳信息、开关量报警信息及模拟量信息。

针对《铁路信号集中监测素查条件》运基信号[2010]709号）要求的其余监测信息，如外电网综合质量监测、列车信号点灯回路电流监测、环境状态模拟量监测等信息，均作为互联互通自定义功能，下文不进行约束。

a)心跳信息

心跳帧用于双方保持通信连接正常。MSS周期性发送心跳帧给微机监测，微机监测同时周期性发送心跳帧给MSS。

b）微机监测开关量报警信息

微机监测周期性MSS发送全体基础信号设备开关量报警信息。

c）微机监测模拟量信息

轨道电压周期性发送，道岔电流在道岔动作完后发送所有电流采集点，绝缘测试在测试完毕后发送测试结果。

d）微机监测系统软件版本号

首次连接、断链重连后或系统软件版本号发生变更后，微机监测向MSS发送监测系统软件版本号。

# 14.1.3通信故障处理

如果MSS方超过额定时间未收到心跳，认为双方连接出现故障，微机监测设备状态为通信中断，并向微机监测发起重连申请；若微机监测超过额定时间未收到心跳，认为双方连接出现故障，此时微机监测方重置通信链路，等待MSS重连。

# 14.2通信层次结构描述

# 14.2.1数据链路层

MAC子层基于IEEE802.3标准。

MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet 帧后面。

# 14.2.2网络层

本接口使用IPv4协议作为网络层的协议。

# 14.2.3传输层

本接口实时传送的信息使川UDP协议作为传输协议。

# 14.2.4应用层

本接口实时传送的信息使用自定义的应用层协议。具体内容参见14.3的规定.

# 14.3接口数据描述

# 14.3.1数据存储方式和通信校验方法

接口数据存储方式采用BigEndian，低地址存放最高有效字节。

通信校验方式采用循环冗余码校验（CRC）。

生成多项式采用CRC32（0x04c11db7），按公式（1）计算，余子式的初始值设为OxFFFFFFFF。

# 14.3.2微机监测 $\longrightarrow$ MSS

14.3.2.1心跳帧

表26规定了微机监测发送给MSS的心跳信息内容。

表26微机监测发送给MSS的心跳信息帧  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>HEADER“</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧开始标志默认值：0xAA</td></tr><tr><td rowspan=1 colspan=1>LEN</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td rowspan=1 colspan=1>STATIOND</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>站报码</td></tr><tr><td rowspan=1 colspan=1>MSGID</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>消息ID默认值：0x10</td></tr><tr><td rowspan=1 colspan=1>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td rowspan=1 colspan=1>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>预留字节</td></tr><tr><td rowspan=1 colspan=1>END</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>帧的结束标识默认值：0x55</td></tr><tr><td rowspan=1 colspan=1>CRC</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CRC校验，校验范围从LEN到END</td></tr></table>

# 14.3.2.2开关量报警信息

开关量信息主要是轨道电压的超限报警。  
表27规定了微机监测发送给MSS的轨道电压报警内容。

表27微机监测发送给MSS的轨道电压报警信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">STATIONID</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">站报码</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x20</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFE后，下一次重新从1开始累加（若数据帧长度大于1024字节，分包的各数据包的序列号保持一致）</td></tr><tr><td colspan="2" rowspan="1">ALARM_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">报警总数</td></tr><tr><td colspan="1" rowspan="5">ALARM(1)</td><td colspan="1" rowspan="1">ALARM_TYPE(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">报警（1）类型0x21：轨道电压超限报警</td></tr><tr><td colspan="1" rowspan="1">ALARM_DEV(1)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">报警设备</td></tr><tr><td colspan="1" rowspan="1">ALARM_STIME(1)</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">报警发生时间，格式同STAMB</td></tr><tr><td colspan="1" rowspan="1">ALARM_NTIME(1)</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">报警恢复时间，格式同STAMP</td></tr><tr><td colspan="1" rowspan="1">ALARM_STATUS(1）</td><td colspan="1" rowspan="1">。1</td><td colspan="1" rowspan="1">报警（1）状态0x00:正常0x55:故障</td></tr><tr><td colspan="1" rowspan="5">ALARM(n)</td><td colspan="1" rowspan="1">ALARM_TYPE(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">报警(n)类型0x21：轨道电压超限报警</td></tr><tr><td colspan="1" rowspan="1">ALARM_DEV(n)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">报警设备</td></tr><tr><td colspan="1" rowspan="1">ALARM_STIME(n)</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">报警发生时间，格式同STAMP</td></tr><tr><td colspan="1" rowspan="1">ALARM_NTIME(n)</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">报警恢复时间，格式同STAMP</td></tr><tr><td colspan="1" rowspan="1">ALARM_STATUS(n)</td><td colspan="1" rowspan="1">1'</td><td colspan="1" rowspan="1">报警(n)状态0x00:正常0x55：故障</td></tr><tr><td colspan="2" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="2" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="2" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从LEN到END</td></tr></table>

# 14.3.2.3模拟量信息

模拟量信息的内容包括：绝缘、道岔电流曲线、轨道电压。其中绝缘、随岔电流曲线，当有数据产生时，监测自主发送数据至MSS。轨道电压置，监测周期性向MSS发送一次所有轨道电压的数据。

在MSG_ID下面定义TYPE_ID，用于区分是哪个类型的数据。

表28规定了微机监测发送给MSS的模拟量内容。

表28微机监测发送给MSS的模拟量类型  

<table><tr><td rowspan=1 colspan=1>TYPE_ID</td><td rowspan=1 colspan=1>定义</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=1>DLJY_INFO</td><td rowspan=1 colspan=1>0×41</td><td rowspan=1 colspan=1>电缆绝缘</td></tr><tr><td rowspan=1 colspan=1>DCDL_INFO</td><td rowspan=1 colspan=1>033</td><td rowspan=1 colspan=1>道岔电流</td></tr><tr><td rowspan=1 colspan=1>GDDY_INFO</td><td rowspan=1 colspan=1>033</td><td rowspan=1 colspan=1>轨道电压</td></tr></table>

由于绝缘、道岔电流曲线数据产生时发送，只能 个数据包发送一个设备的模拟量，所以 安 曾加ITEM NO 务表示设备序号（例如道岔序号）。

对于道岔电流曲线，微机监测需要向MSS传送道岔动作次数，在NTOC(m)增加SW置电曲线的模量，该内容4

对于轨道电压模拟量监测，除电压值以外的信息，均作为自定义字段供厂家使用。

表29规定了微机监测发送的轨道电压模拟量包，格式如下。

表29 微机监测发送给MSS的轨道电压状态信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="1" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td colspan="1" rowspan="1">STATIONID</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">站报码</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x30</td></tr><tr><td colspan="1" rowspan="1">TYPE_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DATA TYPE</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="1" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新从1开始累加</td></tr><tr><td colspan="1" rowspan="1">ANALOG_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模拟量总数</td></tr><tr><td colspan="1" rowspan="1">ANALOG(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模拟量（1）算法是除以10，单位：V</td></tr><tr><td colspan="1" rowspan="1">ANALOG(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">模拟量(n)</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从LEN到END</td></tr></table>

表30规定了微机监测发送的道岔电流模拟量包，格式如下。

表30微机监测发送给MSS的道岔电流信息帧  

<table><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：0xAA</td></tr><tr><td colspan="2" rowspan="1">LEN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td colspan="2" rowspan="1">STATIONID</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">站报码</td></tr><tr><td colspan="2" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID默认值：0x40</td></tr><tr><td colspan="2" rowspan="1">TYPE_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DATA TYPE</td></tr><tr><td colspan="2" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="2" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新从1开始累加</td></tr><tr><td colspan="2" rowspan="1">ITEM_NO</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">设备编号，表示该数据包是第n个设备的内容（对于绝缘、漏流、道岔动作电流需要，其余模拟量可以不使用，按照配置表的顺序即可）</td></tr><tr><td colspan="2" rowspan="1">START_TIME</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td colspan="2" rowspan="1">DIRECTION</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">道岔转换方向0：定位到反位1：反位到定位2：定位到定位3：反位到反位4：定位到故障位5：反位到故障位</td></tr><tr><td colspan="2" rowspan="1">CURVE_TYPR</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">曲线类型0：交流1：直流</td></tr><tr><td colspan="2" rowspan="1">CURVE_NUM</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">曲线数量（如果是直流，则为1。如果是交流，则为3，依次是A、B、C三相）</td></tr><tr><td colspan="1" rowspan="3">CURVE(1)</td><td colspan="1" rowspan="1">POINT_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点数量（采集点的时间间隔：40ms）</td></tr><tr><td colspan="1" rowspan="1">POINT(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点（1）（算法是除以100，单位：A）</td></tr><tr><td colspan="1" rowspan="1">POINT(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点(n）（算法是除以100，单位：A）</td></tr><tr><td colspan="1" rowspan="3">CURVE(n)</td><td colspan="1" rowspan="1">POINT_NUM</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点数量（采集点的时间间隔：40ms）</td></tr><tr><td colspan="1" rowspan="1">POINT(1)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点（1）（算法是除以100，单位：A）</td></tr><tr><td colspan="1" rowspan="1">POINT(n)</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">采集点（n）（算法是除以100，单位：A）</td></tr><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描   述</td></tr><tr><td colspan="1" rowspan="1">SWITCH_CNT</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">道岔动作次数</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">自定义字段</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从LEN到SWITCH_CNT</td></tr><tr><td colspan="1" rowspan="1">ENI)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0×55</td></tr></table>

表31规定了微机监测发送的电缆绝缘模拟量包，格式如下。

表31微机监测发送给MSS的电缆绝缘信息帧  

<table><tr><td colspan="1" rowspan="1">接口内容</td><td colspan="1" rowspan="1">字节长度</td><td colspan="1" rowspan="1">描述</td></tr><tr><td colspan="1" rowspan="1">HEADER</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧开始标志默认值：O△AA</td></tr><tr><td colspan="1" rowspan="1">I.EN</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">帧长度（从STATIONID开始到CRC校验结束）</td></tr><tr><td colspan="1" rowspan="1">STATIONID</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">站报码</td></tr><tr><td colspan="1" rowspan="1">MSG_ID</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">消息ID)，默认值：0x40</td></tr><tr><td colspan="1" rowspan="1">TY PE_ID)</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">DATA TYPE</td></tr><tr><td colspan="1" rowspan="1">STAMP</td><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">年、月、口、时、分、秒各占1个字节(北京时间)</td></tr><tr><td colspan="1" rowspan="1">SN</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下··次重新从1开始累加</td></tr><tr><td colspan="1" rowspan="1">ITEM_NO</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">设备编号，表示该数据包是第n个设备的内容（对于绝缘、漏流、道岔动作电流需要，其余模拟量可以不使用，按照配咒表的顺序即可)</td></tr><tr><td colspan="1" rowspan="1">ANALOG</td><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">电缆绝缘，单位：MΩ，发实际值（算法是除以100）、小于5说明线缆绝缘异常；大于等于20，表示绝缘良好</td></tr><tr><td colspan="1" rowspan="1">Private</td><td colspan="1" rowspan="1">N</td><td colspan="1" rowspan="1">白定义字段</td></tr><tr><td colspan="1" rowspan="1">END</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">帧的结束标识默认值：0x55</td></tr><tr><td colspan="1" rowspan="1">CRC</td><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">CRC校验，校验范围从LEN到END</td></tr></table>

# 14.3.2.4微机监测系统软件版本号

表32规定了微机监测发送的版本内容，格式如下。

表32微机监测发送给MSS的版本信息帧  

<table><tr><td rowspan=1 colspan=3>接口内容</td><td rowspan=1 colspan=1>高茂长度</td><td rowspan=1 colspan=1>描述</td></tr><tr><td rowspan=1 colspan=3>HEADER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>帧开始标志认值：0xAA</td></tr><tr><td rowspan=1 colspan=3>LEN</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>度（从STATIONID开RC校验结束）</td></tr><tr><td rowspan=1 colspan=2>STITIONID</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>报码</td></tr><tr><td rowspan=1 colspan=3>MSG_ID</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>息ID默认值：0x50</td></tr><tr><td rowspan=1 colspan=3>STAMP</td><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>年、月、日、时、分、秒各占1个字节（北京时间）</td></tr><tr><td rowspan=1 colspan=3>SN</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>报文序列号，初始值为1，每次报文依次累加，累计至OxFFFFFFFF后，下一次重新从1开始累加</td></tr><tr><td rowspan=1 colspan=3>VERSION_NUM</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>版本号总数</td></tr><tr><td rowspan=2 colspan=1>DEVICE(1)</td><td rowspan=1 colspan=2>DEVICE_ID(1)</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>设备（1）编号</td></tr><tr><td rowspan=1 colspan=2>DEVICE _VERSION(1)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备（1）版本号</td></tr><tr><td rowspan=2 colspan=1>DEVICE (n)</td><td rowspan=1 colspan=2>DEVICE_ID(n)</td><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>设备(n)编号</td></tr><tr><td rowspan=1 colspan=2>DEVICE _VERSION(n)</td><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>设备（n）版本号</td></tr></table>

中国城市轨道交通协会团体标准

城市轨道交通基于通信的列车运行

控制系统(CBTC）互联互通接口规范

# 第7部分：信号各子系统与维护支持系统(MSS)间接口

T/CAMET 04011.7—2018

\*

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门西街8号）公司网址：http：//www.tdpress.com北铁開有限公司印

开本： $8 8 0 \ \mathrm { \ m m } \times 1 \ 2 3 0 \ \mathrm { \ m m }$ 1/32印张：2.25字数：62下2019年5月第1版2019年5月第1次印刷

书号： $1 5 1 1 3 \cdot 5 7 3 3$ 定价：20.00元

# 版权所有侵权必究