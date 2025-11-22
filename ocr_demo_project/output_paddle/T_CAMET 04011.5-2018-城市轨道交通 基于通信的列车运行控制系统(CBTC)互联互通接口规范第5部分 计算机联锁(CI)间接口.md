# 中国城市轨道交通协会团体标准

T/CAMET 04011.5—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第5部分：计算机联锁（CI）间接口

# Urban rail transit — Interface specification for interoperability of communication based train control system Part 5: Interface between computer interlockings

2018-09-10 发布

2018-12-31 实施

---

## 目 次

前言 …… VII    
引言 …… IX    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 2    
3.1 术语 …… 2    
3.2 缩略语 …… 3    
4 总则 …… 3    
5 CI - CI 通信接口报文规范 …… 3    
5.1 接口连接方式 …… 3    
5.2 通信体系结构 …… 4    
5.3 接口数据描述 …… 5    
5.4 应用信息定义 …… 10

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第4部分：区域控制器（ZC）间接口；

——第5部分:计算机联锁(CI)间接口;

——第6部分：列车自动监控系统（ATS）间接口；

——第7部分:信号各子系统与维护支持系统(MSS)间接口;

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 5 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本规范由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

本部分主要起草人：编写组：宿秀元、张利峰、邱锡宏、陈鹤、高国栋、冯浩楠、段宏伟、张大涛、原志彬、刘清华、胡顺定、王悉。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范 第 5 部分: 计算机联锁(CI) 间接口

## 1 范围

T/CAMET 04011 的本部分规定了计算机联锁系统（CI）不同线路间接口，包括通信方式、拓扑结构、接口描述和信息包内容及异常处理等内容。

本部分适用于国内采用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通线路建设、用击者导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

下列文件对于本部分的所用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 24339.1—2009 轨道交通 通信、信号和处理系统 第1部分：封闭式传输系统中的安全相关通信（IEC 62280-1:2002, IDT）

TB/T 3027—2015 铁路车站计算机联锁技术条件

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 1 部分: 系统总体要求

运基信号 $$ 2010 $$  267 号 RSSP - I 铁路信号安全通信协议

IEEE 802.3 以太网(Ethernet)

---

RFC 791 互联网协议(Internet Protocol)

RFC 768 用户数据报协议 (User Datagram Protocol)

## 3 术语和缩略语

CJ/T 407—2012 和 T/CAMET 04010.1 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车—地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.2 

计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.3 

装备列车 CBTC-equipped trains

装备了 CBTC 系统车载设备且设备处于工作状态的列车。

[T/CAMET 04010.1,术语 3.1.11]

#### 3.1.4 

非装备列车 Non-CBTC-equipped trains

没有装备 CBTC 系统车载设备或者 CBTC 系统车载设备处于不工作状态的列车。

[T/CAMET 04010.1,术语 3.1.12]

---

#### 3.1.5 

常态点灯信号机 initial-lighted signal

无接近信息室外信号机点灯，有接近信息室外信号机根据接近属性显示的信号机。

### 3.2 缩略语

ARB: 始终占用的分区即非正常占用分区 (Always Reporting Block)

CBTC: 基于通信的列车控制 (Communication Based Train Control)

CI: 计算机联锁 (Computer Interlocking)

GAL:通用应用层(General Application Layer)

IPv4: 互联网协议 (Internet Protocol, IP) 的第 4 版

MAC: 媒体访问控制 (Medium Access Control)

RSSP:铁路信号安全协议(Railway Signal Safety Protocol)

TSR: 临时限速 (Temporary Speed Restriction)

UDP: 用户数据报协议 (User Datagram Protocol)

## 4 总则

本规范重点对互联互通不同线路间计算机联锁系统的通信接口进行了描述，最终系统功能、系统设备的工程配置、用户界面及操作方式、与外部系统接口要求、轨旁设备布置原则等本规范未规定的内容应在后续规范或工程实施中完成。

本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对CI间通信接口数据交互内容进行扩展。

## 5 CI - CI 通信接口报文规范

### 5.1 接口连接方式

#### 5.1.1 物理接口

CI 和相邻 CI 采用双路冗余的通信通道（将双网分别定义为 A 网和 B 网）以提高系统的可靠性，任何一个单网的故障都不会对系统的正常使用产生影响。两系统按照 A 网和 A 网相连、B 网和 B 网相连接的方式，

---

其连接方式见图1。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//20e3e6b4-8725-4dbb-a234-fc40fb72974a/markdown_0/imgs/img_in_image_box_199_164_642_321.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A43%3A46Z%2F-1%2F%2Faff12bebcee0dfcdca99ca42df670fe0f7d5f49dfe8b157c9627b9600d976a2e" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 1 CI - CI 双网冗余连接图</div>


### 5.2 通信体系结构

#### 5.2.1 通信模型

图 2 中安全功能模块和通信功能模块属于各子系统内部功能实现，分别用于实现安全功能和对外通信功能。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//20e3e6b4-8725-4dbb-a234-fc40fb72974a/markdown_0/imgs/img_in_image_box_182_530_662_846.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A43%3A46Z%2F-1%2F%2F6e2d63dcb80efa0d8a38f0e4cbe8e51d7686afdaac536ba1f7cca2bb01b0ab2c" alt="Image" width="57%" /></div>


<div style="text-align: center;">图 2 CI - CI 通信协议模型</div>


#### 5.2.2 通信机制

CI间通信机制如下：

a） CI 间通信采用周期发送的方式进行通信；

b）通信双方均采用大端字节序进行数据传输。

#### 5.2.3 通信层次结构

CI 间通信层次结构划分如图 3 所示。

---

a）物理层：采用 IEEE 802.3 标准协议。

b) 数据链路层: MAC 子层基于 IEEE802.3 标准。MAC 头由 14 个字节组成, 1 个帧校验序列 (4 字节) 将被加在 Ethernet 帧后面。



c） 网络层：IPv4。

d）传输层：UDP协议。



e）安全通信协议层：遵循 GB/T 24339.1—2009 标准、TB/T 3027—2015 标准要求，采用 RSSP-I 铁路信号安全通信协议，同时通过序列号对冗余网络数据进行过滤，不作为本文档描述。

f）应用层：包括通用应用层和CI应用层。

注：CI-CI接口单帧报文长度可突破RSSP-I协议传输的最大信息长度限制。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c72a75bc-0daa-41b1-9ca2-c2e53c508475/markdown_0/imgs/img_in_image_box_131_439_700_884.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A43%3A50Z%2F-1%2F%2Fbbe5d4c96def12963251cf4aeba42590d3e11b7385307ee9f9d61f4960cf19fe" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 3 CI 间通信层次结构</div>


### 5.3 接口数据描述

#### 5.3.1 动态交互描述

CI 与邻站 CI 传输分界线两边的设备信息，包括进路内物理区段、逻辑区段、信号机、站台门、紧急关闭按钮、道岔及保护区段状态。双方 CI

---

向对方传输互联互通相关范围内的本联锁管辖范围的设备状态，接收对方CI发送的设备状态。

##### 5.3.1.1 通用应用层消息包定义

按照《RSSP-I 铁路信号安全通信协议》，将相邻 CI 间每个周期需要交互的信息通过组成通用（GAL）信息包进行传输，如图 4 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//503dce9a-517b-4748-bf6c-bf22c40e9fad/markdown_0/imgs/img_in_image_box_200_306_644_495.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A43%3A53Z%2F-1%2F%2F28f9633e68342a905245582903c1fddc07ee445a1e682bc4e1df42b26c481816" alt="Image" width="52%" /></div>


<div style="text-align: center;">图 4 通用信息包和应用层信息包关系结构图</div>


##### 5.3.1.2 信息包格式定义

CI间通信的1个安全连接每周期最多允许发送1个GAL消息包，GAL消息包中包含CI间传输的各条应用信息，每个GAL消息包总长不得超过1000字节，格式定义见表1、表2。

<div style="text-align: center;">表 1 通用信息包格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">接口信息类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型高位</td><td rowspan="2">2字节</td><td rowspan="2">0x0606:CI-CI接口</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td style='text-align: center;'>3</td><td rowspan="4">源ID</td><td rowspan="4">4字节</td><td rowspan="4">发送方联锁ID*</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>6</td></tr></table>

---

<div style="text-align: center;">表 1 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="4">接收方标识信息</td><td style='text-align: center;'>7</td><td rowspan="4">目的ID</td><td rowspan="4">4字节</td><td rowspan="4">接收方联锁ID $ ^{a} $</td></tr><tr><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>9</td></tr><tr><td style='text-align: center;'>10</td></tr><tr><td rowspan="4">电子地图版本校验信息 $ ^{b} $</td><td style='text-align: center;'>11</td><td rowspan="4">CI与CI之间的版本一致性信息</td><td rowspan="4">4字节</td><td rowspan="4">CI-CI重叠区范围内，CI与CI间的数据版本校验信息</td></tr><tr><td style='text-align: center;'>12</td></tr><tr><td style='text-align: center;'>13</td></tr><tr><td style='text-align: center;'>14</td></tr><tr><td rowspan="4">本方消息序列号 $ ^{c} $</td><td style='text-align: center;'>15</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录发送本条消息时，本方的周期计数</td></tr><tr><td style='text-align: center;'>16</td></tr><tr><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>18</td></tr><tr><td rowspan="2">通信周期</td><td style='text-align: center;'>19</td><td rowspan="2">通信周期</td><td rowspan="2">2字节</td><td rowspan="2">单位：ms</td></tr><tr><td style='text-align: center;'>20</td></tr><tr><td rowspan="4">对方消息序列号 $ ^{d} $</td><td style='text-align: center;'>21</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息中的对方消息序列号 $ ^{e} $</td></tr><tr><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>24</td></tr><tr><td rowspan="4">收到上一条消息时本方序列号 $ ^{d} $</td><td style='text-align: center;'>25</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息时，本方的周期计数 $ ^{e} $</td></tr><tr><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>28</td></tr></table>

---

<div style="text-align: center;">表 1 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节
编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td style='text-align: center;'>协议版本号b</td><td style='text-align: center;'>29</td><td style='text-align: center;'>协议版本号</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>CI-CI的协议版本,001~255有效</td></tr><tr><td rowspan="2">应用层报文
总长度</td><td style='text-align: center;'>30</td><td rowspan="2">应用报文总长度</td><td rowspan="2">2字节</td><td rowspan="2">后续报文长度,以字节为单位,不含长度本身两字节</td></tr><tr><td style='text-align: center;'>31</td></tr><tr><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>32~1000</td><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>参见表3格式定义</td></tr><tr><td colspan="5">aID的具体编号原则在工程实现阶段确定。
b电子地图版本校验信息针对CI-CI重叠区电子地图两个CI共用的信息。若“电子地图版本校验信息”或“协议版本号”与相邻CI不一致,则进行丢包或断开通信处理。
序列号有效值为1~(231-1)。发送方应保证生成两包信息包时,两包信息包中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔。
d当未收到对方消息时,序列号发送0xFFFFFFFF。</td></tr></table>

<div style="text-align: center;">表 2 应用层信息格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节 编号</td><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>说 明</td></tr><tr><td rowspan="2">报文长度</td><td style='text-align: center;'>1</td><td rowspan="2">报文长度</td><td rowspan="2">由“报文类型~报文结束”的 帧长度</td></tr><tr><td style='text-align: center;'>2</td></tr><tr><td rowspan="2">报文类型</td><td style='text-align: center;'>3</td><td rowspan="2">定义某一条应用信息的 标识</td><td rowspan="2">自定义,详细内容参见5.3.2</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td rowspan="2">预留</td><td style='text-align: center;'>5</td><td rowspan="2">预留</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>7~报 文结束</td><td style='text-align: center;'>按照报文格式定义的报 文具体内容</td><td style='text-align: center;'>自定义,详细内容参见5.3.2</td></tr></table>

---

##### 5.3.1.3 通信状态管理

5.3.1.3.1 CI 应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站 CI 的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

a）消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查以及信息完整性检查；

b）通用应用(GAL)信息包消息所应包含的信息的完整性；

c）其他逻辑检查。

5.3.1.3.2 CI 应能对通信连接状态进行判断：

a）CI 判断与邻站 CI 通信中断的超时时间定义为  $ T_{C\mathrm{iTimeOut}} $  （可配置，推荐值 5 s）。

b) 通信建立后，CL在 $ T_{C\mathrm{iTimeOut}} $ 超时时间内没有接收到来自邻站CI 的任何消息，则CI应判断与邻站CI通信中断（指应用层根据GAL包头中字段进行判断，而非安全通信协议层进行的判断）。

c) 若 CI 判断接收到邻站 CI 的应用信息延迟已经达到  $ T_{C\mathtt{iT i m e O u t}} $  时，CI 应判断与邻站 CI 通信中断（指应用层根据 GAL 包头中字段进行判断，而非安全通信协议层进行的判断）。

d) CI 与邻站 CI 间通信中断的情况下，本站 CI 无法收到邻站汇报的设备信息。CI 应将邻站所有设备状态设置为安全侧，如将通往邻站进路的始端信号机置为禁止信号，对应来自邻站的区段设置为占用。

e） CI 与邻站 CI 间通信中断的情况下，若本站 CI 收到了合法的邻站 CI 信息，则本站 CI 应认为与邻站 CI 连接恢复。

f) 互联互通线网中，CI与邻站CI的通信超时时间应一致，消息有效期时间应一致。

#### 5.3.2 数据类型定义

表 3 规定了 CI 间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）的内容。

---

<div style="text-align: center;">表 3 CI-CI 通信的应用层信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>长度(字节)</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0201</td><td style='text-align: center;'>道岔状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0202</td><td style='text-align: center;'>物理区段状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0203</td><td style='text-align: center;'>逻辑区段状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0204</td><td style='text-align: center;'>信号机状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0205</td><td style='text-align: center;'>站台门状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0206</td><td style='text-align: center;'>紧急关闭按钮状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0207</td><td style='text-align: center;'>照查状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0208</td><td style='text-align: center;'>防淹门信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0209</td><td style='text-align: center;'>上电锁闭状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020a</td><td style='text-align: center;'>临时限速信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020b</td><td style='text-align: center;'>城市自定义信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020c</td><td style='text-align: center;'>厂商自定义信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr></table>

### 5.4 应用信息定义

#### 5.4.1 道岔状态信息

本 CI 应将互联互通相关范围内的本联锁管辖范围的道岔状态发送给邻站 CI。相邻 CI 间道岔索引顺序应保持一致。道岔状态信息见表 4。

<div style="text-align: center;">表 4 道岔状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的道岔数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>互联互通相关范围内的本联锁区管辖范围的道岔数量 n</td></tr></table>

---

<div style="text-align: center;">表 4 道岔状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td rowspan="2">道岔状态</td><td rowspan="2">n字节</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="2">道岔1封锁状态:01b:未封锁10b:封锁00b:非法*11b:默认值</td><td colspan="2">道岔1单锁状态:01b:未单锁10b:单锁00b:非法11b:默认值b</td><td colspan="2">道岔1引导总锁闭状态:01b:未引导总锁10b:引导总锁00b:非法11b:默认值</td><td colspan="2">道岔1位置:01b:定位10b:反位00b:四开11b:默认值</td></tr><tr><td colspan="10">“非法定义,正常通信过程中不应发送的设备状态,若出现非法设备状态,接收方认为本周期没有收到应用数据包,适用于本协议所有字段。</td></tr><tr><td colspan="10">“默认值定义,通信双方在具体工程项目中不使用的信息码字或联锁系统在初始化完成之前发送的状态,适用于本协议所有字段。</td></tr></table>

#### 5.4.2 物理区段状态信息

本 CI 应将互联互通相关范围内的本联锁区管辖范围内的物理区段状态发送给邻站 CI。相邻 CI 间物理区段索引顺序应保持一致。物理区段状态信息见表 5。

<div style="text-align: center;">表 5 物理区段状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的物理区段数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>互联互通相关范围内的本联锁区管辖范围的物理区段数量 n</td></tr></table>

---

<div style="text-align: center;">表 5 物理区段状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td rowspan="3">物理区段状态</td><td rowspan="2">2×n字节物理区段1的Byte1</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td style='text-align: center;'>区段1故障锁闭状态b,c:01b:区段未故障锁闭;10b:区段故障锁闭;00b:非法状态;11b:默认值</td><td style='text-align: center;'>区段1保护锁闭状态b,c:01b:区段未保护锁闭;10b:区段保护锁闭;00b:非法状态;11b:默认值</td><td style='text-align: center;'>区段1进路锁闭状态b:01b:区段未进路锁闭;10b:区段进路锁闭;00b:非法状态;11b:默认值</td><td style='text-align: center;'>区段1进路锁闭状态b:01b:区段未进路锁闭;10b:区段进路锁闭;00b:非法状态;11b:默认值</td><td style='text-align: center;'>区段1占用状态a:00b:区段占用;01b:非法状态;10b:区段空闲;11b:默认值</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>物理区段1的Byte2</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>区段1锁闭方向d:01b:上行运营方向;10b:下行运营方向;00b:无锁闭方向;11b:默认值</td><td style='text-align: center;'>区段1封锁状态b:01b:区段封锁;10b:区段未封锁;00b:非法状态;11b:默认值</td><td style='text-align: center;'>区段1ARB状态:01b:区段ARB;10b:区段未ARB;00b:非法状态;11b:默认值</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td colspan="10">采集轨道继电器状态。b1.不同厂家转换时,物理区段中任意一个逻辑区段锁闭,则认为物理区段锁闭;2.故障锁闭显示级别优先于进路锁闭,进路锁闭优先于保护区段锁闭;3.进路锁闭包括列车进路、引导进路、调车进路锁闭。c区段进路锁闭状态的一种,不满足解锁原则漏解锁时。d协议要求同一计轴内所有锁闭的逻辑区段方向应一致。</td></tr></table>

#### 5.4.3 逻辑区段状态信息

本 CI 应将互联互通相关范围内的本联锁区管辖范围的逻辑区段状态发送给邻站 CI。相邻 CI 间逻辑区段索引顺序应保持一致。逻辑区段状态信息见表 6。

---

<div style="text-align: center;">表 6 逻辑区段状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td style='text-align: center;'>包含的逻辑区段数量</td><td style='text-align: center;'>1字节</td><td colspan="8">互联互通相关范围内的本联锁区管辖范围内逻辑区段数量n</td></tr><tr><td rowspan="3">逻辑区段状态*</td><td rowspan="2">2×n字节逻辑区段1的Byte1</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>BI</td><td style='text-align: center;'>B0</td></tr><tr><td style='text-align: center;'>区段1锁闭方向：01b：上行运营方向：10b：下行运营方向：00b：无锁闭方向：11b：默认值</td><td style='text-align: center;'>区段1保护锁闭状态：01b：区段未保护锁闭：10b：区段保护锁闭00b：非法状态：11b：默认值</td><td style='text-align: center;'>区段1进路锁闭状态*：01b：区段未进路锁闭：10b：区段进路锁闭：00b：非法状态：11b：默认值</td><td colspan="5">区段1占用状态：00b：非CBTC车占用：01b：CBTC车占用：10b：区段空闲：11b：默认值</td></tr><tr><td style='text-align: center;'>逻辑区段1的Byte2</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>00b：非法状态：11b：默认值</td><td style='text-align: center;'>区段1故障锁闭状态：01b：区段未故障锁闭：10b：区段故障锁闭00b：非法状态：11b：默认值</td><td colspan="3">区段1封锁状态：01b：区段封锁：10b：区段未封锁：00b：非法状态：11b：默认值</td></tr><tr><td colspan="10">*物理区段和逻辑区段中占用、锁闭等状态信息均应同时发送，主要基于到以下几点：a)CBTC和后备模式下，CI对于列车占用状态获取方式包含物理区段、逻辑区段占用；b)互联互通的接口文件中需要兼容各家产品特点，不同厂家的产品内部逻辑或以物理区段的锁闭、占用状态为主，或以逻辑区段的占用、锁闭状态为主；c)为解决相邻联锁集中区站场状态显示不一致问题，应同时发送物理区段和逻辑区段；d)将处理后的逻辑区段占用状态发送给对方，发送方保证发送的状态应与本方人机界面显示状态一致，接收方可直接用于人机界面显示相邻线路复视区域内逻辑区段状态；e)进路锁闭包括列车进路、引导进路、调车进路锁闭。</td></tr></table>

---

#### 5.4.4 信号机状态信息

本 CI 应将互联互通相关范围内的本联锁区管辖范围内的信号机状态发送给邻站 CI。联锁分界点处信号机属于接车方联锁管辖，若联锁分界点有外置保护区段，则发车方联锁也应向接车方联锁发送该信号机状态信息。若联锁分界点无外置保护区段，则发车方联锁不发该信号机状态信息。相邻 CI 间信号机索引顺序应保持一致。信号机状态信息见表 7。

<div style="text-align: center;">表 7 信号机状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td style='text-align: center;'>包含的信号机数量</td><td style='text-align: center;'>1字节</td><td colspan="8">互联互通相关范围内的本联锁区管辖范围的信号机数量n</td></tr><tr><td rowspan="4">信号机状态*</td><td rowspan="2">3×n字节信号机1的Byte1</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="8">信号机1显示状态b:0000 0000b:断丝;0001 0001b:红灯;0001 0010b:黄灯;0001 0100b:绿灯;0001 1000b:红黄灯;1111 1111b:默认值;其他:非法</td></tr><tr><td style='text-align: center;'>信号机1的Byte2</td><td style='text-align: center;'>信号机1保护区段命令c:01b:保护建立请求;10b:保护取消请求;00b:无命令;11b:默认值</td><td colspan="2">信号机1接近锁闭:01b:接近锁闭;10b:未接近锁闭;00b:非法状态;11b:默认值</td><td colspan="2">信号机1封锁状态:01b:封锁;10b:未封锁;00b:非法状态;11b:默认值</td><td colspan="3">信号机1亮灭状态:01b:点灯;10b:灭灯;00b:非法状态;11b:默认值</td></tr><tr><td style='text-align: center;'>信号机1的Byte3</td><td style='text-align: center;'>预留</td><td colspan="2">预留</td><td colspan="2">预留</td><td colspan="3">信号机1保护区段有效标志d:01b:保护区段有效;</td></tr></table>

---

<div style="text-align: center;">表 7 信号机状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="4">说明</td></tr><tr><td style='text-align: center;'>信号机状态*</td><td style='text-align: center;'>信号机1的Byte3</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>预留</td><td style='text-align: center;'>10b:保护区段无效;00b:非法状态;11b:默认值</td></tr><tr><td colspan="6">*分界处的信号机,发车站联锁向接车站联锁仅发送保护区段命令,其他状态发送默认值;接车站联锁向发车站联锁仅发送的保护区段命令为“无命令”,其他信息发送有效值。</td></tr><tr><td colspan="6">*信号机的有效状态包括:亮红、亮黄、亮绿、亮红黄、灭红、灭绿、灭黄。a)灭绿、灭黄定义:CBTC模式进路信号开放;b)亮绿、亮黄定义:后备模式进路信号开放;c)亮红黄定义:引导信号开放;d)断丝定义:亮灯时灯丝继电器落下;e)针对常态点灯的信号机:在联锁控区边界处,接车站信号机开放作为发车站信号开放检查条件的场景下(无论实体或者虚拟):接车站信号机亮绿、亮黄满足发车站信号开放(灭灯开放或者点灯开放)对此条件的检查。</td></tr><tr><td colspan="6">*1.发车站联锁向接车站办理的终端在分界点处的进路完整锁闭且其保护区段建立的触发区段占用条件都具备时开始发送保护区段建立请求,直到保护区段已锁闭;2.发车站联锁收到保护区段停稳信息时,或发车站连接分界点处的区段解锁时发送“保护取消请求”,直到保护区段已解锁;3.其他情况发送无命令;4.主进路与对应保护区段属于不同CI时,保护区段所属CI收到主进路所属CI发送的“保护取消请求”时,可不考虑主进路CI内线路情况,无条件采信。*发送方CI应保证:发送“保护区段有效”状态时,“逻辑区段状态信息”包中,该保护区段内所有逻辑区段的“保护锁闭状态”字段取值均为“区段保护锁闭”。主进路CI判断保护区段是否可用时,除“保护区段有效标志”字段外,可不对保护区段CI范围内的其他条件进行判断。若主进路CI进行了其他判断,则由主进路CI保证系统的可用性。</td></tr></table>

---

#### 5.4.5 站台门状态信息

本 CI 将互联互通相关范围内的本联锁区管辖范围的站台门状态信息发送给邻站 CI。相邻 CI 间站台门索引顺序应保持一致。站台门状态信息见表 8。

<div style="text-align: center;">表 8 站台门状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td colspan="8">互联互通相关范围内的本联锁区管辖范围内站台门数量n</td></tr><tr><td rowspan="2">信息单元状态</td><td rowspan="2">0.5×n字节（进位取整）</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="4">站台门2状态</td><td colspan="2">站台门1旁路标志：01b:未旁路；10b:旁路；00b:非法状态；11b:默认值</td><td colspan="2">站台门1开关状态：01b:开门；10b:关门且锁闭；00b:非法状态；11b:默认值</td></tr></table>

#### 5.4.6 站台紧急关闭按钮信息

本 CI 将互联互通相关范围内的本联锁区管辖范围的站台紧急关闭信息发送给邻站 CI。相邻 CI 间站台紧急关闭索引顺序应保持一致。站台紧急关闭按钮信息见表 9。

<div style="text-align: center;">表 9 站台紧急关闭按钮信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>互联互通相关范围内的本联锁区管辖范围的紧急关闭按钮数量 n</td></tr></table>

---

<div style="text-align: center;">表 9 站台紧急关闭按钮信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td rowspan="2">信息单元状态</td><td rowspan="2">0.25×n字节(进位取整)</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td style='text-align: center;'>紧急关闭4状态</td><td style='text-align: center;'>紧急关闭3状态</td><td style='text-align: center;'>紧急关闭2状态</td><td style='text-align: center;'>紧急关闭1状态</td><td style='text-align: center;'>紧急关闭0状态</td><td style='text-align: center;'>紧急关闭0状态</td><td style='text-align: center;'>紧急关闭0状态</td><td style='text-align: center;'>紧急关闭0状态</td></tr></table>

#### 5.4.7 照查状态信息

本 CI 将互联互通相关范围内的本联锁区管辖范围的照查状态信息发送给邻站 CI。相邻 CI 间照查索引顺序应保持表 10。

<div style="text-align: center;">图表 10 照查状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="9">说 明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td colspan="9">互联互通相关范围内的本联锁区管辖范围的照查数量n</td></tr><tr><td rowspan="2">信息单元状态</td><td rowspan="2">0.25×n字节(进位取整)</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td><td style='text-align: center;'></td></tr><tr><td colspan="2">照查4状态</td><td colspan="2">照查3状态</td><td colspan="2">照查2状态</td><td colspan="3">照查1状态a:01b:照查落下;10b:照查吸起;00b:非法状态;11b:默认值</td></tr><tr><td colspan="11">°照查条件在具体工程中做详细定义。例如:照查条件常态吸起,在发车站末区段锁闭时落下,上电锁闭时照查状态为落下。</td></tr></table>

---

#### 5.4.8 防淹门信息

本 CI 将互联互通相关范围内的本联锁区管辖范围的防淹门信息发送给邻站 CI。相邻 CI 间防淹门索引顺序应保持一致。防淹门信息见表 11。

<div style="text-align: center;">表 11 防淹门信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td colspan="8">互联互通相关范围内的本联锁区管辖范围的防淹门数量n</td></tr><tr><td rowspan="2">信息单元状态</td><td rowspan="2">n字节</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="2">预留</td><td colspan="2">防淹门1关门允许:01b:允许;10b:不允许;00b:非法状态;11b:默认值</td><td colspan="2">防淹门1关门请求:01b:请求;10b:未请求;00b:非法状态;11b:默认值</td><td colspan="2">防淹门1状态:01b:关闭;10b:开放;00b:非法状态;11b:默认值</td></tr></table>

#### 5.4.9 上电锁闭状态信息

本 CI 将本站上电锁闭状态信息发送给邻站 CI。上电锁闭状态信息见表 12。

<div style="text-align: center;">表 12 上电锁闭状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>本CI上电锁闭状态数量n</td></tr><tr><td style='text-align: center;'>信息单元状态</td><td style='text-align: center;'>n字节</td><td style='text-align: center;'>上电锁闭状态: 0x55:设置上电锁闭; 0xaa:未设置上电锁闭; 0xff:默认值; 其他:非法码字</td></tr></table>

---

#### 5.4.10 临时限速信息

本 CI 应将互联互通相关范围内的本联锁管辖范围的临时限速区段状态发送给邻站 CI。相邻 CI 间临时限速区段索引顺序应保持一致。临时限速信息见表 13。

<div style="text-align: center;">表 13 临时限速信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字  段</td><td style='text-align: center;'>长  度</td><td colspan="8">说  明</td></tr><tr><td style='text-align: center;'>包含的临时限速区段数量</td><td style='text-align: center;'>1字节</td><td colspan="8">互联互通相关范围内的本联锁区管辖范围的临时限速区段数量n</td></tr><tr><td rowspan="2">临时限速区段状态</td><td rowspan="2">0.25×n字节(进位取整)</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="2">临时限速区段4TSR状态:01b:区段设置TSR;10b:区段未设置TSR;00b:非法状态;11b:默认值</td><td colspan="2">临时限速区段3TSR状态:01b:区段设置TSR;10b:区段未设置TSR;00b:非法状态;11b:默认值</td><td colspan="2">临时限速区段2TSR状态:01b:区段设置TSR;10b:区段未设置TSR;00b:非法状态;11b:默认值</td><td colspan="2">临时限速区段1TSR状态:01b:区段设置TSR;10b:区段未设置TSR;00b:非法状态;11b:默认值</td></tr></table>

#### 5.4.11 城市自定义信息

本 CI 将互联互通相关范围内的本联锁管辖范围的城市自定义信息发送给邻站 CI，见表 14。

<div style="text-align: center;">表 14 城市自定义信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>城市自定义</td><td style='text-align: center;'>n 字节</td><td style='text-align: center;'>报文内容为城市自定义</td></tr></table>

#### 5.4.12 厂商自定义信息

本 CI 将互联互通相关范围内的本联锁管辖范围的厂商自定义信息

---

发送给邻站 CI, 见表 15。

<div style="text-align: center;">表 15 厂商自定义信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>厂商自定义</td><td style='text-align: center;'>n 字节</td><td style='text-align: center;'>报文内容为厂商自定义</td></tr></table>

---

中国城市轨道交通协会团体标准  

城市轨道交通 基于通信的列车运行  

控制系统（CBTC）互联互通接口规范  

第5部分：计算机联锁（CI）间接口  

T/CAMET 04011.5—2018  

*  

中国铁道出版社有限公司出版发行  

（100054，北京市西城区右安门西街8号）  

公司网址：http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本：880 mm×1230 mm 1/32 印张：1 字数：24千  

2019年5月第1版 2019年5月第1次印刷

书号：15113·5730 定价：15.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//41f3dcf7-92c6-4d84-8d4f-269e2955a781/markdown_0/imgs/img_in_image_box_934_111_1117_287.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A45%3A01Z%2F-1%2F%2F146757db4079aaf147736356c491f002e0b4116edeac3eca623b2c882ceb2a96" alt="Image" width="15%" /></div>