ICS 45.020

S 63

# 中国城市轨道交通协会团体标准

T/CAMET 04011.3—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范 第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口

# Urban rail transit — Interface specification for interoperability of communication based train control system

# Part 3: Interface between onboard Automatic Train Protection (ATP) & Automatic Train Operation (ATO) and vehicle

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
4 总则 …… 3    
5 功能接口 …… 3    
5.1 功能接口类型定义 …… 3    
5.2 输入信号 …… 7    
5.3 输出信号 …… 16    
5.4 电源及其他接口 …… 24    
6 机械接口 …… 24    
6.1 通用要求 …… 24    
6.2 车内设备 …… 25    
6.3 车底设备 …… 26    
6.4 车载无线天线 …… 31    
6.5 连接电缆 …… 36    
附录 A（规范性附录）与车辆功能接口特性参数 …… 37    
参考文献 …… 42

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第2部分：CBTC系统车地连续通信协议；

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第4部分：区域控制器(ZC)间接口；

——第5部分:计算机联锁(CI)间接口;

——第6部分：列车自动监控系统(ATS)间接口；

——第7部分:信号各子系统与维护支持系统(MSS)间接口;

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 3 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

本部分主要起草人：编写组：吕浩炯、任颖、杨晓荣、周元宝、王佳、李博、贾鹏、刘超、袁大鹏、吴苏娇、胡顺定、黄友能、刘宏杰。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行 控制系统(CBTC)互联互通接口规范 第3部分:车载列车自动保护(ATP)/列车自动 运行(ATO)系统与车辆的接口

## 1 范围

## OCIATION

T/CAMET 04011 的本部分规定了城市轨道交通信号系统车载 ATP/ATO 设备与车辆之间的接口，主要包括功能接口定义、机械接口的定义、传输信号的要求和机械接口的安装要求。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

## 轨道

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 19666—2005 阻燃和耐火电线电缆通则

GB/T 25119—2010 轨道交通机车车辆电子装置(IEC 60571:2006, MOD)

TB/T 1484 机车车辆电缆

TB/T 3153—2007 铁路应用机车车辆布线规则

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

---

## 3 术语和缩略语

CJ/T 407—2012 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

车辆接口 vehicle interface

车载 ATP/ATO 设备与安装有该设备的车辆之间的接口。

[CJ/T 407—2012, 定义 7.2]

#### 3.1.2 

输入信号 input signal

表示由车辆传输至车载 ATP/ATO 设备的信号。

[CJ/T 407—2012, 定义 7.2.1]

#### 3.1.3 

输出信号 output signal

表示由车载 ATP/ATO 设备传输至车辆的信号。

[CJ/T 407—2012, 定义 7.2.2]

#### 3.1.4 

左侧 left side of the vehicle

列车运行方向的左侧为车辆左侧。

#### 3.1.5 

右侧 right side of the vehicle

列车运行方向的右侧为车辆右侧。

#### 3.1.6 

互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1,术语3.1.16]

---

### 3.2 缩略语

BTM: 应答器传输模块 (Balise Transfer Module)

## 4 总则

4.1 为促进轨道交通信号系统车载 ATP/ATO 设备与车辆之间的兼容性和互换性，达到互联互通目的，本规范对车载 ATP/ATO 设备与安装有该设备的车辆间接口进行定义，包括接口方式与接口参数，并对车载 ATP/ATO 设备安装位置、安装方式等进行了约束。

4.2 本规范中，功能接口特指车载 ATP/ATO 设备与列车牵引系统、制动系统及车辆控制系统之间的电气接口。

4.3 本规范中机械接口特指车载 ATP/ATO 主机、车载显示器、转速传感器、多普勒雷达传感器、加速度传感器、BTM 天线、车载无线天线的安装位置及空间等相关要求。

4.4 对于互联互通的线路，车载信号设备中车载显示器的显示形式及按键定义、司机操作按钮安装位置及功能定义、指示灯位置及显示定义、车载信号设备与PIS等通信接口及协议等宜保持一致，具体在工程阶段进行约定。

## 5 功能接口

### 5.1 功能接口类型定义

对于功能接口，本规范定义 A 型、B 型及 C 型三种类型。

注：若采用其他类型接口或对下述三种类型接口有不同要求，在工程实施阶段进行约定。

#### 5.1.1 A型接口

A型接口为数字形式，并具有以下特征：

a） 输出信号

车载 ATP/ATO 设备输出方式包括继电器触点和电平输出两种方式，并具有以下定义：

## 1 ）继电器触点方式

---

——控制信号为逻辑“1”，即继电器常开触点闭合或常闭触点断开；

——控制信号为逻辑“0”，即继电器常开触点断开或常闭触点闭合。

## 2 ）电平方式

——控制信号为逻辑“1”表示输出高电平( $ \geq $ DC 77 V);

——控制信号为逻辑“0”表示输出低电平(<DC 25 V)

## 3 ）安全性要求

对于安全关键输出信号，应采用继电器常开触点，逻辑“0”定义为安全侧。

安全关键输出继电器触点宜与车辆执行机构直接连接。



## b) 输入信号

车载 ATP/ATO 设备采集车辆状态，宜采用继电器触点或机械触点信号，也可采用电平信号。

## 1 ）继电器触点方式

——控制信号为逻辑“1”表示车辆继电器常开触点闭合或常闭触点断开；

——控制信号为逻辑“0”表示车辆继电器常开触点断开或常闭触点闭合。

## 2 ）电平方式

——控制信号为逻辑“1”表示输入高电平（≥DC 77 V）；

——控制信号为逻辑“0”表示输入低电平（<DC 25 V）。

注：关于电压与逻辑状态转换关系参见图1。

## 3 ）安全性要求

对于安全关键输入继电器触点信号，车辆宜提供2组触点，且触点宜来源于两组独立继电器；若车辆仅提供1组触点，则应采用线缆全程屏蔽的接线方式。

对于非安全关键输入继电器触点信号，车辆应提供1组触点。

---

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>区域</th><th style='text-align: center;'>电压(DC)</th><th style='text-align: center;'>逻辑值</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>非确定区</td><td style='text-align: center;'>0 V</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>非确定区</td><td style='text-align: center;'>25 V</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>非确定区</td><td style='text-align: center;'>77 V</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>非确定区</td><td style='text-align: center;'>77 V</td><td style='text-align: center;'>1</td></tr>
  </tbody>
</table>

<div style="text-align: center;">图 1 电压与逻辑状态转换关系</div>


#### 5.1.2 B型接口

B型接口具有以下特征

a）接口信号为单向模拟信号；

b）接口采用 $ 0\sim20 $ mA电流环。

#### 5.1.3 C型接口

C型接口具有以下特征：

a）接口采用串行总线通信；

b) 串行通信宜采用 MVB 总线方式，也可采用 RS422 或 RS485 方式；

c）C型接口通信协议可参照《城轨车辆车载控制网络数据传送规范（第2版）》执行。

关于功能接口特性参数要求见附录 A。

#### 5.1.4 功能接口汇总表

表 1 规定了输入类功能接口的名称及要求。

<div style="text-align: center;">表 1 输入类功能接口</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>安全性要求</td><td style='text-align: center;'>是否为选用接口</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>紧急制动状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见 5.2.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>列车完整性状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见 5.2.2</td></tr></table>

---

<div style="text-align: center;">表 1 输入类功能接口(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>安全性要求</td><td style='text-align: center;'>是否为选用接口</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>列车车门锁闭状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.4</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>驾驶室激活状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.6</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>车辆牵引已切除状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.8</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>方向手柄向前及主控手柄零位状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.10</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>司机方向手柄位置</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.11</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>列车车门状态旁路</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.5</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>列车制动状态</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.7</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>列车零速度信号</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.9</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>车载ATP/ATO旁路</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.13</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>列车车门开关状态</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.3</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>车门控制模式选择</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.14</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>司机人工开门信号</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.15</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>司机人工关门信号</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.2.16</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>司机主控手柄位置</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.2.12</td></tr><tr><td colspan="5">注:接口选用“是”表示接口可根据工程实际进行选用,选用“否”接口的均为必须采用的接口。</td></tr></table>

表 2 规定了输出类功能接口的名称及要求。

<div style="text-align: center;">表 2 输出类功能接口</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>安全性要求</td><td style='text-align: center;'>是否为选用接口</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>紧急制动指令</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>开门使能信号</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.4</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>牵引切除指令</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.5</td></tr></table>

---

<div style="text-align: center;">表 2 输出类功能接口(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>接口名称</td><td style='text-align: center;'>安全性要求</td><td style='text-align: center;'>是否为选用接口</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>车载ATP/ATO列车零速度信号</td><td style='text-align: center;'>安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.3.13</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>ATO牵引/制动指令</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.6</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>ATO牵引/制动级位</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.7</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>AM驾驶模式状态</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.8</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>开门指令</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.11</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>关门指令</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>否</td><td style='text-align: center;'>参见5.3.12</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>最大常用制动指令</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.3.2</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>快速制动指令</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.3.3</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>CM驾驶模式状态</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.3.9</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>自动折返</td><td style='text-align: center;'>非安全关键</td><td style='text-align: center;'>是</td><td style='text-align: center;'>参见5.3.10</td></tr></table>

### 5.2 输入信号

#### 5.2.1 紧急制动状态

##### 5.2.1.1 接口描述

紧急制动状态是安全关键输入信号,该接口采用 A 型接口,并具有如下 2 种状态:

——车辆施加紧急制动；

——车辆未施加紧急制动。

##### 5.2.1.2 信号特征

紧急制动状态接口具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示车辆施加紧急制动；

——控制信号为逻辑“0”表示车辆未施加紧急制动。

注：本规范中所定义功能接口，除已声明为安全关键接口，其他未声明的为非安全关键接口。

#### 5.2.2 列车完整性状态

##### 5.2.2.1 接口描述

列车完整性状态是安全关键输入信号，车载 ATP/ATO 设备检测到

---

列车完整性丢失后，将会输出紧急制动指令。该接口采用 A 型接口，并具有如下 2 种状态：

——列车完整性有效；

——列车完整性无效。

#### 5.2.2 信号特征

列车完整性检查接口具有两种输入状态,具体定义如下:

——控制信号为逻辑“1”表示列车完整性有效；

——控制信号为逻辑“0”表示列车完整性无效。

#### 5.2.3 列车车门开关状态

##### 5.2.3.1 接口描述

列车车门开关状态是输入信号，用于列车车门开、关状态。该接口采用 A 型接口方式，并具有如下 2 种状态：

——全部列车车门都处于关闭状态；

——有列车车门未处于关闭状态。

注：本处所定义的列车车门开关状态不包含司机室门状态。如需包含，可在工程阶段进行约定。

##### 5.2.3.2 信号特征

列车车门开关状态具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示全部列车车门都处于关闭状态；

——控制信号为逻辑“0”表示有列车车门未处于关闭状态。

#### 5.2.4 列车车门锁闭状态

##### 5.2.4.1 接口描述

列车车门锁闭状态是指列车车门关闭后的锁闭状态。列车车门锁闭状态是安全关键输入信号，若车载ATP/ATO设备检测到列车车门不处于预期的锁闭状态，将实施相应的安全处理。该接口采用A型接口方式，并具有如下2种状态：

——全部列车车门都处于锁闭状态；

——有列车车门未处于锁闭状态。

当任一列车门紧急打开开关处于允许状态时，车辆应输出所在侧

---

“列车车门未处于锁闭状态”。

本处所定义的列车车门锁闭状态不包含司机室门状态。如需包含，可在工程阶段进行约定。

##### 5.2.4.2 信号特征

列车车门锁闭状态具有两种输入状态,具体定义如下:

——控制信号为逻辑“1”表示全部列车车门都处于锁闭状态；

——控制信号为逻辑“0”表示有列车车门未处于锁闭状态。



#### 5.2.5 列车车门状态旁路

##### 5.2.5.1 接口描述

列车车门状态旁路是安全关键输入信号，用于旁路列车车门状态信号。该接口采用 A 型接口，并具有如下 2 种状态：

——列车车门旁路开关处于旁路状态

——列车车门旁路开关处于非旁路状态。

工程中“列车车门关闭状态”和“列车车门锁闭状态”接口应真实反映列车车门状态。

##### 5.2.5.2 信号特征

列车车门状态旁路具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示列车车门旁路开关处于旁路状态；

——控制信号为逻辑“0”表示列车车门旁路开关处于非旁路状态。

#### 5.2.6 驾驶室激活状态

##### 5.2.6.1 接口描述

驾驶室激活状态是安全关键输入信号,该接口采用 A 型接口,并具有如下 2 种状态:

——驾驶室处于激活状态或车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活状态；

——驾驶室处于激活撤销状态且车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活撤销状态。

##### 5.2.6.2 信号特征

驾驶室激活状态具有两种输入状态,具体定义如下:

---

——控制信号为逻辑“1”表示驾驶室处于激活状态或车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活状态；

——控制信号为逻辑“0”表示驾驶室处于激活撤销状态且车载ATP/ATO设备的虚拟车辆钥匙信号处于激活撤销状态。

车辆应保证两端驾驶室不会同时激活。

#### 5.2.7 列车制动状态

##### 5.2.7.1 接口描述

列车制动状态是安全关键输入信号，该接口采用 A 型接口，并具有如下 2 种状态：

——车辆未施加保持制动、停放制动、常用制动、最大常用制动、快速制动和紧急制动中的任意一种；

——车辆保持制动、停放制动、常用制动、最大常用制动、快速制动和紧急制动，至少有一种已施加。

##### 5.2.7.2 信号特征

列车制动状态接口具有两种输入状态，具体定义如下：

——状态信号为逻辑“1”表示车辆保持制动、停放制动、常用制动、最大常用制动、快速制动或紧急制动施加；

——状态信号为逻辑“0”表示车辆保持制动、停放制动、常用制动、最大常用制动、快速制动和紧急制动未施加。

#### 5.2.8 车辆牵引已切除状态

##### 5.2.8.1 接口描述

车辆牵引已切除状态是安全关键输入信号，该接口采用 A 型接口，并具有如下 2 种状态：

——车辆牵引已切除；

——车辆牵引未切除。

##### 5.2.8.2 信号特征

车辆牵引已切除状态接口具有两种输入状态,具体定义如下:

——控制信号为逻辑“1”表示车辆牵引切除；

——控制信号为逻辑“0”表示车辆牵引未切除。

---

#### 5.2.9 列车零速度信号

##### 5.2.9.1 接口描述

列车零速度信号是安全关键输入信号，该接口采用 A 型接口，并具有如下 2 种状态：

——列车处于零速度状态；

——列车处于非零速度状态。

##### 5.2.9.2 信号特征

列车零速度信号接口具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示列车处于零速度状态；

——控制信号为逻辑“0”表示列车处于非零速度状态。

#### 5.2.10 方向手柄向前及主控手柄零位状态

##### 5.2.10.1 接口描述

方向手柄向前及主控手柄零位状态是安全关键输入信号，该接口采用 A 型接口，并具有如下 2 种状态：

——方向手柄向前且主控手柄零位条件成立；

——方向手柄向前且主控手柄零位条件不成立。

##### 5.2.10.2 信号特征

方向手柄向前及主控手柄零位状态具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示方向手柄向前且主控手柄零位条件成立；

——控制信号为逻辑“0”表示方向手柄向前且主控手柄零位条件不成立。

#### 5.2.11 司机方向手柄位置

##### 5.2.11.1 接口描述

司机方向手柄位置是安全关键输入信号，该接口采用3组A型接口，分别为：

a）向前指示接口；

b) 向后指示接口；

---

c）方向零位指示接口。

##### 5.2.11.2 信号特征

方向向前位、向后位指示接口和方向零位指示接口组合，具体定义见表3。

<div style="text-align: center;">表 3 司机方向手柄位置指示接口信号特征</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>方向向前指示接口</td><td style='text-align: center;'>方向向后指示接口</td><td style='text-align: center;'>方向零位指示接口</td><td style='text-align: center;'>司机方向手柄位置</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>向前位</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>向后位</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>零位</td></tr><tr><td colspan="4">注1:1表示控制信号为逻辑“1”;0表示控制信号为逻辑“0”。注2:除以上组合以外,其余组合关系均为故障值。</td></tr></table>

#### 5.2.12 司机主控手柄位置

##### 5.2.12.1 接口描述

司机主控手柄位置是输入信号，该接口宜采用 A 型接口方式，也可采用 C 型接口方式。

a）对于 C 型接口方式，通过总线通信接收司机主控手柄位置信息。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b）采用 A 型接口方式，通过 2 组 A 型接口进行输入，分别为：

——牵引位置指示接口；

——制动位置指示接口；

——主控零位位置指示接口。

##### 5.2.12.2 信号特征

牵引位置指示接口、制动位置指示接口和主控零位位置指示接口组合，具体定义见表4。

---

<div style="text-align: center;">表 4  司机主控手柄位置指示接口信号特征</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>牵引位置指示接口</td><td style='text-align: center;'>制动位置指示接口</td><td style='text-align: center;'>主控零位位置指示接口</td><td style='text-align: center;'>司机主控手柄位置</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>牵引位</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>制动位</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>零位</td></tr><tr><td colspan="4">注1:1表示控制信号为逻辑“1”;0表示控制信号为逻辑“0”。注2:除以上组合以外其余组合关系均为故障值。</td></tr></table>

#### 5.2.13 车载 ATP/ATO 旁路

##### 5.2.13.1 接口描述

车载 ATP/ATO 旁路信号是安全关键输入信号,该接口采用 A 型接口,并具有如下 2 种状态:

——车载 ATP/ATO 处于旁路状态；

——车载 ATP/ATO 处于非旁路状态。

##### 5.2.13.2 信号特征

车载 ATP/ATO 旁路信号接口具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”表示车载 ATP/ATO 处于非旁路状态；

——控制信号为逻辑“0”表示车载ATP/ATO处于旁路状态。

注：车辆设置车载 ATP/ATO 设备旁路开关。该开关在处于“旁路激活”位置时，断开车载 ATP/ATO 设备与车辆间所有 A 型接口。车辆应对旁路开关采取一定安全防护措施。

#### 5.2.14 车门控制模式选择

##### 5.2.14.1 接口描述

车门控制模式选择是输入信号,该接口采用3组A型接口,分别为:

——自动开门/自动关门选通接口；

——自动开门/人工关门选通接口；

——人工开门/人工关门选通接口。

---

##### 5.2.14.2 信号特征

自动开门/自动关门选通接口、自动开门/人工关门选通接口及人工开门/人工关门选通接口组合，具体定义见表5。

<div style="text-align: center;">表 5 车门控制模式选择接口信号特征</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>自动开门/自动关门选通接口</td><td style='text-align: center;'>自动开门/人工关门选通接口</td><td style='text-align: center;'>人工开门/人工关门选通接口</td><td style='text-align: center;'>车门控制模式选择</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>自动开门/自动关门</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>自动开门/人工关门</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>人工开门/人工关门</td></tr><tr><td colspan="3">其他</td><td style='text-align: center;'>故障模式</td></tr><tr><td colspan="4">注1:1表示控制信号为逻辑“1”;0表示控制信号为逻辑“0”。注2:故障模式下,车载ATP/ATO设备将默认车门采用人工开门/人工关门模式。</td></tr></table>

#### 5.2.15 司机人工开门信号

##### 5.2.15.1 接口描述

司机人工开门信号是输入信号，该接口宜采用 A 型接口方式，也可采用 C 型接口方式。

a）对于 C 型接口方式，通过总线通信接收司机人工开门信息。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b）采用 A 型接口方式，通过 2 组 A 型接口进行输入，分别为：

——司机人工开左侧门信号；

——司机人工开右侧门信号。

开门指令具有两种状态,分别为:

——人工开门有效，表示人工开门信号激活；

——人工开门无效，表示人工开门信号未激活。

##### 5.2.15.2 信号特征

司机人工开左侧门信号具有两种输入状态，具体定义如下：

---

——控制信号为逻辑“1”并持续一段时间，表示司机人工开左侧门有效；

——控制信号为逻辑“0”表示司机人工开左侧门无效。

司机人工开右侧门信号具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间，表示司机人工开右侧门有效；

——控制信号为逻辑“0”表示司机人工开右侧门无效。

注：信号有效持续时间在工程实施阶段约定。

#### 5.2.16 司机人工关门信号

##### 5.2.16.1 接口描述

司机人工关门信号是输入信号，该接口宜采用 A 型接口方式，也可采用 C 型接口方式。

a）对于 C 型接口方式，通过总线通信接收司机人工开门信息。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b）采用 A 型接口方式，通过 2 组 A 型接口进行输入，分别为：

——司机人工关左侧门信号；

——司机人工关右侧门信号。

关门指令具有两种状态,分别为:

——人工关门有效；

——人工关门无效。

##### 5.2.16.2 信号特征

司机人工关左侧门信号具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间，表示司机人工关左侧门有效；

——控制信号为逻辑“0”表示司机人工关左侧门无效。

司机人工关右侧门信号具有两种输入状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间，表示司机人工关右侧门有效；

——控制信号为逻辑“0”表示司机人工关右侧门无效。

---

### 5.3 输出信号

#### 5.3.1 紧急制动指令

##### 5.3.1.1 功能定义

紧急制动指令是安全关键输出信号,该接口采用 A 型接口,并具有如下 2 种状态:

——紧急制动施加；

——紧急制动未施加。

该接口对应以下功能要求：

a） 车辆在接收到紧急制动指令后，应立即执行紧急制动；

b) 车辆在进行紧急制动的同时应切除牵引动力；

c) 车载 ATP/ATO 设备一旦发出紧急制动指令，须在判断列车已停车并在触发紧急制动原因消除后，才能进行紧急制动指令的撤销；

d）紧急制动命令撤销表示允许车辆进行紧急制动的缓解，车辆在进行紧急制动缓解后才能执行牵引；

e） 车载 ATP/ATO 设备在旁路状态下，紧急制动指令接口处于紧急制动状态。

注1：紧急制动原理：紧急制动由列车安全回路失电触发。安全回路失电后，制动系统内部紧急制动电磁阀失电，来自载荷阀的车辆载荷压力直接连通到中继阀，中继阀按照当前车辆载荷压力输出相应的紧急制动压力到基础制动装置。

注2：紧急制动缓解条件：紧急制动的触发条件复位后（如紧急制动按钮复位等），安全回路得电即紧急电磁阀得电且车辆停稳后即可缓解紧急制动。

##### 5.3.1.2 信号特征

紧急制动指令具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示紧急制动指令撤销；

——控制信号为逻辑“0”表示紧急制动指令。

#### 5.3.2 最大常用制动指令

##### 5.3.2.1 接口描述

最大常用制动指令是输出信号，该接口采用 A 型接口，并具有如下

---

两种状态：

——最大常用制动施加；

——最大常用制动未施加。

##### 5.3.2.2 信号特征

最大常用制动指令接口具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示最大常用制动未施加；

——控制信号为逻辑“0”表示最大常用制动施加。

#### 5.3.3 快速制动指令

##### 5.3.3.1 接口描述

快速制动指令是输出信号，该接口采用 A 型接口，并具有如下两种状态：

——快速制动施加；

——快速制动未施加。

##### 5.3.3.2 信号特征

快速制动指令接口具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示快速制动未施加

——控制信号为逻辑“0”表示快速制动

#### 5.3.4 开门使能信号

##### 5.3.4.1 接口描述

市轨道交

开门使能信号为安全关键输出信号，该接口采用2组A型接口，分别为：

a）左侧开门使能；

b）右侧开门使能。

开门使能信号具有两种状态,分别为:

——允许开门；

——禁止开门。

##### 5.3.4.2 信号特征

左侧开门使能具有两种输出状态,具体定义如下:

——控制信号为逻辑“1”表示左侧开门许可；

---

——控制信号为逻辑“0”表示左侧开门许可未激活。

右侧开门使能具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示右侧开门许可；

——控制信号为逻辑“0”表示右侧开门许可未激活。

#### 5.3.5 牵引切除指令

##### 5.3.5.1 接口描述

牵引切除指令是安全关键输出信号，车载 ATP/ATO 设备在输出列车门开门使能过程中，将输出该信号，防止列车在开门期间动车。该接口采用 A 型接口，并具有如下两种状态：

——牵引切除；

——牵引切除撤销。

注：在车载 ATP/ATO 设备在处于旁路模式下，牵引切除指令接口处于牵引切除状态。

##### 5.3.5.2 信号特征

牵引使能指令接口具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示牵引切除撤销；

——控制信号为逻辑“0”表示牵引切除。

#### 5.3.6 ATO 牵引/制动指令

##### 5.3.6.1 接口描述

ATO 牵引/制动指令是输出信号，该接口宜采用 C 型接口方式，也可采用 A 型接口方式。

a）对于 C 型接口方式，通过总线通信指示当前车载 ATP/ATO 设备状态。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b）采用 A 型接口方式，通过 2 组 A 型接口进行输出，分别为：

——牵引指令接口；

——制动指令接口。

该 2 组 A 型接口通过组合, 分别对应四种模式:

——制动模式，ATO命令车辆进入制动工况；

---

——牵引模式，ATO命令车辆进入牵引工况；

——惰行模式，ATO命令车辆进入惰行工况；

——无效状态，ATO 故障或接口故障。

##### 5.3.6.2 信号特征

ATO 牵引/制动请求接口具有四种输出状态，具体定义见表 6。

<div style="text-align: center;">表 6 ATO 牵引/制动请求接口信号特征</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>牵引指令接口</td><td style='text-align: center;'>制动指令接口</td><td style='text-align: center;'>ATO牵引/制动指令模式</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>1</td><td style='text-align: center;'>无效模式</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1</td><td style='text-align: center;'>制动模式</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>惰行模式</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0</td><td style='text-align: center;'>牵引状态</td></tr><tr><td colspan="3">注1:1表示控制信号为逻辑“1”;0表示控制信号为逻辑“0”。注2:在无效状态下,车辆宜按制动模式处理。</td></tr></table>

#### 5.3.7 ATO 牵引/制动级位

##### 5.3.7.1 接口描述

ATO 牵引/制动级位是输出信号，该接口宜采用 C 型接口方式，也可采用 B 型接口方式。接口与 ATO 牵引/制动指令组合，用于 ATO 对列车的驾驶控制。

对于 C 型接口方式，指示车辆按照规定制动率或牵引率进行控制。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》中的规定。

采用 B 型接口方式，通过电流环中电流大小表示当前牵引率/制动率。

##### 5.3.7.2 B型接口信号特征

B型接口信号特征具体如下：

a） ATO 牵引/制动指令为制动模式

电流环中电流大小 $ (I_{\mathrm{Lop}}) $ 表示制动率，具体对应关系如下：

1） $ I_{Lump} \lt 4\ mA $ ，无输出状态，车辆按照制动率为0输出。

2） $ 4\ mA \leqslant I_{1,op} \leqslant 18\ mA $ ，车辆按照线性比例输出制动率，车辆输出制动率 $ L_{z} $ 按公式(1)换算：

---

$$ L_{2}=\frac{I_{Loop}-4}{14}\times 最大常用制动率 $$ 

式中：

 $ L_{z} $ ——车辆输出制动率；

 $ I_{loop} $ ——电流大小的数值,单位为毫安(mA);

数字 4 为最小有效电流 (4 mA)，数字 14 为有效电流范围 (18 mA - 4 mA)

3） $ 18\ mA < I_{Loop} \leq 20\ mA $ ，车辆按照最大常用制动率输出。

4） $ I_{Loop} > 20\ mA $ ，车辆按照最大常用制动率输出。

## b） ATO 牵引/制动指令为牵引模式

电流环中电流大小 $ (I_{\mathrm{Lop}}) $ 表示牵引率，具体对应关系如下：

1） $ I_{Loop} < 4\ mA $ ，无输出状态，车辆按照牵引率为0输出。

2） $ 4\ mA \leqslant I_{Loop} \leqslant 18\ mA $ ，车辆按照线性比例输出牵引率，车辆

输出牵引率 $ L_{0} $ 按公式(2)换算：

 $$ L_{0}=\frac{I_{Loop}-4}{14}\times 最大牵引率 $$ 

式中：

 $ L_{0} $ ——车辆输出牵引率；

 $ I_{Loop} $ ——电流大小的数值,单位为毫安(mA)。

数字 4 为最小有效电流(4 mA), 数字 14 为有效电流范围(18 mA - 4 mA)

3） $ 18\ mA < I_{1,op} \leq 20\ mA $ ，车辆按照最大牵引率输出。

4） $ I_{Loop} > 20  mA $ ，车辆按照切除牵引方式控制。

#### 5.3.8 AM 驾驶模式状态

##### 5.3.8.1 接口描述

AM 驾驶模式状态是输出信号,该接口宜采用 C 型接口方式,也可采用 A 型接口方式。

a）对于 C 型接口方式，通过总线通信指示当前车载 ATP/ATO 设备处于 AM 驾驶模式，具体可参见《城轨车辆车载控制网络数

---

据传送规范(第2版)。

b) 采用 A 型接口方式, 通过 1 组 A 型接口进行输出, 表示如下:

——车载 ATP/ATO 设备处于 AM 驾驶模式激活状态；

——车载 ATP/ATO 设备处于 AM 驾驶模式未激活状态。

##### 5.3.8.2 信号特征

AM 驾驶模式状态具有两种输出状态,具体定义如下:

——控制信号为逻辑“1”表示车载 ATP/ATO 设备处于 AM 驾驶模式激活状态；

——控制信号为逻辑“0”表示车载 ATP/ATO 设备处于 AM 驾驶模式未激活状态。

#### 5.3.9 CM 驾驶模式状态 COCIATION

##### 5.3.9.1 接口描述

CM 驾驶模式状态是输出信号,该接口宜采用 C 型接口方式,也可采用 A 型接口方式。

a) 对于 C 型接口方式，通过总线通信指示当前车载 ATP/ATO 设备处于 CM 驾驶模式。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b) 采用 A 型接口方式，通过 1 组 A 型接口进行输出，表示如下：

——车载 ATP/ATO 设备处于 CM 驾驶模式激活状态；

——车载 ATP/ATO 设备处于 CM 驾驶模式未激活状态。



##### 5.3.9.2 信号特征

CM 驾驶模式状态具有两种输出状态,具体定义如下:

——控制信号为逻辑“1”表示车载 ATP/ATO 设备处于 CM 驾驶模式激活状态；

——控制信号为逻辑“0”表示车载 ATP/ATO 设备处于 CM 驾驶模式未激活状态。

#### 5.3.10 自动折返

##### 5.3.10.1 接口描述

自动折返为输出信号,该接口主要目的是实现车载 ATP/ATO 设备

---

控制列车在特定地点进行折返作业。该接口采用 A 型接口方式。

自动折返接口采用2组A型接口，具体如下：

a） 自动折返运行方向信号接口，该信号具有如下2种状态：

——车载 ATP/ATO 设备命令车辆运行方向为“向前”；

——车载 ATP/ATO 设备撤销运行方向“向前”命令。

b）车辆钥匙虚拟信号接口，该信号具有如下2种状态：

——车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活状态；

——车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活撤销状态。

##### 5.3.10.2 信号特征

自动折返运行方向信号中：

——控制信号为逻辑“1”表示车载 ATP/ATO 设备命令车辆运行方向为“向前”；

——控制信号为逻辑“0”表示撤销运行方向“向前”命令。

车辆钥匙虚拟信号中：

——控制信号为逻辑“1”表示车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活状态；

——控制信号为逻辑“0”表示车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活撤销状态。

注：自动折返也可采用1组A型接口表示，将车辆钥匙虚拟信号和运行方向信号合并输出，对应信号特征如下：

——控制信号为逻辑“1”表示车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活状态且车载 ATP/ATO 设备命令车辆运行方向为“向前”；

——控制信号为逻辑“0”表示车载 ATP/ATO 设备的虚拟车辆钥匙信号处于激活撤销状态及车载 ATP/ATO 设备撤销运行方向“向前”命令。

#### 5.3.11 开门指令

##### 5.3.11.1 接口描述

开门指令是输出信号,该接口宜采用 A 型接口方式,也可采用 C 型

---

接口方式。

a）对于 C 型接口方式，通过总线通信发送开门指令。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b) 采用 A 型接口方式，通过 2 组 A 型接口进行输出，分别为：



——左侧开门指令；

——右侧开门指令。

开门指令具有两种状态，分别为：

——开门指令；

——开门指令撤销。

##### 5.3.11.2 信号特征

左侧开门指令具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间（电平或脉冲），表示左侧开门指令；

——控制信号为逻辑“0”表示左侧开门指令撤销。

右侧开门指令具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间（电平或脉冲），表示右侧开门指令；

——控制信号为逻辑“0”表示右侧开门指令撤销。

#### 5.3.12 关门指令

##### 5.3.12.1 接口描述

关门指令是输出信号，该接口宜采用 A 型接口方式，也可采用 C 型接口方式。

a）对于 C 型接口方式，通过总线通信发送关门指令。具体可参见《城轨车辆车载控制网络数据传送规范（第 2 版）》。

b）采用 A 型接口方式，通过 2 组 A 型接口进行输出，分别为：





——左侧关门指令；

——右侧关门指令。

开门指令具有两种状态，分别为：

——关门指令；

---

——关门指令撤销。

##### 5.3.12.2 信号特征

左侧关门指令具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间，表示左侧关门指令；

——控制信号为逻辑“0”表示左侧关门指令撤销。

右侧关门指令具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”并持续一段时间，表示右侧关门指令；

——控制信号为逻辑“0”表示右侧关门指令撤销。

#### 5.3.13 车载 ATP/ATO 零速度信号

##### 5.3.13.1 接口描述

车载 ATP/ATO 列车零速度信号是安全关键输出信号，该接口采用 A 型接口，并具有如下 2 种状态：

——列车处于零速度状态；

——列车处于非零速度状态。

车载 ATP/ATO 设备通过自身计算，判定列车的停车、移动状态。

##### 5.3.13.2 信号特征

车载 ATP/ATO 列车零速度信号具有两种输出状态，具体定义如下：

——控制信号为逻辑“1”表示列车处于零速度状态；

——控制信号为逻辑“0”表示列车处于非零速度状态。



### 5.4 电源及其他接口

车载 ATP/ATO 设备一般采用车辆蓄电池进行供电。供电特性按 GB/T 25119—2010 中 5.1.1 的规定。

车载 ATP/ATO 将时钟信息周期性通过 TMS 发给车辆。

## 6 机械接口

### 6.1 通用要求

通用要求具体如下：

a）车载 ATP/ATO 设备应安装在规定的设备限界范围内；



b) 车载 ATP/ATO 设备电缆应采用固定架进行固定，并遵循车辆

---

安装规范要求。

### 6.2 车内设备

#### 6.2.1 车载 ATP/ATO 主机

##### 6.2.1.1 安装位置

车载 ATP/ATO 主机应安装在车辆电气屏柜内，在电气屏柜柜门开启后应保证主机柜前留有 600 mm 的维护操作空间，主机柜上下各留有 150 mm 的走线及通风散热空间。

##### 6.2.1.2 安装空间

车辆应为车载 ATP/ATO 主机预留最小为 650 mm（宽）×580 mm（深）×1200 mm（高）的安装空间。

##### 6.2.1.3 通风

车辆提供给车载 ATP/ATO 主机安装空间内应具备良好的通风条件，车载 ATP/ATO 主机安装空间温度满足 GB/T 25119 相关环境条件。

##### 6.2.1.4 接地

车载 ATP/ATO 主机宜采用多点接地并互连，接地电缆的导体截面积应不小于  $ 10 \, mm^{2} $ ，宜采用扁平软铜绞线，长度不大于  $ 500 \, mm $ 。

#### 6.2.2 车载显示器

##### 6.2.2.1 安装位置

ATP 车载显示器安装在司机室主控台，列车司机与车载显示器之间不应有障碍物阻挡司机的视线，车载显示器不宜暴露于直射日光下。

##### 6.2.2.2 安装空间

车辆应为 ATP 车载显示器预留最小为 345 mm（宽）×250 mm（深）×250 mm（高）的安装空间，无障碍物阻挡空间为 415 mm（宽）×250 mm（深）×320 mm（高）。

##### 6.2.2.3 通风

车辆提供给 ATP 车载显示器安装空间内应具备良好的通风条件，车载显示器安装空间与司机室内温度差不宜超过  $ 5^{\circ} $ C。

##### 6.2.2.4 接地

车载显示器采用最短的路径引入最近的接地点，接地电缆的导体截

---

面积应不小于 $ 6\ mm^{2} $ 。如有颜色表示，宜用黄绿色，接地线长度应不大于500 mm。

### 6.3 车底设备

#### 6.3.1 BTM 天线

##### 6.3.1.1 安装位置

BTM 天线应安装在列车中心线上并且靠近前端车钩的位置，如图 2 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//54350439-ccf9-4113-b56b-c6d511077cc5/markdown_0/imgs/img_in_image_box_248_377_635_645.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A06Z%2F-1%2F%2Fb260d9454efbf511ca1e17a33d881b9b97b26b827cf1262bd485535453f9c161" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 2 BTM 天线安装位置</div>


BTM 天线中心线离车辆前端车钩连接面距离见表 7。

<div style="text-align: center;">表 7 中心线距离</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">车钩连接面到车载BTM天线中心线距离(单位:mm,允许误差:±10)</td></tr><tr><td colspan="2"></td><td style='text-align: center;'>L1</td><td style='text-align: center;'>L2</td></tr><tr><td colspan="2">A型车</td><td style='text-align: center;'>3 320</td><td style='text-align: center;'>4 410</td></tr><tr><td rowspan="2">B型车</td><td style='text-align: center;'>I类</td><td style='text-align: center;'>2 690</td><td style='text-align: center;'>3 750</td></tr><tr><td style='text-align: center;'>II类</td><td style='text-align: center;'>3 130</td><td style='text-align: center;'>4 190</td></tr><tr><td colspan="4">注1:L1表示水平梁安装方式下,车钩连接面到车载BTM天线中心线距离。注2:L2表示支架安装方式下,车钩连接面到车载BTM天线中心线距离。注3:I类表示头车长度为20 460 mm的车辆。注4:II类表示头车长度为20 900 mm的车辆。</td></tr></table>

---

##### 6.3.1.2 干扰防护

BTM 天线安装应避开强电磁干扰区域（如电机、风机或其他设备的天线附近），周围不应有频率为  $ 3 \, MHz \sim 5.5 \, MHz $  的信号产生源。

##### 6.3.1.3 安装空间

车载天线附近要求无金属物体，以避免对信号传输的干扰，具体要求如图3和图4所示。天线电缆及固定装置不被当作金属物。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7b93ea8a-14cb-4012-bb93-8da1d9b9db9d/markdown_0/imgs/img_in_image_box_145_336_644_574.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A09Z%2F-1%2F%2Fbd897765f39622a841efbd66a5b11fa5ffcb9a4bffaf28259aaaef6aaf4e3b37" alt="Image" width="59%" /></div>


注： $ a \geqslant 410  mm; b \geqslant 50  mm $ 。

<div style="text-align: center;">图 3 天线安装无金属区域（沿运行方向视图）</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7b93ea8a-14cb-4012-bb93-8da1d9b9db9d/markdown_0/imgs/img_in_image_box_136_681_644_891.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A09Z%2F-1%2F%2F1a465a84e8b31d79579b135f9f03de76621d8df6f4cb7646dc749c9134faf823" alt="Image" width="60%" /></div>


注： $ b \geqslant 50  mm; c \geqslant 450  mm $ 。

<div style="text-align: center;">图 4 天线安装无金属区域（侧视图）</div>


##### 6.3.1.4 安装范围

当安装车载天线时，可根据车辆的具体情况将车载天线安装于车体上或安装于转向架上。当列车处于静态、空载、新轮时，其安装容许误差见表8。

---

<div style="text-align: center;">表 8 安装容差</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>容 差 项</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>图 示</td></tr><tr><td style='text-align: center;'>至钢轨顶面的最小距离Hmin</td><td style='text-align: center;'>165 mm</td><td rowspan="2"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//60a4cfcf-ae76-46e4-89bc-7fcf647251e8/markdown_0/imgs/img_in_image_box_522_195_787_352.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A12Z%2F-1%2F%2Fa8f6cddf85d6e507e9bc049f0d3bf6ed444c4c61155b387b02c5c57217fe0132" ></td></tr><tr><td style='text-align: center;'>至钢轨顶面的最大距离Hmax</td><td style='text-align: center;'>240 mm</td></tr><tr><td style='text-align: center;'>轨道中心线和车上天线的基准点Z之间的最大偏离Ymax</td><td style='text-align: center;'>±5 mm</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//60a4cfcf-ae76-46e4-89bc-7fcf647251e8/markdown_0/imgs/img_in_image_box_519_377_784_536.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A12Z%2F-1%2F%2F0d7b663a149a90f6dd33489602f6bf38b09ad3b7663a972863739b0fac17df6c" ></td></tr><tr><td style='text-align: center;'>沿行车方向的最大侧倾角</td><td style='text-align: center;'>±1°</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//60a4cfcf-ae76-46e4-89bc-7fcf647251e8/markdown_0/imgs/img_in_image_box_519_563_783_720.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A12Z%2F-1%2F%2F0988d11c25398e19cd4daa45d1237cacb4cddbdb29c17a5b8c324f06bbceff56" ></td></tr><tr><td style='text-align: center;'>沿垂向最大倾角</td><td style='text-align: center;'>±1°</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//60a4cfcf-ae76-46e4-89bc-7fcf647251e8/markdown_0/imgs/img_in_image_box_511_753_784_874.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A12Z%2F-1%2F%2F6d23f59e25c5b10935b2c8f1a32f64b911c2cf45ea3e173e704faadfdb6ee60d" ></td></tr><tr><td style='text-align: center;'>沿垂直行车方向最大倾角</td><td style='text-align: center;'>±1°</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//60a4cfcf-ae76-46e4-89bc-7fcf647251e8/markdown_0/imgs/img_in_image_box_513_933_778_1094.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A12Z%2F-1%2F%2Fc14878dadfdf7ad24ccbf67ed72059b0c27197708cb3f173d83901dd939ca5fd" ></td></tr></table>

---

#### 6.3.2 转速传感器

##### 6.3.2.1 安装位置

轮轴转速传感器可采用接触式或非接触式，宜安装在非动力轴的轮轴端部并固定在轴端盖上。接触式轮轴转速传感器其转动部分与车辆的轮轴相连，具体安装位置由工程方案确定。

##### 6.3.2.2 安装空间

为便于电缆连接器插拔，电缆连接器应向下倾斜  $ 15^{\circ} \sim 60^{\circ} $  并且避免对连接器产生挤压。输出电缆的敷设应尽量避开减振弹簧。

轮轴转速传感器电连接器固定板安装应考虑电缆的折弯半径，折弯半径应大于150 mm。具体要求如图5所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//e73cd94f-a90e-4294-9cf4-95276a1ebb76/markdown_0/imgs/img_in_image_box_90_460_700_700.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A16Z%2F-1%2F%2F9e79b67f7109159eb9a6c41fcc7db83c366ba0a15e99746065c0488b3a15819b" alt="Image" width="72%" /></div>


<div style="text-align: center;">图 5 轮轴转速传感器安装空间</div>


#### 6.3.3 多普勒雷达传感器

##### 6.3.3.1 安装位置

雷达传感器安装在车体下方，钢轨内侧固定螺栓的正上方。两个多普勒雷达需要对称于车体中心线进行安装，同时车辆应保证两个多普勒雷达安装在不同车体侧；多普勒雷达不能安装在转向架上，多普勒雷达中心线与钢轨中心线距离为 $ 80\pm10 $  mm。其安装位置选择如图6所示。

##### 6.3.3.2 安装空间

多普勒雷达具体安装空间要求如下：

a）多普勒雷达安装在车辆提供的安装支架上。安装支架的多普勒雷达接触表面平整度小于0.5 mm，与钢轨顶面平行且距离在

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a665f413-34e4-4ae9-b826-08e416554dd7/markdown_0/imgs/img_in_image_box_84_130_794_375.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A19Z%2F-1%2F%2Fb61d2e9955e3089450b274de212f65053d69b4f4ed7a6c771efe90601d92d01b" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 6 多普勒雷达安装位置</div>


500 mm ~ 800 mm 之间。

b）多普勒雷达对安装空间的需求如图7所示。为保证雷达波被正常地发送和接收，图中的阴影区域是一个专用区域，在该区域内不能放置任何其他设备或活动物体。

单位为毫米

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a665f413-34e4-4ae9-b826-08e416554dd7/markdown_0/imgs/img_in_image_box_149_618_741_1057.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A19Z%2F-1%2F%2F2f37770f5c56f83809d7291ad9a1eb2b3a7ffef7f4eec1168bdc9e6d9baa2fd2" alt="Image" width="70%" /></div>


<div style="text-align: center;">图 7 多普勒雷达扫描范围</div>

---

#### 6.3.3 接地

接地电缆的导体截面积应不小于 $ 10\ mm^{2} $ ，宜采用扁平软铜绞线。

#### 6.3.4 加速度传感器

##### 6.3.4.1 安装位置

加速度传感器安装在车内的水平支架上，安装时应确保将加速度传感器的检测方向（单方向传感器或多方向传感器的其中一轴的检测方向）指向轨道中心线列车前进方向，即加速计顶端的箭头必须沿车辆纵向并指向车辆的前进方向。安装后应将列车停放在水平轨道进行支架找平调整，避免静止时的俯仰倾角。

安装位置宜选择车头和车尾的 ATP/ATO 主机机柜下方，两端加速度传感器宜安装在不同车体侧，宜靠近车辆的中心线。其安装位置如图 8 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//11bea5c9-243e-49c4-9993-e4774b7885e3/markdown_0/imgs/img_in_image_box_60_543_759_680.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A23Z%2F-1%2F%2Fb53b51d7619156797ff525bf1534150715f7c1785e87ed9a6b9f585943412cf2" alt="Image" width="83%" /></div>


<div style="text-align: center;">图 8 加速度传感器安装位置</div>


##### 6.3.4.2 安装空间

加速度传感器应安装在支架上，距离车体地板上面高度不宜超过100 mm。安装应满足加速度传感器尺寸、走线、测试和维护需要，加速度传感器的顶端到ATP/ATO主机机柜的底部应有足够空间，具体尺寸在工程实施阶段约定。

##### 6.3.4.3 接地

加速度传感器的接地宜采用扁平软铜绞线。

### 6.4 车载无线天线

车载无线天线具体要求如下：

a）根据车地无线通信使用传播介质的不同，车载安装不同的天线

---

或不同的天线组合，包括：自由波天线、波导天线、漏缆定向平板天线，或三种天线中不同的组合；

b）所有天线的安装均不得超出车辆限界或侵入设备限界；

c）天线安装在列车外部时，应采取防水措施，防止雨水渗入车体内。

#### 6.4.1 自由波天线

自由波天线具体要求如下：

a）自由波天线（八木天线、平板天线或鲨鱼鳍天线）用于接收无线自由波信号。

b) 列车的车头和车尾各安装两套自由波天线，天线的中心线或鳍线应与列车运行方向平行，最大允许水平角度误差  $ \pm1^{\circ} $ ，最大允许垂直角度误差  $ \pm1^{\circ} $ 。

c) 八木天线或平板天线安装在列车驾驶室顶部，需在驾驶室顶部安装平面开孔，天线前必须有一个无金属区，无金属区要求在以天线为中心的70°角范围内。安装时的无金属障碍物区示意图见图9。

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>方向</th><th style='text-align: center;'>车端</th><th style='text-align: center;'>车厢挡板</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>车顶</td><td style='text-align: center;'>70°</td><td style='text-align: center;'>70°</td></tr>
    <tr><td style='text-align: center;'>天线支架</td><td style='text-align: center;'>70°</td><td style='text-align: center;'>70°</td></tr>
    <tr><td style='text-align: center;'>天线</td><td style='text-align: center;'>70°</td><td style='text-align: center;'>70°</td></tr>
    <tr><td style='text-align: center;'>无金属区</td><td style='text-align: center;'>70°</td><td style='text-align: center;'>70°</td></tr>
  </tbody>
</table>

<div style="text-align: center;">图 9 车载天线无金属区</div>


d) 鲨鱼鳍天线应安装在列车车顶，以天线为中心、半径为1 m的范围内不应有超出天线2/3高度的金属障碍物（不含天线），且天线顶部宜与车辆静态限界包络最高值齐平。鲨鱼鳍天线安装时的无金属障碍物区示意见图10。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2783e2e9-abe4-4c77-a568-1e74083ca36d/markdown_0/imgs/img_in_image_box_70_121_722_257.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A32Z%2F-1%2F%2Fd6d2b6379387af6fb8da34bdc7639428db71fd89973b382c058e3fd63ef58537" alt="Image" width="77%" /></div>


<div style="text-align: center;">图 10 车载鲨鱼鳍天线无金属区</div>


e）同一区域安装有多套天线情况下，车载无线天线（含其他系统天线）之间的隔离距离应大于0.6 m。

f) 为确保无线信号质量，选取天线安装位置时应尽可能保证到车载无线单元的射频电缆总长度不宜大于6 m。

g）天线应安装在接地完整的金属平面上

h) 天线底座应与安装面（车顶安装座或天线安装支架）间无缝紧密接触，与接触面的平整度要求小于0.5mm。接口面与天线安装螺钉应采用防水措施，防水材料的选用应考虑后续天线维护的便利。

i) 天线安装支架若采用焊接方式固定在车体，焊接端满焊一周，焊缝处应采取防腐防锈处理。支架对应的车体开过线孔，直径不小于40 mm，支架和车体的过线孔中心点应对齐，误差不超过3 mm。开孔应去毛刺，宜采用过孔保护套进行保护。

#### 6.4.2 波导天线

波导天线具体要求如下：

a）波导天线（平板定向天线）安装于车体底部或转向架（如果车辆采用第三轨方式供电，波导天线可固定安装在车体上，且波导天线应远离第三轨接触杆，二者间距不应小于300 mm），用于接收地面波导管信号。考虑车辆实际的运行，在列车的两端各安装两个波导天线，且每端的波导天线应采用车辆运行方向中心线对称安装方式。

b）波导天线支架可焊接于车体底部，支架不应超过车体界限，支

---

架与天线接触面的平整度要求小于0.5 mm。波导天线中心与列车运行方向中心线距离为1162 mm，天线下表面与钢轨上表面距离宜为320 mm（在新轮、空载、静态情况下），安装误差不超过 $ \pm5 $  mm。波导天线安装示意如图11所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//1329da68-4855-44e0-b01c-96356b07eab7/markdown_0/imgs/img_in_image_box_139_264_727_769.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A36Z%2F-1%2F%2F93e43744af6d8201b0c79ec3d79eff2b11dbb0059be85d00520db12147c9fa0d" alt="Image" width="69%" /></div>


<div style="text-align: center;">图 11 波导天线安装示意图</div>


c）在波导天线下方100 mm，以波导天线为中心150°角形成的区域范围内，以及波导天线下方100 mm到轨面，距波导天线边沿250 mm范围内为非金属区，在该区域内应保证无金属出现。波导天线安装时的无金属区示意如图12所示。

#### 6.4.3 漏缆天线

漏缆天线具体要求如下：

a）如果现场使用漏缆作为媒介传输车地无线信息，宜采用平板定

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//84050e14-46d8-48a5-9d61-713f7a0d0610/markdown_0/imgs/img_in_image_box_34_127_748_401.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A38Z%2F-1%2F%2Fb10c9b6d48a13a4f489d8dd85456522473de56ebb106b601b43021664edc7d55" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 12 波导天线安装环境示意图</div>


向天线（安装在车底侧面）或鲨鱼鳍天线，接收轨旁漏缆辐射出的近场无线信号，定向平板天线或鲨鱼鳍天线正对漏缆开槽。

b）平板天线安装于较低位置，宜距离轨面600 mm ~ 800 mm。

c) 天线前必须有一个无金属区，无金属区要求在以天线为中心的 $ 70^{\circ} $ 角范围内。漏缆天线安装位置及安装时的无金属区示意如图13所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//84050e14-46d8-48a5-9d61-713f7a0d0610/markdown_0/imgs/img_in_image_box_118_684_656_912.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A39Z%2F-1%2F%2F52dac46517e847e4dddecd78f2779bba2bc374d705746dbaaecf0a447345fe22" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 13 漏缆天线安装示意图</div>


d）考虑车辆实际的运行，在列车的车头和车尾各安装两套漏缆天线，每端安装两个漏缆天线，列车运行方向中心线对称安装。漏缆天线距轨旁漏缆的水平距离不宜超过2 m（具体水平距离

---

根据实际工程设计确定）。

### 6.5 连接电缆

#### 6.5.1 电缆性能要求

车载信号用电缆应符合以下要求：

——电缆一般性能应满足标准 TB/T 1484 的要求；

——电缆燃烧性能应满足 GB/T 19666—2005 中成束电缆燃烧试验 C 类规定；

——电缆燃烧时的低烟性能应满足 GB/T 19666—2005 的规定（最小透光率≥80%）；

——电缆无卤指标性能应满足 GB/T 19666—2005 的规定（pH 加权值  $ \geqslant 4.3 $ ，电导率  $ \leqslant 10 $ ）。

#### 6.5.2 电缆布线与安装要求

线缆的走线及固定遵照 TB/T 3153 的要求执行：

a）电缆布放过程中注意对线缆进行保护，宜加装保护外层；裸露在机车外部线缆的转弯半径不小于200 mm，其他线缆转弯半径不小于150 mm。

b) 电缆布线时，应与大功率电器布线分开布放，避免与强电布线平行走线，如：空调电源、电机、头灯电源。与强电布线间距不应小于200 mm。

c）电缆走线应避开高温发热源，保证电缆所处环境温度不超过其允许的工作温度。

d）电缆与设备连接完成后，两端均应预留适当长度后再进行固定，便于连接器拔插，防止布线拉扯过紧，保证设备拆装方便，避免布线脱落及受力过大而造成连接器接触不良。

e）机车外部裸露电缆连接处应采取防水措施。

---

# 附录 A

# (规范性附录) 与车辆功能接口特性参数

### A. 1 A 型接口

A型接口为输出信号，应满足下述要求：

a）在驱动电压 DC 110 V 条件下，最大输出电流 200 mA；

b）开门使能信号、开/关门指令、紧急制动指令在满足相关安全约束条件下，最大输出电流可适当放宽。

A 型接口为输入信号，应满足下述要求

a）输入电流应小于20 mA；

b) 对于安全关键输入继电器触点信号，车辆提供的两组同型号继电器动作时间差应不超过 50 ms。

### A. 2 B 型接口

B型接口输入端应满足下述要求：

a） 检流电阻阻值 R 应满足：100 Ω ≤ R ≤ 500 Ω；

b) 输入端分辨率  $ R_{E} $  应满足  $ R_{E} \geq 2\% $ 

### A.3 紧急制动指令及紧急制动状态

紧急制动指令及紧急制动状态应满足表 A.1 各项要求。紧急制动响应延时见图 A.1。

<div style="text-align: center;">表 A.1 紧急制动指令及紧急制动状态特性参数表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>参数描述</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>可保证的紧急制动减速率</td><td style='text-align: center;'>列车能保证的最小的紧急制动减速率，此数值为安全相关</td><td style='text-align: center;'></td><td style='text-align: center;'>可保证的紧急制动减速率在工程中进行约定</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>牵引切除延时</td><td style='text-align: center;'>在紧急制动触发时刻若存在牵引工况，牵引切除延时所需时间</td><td style='text-align: center;'>≤0.30 s</td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 A.1 紧急制动指令及紧急制动状态特性参数表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>参数描述</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>紧急制动延迟时间</td><td style='text-align: center;'>从信号系统发出紧急制动指令到车辆施加空气制动力10%所需时间</td><td style='text-align: center;'>≤0.5s</td><td style='text-align: center;'>如图A.1中T1</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>紧急制动响应时间</td><td style='text-align: center;'>从信号系统发出紧急制动指令到车辆施加空气制动力90%所需时间</td><td style='text-align: center;'>≤1.6s</td><td style='text-align: center;'>如图A.1中T2</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>紧急制动状态反馈延时</td><td style='text-align: center;'>从信号系统发出紧急制动指令到车辆反馈紧急制动已实施的延时</td><td style='text-align: center;'>≤55ms</td><td style='text-align: center;'>从图A.1中t0至车辆紧急制动状态继电器常开触点闭合时间</td></tr><tr><td colspan="5">注:表A.1、表A.2、表A.3中相关参数均基于下述条件:在AW0、AW2及AW3载重情况下,在平直干燥轨道上,车轮为半磨耗状态,列车从最高运行速度(运营速度在120km/h及以下)到停车。</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6d735cbf-daff-4256-afb7-3a9db6140232/markdown_0/imgs/img_in_image_box_218_579_660_926.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A50Z%2F-1%2F%2F4d7defd7a6bfe8b859af013fda5165fb5a0e761b22d2ec993760314ddbdf8b6c" alt="Image" width="52%" /></div>


说明：1. 纵轴 BR 表示车辆实际制动率，其中 BR_full 表示紧急制动下最大空气制动力；

2. 横轨 t 为时间，其中  $ t_{0} $  为继电器触点闭合时间点；

3. 图中绿色点划线为示意图，非真实紧急制动制动率输出曲线；

4. 图中蓝色线条为车载 ATP/ATO 设备紧急制动输出指令。

<div style="text-align: center;">图 A.1 紧急制动响应延时</div>

---

### A. 4 常用制动相关特性参数

常用制动相关特性参数应满足表 A.2 各项要求。整车最大牵引力到最大常用制动的转换见图 A.2，整车从惰行到最大常用制动响应时间见图 A.3。

<div style="text-align: center;">表 A.2 常用制动相关特性参数表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>ATO下最大常用制动减速率</td><td style='text-align: center;'>≥1.0 m/s²</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>整车常用制动与牵引调节精度</td><td style='text-align: center;'>≤0.1 m/s²</td><td style='text-align: center;'>ATO控制下,整车常用制动与牵引最小调节量</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>整车最大牵引力到最大常用制动的转换时间</td><td style='text-align: center;'>≤3.5 s</td><td rowspan="5">整个过程由4个子过程(3.1~3.4)组成。具体参见图A.2</td></tr><tr><td style='text-align: center;'>3.1</td><td style='text-align: center;'>指令处理周期</td><td style='text-align: center;'>≤200 ms</td></tr><tr><td style='text-align: center;'>3.2</td><td style='text-align: center;'>从最大加速度降低到0的时间</td><td style='text-align: center;'>≤1.5 s</td></tr><tr><td style='text-align: center;'>3.3</td><td style='text-align: center;'>制动系统从接收命令到动作施加时间</td><td style='text-align: center;'>≤0.3 s</td></tr><tr><td style='text-align: center;'>3.4</td><td style='text-align: center;'>制动减速度从0到最大值的时间</td><td style='text-align: center;'>≤1.5 s</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>整车从惰行到最大常用制动力响应时间</td><td style='text-align: center;'>≤1.7 s</td><td style='text-align: center;'>具体参见图A.3</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//dc973274-d70d-4cc8-91ae-ba9e42b6ae4c/markdown_0/imgs/img_in_image_box_105_830_672_1084.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A53Z%2F-1%2F%2Ff437b0b7c6989d5e1163ae76dfa3fe2252f81d7908f7d502e1a0fb3cb131c668" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 A.2 整车最大牵引力到最大常用制动的转换</div>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ce244e88-95dc-40fe-bc6e-7f85e5817e0d/markdown_0/imgs/img_in_image_box_169_146_731_397.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A35%3A57Z%2F-1%2F%2F91ab67cb0b7b966e4346b320aa08a7ea83d65f53af55775891ba3fb9bcfb6488" alt="Image" width="66%" /></div>


<div style="text-align: center;">图 A.3 整车从惰行到最大常用制动响应时间</div>


### A. 5 牵引相关特性参数

牵引相关特性参数应满足表 A.3 各项要求。整车从惰行到最大牵引力的转换时间见图 A.4，整车从最大常用制动到最大牵引力转换时间见图 A.5。

<div style="text-align: center;">表 A.3 牵引相关特性参数表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>备注</td></tr><tr><td rowspan="2">1</td><td rowspan="2">整车从最大牵引力到惰行的转换时间</td><td style='text-align: center;'>$ \leq $ 1.7 s</td><td style='text-align: center;'>常用制动或惰行下的牵引消退</td></tr><tr><td style='text-align: center;'>&lt;0.2 s</td><td style='text-align: center;'>紧急制动下的牵引切除</td></tr><tr><td rowspan="2">2</td><td rowspan="2">整车从惰行到最大牵引力的转换时间</td><td style='text-align: center;'>&lt;0.2 s</td><td style='text-align: center;'>牵引延迟时间从信号系统发出牵引指令到车辆施加牵引力10%所需时间</td></tr><tr><td style='text-align: center;'>$ \leq $ 1.7 s</td><td style='text-align: center;'>牵引建立时间从信号系统发出牵引指令到车辆施加牵引力100%所需时间</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>整车从最大常用制动到最大牵引力转换时间</td><td style='text-align: center;'>$ \leq $ 3.5 s</td><td style='text-align: center;'>具体参见图A.5</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>混合制动切换速度</td><td style='text-align: center;'>4 km/h $ \leq $ v $ \leq $ 8 km/h</td><td style='text-align: center;'>混合制动期间的制动性能偏差要求 $ \leq $  $ \pm $ 10%</td></tr></table>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//146771aa-a9e8-4ae9-8b1f-e9c05068bab7/markdown_0/imgs/img_in_image_box_76_109_712_357.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A36%3A00Z%2F-1%2F%2F0a3efff6afea93ee54f14d60cfa34807b335410542ff2c44a79493629be700b6" alt="Image" width="75%" /></div>


<div style="text-align: center;">图 A.4 整车从惰行到最大牵引力的转换时间</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//146771aa-a9e8-4ae9-8b1f-e9c05068bab7/markdown_0/imgs/img_in_image_box_111_413_678_704.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A36%3A00Z%2F-1%2F%2Fd20d74401b648f9ad34b3afbad7a6c4af179053e52dd8268ed54d4eae35700ab" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 A.5 整车从最大常用制动到最大牵引力转换时间</div>


### A.6 车门控制相关参数

车门控制相关参数应满足表 A.4 各项要求。

<div style="text-align: center;">表 A.4 车门控制相关特性参数表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>参数名称</td><td style='text-align: center;'>数值</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>车门打开/关闭时间</td><td style='text-align: center;'>(3±0.5)s</td><td style='text-align: center;'>从开门动作开始到车门完全打开/关闭的时间</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>从开/关门指令发出到开/关门动作开始的延时</td><td style='text-align: center;'>0~3.0s</td><td style='text-align: center;'>该时间可调</td></tr></table>

---

T/CAMET 04011.3—2018

## 参考文献

[1]城轨车辆车载控制网络数据传送规范(第2版)

—

---

中国城市轨道交通协会团体标准

城市轨道交通 基于通信的列车运行

控制系统(CBTC)互联互通接口规范

第3部分:车载列车自动保护(ATP)/列车自动

运行(ATO)系统与车辆的接口

T/CAMET 04011.3—2018

中国铁道出版社有限公司出版发行

(100054, 北京市西城区右安门西街 8 号)

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm × 1230 mm 1/32 印张：1.625 字数：43千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5728 定价：15.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174