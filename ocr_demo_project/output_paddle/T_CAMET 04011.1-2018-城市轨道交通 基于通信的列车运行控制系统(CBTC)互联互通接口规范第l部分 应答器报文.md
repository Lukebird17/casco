# 中国城市轨道交通协会团体标准

T/CAMET 04011.1—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第1部分：应答器报文

# Urban rail transit — Interface specification for interoperability of communication based train control system Part 1: Balise protocol

2018-09-10 发布

2018-12-31 实施

---

## 目 次

前言 …… VII    
引言 …… IX    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 1    
3.1 术语 …… 2    
3.2 缩略语 …… 2    
4 总则 …… 2    
5 接口描述 …… 3    
5.1 总体要求 …… 3    
5.2 通信结构及接口连接方式 …… 4    
5.3 应答器报文结构 …… 5    
5.4 应答器发包 …… 11

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第4部分：区域控制器(ZC)间接口；

——第5部分：计算机联锁(CI)间接口；

——第6部分：列车自动监控系统(ATS)间接口；

——第7部分:信号各子系统与维护支持系统(MSS)间接口;

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 1 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

本部分主要起草人：编写组：张国振、王佳、张振兴、刘波、杨旭文、许硕、王芃、戴毅欣、杨晓荣、胡顺定、周在福、黄友能、刘键。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范 第 1 部分: 应答器报文

## 1 范围

T/CAMET 04011 的本部分规定了应答器报文的通信结构及接口连接方式、应答器报文结构和应答器发包等内容。

本规范适用于国内采用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 24339.1—2009 轨道交通 通信、信号和处理系统 第1部分:封闭式传输系统中的安全相关通信(IEC 62280-1:2002,IDT)

TB/T 2615—1994 铁路信号故障－安全原则

TB/T 3485—2017 应答器传输系统技术条件

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

## 3 术语和缩略语

CJ/T 407—2012 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

---

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.2 

移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T 407—2012, 定义 3.1.7]

#### 3.1.3 

兼预告的主应答器 primary balise with prediction function

兼具预告应答器功能的主应答器，所对应的进路指的是其所对应的信号机内方的第一条进路；所预告的进路指的是沿进路开放方向的第二架信号机所防护的进路。

### 3.2 缩略语

ATP:列车自动防护(Automatic Train Protection)

BTM: 应答器传输模块 (Balise Transfer Module)

CBTC: 基于通信的列车控制 (Communication Based Train Control)

LEU: 轨旁电子单元(Lineside Electronic Unit)

## 4 总则

4.1 满足城市轨道交通互联互通要求的 CBTC 系统应遵守本规范。

4.2 本规范中应答器报文的制定以不依赖于特定的电子地图描述方式为原则。

---

## 5 接口描述

### 5.1 总体要求

5.1.1 CBTC系统中，车载ATP应通过车载BTM实现与应答器的通信。当列车经过地面应答器时，车载应答器天线激活地面应答器，并接收应答器循环发送的应答器报文。

5.1.2 CBTC 系统应通过车载 BTM 和应答器传输报文实现如下功能：



a）建立列车定位；

b) 校正列车位置；

c） 传输点式移动授权；

d）监控应答器通信状态。

5.1.3 CBTC 的点式后备系统或点式信号主用系统应满足图 1 所示结构的要求。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9330b9ea-aaba-4b96-aa96-1976d774be92/markdown_0/imgs/img_in_image_box_98_619_736_870.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A43%3A30Z%2F-1%2F%2F797d83cd949042840828f7da85c33f0a16d2cd32841659c08dd23fd2a1b13a47" alt="Image" width="75%" /></div>


注：LEU 可通过联锁设备或信号机点灯电路控制，如采用信号机点灯电路控制，应考虑是否能够满足线路拓扑要求。

<div style="text-align: center;">图 1 点式系统结构图</div>


5.1.4 CBTC 的点式后备系统或点式信号主用系统基本功能分配如下：

a）信号机由联锁设备控制；

b）联锁或信号机点灯电路通过 LEU 控制有源应答器报文；

---

c）车载设备通过应答器天线获取应答器信息，根据点式移动授权，生成制动曲线并进行相应的防护。

5.1.5 地面应答器采用无线通信方式向车载应答器天线单方向持续重复的传送报文。

5.1.6 应答器按照报文是否可变，可分为无源应答器和有源应答器。其中无源应答器又称固定应答器，有源应答器可分为主应答器和填充应答器两种。固定应答器报文不可变，主应答器与填充应答器报文可变，主应答器布置在其对应信号机外方，填充应答器布置在其描述的主应答器外方，填充应答器与主应答器的距离宜保证列车不至降速时收到填充应答器报文。

5.1.7 在无点式后备模式时，系统应只配置固定应答器。

### 5.2 通信结构及接口连接方式

5.2.1 物理接口应满足如下要求：地面有源应答器应通过 LEU 进行编码，有源应答器与 LEU 间应采用专用电缆连接。车载应答器天线与 BTM 应通过专用馈缆连接。

5.2.2 地面应答器与车载应答器天线间的信息传输接口（也称接口A）、应答器编码与解码应满足 GB/T 24339.1—2009 和 TB/T 3485—2017 的要求。

5.2.3 通信故障的处理应符合以下原则：

a）如 BTM 无法对应答器报文解码、应答器天线无法激活应答器、传输错误等原因导致车载设备无法接收应答器报文，车载设备应按照应答器丢失处理，应满足 TB/T 2615—1994 中要求的故障导向安全原则。

b）有源应答器与LEU通信故障时，应答器应发送应答器默认报文；LEU与联锁通信中断时，LEU向应答器发送LEU默认报文，并经应答器发送至车载设备。应答器默认报文和LEU默认报文的组包方式参见5.4。

---

### 5.3 应答器报文结构

#### 5.3.1 报文结构

本规范采用830位长报文结构，用户信息包中不足的比特位以1补齐。

报文结构定义(信息帧)见表1。

<div style="text-align: center;">表 1 信息帧的报文结构定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>变量</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>备注</td></tr><tr><td rowspan="10">1</td><td rowspan="10">帧标志</td><td style='text-align: center;'>Q_UPDOWN</td><td style='text-align: center;'>1</td><td style='text-align: center;'>信息传送的方向(0=车对地,1=地对车),本规范中统一为1</td></tr><tr><td style='text-align: center;'>M_VERSION</td><td style='text-align: center;'>7</td><td style='text-align: center;'>语言/代码版本编号(0010000=V1.0)</td></tr><tr><td style='text-align: center;'>Q_MEDIA</td><td style='text-align: center;'>1</td><td style='text-align: center;'>信息传输媒介(0=应答器)</td></tr><tr><td style='text-align: center;'>N_PIG</td><td style='text-align: center;'>3</td><td style='text-align: center;'>本应答器在应答器组中的位置(000=1,111=8),本规范中不设置应答器组,本变量采用000</td></tr><tr><td style='text-align: center;'>N_TOTAL</td><td style='text-align: center;'>3</td><td style='text-align: center;'>应答器组中所包含的应答器数是(000=1,111=8),本规范中不设置应答器组,本变量采用000</td></tr><tr><td style='text-align: center;'>M_DUP</td><td style='text-align: center;'>2</td><td style='text-align: center;'>本应答器信息与前/后应答器信息的关系(00=不同,01=与后一个相同,10=与前一个相同),本规范采用00</td></tr><tr><td style='text-align: center;'>M_MCOUNT*</td><td style='text-align: center;'>8</td><td style='text-align: center;'>报文计数器(0-255)</td></tr><tr><td style='text-align: center;'>NID_Lb</td><td style='text-align: center;'>10</td><td style='text-align: center;'>线路编号</td></tr><tr><td style='text-align: center;'>NID_BG*</td><td style='text-align: center;'>14</td><td style='text-align: center;'>应答器(组)编号</td></tr><tr><td style='text-align: center;'>Q_LINK</td><td style='text-align: center;'>1</td><td style='text-align: center;'>应答器(组)的链接关系(0=不被链接,1=被链接),本规范采用0</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>用户信息包</td><td style='text-align: center;'></td><td style='text-align: center;'>772</td><td style='text-align: center;'>用户信息包区</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>信息结束</td><td style='text-align: center;'></td><td style='text-align: center;'>8</td><td style='text-align: center;'>=11111111,表示信息帧结束</td></tr></table>

---

<div style="text-align: center;">表 1 信息帧的报文结构定义(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>注： $ ^{a} $ M_MCOUNT（报文计数器）：单个应答器会对应多条报文，本变量表示本报文在这些报文中的序号。固定应答器只包含一条报文，M_MCOUNT设为255。有源应答器默认报文，M_MCOUNT设为252。LEU默认报文，M_MCOUNT设为0。M_MCOUNT值禁用253和254。其他报文M_MCOUNT由厂商自定。 $ ^{b} $ NID_L：线路编号采用区域内统一编号的方式，可在区域线路规划时统一分配。 $ ^{c} $ NID_BG：应答器（组）编号，用于在一条线路内，唯一识别的ID，由5位十进制数表示，最大值为16383。</td></tr></table>

#### 5.3.2 用户信息包

5.3.2.1 ETCS-44 包定义见表 2。

<div style="text-align: center;">表 2 ETCS-44 包定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>变量名</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="3">1</td><td style='text-align: center;'>NID_PACKET</td><td style='text-align: center;'>8</td><td style='text-align: center;'>信息包标识码 = 0010 1100</td></tr><tr><td style='text-align: center;'>Q_DIR</td><td style='text-align: center;'>2</td><td style='text-align: center;'>验证方向 (00 = 反向有效, 01 = 正向有效, 10 = 双向有效, 11 = 备用)</td></tr><tr><td style='text-align: center;'>L_PACKET</td><td style='text-align: center;'>13</td><td style='text-align: center;'>信息包位数, 根据子包组成情况而定, 为整个 ETCS-44 包 (含子包) 的位数</td></tr><tr><td rowspan="2">2</td><td style='text-align: center;'>NID_XUSER</td><td style='text-align: center;'>9</td><td style='text-align: center;'>用户数据包标识码</td></tr><tr><td style='text-align: center;'>XXXXXX</td><td style='text-align: center;'></td><td style='text-align: center;'>由 NID_XUSER 确定的信息包</td></tr></table>

每个 ETCS-44 包应只包含一个子包，一个应答器报文中可包含多个 ETCS-44 包。

5.3.2.2 地图版本信息包定义(202 子包)见表 3。

<div style="text-align: center;">表 3 地图版本信息包定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>变量名</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>说明</td></tr><tr><td rowspan="2">1</td><td style='text-align: center;'>NID_XUSER</td><td style='text-align: center;'>9</td><td style='text-align: center;'>用户数据包标识码 = 0 1100 1010(202)</td></tr><tr><td style='text-align: center;'>M_EDITION</td><td style='text-align: center;'>16</td><td style='text-align: center;'>地图版本信息(本应答器所辖范围内的地图版本)</td></tr></table>

---

5.3.2.3 公共信息包定义(203 子包)见表 4。

<div style="text-align: center;">表 4 公共信息包定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>变量名</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>NID_XUSER</td><td style='text-align: center;'>9</td><td style='text-align: center;'>用户数据包标识码=0 1100 1011(203)</td></tr><tr><td rowspan="2">2</td><td style='text-align: center;'>Q_SIGNAL_ASPECT</td><td style='text-align: center;'>19</td><td style='text-align: center;'>主应答器时为该处信号机显示状态。填充应答器时为所填充进路始端信号机的状态</td></tr><tr><td style='text-align: center;'>Q_SIGNAL_ASPECT_PRE</td><td style='text-align: center;'>19</td><td style='text-align: center;'>该应答器预告信号状态。该位仅对于主应答器有效，该位表示该主应答器兼具预告应答器功能时，对应的沿进路方向第二架信号机显示状态。对于不兼具预告功能的主应答器，该位域全部填0。填充应答器该位无效（填充应答器全部填0），应用不应采用</td></tr><tr><td rowspan="2">3</td><td style='text-align: center;'>C_CI_LEU</td><td style='text-align: center;'>1</td><td style='text-align: center;'>联锁与LEU通信状态：0：联锁与LEU通信正常；1：联锁与LEU通信中断。当C_LEU_BALISE为1（即LEU与应答器通信中断）时，该位无效。如系统采用点灯电路的方式驱动LEU，点灯电路故障，按照LEU与联锁通信中断处理</td></tr><tr><td style='text-align: center;'>C_LEU_BALISE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>LEU与应答器通信状态：0：LEU与应答器通信正常；1：LEU与应答器通信中断</td></tr><tr><td rowspan="2">4</td><td style='text-align: center;'>D_DIS</td><td style='text-align: center;'>24</td><td style='text-align: center;'>主应答器至MA终点距离</td></tr><tr><td style='text-align: center;'>D_DIS_OVERLAP</td><td style='text-align: center;'>24</td><td style='text-align: center;'>主应答器至进路末端保护区段起点的距离</td></tr><tr><td rowspan="8">5</td><td style='text-align: center;'>N_SWITCH</td><td style='text-align: center;'>4</td><td style='text-align: center;'>道岔数量，最多15个</td></tr><tr><td style='text-align: center;'>NID_SWITCH1</td><td style='text-align: center;'>16</td><td style='text-align: center;'>道岔1编号</td></tr><tr><td style='text-align: center;'>S_SWITCH1_STATE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>道岔1状态：10-定位，01反位，其他无效</td></tr><tr><td style='text-align: center;'>NID_SWITCH2</td><td style='text-align: center;'>16</td><td style='text-align: center;'>道岔2编号</td></tr><tr><td style='text-align: center;'>S_SWITCH2_STATE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>道岔2状态：10-定位，01反位，其他无效</td></tr><tr><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td><td style='text-align: center;'>...</td></tr><tr><td style='text-align: center;'>NID_SWITCHN</td><td style='text-align: center;'>16</td><td style='text-align: center;'>道岔N编号</td></tr><tr><td style='text-align: center;'>S_SWITCHN_STATE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>道岔N状态：10-定位，01反位，其他无效</td></tr><tr><td colspan="4">注：道岔描述顺序按照主应答器向MA终点的顺序排列。</td></tr></table>

---

表 4 中，O_SIGNAL_ASPECT 取值应符合表 5 的规定。

<div style="text-align: center;">表 5 Q_SIGNAL_ASPECT 取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>信号机显示状态</td><td style='text-align: center;'>Q_SIGNAL_ASPECT 值</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>红灯, 引导、灭灯、或故障都以红灯处理</td><td style='text-align: center;'>XX0 0000 0000 0000 0001</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>绿灯或者黄灯(进路仅涉及顺向道岔反位)无保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 0010</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>绿灯或者黄灯(进路仅涉及顺向道岔反位)有保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 0011</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>黄灯 1(U1)无保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 0100</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>黄灯 1(U1)有保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 0101</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>黄灯 2(U2)无保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 1000</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>黄灯 2(U2)有保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 1001</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>黄灯 3(U3)无保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 1100</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>黄灯 3(U3)有保护区段</td><td style='text-align: center;'>XX0 0000 0000 0000 1101</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>黄灯 N(UN)无保护区段</td><td style='text-align: center;'>XXA BCDE FGHI JKLM NP00(N = A BCDE FGHI JKLM NP)</td></tr><tr><td style='text-align: center;'>—</td><td style='text-align: center;'>黄灯 N(UN)有保护区段</td><td style='text-align: center;'>XXA BCDE FGHI JKLM NP01(N = A BCDE FGHI JKLM NP)</td></tr><tr><td colspan="3">注: XX 为预留, 默认为 00。</td></tr></table>

黄灯序号的确认原则为：对于 Q_SIGNAL_ASPECT 中 ABCDEFGHIJKLMNPOQ，从第3位（P）开始，每一位表示对向道岔（不包含顺向道岔）的状态，对向道岔定位为0，对向道岔反位为1，可最多表示15个对向道岔，不足15个对向道岔，为0。第1位（Q）表示是否有保护区段，0表示无保护区段，1表示有保护区段。例如前方进路存在3个对向道岔，第1个对向道岔反位，第2个对向道岔定位，第3个对向道岔反位。信号机状态及对应内容见表6。

---

<div style="text-align: center;">表 6 信号机状态及对应内容</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>信号机显示状态</td><td style='text-align: center;'>Q_SIGNAL_ASPECT 值</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>黄灯 5(U5)无保护区段</td><td style='text-align: center;'>XX0 0000 0000 0001 0100</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>黄灯 5(U5)有保护区段</td><td style='text-align: center;'>XX0 0000 0000 0001 0101</td></tr></table>

a） 区分对向道岔和顺向道岔的方式：

1）从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔前区域，后搜索到该道岔的岔后区域，则该道岔为该方向上的对向道岔。

2）从线路上沿指定方向搜索到道岔，若先搜索到该道岔的岔后区域，后搜索到该道岔的岔前区域，则该道岔为该方向上的顺向道岔。

b) 由于道岔之间的走向关系，有可能出现黄灯序号不连续的情况，如图2所示。



<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8f33c423-8e86-40f8-9360-c493eb715331/markdown_0/imgs/img_in_image_box_71_505_764_879.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A43%3A56Z%2F-1%2F%2F2837b0b303ec007861c5865931e5104deafc1db0394ce40d5fd6bc8353e5743a" alt="Image" width="82%" /></div>


说明：

对于主应答器 VB01，若办理 X01-X03 进路，因进路内存在两个对向道岔 P01、P03，且 P01 为反位、P03 为定位，故 X01 信号机显示状态应为黄灯 1（U1）有保护区段；若办理 X01-X04 进路，因进路内存在两个对向道岔 P01、P03，且 P01 为反位、P03 为反位，故 X01 信号机显示状态应为黄灯 3（U3）有保护区段。

<div style="text-align: center;">图 2 黄灯序号不连续场景示例</div>

---

c) Q_SIGNAL_ASPECT 所表示的范围为主应答器对应的信号机所防护的进路的情况（即使该主应答器兼具预告应答器功能，Q_SIGNAL_ASPECT 也不报告前方预告进路的情况）。Q_SIGNAL_ASPECT 所表示的道岔不包含保护区段的道岔。

d) Q_SIGNAL_ASPECT_PRE 取值: Q_SIGNAL_ASPECT_PRE 的定义方式与 Q_SIGNAL_APSECT 完全相同, 范围为兼预告的主应答器所预告的第二架信号机处开始至第二架信号防护的进路末端。如果 Q_SIGNAL_APSECT 为红灯, 则 Q_SIGNAL_ASPECT_PRE 取值为 0。

e）D_DIS：主应答器至MA终点距离，至多160km（1cm分辨率）。如果该应答器为填充应答器，则该距离为填充应答器对应的主应答器MA终点距离。如果进路有保护区段，则MA终点放置在保护区段的末端。如果进路无保护区段，则MA终点位于进路最后一个区段的末端。若进路内有车挡，则MA终点应不超过车挡。红灯情况下，该距离为主应答器至主应答器所在进路末端距离。默认报文中，D_DIS填0。

对于兼预告的主应答器，则该距离与预告进路是否开放相关。如果预告进路未开放，则该距离遵从上述原则。如果预告进路开放，则该距离为兼预告主应答器至第二架信号机防护进路的终点的距离，保护区段处理方式相同。

f) D_DIS_OVERLAP: 主应答器至进路保护区段起点的距离，至多160 km（1 cm分辨率）。如果该应答器为填充应答器，则该距离为填充应答器对应的主应答器至主应答器对应的信号机防护进路末端的保护区段起点距离。如果进路无保护区段，D_DIS_OVERLAP 填0。默认报文中，D_DIS_OVERLAP 填0。

对于兼预告的主应答器，则该距离与预告进路是否开放相关。如果预告进路未开放，则该距离遵从上述原则。如果预告进路

---

开放，则该距离为兼预告主应答器至第二架信号机防护进路末端的保护区段起点距离，保护区段处理方式相同。

g）NID_SWITCH：线路内统一编号且唯一。

h) N_SWITCH: MA 范围内道岔的数量，如果进路包含保护区段，则保护区段内的道岔也包含在内。道岔数量应不大于 15，该包根据不同的道岔数量是变长的。道岔数量不足 15 个，包的长度按照实际的道岔数量确定。如果 MA 范围内没有道岔，则 N_SWITCH 为 0，NID_SWITCH 和 S_SWITCH_STATE 位不存在。默认报文中认为 MA 范围内没有道岔。这里的道岔包含对向道岔和顺向道岔。

i) 道岔描述顺序按照主应答器向 MA 终点的顺序排列。

5.3.3 厂商自定义包(204 子包)见表 7。

<div style="text-align: center;">表 7 厂商自定义包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>变量名</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>NID_XUSER</td><td style='text-align: center;'>9</td><td style='text-align: center;'>用户数据包标识码=0 1100 1100(204)</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>NID_PROVIDER</td><td style='text-align: center;'>8</td><td style='text-align: center;'>厂商标识</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>D_RESERVED</td><td style='text-align: center;'>X</td><td style='text-align: center;'>厂商自定义内容及格式</td></tr></table>

5.3.4 城市自定义包(205 子包)见表 8.

<div style="text-align: center;">表 8 城市自定义包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>变量名</td><td style='text-align: center;'>位数</td><td style='text-align: center;'>说明</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>NID_XUSER</td><td style='text-align: center;'>9</td><td style='text-align: center;'>用户数据包标识码=0 1100 1101(205)</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>NID_CITY</td><td style='text-align: center;'>8</td><td style='text-align: center;'>城市标识</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>D_CITY</td><td style='text-align: center;'>X</td><td style='text-align: center;'>城市自定义内容及格式</td></tr></table>

### 5.4 应答器发包

应答器发包情况见表9。

---

<div style="text-align: center;">表 9 应答器发包</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>应答器类型</td><td style='text-align: center;'>报文类型</td><td style='text-align: center;'>功能</td><td style='text-align: center;'>包含的信息包</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>无源应答器</td><td style='text-align: center;'>N/A</td><td style='text-align: center;'>定位</td><td style='text-align: center;'>地图版本信息包(202 子包)</td></tr><tr><td style='text-align: center;'>2</td><td rowspan="3">有源应答器</td><td style='text-align: center;'>正常报文</td><td style='text-align: center;'>亮灯时发送; 灭灯时发送红灯报文</td><td style='text-align: center;'>地图版本信息包(202 子包)、公共信息包(203 子包)、厂商自定义信息包(204 子包,可选)、城市自定义信息包(205 子包,可选)</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>应答器默认报文</td><td style='text-align: center;'>有源应答器与LEU通信中断</td><td style='text-align: center;'>地图版本信息包(202 子包)、公共信息包(203 子包)、C_LEU_BALISE为1</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>LEU默认报文</td><td style='text-align: center;'>LEU与联锁通信中断</td><td style='text-align: center;'>地图版本信息包(202 子包)、公共信息包(203 子包)、C_CI_LEU为1</td></tr></table>

---

中国城市轨道交通协会团体标准  

城市轨道交通 基于通信的列车运行  

控制系统（CBTC）互联互通接口规范  

第1部分：应答器报文  

T/CAMET 04011.1—2018

中国铁道出版社有限公司出版发行

(100054, 北京市西城区右安门西街8号)

公司网址：http://www.tdpress.com

北京格成印刷有限公司印刷

开本：880 mm×1230 mm 1/32 印张：0.75 字数：17千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5707 定价：15.00元

版权所有 侵权必究

凡购买铁道版图书，如有印刷质量问题，请与本公司发行部联系调换  

发行部电话：路（021）73174，市（010）51873174

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>定价：15.00 元</th></tr></thead>
  <tbody>
  </tbody>
</table>