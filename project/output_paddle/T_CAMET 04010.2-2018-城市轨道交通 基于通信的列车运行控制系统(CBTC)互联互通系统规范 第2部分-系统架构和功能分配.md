# 中国城市轨道交通协会团体标准

T/CAMET 04010.2—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第2部分：系统架构和功能分配

# Urban rail transit — System specification for interoperability of communication based train control system Part 2: System architecture and functional allocations

2018-09-10 发布

2018-12-31 实施

---

## 目次

前言 …… VII    
引言 …… VIII    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 1    
3.1 术语 …… 2    
3.2 缩略语 …… 5    
4 系统架构 …… 5    
4.1 架构组成 …… 5    
4.2 CBTC 系统物理接口和功能接口 …… 5    
5 功能对照 …… 7    
6 ATP 功能分配 …… 10    
6.1 ATP 的主要功能 …… 10    
6.2 列车位置确定 …… 12    
6.3 移动防护限制和目标点的确定 …… 19    
6.4 ATP 曲线确定 …… 24    
6.5 确定限制速度 …… 27    
6.6 列车实际速度/列车运行方向确定 …… 28    
6.7 监督/强制允许速度和允许运行方向 …… 30    
6.8 车门/站台门控制 …… 33    
6.9 列车折返 …… 38    
6.10 车载 ATP 用户界面 …… 39    
6.11 自诊断、故障报警及数据记录 …… 40

---

7 ATO 功能分配 …… 40  
7.1 功能描述 …… 40  
7.2 确定 ATO 曲线 …… 40  
7.3 列车速度调整 …… 42  
7.4 门控制 …… 43  
7.5 车载 ATO 用户界面 …… 45  
7.6 自诊断、故障报警及数据记录 …… 45  
8 ATS 功能分配 …… 46  
8.1 功能描述 …… 46  
8.2 列车识别 …… 46  
8.3 列车追踪 …… 48  
8.4 列车进路办理 …… 48  
8.5 列车调整 …… 50  
8.6 列车运行控制 …… 51  
8.7 控制列车运行 …… 53  
8.8 时刻表编制 …… 53  
8.9 模拟培训 …… 53  
8.10 用户界面 …… 54  
9 CI 功能分配 …… 56  
9.1 功能描述 …… 56  
9.2 进路办理 …… 56  
9.3 锁闭/解锁进路/区段 …… 58  
9.4 紧急停车按钮 …… 59  
9.5 故障监测及操作记录 …… 59  
参考文献 …… 61

---

## 前言

T/CAMET 04010《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》分为以下四个部分：

——第1部分：系统总体要求；

——第2部分：系统架构和功能分配；

——第3部分：车载电子地图；

——第4部分：互联互通危害分析。

本部分是 T/CAMET 04010 的第 2 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京交通大学、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：郜春海、黄友能、王伟、刘波、李凯、王悉、刘宏杰、孙晓光、刘鲁鹏、吕浩炯、刘志水、尹逊政、孙旺、高晓菲、胡顺定。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》、《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》、《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》、《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范 第2部分:系统架构和功能分配

## 1 范围

T/CAMET 04010 的本部分定义了互联互通的系统架构和功能分配技术要求，包括互联互通下 OBTC 系统的物理接口和功能接口，以及 ATP、ATO、ATS、CI 各系统的功能分配。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

T/CAMET 04010.1—2018 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第1部分：系统总体要求

## 3 术语和缩略语

GB/T 12758—2004、GB 50157—2013、CJ/T 407—2012 和 T/CAMET

---

04010.1—2018界定的及下列术语和缩略语适用于本部分，为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

## 城市轨道交通信号 urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T 12758—2004, 术语与定义 3.1]

#### 3.1.2 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术，连续车一地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.3 

## 移动闭塞 moving block

前方列车与后续列车之间的最小安全追踪间隔距离单元不预定设定，并随列车的移动、速度的变化而变化的闭塞方式。

[GB/T 12758—2004 术语与定义 3.10]

#### 3.1.4 

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.37]

#### 3.1.5 

## 列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB 50157—2013,定义2.0.38]

---

#### 3.1.6 

## 列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB 50157—2013, 定义 2.0.39]

#### 3.1.7 

## 列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。 $$ GB 50157—2013, 定义 2.0.40 $$ 



#### 3.1.8 

## 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.9 

维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护

#### 3.1.10 

## 保护区段 overlap section

为实现超速防护，保证安全停车而延伸的闭塞区段。

[GB/T 12758—2004, 术语与定义 3.12]

#### 3.1.11 

目标速度 target speed

列车运行至前方目标地点应达到的允许速度。

[GB/T 12758—2004, 术语与定义 3.13]

#### 3.1.12 

## 目标距离 target distance

列车运行至前方目标地点的走行距离。

---

[GB/T 12758—2004, 术语与定义 3.14]

#### 3.1.13 

## 安全保护距离 safe protection distance

列车自动防护系统中，列车超速防护实施安全停车控制时，为防止停车位置离散性可能造成的危险，而设置的自预定停车位置至目标地点的安全距离。

[GB/T 12758—2004, 术语与定义 3.15]

#### 3.1.14 

## 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点。

[T/CAMET 04010.1, 术语和缩略语 3.1.10]

#### 3.1.15 

## 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可

[CJ/T 407—2012, 定义 3.1.7]

#### 3.1.16 

## 限制速度 restricted speed

线路、车辆结构等限制及列车移动授权所获取的最严格的速度限制。

[CJ/T 407—2012, 定义 3.1.11]

#### 3.1.17 

## 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通、安全可靠运营。

[T/CAMET 04010.1, 术语和缩略语 3.1.16]

#### 3.1.18 

## 共线运行 mix operation

装备不同厂家车载信号设备的列车可以在装备同一厂家轨旁信号设

---

备线路上支持以点式列车控制级别和连续式列车控制级别无缝安全可靠运营。

### 3.2 缩略语

AM:列车自动驾驶模式(Automatic Train Operating Mode)

ATC:列车自动控制(Automatic Train Control)

ATO:列车自动运行(Automatic Train Operation)

ATP:列车自动防护(Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

CBTC: 基于通信的列车控制系统（Communication Based Train Control）

CI: 计算机联锁 (Computer Interlocking)

CM:列车自动防护模式(Code Train Operating Mode)

DCS: 数据通信系统 (Data Communication System)

LEU: 轨旁电子单元(Lineside Electronic Unit)

MSS:维护支持子系统(Maintenance Support System)

RM:限制人工驾驶模式(Restricted Train Operating Mode)

SIL: 安全完整性等级 (Safety Integrity Level)

ZC: 区域控制器(Zone Controller)

## 4 系统架构

### 4.1 架构组成

CBTC 系统由 ATS、CBTC 轨旁（轨旁 CBTC 设备，含区域控制器等）、CBTC 车载（车载 CBTC 设备，含车载 ATP、车载 ATO 等）、CI、DCS 子系统组成。

### 4.2 CBTC 系统物理接口和功能接口

CBTC 系统物理接口和功能接口示意图见图 1, 互联互通下 CBTC 系统物理接口和功能接口示意图见图 2。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//3b48f4a1-350a-4553-9eef-5984de7e511f/markdown_0/imgs/img_in_image_box_126_124_768_649.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A16%3A00Z%2F-1%2F%2Fd78e3f1350ff17c020f54f4ddbec02427ab963d55887b53e85bcb7294c7bfc2d" alt="Image" width="76%" /></div>


<div style="text-align: center;">图 1 CBTC 系统物理接口和功能接口示意图</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//3b48f4a1-350a-4553-9eef-5984de7e511f/markdown_0/imgs/img_in_image_box_80_730_837_1088.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A16%3A00Z%2F-1%2F%2F5289eafcb8030e5af74cbfa61f9fef8e48a2ce768c0a29102183627f7fb342b1" alt="Image" width="89%" /></div>


<div style="text-align: center;">图 2 互联互通下 CBTC 系统物理接口和功能接口示意图</div>

---

相对于 CBTC 系统物理接口和功能接口，互联互通下 CBTC 系统物理接口和功能接口，增加了列车与邻线地面设备间的接口，以及各线间地面设备间的接口（CBTC 轨旁间及 CI 设备间）。

## 5 功能对照

功能分配与总体要求的对照内容见表1。

<div style="text-align: center;">表 1 功能对照表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>总体要求中的功能点名称</td><td style='text-align: center;'>对应本文章节</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>初始化CBTC列车位置</td><td style='text-align: center;'>6.2.2</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>确定CBTC列车位置</td><td style='text-align: center;'>6.2.3</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>确定轨道区段占用状态</td><td style='text-align: center;'>6.2.4</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>防护列车丢失位置报告</td><td style='text-align: center;'>6.2.5.2</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>防护列车完整性丢失</td><td style='text-align: center;'>6.2.5.3</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>确定前方CBTC列车位置</td><td style='text-align: center;'>6.3.2.2</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>确定前方安全进路限制</td><td style='text-align: center;'>6.3.2.3</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>确定移动授权</td><td style='text-align: center;'>6.3.3.2</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>确定目标点</td><td style='text-align: center;'>6.3.4.2</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>响应紧急停车按钮</td><td style='text-align: center;'>6.3.4.3</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>道岔状态防护</td><td style='text-align: center;'>6.3.4.4</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>车载故障处理</td><td style='text-align: center;'>6.3.5.2</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>固定速度限制防护</td><td style='text-align: center;'>6.4.2</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>临时限速限制防护</td><td style='text-align: center;'>6.4.3</td></tr></table>

---

<div style="text-align: center;">表 1 功能对照表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>总体要求中的功能点名称</td><td style='text-align: center;'>对应本文章节</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>确定制动曲线</td><td style='text-align: center;'>6.4.4</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>列车超速防护</td><td style='text-align: center;'>6.4.4.3</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>列车速度测定</td><td style='text-align: center;'>6.6.2</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>测速误差补偿</td><td style='text-align: center;'>6.6.2.3</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>零速状态确定</td><td style='text-align: center;'>6.6.2.4</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>列车运行方向确定</td><td style='text-align: center;'>6.6.3</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>列车运行方向防护</td><td style='text-align: center;'>6.7.3.2</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>退行防护</td><td style='text-align: center;'>6.7.3.3</td></tr><tr><td style='text-align: center;'>23</td><td style='text-align: center;'>越过移动授权终点防护</td><td style='text-align: center;'>6.7.4.1</td></tr><tr><td style='text-align: center;'>24</td><td style='text-align: center;'>移动授权更新超时防护</td><td style='text-align: center;'>6.7.4.3</td></tr><tr><td style='text-align: center;'>25</td><td style='text-align: center;'>紧急制动缓解</td><td style='text-align: center;'>6.7.4.4</td></tr><tr><td style='text-align: center;'>26</td><td style='text-align: center;'>车门允许</td><td style='text-align: center;'>6.8.2</td></tr><tr><td style='text-align: center;'>27</td><td style='text-align: center;'>站台门控制</td><td style='text-align: center;'>6.8.2.3</td></tr><tr><td style='text-align: center;'>28</td><td style='text-align: center;'>车门防护</td><td style='text-align: center;'>6.8.3.2</td></tr><tr><td style='text-align: center;'>29</td><td style='text-align: center;'>车门防护切除</td><td style='text-align: center;'>6.8.4.4</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'>站台门防护</td><td style='text-align: center;'>6.8.3</td></tr><tr><td style='text-align: center;'>31</td><td style='text-align: center;'>列车折返</td><td style='text-align: center;'>6.9</td></tr><tr><td style='text-align: center;'>32</td><td style='text-align: center;'>车载ATP界面功能</td><td style='text-align: center;'>6.10.1</td></tr><tr><td style='text-align: center;'>33</td><td style='text-align: center;'>ATP自诊断、故障报警及数据记录</td><td style='text-align: center;'>6.11</td></tr><tr><td style='text-align: center;'>34</td><td style='text-align: center;'>模式转换</td><td style='text-align: center;'>6.2.3.10</td></tr></table>

---

<div style="text-align: center;">表 1 功能对照表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>总体要求中的功能点名称</td><td style='text-align: center;'>对应本文章节</td></tr><tr><td style='text-align: center;'>35</td><td style='text-align: center;'>ZC间移交</td><td style='text-align: center;'>6.3.4.5</td></tr><tr><td style='text-align: center;'>36</td><td style='text-align: center;'>电子地图存储</td><td style='text-align: center;'>6.2.2.4</td></tr><tr><td style='text-align: center;'>37</td><td style='text-align: center;'>停稳停准判断</td><td style='text-align: center;'>6.2.3.8</td></tr><tr><td style='text-align: center;'>38</td><td style='text-align: center;'>确定ATO曲线</td><td style='text-align: center;'>7.2.1</td></tr><tr><td style='text-align: center;'>39</td><td style='text-align: center;'>精确停车</td><td style='text-align: center;'>7.2.2</td></tr><tr><td style='text-align: center;'>40</td><td style='text-align: center;'>根据ATO曲线调整列车速度</td><td style='text-align: center;'>7.3.1</td></tr><tr><td style='text-align: center;'>41</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>7.3.2</td></tr><tr><td style='text-align: center;'>42</td><td style='text-align: center;'>运营调整</td><td style='text-align: center;'>7.3.3</td></tr><tr><td style='text-align: center;'>43</td><td style='text-align: center;'>开关车</td><td style='text-align: center;'>7.3.4.1</td></tr><tr><td style='text-align: center;'>44</td><td style='text-align: center;'>ATO界面显示</td><td style='text-align: center;'>7.3.5</td></tr><tr><td style='text-align: center;'>45</td><td style='text-align: center;'>ATO自诊断、故障预警及数据记录</td><td style='text-align: center;'>7.3.6.2</td></tr><tr><td style='text-align: center;'>46</td><td style='text-align: center;'>ATO发送列车运行信息</td><td style='text-align: center;'>7.3.4</td></tr><tr><td style='text-align: center;'>47</td><td style='text-align: center;'>ATO发送旅客信息</td><td style='text-align: center;'>7.6.3</td></tr><tr><td style='text-align: center;'>48</td><td style='text-align: center;'>确定列车识别号</td><td style='text-align: center;'>8.2</td></tr><tr><td style='text-align: center;'>49</td><td style='text-align: center;'>ATS列车追踪</td><td style='text-align: center;'>8.3</td></tr><tr><td style='text-align: center;'>50</td><td style='text-align: center;'>列车进路办理</td><td style='text-align: center;'>8.4</td></tr><tr><td style='text-align: center;'>51</td><td style='text-align: center;'>列车自动调整</td><td style='text-align: center;'>8.5.1</td></tr><tr><td style='text-align: center;'>52</td><td style='text-align: center;'>节能运行</td><td style='text-align: center;'>8.5.2</td></tr><tr><td style='text-align: center;'>53</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>8.6.1</td></tr><tr><td style='text-align: center;'>54</td><td style='text-align: center;'>提前发车</td><td style='text-align: center;'>8.6.2</td></tr></table>

---

<div style="text-align: center;">表 1 功能对照表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>总体要求中的功能点名称</td><td style='text-align: center;'>对应本文章节</td></tr><tr><td style='text-align: center;'>55</td><td style='text-align: center;'>跳停</td><td style='text-align: center;'>8.6.3</td></tr><tr><td style='text-align: center;'>56</td><td style='text-align: center;'>设置/取消临时限速</td><td style='text-align: center;'>8.7</td></tr><tr><td style='text-align: center;'>57</td><td style='text-align: center;'>时刻表编制管理</td><td style='text-align: center;'>8.8</td></tr><tr><td style='text-align: center;'>58</td><td style='text-align: center;'>模拟培训</td><td style='text-align: center;'>8.9</td></tr><tr><td style='text-align: center;'>59</td><td style='text-align: center;'>ATS界面功能</td><td style='text-align: center;'>8.10.1</td></tr><tr><td style='text-align: center;'>60</td><td style='text-align: center;'>ATS数据记录</td><td style='text-align: center;'>8.10.2.4</td></tr><tr><td style='text-align: center;'>61</td><td style='text-align: center;'>中控/站控转换</td><td style='text-align: center;'>8.6.4</td></tr><tr><td style='text-align: center;'>62</td><td style='text-align: center;'>进路办理</td><td style='text-align: center;'>9.2.2</td></tr><tr><td style='text-align: center;'>63</td><td style='text-align: center;'>保护区段建立</td><td style='text-align: center;'>9.2.4</td></tr><tr><td style='text-align: center;'>64</td><td style='text-align: center;'>进路/区段锁闭</td><td style='text-align: center;'>9.3.2</td></tr><tr><td style='text-align: center;'>65</td><td style='text-align: center;'>道岔单操、单锁</td><td style='text-align: center;'>9.3.3</td></tr><tr><td style='text-align: center;'>66</td><td style='text-align: center;'>车站/区间封锁</td><td style='text-align: center;'>9.3.2</td></tr><tr><td style='text-align: center;'>67</td><td style='text-align: center;'>紧急停车按钮</td><td style='text-align: center;'>9.4</td></tr><tr><td style='text-align: center;'>68</td><td style='text-align: center;'>CI接口</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>69</td><td style='text-align: center;'>CI自检、故障报警及数据记录</td><td style='text-align: center;'>9.5</td></tr><tr><td style='text-align: center;'>70</td><td style='text-align: center;'>进路解锁及取消</td><td style='text-align: center;'>9.3.2</td></tr><tr><td style='text-align: center;'>71</td><td style='text-align: center;'>计轴故障恢复</td><td style='text-align: center;'>9.3.4</td></tr><tr><td style='text-align: center;'>72</td><td style='text-align: center;'>扣车</td><td style='text-align: center;'>8.6.1</td></tr><tr><td style='text-align: center;'>73</td><td style='text-align: center;'>站控/遥控</td><td style='text-align: center;'>8.6.4</td></tr><tr><td style='text-align: center;'>74</td><td style='text-align: center;'>CI权限设置</td><td style='text-align: center;'>无</td></tr></table>

## 6 ATP 功能分配

### 6.1 ATP 的主要功能

ATP 的主要功能见图 3。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ceb68824-c5ed-4cf0-b0a8-987e664bb0df/markdown_0/imgs/img_in_image_box_72_159_787_923.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A16%3A16Z%2F-1%2F%2Fd8c4304c97160ce4787d069b58cc77c8b89e7fb1cd694fbffbc33f21ccd3826b" alt="Image" width="84%" /></div>


说明：

实线框——其他章节描述内容；虚线框——本章节描述内容。



<div style="text-align: center;">图 3 ATP 主要功能</div>

---

### 6.2 列车位置确定

#### 6.2.1 确定列车位置关系图

图 4 概括了本段中所描述的子功能（实线框）之间的接口，以及其他段落中描述的子功能（虚线框）间的接口。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//35108014-cea0-4889-87c2-35cde2203a61/markdown_0/imgs/img_in_image_box_132_264_760_813.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A16%3A20Z%2F-1%2F%2Ffbf18f84219fbabae959ab6c91477f97820e93ecd2713080c02360d154123896" alt="Image" width="74%" /></div>


说明：

实线框——定位功能的条件；

虚线框——定位功能的用途

<div style="text-align: center;">图 4 确定列车位置关系图</div>


#### 6.2.2 初始化 CBTC 列车位置

##### 6.2.2.1 概述

此功能用于初始化 CBTC 列车位置，即确定 CBTC 装备列车的初始位置。表 2 ~ 表 4 规定了列车定位初始化的内容。

---

#### 6.2.2 进入 CBTC 区域的 CBTC 列车位置初始化

CBTC 列车位置初始化，并自动检测每列符合装备 CBTC 设备的列车，进入 CBTC 区域无需手动输入列车位置或列车长度的数据，见表 2。

<div style="text-align: center;">表 2 进入 CBTC 区域的 CBTC 列车位置初始化</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td colspan="4">注1:“输入”为该功能提供输入的子系统；“实现”该功能的子系统；“输出”接收该功能实现结果的子系统（适用于后续表格的内容）注2：本表格及后续表格中的“CBTC轨旁”包含“CBTC轨旁、应答器、LEU”</td></tr></table>

##### 6.2.2.3 从设备故障中恢复的 CBTC 列车完成位置初始化

CBTC列车位置初始化，并应自动检测每列装备CBTC设备的列车，从CBTC设备故障中恢复的列车无需手动输入列车位置或列车长度的数据，见表3。

<div style="text-align: center;">表 3 进从设备故障中恢复的 CBTC 列车完成位置初始化</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.2.2.4 电子地图存储

CBTC 系统的车载设备和轨旁设备应根据运行和管辖范围的不同，分别存储相关线路范围的电子地图，见表 4：

---

<div style="text-align: center;">表 4 电子地图存储</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.2.3 确定 CBTC 列车位置

##### 6.2.3.1 概述

此功能确定列车运行前方和后方的相邻 CBTC 列车的位置。表 5 ~ 表 13 规定了列车位置用途的内容。

##### 6.2.3.2 确定列车长度

CBTC 列车位置应能确定列车长度，见表 5

<div style="text-align: center;">表 5 确定列车长度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

##### 6.2.3.3 确定 CBTC 列车位置

CBTC列车位置的确定应包括安全、准确地确定列车车头和车尾的位置，并用足够的分辨率和精准度来满足性能和安全需求，见表6。

<div style="text-align: center;">表 6 确定 CBT 列车位置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

---

##### 6.2.3.4 位置误差校正

CBTC列车位置的确定应包含测距误差的影响，并对位置误差包含合适的余量，见表7。

<div style="text-align: center;">表 7 位置误差校正</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.2.3.5 列车完整性检测

CBTC系统应能实现列车的完整性检测，当车载设备检测到列车完整性信息丢失，列车完整性检查电路中断时，应对列车实施紧急制动，并丢失定位，同时系统应对后续追踪列车进行安全防护，保证后续列车安全运行，见表8。

<div style="text-align: center;">表 8 列车完整性检测</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>外部系统(车辆)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.2.3.6 列车轮径校正

CBTC系统应能实现列车轮径校正功能，系统宜在列车进入转换轨前设置轮径自动补偿设备，并在出段/场前完成自动轮径补偿，见表9。

---

<div style="text-align: center;">表 9 列车轮径校正</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.2.3.7 列车升级至 CBTC 级别

当系统由点式列车控制级别或联锁控制级别升级为连续式列车控制级别时，应满足如下转换条件：

——ATP 车载设备无故障，且完成列车定位；

——ATP 车载设备收到 ATP 轨旁设备发送的有效 MA 信息，见表 10

<div style="text-align: center;">表 10 列车升级至 CBTC 级别</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 6.2.3.8 确定列车停站位置

CBTC 系统应根据不同的列车长度，确定列车的停站位置，见表 11。

<div style="text-align: center;">表 11 确定列车停站位置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

---

##### 6.2.3.9 列车驾驶模式

列车应具有的驾驶模式包括：列车自动运行模式（AM）、列车自动防护模式（CM）、限制人工驾驶模式（RM）、非限制人工驾驶模式（EUM）、列车自动运行模式（AM），列车自动防护模式（CM）为列车正常运行模式，见表12。

<div style="text-align: center;">表 12 列车驾驶模式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td colspan="2">X SOCIATION OX</td><td style='text-align: center;'>X</td></tr></table>

##### 6.2.3.10 驾驶模式转换

列车驾驶模式等级由高至低分别为：AM、CM、RM，各驾驶模式满足转换条件可由人工转换，也可自动转换，车载设备应予以记录和显示。

为保证行车安全，列车驾驶模式由AM、CM转换为RM时，列车应停车，驾驶模式由低等级向高等级转换时，列车不停车转换驾驶模式，见表13。

<div style="text-align: center;">表 13 驾驶模式转换</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.2.4 确定轨道区段占用状态

##### 6.2.4.1 概述

此功能用于确定轨道区段的占用状态。表 14 和表 15 规定了轨道区段占用状态的内容。

---

##### 6.2.4.2 轨道区段的占用状态

CBTC 系统可根据轨旁次级占用检测设备提供的信息，结合 CBTC 列车汇报的位置信息，确定轨道区段的占用状态（有一辆或多辆车占用区段，包括 CBTC 列车和（或）装有无效的 CBTC 车载设备的列车）见表 14。

<div style="text-align: center;">表 14 轨道区段的占用状态</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>外部系统(次级占用检测设备)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.2.4.3 前方轨道区段占用状态

当 CBTC 列车前方区段被故障列车或者非 CBTC 装备列车占用时，CBTC 系统应根据前方区段占用状态确定 CBTC 列车的安全边界，见表 15。

<div style="text-align: center;">表 15 前方轨道区段的占用状态</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 6.2.5 故障管理

##### 6.2.5.1 概述

与基础的 CBTC 系统功能组合，后备轨旁系统和/或操作程序应在确

---

定列车位置功能故障情况下，为列车移动提供安全保障。表 16 和表 17 规定了列车位置功能故障的内容。

##### 6.2.5.2 防护列车丢失位置报告

当列车丢失位置报告后，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段，见表16。

<div style="text-align: center;">表 16 防护列车丢失位置报告</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.2.5.3 列车完整性丢失防护

在检测到列车完整性丢失时，CBTC系统将提供移动授权防护，避免其他列车进入无位置汇报列车占用的区段，见表17。

<div style="text-align: center;">表 17 列车完整性丢失防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC ATS 设备</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBT 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 6.3 移动防护限制和目标点的确定

#### 6.3.1 移动防护限制和相关的目标点

这一功能为 CBTC 列车确立了移动防护限制和相关的目标点。图 5 为移动保护的限定和目标点测定。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//027c2794-626b-43c6-9f57-639ba986271b/markdown_0/imgs/img_in_image_box_114_140_787_778.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A16%3A47Z%2F-1%2F%2Fee18805a6a7a6d8b2f815cd7f8653c38f76f218a5713d024376e873af475da98" alt="Image" width="79%" /></div>


说明：

实线框——移动授权确定的具体条件；

虚线框——移动授权保护的限定和失效防护

<div style="text-align: center;">图 5 移动保护的限定和目标点测定</div>


#### 6.3.2 确定移动防护的潜在限制

##### 6.3.2.1 功能描述

此功能用于确定 CBTC 列车前方移动授权的限制。表 18 和表 19 规定了列车位置用途的内容。

##### 6.3.2.2 CBTC 列车前方位置

对于每辆 CBTC 列车，应确定列车前方的 CBTC 列车位置，见表 18。

---

<div style="text-align: center;">表 18 CBTC 列车前方位置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 6.3.2.3 前方安全进路限制

对于每辆 CBTC 列车，系统应确定列车的安全进路位置，见表 19.

<div style="text-align: center;">表 19 前方安全进路限制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输</td><td style='text-align: center;'>输 出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

#### 6.3.3 移动授权的确定

##### 6.3.3.1 概述

分轨道

此功能确定移动授权。表20规定了移动授权的内容。

##### 6.3.3.2 移动授权的确定

为对列车进行合适的移动防护限制，CBTC 系统应估算最大移动授权限制位置，见表 20。

<div style="text-align: center;">表 20 移动授权的确定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

#### 6.3.4 目标点确定

##### 6.3.4.1 概述

此功能确定移动防护限制的目标点。表 21 ~ 表 24 规定了目标点的内容。

##### 6.3.4.2 目标点确定

为了确保列车不超过移动授权，CBTC系统应确定一个目标点，见表21。

<div style="text-align: center;">表 21 目标点确定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.3.4.3 响应紧急停车按钮的按下

当 ATP 轨旁设备接收到站台紧急停车按钮被按下的信息时，应通过车地通信设备向列车发送相应的列车控制命令信息，见表 22。

<div style="text-align: center;">表 22 响应紧急停车按钮的按下</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.3.4.4 道岔状态防护

CBTC 系统应控制区域内道岔状态并进行防护。当道岔状态丢失时，移动授权回撤至道岔区域的边界位置；当列车已驶入丢失状态的道岔

---

区域时，列车应实施紧急制动，见表23。

<div style="text-align: center;">表 23 道岔状态保护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.3.4.5 ZC 切换

两条连续式列车控制级别线路间应设置移交边界和移交重叠区。

列车进入移交重叠区后，车载 ATP 设备应同时与移交、接管线路的轨旁 ATP 设备建立通信，并根据列车是否越过移交边界选择采用移交/接管线路的轨旁 ATP 设备发送的 MA；移交、接管线路的轨旁 ATP 设备间应互传线路状态、列车位置等信息，并向车载 ATP 设备发送 MA 信息，见表 24。

<div style="text-align: center;">表 24 ZC 切换</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 6.3.5 故障管理

##### 6.3.5.1 概述

本功能明确 ATP 故障管理的要求。表 25 规定了故障管理的内容。

##### 6.3.5.2 故障管理

列车的非预期移动、ATP 轨旁设备故障、车载设备故障、超过系统允

---

许范围的车地通信中断等均应给出报警提示，与行车安全相关的故障均应产生紧急制动，见表25.

<div style="text-align: center;">表 25 故障管理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 6.4 ATP 曲线确定

#### 6.4.1 ATP 曲线计算

该功能用于计算 ATP 曲线，如图 6 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//d16d99ba-f8ee-498a-8328-0e199d6c1a48/markdown_0/imgs/img_in_image_box_177_615_739_940.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A01Z%2F-1%2F%2F72f3e7948e048f054c86a14aa87d156437db8db7367ac63cf95374be42989f8d" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 6 ATP 曲线计算</div>


#### 6.4.2 固定限制速度防护

此功能确定列车的固定限制速度。表 26 和表 27 规定了固定限制速度防护。

---

##### 6.4.2.1 固定线路限制速度

CBTC 应提供固定线路限速的限制防护，见表 26。

<div style="text-align: center;">表 26 固定线路限制速度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.4.2.2 列车构造限制速度

系统应提供列车构造速度的防护，见表27

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//05245287-edf7-4357-926c-6b7e53d6621f/markdown_0/imgs/img_in_seal_box_270_427_577_738.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A05Z%2F-1%2F%2F18cd09d4e61f3b74e3933600ae406c0f42c9b550a0b4ee736d73379383733041" alt="Image" width="36%" /></div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>人</td><td style='text-align: center;'>实</td><td style='text-align: center;'>输</td><td style='text-align: center;'>出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>中国</td><td style='text-align: center;'>中国</td><td style='text-align: center;'>中国</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 6.4.3 临时限速限制防护

##### 6.4.3.1 概述

此功能确定列车的临时限速防护。表 28 规定了临时限速限制防护问题。

##### 6.4.3.2 临时限制速度限制

CBTC 应按照系统设置的临时限速，为列车计算移动授权，对临时限速进行防护，见表 28。

<div style="text-align: center;">表 28 临时限制速度限制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 28 临时限制速度限制（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.4.4 确定制动曲线

##### 6.4.4.1 概述

此功能确定制动曲线，以保证列车在指定的目标点停车。表29和表30规定制动曲线的内容。

##### 6.4.4.2 目标点的制动曲线

表 29 规定了目标点制动曲线的内容。

<div style="text-align: center;">表 29 目标点的制动曲线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'>✗</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td></tr></table>

##### 6.4.4.3 防止制动曲线超过速度限制

CBTC 应保证制动曲线在超过固定或临时限速之前减速，见表 30.

<div style="text-align: center;">表 30 防止制动曲线超过速度限制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.4.5 计算 ATP 曲线

##### 6.4.5.1 概述

此功能用于计算完整的 ATP 曲线。表 31 规定了 ATP 曲线的内容。

---

##### 6.4.5.2 ATP 曲线

CBTC 应为每辆列车计算完整的 ATP 曲线，见表 31。

<div style="text-align: center;">表 31 ATP 曲线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 6.5 确定限制速度

#### 6.5.1 CBTC 列车限制速度

此功能确定对 CBTC 列车的限制速度。

图 7 概括了本条目描述的子功能接口和其他条目描述的子功能接口。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//77270764-d457-4567-9520-3fa1affc9123/markdown_0/imgs/img_in_image_box_173_637_689_803.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A13Z%2F-1%2F%2Fca12807f31c907ff961961cf666c7e60a9f254fd38692108465e88da184ffc11" alt="Image" width="61%" /></div>


<div style="text-align: center;">图 7 确定限制速度</div>


#### 6.5.2 确定限制速度

##### 6.5.2.1 概述

此功能确定列车当前位置的限制速度。表 32 规定了限制速度的内容。

##### 6.5.2.2 确定授权速度

CBTC 应基于 ATP 曲线，确定列车当前位置的限制速度，见表 32。

---

<div style="text-align: center;">表 32 确定授权速度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 6.6 列车实际速度/列车运行方向确定

#### 6.6.1 概述

图 8 概括了本条目描述的子功能接口和其他条目描述的子功能接口。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//37c563ac-e2dc-4643-bb04-c828ab43f122/markdown_0/imgs/img_in_image_box_169_456_744_804.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A16Z%2F-1%2F%2Fd77636c7841dcf5146b5b378a64699349c5c90a703bcd551ec6738897352592f" alt="Image" width="68%" /></div>


<div style="text-align: center;">图 8 实际列车速度/运行方向确定</div>


#### 6.6.2 CBTC 列车速度测定

##### 6.6.2.1 概述

此功能确定列车的速度。表 33 ~ 表 35 规定了 CBTC 列车速度测定的内容。

##### 6.6.2.2 确定 CBTC 列车实际速度

CBTC 应确定每辆 CBTC 装备列车的实际速度，速度满足分辨率和精度的要求，见表 33。

---

<div style="text-align: center;">表 33 确定 CBTC 列车实际速度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.6.2.3 测速误差补偿

CBTC 系统应能够补偿测速误差产生的影响，并对测速作出合适的补偿，见表 34。

<div style="text-align: center;">表 34 测速误差补偿</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输</td><td style='text-align: center;'>实</td><td style='text-align: center;'>输</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.6.2.4 零速状态确定

CBTC 应确定零速度状态，见表 35。

<div style="text-align: center;">表 35 零速状态确定</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 6.6.3 CBTC 列车运行方向确定

##### 6.6.3.1 概述

此功能确定列车实际运行方向。表 36 规定了 CBTC 列车运行方向。

##### 6.6.3.2 确定 CBTC 列车运行方向

CBTC 系统应确定每辆 CBTC 列车的实际运行方向，见表 36。

---

<div style="text-align: center;">表 36 确定 CBTC 列车运行方向</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 6.7 监督/强制允许速度和允许运行方向

#### 6.7.1 功能描述

该功能是监督和强制执行允许速度和允许运行方向。

#### 6.7.2 速度监督和防护

##### 6.7.2.1 概述

此功能监督和防护列车速度，如图9所示。表37和表38规定了速度监督和防护的内容。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a22b1b2e-5333-4790-a409-2600e846b39b/markdown_0/imgs/img_in_image_box_133_581_542_1087.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A23Z%2F-1%2F%2F9b6ec222b6972e313f17af4c37f1f7a05acb264524897e87e64fd4159231724c" alt="Image" width="48%" /></div>


6.7.4.4 紧急制动缓解

<div style="text-align: center;">图 9 监督/施加授权速度和运行方向</div>

---

##### 6.7.2.2 速度监督和防护

如果列车实际速度超过限制速度，CBTC应实施紧急制动，见表37。

<div style="text-align: center;">表 37 速度监督和防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.7.2.3 最不利情况下的影响

CBTC 的速度监督/执行应包括对最差情况下系统偏差、反应次数和反应时间的补偿，见表 38。

<div style="text-align: center;">表 38 最不利情况下的影响</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.7.3 运行方向监督和防护

##### 6.7.3.1 功能描述

此功能监督和防护列车运行方向。表 39 和表 40 规定了运行方向监督和防护的内容。

##### 6.7.3.2 监督/防护运行方向

如果列车实际运行方向与授权的列车运行方向不一致，CBTC 应实施紧急制动，见表 39。

<div style="text-align: center;">表 39 监督/防护运行方向</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

---

<div style="text-align: center;">表 39 监督/防护运行方向(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.7.3.3 退行防护

ATP 车载设备应具有退行防护功能。当退行距离和退行速度超过允许值时，系统应立即采取紧急制动。在列车退行过程中，系统应对追踪运行的列车提供安全间隔防护。退行距离超过限制，车载设备应丢失定位，见表 40。

<div style="text-align: center;">表 40 退行防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.7.4 故障管理

##### 6.7.4.1 越过移动授权终点的响应

系统应确保不会越过移动授权终点。表 41 ~ 表 44 规定了故障管理的内容。

<div style="text-align: center;">表 41 越过移动授权终点的响应</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.7.4.2 移动授权更新时的速度防护

移动授权更新时，如果列车的实际运行速度超过移动授权更新后的

---

紧急制动触发速度，系统应实施紧急制动。见表42。

<div style="text-align: center;">表 42 移动授权更新的速度防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.7.4.3 移动授权更新超时的防护

移动授权更新超时，系统应实施紧急制动，见表43。

<div style="text-align: center;">表 43 移动授权更新超时的防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.7.4.4 紧急制动缓解

在保证安全的条件下，系统可以缓解已施加的紧急制动，见表44。

<div style="text-align: center;">表 44 紧急制动缓解</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 6.8 车门/站台门控制

#### 6.8.1 功能描述

此功能实现车门/站台门控制，如图 10 所示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fa8044d2-c23f-4ddb-ad21-970d2da04052/markdown_0/imgs/img_in_image_box_180_143_771_636.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A17%3A37Z%2F-1%2F%2F8a109a68f4fa433ec8ac53080b74b6c5d16e578959827fc278092c21e8412ad8" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 10 车门/站台门控制</div>


#### 6.8.2 车门允许

##### 6.8.2.1 概述

表 45 ~ 表 47 规定了车门允许的内容。

##### 6.8.2.2 车门允许

CBTC 在开车门之前，应满足下列条件：

a）列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；

b）开门侧与站台一致；

c）列车零速；

d）保持制动已施加。



列车在车站规定的位置停准停稳后，车载ATP应允许打开对应侧车门及站台门或双侧车门及站台门，并可选择通过自开自关、自开人关、人

---

开人关三种方式，自动或者人工打开车门：在AM驾驶模式下，可提供三种开门方式，CM驾驶模式下，仅能实现人工开门。见表45。

列车在车站停车超出停车窗范围，车载设备应不允许车门和站台门打开，司机可在车载设备防护条件下前进或后退，直至停车对位。

<div style="text-align: center;">表 45 车门允许</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.8.2.3 站台门控制

CBTC 应打开站台门之前，应检查下列条件满足：

a) 列车“正确对齐”在一个指定的停止点，停止点偏差在允许范围内；

b) 站台门侧与车门侧一致；

c) 列车零速；

d) 保持制动已施加。

控制内容见表46。

<div style="text-align: center;">表 46 站台门控制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 6.8.2.4 车门操作切除

车辆可以提供单个车门切除功能（全自动下），切除后的车门不响应

---

列车开门命令，见表47.

<div style="text-align: center;">表 47 车门操作切除</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>外部系统(车辆)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 6.8.3 车门、站台门防护

##### 6.8.3.1 概述

表 48 和表 49 规定了车门和站台门防护的内容。

##### 6.8.3.2 车门防护

仅在车门处于“关闭且锁闭”状态时，系统方允许列车移动，见表48。

<div style="text-align: center;">表 48 车门防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.8.3.3 站台门锁闭状态防护

仅在站台门处于“关闭且锁闭”状态时，系统方允许列车移动CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；已进站未停稳以及正在出站的列车应立即紧急制动；已完全出站的列车不受影响，见表49。

---

<div style="text-align: center;">表 49 车门防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 6.8.4 故障管理

##### 6.8.4.1 概述

表 50 ~ 表 52 规定了车门和站台门故障管理的内容。

##### 6.8.4.2 车门状态丢失防护

列车在运行过程中，车载设备应实时监督列车车门状态，当检测到车门不为关门且锁闭状态时，系统宜采取下列措施之一：

a） 切除牵引但不实施制动：

b) 不切除牵引，也不实施制动，列车运行至下一座车站；

c) 实施紧急制动；

d) 实施全常用制动。市轨道交通



丢失防护内容见表50。

<div style="text-align: center;">表 50 车门状态丢失防护</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

##### 6.8.4.3 站台门状态丢失的响应

当列车靠近车站时或者列车已在站台区域时，站台门关闭状态丢失，CBTC系统采取保证列车安全的措施，见表51。

---

<div style="text-align: center;">表 51 站台门状态丢失的响应</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 6.8.4.4 车门防护切除

系统在车门故障时，可提供车门切除功能，此时 ATP 不再对车门状态进行防护，见表 52。

<div style="text-align: center;">表 52 车门防护切除</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 6.9 列车折返

列车折返方式应包括 ATO 无人自动折返模式、ATO 有人自动折返模式、ATP 监督下的人工折返模式。表 53 规定了列车折返方式的内容。

<div style="text-align: center;">表 53 列车折返方式</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

### 6.10 车载 ATP 用户界面

#### 6. 10. 1 CBTC 车载 ATP 显示数据

表 54 规定了车载 ATP 显示数据界面的内容, CBTC 车载显示屏显示 ATP 数据应包括:

a）列车运行模式；

b) CBTC 运行状态;

c）当前列车速度；

d）当前最大允许CBTC速度；

e）超速报警。

<div style="text-align: center;">表 54 CBTC 车载 ATP 显示数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 6.10.2 CBTC 车载 ATP 输入数据

表 55 规定了车载 ATP 输入数据的内容, 用户 ATP 信息输入到 CBTC 应包括:

a）运行模式选择；

b) 超速报警情况确认。

<div style="text-align: center;">表 55 CBTC 车载 ATP 输入数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

---

### 6.11 自诊断、故障报警及数据记录

ATP 车载设备具备自诊断、故障报警及列车运行重要数据的记录功能，并可通过离线设备打印。记录的内容包括事件的时间和日期，并保存7天，保存的数据可实现上传，并宜实现自动转存。记录内容包括：设备运行状况、行车里程、控制情况、驾驶模式、速度、列车日检数据。表56规定了自诊断、故障报警及数据记录的内容。

<div style="text-align: center;">表 56 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

## 7 ATO 功能分配

### 7.1 功能描述

ATO 主要功能如图 11 所示。

### 7.2 确定 ATO 曲线

#### 7.2.1 为启动、停止、调速，确定 ATO 曲线

CBTC 系统应为列车确定 ATO 曲线 ATO 子系统在 ATP 子系统的保护下，根据 ATS 子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制 ATO 子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制。表 57 规定了 ATO 曲线的内容。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//635213c0-e29b-4cc4-ad62-afec02d67d28/markdown_0/imgs/img_in_image_box_66_152_784_761.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A18%3A02Z%2F-1%2F%2F199146fa08b4b7ee921e106f01499e90fad1fad1eacc4fd0ba16913242709e6e" alt="Image" width="85%" /></div>


<div style="text-align: center;">表 57 确定 ATO 曲线</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 7.2.2 列车进站精确停车

ATO 子系统应具备列车进站精确停车功能，不同编组的列车可以停靠的不同的停车位置。表 58 规定了列车进站精确停车的内容。

---

<div style="text-align: center;">表 58 列车进站精确停车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 7.3 列车速度调整

#### 7.3.1 根据 ATO 曲线调整列车速度

CBTC 系统须根据 ATO 曲线调整列车速度。表 59 规定了列车调速的内容。

<div style="text-align: center;">表 59 列车调速功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 7.3.2 跳停

表 60 规定了 ATO 响应 ATS 跳停的内容

<div style="text-align: center;">表 60 ATO 响应 ATS 系统设置的跳停命令</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 7.3.3 运营调整

在 AM 模式下，ATO 子系统可根据 ATS 的调整指令控制区间走行时分，达到列车运行自动调整的目的。表 61 规定了列车自动调整的内容。

---

<div style="text-align: center;">表 61 列车运行自动调整功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 7.3.4 在线列车监控

ATO 予系统向 ATS 子系统发送列车运行信息，以便 ATS 子系统能对在线列车进行监控。表 62 规定了在线列车进行监控的内容。

<div style="text-align: center;">表 62 在线列车进行监控</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

### 7.4 门控制

#### 7.4.1 开列车门/站台门

表 63 和表 64 规定了门控制的内容

##### 7.4.1.1 开列车门

在 AM 驾驶模式下，在 ATP 的防护下可提供自动开门或者人工开门两种开门方式，见表 63。

<div style="text-align: center;">表 63 开列车门</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 63 开列车门(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>车辆(外部接口)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 7.4.1.2 开站台门

CBTC 系统须能自动或者人工开启站台门，见表 64。

<div style="text-align: center;">表 64 开站台门</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 7.4.2 关闭车门/站台门

##### 7.4.2.1 概述

表 65 和表 66 规定了关列车门/站台门。

##### 7.4.2.2 关闭列车门

在 AM 驾驶模式下，可提供自动关门或者人工关门两种关门方式，见表 65 和表 66。

<div style="text-align: center;">表 65 关闭列车门</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>车辆(外部接口)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

---

<div style="text-align: center;">表 66 关闭站台门</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">子功能:关闭站台门CBTC系统应能自动或者人工关闭站台门</td></tr><tr><td colspan="4">功能分配:</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

### 7.5 车载 ATO 用户界面

在列车显示屏上显示的 CBTC 车载 ATO 数据应由授权管理部门规定。表 67 规定了 ATO 显示数据的内容。

<div style="text-align: center;">表 67 CBTC 车载 ATO 显示数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>人</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>市轨道交通</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 7.6 自诊断、故障报警及数据记录

#### 7.6.1 概述

表 68 和表 69 规定了自诊断、故障报警及数据记录的内容。

#### 7.6.2 自诊断、故障报警及数据记录

ATO 子系统应具有自诊断功能，记录和分析故障报警信息，并能将报警信息传至中心 ATS，见表 68。

---

<div style="text-align: center;">表 68 自诊断、故障报警及数据记录</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

#### 7.6.3 车载旅客信息数据

ATO 车载设备应向 TMS 提供有关车载旅客信息的数据，见表 69.

<div style="text-align: center;">表 69  车载旅客信息数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>✗</td><td style='text-align: center;'>✗</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>外部车辆系统</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>✗</td></tr></table>

## 8 ATS 功能分配

### 8.1 功能描述

图 12 总结了主要的与 CBTC 相关的 ATS 功能。

### 8.2 列车识别

#### 8.2.1 概述

表 70 和表 71 规定了列车识别号的内容。

#### 8.2.2 CBTC 的运行列车识别号

每一个运行在 CBTC 区域内的装备 CBTC 的列车都应该分配一个运行列车标识号，列车识别号应由列车表号、车次号、车组号、目的地号组成。见表 70。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c98053b7-e89e-4e7b-848f-2ca8508d6921/markdown_0/imgs/img_in_image_box_114_123_728_816.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A18%3A22Z%2F-1%2F%2F8d838b356d2fd34fdd85fd14a52bff139a9ad83966d9a8df31dcd4c4438dc79d" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 12 ATS 的主要功能</div>


<div style="text-align: center;">表 70 CBTC 的运行列车识别号</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

#### 8.2.3 列车识别号丢失处理

在列车识别号因故丢失情况下，系统应根据运行图、列车位置及时间自动推算并自动设置列车识别号，且能通过车－地双向通信传输信息校核，见表71。

<div style="text-align: center;">表 71 列车识别号丢失处理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 8.3 列车追踪

ATS 系统应该具有自动追踪，获取所有运行在 CBTC 区域的装备 CBTC 的列车记录并在 ATS 用户界面显示位置、标识、列车时刻表，及其他相关的信息并保持这些信息的能力。列车的前后位置应该依据 CBTC 列车位置报告来进行追踪并显示在 ATS 用户界面上列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能。表 72 规定了 ATS 列车追踪的内容。

<div style="text-align: center;">表 72 ATS 列车追踪</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 8.4 列车进路办理

#### 8.4.1 概述

表 73 ~ 表 75 规定了列车进路办理的内容。

---

#### 8.4.2 列车进路办理——自动

ATS 系统应该具有列车自动办理进路的功能。ATS 系统依照列车运行图/时刻表、在线列车运行信息、车站联锁表自动设置发车进路，指挥在线列车运行，见表 73。

<div style="text-align: center;">表 73 列车进路自动办理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

#### 8.4.3 列车人工进路办理

ATS 系统应该具有手动办理进路的功能，见表 74。

<div style="text-align: center;">表 74 列车人工进路办理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>人</td><td style='text-align: center;'>实</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 8.4.4 列车进路办理——冲突检查

当列车运行偏离计划，不同运行交路的列车经过同一地点时，系统应能检测到列车计划冲突，并提示调度员采取列车计划冲突干预方案，见表75。

<div style="text-align: center;">表 75 列车进路冲突检查</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 75 列车进路冲突检查(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 8.5 列车调整

#### 8.5.1 列车自动调整

##### 8.5.1.1 概述

表 76 ~ 表 78 规定了列车调整的内容。

##### 8.5.1.2 自动调度

ATS 系统可包括自动调度功能，见表 76.

<div style="text-align: center;">表 76 自动调度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 8.5.1.3 列车时刻表/发车（运行）间隔调整

ATS 系统可具有监视与自动调整的功能，见表 77。

<div style="text-align: center;">表 77 列车时刻表调整功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 8.5.1.4 冲突自动调整

在 CBTC 列车位置报告的基础上，ATS 系统应包括基于列车位置报告的列车自动调整功能，来处理列车冲突，以把整个系统的延迟减少到最

---

小，见表78。

<div style="text-align: center;">表 78 冲突自动调整</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 8.5.2 节能运行

ATS 系统可具有通过实时控制及协调列车加速、列车滑行、列车制动来实施能源优化的功能，表 79 规定了节能运行的内容。

<div style="text-align: center;">表 79 节能运行</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 8.6 列车运行控制

#### 8.6.1 扣车

ATS 系统应具有在车站扣车能力。表 80 规定了扣车的内容。

<div style="text-align: center;">表 80 扣车功能</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

---

#### 8.6.2 提前发车

ATS 系统应具有设置站台提前发车的功能。表 81 规定了提前发车的内容。

<div style="text-align: center;">表 81 提前发车</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 8.6.3 跳停

ATS 系统应具有设置一个或多个装备 CBTC 的列车经过下一个或下几个车站而不停车的功能。表 82 规定了跳停车站的内容。

<div style="text-align: center;">表 82 跳停车站</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 8.6.4 控制权转换

在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号列车进路控制权的优先级为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制。表83规定了控制权转换的内容。

<div style="text-align: center;">表 83 控制权转换</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 83 控制权转换(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

### 8.7 控制列车运行

ATS 系统应具有在 CBTC 区域内任何轨道区段，设置（与取消）临时限速的能力。表 84 规定了临时限速的内容。

<div style="text-align: center;">表 84 临时限速</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输人</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>中</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>中</td><td style='text-align: center;'>X</td></tr></table>

### 8.8 时刻表编制

ATS应具备变更计划运行图/时刻表的功能，并按照变更后的结果组织和实施当日的列车运行。表85规定了时刻表编制的内容。

<div style="text-align: center;">表 85 时刻表编制</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 8.9 模拟培训

ATS 应具备模拟演示及培训系统，实现对调度员的培训。表 86 规定了模拟培训的内容。

---

<div style="text-align: center;">表 86 模拟培训</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

### 8.10 用户界面

#### 8.10.1 显示数据

CBTC 的 ATS 显示应能表示以下信息：

a）精确的和区域相关的信息；

b) 列车状态相关信息；

c) 列车移动授权/进路信息；

d）被控列车运行相关的信息，如防护区段信息、锁闭的进路/区段以及临时限速极限和限速值；

e）其他

表 87 规定了 ATS 显示数据的内容

<div style="text-align: center;">表 87 ATS 显示数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

#### 8.10.2 数据管理

8.10.2.1 概述

表 88 ~ 表 90 规定了 CBTC 输入数据的内容。

---

##### 8. 10. 2. 2 CBTC 输入数据

CBTC 的 ATS 用户界面显示应能够接收以下 ATS 用户输入：

a）办理和取消进路输入；

b）建立和取消防护区段，锁闭进路/区段，以及临时限速输入；

c）其他。

表 88 规定了 CBTC 输入数据的内容。

<div style="text-align: center;">表 88 CBTC 输入数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

##### 8.10.2.3 发送报警数据

ATS 子系统可将自身的报警信息、ATP 车载子系统、ATO 子系统、CI 子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站，见表 89。

<div style="text-align: center;">表 89 发送报警数据</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>MSS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

##### 8.10.2.4 数据记录及回放

系统应对各种操作信息、设备运行状态信息及运行数据进行记录和备份，并具有根据记录数据对任何时间、任何信息点进行过程回放功能，综合维修中心的信号监测报警工作站系统应具备在线回放功能，回放记

---

录应保存不少于30天，见表90.

<div style="text-align: center;">表 90 数据记录及回放</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>MSS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

## 9 CI 功能分配

### 9.1 功能描述

CBTC 相关的 CI 主要功能分配，如图 13 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//fa9644b3-0c93-476b-b7dd-5088f5ffadc4/markdown_0/imgs/img_in_image_box_159_657_759_774.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A18%3A55Z%2F-1%2F%2F0f50514673f7869aefbe67786df105dff16ea4c3b549f9375a559dd86ee49b2c" alt="Image" width="71%" /></div>


<div style="text-align: center;">图 13 CI 的主要功能</div>


### 9.2 进路办理

#### 9.2.1 功能描述

表 91 ~ 表 93 规定了进路办理的内容。

#### 9.2.2 进路办理

联锁应具备进路办理功能。包括人工办理列车进路、设置自动进路和自动折返进路。联锁将办理的进路信息提供给ATP系统，用于移动授权的计算，见表91。

---

<div style="text-align: center;">表 91 进路办理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

#### 9.2.3 装有无效 CBTC 装备的列车进路办理

对于设备故障的 CBTC 列车或无装备的列车，在前方进路出清并重新开放后，装有无效 CBTC 装备的列车方可驶入，见表 92。

<div style="text-align: center;">表 92 故障列车进路办理</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>人</td><td style='text-align: center;'>实</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

#### 9.2.4 保护区段

联锁子系统除对正常的列车进路进行防护外，还应建立列车进路的保护区段，并予以防护，见表93。

<div style="text-align: center;">表 93 保护区段</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

---

### 9.3 锁闭/解锁进路/区段

#### 9.3.1 概述

表 94 ~ 表 97 规定了锁闭/解锁进路/区段的内容。

#### 9.3.2 进路/区段锁闭

系统应具有锁闭（并随后解锁）CBTC区域内的道岔、信号机或轨道区段的能力，CI子系统应对进路实现预先锁闭和接近锁闭，锁闭的进路随列车的运行自动分段解锁，见表94。

<div style="text-align: center;">表 94 进路/区段锁闭</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

#### 9.3.3 道岔单操、单锁

联锁应具备道岔单独操纵及锁闭的能力，见表95。

<div style="text-align: center;">表 95 道岔操作</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

#### 9.3.4 计轴故障恢复

系统应具有计轴故障恢复的能力，见表96。

---

<div style="text-align: center;">表 96 计轴故障恢复</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

### 9.4 紧急停车按钮

联锁子系统检查站台紧急停车按钮的状态，一旦检测到按钮被按下，应立即关闭相应的进路。表97规定了紧急停车按钮的内容。

<div style="text-align: center;">表 97 紧急停车按钮</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr></table>

### 9.5 故障监测及操作记录

CI 子系统具有自检、自诊断和对信号机、转辙机等基础信号设备的监测报警功能，并在车站的维护工作站上显示及报警。表 98 规定了故障监测及操作记录的内容。

<div style="text-align: center;">表 98 故障检测</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 98 故障检测(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

---

## 参考文献

# [1] IEEE 1474.3 IEEE Recommended Practice for Communications-Based Train Control (CBTC) System Design and Functional Allocations

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//406b0e3b-84a8-4f95-9b0a-abe26827ae8a/markdown_0/imgs/img_in_seal_box_239_409_599_744.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A19%3A10Z%2F-1%2F%2F8d380a846081c16a52e36093fd618d4c414e215df2e1ee71870d8fcee136668b" alt="Image" width="42%" /></div>

---

# 中国城市轨道交通协会团体标准   城市轨道交通 基于通信的列车运行   控制系统（CBTC）互联互通系统规范   第2部分：系统架构和功能分配   T/CAMET 04010.2—2018

 $ ^{*} $ 

中国铁道出版社有限公司出版发行

(100054, 北京市西城区石安门西街 8 号)

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm×1230 mm 1/32 印张：2.25 字数：61千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5656 定价：20.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174