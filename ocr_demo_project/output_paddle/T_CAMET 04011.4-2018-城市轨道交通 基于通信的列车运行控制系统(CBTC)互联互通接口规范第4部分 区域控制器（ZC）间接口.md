# 中国城市轨道交通协会团体标准

T/CAMET 04011.4—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第4部分：区域控制器（ZC）间接口

# Urban rail transit — Interface specification for interoperability of communication based train control system Part 4: Interface between zone controllers

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
5 ZC-ZC 通信接口报文规范 …… 4    
5.1 接口连接方式 …… 4    
5.2 通信体系结构 …… 4    
5.3 接口数据描述 …… 6    
5.4 应用信息定义 …… 10    
附录 A（规范性附录） 列车控制权切换正常流程示例及列车移交相关原则 …… 29

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第4部分：区域控制器（ZC）间接口；

——第5部分:计算机联锁(CI)间接口;

——第6部分：列车自动监控系统(ATS)间接口；

——第7部分：信号各子系统与维护支持系统(MSS)间接口；

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 4 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

主要起草人：编写组：耿鹏、聂宇威、骆正新、杨旭文、张春雨、刘剑、姜庆阳、吕浩炯、陈昕、陆晓红、胡顺定、刘宏杰、刘键。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范 第4部分:区域控制器(ZC)间接口

## 1 范围

T/CAMET 04011 的本部分定义了区域控制器（ZC）间接口，规定了相关的系统架构、功能、性能接口、验证等内容；最终系统功能、系统设备的工程配置、用户界面及操作方式、与外部系统接口要求、轨旁设备布置原则等。

本部分适用于国内采用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

市轨道交

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 1 部分: 系统总体要求

运基信号 $$ 2010 $$  267 号 RSSP - I 铁路信号安全通信协议

IEEE 802.3 以太网(Ethernet)

RFC 791 互联网协议 (Internet Protocol)

---

RFC 768 用户数据报协议 (User Datagram Protocol)

## 3 术语和缩略语

GB 50157—2013 和 CJ/T 407—2012 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.2 

## 正线 main line

载客列车运营的贯穿全程的线路。

[GB 50157—2013, 定义 2.0.11]

#### 3.1.3 

列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB 50157—2013, 定义 2.0.38]

#### 3.1.4 

列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB 50157—2013, 定义 2.0.39]

#### 3.1.5 

## 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

---

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.6 

## 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点。

#### 3.1.7 

## 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T 407—2012, 定义 3.1.7]

#### 3.1.8 

## 跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 04010.1,术语 3.1.14]

### 3.2 缩略语

AM: 列车自动驾驶模式 (Automatic Train Operating Mode)

AR: 自动折返 (Automatic Reversal Operation)

ATP: 列车自动防护 (Automatic Train Protection)

ATS: 列车自动监控 (Automatic Train Supervision)

CBTC: 基于通信的列车控制 (Communication Based Train Control)

CI: 计算机联锁 (Computer Interlocking)

CM: 列车自动防护模式 (Coded Train Operating Mode)

EUM: 非限制人工驾驶模式 (Emergency Unrestricted Train Operating Mode)

GAL: 通用应用层 (General Application Layer)

IPv4: 互联网协议 (Internet Protocol, IP) 的第 4 版

MA: 移动授权 (Movement Authority)

PSD: 站台门 (Platform Screen Door)

RM: 限制人工驾驶模式 (Restricted Train Operating Mode)

TSR: 临时限速 (Temporary Speed Restriction)

UDP: 用户数据报协议 (User Datagram Protocol)

---

ZC: 区域控制器 (Zone Controller)

## 4 总则

4.1 本规范重点针对互联互通中关键的跨线区域控制器间的通信接口，本规范未规定的内容应在后续规范或工程实施中完成。

4.2 满足城市轨道交通互联互通要求的 CBTC 系统应遵守本规范。

4.3 本规范对通用性的互联互通接口数据进行定义，可根据工程项目具体情况，对 ZC 间通信接口数据交互内容进行扩展。

## 5 ZC - ZC 通信接口报文规范

### 5.1 接口连接方式

#### 5.1.1 物理接口

ZC 应冗余接入信号安全数据网，网络拓扑结构采用 A 网 - A 网、B 网 - B 网两个链路。

### 5.2 通信体系结构

#### 5.2.1 通信模型

图 1 中安全功能模块和通信功能模块应由各厂家 ZC 子系统内部功能实现，分别用于实现安全功能和对外通信功能。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7da38242-50f4-4341-99ab-bd9f284e894f/markdown_0/imgs/img_in_image_box_188_753_634_1074.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A57%3A39Z%2F-1%2F%2F78141648b6a76c67f98c7bc04b1ffe679d1e5cae264d7b0439606a235c051bb1" alt="Image" width="53%" /></div>


<div style="text-align: center;">图 1 ZC - ZC 通信协议模型</div>

---

#### 5.2.2 通信机制

ZC 间通信机制如下：

a） ZC 间通信应采用周期发送的方式进行通信；

b）通信双方均采用大端字节序进行数据传输。





#### 5.2.3 通信层次结构

ZC 间通信层次结构划分如图 2 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c286a5a1-1c7f-4a82-904e-4ab45c48bdc1/markdown_0/imgs/img_in_image_box_165_334_708_815.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A57%3A43Z%2F-1%2F%2F2f65d4f9e1f2d06c0e0a19a869dd369979985760a33c55b01141f94044bfbf2f" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 2 ZC 间通信层次结构</div>


图 2 中使用的通信协议如下：

a） 物理层：采用 IEEE802.3 标准协议；

b）网络层：IPv4；

c) 传输层: UDP 协议;

d) 安全通信协议层:采用 RSSP-I 铁路信号安全通信协议;



e）应用层：参见 5.3.1 详细定义。

注：ZC-ZC接口单帧报文长度可突破RSSP-I协议传输的最大信息长度限制。

---

### 5.3 接口数据描述

#### 5.3.1 动态交互描述

##### 5.3.1.1 通信应用层消息包定义

按照《RSSP-I 铁路信号安全通信协议》，将相邻 ZC 间每个周期需要交互的信息通过组成通用（GAL）信息包进行传输，如图 3 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//de10c585-ee48-4e23-b986-3e68266da87e/markdown_0/imgs/img_in_image_box_168_299_641_458.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A57%3A46Z%2F-1%2F%2Fe5809a485d68c3b272ca8f8d576506d6366d1a891e950746f57cda5b65582cc0" alt="Image" width="56%" /></div>


<div style="text-align: center;">图 3 通用信息包和应用层信息包关系结构图</div>


##### 5.3.1.2 信息包格式定义

ZC 间通信的 1 个安全连接每周期最多允许发送 1 个 GAL 消息包，GAL 包中包含 ZC 间传输的各条应用信息。GAL 包格式定义见表 1。

<div style="text-align: center;">表 1 通用信息包格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="2">接口信息类型</td><td style='text-align: center;'>1</td><td style='text-align: center;'>类型高位</td><td rowspan="2">2字节</td><td rowspan="2">0x0101:ZC-ZC 接口</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>类型低位</td></tr><tr><td rowspan="4">发送方标识信息</td><td style='text-align: center;'>3</td><td rowspan="4">源ID</td><td rowspan="4">4字节</td><td rowspan="4">发送方ZC ID</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>6</td></tr><tr><td rowspan="4">接收方标识信息</td><td style='text-align: center;'>7</td><td rowspan="4">目的ID</td><td rowspan="4">4字节</td><td rowspan="4">接收方ZC ID</td></tr><tr><td style='text-align: center;'>8</td></tr><tr><td style='text-align: center;'>9</td></tr><tr><td style='text-align: center;'>10</td></tr></table>

---

<div style="text-align: center;">表 1 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>信息位定义及说明</td></tr><tr><td rowspan="4">数据版本校验信息</td><td style='text-align: center;'>11</td><td rowspan="4">线路数据版本</td><td rowspan="4">4字节</td><td rowspan="4">ZC重叠区内数据版本信息</td></tr><tr><td style='text-align: center;'>12</td></tr><tr><td style='text-align: center;'>13</td></tr><tr><td style='text-align: center;'>14</td></tr><tr><td rowspan="4">本方消息序列号a</td><td style='text-align: center;'>15</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录发送木条消息时，本方的周期计数</td></tr><tr><td style='text-align: center;'>16</td></tr><tr><td style='text-align: center;'>17</td></tr><tr><td style='text-align: center;'>18</td></tr><tr><td rowspan="2">通信周期</td><td style='text-align: center;'>19</td><td rowspan="2">通信周期</td><td rowspan="2">2字节</td><td rowspan="2">设备通信周期，单位：ms</td></tr><tr><td style='text-align: center;'>20</td></tr><tr><td rowspan="4">对方消息序列号a</td><td style='text-align: center;'>21</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息中的对方消息序列号。默认值：0xFFFFFFFb</td></tr><tr><td style='text-align: center;'>22</td></tr><tr><td style='text-align: center;'>23</td></tr><tr><td style='text-align: center;'>24</td></tr><tr><td rowspan="4">收到上一条消息时本方序列号a</td><td style='text-align: center;'>25</td><td rowspan="4">序列号</td><td rowspan="4">4字节</td><td rowspan="4">记录收到对方上一条消息时，本方的周期计数。默认值：0xFFFFFFFb</td></tr><tr><td style='text-align: center;'>26</td></tr><tr><td style='text-align: center;'>27</td></tr><tr><td style='text-align: center;'>28</td></tr><tr><td style='text-align: center;'>协议版本号a</td><td style='text-align: center;'>29</td><td style='text-align: center;'>协议版本号</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>ZC-ZC的协议版本</td></tr><tr><td rowspan="2">应用层信息长度</td><td style='text-align: center;'>30</td><td rowspan="2">应用层信息长度</td><td rowspan="2">2字节</td><td rowspan="2">从应用层数据开始到应用层数据结束的总字节数，不含报文头长度</td></tr><tr><td style='text-align: center;'>31</td></tr><tr><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>32~结束</td><td style='text-align: center;'>应用层数据</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>参见表2格式定义</td></tr></table>

---

<div style="text-align: center;">表 1 通用信息包格式定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>$ ^{*} $ 1. 序列号有效值为  $ 1 \sim (2^{31} - 1) $ 。发送方必须保证生成两包信息包时，两包信息报中的“本方消息序列号”字段的差值与“通信周期”相乘等于生成两包消息的时间间隔。
2. 当 ZC 判断“数据版本校验信息”或“协议版本号”字段校验不通过时，应进行丢包或断开安全连接处理。
 $ ^{*} $ 当未收到对方消息时，填写默认值。</td></tr></table>

<div style="text-align: center;">表 2 应用层信息格式定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息域定义</td><td style='text-align: center;'>字节编号</td><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="2">报文长度</td><td style='text-align: center;'>1</td><td rowspan="2">报文长度(报文类型~ 报文结束)</td><td rowspan="2">自定义,详细内容参 见5.3.2</td></tr><tr><td style='text-align: center;'>2</td></tr><tr><td rowspan="2">报文类型</td><td style='text-align: center;'>3</td><td rowspan="2">定义某一条应用信息的 标识</td><td rowspan="2">自定义,详细内容参 见5.3.2</td></tr><tr><td style='text-align: center;'>4</td></tr><tr><td rowspan="2">预留</td><td style='text-align: center;'>5</td><td rowspan="2">预留</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>报文内容</td><td style='text-align: center;'>7~报文 结束</td><td style='text-align: center;'>按照报文格式定义的报 文具体内容</td><td style='text-align: center;'>自定义,详细内容参见5.4</td></tr></table>

##### 5.3.1.3 通信状态管理

ZC 间通信状态管理如下：

a）ZC 应对接收到的应用消息进行合法性检查，若检查未通过，认为本周期未收到邻站 ZC 的应用信息或主动断开安全连接，并记录报警信息。具体检查方式如下：

1）消息内容的一致性检查：包括信息的字段合法性检查、字段组合合法性检查，以及信息完整性检查。若消息中存在字段的“非法”取值，应对本 GAL 包信息中所有进行丢弃处理。

2）通用应用(GAL)信息包消息所应包含的信息的完整性。

---

3）其他逻辑检查。

b） ZC 应能对通信连接状态进行判断（指应用层根据 GAL 包头中字段进行判断，而非安全通信协议层进行的判断）：

1）ZC 认为与邻站 ZC 通信中断的超时时间定义为  $ T_{ZCTimeout} $  （1.5 s~6 s，可配置，典型值：4.5 s）；

2）在通信建立后，若 ZC 在  $ T_{ZCTimeout} $  超时时间内没有接收到来自邻站 ZC 的任何消息，则 ZC 应认为与邻站 ZC 通信中断；

3）若 ZC 判断接收到邻站 ZC 的 GAL 包延迟已经达到  $ T_{ZCTimeout} $  时，ZC 应丢弃此 GAL 包，或认为与邻站 ZC 通信中断；

4）通信中断的情况下应生成报警信息，并进行安全侧处理；

5）ZC与邻站ZC间通信中断的情况下，若本站ZC收到了合法的邻站ZC信息，则本站ZC应认为与邻站ZC连接恢复；

6）互联互通线网中，各厂商 ZC 间的通信超时时间应一致，消息有效期时间应一致。

#### 5.3.2 数据类型定

表 3 规定了 ZC 间通信的所有应用信息类型及其含义、发送方向、长度范围、发送方式（周期/非周期）的内容。

<div style="text-align: center;">表 3 ZC-ZC 通信的应用层信息定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>长度(字节)</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x0204</td><td style='text-align: center;'>道岔状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x0208</td><td style='text-align: center;'>物理区段状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020A</td><td style='text-align: center;'>移交状态信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020B</td><td style='text-align: center;'>移交列车信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020C</td><td style='text-align: center;'>城市自定义包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>非周期</td></tr><tr><td style='text-align: center;'>0x020D</td><td style='text-align: center;'>厂商自定义包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>非周期</td></tr></table>

---

<div style="text-align: center;">表 3 ZC - ZC 通信的应用层信息定义（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信息类型</td><td style='text-align: center;'>信息包名</td><td style='text-align: center;'>发送方向</td><td style='text-align: center;'>长度(字节)</td><td style='text-align: center;'>发送方式</td></tr><tr><td style='text-align: center;'>0x020E</td><td style='text-align: center;'>站场信息延时包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr><tr><td style='text-align: center;'>0x020F</td><td style='text-align: center;'>轨道区段列车排序信息包</td><td style='text-align: center;'>双向</td><td style='text-align: center;'>xx</td><td style='text-align: center;'>周期</td></tr></table>

### 5.4 应用信息定义

#### 5.4.1 说明

本节中的“非法”值：正常通信时发送方不应发送的非法取值。接收方收到GAL包中的应用信息帧中存在“非法”值时，应判断本GAL包数据有误，丢弃本GAL包，并认为本周期未收到数据。

本节中的“默认”值：(1) 针对具体工程中不实现的功能，通信双方可在具体工程中约定，相关字段取值发送“默认”值；(2) 设备在初始化完成前，无法确定状态时，相关字段取值发送“默认值”。接收方收到“默认”值后，应认为信息有效，不进行处理。

本节中的设备索引值均从 1 开始。

本节中涉及“上行”、“下行”的方向定义，均采用运营方向规定的上下行。跨线时，两条线路上下行运营方向定义不一致时，发送上下行方向信息的原则确定为：发送方ZC按照自身所属线路上下行定义进行发送，由接收方ZC适配处理。

本节中的“预留”字段，发送方统一填0，接收方可不对预留字段进行校验。

本节中的轨道区段内的偏移量，基准点均为车载电子地图中，该轨道区段沿车载电子地图上行方向的起点。

#### 5.4.2 道岔状态信息

本 ZC 应将配置重叠区内所有道岔状态发送给邻站 ZC。相邻 ZC 间道岔索引顺序应保持一致。该信息包格式见表 4。

<div style="text-align: center;">表 4 道岔状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的道岔数量</td><td style='text-align: center;'>1 字节</td><td style='text-align: center;'>配置重叠区本 ZC 管辖范围内道岔数量 n（最多 128 个）安全信息</td></tr></table>

---

<div style="text-align: center;">表 4 道岔状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="7">说 明</td></tr><tr><td rowspan="2">道岔状态a</td><td rowspan="2">n/4字节(向上取整)</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td></tr><tr><td style='text-align: center;'>道岔4状态</td><td colspan="2">道岔3状态</td><td colspan="2">道岔2状态</td><td colspan="2">道岔1状态:01b:定位;10b:反位;00b:四开;11b:默认值(填充信息或无法提供该信息,应填写“默认值”)。安全信息</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>......</td><td colspan="2">......</td><td colspan="2">......</td><td colspan="2">......</td></tr><tr><td colspan="9">“对于双动道岔,ZC应按照2个单独道岔向相邻ZC发送。bZC收到相邻ZC发送的“道岔状态”字段取值为默认值时,应对道岔状态进行安全侧处理。</td></tr></table>

#### 5.4.3 物理区段状态信息

本 ZC 将配置重叠区内本管辖区物理区段信息发送给邻站 ZC。相邻 ZC 需对物理区段进行排序，并且同一物理区段在发送方的排序位置与接收方的排序位置相同。该信息包格式见表 5。

<div style="text-align: center;">表 5 物理区段状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="2">字  段</td><td style='text-align: center;'>长度</td><td colspan="8">说  明</td></tr><tr><td colspan="2">包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td colspan="8">配置重叠区本ZC管辖范围内物理区段数量n(最多60个)。安全信息</td></tr><tr><td rowspan="2">物理区段1信息</td><td rowspan="2">物理区段1状态</td><td rowspan="2">1字节</td><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="2">预留</td><td colspan="2">预留</td><td colspan="2">预留</td><td colspan="2">物理区段1占用状态:01b:空闲;10b:占用;其他:非法。安全信息</td></tr></table>

---

<div style="text-align: center;">表 5 物理区段状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>物理区段2信息</td><td style='text-align: center;'>同上</td><td style='text-align: center;'>同上</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>物理区段n信息</td><td style='text-align: center;'>同上</td><td style='text-align: center;'>同上</td></tr></table>

#### 5.4.4 移交状态信息

移交状态信息包用于 ZC 切换的管理，信息包含移交与接管 ZC 交互的各自边界点移交状态信息。该信息包格式见表 6。

<div style="text-align: center;">表 6 移交状态信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>与交互ZC的移交边界数n，按照实际边界数填写。有效范围：1~20。
安全信息</td></tr><tr><td rowspan="4">信息单元状态</td><td rowspan="4">变长字节</td><td style='text-align: center;'>边界点ID(4字节)：
ZC移交边界ID。一个物理边界点应使用一个唯一ID，即使在此边界点可进行双方向移交。
安全信息</td></tr><tr><td style='text-align: center;'>接近列车ID(4字节)：
非通信车默认ID：0xFFFFFFF；
默认值：0x00000000。
安全信息</td></tr><tr><td style='text-align: center;'>接近列车距离，单位：cm(4字节)：
有效范围：0x0~0xFFFFFFF；
默认值：0xFFFFFFF。
安全信息</td></tr><tr><td style='text-align: center;'>接近列车运行等级(1字节)：
0x01：CBTC；
0x02：点式；</td></tr></table>

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="6">信息单元状态</td><td rowspan="6">变长字节</td><td style='text-align: center;'>0x03:联锁级;0xFF:默认值;其他:非法。安全信息</td></tr><tr><td style='text-align: center;'>接近列车车载ATP当前模式(1字节) $ ^{*} $ :0x01:AM模式;0x02:CM模式;0x03:RM模式;0x04:EIM模式;0xFF:默认值;其他:非法。安全信息</td></tr><tr><td style='text-align: center;'>停车保证请求(1字节) $ ^{b} $ :有:0x55;无:0AA;其他:非法。停车保证功能可选,根据工程项目需求确定,如无此功能则默认填写无停车保证请求安全信息</td></tr><tr><td style='text-align: center;'>停车保证请求序列号(4字节) $ ^{b} $ :有效范围:1~(2 $ ^{31} $ -1);默认值:0xFFFFFFF。安全信息</td></tr><tr><td style='text-align: center;'>移交列车VID(4字节):默认值:0x00000000。无列车移交时填写默认值。安全信息</td></tr><tr><td style='text-align: center;'>列车移交接管状态(1字节):0x00:移交接管未触发(列车未处于移交/接管状态);0x11:列车移交(移交ZC向接管ZC发送,当前列车已处于移交状态);</td></tr></table>

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="2">说明</td></tr><tr><td rowspan="9">信息单元状态</td><td rowspan="9">变长字节</td><td colspan="2">0x22:列车接管(接管ZC向移交ZC发送,当前列车已处于接管状态,接管ZC计算的MA可越过移交边界);0xFF:禁止驶入(接管ZC向移交ZC发送,指示不允许MA进入接管ZC管辖范围);其他:非法。安全信息</td></tr><tr><td colspan="2">MA是否有效(1字节):本车有在本ZC管辖范围内的MA:0x55;本车无在本ZC管辖范围内的MA:0xAA;其他:非法。安全信息</td></tr><tr><td rowspan="7">列车在本ZC管辖范围内的MA信息(变长)</td><td style='text-align: center;'>MA方向(1字节):MA起点朝向MA终点的方向,以MA起点处的上下行方向确定。上行:0x55;下行:0xAA;其他:非法。安全信息</td></tr><tr><td style='text-align: center;'>MA起点位置(8字节)安全信息</td></tr><tr><td style='text-align: center;'>安全防护点位宽(8字节)安全信息</td></tr><tr><td style='text-align: center;'>区段ID:4字节默认值:0x00000000</td></tr><tr><td style='text-align: center;'>区段内偏移量(4字节):单位:cm有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFFF</td></tr><tr><td style='text-align: center;'>区段ID:4字节默认值:0x00000000</td></tr><tr><td style='text-align: center;'>区段内偏移量(4字节):单位:cm有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFFF</td></tr></table>

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="3">说明</td></tr><tr><td rowspan="12">信息单元状态</td><td rowspan="12">变长字节</td><td rowspan="12">列车在本ZC管辖范围内的MA信息(变长)”</td><td rowspan="2">障碍点信息(8字节)安全信息</td><td style='text-align: center;'>轨道区段ID:4字节默认值:0x00000000</td></tr><tr><td style='text-align: center;'>区段内偏移量(4字节):单位:cm有效范围:0x0~0xFFFFFFF默认值:0xFFFFFFF</td></tr><tr><td colspan="2">保护区段有效性(1字节):有效:0x55;无效:0xAA;默认值:0xFF;其他:非法。安全信息</td></tr><tr><td rowspan="6">道岔信息(变长):MA(含保护区段)覆盖范围内所有道岔的信息安全信息</td><td style='text-align: center;'>道岔个数n有效范围:0~20(1字节)</td></tr><tr><td style='text-align: center;'>道岔(1)ID:4字节</td></tr><tr><td style='text-align: center;'>道岔(1)状态:1字节定位:0x55;反位:0xAA;其他:非法</td></tr><tr><td style='text-align: center;'>道岔(2)ID:4字节</td></tr><tr><td style='text-align: center;'>道岔(2)状态:1字节</td></tr><tr><td style='text-align: center;'>……</td></tr><tr><td rowspan="3">PSD信息(变长):MA覆盖范围内所有PSD的信息安全信息</td><td style='text-align: center;'>PSD个数n有效范围:0~10(1字节)</td></tr><tr><td style='text-align: center;'>PSD(1)ID:4字节</td></tr><tr><td style='text-align: center;'>PSD(1)状态:1字节开门:0x55;关门:0xAA;</td></tr></table>

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="3">说明</td></tr><tr><td rowspan="15">信息单元状态</td><td rowspan="15">变长字节</td><td rowspan="15">列车在本ZC管辖范围内的MA信息(变长)c</td><td style='text-align: center;'>PSD信息(变长):MA覆盖范围内所有PSD的信息</td><td style='text-align: center;'>互锁解除:0xCG;其他:非法。若ZC无互锁解除功能,则互锁解除认为“关门”</td></tr><tr><td rowspan="3">安全信息</td><td style='text-align: center;'>PSD(2)ID:4字节</td></tr><tr><td style='text-align: center;'>PSD(2)状态:1字节</td></tr><tr><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>ESB信息(变长):MA覆盖范围内所有ESB的信息</td><td style='text-align: center;'>ESB个数n有效范围:0~10(1字节)</td></tr><tr><td rowspan="5">安全信息</td><td style='text-align: center;'>ESB(1)ID:4字节</td></tr><tr><td style='text-align: center;'>ESB(1)状态:1字节按下:0x55;未按下:0xAA;其他:非法</td></tr><tr><td style='text-align: center;'>ESB(2)ID:(4字节)</td></tr><tr><td style='text-align: center;'>ESB(2)状态:(1字节)</td></tr><tr><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>无人折返按钮状态(1字节)非安全信息</td><td style='text-align: center;'>无人折返按钮状态(列车停靠无人折返站台时方可发送按下):(1字节)按下:0x55;未按下:0xAA(默认值)</td></tr><tr><td style='text-align: center;'>临时限速信息(变长):MA覆盖范围内所有临时限速的信息</td><td style='text-align: center;'>临时限速信息个数n:有效范围:0~10(1字节)</td></tr><tr><td rowspan="3">安全信息</td><td style='text-align: center;'>临时限速信息个数n:有效范围:0~10(1字节)</td></tr><tr><td style='text-align: center;'>临时限速信息个数n:有效范围:0~10(1字节)</td></tr><tr><td style='text-align: center;'>临时限速信息个数n:有效范围:0x0~0xFFFFFFF(4字节)</td></tr></table>

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="4">说明</td></tr><tr><td rowspan="3">信息单元状态</td><td rowspan="3">变长字节</td><td rowspan="3">列车在本ZC管辖范围内的M5信息(变长)</td><td rowspan="2">临时限速信息(变长):MA覆盖范围内所有临时限速的信息安全信息</td><td style='text-align: center;'>临时限速(1)信息</td><td style='text-align: center;'>终端轨道区段ID(4字节)终端轨道区段内偏移量:单位:cm有效范围:0x0~0xFFFFFE(4字节)预留(1字节)临时限速值(1字节):单位:km/h有效范围:0~2540xFF:无临时限速</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>临时限速(n)信息</td></tr><tr><td style='text-align: center;'>运载目的地属性信息</td><td colspan="2">MA终端处目的地属性:通过:0x55;抓取:0xAA;回放:0xCC;默认值:0xFF。若ZC无相关功能,则发送默认值。若ATP无相关功能,则接收此信息时不进行处理。非安全信息</td></tr><tr><td colspan="6">注:对于移交ZC,当移交列车最大安全前端在ZC重叠区移交ZC的管辖区内,且MA达到边界点时开始针对该边界点发送列车移交状态,并在移交列车最小安全后端离开移交ZC的管辖范围(越过ZC边界)后停止发送该列车的移交状态。对于接管ZC,当正在移交的列车最大安全前端或者最小安全后端在相邻ZC重叠区,接管ZC针对该边界点发送的“移交状态信息”包中的“移交列车VID”应包含该列车。如果接管ZC为该车计算的MA可进入接管ZC,则接管ZC发送该边界点允许该移交列车驶入;否则,接管ZC发送该边界点不允许该移交列车驶入。当接管ZC向移交ZC发送禁止驶入时,移交ZC应限制列车MA越过边界点。</td></tr></table>

---

移交 ZC 应限制向列车发送的 MA 信息在接管 ZC 向移交 ZC 发送的移动授权范围之内。

具体移交流程如下：



a）移交 ZC 未收到接管 ZC 发送的允许越过移交边界的 MA（“列车移交接管状态”字段取值为“列车接管”，且“MA 是否有效”字段取值为“本车有在本 ZC 管辖范围内的 MA”）前，应不允许 MA 越过移交边界。

b) 移交 ZC 根据接管 ZC 发送的站场信息按照自身逻辑判断 MA 是否到达移交边界。

c) 移交 ZC 判断 MA 到达移交边界后，向接管 ZC 发起请求（“列车移交接管状态”字段填写“列车移交”），并向接管 ZC 发送该车在自身管辖范围内的 MA 信息（终点为边界点，不能有安全余量）。

d）接管 ZC 计算移交列车在自身管辖范围内的 MA：

1) 若接管 ZC 判断 MA 可进入自身管辖范围，则应向移交 ZC 发送该车在自身管辖范围内的 MA 信息（“列车移交接管状态”字段取值为“列车接管”，且“MA 是否有效”字段取值为“本车有在本 ZC 管辖范围内的 MA”，MA 起点从边界点开始），且将自身管辖范围内的 MA 与移交 ZC 发送的 MA 信息拼接，并向 VOBC 发送。接管 ZC 应保证向移交 ZC 发送的自身管辖范围内的 MA 供移交 ZC 拼接后，不超出 MA 内设备最大数量的限制。

2) 若接管 ZC 判断 MA 无法进入自身管辖范围，则向移交 ZC 发送禁止进入的移交状态（“列车移交接管状态”字段取值为“禁止驶入”，且“MA 是否有效”字段取值为“本车无在本 ZC 管辖范围内的 MA”），并向 VOBC 发送特殊控制命令。

e)

1) 若移交 ZC 未收到接管 ZC 发送的可进入接管 ZC 管辖范围的 MA 信息，则移交 ZC 应向 VOBC 发送自身管辖范围内的 MA。

2) 若移交 ZC 收到接管 ZC 发送的可进入接管 ZC 管辖范围的 MA 信息，则移交 ZC 应将自身管辖范围内的 MA 与接管 ZC 发送的 MA 信息拼接，并向 VOBC 发送。移交 ZC 拼接接管 ZC 发送的 MA 时，若判断拼接后 MA 内设备最大数量已突破限制，则不采信接管 ZC 发送的 MA，将 MA 终点置为移交边界，并重新启动上述移交流程。

正常移交的流程示例参见附录 A。

1. 本注释中，近端指列车靠近边界点的端，远端指列车远离边界点的端。

2. 以边界点为单位，移交 ZC 与接管 ZC 交互后按实装车。



2. 以边界点为单位，移交 ZC 与接管 ZC 交互指定范围内距离边界点最近的列车 ID 及距离。指定范围应满足：

---

# 表 6 移交状态信息(续)

1) 不小于具体工程约定的信号机接近距离；

2) 以物理区段边界点为边界。

3. ZC 查找列车从边界点开始，沿远离边界点的方向顺序查找，遇道岔区段时，若道岔非四开，则按照道岔开向查找，若道岔四开，则可停止继续查找（该四开道岔属于查找范围）或沿道岔可能开向继续查找。

4. 若通信列车安全包络跨压分界点，则该通信列车视为最接近该边界点的列车。

5. 若接近列车为通信车，则“接近列车 ID”字段填写该通信车 ID，“接近列车运行等级”、“接近列车车载 ATP 当前模式”字段填写该通信车 VOBC 发送的“列车运行控制级别”、“列车驾驶模式”信息。

1) 若列车安全包络未跨压边界点，则“接近列车距离”字段填写该通信车列车安全包络的近端到边界点的距离；

2) 若列车安全包络跨压边界点，则“接近列车距离”字段填写 0。

6. 若接近列车为非通信车，则“接近列车ID”字段填写非通信车默认ID，“接近列车运行等级”、“接近列车车载ATP当前模式”字段填写默认值，“接近列车距离”字段填写该非通信车可能占用的距离边界点最近的物理区段的近端距边界点的距离，该物理区段占用状态应为“占用”状态或有列车安全包络占用。

7. 若查找范围内无列车，则“接近列车ID”、“接近列车运行等级”、“接近列车车载ATP当前模式”、“接近列车距离”字段均填写默认值。

8. 对于移交 ZC 发送的“移交状态信息”包，若该边界点有移交列车（“移交列车 VID”字段取值不为默认值），则“移交列车 VID”字段取值应与“接近列车 ID”字段取值一致。

 $ ^{b} $ 1. ZC 每次生成停车保证请求时，应更新停车保证请求序列号，无停车保证请求时，停车保证请求序列号应为默认值。

2. 发送方 ZC 应保证：若 MA 有效，则停车保证请求对应位置应为 MA 终点位置；若 MA 无效，则停车保证请求对应点为边界点。

3. 移交 ZC 应保证：接管 ZC 发送停车保证请求时可直接采用移交 ZC 发送的“移交列车 VID”作为停车保证请求对应的列车。

4. 停车保证的发起 ZC 应保证自身可区分不同的停车保证命令及响应。

5. VOBC 采信的 MA 中包含停车保证请求时，应向移交/接管 ZC 发送有效（能停下/不能停下）的停车保证响应（即使不使用该 ZC 的 MA），该停车保证响应的位置应与所采信的 MA 中的停车保证请求中的位置一致。

6. 移交 ZC 收到 VOBC 发送的停车保证响应后，向接管 ZC 转发。

7. 接管 ZC 向移交 ZC 发送停车保证请求时，若对应停车保证请求进路的列车安全包络完全位于接管 ZC 范围内，则接管 ZC 应不向移交 ZC 发送该请求。

---

<div style="text-align: center;">表 6 移交状态信息(续)</div>


1. 当无列车处于移交过程中，或有列车处于移交过程，但发送方 ZC 判断该列车无在本 ZC 管辖范围内的 MA 时，“MA 是否有效”字段取值为：0xAA（本车无在本 ZC 管辖范围内的 MA）。

2. 若“MA 是否有效”字段取值为：0xAA（本车无在本 ZC 管辖范围内的 MA），则后续“列车在本 ZC 管辖范围内的 MA 信息”字段应不填写。

3. 移交 ZC 向接管 ZC 发送的自身管辖范围内的 MA 信息，安全防护点应为移交边界（无安全余量）；接管 ZC 向移交 ZC 发送的自身管辖范围内的 MA 信息，起点应为移交边界。

4. 接管 ZC 不允许 MA 进入接管 ZC 管辖范围时，移交 ZC 向 VOBC 发送的 MA 若到达 ZC 边界，则应使用移交 ZC 管辖范围内的轨道区段描述。

5. 对于发送方 ZC，“列车在本 ZC 管辖范围内的 MA 信息”里属于重叠区本 ZC 管辖范围内的道岔状态应与道岔状态信息包中相应道岔状态一致。

6. 对于主进路在移交 ZC 管辖区内，保护区段在接管 ZC 管辖区内，保护区段有效，接管 ZC 判断自身管辖范围内对移交列车来说仅有保护区段可用的场景下，移交流程如下：

1) 移交 ZC 判断 MA 到达移交边界时，未收到接管 ZC 发送的可进入接管 ZC 管辖范围的 MA 信息之前，向接管 ZC 发送的“移交状态信息”包中的 MA 信息中，障碍点为默认值，安全防护点为移交边界点，保护区段有效性为“无效”或“默认值”；向 VOBC 发送的列车控制信息中，障碍点为默认值，保护区段有效性为“无效”或“默认值”。

2) 接管 ZC 接收到移交 ZC 发送的移交请求之后，向移交 ZC 发送的“移交状态信息”包中的 MA 信息中，障碍点、起点位置均为移交边界点，安全防护点位置应确保列车可正常进站停车，同时应确保安全性，保护区段有效性为“有效”；向 VOBC 发送的列车控制信息中，障碍点为移交边界点，安全防护点位置与向移交 ZC 发送的安全防护点位置相同，保护区段有效性为“有效”。

3) 移交 ZC 接受到接管 ZC 发送的可进入接管 ZC 管辖范围的 MA 信息后进行拼接，拼接后发给 VOBC 的 MA 障碍点为移交边界点，安全防护点位置为接管 ZC 发送的安全防护点位置，保护区段有效性为“有效”；发给接管 ZC 的 MA 信息中，障碍点为默认值、安全防护点为移交边界，保护区段有效性为“无效”或“默认值”。

#### 5.4.5 移交列车信息

移交列车信息包用于列车相关的功能，ZC 将所有最大安全前端或最小安全后端位于重叠区本管辖区范围的列车（含非 CBTC 列车）的信息发送给相邻 ZC。该信息包格式见表 7。

---

<div style="text-align: center;">表 7 移交列车信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的信息单元数量</td><td style='text-align: center;'>1字节</td><td style='text-align: center;'>配置重叠区本ZC管辖范围内控制列车数量n，有效范围：0~30。
安全信息</td></tr><tr><td rowspan="6">信息单元状态</td><td rowspan="6">n×85字节</td><td style='text-align: center;'>移交列车VID(4字节)
安全信息</td></tr><tr><td style='text-align: center;'>列车运行方向(1字节)：
最小安全后端指向最大安全前端的方向，以最小安全后端处的上下行定义确定。
上行：0x55
下行：0xA1
其他：非法。
安全信息</td></tr><tr><td style='text-align: center;'>激活端(1字节)：
本V0BC是否为激活端(首尾冗余的V0BC统一发送是激活端。
激活端0x55；
非激活端0xAA；
其他：非法。
安全信息</td></tr><tr><td style='text-align: center;'>列车消息序列号(4字节)：
ZC实际接收到的车载ATP发送的列车消息序列号。
安全信息</td></tr><tr><td style='text-align: center;'>列车通信周期(2字节)
ZC实际接收到的车载ATP发送的列车通信周期。
安全信息</td></tr><tr><td style='text-align: center;'>列车最大安全前端位置(8字节)：
轨道区段ID(4字节)+所在区段偏移量(4字节)
偏移量单位：cm，有效范围：0x0~0xFFFFFFE；
安全信息</td></tr></table>

---

<div style="text-align: center;">表 7 移交列车信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="7">信息单元状态</td><td rowspan="7">n×85字节</td><td style='text-align: center;'>列车最小安全前端位置(8字节)*:轨道区段ID(4字节)+所在区段偏移量(4字节)偏移量单位:cm,有效范围:0x0~0xFFFFFFE;安全信息</td></tr><tr><td style='text-align: center;'>列车最大安全后端位置(8字节)*:轨道区段ID(4字节)+所在区段偏移量(4字节)偏移量单位:cm,有效范围:0x0~0xFFFFFFE;安全信息</td></tr><tr><td style='text-align: center;'>列车最小安全后端位置(8字节)*:轨道区段ID(4字节)+所在区段偏移量(4字节)偏移量单位:cm,有效范围:0x0~0xFFFFFFE;安全信息</td></tr><tr><td style='text-align: center;'>受控ZC ID(4字节):ZC间转发V0BC向ZC发送的“受控ZC ID”。安全信息</td></tr><tr><td style='text-align: center;'>本ZC记录的与车载的通信状态(2字节):ZC判断V0BC与ZC之间通信的延迟时间,单位:ms,有效范围:0~10 000;安全信息</td></tr><tr><td style='text-align: center;'>列车停准停稳信息(1字节):0x55:停准且停稳;0xAA:未停稳;0xCC:停稳但未停准;其他:非法。安全信息</td></tr><tr><td style='text-align: center;'>紧急制动状态(1字节):无紧急制动:0x55;有紧急制动:0xAA;其他:非法。非安全信息</td></tr></table>

---

<div style="text-align: center;">表 7 移交列车信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="6">信息单元状态</td><td rowspan="6">n×85字节</td><td style='text-align: center;'>列车运行等级(1字节):
0x01:CBTC;
0x02:点式;
0x03:联锁级;
其他:非法。
安全信息</td></tr><tr><td style='text-align: center;'>车载ATP当前模式(1字节):
0x01:AM模式;
0x02:CM模式;
0x03:RM模式;
0x04:FUM模式;
其他:非法。
安全信息</td></tr><tr><td style='text-align: center;'>列车折返状态(1字节):
0x55:AR状态;
0xAA:非AR状态;
其他:非法。
非安全信息</td></tr><tr><td style='text-align: center;'>列车完整性(1字节):
完整:0x55;
不完整:0xAA;
其他:非法。
安全信息</td></tr><tr><td style='text-align: center;'>列车长度(2字节):
单位:cm,高字节在前,低字节在后,有效范围:1 000~50 000。
安全信息</td></tr><tr><td style='text-align: center;'>列车悬垂长度(2字节)(列车车钩到第一轮对的距离):
单位:cm,高字节在前,低字节在后,有效范围:1~1 000。
安全信息</td></tr></table>

---

<div style="text-align: center;">表 7 移交列车信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="7">信息单元状态</td><td rowspan="7">n×85字节</td><td style='text-align: center;'>停车保证响应序列号(4字节) b:有效范围:1~(231-1)。默认值:0xFFFFFFF。安全信息</td></tr><tr><td style='text-align: center;'>停车保证对应安全防护点轨道区段ID(4字节) b:默认值:0x00000000。安全信息</td></tr><tr><td style='text-align: center;'>停车保证对应安全防护点轨道区段偏移量(4字节) b:单位:cm,有效范围:0x0~0xFFFFFFF;默认值:0xFFFFFFF。安全信息</td></tr><tr><td style='text-align: center;'>停车保证对应障碍点轨道区段ID(4字节) b:默认值:0x00000000。安全信息</td></tr><tr><td style='text-align: center;'>停车保证对应障碍点轨道区段偏移量(4字节) b:单位:cm,有效范围:0x0~0xFFFFFFF;默认值:0xFFFFFFF。安全信息</td></tr><tr><td style='text-align: center;'>停车保证对应保护区段有效性(1字节) b:有效:0x55;无效:0xAA;默认值:0xFF。安全信息</td></tr><tr><td style='text-align: center;'>速度方向(1字节):ZC接收的V0BC发送的速度方向0x55:车轮正转;0xAA:车轮反转;其他:非法。安全信息</td></tr></table>

---

<div style="text-align: center;">表 7 移交列车信息(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td colspan="8">说明</td></tr><tr><td rowspan="3">信息单元状态</td><td rowspan="3">n×85字节</td><td colspan="8">列车速度信息(2字节):单位:cm/s,有效范围:0~15 000;安全信息</td></tr><tr><td style='text-align: center;'>B7</td><td style='text-align: center;'>B6</td><td style='text-align: center;'>B5</td><td style='text-align: center;'>B4</td><td style='text-align: center;'>B3</td><td style='text-align: center;'>B2</td><td style='text-align: center;'>B1</td><td style='text-align: center;'>B0</td></tr><tr><td colspan="7">停车保证:00b:无法停车;01b:可以停车;11b:默认值(当列车未回复有效停车保证(含可以停车、无法停车、默认值)时,填写默认值);其他:非法(依据业主需求确定本字段,若业主不需要,则本字段为预留字段,填写00b)安全信息</td><td style='text-align: center;'>(预留)</td></tr></table>

---

2. 对于发送方 ZC，列车位置信息体现的道岔状态应与轨道区段列车排序信息包中“轨道区段 x 列车排序信息”体现的相应道岔状态，以及道岔状态信息包中相应道岔状态一致。

 $ ^{b} $ 1. 参考《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第2部分：CBTC系统车地连续通信协议》中“VOBC-ZC报文规范”中的相关内容。

2. 接管 ZC 收到移交 ZC 发送的停车保证响应时，应判断停车保证响应序列号与自身发送的停车保证请求信息一致，且停车保证响应对应位置满足：

1) 位于移交 ZC 管辖范围内；

2) 位于接管 ZC 管辖范围内，或与自身发送的停车保证请求信息一致时，方可采信停车保证响应。

列车头筛是指：ZC 判断列车前方是否存在其他隐藏列车。若列车完成头筛，则列车前方无其他隐藏列车。

 $ ^{4} $ 列车尾筛是指：ZC 判断列车后方是否存在其他隐藏列车。若列车完成尾筛，则列车后方无其他隐藏列车。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//73e2a644-737b-48fa-b73d-d0f873397355/markdown_0/imgs/img_in_image_box_95_626_795_880.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A06Z%2F-1%2F%2F2a63a50c456569d485966e5001fecb77f13a365c7d23ce0e5fd1a15b8d4318cd" alt="Image" width="83%" /></div>


<div style="text-align: center;">图 4 列车安全位置示意图</div>


#### 5.4.6 城市自定义包

自定义信息，用于实现各城市特有的互联互通相关功能。该信息包格式见表8，具体内容在工程中根据实际需求约定，各厂商均应实现相应功能。

---

<div style="text-align: center;">表 8 城市自定义包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容在工程中约定</td></tr></table>

#### 5.4.7 厂商自定义包

自定义信息，用于实现各厂商特有功能。该信息包格式见表9，各厂商分别定制，ZC判断通信ZC与自身属于同一厂商时，方可发送厂商自定义包。

<div style="text-align: center;">表 9 厂商自定义包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>信息定义</td><td style='text-align: center;'>N</td><td style='text-align: center;'>具体内容由各厂商分别定制</td></tr></table>

#### 5.4.8 站场信息延时包

用于表明本 GAL 包内站场信息的最大已存在时间，该信息包格式见表 10。站场信息的最大已存在时间指来自 CI 的站场信息在发送方 ZC 发出该信息前已存在的时间。

涉及站场信息包括：道岔状态信息包、物理区段状态信息包、移交状态信息包中的距边界点最近的列车信息、轨道区段列车排序信息包。

ZC 判断相邻 ZC 发送的 GAL 包中站场信息是否可用时，应考虑站场信息已存在时间。

<div style="text-align: center;">表 10 站场信息延时包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>接口内容</td><td style='text-align: center;'>字节长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>站场信息已存在时间安全信息</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>本 GAL 包内站场信息的最大已存在时间，单位：ms。有效范围：1~10 000；默认值：0xFFFF。ZC 判断与 CI 通信中断时，填写默认值</td></tr></table>

#### 5.4.9 轨道区段列车排序信息

本 ZC 应将配置重叠区内本 ZC 管辖范围内所有轨道区段上的列车

---

顺序信息发送给邻站 ZC，列车排序信息见表 11。相邻 ZC 间轨道区段索引顺序应保持一致。

<div style="text-align: center;">表 11 轨道区段列车排序信息</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>字段</td><td style='text-align: center;'>长度</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>包含的轨道区段数量</td><td style='text-align: center;'>2字节</td><td style='text-align: center;'>配置重叠区本ZC管辖范围内轨道区段数量n，有效范围：1~256。安全信息</td></tr><tr><td rowspan="4">轨道区段1列车排序信息</td><td rowspan="4">变长</td><td style='text-align: center;'>轨道区段1内列车数量（1字节）：表明此轨道区段列车顺序中的列车数量a，有效范围：0~20。安全信息</td></tr><tr><td style='text-align: center;'>列车（1）ID（4字节）：列车顺序中第一列车的ID，若为通信车，则取值为该车的VID，若为非通信车（含ZC无法判断的隐藏列车），则取值为非通信车默认ID：0xFFFFFFF。安全信息</td></tr><tr><td style='text-align: center;'>......</td></tr><tr><td style='text-align: center;'>列车（a）ID（4字节）安全信息</td></tr><tr><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td></tr><tr><td style='text-align: center;'>轨道区段n列车排序信息</td><td style='text-align: center;'>变长</td><td style='text-align: center;'>同“轨道区段1列车排序信息”定义。安全信息</td></tr><tr><td colspan="3">注：轨道区段内列车排序原则为：a）通信列车排序按照V0BC发送的原始位置报告进行；b）若发送方ZC发送的轨道区段上无列车序列，且在“物理区段状态信息”包中，该轨道区段所在物理区段的“物理区段占用状态”取值为“占用”，则发送方ZC应保证该轨道区段上无非通信车；c）轨道区段上的列车应按照从边界点向远离边界点的方向排序；d）轨道区段内相邻的非通信车可合并为一列非通信车。</td></tr></table>

---

## 附录 A

(规范性附录)

列车控制权切换正常流程示例及列车移交相关原则

### A.1 列车控制权切换正常流程示例

列车控制权切换的正常流程示例如图 A.1 所示，其中 ZC1 为移交 ZC，ZC2 为接管 ZC。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6f53c83c-c284-4aa5-a75a-2fbba6f40e26/markdown_0/imgs/img_in_image_box_44_434_746_1101.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A16Z%2F-1%2F%2F10da28d4693b053cd74b67d1ca800eecc8ce5818fb2bd31b73a614d8050b9648" alt="Image" width="83%" /></div>


<div style="text-align: center;">图 A.1 列车控制权切换流程示例</div>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//352711f6-9ea2-4564-a8e4-3f57c302fe81/markdown_0/imgs/img_in_image_box_87_133_792_957.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A19Z%2F-1%2F%2Fee50bd0cd8068d4a0f238cbb51bf5df12ad4196a9a951309f225dab6d65fde2e" alt="Image" width="83%" /></div>


<div style="text-align: center;">图 A.1 列车控制权切换流程示例（续）</div>


a）前置条件：

1）设置 ZC1 和 ZC2 管辖边界及重叠区域；

---

2）各 ZC 将重叠区域属于各自管辖的物理区段、道岔等站场信息周期互传；

3）各 ZC 将包络处于重叠区域内的列车位置报告等列车信息周期互传；

4）各 ZC 将边界点的移交状态等信息周期互传；

5）两个相邻 ZC 的同一个边界点同时只能由一列车处于控制权切换流程，追踪列车应顺序进行控制权切换。



## b）正常移交流程：

步骤1：列车1安全包络未进入ZC1重叠区范围，仅与ZC1建立通信，移交流程未启动。列车1完全受ZC1的控制，使用ZC1发送的MA运行。

步骤2：列车1的最大安全前端进入ZC1重叠区范围，仅与ZC1建立通信，移交流程未启动。

步骤3：列车1的安全包络完全进入ZC1重叠区范围后，列车1注册ZC2，同时与ZC1和ZC2建立通信，此时移动授权终点还未达到移交边界，移交流程未启动。

步骤4：ZC1为列车1计算的移动授权终点到达移交边界，移交流程启动。ZC1向ZC2发送的移交列车信息包含列车1，“移交状态信息”包中的“移交列车VID”为列车1的VID。

步骤5：ZC2收到ZC1的移交状态信息中包含列车1的“列车移交”状态，则ZC2为列车1计算移动授权，若移动授权可延伸进入ZC2管辖范围，ZC2向ZC1发送的“列车移交接管状态”为“列车接管”，ZC1将列车1的移动授权延伸进入ZC2管辖范围，最远不能越过ZC2计算的移动授权终点。

步骤6：列车1向前运行，最大安全前端驶出ZC1管辖范围，ZC1和ZC2互发列车1的移交状态信息和移交列车信息，并均向列车1发送移动授权。列车1根据自身位置判断使用的移动授权。

步骤 7: 列车 1 安全包络驶过移交边界, 完全驶出 ZC1 管辖范围后, 列车 1 断开与 ZC1 的通信。ZC2 向 ZC1 发送的移交列车信息中包含列

---

车 1, ZC1 和 ZC2 相互发送的“移交状态信息”包中“移交列车 VID”均不包含列车 1。至此，列车 1 完成控制权由 ZC1 向 ZC2 的切换。

步骤8：列车2在列车1后方，在列车1完成移交后，列车2执行切换流程，重复步骤1～步骤7。ZC2向ZC1发送列车1的移交列车信息，ZC1向列车2发送的移动授权终点应与列车1的车尾保持安全距离。

### A.2 ZC 重叠区边界列车安全包络处理方案

#### A.2.1 概述

列车移交过程中，ZC 需在“移交列车信息”包中向相邻 ZC 发送列车位置信息。列车位置信息以列车安全包络描述，列车安全包络示意如图 A.2 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0fc997d1-fa28-44d5-ba73-6e9b3345f2ce/markdown_0/imgs/img_in_image_box_73_513_791_795.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A26Z%2F-1%2F%2Ff5214a6bd5809e54ffcc73e70da46c477699a7e67db0b962996d98848e9d6834" alt="Image" width="85%" /></div>


<div style="text-align: center;">图 A.2 列车安全包络示意图</div>


ZC 向相邻 ZC 发送的“移交列车信息”包中，涉及列车安全包络的信息包括：列车最大安全前端位置、列车最小安全前端位置、列车最大安全后端位置、列车最小安全后端位置、列车长度。

ZC 向相邻 ZC 发送列车的“移交状态信息”包的条件为：ZC 判断该列车最大安全前端或最小安全后端在 ZC 重叠区本 ZC 管辖范围内。

---

特殊场景如下：

a) 对移交 ZC, 列车最大安全前端刚进入 ZC 重叠区本 ZC 管辖范围, 最小安全后端还在 ZC 重叠区本 ZC 管辖范围之外;

b) 对移交 ZC，列车最大安全前端已越过移交边界，离开 ZC 重叠区本 ZC 管辖范围，最小安全后端还在 ZC 重叠区本 ZC 管辖范围之内；

c) 对接管 ZC，列车最大安全前端刚越过移交边界，进入 ZC 重叠区本 ZC 管辖范围，最小安全后端还未进入 ZC 重叠区本 ZC 管辖范围；

d）对接管 ZC，列车最大安全前端已离开 ZC 重叠区本 ZC 管辖范围，最小安全后端已离开 ZC 重叠区本 ZC 管辖范围之内。

上述特殊场景，均存在ZC向相邻ZC发送的“移交列车信息”包中，列车安全包络不完全位于ZC重叠区内本ZC管辖范围内的情况。

对于场景 b)、c)、列车安全包络完全位于 ZC 重叠区内（通过重叠区设置原则可保证），由 Z 相邻 Z6 均有 ZC 重叠区内线路地图，故 ZC 可确定列车安全包络位置对开场景 a)、d)，列车安全包络不完全位于 ZC 重叠区内，相邻 ZC 无该部分线路地图，故无法确定列车安全包络位置。故此，针对场景 a)、d)，ZC 发送信息“包线信息”包时，需对列车安全包络相关信息进行特殊处理，使相邻 ZC 获得列车安全包络完全处于 ZC 重叠区内。

#### A.2.2 场景名词定义

A.2.1 中场景 a)、d) 以边界点为中心对称，故分析时将两种场景合并为列车安全包络跨 ZC 重叠区边界的场景统一描述。

场景中基本定义如下,如图 A.3 所示:

近端、远端：以 ZC 移交边界为基准，向 ZC 内部计算，靠近 ZC 移交边界的列车端为近端，远离 ZC 移交边界的列车端为远端；

近侧、远侧：以某点为基准，该点靠近 ZC 移交边界的一侧为该点的近侧，远离 ZC 移交边界的一侧为该点的远侧。

在此基础上，场景中的名称与具体场景的对应见表A.1。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c2be2922-0061-48ef-b068-aa3fe5d6e34a/markdown_0/imgs/img_in_image_box_89_148_780_461.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A33Z%2F-1%2F%2Fd5eeaf37770610bed228b7318899c9e677658ab3f6b417e8426caf49e4838779" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 A.3 场景名词定义</div>


<div style="text-align: center;">表 A.1 场景对照表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>移交 ZC</td><td style='text-align: center;'>接管 ZC</td></tr><tr><td style='text-align: center;'>近端近侧包络</td><td style='text-align: center;'>列车最大安全前端</td><td style='text-align: center;'>列车最小安全后端</td></tr><tr><td style='text-align: center;'>近端远侧包络</td><td style='text-align: center;'>列车最小安全前端</td><td style='text-align: center;'>列车最大安全后端</td></tr><tr><td style='text-align: center;'>远端近侧包络</td><td style='text-align: center;'>列车最大安全后端</td><td style='text-align: center;'>列车最小安全前端</td></tr><tr><td style='text-align: center;'>远端远侧包络</td><td style='text-align: center;'>列车最小安全后端</td><td style='text-align: center;'>列车最大安全前端</td></tr><tr><td style='text-align: center;'>列车安全包络：近端近侧包络到远端远侧包络范围</td><td style='text-align: center;'>列车最大安全前端到列车最小安全后端范围</td><td style='text-align: center;'>列车最大安全前端到列车最小安全后端范围</td></tr></table>

真实 X(X 为表中名称,例如近端近侧包络等):指 ZC 收到的 VOBC 发送的 X,或 ZC 根据 VOBC 发送的信息计算所得的 X;

处理后 X: 指 ZC 经过处理, 向相邻 ZC 发送的 X, 或根据 ZC 处理后信息计算所得的 X。

注：下文中均基于此节定义进行描述。

#### A.2.3 处理方案

对“移交列车信息”包中列车安全包络相关信息的处理方案为：

a）ZC 判断 ZC 重叠区边界在真实列车安全包络范围内（含与近端近侧包络、远端远侧包络位置相同的情况）时，向相邻 ZC 发送

---

“移交列车信息”时，对列车安全包络相关信息进行处理。

b）处理后发送信息见表 A.2。

<div style="text-align: center;">表 A.2 列车包络相关信息处理对照表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>名称</td><td style='text-align: center;'>计算结果</td></tr><tr><td style='text-align: center;'>近端近侧包络</td><td style='text-align: center;'>真实近端近侧包络</td></tr><tr><td style='text-align: center;'>近端远侧包络</td><td style='text-align: center;'>真实近端近侧包络</td></tr><tr><td style='text-align: center;'>远端近侧包络</td><td style='text-align: center;'>ZC重叠区边界</td></tr><tr><td style='text-align: center;'>远端远侧包络</td><td style='text-align: center;'>ZC重叠区边界</td></tr></table>

c）发送方 ZC 不对 VOBC 发送的“列车长度”字段进行修改。

d）接收方 ZC 应采信发送方 ZC 发送的列车远端远侧包络、远端近侧包络、近端远侧包络、近端近侧包络。

e）接收方 ZC 收到发送方 ZC 发送的列车远端远侧包络为 ZC 重叠区边界位置时，不应将“列车长度”字段与列车安全包络相关信息进行校验。

f) 接收方 ZC 应允许通过发送方 ZC 发送的列车位置计算所得的列车测距误差小于真实列车的测距误差，最小值允许为 0。

### A.3 重叠区划分原则

为实现装备不同信号厂家车载设备的列车在互联互通线路上的跨线切换，本规范将定义 ZC 切换重叠区，用于实现线间的 ZC 切换。

#### A. 3.1 ZC 边界

设计人员在设置 ZC 边界时，应遵循如下原则：

a）ZC 边界应设置在计轴点，且与联锁边界相同；

b）ZC 边界不应设置在折返区段中间（不含折返区段边界）；

c）ZC 边界不应设置在站台区段中间（不含站台区段边界）；

d）ZC 边界应设置实体信号机或虚拟信号机；

e）ZC 系统及 ZC-ZC 通信接口规范（线间）应支持相邻 ZC 间设置有多个 ZC 边界。

#### A. 3.2 ZC 切换重叠区

设计人员在定义 ZC 切换重叠区时，应遵循如下原则：

---

a）每个ZC边界的上行方向和下行方向，ZC系统应分别定义ZC切换重叠区，并在电子地图中分别定义。

b）ZC 切换重叠区的设置应保证列车通过 ZC 边界时不减速运行，具体长度应在工程阶段确定。

c）ZC 重叠区移交 ZC 管辖范围应至少包括接管 ZC 管辖范围内第一条进路的接近区段。

d）移交重叠区范围应保证最不利情况下，列车不会在 ZC 超时时间内由移交重叠区外越过移交 ZC 边界进入接管 ZC。

e）重叠区内计轴长度不得小于列车最大回退距离+外悬的长度。

f) 重叠区内边界点处计轴区段长度不应小于“最大车速×（相邻ZC的延时+从车轧入计轴区段到本ZC将该计轴区段状态的占用信息传出的时间消耗）-最小车长+2×列车悬垂”。

g）ZC 切换重叠区的始端应为计轴点，距离 ZC 边界的长度应大于一定的距离，该取值应至少考虑接管 ZC 建立连接时间、列车常用制动距离。

以图 A.4 为例，移交 ZC 重叠区长度按公式 A.1 计算：

 $$ L_{ 移交 ZC 垂直区长度 }=L_{Train}+L_{Dis}+L_{ 常用制动 }+V_{max}\times T_{ 建立连接 } $$ 

式中：

 $ L_{Train} $ ——列车长度，单位为米（m）；

 $ L_{Dis} $  ——列车安全包络的最大误差，单位为米（m）；

 $ L_{常用制动} $ ——列车以最高运行速度至信号机的常用制动距离，单位为米（m）；

 $ V_{max} $ ——列车最高允许速度，单位为米每秒(m/s);

 $ T_{建立连接} $ ——列车与接管 ZC 建立连接时间，从列车开始连接接管 ZC 开始，到完成注册，移交 ZC 向列车发送的移动授权延伸至接管 ZC 管辖范围截止（典型值 12 s）。

列车常用制动距离按公式 A.2 计算：

 $$ L_{ 常用制动 }=(V_{max}^{2}-0^{2})/(2\times b_{ 常用减速度 }) $$ 

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fa2a8185-5cbf-4eab-a58e-8f80ba113db4/markdown_0/imgs/img_in_image_box_59_138_741_403.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A44Z%2F-1%2F%2F8cfe98c1efd4ba18af13bc75d442e62658e2d01f1fc3e2dd1412b504c7ec2054" alt="Image" width="81%" /></div>


<div style="text-align: center;">图 A.4 移交 ZC 重叠区</div>


式中：

 $ V_{max} $ ——列车最高允许速度单位为米每秒(m/s);

 $ b_{常用减速度} $  ——常用制动减速度，单位为米每二秒 $ (\mathrm{m}/\mathrm{s}^{2}) $ 。

对于互联互通线路由于列车长度、列车车辆参数等因素，各厂家应分别计算各自的  $ L_{移交ZC重叠区长度} $ ，然后取最大值作为实际的  $ L_{移交ZC重叠区长度} $ 。

h）重叠区的边界点与Z边界点之间至少包含两个计轴区段。

i) ZC 移交重叠区的典型设计如图 A.5 所示

ZCI 中控

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fa2a8185-5cbf-4eab-a58e-8f80ba113db4/markdown_0/imgs/img_in_image_box_64_742_734_1010.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A59%3A45Z%2F-1%2F%2F8f8c663ed319492adde0b08cbc8d4e8f7116701e64fc25eb11976996a530b932" alt="Image" width="79%" /></div>


<div style="text-align: center;">图 A.5 不同方向的重叠区</div>

---

中国城市轨道交通协会团体标准  

城市轨道交通 基于通信的列车运行  

控制系统（CBTC）互联互通接口规范  

第4部分：区域控制器（ZC）间接口  

T/CAMET 04011.4—2018

*

中国铁道出版社有限公司出版发行  

(100054, 北京市西城区右安门西街 8 号)  

公司网址：http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本：880 mm × 1230 mm 1/32 印张：1.5 字数：39 千  

2019 年 5 月第 1 版 2019 年 5 月第 1 次印刷

书号：15113·5731 定价：15.00元 版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>定价：15.00 元</th></tr></thead>
  <tbody>
  </tbody>
</table>