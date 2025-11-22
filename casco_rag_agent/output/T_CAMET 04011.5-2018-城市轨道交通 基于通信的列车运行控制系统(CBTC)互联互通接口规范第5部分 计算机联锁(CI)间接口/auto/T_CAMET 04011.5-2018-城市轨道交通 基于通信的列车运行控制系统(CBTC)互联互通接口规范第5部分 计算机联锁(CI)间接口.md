# 中国城市轨道交通协会团体标准

T/CAMET 04011.5—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范第5部分：计算机联锁（CI）间接口

Urban rail transit— Interface specification for interoperabiity of communication based train control system Part 5: Interface between computer interlockings

# 目 次

前言 VⅢ引言 IX

1范围  
2规范性引用文件 1  
3 术语和缩略语 2  
3.1术语…  
3.2缩略语 3

4 总则 3

5CI-CI通信接口报文规范 3

5.1接口连接方式 3  
5.2 通信体系结构 4  
5.3接口数据描述 5  
5.4 应用信息定义… 10

# 前 言

T/CAMET04011《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

第1部分：应答器报文；  
第2部分：CBTC系统车地连续通信协议；  
第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口；  
第4部分：区域控制器（ZC）间接口；  
第5部分：计算机联锁（CI）间接口；  
第6部分：列车自动监控系统（ATS）间接口；  
第7部分：信号各子系统与维护支持系统（MSS）间接口；  
第8部分：车载人机界面。

本部分是T/CAMET04011的第5部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本规范由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

本部分主要起草人：编写组：宿秀元、张利峰、邱锡宏、陈鹤、高国栋、冯浩楠、段宏伟、张大涛、原志彬、刘清华、胡顺定、王悉。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

# 引 言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

# 城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第5部分：计算机联锁（CI）间接口

# 1范围

T/CAMET04011的本部分规定了计算机联锁系统（CI）不同线路间接口，包括通信方式、拓扑内容。 ME

本适用于国 基于通信的列车运控制系统（CBTC）的新成市轨道交通线路建设，用指导信号系统的系统设计、产品设计、设备招标 仙

# 2规范性引用文件

下列文件对于本部分的用薪置变少。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T24339.1—-2009 轨道交通 通信、信号和处理系统 第1部分：封闭式传输系统中的安全相关通信（IEC62280-1：2002，IDT）

TB/T3027—2015 铁路车站计算机联锁技术条件

CJ/T407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET04010.1 城市轨道交通 基于通信的列车运控制系统（CBTC）互联互通系统规范第1部分：系统总体要求

运基信号[2010]267号 RSSP-I铁路信号安全通信协议

IEEE 802.3 以太网（Ethernet)

RFC 791互联网协议（Internet Protocol）RFC768用户数据报协议（UserDatagram Protocol）

# 3术语和缩略语

CJ/T407—2012和T/CAMET04010.1界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1术语

3.1.1

基于通信的列车控制communication based train control（CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车一地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T407——2012，定义3.1.1]

# 3.1.2

计算机联锁computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T407——2012，定义3.1.6]

# 3.1.3

装备列车CBTC-equipped trains

装备了CBTC系统车载设备且设备处于工作状态的列车。[T/CAMET 04010.1,术语 3.1.11]

# 3.1.4

非装备列车Non-CBTC-equipped trains

没有装备CBTC系统车载设备或者CBTC系统车载设备处于不工作状态的列车。

[T/CAMET 04010.1,术语 3.1.12]

# 3.1.5

# 常态点灯信号机inital-lighted signal

无接近信息室外信号机点灯，有接近信息室外信号机根据接近属性显示的信号机。

# 3.2缩略语

ARB：始终占用的分区即非正常占用分区（AlwaysReportingBlock）  
CBTC：基于通信的列车控制（CommunicationBased Train Control）  
CI：计算机联锁（Computer Interlocking）  
GAL：通用应用层（General Application Layer）  
IPv4：互联网协议（InternetProtocol,IP）的第4版  
MAC:媒体访问控制（Medium AccessControl）  
RSSP：铁路信号安全协议（Railway Signal Safety Protocol）  
TSR;临时限速（Temporary Speed Restriction）  
UDP:用户数据报协议（UserDatagramProtocol）

# 4 总则

本规范重点对互联互通不同线路间计算机联锁系统的通信接口进行了描述，最终系统功能、系统设备的工程配置、用户界面及操作方式、与外部系统接口要求、轨旁设备布置原则等本规范未规定的内容应在后续规范或工程实施中完成。

本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对CI间通信接口数据交互内容进行扩展。

# 5CI-CI通信接口报文规范

# 5.1 接口连接方式

# 5.1.1 物理接口

CI和相邻CI采用双路冗余的通信通道（将双网分别定义为A网和B网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。两系统按照A网和A网相连、B网和B网相连接的方式，

其连接方式见图1。

![](images/09194fc5f0ef59ea815f3b248f502aeab53fe7367bc2d566e7f449adada55ab7.jpg)  
图1 CI-CI双网冗余连接图

# 5.2 通信体系结构

# 5.2.1 通信模型

图2中安全功能模块和通信功能模块属于各子系统内部功能实现，分别用于实现安全功能和对外通信功能。

![](images/6f5e245a34a59911c1086c08282916918b6fa89d0c625880c800ea3335aa7db1.jpg)  
图2 CI-CI通信协议模型

# 5.2.2 通信机制

CI间通信机制如下：

a）CI间通信采用周期发送的方式进行通信；  
b）通信双方均采用大端字节序进行数据传输。

# 5.2.3 通信层次结构

CI间通信层次结构划分如图3所示。

a) 物理层：采用IEEE802.3标准协议。  
b) 数据链路层：MAC子层基于IEEE802.3标准。MAC头由14个字节组成，1个帧校验序列（4字节）将被加在Ethernet帧后面。  
c ) 网络层： $\mathrm { { I P v 4 } }$   
d) 传输层：UDP协议。  
e) 安全通信协议层：遵循GB/T24339.1—2009标准、TB/T3027—2015标准要求，采用RSSP-I铁路信号安全通信协议，同时通过序列号对冗余网络数据进行过滤，不作为本文档描述。

f）应用层：包括通用应用层和CI应用层。

注：CI-CI接口单帧报文长度可突破RSSP-I协议传输的最大信息长度限制。

![](images/09dddda83654156ec0f324c59b3d9e6dca1904f369759c5ad6cbbece0c738c50.jpg)  
图3 CI间通信层次结构

# 5.3 接口数据描述

# 5.3.1 动态交互描述

CI与邻站CI传输分界线两边的设备信息，包括进路内物理区段、逻辑区段、信号机、站台门、紧急关闭按钮、道岔及保护区段状态。双方CI

向对方传输互联互通相关范围内的本联锁管辖范围的设备状态，接收对方CI发送的设备状态。

# 5.3.1.1通用应用层消息包定义

按照《RSSP-I铁路信号安全通信协议》，将相邻CI间每个周期需要交互的信息通过组成通用（GAL)信息包进行传输，如图4所示。

![](images/398c5c03eecaff570be97593091dc807990a8b7c0b0016291a6647124209bfc2.jpg)  
图4通用信息包和应用层信息包关系结构图

# 5.3.1.2信息包格式定义

CI间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL消息包中包含CI间传输的各条应用信息，每个GAL消息包总长不得超过1000字节，格式定义见表1、表2。

表1通用信息包格式定义  

<table><tr><td colspan="1" rowspan="1">信息域定义</td><td colspan="1" rowspan="1">字节编号</td><td colspan="1" rowspan="1">字段</td><td colspan="1" rowspan="1">长度</td><td colspan="1" rowspan="1">信息位定义及说明</td></tr><tr><td colspan="1" rowspan="2">接口信息类型</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型高位</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">0x0606:CI-CI接口</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">类型低位</td></tr><tr><td colspan="1" rowspan="4">发送方标识信息</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="4">源ID</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">发送方联锁ID"</td></tr><tr><td colspan="1" rowspan="1">4</td></tr><tr><td colspan="1" rowspan="1">5</td></tr><tr><td colspan="1" rowspan="1">6</td></tr><tr><td colspan="1" rowspan="4">接收方标识信息</td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="4">日的ID</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">接收方联锁1D"</td></tr><tr><td colspan="1" rowspan="1">8</td></tr><tr><td colspan="1" rowspan="1">9</td></tr><tr><td colspan="1" rowspan="1">10</td></tr><tr><td colspan="1" rowspan="4">电子地图版本校验信息"</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="4">CI与CI之间的版本一致性信息</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">CI-CI重登区范围内，CI与CI问的数据版本校验信息</td></tr><tr><td colspan="1" rowspan="1">12</td></tr><tr><td colspan="1" rowspan="1">13</td></tr><tr><td colspan="1" rowspan="1">14</td></tr><tr><td colspan="1" rowspan="4">本方消息序列号"</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录发送本条消息时，本方的周期计数</td></tr><tr><td colspan="1" rowspan="1">16</td></tr><tr><td colspan="1" rowspan="1">17</td></tr><tr><td colspan="1" rowspan="1">18</td></tr><tr><td colspan="1" rowspan="2">通信周期</td><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="2">通信周期</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">单位：ms</td></tr><tr><td colspan="1" rowspan="1">20</td></tr><tr><td colspan="1" rowspan="4">对方消息序列号</td><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录收到对方上一条消息巾的对方消息序列号"</td></tr><tr><td colspan="1" rowspan="1">22</td></tr><tr><td colspan="1" rowspan="1">23</td></tr><tr><td colspan="1" rowspan="1">24</td></tr><tr><td colspan="1" rowspan="4">收到上一条消息时本方序列号"</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录收到对方上一条消息时，本方的周期计数"</td></tr><tr><td colspan="1" rowspan="1">26</td></tr><tr><td colspan="1" rowspan="1">27</td></tr><tr><td colspan="1" rowspan="1">28</td></tr><tr><td colspan="1" rowspan="1">协议版本号</td><td colspan="1" rowspan="1">29</td><td colspan="1" rowspan="1">协议版本号</td><td colspan="1" rowspan="1">1字节</td><td colspan="1" rowspan="1">CI-CI的协议版本，001～255有效</td></tr><tr><td colspan="1" rowspan="2">应用层报文总长度</td><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="2">应用报文总长度</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">后续报文长度，以字节为单位，不含长度本身两字节</td></tr><tr><td colspan="1" rowspan="1">31</td></tr><tr><td colspan="1" rowspan="1">应用层数据</td><td colspan="1" rowspan="1">32-1000</td><td colspan="1" rowspan="1">应用层数据</td><td colspan="1" rowspan="1">变长</td><td colspan="1" rowspan="1">参见表3格式定义</td></tr><tr><td colspan="5" rowspan="1">ID的具体编号原则在工程实现阶段确定。电子地图版本校验信息针对CI-CI重叠区电子地图两个CI共用的信息。若“电子地图版本校验信息”或“协议版本号”与相邻CI不一致，则进行丢包或断开通信处理。序列号有效值为1~(231-1)。发送方应保证生成两包信息包时，两包信息包中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔。当未收到对方消息时，序列号发送OxFFFFFFFF。</td></tr></table>

表2应用层信息格式定义  

<table><tr><td rowspan=1 colspan=1>信息域定义</td><td rowspan=1 colspan=1>字节编号</td><td rowspan=1 colspan=1>报文内容</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=2 colspan=1>报文长度</td><td rowspan=1 colspan=1>1</td><td rowspan=2 colspan=1>报文长度</td><td rowspan=2 colspan=1>由“报文类型~报文结束”的帧长度</td></tr><tr><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=2 colspan=1>报文类型</td><td rowspan=1 colspan=1>3</td><td rowspan=2 colspan=1>定义某一条应用信息的标识</td><td rowspan=2 colspan=1>自定义，详细内容参见5.3.2</td></tr><tr><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=2 colspan=1>预留</td><td rowspan=1 colspan=1>5</td><td rowspan=2 colspan=1>预留</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>报文内容</td><td rowspan=1 colspan=1>7~报</td><td rowspan=1 colspan=1>按照报文格式定义的报文结束文具体内容</td><td rowspan=1 colspan=1>自定义，详细内容参见5.3.2</td></tr></table>

# 5.3.1.3通信状态管理

5.3.1.3.1CI应对接收到的应用消息进行合法性检查，若检查未通过，认为木周期未收到邻站CI的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

a) 消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查以及信息完整性检查；  
b) 通用应用（GAL）信息包消息所应包含的信息的完整性；  
c) 其他逻辑检查。

5.3.1.3.2CI应能对通信连接状态进行判断：

a) CI判断与邻站CI通 的超时时间定义为 $T _ { \mathrm { ( ; i T i m e 0 ) } \parallel }$ （叮配置，推荐值5s)  
b) 通信建立后 $\mathcal { \tilde { T } } _ { \mathrm { c i T i m e 0 u l } }$ 有接收到来白邻站CI的任何消息 中断（指应用层根据GAL包头 段进行判断，而非安全通信协议层进行的判断）。 $T _ { \mathrm { c i T i m e 3 0 u l } }$ 时，根据GAI包头中字段进行判断，而非安  
d) CI与邻站CI间通信中断的情况下，本站CI无法收到邻站汇报的设备信息。CI应将邻站所有设备状态设置为安全侧，如将通往邻站进路的始端信号机置为禁止信号，对应来白邻站的区段设置为占用。  
e) CI与邻站CI间通信中断的情况下，若本站CI收到了合法的邻站CI信息，则本站CI应认为与邻站CI连接恢复。  
f) 互联互通线网中，CI与邻站CI的通信超时时问应一致，消息有效期时间应一致。

# 5.3.2数据类型定义

表3规定了CI间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）的内容。

表3CI-CI通信的应用层信息定义  

<table><tr><td rowspan=1 colspan=1>信息类型</td><td rowspan=1 colspan=1>信息包名</td><td rowspan=1 colspan=1>发送方向</td><td rowspan=1 colspan=1>长度（字节）</td><td rowspan=1 colspan=1>发送方式</td></tr><tr><td rowspan=1 colspan=1>0x0201</td><td rowspan=1 colspan=1>道岔状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0202</td><td rowspan=1 colspan=1>物理区段状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0203</td><td rowspan=1 colspan=1>逻辑区段状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0204</td><td rowspan=1 colspan=1>信号机状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0205</td><td rowspan=1 colspan=1>站台门状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0206</td><td rowspan=1 colspan=1>紧急关闭按钮状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0207</td><td rowspan=1 colspan=1>照查状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0208</td><td rowspan=1 colspan=1>防淹门信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x0209</td><td rowspan=1 colspan=1>上电锁闭状态信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x020a</td><td rowspan=1 colspan=1>临时限速信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x020b</td><td rowspan=1 colspan=1>城市自定义信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr><tr><td rowspan=1 colspan=1>0x020c</td><td rowspan=1 colspan=1>厂商自定义信息包</td><td rowspan=1 colspan=1>双向</td><td rowspan=1 colspan=1>xx</td><td rowspan=1 colspan=1>周期</td></tr></table>

# 5.4 应用信息定义

# 5.4.1道岔状态信息

本CI应将互联互通相关范围内的本联锁管辖范围的道岔状态发送给邻站 $\mathrm { C I }$ 。相邻CI间道岔索引顺序应保持一致。道岔状态信息见表4。

表4道岔状态信息  

<table><tr><td colspan="1" rowspan="1">字段长度</td><td colspan="1" rowspan="1">字段长度</td><td colspan="8" rowspan="1">说明</td></tr><tr><td colspan="1" rowspan="1">包含的道岔数量</td><td colspan="1" rowspan="1">1字节</td><td colspan="8"></td></tr><tr><td colspan="1" rowspan="1">字段长度</td><td colspan="1" rowspan="1">字段长度</td><td colspan="8" rowspan="1">说   明</td></tr><tr><td colspan="1" rowspan="2">道岔状态</td><td colspan="1" rowspan="2">n字节</td><td colspan="1" rowspan="1">B7</td><td colspan="1" rowspan="1">B6</td><td colspan="1" rowspan="1">B5</td><td colspan="1" rowspan="1">B4</td><td colspan="1" rowspan="1">B3</td><td colspan="1" rowspan="1">B2</td><td colspan="1" rowspan="1">B1</td><td colspan="1" rowspan="1">B0</td></tr><tr><td colspan="2" rowspan="1">道岔1封锁状态：01b:木封锁10b:封锁00b:非法11b:默认值</td><td colspan="2" rowspan="1">道岔1单锁总锁闭状态：状态：01b:未单锁10b:单锁00b:非法11b:默认值</td><td colspan="2" rowspan="1">道岔1引导道岔1单锁总锁闭状态：01b:未引导总锁10b:引导总锁00h：非法11b:默认值</td><td colspan="2" rowspan="1">道贫1位置：01b:定位10b:反位00b:四开11b:默认值</td></tr><tr><td colspan="10" rowspan="1">a非法定义，正常通信过程中不应发送的设备状态，若出现非法设备状态，接收方认为本周期没有收到应用数据包，适用于本协议所有字段。默认值定义，通信双方在具休工程项日中不使用的信息码字或联锁系统在初始化完成之前发送的状态，适用于本协议所有字段。</td></tr></table>

# 5.4.2物理区段状态信息

本CI应将互联互通相关范围内的本联锁区管辖范围内的物理区段状态发送给邻站CI。相邻CI间物理区段索引顺序应保持一致。物理区段状态信息见表5。

表5物理区段状态信息  

<table><tr><td colspan="1" rowspan="1">字段长度</td><td colspan="1" rowspan="1">字段长度</td><td colspan="8" rowspan="1">说</td></tr><tr><td colspan="1" rowspan="1">包含的物理区段数量</td><td colspan="1" rowspan="1">1字节</td><td colspan="8"></td></tr><tr><td colspan="1" rowspan="1">字段</td><td colspan="1" rowspan="1">长度</td><td colspan="8" rowspan="1">说   明</td></tr><tr><td colspan="1" rowspan="3">物理区段状态</td><td colspan="1" rowspan="2">2×n字节物理区段1的Bytel</td><td colspan="1" rowspan="1">B7</td><td colspan="1" rowspan="1">B6</td><td colspan="1" rowspan="1">B5</td><td colspan="1" rowspan="1">B4</td><td colspan="1" rowspan="1">B3</td><td colspan="1" rowspan="1">B2</td><td colspan="1" rowspan="1">B1</td><td colspan="1" rowspan="1">B0</td></tr><tr><td colspan="2" rowspan="1">区段1故障锁闭状态"：01b:区段未故障锁闭；10b:区段故障锁闭；00b：非法状态；11b:默认值</td><td colspan="2" rowspan="1">区段1保护锁闭状态：01b:区段未保护锁闭；10b:区段保护锁闭；00b：非法状态；11b:默认值</td><td colspan="2" rowspan="1">区段1进路锁闭状态：01b：区段未进路锁闭；10b:区段进路锁闭；00b：非法状态；11b:默认值</td><td colspan="2" rowspan="1">区段1占用状态"：00b：区段占用；01b：非法状态；10b：区段空闲；11b：默认值</td></tr><tr><td colspan="1" rowspan="1">物理区段1的Byte2</td><td colspan="2" rowspan="1">预留</td><td colspan="2" rowspan="1">区段1锁闭方向：01b：上行运营方向；10b：下行运营方向；00b：无锁闭方向；11b:默认值</td><td colspan="2" rowspan="1">区段1封锁状态：01b：区段封锁；10b：区段未封锁；00b：非法状态；11b:默认值</td><td colspan="2" rowspan="1">区段1ARB状态：01b：区段ARB;10b：区段未ARB；00b：非法状态；11b:默认值</td></tr><tr><td colspan="10" rowspan="1">采集轨道继电器状态。1.不同厂家转换时，物理区段中任意一个逻辑区段锁闭，则认为物理区段锁闭；2.故障锁闭显示级别优先于进路锁闭，进路锁闭优先于保护区段锁闭；3.进路锁闭包括列车进路、引导进路、调车进路锁闭。区段进路锁闭状态的一种，不满足解锁原则漏解锁时。协议要求同一计轴内所有锁闭的逻辑区段方向应一致。</td></tr></table>

# 5.4.3 逻辑区段状态信息

本CI应将互联互通相关范围内的本联锁区管辖范围的逻辑区段状态发送给邻站CI。相邻CI间逻辑区段索引顺序应保持一致。逻辑区段状态信息见表6。

表6逻辑区段状态信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说明</td></tr><tr><td rowspan=1 colspan=1>包含的逻辑区段数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>互联互通相关范围内的本联锁区管辖范围内逻辑区段数量n</td></tr><tr><td rowspan=3 colspan=1>逻辑X段状态“</td><td rowspan=2 colspan=1>2xn字节逻辑区段1的Bytel</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=2>区段1锁闭方向：01b：上行运营方向；10b：下行运营方向；00b:无锁方向；11b;</td><td rowspan=1 colspan=2>区段1保护锁闭状态：01h：区段未保护锁闭；10b.区段保状态；11b:默认值</td><td rowspan=1 colspan=2>区段1进路锁闭状态”：01b:区段未进路锁闭；10b:区段进路锁闭；00b：法状认值</td><td rowspan=1 colspan=2>区段1占用状态：00b:非CBTC车占用；01b:CBTC车占用；10b:区段空闲；1Ib:默认值</td></tr><tr><td rowspan=1 colspan=1>逻辑区段1的Byte2</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>故障锁段未;区段故00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>区段1封锁状态：01b：区段封锁；10h：区段未封锁；00b：非法状态；11b:默认值</td></tr><tr><td rowspan=1 colspan=10>物理区段利逻辑区段中占用、锁闭等状态信息均应同时发送，主要基于到以下几点：a)CBTC和后备模式下，CI对于列车占用状态获取方式包含物理区段、逻辑区段占川：b）互联互通的接口文件中需要兼容各家产品特点，不同厂家的产品内部逻辑或以物理区段的锁闭、占用状态为主，或以逻辑区段的占用、锁闭状态为主：c)为解决相邻联锁集中区站场状态显示不一致问题，应同时发送物理区段和逻辑区段；d)将处理后的逻辑区段占用状态发送给对方，发送方保证发送的状态应与本方人机界而显示状态一致，接收方可直接用于人机界面显示相邻线路复视区域内逻辑区段状态；e）进路销闭包括列车进路引导进路调车进路销团</td></tr></table>

# 5.4.4 信号机状态信息

本CI应将互联互通相关范围内的本联锁区管辖范围内的信号机状态发送给邻站CI。联锁分界点处信号机属于接车方联锁管辖，若联锁分界点有外置保护区段，则发车方联锁也应向接车方联锁发送该信号机状态信息。若联锁分界点无外置保护区段，则发车方联锁不发该信号机状态信息。相邻CI间信号机索引顺序应保持一致。信号机状态信息见表7。

表7 信号机状态信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说明</td></tr><tr><td rowspan=1 colspan=1>包含的信号机数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>互联互通相关范围内的本联锁区管辖范围的信号机数量n</td></tr><tr><td rowspan=4 colspan=1>信号机状态“</td><td rowspan=2 colspan=1>3xn字节信号机1的Bytel</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=8>信号机1显示状态：00000000b:断丝;00010001b：红灯；00010010b：黄灯;00010100b：绿灯；00011000b:红黄灯;11111111b：默认值；其他：非法</td></tr><tr><td rowspan=1 colspan=1>信号机1的Byte2</td><td rowspan=1 colspan=2>信号机1保护区段命令°：01b:保护建立请求；10b:保护取消请求；00b:无命令；11b:默认值</td><td rowspan=1 colspan=2>信号机1接近锁闭：01b：接近锁闭；10b：未接近锁闭；00b:非法状态；11b:默认值</td><td rowspan=1 colspan=2>信号机1封锁状态：01b:封锁；10b:未封锁；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>信号机1亮灭状态：01b:点灯；10b:灭灯；00b：非法状态；11b:默认值</td></tr><tr><td rowspan=1 colspan=1>信号机1的Byte3</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>信号机1保护区段有效标志：01b：保护区段有效；</td></tr></table>

表7信号机状态信息(续）  

<table><tr><td>字段</td><td>长度</td><td colspan="3">说明</td></tr><tr><td>信号 机状 态</td><td>信号机 1的 Byte3</td><td>预留 分界处的信号机，发车站联锁向接车站联锁仅发送保护区段命令，其他状态</td><td>预留</td><td>预留</td><td>10b：保护区 段无效； 00b：非法状 态； 11h:默认值</td></tr><tr><td colspan="6">发送默认值；接车站联锁向发车站联锁仅发送的保护区段命令为“无命令”， 其他信息发送有效值。 信号机的有效状态包括：亮红、亮黄、亮绿、亮红黄、灭红、灭绿、灭黄。 a）灭绿、灭黄定义：CBTC模式进路信号开放； b）亮绿、亮黄定义：后备模式进路信号开放； c）亮红黄定义：引导信号开放； d）断丝定义：亮灯时灯丝继电器落下； e)针对常态点灯的信号机：在联锁控区边界处，接车站信号机开放作为发车 站信号开放检查条件的场景下（无论实体或者虚拟）：接车站信号机亮绿、 亮黄满足发车站信号开放（灭灯开放或者点灯开放）对此条件的检查。 1．发车站联锁向接车站办理的终端在分界点处的进路完整锁闭且其保护区 段建立的触发区段占用条件都具备时开始发送保护区段建立请求，直到保</td></tr><tr><td colspan="6">护区段已锁闭： 2.发车站联锁收到保护区段停稳信息时，或发车站连接分界点处的区段解锁 时发送“保护取消请求”，直到保护区段已解锁； 3．其他情况发送无命令； 4.主进路与对应保护区段属于不同CI时，保护区段所届CI收到主进路所属CI</td></tr><tr><td colspan="4">发送的“保护取消请求”时，可不考虑主进路CI内线路情况，无条件采信。 “发送方CI应保证：发送“保护区段有效”状态时，“逻辑区段状态信息”包中，</td><td colspan="2"></td></tr><tr><td colspan="4">该保护区段内所有逻辑区段的“保护锁闭状态”字段取值均为“区段保护锁 闭”。主进路CI判断保护区段是否可用时，除“保护区段有效标志”字段外， 可不对保护区段CI范围内的其他条件进行判断。若主进路CI进行了其他判 断，则由主进路CI保证系统的可用性。</td><td colspan="2"></td></tr></table>

# 5.4.5 站台门状态信息

本CI将互联互通相关范围内的本联锁区管辖范围的站台门状态信息发送给邻站CI。相邻CI间站台门索引顺序应保持一致。站台门状态信息见表8。

表8 站台门状态信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说  明</td></tr><tr><td rowspan=1 colspan=1>包含的信息单元数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>互联互通相关范围内的本联锁区管辖范围内站台门数量n</td></tr><tr><td rowspan=2 colspan=1>信息单元状态</td><td rowspan=2 colspan=1>0.5×n字节（进位取整）</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=4>站台门2状态</td><td rowspan=1 colspan=2>站台门1旁路标志：01b:未旁路；10b:旁路；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>站台门1开关状态：01b：开门；10b:关门且锁闭；00b：非法状态；11b:默认值</td></tr></table>

# 5.4.6 站台紧急关闭按钮信息

本CI将互联互通相关范围内的本联锁区管辖范围的站台紧急关闭信息发送给邻站 $\mathrm { C I }$ 。相邻CI间站台紧急关闭索引顺序应保持一致。站台紧急关闭按钮信息见表9。

表9 站台紧急关闭按钮信息  

<table><tr><td colspan="1" rowspan="1">字段长度</td><td colspan="1" rowspan="1">字段长度</td><td colspan="8" rowspan="1">说明</td></tr><tr><td colspan="1" rowspan="1">包含的元数量</td><td colspan="1" rowspan="1"></td><td colspan="8"></td></tr><tr><td colspan="1" rowspan="1">字段长度</td><td colspan="1" rowspan="1">字段长度</td><td colspan="8" rowspan="1">说   明</td></tr><tr><td colspan="1" rowspan="2">信息单元状态</td><td colspan="1" rowspan="2">0.25 ×n字节（进位取整）</td><td colspan="1" rowspan="1">B7</td><td colspan="1" rowspan="1">B6</td><td colspan="1" rowspan="1">R5</td><td colspan="1" rowspan="1">B4</td><td colspan="1" rowspan="1">B3</td><td colspan="1" rowspan="1">B2</td><td colspan="1" rowspan="1">B1</td><td colspan="1" rowspan="1">B0</td></tr><tr><td colspan="2" rowspan="1">紧急关闭4状态</td><td colspan="2" rowspan="1">紧急关闭3状态</td><td colspan="2" rowspan="1">紧急关闭2状态</td><td colspan="2" rowspan="1">紧急关闭按钮1状态：01b:按下；10b:术按下；00b:非法状态；11b:默认值</td></tr></table>

CIATION

# 5.4.7照查状态信息

表10。 本口将互政由内的木職鎖的服世状志信自

表10 照查状态信息  

<table><tr><td rowspan=1 colspan=1>字段长度</td><td rowspan=1 colspan=1>字段长度</td><td rowspan=1 colspan=8>城市          说</td></tr><tr><td rowspan=1 colspan=1>包含的信息单元数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>城市 轨道互联互通相关范围内的本联锁区管辖范围的照查数量n</td></tr><tr><td rowspan=2 colspan=1>信息单元状态</td><td rowspan=2 colspan=1>0.25 ×n字节（进位取整）</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>BO</td></tr><tr><td rowspan=1 colspan=2>照查4状态</td><td rowspan=1 colspan=2>照查3状态</td><td rowspan=1 colspan=2>照查2状态</td><td rowspan=1 colspan=2>照查1状态&quot;：01b:照查落下；10b:照查吸起；00b:非法状态；11b:默认值</td></tr><tr><td rowspan=1 colspan=10>“照查条件在具体工程中做详细定义。例如：照查条件常态吸起，在发车站末区段锁闭时落下，上电锁闭时照查状态为落下。</td></tr></table>

# 5.4.8 防淹门信息

本CI将互联互通相关范围内的本联锁区管辖范围的防淹门信息发送给邻站CI。相邻CI间防淹门索引顺序应保持一致。防淹门信息见表11。

表11 防淹门信息  

<table><tr><td rowspan=1 colspan=1>字段长度</td><td rowspan=1 colspan=1>字段长度</td><td rowspan=1 colspan=8>说  明</td></tr><tr><td rowspan=1 colspan=1>包含的信息单元数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>互联互通相关范围内的本联锁区管辖范围的防淹门数量n</td></tr><tr><td rowspan=2 colspan=1>信息单元状态</td><td rowspan=2 colspan=1>n字节</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>防淹门1关门允许：01b:允许；10b：不允许；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>防淹门1关门请求：01b：请求；10b:未请求；00b:非法状态；11b:默认值</td><td rowspan=1 colspan=2>防淹门1状态：01b:关闭；10b：开放；00b：非法状态；11b:默认值</td></tr></table>

# 5.4.9上电锁闭状态信息

本CI将本站上电锁闭状态信息发送给邻站CI。上电锁闭状态信息见表12。

表12上电锁闭状态信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>包含的信息单元数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=1>本CI上电锁闭状态数量n</td></tr><tr><td rowspan=1 colspan=1>信息单元状态</td><td rowspan=1 colspan=1>n字节</td><td rowspan=1 colspan=1>上电锁闭状态：0x55：设置上电锁闭；Oxaa：未设置上电锁闭；0xff:默认值；其他：非法码字</td></tr></table>

# 5.4.10临时限速信息

本CI应将互联互通相关范围内的本联锁管辖范围的临时限速区段状态发送给邻站CI。相邻CI间临时限速区段索引顺序应保持一致。临时限速信息见表13。

表13临时限速信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说   明</td></tr><tr><td rowspan=1 colspan=1>包含的临时限速区段数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>互联互通相关范围内的本联锁区管辖范围的临时限速区段数量n</td></tr><tr><td rowspan=2 colspan=1>临时限速区段状态</td><td rowspan=2 colspan=1>0.25 ×n字节（进位取整）</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=2>临时限速区段4TSR状态：01b:区段设置TSR；10b:区段禾设置TSR；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>临时限速区段3TSR状态：01b:区段设置TSR；10b：区段未设置TSR；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>临时限速区段2TSR状态：01b：区段设置TSR；10b：区段未设置TSR；00b：非法状态；11b:默认值</td><td rowspan=1 colspan=2>临时限速区段ITSR状态：01b：区段设置TSR；10b:区段未设置TSR；00b:非法状态；11b:默认值</td></tr></table>

# 5.4.11城市自定义信息

本CI将互联互通相关范围内的本联锁管辖范围的城市自定义信息发送给邻站CI，见表14。

表14城市自定义信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>明</td></tr><tr><td rowspan=1 colspan=1>城市自定义</td><td rowspan=1 colspan=1>n字节</td><td rowspan=1 colspan=1>报文内容为城市自定义</td></tr></table>

# 5.4.12厂商自定义信息

本CI将互联互通相关范围内的本联锁管辖范围的厂商自定义信息

发送给邻站CI，见表15。

表15厂商自定义信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>厂商自定义</td><td rowspan=1 colspan=1>n字节</td><td rowspan=1 colspan=1>报文内容为厂商自定义</td></tr></table>

中国城市轨道交通协会团体标准  
城市轨道交通基于通信的列车运行  
控制系统（CBTC）互联互通接口规范  
第5部分：计算机联锁（CI）间接口  
T/CAMET04011.5—2018  
\*  
中国铁道出版社有限公司出版发行  
（100054，北京市西城区右安门西街8号）  
公司网址：http：//www.tdpress.com  
北京铭成印刷有限公司印刷  
开本： $8 8 0 \ m m \times 1 \ 2 3 0 \ \ m m$ 1/32印张：1字数：24千  
2019年5月第1版2019年5月第1次印刷  
书号： $1 5 1 1 3 \cdot 5 7 3 0$ 定价：15.00元  
版权所有侵权必究  
凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。  
发行部电话：路（021）73174，市（010）51873174