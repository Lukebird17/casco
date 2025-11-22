# 中国城市轨道交通协会团体标准

T/CAMET 04011.4—2018

# 城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第4部分：区域控制器（ZC）间接口

Urban rail transit—Interface specification for interoperability of communication based train control system Part 4: Interface between zone controllers

# 目 次

前言 VI  
引言   
1范围  
2规范性引用文件  
3术语和缩略语3.1术语…3.2缩略语 3  
4总则 4  
5ZC-ZC通信接口报文规范 45.1接口连接方式5.2通信体系结构 45.3接口数据描述 65.4应用信息定义· 10  
附录A（规范性附录）列车控制权切换正常流程示例及列车移交相关原则 29

# 前 言

T/CAMET04011《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

-第1部分：应答器报文；  
第2部分：CBTC系统车地连续通信协议；  
第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口；  
第4部分：区域控制器（ZC）间接口；  
第5部分：计算机联锁（CI）间接口；  
第6部分：列车自动监控系统（ATS）间接口；  
第7部分：信号各子系统与维护支持系统（MSS）间接口；  
第8部分：车载人机界面。

本部分是T/CAMET04011的第4部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

主要起草人：编写组：耿鹏、聂宇威、骆正新、杨旭文、张春雨、刘剑、姜庆阳、吕浩炯、陈昕、陆晓红、胡顺定、刘宏杰、刘键。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

# 引 言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通T程规范》4个规范（17个部分）。

# 城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范第4部分：区域控制器（ZC）间接口

# 1范围

T/CAMET04011的本部分定 域控制器（ZC）间接口，规定了相关的系统架构、功能、 最终系统功能、系统设备口要求、轨旁设备布置原则等。

本部分适用于国内来用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通乡 洛建设， 用饭 指导信号系统的系统设计、产品设计、设备招标、工程建设。

# 2规范性引用文件

# 轨道

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB50157—2013地铁设计规范

CJ/T407—2012城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET04010.1城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范第1部分：系统总体要求

运基信号[2010]267号RSSP-I铁路信号安全通信协议

IEEE 802.3以太网(Ethernet)

RFC 791互联网协议(Internet Protocol)

# RFC768用广数据报协议（User Datagram Protocol）

# 3术语和缩略语

GB50157—2013和CJ/T407—2012界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1术语

3.1.1

基于通信的列车控制communication based train control （CBTC）

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车一地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车白动控制系统。

[CJ/T407—2012,定义3.1.1]

# 3.1.2

正线 main line 载客列车运营的贯穿全程的线路。 [GB50157—2013，定义2.0.11]

# 3.1.3

列车自动监控automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB50157—2013，定义2.0.38]

3.1.4

列车自动防护automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB50157—2013，定义2.0.39]

# 3.1.5

计算机联锁computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T407—2012,定义3.1.6]

3.1.6

危险点danger point列车运行前方不允许列车任何部位越过的特定点。

3.1.7

移动授权movement authority   
列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。 [CJ/T407—2012，定义3.1.7]

# 3.1.8

# 跨线运行overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进人另外一条线路进行共线运行的方式。

[T/CAMET 04010.1,术语3.1.14]

# 3.2缩略语

AM:列车自动驾驶模式（Automatic Train Operating Mode）  
AR：白动折返（Automatic Reversal Operation)  
ATP:列车自动防护（AutomaticTrain Protection）  
ATS:列车自动监控（Automatic Train Supervision）  
CBTC:基于通信的列车控制（Communication Based Train Control）  
CI:计算机联锁（Computer Interlocking)  
CM:列车自动防护模式(Coded Train Operating Mode)  
EUM:非限制人工驾驶模式（Emergency Unrestricted Train Operating Mode)  
GAL:通用应用层（General Application Layer）  
$\mathrm { { I P v 4 } }$ :互联网协议（InternetProtocol,IP）的第4版  
MA：移动授权（Movement Authority）  
PSD:站台门(Platform Screen Door)  
RM:限制人丁驾驶模式（Restricted Train Operating Mode）  
TSR: 临时限速（Temporary Speed Restriction)  
UDP:用户数据报协议（User Datagram Protocol）

ZC:区域控制器（Zone Controller）

# 4 总则

4.1本规范重点针对互联互通中关键的跨线区域控制器间的通信接口，本规范未规定的内容应在后续规范或工程实施中完成。

4.2满足城市轨道交通互联互通要求的CBTC系统应遵守本规范。

4.3本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对ZC间通信接口数据交互内容进行扩展。

# 5 ZC-ZC通信接口报文规范

# 5.1 接口连接方式

# 5.1.1 物理接口

ZC应冗余接人信号安全数据网，网络拓扑结构采用A网-A网、B网-B网两个链路。

# 5.2 通信体系结构

# 5.2.1 通信模型

图1中安全功能模块和通信功能模块应由各厂家ZC子系统内部功能实现，分别用于实现安全功能和对外通信功能。

![](images/ce2f3fc8780299799bfbee37afd1c03e888eacb5dbd267637c4e7a7096761ff8.jpg)  
图1 ZC-ZC通信协议模型

# 5.2.2通信机制

ZC间通信机制如下：

a）ZC间通信应采用周期发送的方式进行通信；  
b）通信双方均采用大端字节序进行数据传输。

# 5.2.3通信层次结构

ZC间通信层次结构划分如图2所示。

![](images/b65336c67bdff26ca4e1eb4d9a2cce1604686c4729a378a9f1214182cac42ff5.jpg)  
图2ZC间通信层次结构

图2中使用的通信协议如下：

a) 物理层：采用IEEE802.3标准协议；  
b) 网络层： $\mathrm { { I P v 4 } }$ ;  
c ) 传输层：UDP协议；  
d) 安全通信协议层：采用RSSP－I铁路信号安全通信协议；  
e) 应用层：参见5.3.1详细定义。

注：ZC-ZC接口单帧报文长度可突破RSSP－Ⅰ协议传输的最大信息长度限制。

# 5.3接口数据描述

# 5.3.1动态交互描述

# 5.3.1.1通信应用层消息包定义

按照《RSSP-I铁路信号安全通信协议》，将相邻ZC间每个周期需要交互的信息通过组成通用（GAL）信息包进行传输，如图3所示。

![](images/5f494774868098a77185e3ea5131c720fd20ee33bf15c636dbe5d98db5236f9f.jpg)  
图3通用信息包和应用层信息包关系结构图

# 5.3.1.2信息包格式定义

ZC间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL包中包含ZC问传输的各条应用信息。GAL包格式定义见表1。

表1通用信息包格式定义  

<table><tr><td colspan="1" rowspan="1">信息域定义</td><td colspan="1" rowspan="1">字节编号</td><td colspan="1" rowspan="1">字段</td><td colspan="1" rowspan="1">长度</td><td colspan="1" rowspan="1">信息位定义及说明</td></tr><tr><td colspan="1" rowspan="2">接口信息类型</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">类型高位</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">0x0101:ZC-ZC接口</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">类型低位</td></tr><tr><td colspan="1" rowspan="3">发送方标识信息</td><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="3">源ID</td><td colspan="1" rowspan="3">4字节</td><td colspan="1" rowspan="3">发送方ZCID</td></tr><tr><td colspan="1" rowspan="1">45</td></tr><tr><td colspan="1" rowspan="1">6</td></tr><tr><td colspan="1" rowspan="4">接收方标识信息</td><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="4">日的ID</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">接收方ZCID</td></tr><tr><td colspan="1" rowspan="1">8</td></tr><tr><td colspan="1" rowspan="1">9</td></tr><tr><td colspan="1" rowspan="1">10</td></tr><tr><td colspan="1" rowspan="4">数据版本校验信息</td><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="4">线路数据版木</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">ZC重叠区内数据版本信息</td></tr><tr><td colspan="1" rowspan="1">12</td></tr><tr><td colspan="1" rowspan="1">13</td></tr><tr><td colspan="1" rowspan="1">14</td></tr><tr><td colspan="1" rowspan="4">本方消息序列号“</td><td colspan="1" rowspan="1">15</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录发送木条消息时，本方的周期计数</td></tr><tr><td colspan="1" rowspan="1">16</td></tr><tr><td colspan="1" rowspan="1">17</td></tr><tr><td colspan="1" rowspan="1">18</td></tr><tr><td colspan="1" rowspan="2">通信周期</td><td colspan="1" rowspan="1">19</td><td colspan="1" rowspan="2">通信周期</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">设备通信周期，单位：ms</td></tr><tr><td colspan="1" rowspan="1">20</td></tr><tr><td colspan="1" rowspan="4">对方消息序列号"</td><td colspan="1" rowspan="1">21</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录收到对方上一条消息中的对方消息序列号。默认值：OxFFFFFFFFb</td></tr><tr><td colspan="1" rowspan="1">22</td></tr><tr><td colspan="1" rowspan="1">23</td></tr><tr><td colspan="1" rowspan="1">24</td></tr><tr><td colspan="1" rowspan="4">收到上一条消息时本方序列号"</td><td colspan="1" rowspan="1">25</td><td colspan="1" rowspan="4">序列号</td><td colspan="1" rowspan="4">4字节</td><td colspan="1" rowspan="4">记录收到对方上一条消息时，本方的周期计数。默认值：0xFFFFFFFFb</td></tr><tr><td colspan="1" rowspan="1">26</td></tr><tr><td colspan="1" rowspan="1">27</td></tr><tr><td colspan="1" rowspan="1">28</td></tr><tr><td colspan="1" rowspan="1">协议版本号"</td><td colspan="1" rowspan="1">29</td><td colspan="1" rowspan="1">协议版本号</td><td colspan="1" rowspan="1">1字节</td><td colspan="1" rowspan="1">ZC-ZC的协议版本</td></tr><tr><td colspan="1" rowspan="2">应用层信息长度</td><td colspan="1" rowspan="1">30</td><td colspan="1" rowspan="2">应用层信息长度</td><td colspan="1" rowspan="2">2字节</td><td colspan="1" rowspan="2">从应用层数据开始到应用层数据结束的总字节数，不含报文头长度</td></tr><tr><td colspan="1" rowspan="1">31</td></tr><tr><td colspan="1" rowspan="1">应用层数据</td><td colspan="1" rowspan="1">32~结束</td><td colspan="1" rowspan="1">应用层数据</td><td colspan="1" rowspan="1">变长</td><td colspan="1" rowspan="1">参见表2格式定义</td></tr></table>

# 表1通用信息包格式定义（续）

"1．序列号有效值为 $1 \sim ( 2 ^ { 3 ! } - 1 )$ 。发送方必须保证生成两包信息包时，两包信息报中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔。

2.当ZC判断“数据版本校验信息”或“协议版本号”字段校验不通过时，应进行丢包或断开安全连接处理。

「当未收到对方消息时，填写默认值。

表2应用层信息格式定义  

<table><tr><td rowspan=1 colspan=1>信息域定义</td><td rowspan=1 colspan=1>字节编号</td><td rowspan=1 colspan=1>报文内容</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=2 colspan=1>报文长度</td><td rowspan=1 colspan=1>1</td><td rowspan=2 colspan=1>报文长度（报文类型~报文结束）</td><td rowspan=2 colspan=1>自定义，详细内容参见5.3.2</td></tr><tr><td rowspan=1 colspan=1>2</td></tr><tr><td rowspan=2 colspan=1>报文类型</td><td rowspan=1 colspan=1>3</td><td rowspan=2 colspan=1>定义某一条应用信息的标识</td><td rowspan=2 colspan=1>自定义，详细内容参见5.3.2</td></tr><tr><td rowspan=1 colspan=1>4</td></tr><tr><td rowspan=2 colspan=1>预留</td><td rowspan=1 colspan=1>5</td><td rowspan=2 colspan=1>预留</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>0</td></tr><tr><td rowspan=1 colspan=1>报文内容</td><td rowspan=1 colspan=1>7~报文结束</td><td rowspan=1 colspan=1>按照报文格式定义的报文具体内容</td><td rowspan=1 colspan=1>自定义，详细内容参见5.4</td></tr></table>

# 5.3.1.3通信状态管理

ZC间通信状态管理如下：

a）ZC应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站ZC的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

1）消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。若消息中存在字段的“非法”取值，应对本GAL包信息中所有进行丢弃处理。

2）通用应用(GAL)信息包消息所应包含的信息的完整性。

3）其他逻辑检查。

b）ZC应能对通信连接状态进行判断（指应用层根据GAL包头中字段进行判断，而非安全通信协议层进行的判断）：

1）ZC认为与邻站ZC通信中断的超时时间定义为 $T _ { \mathrm { { z c r i m e o u l } } }$ ( $\mathrm { ~ I ~ . ~ } 5 \mathrm { ~ s ~ } \sim 6 \mathrm { ~ s ~ }$ ，可配置，典型值：4.5s）；  
2) 在通信建立后，若ZC在 $T _ { \mathrm { z c T i m e o u l } }$ 超时时间内没有接收到来自邻站ZC的任何消息，则ZC应认为与邻站ZC通信中断；  
3) 若ZC判断接收到邻站ZC的GAL包延迟已经达到(cid:) $T _ { \mathrm { z c r i m e s u t } }$ 时，ZC 应丢弃此GAL包，或认为与邻站 ZC 通

# 5.3.2数据类型定

表3规定了ZC间通信的所有应用信息类型度其含义、发送方向、长度范围、发送方式（周期/非周势）轨渣。 交

表3ZC-ZC通信的应用层信息定义  

<table><tr><td colspan="1" rowspan="1">信息类型</td><td colspan="1" rowspan="1">信息包名</td><td colspan="1" rowspan="1">发送方向</td><td colspan="1" rowspan="1">长度（字节）</td><td colspan="1" rowspan="1">发送方式</td></tr><tr><td colspan="1" rowspan="1">0x0204</td><td colspan="1" rowspan="1">道岔状态信息包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">XX</td><td colspan="1" rowspan="1">周期</td></tr><tr><td colspan="1" rowspan="1">0x0208</td><td colspan="1" rowspan="1">物理区段状态信息包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">xx</td><td colspan="1" rowspan="1">周期</td></tr><tr><td colspan="1" rowspan="1">0x020A</td><td colspan="1" rowspan="1">移交状态信息包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">Xx</td><td colspan="1" rowspan="1">周期</td></tr><tr><td colspan="1" rowspan="1">0x020B</td><td colspan="1" rowspan="1">移交列车信息包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">xx</td><td colspan="1" rowspan="1">周期</td></tr><tr><td colspan="1" rowspan="1">0x020C</td><td colspan="1" rowspan="1">城市自定义包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">xx</td><td colspan="1" rowspan="1">非周期</td></tr><tr><td colspan="1" rowspan="1">0x020D</td><td colspan="1" rowspan="1">厂商自定义包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">XX</td><td colspan="1" rowspan="1">非周期</td></tr><tr><td colspan="1" rowspan="1">0x020E</td><td colspan="1" rowspan="1">站场信息延时包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">XX</td><td colspan="1" rowspan="1">周期</td></tr><tr><td colspan="1" rowspan="1">0x020F</td><td colspan="1" rowspan="1">轨道区段列车排序信息包</td><td colspan="1" rowspan="1">双向</td><td colspan="1" rowspan="1">XX</td><td colspan="1" rowspan="1">周期</td></tr></table>

# 5.4应用信息定义

# 5.4.1说明

本节中的“非法”值：正常通信时发送方不应发送的非法取值。接收方收到GAL包中的应用信息帧中存在“非法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认为本周期未收到数据。

本节中的“默认”值：（1）针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；（2）设备在初始化完成前，无法确定状态时，相关字段取值发送“默认值”。接收方收到“默认”值后，应认为信息有效，不进行处理。

本节中的设备索引值均从1开始。

本节巾涉及“上行”、“下行”的方向定义，均采用运营方向规定的上下行。跨线时，两条线路上下行运营方向定义不一致时，发送上下行方向信息的原则确定为：发送方ZC按照自身所属线路上下行定义进行发送，由接收方ZC适配处理。

本节中的“预留”字段，发送方统一填0，接收方可不对预留字段进行校验。

本节中的轨道区段内的偏移量，基准点均为车载电子地图中，该轨道区段沿车载电子地图上行方向的起点。

# 5.4.2道岔状态信息

本ZC应将配置重叠区内所有道岔状态发送给邻站ZC。相邻ZC间道岔索引顺序应保持一致。该信息包格式见表4。

表4道岔状态信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>包含的道岔数量</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=1>配置重叠区本ZC管辖范围内道岔数量n（最多128个）安全信息</td></tr></table>

表4道岔状态信息（续）  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说   明</td></tr><tr><td rowspan=2 colspan=1>道岔状态&quot;</td><td rowspan=2 colspan=1>n/4字节（向上取整）</td><td rowspan=1 colspan=1>B7d</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>B1</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=2>道岔4状态</td><td rowspan=1 colspan=2>道岔3状态</td><td rowspan=1 colspan=2>道岔2状态</td><td rowspan=1 colspan=2>道岔Ⅰ状态：01b:定位；10h：反位；00b:四开；11b:默认值（填充信息或无法提供该信息，应填写“默认值”)安全信息</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>++-</td></tr><tr><td rowspan=1 colspan=10>“对于双动道贫、ZC应按照2个单独道岔向和邻ZC发送。ZC收到相邻ZC发送的“道岔状态”字段取值为默认值时，应对道岔状态进行安全侧处理。</td></tr></table>

# 5.4.3物理区段状态信息

本ZC将配置重叠I区内本管辖区物理区段信息发送给邻站ZC。相邻ZC需对物理区段进行排序，并且同一物理区段在发送方的排序位置与接收方的排序位置相同。该信息包格式见表5。

表5物理区段状态信息  

<table><tr><td rowspan=1 colspan=2>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说明</td></tr><tr><td rowspan=1 colspan=2>包含的信息单元数最</td><td rowspan=1 colspan=1>1字节</td><td rowspan=1 colspan=8>配置重叠区本ZC管辖范围内物理区段数量n（最多60个）。安全信息</td></tr><tr><td rowspan=2 colspan=1>物理区段1信息</td><td rowspan=2 colspan=1>物理区段1状态</td><td rowspan=2 colspan=1>1字节</td><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>BI</td><td rowspan=1 colspan=1>BO</td></tr><tr><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>预留</td><td rowspan=1 colspan=2>物理区段1占用状态：01b:空闲；10b：占用；其他：非法。安全信息</td></tr></table>

表5物理区段状态信息（续）  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>物理区段2信息</td><td rowspan=1 colspan=1>同上</td><td rowspan=1 colspan=1>同上</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>物理区段n信息</td><td rowspan=1 colspan=1>同上</td><td rowspan=1 colspan=1>同</td></tr></table>

# 5.4.4移交状态信息

移交状态信息包用于ZC切换的管理，信息包含移交与接管ZC交互的各自边界点移交状态信息。该信息包格式见表6。

表6移交状态信息  

<table><tr><td colspan="1" rowspan="1">字段</td><td colspan="1" rowspan="1">长度</td><td colspan="1" rowspan="1">说明</td></tr><tr><td colspan="1" rowspan="1">包含的信息单元数量</td><td colspan="1" rowspan="1">1字节</td><td colspan="1" rowspan="1">与交互ZC的移交边界数n，按照实际边界数填写。有效范同：1~20。安全信息</td></tr><tr><td colspan="1" rowspan="4">信息单元状态</td><td colspan="1" rowspan="4">变长字节</td><td colspan="1" rowspan="1">边界点ID(4字节）：ZC移交边界ID。一个物理边界点应使H一个唯一ID，即使在此边界点可进行双方向移交。安全信息</td></tr><tr><td colspan="1" rowspan="1">接近列车ID（4字节）”：非通信车默认ID：OxFFFFFFFE；默认值：0x00000000安全信息</td></tr><tr><td colspan="1" rowspan="1">接近列车距离，单位：cm（4字节）：有效范围：OxO~OxFFFFFFFE"：默认值：OxFFFFFFFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">接近列乍运行等级（1字节）：0x01:CBTC;0x02：点式；</td></tr><tr><td colspan="1" rowspan="6">信息单元状态</td><td colspan="1" rowspan="6">变长字节</td><td colspan="1" rowspan="1">0x03：联锁级；OxFF:默认值；其他：非法。安全信息</td></tr><tr><td colspan="1" rowspan="1">接近列车车载ATP当前模式（1字节）"：0x01:AM模式；0x02:CM模式；0x03:RM模式：0x04:EU0xFI</td></tr><tr><td colspan="1" rowspan="1">正请求（  子节）AA;停                                需求确定，如无此功能则默认填写安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证请求序列号（4字节）：有效范围：1~(231-1）：默认值：OxFFFFFFFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">移交列车VID（4字节）：默认值：0x00000000。无列车移交时填写默认值。安全信息</td></tr><tr><td colspan="1" rowspan="1">列车移交接管状态（1字节）：0x00：移交接管未触发（列车未处于移交/接管状态）；0x11：列车移交（移交ZC向接管ZC发送，当前列车已处于移交状态）；</td></tr></table>

表6移交状态信息（续）  

<table><tr><td>字段</td><td>长度</td><td colspan="3">说明</td></tr><tr><td rowspan="8">信息单元 状态</td><td rowspan="8">变长</td><td rowspan="8"></td><td colspan="3">0x22：列车接管（接管ZC向移交ZC发送，当前列车已处于 接管状态，接管ZC计算的MA可越过移交边界）； 0xFF：禁止驶人（接管ZC向移交ZC发送，指示不允许MA 进入接管ZC管辖范围）； 其他：非法。</td></tr><tr><td colspan="3">安全信息 MA是否有效（1字节）： 本车有在本ZC管辖范用内的MA：0x55；</td></tr><tr><td colspan="3">本车无在本ZC管辖范围内的MA：0xAA； 其他：非法。 安全信息 MA方向（1字节）： MA起点朝向MA终点的方向，以MA起点处的</td></tr><tr><td rowspan="3">字节 列车在 本ZC管 辖范围内 的MA信 息（变长）</td><td colspan="2">上下行方向确定。 上行：0x55； 下行：0xAA； 其他：非法。 安全信息</td></tr><tr><td>MA起点 位置（8字 节） 安全信息</td><td>区段ID：4字节 默认值：0x00000000 区段内偏移量(4字节）：单位：em 有效范围：OxO~OxFFFFFFFE</td></tr><tr><td rowspan="2">安全防护</td><td colspan="2">默认值：O×FFFFFFFF 区段ID：4字节 默认值：0x00000000</td></tr><tr><td rowspan="2">点位置（8字 节）</td><td colspan="2">区段内偏移量（4字节）：单位：cm 有效范用：OxO~OxFFFFFFFE 默认值：OxFFFFFFFF</td></tr><tr><td colspan="2">安全信息</td></tr></table>

√

表6移交状态信息（续）  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=5>说明</td></tr><tr><td rowspan=12 colspan=1>信息单元状态</td><td rowspan=12 colspan=1>变长字节</td><td rowspan=12 colspan=1>列车在本ZC管辖范围内的MA信息（变长）</td><td rowspan=2 colspan=3>障碍点信息(8字节)安全信息</td><td rowspan=1 colspan=1>轨道区段ID：4字节默认值：0x00000000</td></tr><tr><td rowspan=1 colspan=1>区段内偏移量（4宇节）：单位：cm有效范围：0xO~OxFFFFFFFE默认值：0xFFFFFFFF</td></tr><tr><td rowspan=1 colspan=4>保护区段有效性(1字节）：有效：0x55；无效：0xAA；默认值：0xFF；其他：非法。安全信息</td></tr><tr><td rowspan=2 colspan=3>道岔信息</td><td rowspan=1 colspan=1>道岔个数n有效范围：0~20（1字节）</td></tr><tr><td rowspan=1 colspan=1>息</td><td rowspan=1 colspan=1>道岔(1)ID:4字节</td></tr><tr><td rowspan=4 colspan=3>（变长）：MA（含保护区段）覆盖范用内所有道岔的信息安全信息</td><td rowspan=1 colspan=1>道岔（1）状态：1字节定位：0x55；反位：0xAA；其他：非法</td></tr><tr><td rowspan=1 colspan=1>道岔(2)ID：4字节</td></tr><tr><td rowspan=1 colspan=1>道岔(2)状态：1字节</td></tr><tr><td rowspan=1 colspan=1>……·</td></tr><tr><td rowspan=2 colspan=3>PSD信息（变长）：MA覆盖范围内</td><td rowspan=1 colspan=1>PSD个数n有效范围：0~10（1字节）</td></tr><tr><td rowspan=1 colspan=2>围内</td><td rowspan=1 colspan=1>PSD(1)ID:4字节</td></tr><tr><td rowspan=1 colspan=3>所有PSD的信息安全信息</td><td rowspan=1 colspan=1>PSD(I)状态:1字节开门：0x55；关门：0xAA；</td></tr></table>

表6移交状态信息（续）  

<table><tr><td rowspan=1 colspan=1>宇段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=3>说明</td></tr><tr><td rowspan=14 colspan=1>信息单元状态</td><td rowspan=14 colspan=1>变长字节</td><td rowspan=14 colspan=1>列车在本ZC管辖范围内的MA信息（变长）</td><td rowspan=4 colspan=1>PSD信息（变长）：MA覆盖范围内所有PSD的信息安全信息</td><td rowspan=1 colspan=1>互锁解除：0xCC；其他：非法。若ZC无互锁解除功能，则互锁解除认为“关门”</td></tr><tr><td rowspan=1 colspan=1>PSD(2)ID:4字节</td></tr><tr><td rowspan=1 colspan=1>PSD(2）状态：1字节</td></tr><tr><td rowspan=1 colspan=1>……</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>ESB个数n有效范围：0~10（1字节）</td></tr><tr><td rowspan=1 colspan=1>ESB信息</td><td rowspan=1 colspan=1>ESB(1)ID:4字节</td></tr><tr><td rowspan=4 colspan=1>（变长）：MA薇盖范围内所有ESB的信息安全信息</td><td rowspan=1 colspan=1>ESB(1)状态：1字节按下：0x55；未按下：0xAA；其他：非法</td></tr><tr><td rowspan=1 colspan=1>ESB（2）ID:（4字节）</td></tr><tr><td rowspan=1 colspan=1>ESB（2）状态：（1字节）</td></tr><tr><td rowspan=1 colspan=1>---</td></tr><tr><td rowspan=1 colspan=1>无人折返按钮状态（1字节）非安全信息</td><td rowspan=1 colspan=1>无人折返按钮状态（列车停靠无人折返站台时方可发送按下）：（1字节）按下：0x55；未按下：OxAA（默认值）</td></tr><tr><td rowspan=3 colspan=1>临时限速信息（变长）：MA覆盖范围内所有临时限速的信息安全信息</td><td rowspan=1 colspan=1>临时限速信息个数n：有效范周：0~10（1字节）</td></tr><tr><td rowspan=1 colspan=1>始端轨道区段IID（4字节）</td></tr><tr><td rowspan=1 colspan=1>始端轨道区段内偏移量：单位：cm有效范围：0x0~0xFFFFFFFE（4字节）</td></tr></table>

表6移交状态信息（续）  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=4>说明</td></tr><tr><td rowspan=7 colspan=1>信息单元状态</td><td rowspan=7 colspan=1>变长学节</td><td rowspan=7 colspan=1>列车在本ZO销</td><td rowspan=6 colspan=1>临时限速信息（变长）：MA覆盖范围内所有临时限速</td><td rowspan=4 colspan=1>临时限速(1）信息</td><td rowspan=1 colspan=1>终端轨道区段ID（4字节）</td></tr><tr><td rowspan=1 colspan=1>终端轨道区段内偏移量：单位：m有效范围：OxO~OxFFFFFFFE(4字节）</td></tr><tr><td rowspan=1 colspan=1>预留（1字节）</td></tr><tr><td rowspan=1 colspan=1>临时限速值（1字节）：单位：km/h有效范围：0~254xFF：无临时限速</td></tr><tr><td rowspan=1 colspan=2></td></tr><tr><td rowspan=1 colspan=2>限速（n）信息</td></tr><tr><td rowspan=1 colspan=1>地属</td><td rowspan=1 colspan=2>MA经目的地属性：AA;0xCC;默认值：OxFF若ZC无相关功能，则发送默认值。若ATP无和关功能，则接收此信息时不进行处理。非安全信息</td></tr><tr><td rowspan=1 colspan=6>注：对于移交ZC，当移交列车最大安全前端在ZC重登区移交ZC的管转区内，且MA达到边界点时开始针对该边界点发送列车移交状态，并在移交列车最小安全后端离开移交ZC的管辖范围（越过ZC边界）后停止发送该列车的移交状态。对于接管ZC，当正在移交的列车最大安全前端或者最小安全后端在相邻ZC重叠区，接管ZC针对该边界点发送的“移交状态信息”包中的“移交列车VID”应包含该列车。如果接管ZC为该车计算的MA可进人接管ZC，则接管ZC发送该边界点允许该移交列车驶人；否则，接管ZC发送该边界点不允许该移交列车驶人。当接管ZC向移交ZC发送禁止驶人时，移交ZC应限制列车MA越过边界点。</td></tr></table>

# 表6移交状态信息（续）

移交ZC应限制向列车发送的MA信息在接管ZC向移交ZC发送的移动授权范围之内。

具体移交流程如下：

） 移交ZC未收到接管ZC发送的允许越过移交边界的MA（“列车移交接管状态”字段取值为“列车接管”，且“MA是否有效”字段取值为“本车有在本ZC管辖范围内的MA”）前，应不允许MA越过移交边界。  
b) 移交ZC根据接管ZC发送的站场信息按照自身逻辑判断MA是否到达移交边界。  
c) 移交ZC判断MA到达移交边界后，向接管ZC发起请求（“列车移交接管状态”字段填写“列车移交”），并向接管ZC发送该车在自身管辖范围内的MA信息（终点为边界点，不能有安全余量）。

d）接管ZC计算移交列车在自身管辖范围内的MA：

1)若接管ZC判断MA可进入自身管辖范围，则应向移交ZC发送该车在自身管辖范围内的MA信息（“列车移交接管状态”字段取值为“列车接管”，且“MA是否有效”字段取值为“本车有在本ZC管辖范围内的MA”，MA起点从边界点开始），且将自身管辖范围内的MA与移交ZC发送的MA信息拼接，并向VOBC发送。接管ZC应保证向移交ZC发送的自身管辖范围内的MA供移交ZC拼接后，不超出MA内设备最大数量的限制。

2）若接管ZC判断MA无法进入自身管辖范围，则向移交ZC发送禁止进人的移交状态（“列车移交接管状态”字段取值为“禁止驶入”，且“MA是否有效”字段取值为“本车无在本ZC管辖范围内的MA”），并向VOBC发送特殊控制命令。

1）若移交ZC未收到接管ZC发送的可进人接管ZC管辖范围的MA信息，则移交ZC应向VOBC发送自身管辖范围内的MA。

2)若移交ZC收到接管ZC发送的可进人接管ZC管辖范围的MA信息，则移交ZC应将自身管辖范围内的MA与接管ZC发送的MA信息拼接，并向VOBC发送。移交ZC拼接接管ZC发送的MA时，若判断拼接后MA内设备最大数量已突破限制，则不采信接管ZC发送的MA，将MA终点置为移交边界，并重新启动上述移交流程。

正常移交的流程示例参见附录A。

$^ { \circ } 1$ 本注释中，近端指列车靠近边界点的端，远端指列车远离边界点的端。

2.以边界点为单位，移交ZC与接管ZC交互指定范围内距离边界点最近的列车ID及距离。指定范围应满足：

# 表6移交状态信息（续）

1）不小于具体工程约定的信号机接近距离；2)以物理区段边界点为边界。  
3.ZC查找列车从边界点开始，沿远离边界点的方向顺序查找，遇道岔区段时，若道岔非四开，则按照道岔开向查找，若道岔四开，则可停止继续查找（该四开道岔属于查找范围）或沿道岔可能开向继续查找。  
4.若通信列车安全包络跨压分界点，则该通信列车视为最接近该边界点的列车。  
5.若接近列车为通信车，则“接近列车ID”字段填写该通信车ID，“接近列车运行等级”、“接近列车车载ATP当前模式”字段填写该通信车VOBC发送的“列车运行控制级别”、“列车驾驶模式”信息。1)若列车安全包络未跨压边界点，则“接近列车距离”字段填写该通信车列车安全包络的近端到边界点的距离；2)若列车安全包络跨压边界点，则“接近列车距离”字段填写0。  
6.若接近列车为非通信车，则“接近列车ID”字段填写非通信车默认ID，“接近列车运行等级”、“接近列车车载ATP当前模式”字段填写默认值，“接近列车距离”字段填写该非通信车可能占用的距离边界点最近的物理区段的近端距边界点的距离，该物理区段占用状态应为“占用”状态或有列车安全包络占用。  
7.若查找范围内无列车，则“接近列车ID”、“接近列车运行等级”、“接近列车车载ATP当前模式”、“接近列车距离”字段均填写默认值。  
8.对于移交ZC发送的“移交状态信息”包，若该边界点有移交列车（“移交列车VID”字段取值不为默认值），则“移交列车VID”字段取值应与“接近列车ID”字段取值一致。  
$^ { \mathrm { i } } 1$ .ZC每次生成停车保证请求时，应更新停车保证请求序列号，无停车保证请求时，停车保证请求序列号应为默认值。2.发送方ZC应保证：若MA有效，则停车保证请求对应位置应为MA终点位置；若MA无效，则停车保证请求对应点为边界点。3.移交ZC应保证：接管ZC发送停车保证请求时可直接采用移交ZC发送的“移交列车VID”作为停车保证请求对应的列车。4.停车保证的发起ZC应保证自身可区分不同的停车保证命令及响应。5.VOBC采信的MA中包含停车保证请求时，应向移交/接管ZC发送有效（能停下/不能停下）的停车保证响应（即使不使用该ZC的MA），该停车保证响应的位置应与所采信的MA中的停车保证请求中的位置一致。6.移交ZC收到VOBC发送的停车保证响应后，向接管ZC转发。7.接管ZC向移交ZC发送停车保证请求时，若对应停车保证请求进路的列车安全包络完全位于接管ZC范围内，则接管ZC应不向移交ZC发送该请求。

“1.当无列车处于移交过程中，或有列车处于移交过程，但发送方ZC判断该列车无在本ZC管辖范围内的MA时，“MA是否有效”字段取值为：OxAA（本车无在本ZC管辖范围内的MA)。

2.若“MA是否有效”字段取值为：0xAA（本车无在本ZC管辖范围内的MA），则后续“列车在本ZC管辖范围内的MA信息”字段应不填写。

3.移交ZC向接管ZC发送的自身管辖范围内的MA信息，安全防护点应为移交边界（无安全余量）；接管ZC向移交ZC发送的自身管辖范围内的MA信息，起点应为移交边界。

4.接管ZC不允许MA进入接管ZC管辖范围时，移交ZC向VOBC发送的MA若到达ZC边界，则应使用移交ZC管辖范围内的轨道区段描述。

5.对于发送方ZC，“列车在本ZC管辖范围内的MA信息”里属于重叠区本ZC管辖范围内的道岔状态应与道岔状态信息包中相应道岔状态一致。

6.对于主进路在移交ZC管辖区内，保护区段在接管ZC管辖区内，保护区段有效，接管ZC判断自身管辖范围内对移交列车来说仅有保护区段可用的场景下，移交流程如下：

1）移交ZC判断MA到达移交边界时，未收到接管ZC发送的可进入接管ZC管辖范围的MA信息之前，向接管ZC发送的“移交状态信息”包中的MA信息中，障碍点为默认值，安全防护点为移交边界点，保护区段有效性为“无效”或“默认值”；向VOBC发送的列车控制信息中，障碍点为默认值，保护区段有效性为“无效”或“默认值”。

2）接管ZC接收到移交ZC发送的移交请求之后，向移交ZC发送的“移交状态信息”包中的MA信息中，障碍点、起点位置均为移交边界点，安全防护点位置应确保列车可正常进站停车，同时应确保安全性，保护区段有效性为“有效”；向VOBC发送的列车控制信息中，障碍点为移交边界点，安全防护点位置与向移交ZC发送的安全防护点位置相同，保护区段有效性为“有效”。

3）移交ZC接受到接管ZC发送的可进人接管ZC管辖范围的MA信息后进行拼接，拼接后发给VOBC的MA障碍点为移交边界点，安全防护点位置为接管ZC发送的安全防护点位置，保护区段有效性为“有效”；发给接管ZC的MA信息中，障碍点为默认值、安全防护点为移交边界，保护区段有效性为“无效”或“默认值”。

# 5.4.5 移交列车信息

移交列车信息包用于列车相关的功能，ZC将所有最大安全前端或最小安全后端位于重叠区本管辖区范围的列车（含非CBTC列车）的信息发送给相邻ZC。该信息包格式见表7。

表7移交列车信息  

<table><tr><td>字段 长度 包含的信 1字节0~30。 息单元数量</td><td>说明 配置重叠区本ZC管辖范围内控制列车数量n，有效范围：</td></tr><tr><td rowspan="7"></td><td>安全信息 移交列车VID(4字节）</td></tr><tr><td>安全信息 列作运行方向（1字节）： 最小安全后端指问最大安全前端的方向，以最小安全后端</td></tr><tr><td>处的上下行定 上行 法。 信息 OBC是否 （首尾 VOBC统·发送是激</td></tr><tr><td>活 n×85 激 55 字节 非激 其他：非法</td></tr><tr><td>安个信息 列车消息序列号（4字节）： ZC实际接收到的车载ATP发送的列车消息序列号。 安全信息</td></tr><tr><td>列车通信周期（2字节） ZC实际接收到的车载ATP发送的列车通信周期 安全信息 列车最人安全前端位置（8字节）&quot;：</td></tr><tr><td>轨道区段ID（4字节）+所在区段偏移（4字节） 偏移量单位：cm，有效范：OxO~OxFFFFFFFE； 安全信息</td></tr></table>

表7移交列车信息（续）  

<table><tr><td colspan="1" rowspan="1">字段</td><td colspan="1" rowspan="1">长度</td><td colspan="1" rowspan="1">说明</td></tr><tr><td colspan="1" rowspan="7">信息单元状态</td><td colspan="1" rowspan="7">n×85字节</td><td colspan="1" rowspan="1">列车最小安全前端位置（8字节）：轨道区段ID（4字节）+所在区段偏移量（4字节）偏移量单位：cm，有效范围：0xO~OxFFFFFFFE；安全信息</td></tr><tr><td colspan="1" rowspan="1">列车最大安全后端位置（8字节）：轨道区段ID（4字节）+所在区段偏移量（4字节）偏移量单位：cm，有效范围：OxO~OxFFFFFFFE；安全信息</td></tr><tr><td colspan="1" rowspan="1">列车最小安全后端位置（8字节）：轨道区段ID（4字节）+所在区段偏移量（4字节）偏移量单位：cm，有效范围：OxO~OxFFFFFFFE；安全信息</td></tr><tr><td colspan="1" rowspan="1">受控ZCID(4字节）：ZC间转发VOBC向ZC发送的“受控ZCID”。安全信息</td></tr><tr><td colspan="1" rowspan="1">本ZC记录的与车载的通信状态（2字节）：ZC判断VOBC与ZC之间通信的延迟时间，单位：ms，有效范围：0~10000;安全信息</td></tr><tr><td colspan="1" rowspan="1">列车停准停稳信息（1字节）：0x55：停准且停稳；OxAA：未停稳；OxCC：停稳但未停准；其他：非法。安全信息</td></tr><tr><td colspan="1" rowspan="1">紧急制动状态（1字节）：无紧急制动：0x55；有紧急制动：0xAA；其他：非法。非安全信息</td></tr><tr><td colspan="2" rowspan="6">信息单元n×85状态         字节</td><td colspan="1" rowspan="1">列车运行等级（1字节）：0x01:CBTC;0x02：点式；0x03：联锁级；其他：非法。安全信息</td></tr><tr><td colspan="1" rowspan="1">车载ATP当前模式（1字节）：0x01:AM模式；0x02:CM模式；0x03:RM模式；0x04：FUM模式；其他：非法。安全信息</td></tr><tr><td colspan="1" rowspan="1">列车折返状态（1字节）：0x55:AR状态；OxAA:非AR状态；其他：非法，非安全信息</td></tr><tr><td colspan="1" rowspan="1">列车完整性（1字节）：完整：0x55；不定整：0xAA；其他：非法。安全信息</td></tr><tr><td colspan="1" rowspan="1">列车长度（2字节）：单位：m，高字节在前，低字节在后，有效范围：1000~50000。安全信息</td></tr><tr><td colspan="1" rowspan="1">列车悬垂长度（2字节）（列车车钩到第一轮对的距离）：单位：cm，高字节在前，低字节任后，有效范围：1~1000，安全信息</td></tr><tr><td colspan="1" rowspan="7">信息单元状态</td><td colspan="1" rowspan="7">n×85字节</td><td colspan="1" rowspan="1">停车保证响应序列号（4字节）：有效范围：1~(231-1)。默认值：OxFFFFFFFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证对应安全防护点轨道区段ID（4字节）：默认值：0x00000000。安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证对应安全防护点轨道区段偏移量（4字节）：单位：cm，有效范围：0xO~OxFFFFFFFE；默认值：OxFFFFFFFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证对应障碍点轨道区段ID（4字节）：默认值：0x00000000。安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证对应障碍点轨道区段偏移量（4字节）：单位：cm，有效范围：OxO~OxFFFFFFFE；默认值：OxFFFFFFFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">停车保证对应保护区段有效性（1字节）：有效：0x55；无效：0xAA;默认值：0xFF。安全信息</td></tr><tr><td colspan="1" rowspan="1">速度方向（1字节）：ZC接收的VOBC发送的速度方向0x55：车轮正转；OxAA：车轮反转；其他：非法。安全信息</td></tr></table>

表7移交列车信息（续）  

<table><tr><td rowspan=1 colspan=1>字   段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=8>说明</td></tr><tr><td rowspan=3 colspan=1>信息单元状态</td><td rowspan=3 colspan=1>n×85字节</td><td rowspan=1 colspan=8>列车速度信息（2宁节）：单位：cm/s，有效范围：0~15000；安全信息</td></tr><tr><td rowspan=1 colspan=1>B7</td><td rowspan=1 colspan=1>B6</td><td rowspan=1 colspan=1>B5</td><td rowspan=1 colspan=1>B4</td><td rowspan=1 colspan=1>B3</td><td rowspan=1 colspan=1>B2</td><td rowspan=1 colspan=1>Bi</td><td rowspan=1 colspan=1>B0</td></tr><tr><td rowspan=1 colspan=2>停车保证：00b：无法停车；01b：可以停车；回停车无车  国城市时默认值）其他（依据业需求确定本宁段、若业主不需要，则本字段为预留字段，填写00b)安全信息</td><td rowspan=1 colspan=2>斗筛状态00b=未11b=已完成；其他·非</td><td rowspan=1 colspan=2>状态&quot;：未完成已完他：非法。安全信息</td><td rowspan=1 colspan=2>（预留）</td></tr><tr><td rowspan=1 colspan=10>&quot;1.ZC间互传的列车位置信息应为VOBC向ZC发送的列车位置（列车位置的描述如图4所示），但若VOBC发送的列车安全包络糍盖ZC重登区边界点，则发送方ZC应对列车位置信息进行处理，使发送的列车位置信息中的列车安全包络完全处于重叠区内：具体处理原则参见附录2。</td></tr></table>

# 表7移交列车信息（续）

2.对于发送方ZC，列车位置信息体现的道岔状态应与轨道区段列车排序信息包中“轨道区段 $\mathbf { x }$ 列车排序信息”体现的相应道岔状态，以及道岔状态信息包中相应道岔状态一致。

${ } ^ { \mathbf { b } } \mathbf { 1 }$ 参考《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范第2部分：CBTC系统车地连续通信协议》中“VOBC-ZC报文规范”中的相关内容。

2.接管ZC收到移交ZC发送的停车保证响应时，应判断停车保证响应序列号与自身发送的停车保证请求信息一致，且停车保证响应对应位置满足：

1)位于移交ZC管辖范围内；

2）位于接管ZC管辖范围内，或与自身发送的停车保证请求信息一致时，方可采信停车保证响应。

“列车头筛是指：ZC判断列车前方是否存在其他隐藏列车。若列车完成头筛，则列车前方无其他隐藏列车。

列车尾筛是指：ZC判断列车后方是否存在其他隐藏列车。若列车完成尾筛，则列车后方无其他隐藏列车。

![](images/04508736f948815496dbc0c425d71cc82a5db02a7738a5632b8fb40e3d3c833b.jpg)  
图4列车安全位置示意图

# 5.4.6 城市自定义包

自定义信息，用于实现各城市特有的互联互通相关功能。该信息包格式见表8，具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。

表8城市自定义包  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>信息定义</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>具体内容在工程中约定</td></tr></table>

# 5.4.7厂商自定义包

自定义信息，用于实现各厂商特有功能。该信息包格式见表9，各厂商分别定制，ZC判断通信ZC与自身属于同一厂商时，方可发送厂商白定义包。

表9厂商自定义包  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>信息定义</td><td rowspan=1 colspan=1>N</td><td rowspan=1 colspan=1>具体内容由各厂商分别定制</td></tr></table>

# 5.4.8站场信息延时包

用于表明本GAL包内站场信息的最大已存在时间，该信息包格式见表10。站场信息的最大已存在时间指来自CI的站场信息在发送方ZC发出该信息前已存在的时间。

涉及站场信息包括：道岔状态信息包、物理区段状态信息包、移交状态信息包中的距边界点最近的列车信息、轨道区段列车排序信息包。

ZC判断相邻ZC发送的GAL包中站场信息是否可用时，应考虑站场信息已存在时间。

表10站场信息延时包  

<table><tr><td rowspan=1 colspan=1>接口内容</td><td rowspan=1 colspan=1>字节长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>站场信息已存在时间安全信息</td><td rowspan=1 colspan=1>2字节</td><td rowspan=1 colspan=1>本GAL包内站场信息的最大已存在时问，单位：ms。有效范围：1~10000；默认值：0xFFFFZC判断与CI通信中断时，填写默认值</td></tr></table>

# 5.4.9轨道区段列车排序信息

本ZC应将配置重叠区内本ZC管辖范围内所有轨道区段I的列车顺序信息发送给邻站ZC，列车排序信息见表11。相邻ZC间轨道区段索引顺序应保持一致。

表11 轨道区段列车排序信息  

<table><tr><td rowspan=1 colspan=1>字段</td><td rowspan=1 colspan=1>长度</td><td rowspan=1 colspan=1>说明</td></tr><tr><td rowspan=1 colspan=1>包含的轨道区段数量</td><td rowspan=1 colspan=1>2字节</td><td rowspan=1 colspan=1>配置重叠区本ZC管辖范围内轨道区段数量n，有效范围：1~256。安全信息</td></tr><tr><td rowspan=4 colspan=1>轨道区段1列车排序信息</td><td rowspan=4 colspan=1>变长</td><td rowspan=1 colspan=1>轨道区段1内列车数量（1字节）：表明此轨道区段列车顺序中的列车数量a，有效范围：0~20。安全信息</td></tr><tr><td rowspan=1 colspan=1>列车（1）ID（4字节）：列车顺序中第一列车的ID，若为通信车，则取值为该车的VID，若为非通信车（含ZC无法判断的隐藏列车），则取值为非通信车默认ID：OxFFFFFFFE。安全信息</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>列车（a)ID(4字节）安全信息</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>……</td></tr><tr><td rowspan=1 colspan=1>轨道区段n列车排序信息</td><td rowspan=1 colspan=1>变长</td><td rowspan=1 colspan=1>同“轨道区段1列车排序信息”定义。安全信息</td></tr></table>

注：轨道区段内列车排序原则为：

a）通信列车排序按照VOBC发送的原始位置报告进行；  
b）若发送方ZC发送的轨道区段上无列车序列，且在“物理区段状态信息”包中，该轨道区段所在物理区段的“物理区段占用状态”取值为“占用”，则发送方ZC应保证该轨道区段上无非通信车；  
c）轨道区段上的列车应按照从边界点向远离边界点的方向排序；  
d）轨道区段内相邻的非通信车可合并为一列非通信车。

# 附录A

（规范性附录）

# 列车控制权切换正常流程示例及列车移交相关原则

# A.1 列车控制权切换正常流程示例

列车控制权切换的正常流程示例如图A.1所示，其中ZC1为移交ZC,ZC2为接管ZC。

![](images/0a7590895dfc903abf5ce034fb70885d0db232a6511c841faafd5fcc3f2035d3.jpg)  
图A.1列车控制权切换流程示例

![](images/843c87f46d692dd947ba51c12955a61b0974a053b061b0f2d6287bd511240c84.jpg)  
图A.1 列车控制权切换流程示例（续）

a)前置条件：

1) 设置ZC1和ZC2管辖边界及重叠区域；

2）各ZC将重叠区域属于各自管辖的物理区段、道岔等站场信息周期互传；  
3） 各ZC将包络处于重叠区域内的列车位置报告等列车信息周期互传；  
4） 各ZC将边界点的移交状态等信息周期互传；  
5） 两个相邻ZC的同一个边界点同时只能由一列车处于控制权切换流程，追踪列车应顺序进行控制权切换。

b）正常移交流程：

步骤1：列车1安全包络未进入ZC1重叠区范围，仅与ZC1建立通信，移交流程未启动。列车1完全受ZC1的控制，使用ZC1发送的MA运行。

步骤2：列车1的最大安全前端进人ZC1重叠区范围，仅与ZC1建立通信，移交流程未启动。

步骤3：列车1的安全包络完全进人ZC1重叠区范围后，列车1注册ZC2，同时与ZC1和ZC2建立通信，此时移动授权终点还未达到移交边界，移交流程未启动。

步骤4：ZC1为列车1计算的移动授权终点到达移交边界，移交流程启动。ZC1向ZC2发送的移交列车信息包含列车1，“移交状态信息”包中的“移交列车VID”为列车1的VID。

步骤5：ZC2收到ZC1的移交状态信息中包含列车1的“列车移交”状态，则ZC2为列车1计算移动授权，若移动授权可延伸进入ZC2管辖范围，ZC2向ZC1发送的“列车移交接管状态”为“列车接管”，ZCI将列车1的移动授权延伸进入ZC2管辖范围，最远不能越过ZC2计算的移动授权终点。

步骤6：列车1向前运行，最大安全前端驶出ZC1管辖范围，ZC1和ZC2互发列车1的移交状态信息和移交列车信息，并均向列车1发送移动授权。列车1根据自身位置判断使用的移动授权。

步骤7：列车1安全包络驶过移交边界，完全驶出ZC1管辖范围后，列车1断开与ZC1的通信。ZC2向ZC1发送的移交列车信息中包含列车1，ZC1和ZC2相互发送的“移交状态信息”包中“移交列车VID”均不包含列车1。至此，列车1完成控制权由ZC1向ZC2的切换。

步骤8：列车2在列车1后方，在列车1完成移交后，列车2执行切换流程，重复步骤 $1 ~ \sim$ 步骤7。ZC2向ZC1发送列车1的移交列车信息，ZC1向列车2发送的移动授权终点应与列车1的车尾保持安全距离。

# A.2 ZC重叠区边界列车安全包络处理方案

# A.2.1 概述

列车移交过程中，ZC需在“移交列车信息”包中向相邻ZC发送列车位置信息。列车位置信息以列车安全包络描述，列车安全包络示意如图A.2所示。

![](images/2eb62d21f568c885155c4cf164f1edd4966dfe6ab369391a4899da0aa9b2c7a3.jpg)  
图A.2 列车安全包络示意图

ZC向相邻ZC发送的“移交列车信息”包中，涉及列车安全包络的信息包括：列车最大安全前端位置、列车最小安全前端位置、列车最大安全后端位置、列车最小安全后端位置、列车长度。

ZC向相邻ZC发送列车的“移交状态信息”包的条件为：ZC判断该列车最大安全前端或最小安全后端在ZC重叠区本ZC管辖范围内。

特殊场景如下：

a）对移交ZC，列车最大安全前端刚进人ZC重叠区本ZC管辖范围，最小安全后端还在ZC重叠区本ZC管辖范围之外；  
b) 对移交ZC，列车最大安全前端已越过移交边界，离开ZC重叠区本ZC管辖范围，最小安全后端还在ZC重叠区本ZC管辖范围之内；  
c) 对接管ZC，列车最大安全前端刚越过移交边界，进入ZC重叠区本ZC管辖范围，最小安全后端还未进人ZC重叠区本ZC管辖范围；  
d) 对接管ZC，列车最大安 端已离开ZC重叠区本ZC管辖范围，最小安全后AO管辖范围之内。

上述特殊场景，均 ZC向相邻ZC发的移交列车信息”包中，列车安全包络不完全/ZC重叠区内本ZC转范围内的情况。

对于场景b) $\mathbf { \nabla } _ { \mathbf { \lambda } ^ { \ast } } \mathrm { c }$ 车 已络完全位于水重登区内（通过重叠区设置原则可保证），日 路地图，故ZC可确定列车安全包络位置 络不完全位于ZC重车安全包络位置。故关信息进行特殊处理，使相邻ZC 的列车安全包络完全处于ZC重叠区内。

# A.2.2 场景名词定义

A.2.1中场景a）、d）以边界点为中心对称，故分析时将两种场景合并为列车安全包络跨ZC重叠区边界的场景统一描述。

场景中基本定义如下，如图A.3所示：

近端、远端：以ZC移交边界为基准，向ZC内部计算，靠近ZC移交边界的列车端为近端，远离ZC移交边界的列车端为远端；

近侧、远侧：以某点为基准，该点靠近ZC移交边界的一侧为该点的近侧，远离ZC移交边界的一侧为该点的远侧。

在此基础上，场景中的名称与具体场景的对应见表A.1。

![](images/09016f6cf80f04c0061ffb69f1904846f3bd97e931025392b865b8b76fca567a.jpg)  
图A.3 场景名词定义

表A.1 场景对照表  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>移交ZC</td><td rowspan=1 colspan=1>接管ZC</td></tr><tr><td rowspan=1 colspan=1>近端近侧包络</td><td rowspan=1 colspan=1>列车最大安全前端</td><td rowspan=1 colspan=1>列车最小安全后端</td></tr><tr><td rowspan=1 colspan=1>近端远侧包络</td><td rowspan=1 colspan=1>列车最小安全前端</td><td rowspan=1 colspan=1>列车最大安全后端</td></tr><tr><td rowspan=1 colspan=1>远端近侧包络</td><td rowspan=1 colspan=1>列车最大安全后端</td><td rowspan=1 colspan=1>列车最小安全前端</td></tr><tr><td rowspan=1 colspan=1>远端远侧包络</td><td rowspan=1 colspan=1>列车最小安全后端</td><td rowspan=1 colspan=1>列车最大安全前端</td></tr><tr><td rowspan=1 colspan=1>列车安全包络：近端近侧包络到远端远侧包络范围</td><td rowspan=1 colspan=1>列车最大安全前端到列车最小安全后端范围</td><td rowspan=1 colspan=1>列车最大安全前端到列车最小安全后端范围</td></tr></table>

真实X（X为表中名称，例如近端近侧包络等）：指ZC收到的VOBC发送的X，或ZC根据VOBC发送的信息计算所得的X；

处理后X：指ZC经过处理，向相邻ZC发送的X，或根据ZC处理后信息计算所得的X。

注：下文中均基于此节定义进行描述。

# A.2.3 处理方案

对“移交列车信息”包中列车安全包络相关信息的处理方案为：

a）ZC判断ZC重叠区边界在真实列车安全包络范围内（含与近端近侧包络、远端远侧包络位置相同的情况）时，向相邻ZC发送“移交列车信息”时，对列车安全包络相关信息进行处理。

b）处理后发送信息见表A.2。

表A.2列车包络相关信息处理对照表  

<table><tr><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>计算结果</td></tr><tr><td rowspan=1 colspan=1>近端近侧包络</td><td rowspan=1 colspan=1>真实近端近侧包络</td></tr><tr><td rowspan=1 colspan=1>近端远侧包络</td><td rowspan=1 colspan=1>真实近端近侧包络</td></tr><tr><td rowspan=1 colspan=1>远端近侧包络</td><td rowspan=1 colspan=1>ZC重叠区边界</td></tr><tr><td rowspan=1 colspan=1>远端远侧包络</td><td rowspan=1 colspan=1>ZC重叠区边界</td></tr></table>

c）发送方ZC不对VOBC发送的“列车长度”字段进行修改。

d) 接收方ZC应采信发送方ZC发送的列车远端远侧包络、远端近侧包络、近端远侧包络、近端近侧包络。  
e) 接收方ZC收到发送方ZC发送的列车远端远侧包络为ZC重叠区边界位置时，不应将“列车长度”字段与列车安全包络相关信息进行校验。  
f) 接收方ZC应允许通过发送方ZC发送的列车位置计算所得的列车测距误差小于真实列车的测距误差，最小值允许为0。

# A.3 重叠区划分原则

为实现装备不同信号厂家车载设备的列车在互联互通线路上的跨线切换，本规范将定义ZC切换重叠区，用于实现线间的ZC切换。

A.3.1 ZC边界

设计人员在设置ZC边界时，应遵循如下原则：

a) ZC边界应设置在计轴点，且与联锁边界相同；  
b) ZC边界不应设置在折返区段中间（不含折返区段边界）；  
c) ZC边界不应设置在站台区段中间（不含站台区段边界）；  
d) ZC边界应设置实体信号机或虚拟信号机；  
e) ZC系统及ZC-ZC通信接口规范（线间）应支持相邻ZC间设置有多个ZC边界。

# A.3.2 ZC切换重叠区

设计人员在定义ZC切换重叠区时，应遵循如下原则：

b) ZC切换重叠区的设置应保证列车通过ZC边界时不减速运行，具体长度应在工程阶段确定。

c） ZC重叠区移交ZC管辖范围应至少包括接管ZC管辖范围内第一条进路的接近区段。

d） 移交重叠区范围应保证最不利情况下，列车不会在ZC超时时间内由移交重叠区外越过移交ZC边界进入接管ZC。

e）重叠区内计轴长度不得小于列车最大回退距离 $^ +$ 外悬的长度。

f) 重叠区内边界点处计轴区段长度不应小于“最大车速 $\times$ （相邻ZC的延时 $^ +$ 从车轧入计轴区段到本ZC将该计轴区段状态的占用信息传出的时间消耗）-最小车长 $+ 2 \times$ 列车悬垂”。

g）ZC切换重叠区的始端应为计轴点，距离ZC边界的长度应大于一定的距离，该取值应至少考虑接管ZC建立连接时间、列车常用制动距离。

以图A.4为例，移交ZC重叠区长度按公式A.1计算：

$L _ { \tt R S A C C B R S R } = L _ { \tt T r a i n } + L _ { \tt D i s } + L _ { \tt R F B i \tt S i } + V _ { \tt m a x } \times T _ { \tt N B i \tt S i \tt S }$ ……(A.1)

式中：

$L _ { \mathrm { T r a i n } }$ 列车长度，单位为米（m）；Lpis 列车安全包络的最大误差，单位为米（m）；  
L常用制动 列车以最高运行速度至信号机的常用制动距离，单位为米(m）;$V _ { \mathrm { m a x } }$ 列车最高允许速度，单位为米每秒 $\mathrm { m } / { \mathsf { s } } )$ ;  
T建立连接 列车与接管ZC建立连接时间，从列车开始连接接管ZC开始，到完成注册，移交ZC向列车发送的移动授权延伸至接管ZC管辖范围截止（典型值 $1 2 \mathrm { ~ s ~ }$ )。

列车常用制动距离按公式A.2计算：

$L _ { \mathfrak { R H M } \bar { z } \mathfrak { t } \mathfrak { z } } = \big ( V _ { \mathrm { m a x } } ^ { 2 } - 0 ^ { 2 } \big ) / \big ( 2 \times b _ { \mathfrak { R H M a x } \bar { z } \bar { z } \mathfrak { k } } \big )$ (id:) …(A. 2)

![](images/8870e2b985682b0eee64efc786e5215fc1b51e5ff1146ef9ddd2791f310499d3.jpg)  
图A.4移交ZC重叠区

式中：

$V _ { m a x }$ $\mathrm { m } / \mathrm { s }$ b盘用减速度 ，单位为米每 $\mathrm { \ L m / s } ^ { 2 } \mathrm { \Delta }$ 别联 $L _ { \# }$ 于列车长度、列在车数因素，各厂家应h)重叠区的边盟点导边界点之间至少含两个计轴区段。

i） ZC移交重登区的典型设计如图A.5

![](images/d9421113db286cc3318b865e97ab7a0586b7f919c340177ba7ac592314b3e034.jpg)  
图A.5 不同方向的重叠区

中国城市轨道交通协会团体标准  
城市轨道交通基于通信的列车运行  
控制系统（CBTC）互联互通接口规范  
第4部分：区域控制器（ZC）间接口T/CAMET04011.4—2018

\*

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门西街8号）公司网址：http：//www.idpress.com北京铭成印刷有限公司印刷

开本： $8 8 0 \ \mathrm { m m } \times 1 \ 2 3 0 \ \mathrm { m m }$ 1/32印张：1.5字数：39千2019年5月第1版2019年5月第1次印刷

书号： $1 5 1 1 3 \cdot 5 7 3 1$ 定价：15.00元

# 版权所有侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174