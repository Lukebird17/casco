# 中国城市轨道交通协会团体标准

T/CAMET 04010.4—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第4部分：互联互通危害分析

# Urban rail transit — System specification for interoperability of communication based train control system Part 4: Hazard analysis of interoperability

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
3.2 缩略语 …… 4    
4 总则 …… 5    
4.1 概述 …… 5    
4.2 系统定义和应用条件 …… 5    
5 保护对象 …… 13    
5.1 概述 …… 13    
5.2 人员 …… 13    
5.3 物资 …… 14    
6 危害识别及保障机制 …… 14    
6.1 危害识别方法说明 …… 14    
6.2 事故分析 …… 15    
6.3 危害分析 …… 17    
6.4 危害结果 …… 128    
7 安全要求 …… 135    
7.1 系统需求 …… 135    
7.2 互联互通接口需求 …… 143    
7.3 建设运营维护 …… 145    
参考文献 …… 149    
V

---

## 前言

T/CAMET 04010《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》分为以下四个部分：

——第1部分：系统总体要求；

——第2部分：系统架构和功能分配；

——第3部分：车载电子地图；

——第4部分：互联互通危害分析。

本部分是 T/CAMET 04010 的第 4 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、浙江众合科技股份有限公司、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、中铁检验认证中心。

本部分主要起草人：编写组：袁彬彬、胡妃俨、陈磊、师秀霞、朱胜远、吴炳昊、张楠乔、方力一、徐意、赵天时、郎学伟。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、张琼燕、段晨宁、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、王道敏、徐鼎。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车 运行控制系统(CBTC)互联互通系统规范 第4部分:互联互通危害分析

## 1 范围

本部分规定了城市轨道交通互联互通 CBTC 系统危害分析，包含安全职责、系统范围、保护对象、危害识别及安全要求。

本部分适用于国内采用基于通信的列车运行控制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的互联互通部分危害分析。

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 21562—2008 轨道交通 可靠性、可用性、可维修性和安全性规范及示例(IEC 62278:2002, IDT)

GB/T 21562.2—2015 轨道交通 可靠性、可用性、可维护性和安全性规范及示例 第2部分：安全性应用指南

GB/T 32588.1—2016 轨道交通 自动化的城市轨道交通(AUGT)

安全要求 第1部分: 总则 (IEC 6227:2009, MOD)

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

---

## 3 术语和缩略语

GB 50157—2013、CJ/T 407—2012 和 T/CAMET 04010.1 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

### 3.1 术语

#### 3.1.1 

基于通信的列车控制 communication based train control(CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术，连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.2 

## 正线 main line

载客列车运营的贯穿全程的线路。

[GB 50157—2013, 定义 2.0.11]

#### 3.1.3 

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.38]

#### 3.1.4 

## 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.5 

移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T 407—2012, 定义 3.1.7]

---

#### 3.1.6 

## 跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 04010.1, 定义 3.1.14]

#### 3.1.7 

## 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通安全可靠运营。

[T/CAMET 04010.1, 定义 3.1.16]

#### 3.1.8 

## 共线运行 mix operation

装备不同厂家车载信号设备的列车可以在装备同一厂家轨旁信号设备线路上支持以点式列车控制级别和连续式列车控制级别无缝安全可靠运营。

[T/CAMET 04010.2, 定义 3.1.18]

#### 3.1.9 

## 上线测试 running test

装备不同厂家车载设备的列车在本线进行动车测试。

#### 3.1.10 

## 互联互通试运营 interoperabetrial operation

装备不同厂家车载设备的列车可以在装备不同厂家轨旁设备的多条轨道交通线路上满足互联互通功能要求，且系统性能满足工程要求，开始载客运营。

#### 3.1.11 

本线 local line

指由单个集成商所负责的轨旁信号设备所对应的线路。

#### 3.1.12 

## 他线 ___ neighbouring line

---

与本线互联互通的其他线路。

#### 3.1.13 

## 单线 single line

指装备本线信号设备供应商的车载信号列车在本线线路上运行。

#### 3.1.14 

最大退行停车距离 maximum exit parking distance

最大退行停车距离 = 最大退行 EB 触发距离 + EB 制动距离。



#### 3.1.15 

最大后溜停车距离 Maximum rear slip parking distance  

最大后溜停车距离 = 最大后溜 EB 触发距离 + EB 制动距离。



### 3.2 缩略语

AM:列车自动驾驶模式(Automatic Train Operating Mode)

ATC:列车自动控制(Automatic Train Control)

ATO:列车自动运行(Automatic Train Operation)

ATP:列车自动防护(Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

BTM: 应答器传输模块 (Balise Transfer Module)

CBTC:基于通信的列车控制(Communication Based Train Control)

CI: 计算机联锁 (Computer Interlocking)

CM:列车自动防护模式(Coded Train Operating Mode)

DCS: 数据通信系统 (Data Communication System)

EUM: 非限制人工驾驶模式 (Emergency Unrestricted Train Operating Mode)

ITC: 点式运行级别 (Intermittent Train Control)

LEU: 轨旁电子单元 (Lineside Electronic Unit)

PSD:站台门(Platform Screen Door)

RM:限制人工驾驶模式(Restricted Train Operating Mode)

V0BC:车载控制器(Vehicle On-Board Controller)

ZC: 区域控制器 (Zone Controller)

---

## 4 总则

### 4.1 概述

按照 GB/T 21562—2008 规定的生命周期模型, 确定本部分危害分析和安全要求识别过程, 如图 1 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c3384089-7723-4903-89b4-6c1c95e4b8d5/markdown_0/imgs/img_in_image_box_69_278_805_807.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A22%3A40Z%2F-1%2F%2F45f3896c886b70037fe9d8327217edcbbf32eefb0738bb349cbaa5628e6c1a39" alt="Image" width="87%" /></div>


实线框过程为本规范描述范围。

<div style="text-align: center;">图 1 本规范覆盖的全生命周期阶段</div>


本规范所应用的方法（如图1中的实线框部分所示）包括：

a）定义互联互通信号系统及其应用条件；

b）在系统级级别执行初步危害分析；

c）确定安全要求。

### 4.2 系统定义和应用条件

#### 4.2.1 系统描述

城市轨道交通互联互通 CBTC 系统应具备下列功能：

---

a） 提供城市轨道交通互联互通系统的信号控制系统；

b) 按不同运营级别控制列车运营；

c） 控制列车在专用轨道上运行，含本线轨道、他线轨道和跨线轨道；

d）信号系统控制运营级别下，提供列车安全运行的条件；

e）装备不同厂家车载设备的列车可以在装备同一厂家轨旁设备线路上无缝安全可靠运营，如图2所示；

f）装备不同厂家车载设备的列车可以通互联互通联络线在装载不同厂商轨旁设备的不同线路间无缝安全可靠运营，如图3所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6e0daa72-172e-4cb6-92e7-01955b8c7299/markdown_0/imgs/img_in_image_box_72_404_783_623.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A22%3A43Z%2F-1%2F%2Fcef94d67c1b847eea6f31b1592a4e3ff16b994419891ae90a2f1d7ce139952a2" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 2 共线运行示意图</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6e0daa72-172e-4cb6-92e7-01955b8c7299/markdown_0/imgs/img_in_image_box_75_711_784_925.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A22%3A43Z%2F-1%2F%2F8041a4a315a36cc6bff772ed401eb828efe0e70a519570b21af95f9b9c88bb7d" alt="Image" width="84%" /></div>


<div style="text-align: center;">图 3 跨线运行示意图</div>


#### 4.2.2 CBTC 信号系统架构

本规范描述的危害分析适用的单线 CBTC 信号系统如图 4 所示，互联互通 CBTC 信号系统如图 5 所示：

---

注：本规范不对单线 CBTC 系统开发、实施、运营过程的危害进行分析，仅对由两个或两个以上厂家提供的 CBTC 系统中的子系统构成的互联互通 CBTC 系统进行危害分析。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//2f95261e-94e9-4334-ad86-940659eea055/markdown_0/imgs/img_in_image_box_167_227_698_840.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A22%3A46Z%2F-1%2F%2F00861c14437929660850eb29d514f9025efa342bc081ac31b31a016be71c04fe" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 4 单线 CBTC 系统架构示意图</div>


图 5 为互联互通 CBTC 信号系统各子系统间、信号系统与外部接口示意图。信号系统的功能由接口实现，即信号系统通过接口与外界系统进行交互，实现信号系统在整个轨道交通系统中的功能。信号系统与外界系统的交互可以通过物理的接口，也可以通过人员的操作、使用和维护实现。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c37546ff-c959-446c-a403-cb50ca5985fc/markdown_0/imgs/img_in_image_box_93_160_1137_711.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A22%3A48Z%2F-1%2F%2Fe98714029386badd79ffc3758700e7830fa82f18bf4b39b2005361069efc84c6" alt="Image" width="87%" /></div>


<div style="text-align: center;">图5 互联互通CBTC系统架构示意图</div>

---

#### 4.2.3 CBTC 信号系统边界

表 1 规定了本部分危害分析的系统边界。

<div style="text-align: center;">表 1 CBTC 信号系统边界</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信号系统接口</td><td style='text-align: center;'>功能边界</td><td style='text-align: center;'>交互方式及内容</td><td style='text-align: center;'>物理边界</td></tr><tr><td style='text-align: center;'>信号系统与车辆</td><td style='text-align: center;'>安全地控制列车运行（包括前进、后退、停车开门和紧急停车）；从车辆获得制动状态和车门列车完整性信息的安全状态</td><td style='text-align: center;'>信号系统向列车发送：牵引命令、切除牵引命令、制动命令、保持制动命令、紧急制动命令、开关门命令、车辆激活端命令；车辆的牵引系统、制动系统和门系统对这些命令进行响应；信号系统采集列车的状态信息：速度信息、紧急制动施加信息、方向手柄信息、门状态信息、完整性信息、网络接口内容信息</td><td style='text-align: center;'>通过继电器驱动和采集开关吊信息；通过机械结构安装车载信号设备；通过模拟电流发送模拟量信息；通过网络与通信系统接口；通过继电器，实现信号系统输入输出控制功能</td></tr><tr><td style='text-align: center;'>信号系统与站台门</td><td style='text-align: center;'>信号系统正确地控制站台门开关；获得站台门关闭且锁闭和互锁解除信息，并保证行车安全</td><td style='text-align: center;'>信号系统向站台门发送：对应侧站台门开启命令；对应侧站台门关闭命令。信号系统接收站台门的信息：站台门开启或关闭状态信息；站台门关门且锁闭，互锁解除信息</td><td style='text-align: center;'>继电器</td></tr><tr><td style='text-align: center;'>防淹门</td><td style='text-align: center;'>防淹门关闭过程及关闭后，保证列车行车安全</td><td style='text-align: center;'>防淹门关闭、开启命令及状态采集：防淹门关闭请求；允许关闭防淹门；防淹门完全开启且锁定状态</td><td style='text-align: center;'>继电器</td></tr></table>

---

<div style="text-align: center;">表 1 CBTC 信号系统边界(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信号系统接口</td><td style='text-align: center;'>功能边界</td><td style='text-align: center;'>交互方式及内容</td><td style='text-align: center;'>物理边界</td></tr><tr><td rowspan="7">信号系统与运营及操作</td><td style='text-align: center;'>信号系统建立安全的进路（全线，包括车辆段）</td><td style='text-align: center;'>通过司机对信号机显示响应实现列车在正确联锁关系的进路中行驶</td><td style='text-align: center;'>信号机（点灯状态时）</td></tr><tr><td style='text-align: center;'>信号系统实现正线、试车线移动闭塞的列车连续追踪运行安全防护和超速防护功能</td><td style='text-align: center;'>信号系统通过为列车计算移动授权来给列车发送控制命令，控制列车在安全范围内行驶</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>信号系统实现进路闭塞的列车运行安全防护和超速防护功能（正线）</td><td style='text-align: center;'>信号系统通过为列车计算移动授权来给列车发送控制命令，控制列车在安全范围内行驶</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>信号系统实现线路双向的移动闭塞的列车运行安全防护和超速防护功能（正线）</td><td style='text-align: center;'>信号系统通过为列车计算移动授权来给列车发送控制命令，控制列车在安全范围内行驶</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>信号系统向司机提供驾驶提示信息</td><td style='text-align: center;'>信号系统通过车载显示器和按钮、声音给司机提供相应的信息</td><td style='text-align: center;'>人机接口（车载显示器、车载按钮灯）</td></tr><tr><td style='text-align: center;'>信号系统允许司机对列车的运行进行干预和人工操作，包括控制列车的启动、停止、开关门和模式转换</td><td style='text-align: center;'>司机通过对驾驶室手柄和按钮的操作，实现对列车运行的控制</td><td style='text-align: center;'>人机接口（列车驾驶手柄、车载按钮及开关）</td></tr><tr><td style='text-align: center;'>信号系统对司机的操作进行安全防护</td><td style='text-align: center;'>对于司机的错误操作，信号系统的反应应该导向安全侧</td><td style='text-align: center;'>按钮/开关</td></tr></table>

---

<div style="text-align: center;">表 1 CBTC 信号系统边界(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>信号系统接口</td><td style='text-align: center;'>功能边界</td><td style='text-align: center;'>交互方式及内容</td><td style='text-align: center;'>物理边界</td></tr><tr><td rowspan="3">信号系统与运营及操作</td><td style='text-align: center;'>信号系统向调度及值班员提供线路运营信息</td><td style='text-align: center;'>信号系统通过中心和车站显示和监控设备，提供线路运营信息，供调度及值班员对线路运营进行监控</td><td style='text-align: center;'>人机接口（中心和车站 ATS 显示器）</td></tr><tr><td style='text-align: center;'>信号系统允许调度及值班员对线路运营进行控制，包括进路控制、道岔控制、设置临时限速、设置区段封锁、运行图调整、列车停站控制</td><td style='text-align: center;'>调度及值班员通过在中心或车站的监控设备的电脑终端上进行操作，对全线的运营进行干预</td><td style='text-align: center;'>人机接口（中心 ATS 显示器、中心 ATS 操作台、现地工作站显示器、现地工作站操作台）、IBP 盘</td></tr><tr><td style='text-align: center;'>信号系统对调度及值班员的操作进行安全防护</td><td style='text-align: center;'>通过规范化的操作过程，来防止操作人员的误操作</td><td style='text-align: center;'>人机接口（中心 ATS 显示器、中心 ATS 操作台、现地工作站显示器、现地工作站操作台）</td></tr><tr><td style='text-align: center;'>信号系统与维护</td><td style='text-align: center;'>信号系统需提供维护数据供维护人员下载分析；信号系统需保证维护人员维护工作的安全性</td><td style='text-align: center;'>信号系统向维护人员提供直观的设备运行状态；通过维护手册对维护作业进行约束</td><td style='text-align: center;'>面板指示灯、开关、人机界面</td></tr></table>

#### 4.2.4 列车运行安全职责

表 2 规定了 4.2.1、4.2.2、4.2.3 所描述的 CBTC 信号系统实现列车运行基本功能的安全职责。

---

<div style="text-align: center;">表 2 列车运行职责</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2" colspan="2">列车运行基本功能</td><td style='text-align: center;'>非限制人工驾驶模式</td><td style='text-align: center;'>限制人工驾驶模式</td><td style='text-align: center;'>列车自动防护下的人工驾驶模式</td><td style='text-align: center;'>列车自动驾驶模式</td></tr><tr><td style='text-align: center;'>EUM</td><td style='text-align: center;'>RM</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>AM</td></tr><tr><td rowspan="3">确保列车安全运行</td><td style='text-align: center;'>确保安全进路</td><td style='text-align: center;'>H并S(道岔控制由系统实现)</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保列车安全间隔</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保安全速度(包含:EBI、临时限速、牵引切除及恢复)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>驾驶列车运行</td><td style='text-align: center;'>控制牵引和制动(含ATP、ATO)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td></tr><tr><td rowspan="2">轨道监控</td><td style='text-align: center;'>防止和障碍物碰撞</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td style='text-align: center;'>防止和人员碰撞</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td rowspan="3">乘客乘降监控</td><td style='text-align: center;'>控制乘客通行的车门</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>防止车体之间或站台与列车之间的人员伤亡</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td style='text-align: center;'>确保安全发车条件</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td rowspan="2">单车运营</td><td style='text-align: center;'>投入或退出运营</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>监控列车状态(包含列车完整性、紧急制动实施、车门状态)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保紧急情况的检测和管理</td><td style='text-align: center;'>列车性能诊断,烟/火检测,紧急情况处理(呼叫/疏散,监控)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td colspan="6">注:H——运营人员职责;S——由信号系统实现;并——运营人员和系统共同实现安全功能。</td></tr></table>

---

## 5 保护对象

### 5.1 概述

在具体项目风险管理中进行危险分析时，应考虑可能影响人员和物资的危害。

### 5.2 人员

#### 5.2.1 概述

人员划分为乘客、公众和员工，包括外部应急服务。CBTC互联互通信号系统防护对象是乘客及员工，外部应急服务及公众不在本规范描述范围。

#### 5.2.2 乘客

通过轨道交通系统从一个车站到另一个车站，通过付费或经过授权（例如，与交通部门相关的）使用系统提供服务的人员，可根据个人意愿选择任一特定时间使用系统。

乘客对应急情况的认知水平、行动能力和反应能力是有区别的，乘客可能会：

- 携带大小、形状不一的物品：

·携带儿童或怀抱婴儿（包括婴儿车内的儿童等）；

· 是儿童；

· 行动不便(老人、身有残疾的人)；

· 理解能力受限(语言不通的、受酒精或药物影响的):

· 患有智力障碍；

· 患有听力或视力障碍等。

轨道交通主管部门应与安全主管部门协商，在风险评估中分析乘客应对能力水平的不同以及带儿童、行李和物品的情况。

#### 5.2.3 员工

受雇于轨道交通部门或其他相关机构的人员。

员工有不同类型的人员，包括：

---

·运营人员：

· 维护人员：

· 营救人员：

· 外部工作人员（例如，维护和清洁人员）。

### 5.3 物资

物资包括整个系统的基础设施、列车、CBTC互联互通系统设备、邻近系统边界的物品和系统周边设施，还有乘客携带的物品。

## 6 危害识别及保障机制

### 6.1 危害识别方法说明

本规范将互联互通信号系统作为一个完整系统来看待，根据信号系统的应用原则和以往的运营经验对信号系统的边界条件和所处环境进行分析，以识别信号系统危害。信号系统的边界将基于信号系统的设备接口，以及信号系统的主要功能来进行定义，具体参见4.2.2和4.2.3。

图3中将互联互通CBTC信号系统当作完整系统看待，通过对信号系统与外部系统的相互影响和作用识别出信号系统的危害。初步危害的识别采用至上而下的方式，系统地对信号系统设计以及操作相关的危害进行确定。根据多年来铁路行业的事故总结的经验，同时根据互联互通信号系统的使用条件，把可能产生的事故进行整理，并逐层向下分解，识别出导致事件发生的信号系统的因素。

信号系统的使用条件包括：

·列车是在轨道上运行的；

·轨道上有道岔；

· 线路上布置有信号机；

·列车是由多节且节数已知的车厢组成起来的；

·列车上有车门，以防司机与乘务人员从车上坠入路轨；

·车站上装置有站台门，以防乘客坠入路轨；

· 信号系统使用环境是封闭的；

· 线上运行车辆应被信号系统识别。

---

### 6.2 事故分析

参照 GB/T 21562.2—2015 附录 B 中危害清单及轨道交通行业事故统计及经验总结，互联互通 CBTC 信号系统可能产生的事故分为以下几种类型：撞击、脱轨、人员跌落、触电、火灾、有毒物质或气体、爆炸、辐射、干扰、环境、恶意破坏、意外和灾难。表 3 对各个事故进行了详细描述。

<div style="text-align: center;">表 3 事故分解表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>事故</td><td style='text-align: center;'>1级编号</td><td style='text-align: center;'>事故场景初步分解</td><td style='text-align: center;'>2级编号</td><td style='text-align: center;'>事故场景细化分解</td></tr><tr><td rowspan="9">撞击</td><td rowspan="4">Ref-1</td><td rowspan="4">列车与列车相撞</td><td style='text-align: center;'>Ref-1.1</td><td style='text-align: center;'>列车追尾相撞</td></tr><tr><td style='text-align: center;'>Ref-1.2</td><td style='text-align: center;'>列车侧面相撞</td></tr><tr><td style='text-align: center;'>Ref-1.3</td><td style='text-align: center;'>列车迎面相撞</td></tr><tr><td style='text-align: center;'>Ref-1.4</td><td style='text-align: center;'>列车解体导致撞车</td></tr><tr><td rowspan="4">Ref-2</td><td rowspan="4">列车与结构物或障碍物
体相撞</td><td style='text-align: center;'>Ref-2.1</td><td style='text-align: center;'>列车与侵限物体相撞</td></tr><tr><td style='text-align: center;'>Ref-2.2</td><td style='text-align: center;'>列车冲出轨道尽头，撞
到轨道终端的缓冲车挡</td></tr><tr><td style='text-align: center;'>Ref-2.3</td><td style='text-align: center;'>列车与防淹门相撞</td></tr><tr><td style='text-align: center;'>Ref-2.4</td><td style='text-align: center;'>列车与人防门相撞</td></tr><tr><td style='text-align: center;'>Ref-3</td><td style='text-align: center;'>列车撞人</td><td style='text-align: center;'>Ref-3.1</td><td style='text-align: center;'>列车撞到乘客或工作人员</td></tr><tr><td rowspan="3">脱轨</td><td rowspan="3">Ref-4</td><td rowspan="3">列车脱轨</td><td style='text-align: center;'>Ref-4.1</td><td style='text-align: center;'>列车失去运行方向引导</td></tr><tr><td style='text-align: center;'>Ref-4.2</td><td style='text-align: center;'>列车运行过程中失稳</td></tr><tr><td style='text-align: center;'>Ref-4.3</td><td style='text-align: center;'>列车脱轨侵入其他轨道</td></tr><tr><td rowspan="5">人员跌落</td><td rowspan="3">Ref-5</td><td rowspan="3">人员跌入轨道区域</td><td style='text-align: center;'>Ref-5.1</td><td style='text-align: center;'>人员从站台跌入轨道区域</td></tr><tr><td style='text-align: center;'>Ref-5.2</td><td style='text-align: center;'>人员从列车跌入轨道区域</td></tr><tr><td style='text-align: center;'>Ref-5.3</td><td style='text-align: center;'>人员被夹在列车与站台
的间隙中</td></tr><tr><td rowspan="2">Ref-6</td><td rowspan="2">人员在列车内跌倒</td><td style='text-align: center;'>Ref-6.1</td><td style='text-align: center;'>乘客在列车客室跌倒</td></tr><tr><td style='text-align: center;'>Ref-6.2</td><td style='text-align: center;'>司机等员工在司机室
跌倒</td></tr></table>

---

<div style="text-align: center;">表 3 事故分解表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>事故</td><td style='text-align: center;'>1级编号</td><td style='text-align: center;'>事故场景初步分解</td><td style='text-align: center;'>2级编号</td><td style='text-align: center;'>事故场景细化分解</td></tr><tr><td style='text-align: center;'>触电</td><td style='text-align: center;'>Ref-7</td><td style='text-align: center;'>触电</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>火灾</td><td style='text-align: center;'>Ref-8</td><td style='text-align: center;'>火灾</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>有毒物质或气体</td><td style='text-align: center;'>Ref-9</td><td style='text-align: center;'>有毒物质或气体</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>Ref-10</td><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>辐射</td><td style='text-align: center;'>Ref-11</td><td style='text-align: center;'>辐射</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="4">干扰</td><td style='text-align: center;'>Ref-12</td><td style='text-align: center;'>电磁干扰导致信号系统功能失效</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-13</td><td style='text-align: center;'>信号系统电磁干扰超标</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-14</td><td style='text-align: center;'>雷击导致系统功能失效</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-15</td><td style='text-align: center;'>系统网络受到外部入侵</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">环境因素导致失效</td><td style='text-align: center;'>Ref-16</td><td style='text-align: center;'>气候条件导致信号系统失效</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-17</td><td style='text-align: center;'>振动导致信号系统失效</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-18</td><td style='text-align: center;'>海拔条件导致信号系统失效</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>恶意破坏</td><td style='text-align: center;'>Ref-19</td><td style='text-align: center;'>人为恶意破坏</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>灾难</td><td style='text-align: center;'>Ref-20</td><td style='text-align: center;'>洪水/地震/强风</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">基础建设损坏</td><td style='text-align: center;'>Ref-21</td><td style='text-align: center;'>基础措施过度承载</td><td style='text-align: center;'>Ref-21.1</td><td style='text-align: center;'>桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故</td></tr><tr><td style='text-align: center;'>Ref-22</td><td style='text-align: center;'>基础设施沉降</td><td style='text-align: center;'>Ref-22.1</td><td style='text-align: center;'>基础设施沉降导致列车脱轨</td></tr><tr><td style='text-align: center;'>Ref-23</td><td style='text-align: center;'>基础设施坍塌</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">运营与维护过程伤害</td><td rowspan="2">Ref-24</td><td rowspan="2">维护过程中，造成人员伤亡</td><td style='text-align: center;'>Ref-24.1</td><td style='text-align: center;'>道岔动作造成维护人员伤亡</td></tr><tr><td style='text-align: center;'>Ref-24.2</td><td style='text-align: center;'>列车撞到现场维护人员</td></tr><tr><td style='text-align: center;'>Ref-25</td><td style='text-align: center;'>救援与疏散过程中，造成人员伤亡</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td></tr></table>

---

### 6.3 危害分析

根据轨道交通运营场景、互联互通 CBTC 系统架构、系统功能及互联互通接口规范，进行互联互通危害分析及安全要求识别。同时参照 CJ/T 407—2012《城市轨道交通基于通信的列车自动控制系统技术要求》进行系统功能安全要求分配，见表 4。

注：本规范适用互联互通运营场景下的 CBTC 系统的危害分析，对单线 CBTC 系统的危害不作专门分析，但是本规范分析过程中会涉及部分单线 CBTC 系统危害识别。本规范分析结果，适用于互联互通信号系统供应商、运营商的互联互通系统建设和运营维护。

本规范中的安全要求应视为基本要求，技术方案变化或特殊地理环境、社会环境、法律法规条款可能导致安全要求变更或增加，集成商应对修改或新增的安全要求进行风险评估。

<div style="text-align: center;">表4 互联互通危害分析</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="2">Ref-1.1</td><td rowspan="2">列车追尾相撞</td><td rowspan="2">PH-1</td><td rowspan="2">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td rowspan="2">SHA-1</td><td rowspan="2">列车在前后追踪运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-1</td><td style='text-align: center;'>在CBTC、ITC级别下，车载ATP应根据当前列车运行速度限制条件进行紧急制动触发速度(EBI)的计算，列车当前速度≥EBI速度时，ATP实施紧急制动</td><td style='text-align: center;'>确定制动曲线、列车速度测定、测速误差补偿</td></tr><tr><td style='text-align: center;'>SR-S-2</td><td style='text-align: center;'>车载ATP系统测速测距精度满足控车要求，且满足安装环境下的振动和气候要求，如雨雪、温度的要求。车载ATP测速测距故障时，系统应对列车实施紧急制动</td><td style='text-align: center;'>列车速度测定、测速误差补偿、紧急制动状态</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-1</td><td rowspan="6">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td rowspan="6">SHA-1</td><td rowspan="6">列车在前后追踪运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-3</td><td style='text-align: center;'>在CBTC控制级别下，ZC确定列车的运行方向和列车的运行权限，并保证前行列车和追踪列车间的安全间隔</td><td style='text-align: center;'>确定移动授权</td></tr><tr><td style='text-align: center;'>SR-I-39</td><td style='text-align: center;'>ZC子系统应能识别车载ATP系统通信中断故障，并提供防护</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-4</td><td style='text-align: center;'>联络线联锁设备建立进路时，敌对进路应相互照查</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-5</td><td style='text-align: center;'>联络线联锁设备需保证建立的进路为锁闭状态，不能迎面解锁列车运行前方的部分进路</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-6</td><td style='text-align: center;'>信号开放/进路办理检查条件应符合联锁表要求</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-7</td><td style='text-align: center;'>单列或多列车在同一区段内运行时，轨道占用检测设备应能正确判断计轴区段的占用/出清状态，符合故障导向安全原则</td><td style='text-align: center;'>进路办理</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-1</td><td rowspan="6">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td rowspan="6">SHA-1</td><td rowspan="6">列车在前后追踪运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-8</td><td style='text-align: center;'>计轴复位命令需经过二次确认</td><td style='text-align: center;'>计轴故障恢复</td></tr><tr><td style='text-align: center;'>SR-S-9</td><td style='text-align: center;'>应采用安全继电器或其他安全接口技术传输轨道的占用状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-O-1</td><td style='text-align: center;'>营运责任方制定计轴直接复位的操作规范，运营人员必须确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-10</td><td style='text-align: center;'>互联互通公用电子地图应包含车载ATP计算EBI的所有线路数据，包含线路静态限速、坡度信息、道岔</td><td style='text-align: center;'>电子地图技术规范“线路数据”</td></tr><tr><td style='text-align: center;'>SR-I-40</td><td style='text-align: center;'>CBTC控制级别下，临时限速应被正确设置，ZC子系统应能正确处理并正确传输给车载ATP</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-1</td><td style='text-align: center;'>CBTC级别下，车载ATP系统计算EBI时正确使用临时限速</td><td style='text-align: center;'>V0BC-ZC接口规范“临时限速信息”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-1</td><td rowspan="6">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td rowspan="4">SHA-1</td><td rowspan="4">列车在前后追踪运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-O-2</td><td style='text-align: center;'>非CBTC级别下，临时限速信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定临时限速操作规程，确保临时限速信息及时传递到司机</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>VOBC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>VOBC-ZC接口规范“安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-S-12</td><td style='text-align: center;'>互联互通联络线ZC交接时，本线ZC应保证为他线CBTC列车计算MA的正确</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">IHA-1</td><td rowspan="2">列车编组信息与车长不匹配</td><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-14</td><td style='text-align: center;'>VOBC-ZC接口信息应包含互联互通列车车长信息</td><td style='text-align: center;'>VOBC-ZC接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-1</td><td rowspan="5">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td rowspan="5">HHA-2</td><td rowspan="5">联络线交接时，通信延时导致列车在本线丢失</td><td style='text-align: center;'>SR-S-96</td><td style='text-align: center;'>故障管理</td></tr><tr><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>列车交接过程中，ZC-ZC通信中断时，车载ATP应保证列车在当前ZC分界点停车或紧急停车</td></tr><tr><td style='text-align: center;'>SR-S-16</td><td style='text-align: center;'>SC应对管辖范围内的列车进行识别和跟踪，保证列车序列正确，并根据列车安全位置及进路信息，为CBTC级别列车计算MA</td></tr><tr><td style='text-align: center;'>SR-S-17</td><td style='text-align: center;'>SC交接</td></tr><tr><td style='text-align: center;'>SR-S-18</td><td style='text-align: center;'>SC应对管辖范围内的所有共线、跨线运营列车ID进行管理，对各CBTC列车ID进行唯一检查，发现本ZC管辖范围重复ID时，重复ID列车降级运行；发现向接管ZC申请授权列车重复ID时，ZC则拒绝该车的报文，不让成功建链</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>互联互通信号系统</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-1</td><td rowspan="4">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线CBTC、ITC车辆</td><td style='text-align: center;'>HSA-3</td><td style='text-align: center;'>联络线交接时，通信延时导致列车在他线丢失</td><td style='text-align: center;'>联络线车辆交接时，车载ATP应能正确处理此线ZC发送的MA</td></tr><tr><td style='text-align: center;'>HRA-3</td><td style='text-align: center;'>HRA-3</td><td style='text-align: center;'>联络线车辆交接时，车载ATP应能正确处理此线ZC发送的MA</td></tr><tr><td style='text-align: center;'>HRA-4</td><td style='text-align: center;'>HRA-4</td><td style='text-align: center;'>联络线车辆交接时，车载ATP应能正确处理此线ZC发送的MA</td></tr><tr><td style='text-align: center;'>HRA-</td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-1</td><td rowspan="6">跨线运营时，本线列车移动授权错误，导致本线CBTC、ITC列车行驶至联络线撞击联络线CBTC、ITC车辆</td><td style='text-align: center;'>IHA-5</td><td style='text-align: center;'>联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="5">IHA-6</td><td rowspan="5">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-2</td><td rowspan="5">SHA-2</td><td rowspan="5">后车MA计算未计算前车最大退行停车距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-14</td><td style='text-align: center;'>V0BC-ZC接口信息应包含互联互通列车车长信息</td><td style='text-align: center;'>V0BC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-27</td><td style='text-align: center;'>车载ATP将实际速度与当前EBI进行比较，如果实际速度≥监控速度，应输出紧急制动命令</td><td style='text-align: center;'>列车超速防护、列车速度测定、测速误差补偿</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-2</td><td rowspan="4">跨线运营时，本线CBTC列车进行撞击联络线CBTC列车</td><td rowspan="4">SHA-3</td><td rowspan="4">列车动作违反了信号系统授权时，车载ATP没有有效输出紧急制动</td><td style='text-align: center;'>SR-S-28</td><td style='text-align: center;'>车载ATP系统监督列车的退行速度和退行距离，列车退行超过允许退行速度或最大退行EB触发距离后，将实施紧急制动</td><td style='text-align: center;'>退行防护、列车速度测定、测速误差补偿</td></tr><tr><td style='text-align: center;'>SR-S-29</td><td style='text-align: center;'>车载ATP系统监督列车的后溜速度和后溜距离，列车后溜超过允许后溜速度或最大后溜EB触发距离后，列车将实施紧急制动</td><td style='text-align: center;'>列车运行方向确定、列车运行方向防护、列车速度测定、测速误差补偿</td></tr><tr><td style='text-align: center;'>SR-S-30</td><td style='text-align: center;'>在车辆保证紧急制动力正常的前提下，车载ATP向车辆输出的紧急制动命令须能保证列车在安全制动距离范围完全停稳</td><td style='text-align: center;'>越过移动授权终点防护、移动授权更新超时超速防护</td></tr><tr><td style='text-align: center;'>SR-S-31</td><td style='text-align: center;'>车载ATP一旦开始向车辆输出紧急制动命令，在紧急制动触发条件解除前，ATP不能自行缓解紧急制动</td><td style='text-align: center;'>紧急制动缓解</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="3">PH-2</td><td rowspan="3">跨线运营时，本线CBTC列车退行撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-4</td><td style='text-align: center;'>车载ATP紧急制动输出故障</td><td style='text-align: center;'>SR-1-9</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术传输车辆实施紧急制动命令及采集紧急制动状态信息</td><td style='text-align: center;'>紧急制动状态</td></tr><tr><td style='text-align: center;'>OSHA-1</td><td style='text-align: center;'>车辆紧急制动系统失效</td><td style='text-align: center;'>SR-O-3</td><td style='text-align: center;'>车辆采购及维护符合车辆专业相关规定，并满足信号系统输出的安全要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制的退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">PH-3</td><td rowspan="2">跨线运营时，本线CBTC列车后溜撞击联络线CBTC列车</td><td rowspan="2">SHA-6</td><td rowspan="2">后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="3">PH-3</td><td rowspan="3">跨线运营时，本线CBTC列车后溜撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-7</td><td style='text-align: center;'>ZC计算MA未包含前车最大后溜距离</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权</td></tr><tr><td style='text-align: center;'>IHA-1</td><td style='text-align: center;'>列车编组信息与车长不匹配</td><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-8</td><td style='text-align: center;'>CBTC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">PH-4</td><td rowspan="2">跨线运营时，本线CBTC列车退行撞击联络线ITC列车</td><td rowspan="2">SHA-2</td><td rowspan="2">后车MA计算未计算前车最大退行停车距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="4">PH-4</td><td rowspan="4">跨线运营时，本线CBTC列车退行撞击联络线ITC列车</td><td style='text-align: center;'>SHA-9</td><td style='text-align: center;'>ITC列车VOBC计算MA（防护点）未包含前车最大退行距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>IHA-1</td><td style='text-align: center;'>列车编组信息与车长不匹配</td><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-5</td><td style='text-align: center;'>跨线运营时，本线ITC列车退行撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-2</td><td style='text-align: center;'>后车MA计算未计算前车最大退行停车距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-5</td><td rowspan="4">跨线运营时,本线ITC列车退行撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-2</td><td style='text-align: center;'>后车MA计算未计算前车最大退行停车距离</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>IHA-1</td><td style='text-align: center;'>列车编组信息与车长不匹配</td><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-11</td><td style='text-align: center;'>ITC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-6</td><td rowspan="5">跨线运营时，本线CBTC列车后溜撞击联络线ITC列车</td><td rowspan="2">SHA-6</td><td rowspan="2">后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-9</td><td style='text-align: center;'>ITC列车VOBC计算MA（防护点）未包含前车最大退行距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算段线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>IHA-1</td><td style='text-align: center;'>列车编组信息与车长不匹配</td><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td style='text-align: center;'>PH-6</td><td style='text-align: center;'>跨线运营时,本线CBTC列车后溜撞击联络线ITC列车</td><td style='text-align: center;'>SHA-8</td><td style='text-align: center;'>CBTC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离;列车后溜超过互联互通最大后溜停车距离时,车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-7</td><td rowspan="3">跨线运营时,本线ITC列车后溜撞击联络线CBTC列车</td><td rowspan="2">SHA-6</td><td rowspan="2">后车MA计算未包含前车最大后溜停车距离,最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下,ZC计算MA时,应包含运行前方列车最大后溜停车距离;ITC级别下,车载ATP计算MA时,应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离;列车后溜超过互联互通最大后溜停车距离时,车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td style='text-align: center;'>PH-7</td><td style='text-align: center;'>跨线运营时,本线ITC列车后溜撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-12</td><td style='text-align: center;'>ITC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-8</td><td rowspan="3">跨线运营时,本线CBTC列车退行撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害
编号</td><td rowspan="2">互联互通信号系
统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车
追尾相
撞</td><td rowspan="4">PH-9</td><td rowspan="4">跨线运
营时,本线
RM模式列
车退行撞
击联络线
CBTC列车</td><td rowspan="2">SHA-2</td><td rowspan="2">后车MA计
算未计算前车
最大退行停车
距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下,ZC计算MA
时,应包含运行前方列车最大
退行停车距离;ITC级别下,车
载ATP计算MA时,应包含运
行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移
动授权、确
定目标点</td></tr><tr><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC
级别下移动授权防护中最大退
行停车距离应≥各厂商本线的
最大退行停车距离;列车退行
超过互联互通最大退行停车距
离时,车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设
计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应
计算慢线计轴、列车悬垂距离、
通信延迟、列车最大退行/后溜
停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-2</td><td style='text-align: center;'>联锁级别
下,司机无限
制地退行</td><td style='text-align: center;'>SR-O-5</td><td style='text-align: center;'>统一RM/EUM模式最大退
行距离及退行作业细则</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-10</td><td style='text-align: center;'>跨线运
营时,本线
CBTC列车
后溜撞击
联络线RM
模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设
计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应
计算慢线计轴、列车悬垂距离、
通信延迟、列车最大退行/后溜
停车距离</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="2">PH-10</td><td rowspan="2">跨线运营时，本线CBTC列车后溜撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-8</td><td style='text-align: center;'>CBTC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">PH-11</td><td rowspan="2">跨线运营时，本线RM模式列车后溜撞击联络线CBTC列车</td><td rowspan="2">SHA-6</td><td rowspan="2">后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="2">PH-11</td><td rowspan="2">跨线运营时，本线RM模式列车后溜撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-2</td><td style='text-align: center;'>联锁级别下，司机无限制地退行</td><td style='text-align: center;'>SR-O-5</td><td style='text-align: center;'>统一RM/EUM模式最大退行距离及退行作业细则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-12</td><td rowspan="3">跨线运营时，本线CBTC列车退行撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-13</td><td rowspan="4">跨线运营时，本线切除ATP列车或未装备ATP列车退行撞击联络线CBTC列车</td><td rowspan="2">SHA-6</td><td rowspan="2">后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-4</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机无限制地退行</td><td style='text-align: center;'>SR-O-5</td><td style='text-align: center;'>统一RM/EUM模式最大退行距离及退行作业细则</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-14</td><td rowspan="4">跨线运营时,本线CBTC列车后溜撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算促线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车后机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车,司机按照联锁信号或人工调度行车,行车安全由司机保障</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离;列车退行超过互联互通最大退行停车距离时,车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-8</td><td style='text-align: center;'>CBTC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离;列车后溜超过互联互通最大后溜停车距离时,车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="3">PH-15</td><td rowspan="3">跨线运营时，本线切除ATP列车或未装备ATP列车后溜撞击联络线CBTC列车</td><td style='text-align: center;'>SHA-6</td><td style='text-align: center;'>后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仪表线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-5</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车无限制后溜</td><td style='text-align: center;'>SR-O-7</td><td style='text-align: center;'>统一EUM模式列车后溜防护细则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">PH-16</td><td rowspan="2">跨线运营时，本线ITC级别列车后溜撞击联络线ITC列车</td><td style='text-align: center;'>SHA-6</td><td style='text-align: center;'>后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SHA-9</td><td style='text-align: center;'>ITC列车VOBC计算MA（防护点）未包含前车最大退行距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="2">PH-16</td><td rowspan="2">跨线运营时，本线ITC级别列车后溜撞击联络线ITC列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仪线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-12</td><td style='text-align: center;'>ITC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">PH-17</td><td rowspan="2">跨线运营时，本线ITC级别列车退行撞击联络线ITC列车</td><td style='text-align: center;'>SHA-2</td><td style='text-align: center;'>后车MA计算未计算前车最大退行停车距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SHA-9</td><td style='text-align: center;'>ITC列车VOBC计算MA（防护点）未包含前车最大退行距离</td><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="2">PH-17</td><td rowspan="2">跨线运营时，本线ITC级别列车退行撞击联络线ITC列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仪线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-11</td><td style='text-align: center;'>ITC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-18</td><td rowspan="3">跨线运营时，本线ITC级别列车退行撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仪线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-11</td><td style='text-align: center;'>ITC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr></table>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td rowspan="5">PH-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-19</td><td rowspan="5">跨线运营时，ITC级别列车后溜撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仅线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>车司机未按联锁信号行车</td><td style='text-align: center;'>SR-S-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td></tr><tr><td style='text-align: center;'>SHA-12</td><td style='text-align: center;'>ITC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td></tr><tr><td rowspan="2">SHA-20</td><td style='text-align: center;'>跨线运营时，ITC级别列车退行撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算仅线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td></tr><tr><td style='text-align: center;'>SHA-11</td><td style='text-align: center;'>ITC列车无限制地退行</td><td style='text-align: center;'>SR-S-25</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td style='text-align: center;'>PH-20</td><td style='text-align: center;'>跨线运营时，ITC级别列车退行撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-21</td><td rowspan="3">跨线运营时，ITC级别列车后溜撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算促线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-12</td><td style='text-align: center;'>ITC列车无限制地向后溜车</td><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="3">PH-22</td><td rowspan="3">跨线运营时，RM模式列车退行撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-2</td><td style='text-align: center;'>联锁级别下，司机无限制地退行</td><td style='text-align: center;'>SR-O-5</td><td style='text-align: center;'>统一RM/EUM模式最大退行距离及退行作业细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-23</td><td rowspan="3">跨线运营时，RM模式列车后溜撞击联络线RM模式列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-6</td><td style='text-align: center;'>RM模式列车无限制后溜</td><td style='text-align: center;'>SR-O-7</td><td style='text-align: center;'>统一EUM模式列车后溜防护细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="3">PH-24</td><td rowspan="3">跨线运营时，RM模式列车退行撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-2</td><td style='text-align: center;'>联锁级别下，司机无限制地退行</td><td style='text-align: center;'>SR-O-5</td><td style='text-align: center;'>统一RM/EUM模式最大退行距离及退行作业细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-25</td><td rowspan="3">跨线运营时，RM模式列车后溜撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-6</td><td style='text-align: center;'>RM模式列车无限制后溜</td><td style='text-align: center;'>SR-O-7</td><td style='text-align: center;'>统一EUM模式列车后溜防护细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="3">PH-26</td><td rowspan="3">跨线运营时，切除ATP列车或未装备ATP列车进行撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-4</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机无限制地退行</td><td style='text-align: center;'>SR-0-5</td><td style='text-align: center;'>统一RM/EUM模式及大退行距离及退行作业细则</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-0-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-27</td><td rowspan="3">跨线运营时，切除ATP列车或未装备ATP列车后溜撞击联络线切除ATP列车或未装备ATP列车</td><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-5</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车无限制后溜</td><td style='text-align: center;'>SR-0-7</td><td style='text-align: center;'>统一EUM模式列车后溜防护细则</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-0-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td style='text-align: center;'>PH-28</td><td style='text-align: center;'>跨ZC-ZC通信延迟</td><td style='text-align: center;'>SHA-14</td><td style='text-align: center;'>联络线交接时，由于通信延迟导致列车在本线丢失</td><td style='text-align: center;'>SR-S-35</td><td style='text-align: center;'>互联互通线路应规范ZC-ZC间通信延时时间，超时应判断为通信中断，ZC回缩移动授权至ZC边界前一计轴入口点撤回一个最大允许安装误差处</td><td style='text-align: center;'>故障管理</td></tr><tr><td rowspan="4">PH-29</td><td rowspan="4">共线运行时，他线CBTC列车计算错误的EBI，导致行车事故</td><td rowspan="4">SHA-15</td><td rowspan="4">列车位置计算错误，导致当前位置EBI计算过高</td><td style='text-align: center;'>SR-S-2</td><td style='text-align: center;'>车载ATP系统测速测距精度满足控车要求，且满足安装环境下的振动和气候要求，如雨雪、温度的要求车载ATP测速测距故障时，系统应对列车实施紧急制动</td><td style='text-align: center;'>列车速度测定、测速误差补偿、紧急制动状态</td></tr><tr><td style='text-align: center;'>SR-I-10</td><td style='text-align: center;'>统一互联互通ZC-V0BC接口，保证接口数据全面、正确</td><td style='text-align: center;'>V0BC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-36</td><td style='text-align: center;'>车载ATP计算列车安全包络时，应包含列车当前速度、加速度、测速测距误差、轨旁设备安装误差及通信延时时间（速度信号生成至车载ATP位置计算完成时间）</td><td style='text-align: center;'>确定前方CBTC列车位置、确定移动授权</td></tr><tr><td style='text-align: center;'>SR-I-11</td><td style='text-align: center;'>V0BC-II接口信息包含列车前后端安全包络信息</td><td style='text-align: center;'>V0BC-ZC接口规范“列车包络线”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="7">Ref-1.1</td><td rowspan="7">列车追尾相撞</td><td rowspan="7">PH-29</td><td rowspan="7">共线运行时,他线CBTC列车计算错误的EBI,导致行车事故</td><td style='text-align: center;'>SHA-15</td><td style='text-align: center;'>列车位置计算错误,导致当前位置EBI计算过高</td><td style='text-align: center;'>SR-1-12</td><td style='text-align: center;'>V0BC-12接口信息包含列车当前速度及速度方向</td><td style='text-align: center;'>V0BC-ZC接口规范“运行方向”、“列车速度/距离信息”</td></tr><tr><td rowspan="6">SHA-16</td><td rowspan="6">线路数据错误导致EBI计算错误</td><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范,确保数据全面、正确,该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-37</td><td style='text-align: center;'>地面设备提供商应保证线路限速数据(弯道、站台、线路最高限速)正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-38</td><td style='text-align: center;'>地面设备提供商应保证线路坡度数据正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-39</td><td style='text-align: center;'>地面设备提供商应保证道岔限速数据正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-40</td><td style='text-align: center;'>车载设备提供方应保证列车构造速度数据正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-41</td><td style='text-align: center;'>地面设备提供商应保证线路道岔位置数据正确</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="8">Ref-1.1</td><td rowspan="8">列车追尾相撞</td><td rowspan="8">PH-29</td><td rowspan="8">共线运行时,他线CBTC列车计算错误的EBI,导致行车事故</td><td rowspan="2">SHA-16</td><td rowspan="2">线路数据错误导致EBI计算错误</td><td style='text-align: center;'>SR-S-42</td><td style='text-align: center;'>地面设备提供商应保证列车在各站台开关站台门信息数据正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-43</td><td style='text-align: center;'>地面设备提供商应保证线路紧急关闭按钮信息正确</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="6">SHA-17</td><td rowspan="6">线路障碍物状态信息错误导致EBI计算错误</td><td style='text-align: center;'>SR-S-44</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集道岔的状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-13</td><td style='text-align: center;'>CI采用安全继电器或其他安全接口技术采集站台门状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-45</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集紧急关闭按钮状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-14</td><td style='text-align: center;'>ZC-I-14接口信息包含道岔状态信息</td><td style='text-align: center;'>V0BC-ZC接口规范“路径信息”</td></tr><tr><td style='text-align: center;'>SR-I-15</td><td style='text-align: center;'>ZC-I-15接口信息包含站台门状态信息</td><td style='text-align: center;'>V0BC-ZC接口规范“PSD状态”</td></tr><tr><td style='text-align: center;'>SR-I-16</td><td style='text-align: center;'>ZC-I-16接口信息包含紧急关闭按钮状态信息</td><td style='text-align: center;'>V0BC-ZC接口规范“ESB状态”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-29</td><td rowspan="5">共线运行时,他线CBTC列车计算错误的EBI,导致行车事故</td><td rowspan="3">SHA-18</td><td rowspan="3">CBTC级别下,临时限速未正确传输至车载ATP系统</td><td style='text-align: center;'>SR-S-46</td><td style='text-align: center;'>CBTC级别下,车载ATP计算EBI曲线时,应包含互联互通临时限速</td><td style='text-align: center;'>列车超速防护、确定制动曲线</td></tr><tr><td style='text-align: center;'>SR-I-17</td><td style='text-align: center;'>ZC-I-17接口信息包含临时限速信息</td><td style='text-align: center;'>V0BC-ZC接口规范“临时限速信息”</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr><tr><td rowspan="2">IHA-7</td><td rowspan="2">共线V0BCZC通信故障判断不及时,导致应回撤的MA未及时回撤</td><td style='text-align: center;'>SR-I-18</td><td style='text-align: center;'>V0BC-ZC通信中断判断时间应统一,并满足本团体标准要求</td><td style='text-align: center;'>V0BC-ZC接口规范“ZC和V0BC应能分别对通信连接状态进行判断”</td></tr><tr><td style='text-align: center;'>SR-O-8</td><td style='text-align: center;'>V0BC-ZC通信判断中断过程中,由于信号系统故障或其他突发事件导致MA回撤,V0BC未能及时接收从而导致的行车风险无法通过信号系统防护</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-30</td><td rowspan="6">共线运行时,他线ITC列车计算错误的EBI,导致行车事故</td><td rowspan="6">SHA-19</td><td rowspan="6">ITC级别下,车载MA计算错误</td><td style='text-align: center;'>SR-S-47</td><td style='text-align: center;'>统一互联互通应答器报文格式,保证接口数据全面、正确</td><td style='text-align: center;'>应答器报文规范</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范,确保数据全面、正确,该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-48</td><td style='text-align: center;'>ITC车载ATP计算MA终点时,应回撤安全防护距离</td><td style='text-align: center;'>确定移动授权、确定目标点</td></tr><tr><td style='text-align: center;'>SR-S-49</td><td style='text-align: center;'>地面设备提供商应保证主应答器报文数据正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-50</td><td style='text-align: center;'>主应答器报文应包含道岔状态信息</td><td style='text-align: center;'>应答器报文规范“公共信息包定义(203子包)”</td></tr><tr><td style='text-align: center;'>SR-S-51</td><td style='text-align: center;'>主应答器报文应包含联锁与LEU通信状态信息</td><td style='text-align: center;'>应答器报文规范“应答器默认报文”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-30</td><td rowspan="5">共线运行时,他线ITC列车计算错误的EBI,导致行车事故</td><td rowspan="2">SHA-19</td><td rowspan="2">ITC级别下,车载MA计算错误</td><td style='text-align: center;'>SR-S-52</td><td style='text-align: center;'>主应答器报文应包含LEU与应答器通信状态信息</td><td style='text-align: center;'>应答器报文规范“LEU 默认报文”</td></tr><tr><td style='text-align: center;'>SR-S-53</td><td style='text-align: center;'>如应答器实际位置与电子地图图位登偏差超出安全距离,车辆ATP系统应能判断出,并导向安全侧处理</td><td style='text-align: center;'>防护列车丢失位置报告</td></tr><tr><td rowspan="3">IHA-8</td><td rowspan="3">共线车地应答器通信故障</td><td style='text-align: center;'>SR-S-54</td><td style='text-align: center;'>他线列车应丢弃本线应答器报文自定义包</td><td style='text-align: center;'>应答器报文规范“自定义包”</td></tr><tr><td style='text-align: center;'>SR-S-55</td><td style='text-align: center;'>在应答器开窗范围内,未能完成本轮通信,应判定应答器丢失</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-O-2</td><td style='text-align: center;'>非CBTC级别下,临时限速信息不能通过信号系统传递到车载ATP系统进行防护,运营责任方应制定临时限速操作规程,确保临时限速信息及时传递到司机</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-31</td><td rowspan="4">共线运行时,本线ZC系统为他线车载ATP计算了错误的MA,导致行车事故</td><td rowspan="3">SHA-20</td><td rowspan="3">运行方向错误导致ZCMA计算错误,从而导致行车事故</td><td style='text-align: center;'>SR-S-2</td><td style='text-align: center;'>车载ATP系统测速测距精度满足控车要求,且满足安装环境下的振动和气候要求,如雨雪、温度的要求 车载ATP测速测距故障时,系统应对列车实施紧急制动</td><td style='text-align: center;'>列车速度测定、测速误差补偿、紧急制动状态</td></tr><tr><td style='text-align: center;'>SR-S-56</td><td style='text-align: center;'>ZC计算列车MA时,应检查列车运行方向和进路一致性</td><td style='text-align: center;'>确定移动授权、确定前方安全进路限制、列车运行方向确定</td></tr><tr><td style='text-align: center;'>SR-I-12</td><td style='text-align: center;'>V0BC-ZC接口信息包含列车当前速度及速度方向</td><td style='text-align: center;'>V0BC-ZC接口规范“运行方向”、“列车速度/距离信息”</td></tr><tr><td style='text-align: center;'>SHA-21</td><td style='text-align: center;'>列车折返过程中,ATP错误输出激活端信息,导致ZC错误控制列车</td><td style='text-align: center;'>SR-S-57</td><td style='text-align: center;'>列车折返换端过程中,车载ATP应保证列车不能移动</td><td style='text-align: center;'>列车折返</td></tr></table>

---

<div style="text-align: center;">表4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="5">PH-31</td><td rowspan="5">共线运行时,本线ZC系统为他线车载ATP计算了错误的MA,导致行车事故</td><td rowspan="5">SHA-22</td><td rowspan="5">列车安全位置输出错误,导致地面ZC为该列车或道路该列车的其他列车MA计算错误</td><td style='text-align: center;'>SR-S-2</td><td style='text-align: center;'>车载ATP系统测速测距精度满足控车要求,且满足安装环境下的振动和气候要求,如雨雪、温度的要求。车载ATP测速测距故障时,系统应对列车实施紧急制动</td><td style='text-align: center;'>列车速度测定、测速误差补偿、紧急制动状态</td></tr><tr><td style='text-align: center;'>SR-S-38</td><td style='text-align: center;'>列车测速测距系统应能准确判断出列车的速度和方向</td><td style='text-align: center;'>列车运行方向确定</td></tr><tr><td style='text-align: center;'>SR-I-12</td><td style='text-align: center;'>V0BC-12接口信息包含列车当前速度及速度方向</td><td style='text-align: center;'>V0BC-ZC接口规范“运行方向”、“列车速度/距离信息”</td></tr><tr><td style='text-align: center;'>SR-S-36</td><td style='text-align: center;'>车载ATP计算列车安全包络时,应包含列车当前速度、加速度、测速测距误差、轨旁设备安装误差及通信延时时间(速度信号生成至车载ATP位置计算完成时间)</td><td style='text-align: center;'>确定前方CBTC列车位置、确定移动授权</td></tr><tr><td style='text-align: center;'>SR-I-11</td><td style='text-align: center;'>V0BC-11接口信息包含列车前后端安全包络信息</td><td style='text-align: center;'>V0BC-ZC接口规范“列车包络线”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.1</td><td rowspan="6">列车追尾相撞</td><td rowspan="6">PH-31</td><td rowspan="6">共线运行时,本线ZC系统为他线车载ATP计算了错误的MA,导致行车事故</td><td rowspan="6">SHA-22</td><td rowspan="6">列车安全位置输出错误,导致地面ZC为该列车或追踪该列车的其他列车MA计算错误</td><td style='text-align: center;'>SR-S-28</td><td style='text-align: center;'>车载ATP系统监督列车地退行速度和退行距离,列车退行超过允许退行速度或最大退行EB触发距离后,将实施紧急制动</td><td style='text-align: center;'>退行防护、列车速度测定、测速误差补偿</td></tr><tr><td style='text-align: center;'>SR-I-19</td><td style='text-align: center;'>V0BC-19接口信息包含列车退行距离</td><td style='text-align: center;'>V0BC-ZC接口规范“列车速度/距离信息”</td></tr><tr><td style='text-align: center;'>SR-S-29</td><td style='text-align: center;'>车载ATP系统监督列车的后溜速度和后溜距离,列车后溜超过允许后溜速度或最大后溜EB触发距离后,列车将实施紧急制动</td><td style='text-align: center;'>列车运行方向确定、列车运行方向防护、列车速度测定、测速误差补偿</td></tr><tr><td style='text-align: center;'>SR-I-20</td><td style='text-align: center;'>V0BC-20接口信息包含列车后溜距离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-59</td><td style='text-align: center;'>车载ATP应能正确判断出列车停准停稳状态</td><td style='text-align: center;'>零速状态确定</td></tr><tr><td style='text-align: center;'>SR-I-21</td><td style='text-align: center;'>V0BC-21接口信息包含列车停准停稳信息</td><td style='text-align: center;'>V0BC-ZC接口规范“列车速度/距离信息”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="3">PH-31</td><td rowspan="3">共线运行时,本线ZC系统为他线车载ATP计算了错误的MA,导致行车事故</td><td rowspan="3">SHA-23</td><td rowspan="3">列车运行控制级别、驾驶模式传输错误,导致地面ZC为该列车或追踪该列车的其他列车MA计算错误</td><td style='text-align: center;'>SR-S-60</td><td style='text-align: center;'>ZC系统应对在线运行列车控制级别或驾驶模式进行管理</td><td style='text-align: center;'>模式转换</td></tr><tr><td style='text-align: center;'>SR-S-61</td><td style='text-align: center;'>ZC系统为CBTC列车计算MA时,应识别前车运行级别及其后端安全包络</td><td style='text-align: center;'>模式转换、确定移动授权</td></tr><tr><td style='text-align: center;'>SR-I-22</td><td style='text-align: center;'>V0BC-22接口信息包含列车列车控制级别、驾驶模式</td><td style='text-align: center;'>V0BC-ZC接口规范“列车运行控制级别”、“列车驾驶模式”</td></tr><tr><td rowspan="2">PH-32</td><td rowspan="2">停车保证输出错误,导致联锁错误解锁进路</td><td rowspan="2">SHA-24</td><td rowspan="2">列车停车保证计算错误</td><td style='text-align: center;'>SR-S-62</td><td style='text-align: center;'>车载ATP系统停车保证功能,应包含列车当前位置、速度、安全防护距离</td><td style='text-align: center;'>越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.1</td><td rowspan="4">列车追尾相撞</td><td rowspan="4">PH-33</td><td rowspan="4">保护区段允许解锁</td><td rowspan="4">SHA-25</td><td rowspan="4">列车输出保护区段允许解锁信息后，列车不安全启动</td><td style='text-align: center;'>SR-S-63</td><td style='text-align: center;'>列车仅在保证列车不会进入前方保护区段后，才能发出保护区段允许解锁</td><td style='text-align: center;'>越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>SR-S-64</td><td style='text-align: center;'>在联锁无法接收ATP发送的停稳信息时，采用计时方式判定停稳，计时时间应根据列车停稳计算取最大值</td><td style='text-align: center;'>越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>SR-I-23</td><td style='text-align: center;'>V0BC-23接口信息应包含保护区段允许解锁信息</td><td style='text-align: center;'>V0BC-CI接口规范“允许保护区段解锁命令”</td></tr><tr><td style='text-align: center;'>SR-I-24</td><td style='text-align: center;'>V0BC和CI间通信采用RSSP-Ⅱ标准安全通信协议</td><td style='text-align: center;'>V0BC-CI接口规范“RSSP-Ⅱ标准安全通信协议”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.1</td><td rowspan="5">列车追尾相撞</td><td rowspan="2">PH-33</td><td rowspan="2">保护区段允许解锁</td><td rowspan="2">SHA-25</td><td rowspan="2">列车输出保护区段允许解锁信息后，列车不安全启动</td><td style='text-align: center;'>SR-1-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-S-65</td><td style='text-align: center;'>V0BC发送“允许解锁”信息后，应保证列车不会进入前方保护区段，直至前方进路重新开放</td><td style='text-align: center;'>越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td rowspan="3">PH-34</td><td rowspan="3">紧急制动命令</td><td rowspan="3">IHA-9</td><td rowspan="3">ZC向V0BC发送紧急停车命令不成功</td><td style='text-align: center;'>SR-I-25</td><td style='text-align: center;'>ZC-V0BC接口信息包含紧急制动命令信息</td><td style='text-align: center;'>V0BC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-S-66</td><td style='text-align: center;'>CBTC级别下，互联互通车载ATP收到ZC列车控制信息紧急制动命令或有紧急制动命令报文的特殊命令，应立即执行紧急制动</td><td style='text-align: center;'>ZC-V0BC接口规范“紧急制动命令”、“特殊控制报文”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-35</td><td rowspan="5">跨线运营时，他线CBTC列车进入联络线时侧面撞击本线CBTC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'></td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-35</td><td rowspan="6">跨线运营时，他线CBTC列车进入联络线时侧面撞击本线CBTC列车</td><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="5">IHA-6</td><td rowspan="5">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-36</td><td rowspan="5">他线CBTC列车进入联络线时侧面撞击本线CBTC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照设限设计</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-36</td><td rowspan="6">他线CBTC列车进入联络线时侧面撞击本线CBTC列车</td><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="5">IHA-6</td><td rowspan="5">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-37</td><td rowspan="5">他线CBTC列车进入联络线时侧面撞击本线ITC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照限设计</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-37</td><td rowspan="6">他线CBTC列车进入联络线时侧面撞击本线ITC列车</td><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范&quot;RSSP-I铁路信号安全通信协议&quot;</td></tr><tr><td rowspan="5">IHA-6</td><td rowspan="5">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-38</td><td rowspan="5">本线ITC列车侧面撞击进入联络线的他线CBTC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-38</td><td rowspan="6">本线ITC列车侧面撞击进入联络线的他线CBTC列车</td><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="5">IHA-6</td><td rowspan="5">车联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-39</td><td rowspan="5">他线CBTC列车进入联络线时侧面撞击本线RM模式列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进行信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'></td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-39</td><td rowspan="5">他线CBTC列车进入联络线时侧面撞击本线RM模式列车</td><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="4">IHA-6</td><td rowspan="4">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="2">PH-39</td><td rowspan="2">他线CBTC列车进入联络线时侧面撞击本线RM模式列车</td><td style='text-align: center;'>IHA-6</td><td style='text-align: center;'>互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-40</td><td rowspan="3">本线RM模式列车侧面撞击进入联络线的他线CBTC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-40</td><td rowspan="6">本线RM模式列车侧面撞击进入联络线的他线CBTC列车</td><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-1-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-1-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保压接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td style='text-align: center;'>轨道</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-1-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="3">IHA-6</td><td rowspan="3">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-1-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="3">PH-40</td><td rowspan="3">本线RM模式列车侧面撞击进入联络线的他线CBTC列车</td><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据的正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-41</td><td rowspan="3">他线ITC列车进入联络线时侧面撞击本线ITC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'></td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-41</td><td rowspan="6">他线ITC列车进入联络线时侧面撞击本线ITC列车</td><td style='text-align: center;'>IHA-5</td><td style='text-align: center;'>联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-1安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-1铁路信号安全通信协议”</td></tr><tr><td rowspan="3">IHA-4</td><td rowspan="3">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-1铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-1铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="2">PH-41</td><td rowspan="2">他线ITC列车进入联络线时侧面撞击本线ITC列车</td><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据的正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td rowspan="3">PH-42</td><td rowspan="3">本线ITC列车侧面撞击进入联络线的他线ITC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-42</td><td rowspan="6">本线ITC列车侧面撞击进入联络线的他线ITC列车</td><td rowspan="4">IHA-5</td><td rowspan="4">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="2">PH-42</td><td rowspan="2">本线ITC列车侧面撞击进入联络线的他线ITC列车</td><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td rowspan="3">PH-43</td><td rowspan="3">他线ITC列车进入联络线时侧面撞击本线RM模式列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照设限设计</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-43</td><td rowspan="6">他线ITC列车进入联络线时侧面撞击本线RM模式列车</td><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td rowspan="2">IHA-4</td><td rowspan="2">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="2">PH-43</td><td rowspan="2">他线ITC列车进入联络线时侧面撞击本线RM模式列车</td><td rowspan="2">IHA-6</td><td rowspan="2">互联互通车载电子地图错误</td><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据的正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td><td style='text-align: center;'>电子地图存储</td></tr><tr><td rowspan="3">PH-44</td><td rowspan="3">本线RM模式列车侧面撞击进入联络线的他线ITC列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref.1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-44</td><td rowspan="5">本线RM模式列车侧面撞击进入联络线的他线ITC列车</td><td rowspan="4">IHA-5</td><td rowspan="4">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-0-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-45</td><td rowspan="5">他线RM模式列车进入联络线时侧面撞击本线RM模式列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="3">PH-45</td><td rowspan="3">他线RM模式列车进入联络线时侧面撞击本线RM模式列车</td><td rowspan="2">IHA-4</td><td rowspan="2">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-1-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-46</td><td rowspan="3">本线RM模式列车侧面撞击进入联络线的他线RM模式列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>互联互通信号系统</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td rowspan="7">Ref.1.2</td><td rowspan="7">列车侧面相撞</td><td rowspan="7">PH-46</td><td rowspan="7">IHA-5</td><td rowspan="7">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-1-7</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-1-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-1-9</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-1-10</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-1-11</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-1-12</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-1-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-47</td><td rowspan="5">本线非装备列车侧面撞击进入联络线的他线RM模式列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="4">PH-47</td><td rowspan="4">本线非装备列车侧面撞击进入联络线的他线RM模式列车</td><td rowspan="2">IHA-4</td><td rowspan="2">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-48</td><td style='text-align: center;'>他线RM模式列车进入联络线时侧面撞击本线非装备列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-1.2</td><td rowspan="6">列车侧面相撞</td><td rowspan="6">PH-48</td><td rowspan="6">他线RM模式列车进入联络线时侧面撞击本线非装备列车</td><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td rowspan="2">IHA-4</td><td rowspan="2">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="2">PH-48</td><td rowspan="2">他线RM模式列车进入联络线时侧面撞击本线非装备列车</td><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-0-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-0-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-49</td><td rowspan="3">本线非装备列车侧面撞击进入联络线的他线非装备列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-49</td><td rowspan="5">本线非装备列车侧面撞击进入联络线的他线非装备列车</td><td rowspan="2">IHA-5</td><td rowspan="2">联络线 ZC-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通 CI-CI接口协议应采用 RSSP-I 安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通 CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr><tr><td rowspan="2">IHA-4</td><td rowspan="2">联络线 ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通 ZC-ZC接口协议应采用 RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通 ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="5">PH-50</td><td rowspan="5">他线非装备列车进入联络线时侧面撞击本线非装备列车</td><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-27</td><td rowspan="2">联络线计轴点设置不满足侧防安全距离</td><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照促限设计</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">IHA-5</td><td rowspan="2">联络线CI-CI接口信息传输错误</td><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-I安全协议</td><td style='text-align: center;'>CI-CI接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td><td style='text-align: center;'>CI-CI接口规范</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.2</td><td rowspan="5">列车侧面相撞</td><td rowspan="4">PH-50</td><td rowspan="4">他线非装备列车进入联络线时侧面撞击本线非装备列车</td><td rowspan="2">IHA-4</td><td rowspan="2">联络线ZC-ZC接口信息传输错误</td><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-I铁路信号安全通信协议</td><td style='text-align: center;'>ZC-ZC接口规范“RSSP-I铁路信号安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td><td style='text-align: center;'>ZC-ZC接口规范</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td colspan="7">共线列车运行侧面相撞防护由单线CBTC系统防护，不在本规范范围</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-1.3</td><td rowspan="3">列车迎面相撞</td><td rowspan="2">PH-51</td><td rowspan="2">两CBTC模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-28</td><td style='text-align: center;'>联络线列车反向运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>PH-52</td><td style='text-align: center;'>CBTC模式列车与ITC模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-28</td><td style='text-align: center;'>联络线列车反向运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-1.3</td><td rowspan="3">列车迎面相撞</td><td rowspan="2">PH-52</td><td rowspan="2">CBTC模式列车与ITC模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-30</td><td style='text-align: center;'>联络线列车反向运行时，信号系统给出ITC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>PH-53</td><td style='text-align: center;'>CBTC模式列车与RM模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-28</td><td style='text-align: center;'>联络线列车反向运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-1.3</td><td rowspan="3">列车迎面相撞</td><td rowspan="3">PH-53</td><td rowspan="3">CBTC模式列车与RM模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段倾闭</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.3</td><td rowspan="4">列车迎面相撞</td><td rowspan="4">PH-54</td><td rowspan="4">CBTC模式列车与切除ATP列车或未装备ATP列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-28</td><td style='text-align: center;'>联络线列车反向运行时，ZC子系统为CBTC车计算了不安全的MA</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="2">Ref-1.3</td><td rowspan="2">列车迎面相撞</td><td rowspan="2">PH-55</td><td rowspan="2">两ITC模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-30</td><td style='text-align: center;'>联络线列车反向运行时，信号系统给出ITC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.3</td><td rowspan="4">列车迎面相撞</td><td rowspan="4">PH-56</td><td rowspan="4">ITC模式列车与RM模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-8-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-30</td><td style='text-align: center;'>联络线列车反向运行时，信号系统给出ITC级别列车不安全的授权</td><td style='text-align: center;'>SR-8-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-1.3</td><td rowspan="4">列车迎面相撞</td><td rowspan="4">PH-57</td><td rowspan="4">ITC模式列车与切除ATP列车或未装备ATP列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-30</td><td style='text-align: center;'>联络线列车反向运行时，信号系统给出ITC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.3</td><td rowspan="5">列车迎面相撞</td><td rowspan="2">PH-58</td><td rowspan="2">两RM模式列车在联络线或相邻计轴区段迎面相撞</td><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-59</td><td rowspan="3">RM模式列车与切除ATP列车或未装备ATP列车迎面相撞</td><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-1.3</td><td rowspan="3">列车迎面相撞</td><td rowspan="2">PH-60</td><td rowspan="2">两切除ATP列车或未装备ATP列车迎联络线或相邻计轴区段面相撞</td><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时,信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能,联络线方向运行进路建立后,敌对进路不能建立</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车,司机按照联锁信号或人工调度行车,行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td colspan="7">共线列车运行迎面相撞防护由单线CBTC系统防护,不在本规范范围</td></tr><tr><td rowspan="2">Ref-1.4</td><td rowspan="2">列车解体导致撞车</td><td rowspan="2">PH-61</td><td rowspan="2">列车解体后不受信号系统控制</td><td style='text-align: center;'>SHA-32</td><td style='text-align: center;'>车载ATP对列车解体没有防护</td><td style='text-align: center;'>SR-S-72</td><td style='text-align: center;'>在CBTC级别、ITC级别和RM模式下,车载ATP需能够持续监督车辆发送的列车完整性状态,若采集到列车完整性丢失,ATP应向车辆持续输出紧急制动命令</td><td style='text-align: center;'>防护列车完整性丢失、列车运行方向确定</td></tr><tr><td style='text-align: center;'>IHA-10</td><td style='text-align: center;'>车载ATP对列车解体采集信息失效</td><td style='text-align: center;'>SR-1-26</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术采集列车完整性信息</td><td style='text-align: center;'>车载ATO/ATP与车辆接口“列车完整性状态”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-1.4</td><td rowspan="5">列车解体导致撞车</td><td rowspan="5">PH-61</td><td rowspan="5">列车解体后不受信号系统控制</td><td style='text-align: center;'>SHA-33</td><td style='text-align: center;'>车载ATP紧急制动输出故障</td><td style='text-align: center;'>SR-I-9</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术传输车辆实施紧急制动命令及采集紧急制动状态信息</td><td style='text-align: center;'>车载ATO/ATP与车辆接口“列车完整性状态”</td></tr><tr><td style='text-align: center;'>OSHA-7</td><td style='text-align: center;'>车辆紧急制动系统失效</td><td style='text-align: center;'>SR-0-3</td><td style='text-align: center;'>车辆采购及维护符合车辆专业相关规定，并满足信号系统输出的安全要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>IHA-11</td><td style='text-align: center;'>车辆没有正确采集车载ATP的紧急制动信息</td><td style='text-align: center;'>SR-I-9</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术传输车辆实施紧急制动命令及采集紧急制动状态信息</td><td style='text-align: center;'>车载ATO/ATP与车辆接口“列车完整性状态”</td></tr><tr><td style='text-align: center;'>OSHA-8</td><td style='text-align: center;'>解体列车的某部分已经完全与车载ATP物理隔离，无法收到ATP紧急制动的信息</td><td style='text-align: center;'>SR-G-9</td><td style='text-align: center;'>解体列车的某部分已经完全与车载ATP物理隔离，无法收到ATP紧急制动的信息。该危害信号系统无法减轻或消除</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-9</td><td style='text-align: center;'>ZC系统未处理解体列车信息，导致后续列车与解体列车相撞</td><td style='text-align: center;'>SR-O-10</td><td style='text-align: center;'>信号系统无法检测到解体后列车具体位置，车载ATP系统无法提供安全防护。运营责任方应制定该情况下应急预案，避免或减轻事故</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-2.1</td><td rowspan="6">列车与役限物体相撞</td><td rowspan="3">PH-62</td><td rowspan="3">列车与工具或施工材料相撞</td><td rowspan="2">OSHA-10</td><td rowspan="2">列车撞到轨道(含联络线)上施工或维护的工具或材料</td><td style='text-align: center;'>SR-O-11</td><td style='text-align: center;'>制定现场施工管理细则,列车在线路上运营时,禁止运营交路涉及的站台范围的施工或维护工作进行</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-O-12</td><td style='text-align: center;'>制定现场施工管理细则,作业责任方应完成施工材料、工具、废弃物清除,严禁遗漏在轨道上或其他形式的侵限限界</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-11</td><td style='text-align: center;'>列车撞到站台上施工或维护遗落的工具或材料</td><td style='text-align: center;'>SR-O-13</td><td style='text-align: center;'>动车调试或列车运营时,站台上的施工作业界面应清晰明确,做好切实可行的防护方案后方可进行交叉作业</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">PH-63</td><td rowspan="3">列车与轨道上物体相撞</td><td style='text-align: center;'>OSHA-12</td><td style='text-align: center;'>列车与轨道上的信号设备相撞</td><td style='text-align: center;'>SR-O-14</td><td style='text-align: center;'>信号设备安装满足设备限界要求</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">OSHA-13</td><td rowspan="2">列车与跌落在轨道上的其他物体相撞</td><td style='text-align: center;'>SR-O-15</td><td style='text-align: center;'>列车运营线路应实施全面防护</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-O-16</td><td style='text-align: center;'>每天开始正式运营前,运营责任方应组织当天所有可能涉及线路的压道作业,确认线路无障碍物,方可进入运营</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-2.1</td><td rowspan="3">列车与役限物体相撞</td><td rowspan="2">PH-64</td><td rowspan="2">列车与平交道口上物体相撞</td><td style='text-align: center;'>OSHA-14</td><td style='text-align: center;'>列车与车辆段平交道口的汽车或其他机动车相撞</td><td style='text-align: center;'>SR-O-17</td><td style='text-align: center;'>运营责任方应该制定相关规则，防止列车与车辆段里的汽车、行人、其他机动车相撞</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-15</td><td style='text-align: center;'>列车与掉落在车辆段平交道口区域的物体（从其他交通工具掉落的物体）相撞</td><td style='text-align: center;'>SR-O-18</td><td style='text-align: center;'>运营责任方应该制定相关规则，防止列车与车辆段里掉落在平交道口区域的物体相撞</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-65</td><td style='text-align: center;'>不能被信号系统识别的列车上线安全事故导致</td><td style='text-align: center;'>OSHA-16</td><td style='text-align: center;'>不能被信号系统识别的列车上线安全事故导致</td><td style='text-align: center;'>SR-O-19</td><td style='text-align: center;'>运营责任方应该制定相关规则，确保不能被信号系统识别的列车上线行驶安全及安全退出线路</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-2.2</td><td style='text-align: center;'>列车冲出轨道尽头，撞到轨道终端的缓冲车挡</td><td style='text-align: center;'>PH-66</td><td style='text-align: center;'>列车冲出轨道尽头，撞到轨道终端的缓冲车挡</td><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="7">Ref-2.2</td><td rowspan="7">列车冲出轨道尽头，撞到轨道终端的缓冲车挡</td><td rowspan="7">PH-66</td><td rowspan="7">列车冲出轨道尽头，撞到轨道终端的缓冲车挡</td><td rowspan="2">SHA-34</td><td rowspan="2">信号系统给CBTC级别列车的授权超出了线路边界</td><td style='text-align: center;'>SR-1-2</td><td style='text-align: center;'>VOBC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>VOBC-ZC接口规范“安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">SHA-35</td><td rowspan="2">信号系统给ITC级别列车的授权超出了线路边界</td><td style='text-align: center;'>SR-S-73</td><td style='text-align: center;'>车地应答器通信应满足欧标要求</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-36</td><td style='text-align: center;'>信号系统给RM模式列车的授权超出了线路边界</td><td style='text-align: center;'>SR-S-74</td><td style='text-align: center;'>运营线路终端的信号机应常亮红灯显示</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-2.3</td><td rowspan="6">列车与防淹门相撞</td><td rowspan="5">PH-67</td><td rowspan="5">防淹门已关闭，列车运行撞到防淹门</td><td rowspan="5">IHA-12</td><td rowspan="5">信号系统未检测到防淹门关闭，ZC为CBTC、HTC列车计算MA段对防淹门</td><td style='text-align: center;'>SR-I-27</td><td style='text-align: center;'>联锁系统与防淹门接口采用安全继电器或其他安全接口技术</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-28</td><td style='text-align: center;'>联锁系统除非采集到防淹门完全开启且锁定状态，否则施门所在进路不允许开放</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>信号系统未检测到防淹门关闭，联锁系统为RM列车开放不安全进路</td><td style='text-align: center;'>SR-I-28</td><td style='text-align: center;'>联锁系统除非采集到防淹门完全开启且锁定状态，否则施门所在进路不允许开放</td></tr><tr><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-0-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td></tr><tr><td style='text-align: center;'>PH-68</td><td style='text-align: center;'>防淹门关闭时，撞击正在通过的列车</td><td style='text-align: center;'>IHA-14</td><td style='text-align: center;'>列车正在通过防淹门时，防淹关闭，列车撞上防淹门</td><td style='text-align: center;'>SR-I-29</td><td style='text-align: center;'>防淹门关闭前，应向联锁系统发送请求关闭命令，联锁系统确定对应区间无列车占用或即将占用，方可允许关闭防淹门</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-2.3</td><td rowspan="3">列车与防淹门相撞</td><td rowspan="2">PH-68</td><td rowspan="2">防淹门关闭时，撞击正在通过的列车</td><td rowspan="2">IHA-15</td><td rowspan="2">列车即将进入防淹门所在进路时防范关闭，列车撞上防淹门</td><td style='text-align: center;'>SR-S-75</td><td style='text-align: center;'>信号系统应保证CBTC列车在防淹门进路停稳，方可允许关闭防淹门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-O-20</td><td style='text-align: center;'>防淹门关闭信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>PH-69</td><td style='text-align: center;'>信号系统与防淹门无接口</td><td style='text-align: center;'>OSHA-17</td><td style='text-align: center;'>信号系统与防淹门无接口信息，列车行车安全信号系统无法防护</td><td style='text-align: center;'>SR-O-21</td><td style='text-align: center;'>信号系统与防淹门无接口情况下，运营责任方应制定防淹门关闭、开启应急预案，避免或减轻事故</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>Ref-2.4</td><td style='text-align: center;'>列车与人防门相撞</td><td style='text-align: center;'>PH-70</td><td style='text-align: center;'>列车与人防门相撞</td><td style='text-align: center;'>OSHA-44</td><td style='text-align: center;'>信号系统与人防门无接口信息，列车行车安全信号系统无法防护</td><td style='text-align: center;'>SR-O-22</td><td style='text-align: center;'>信号系统与人防门无接口情况下，运营责任方应制定人防门关闭、开启应急预案，避免或减轻事故</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-3.1</td><td rowspan="5">列车撞到乘客或工作人员</td><td rowspan="5">PH-71</td><td rowspan="5">站台门打开时，列车在站台区域移动，列车撞到站台的乘客</td><td rowspan="5">IHA-16</td><td rowspan="5">站台门打开时，信号系统给出CBTC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-76</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车即将进入站台轨时，站台门打开，车载ATP应保证列车在站外停车或实施紧急制动</td><td style='text-align: center;'>站台门防护、越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>SR-S-77</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，进站过程中，站台门打开，车载ATP应实施紧急制动</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>SR-S-78</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车出站过程中且最小安全后端尚未出清站台轨，站台门打开，车载ATP应实施紧急制动</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>SR-S-79</td><td style='text-align: center;'>CBTC级别下，ZC设备监控站台门的开启、关闭和未知状态，并实时传递给车载ATP系统</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-I-13</td><td style='text-align: center;'>CI采用安全继电器或其他安全接口技术采集站台门状态信息</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-3.1</td><td rowspan="3">列车撞到乘客或工作人员</td><td rowspan="3">PH-71</td><td rowspan="3">站台门打开时，列车在站台区域移动，列车撞到站台的乘客</td><td style='text-align: center;'>OSHA-18</td><td style='text-align: center;'>站台门打开时，信号系统给出ITC、CI级别列车不安全的授权</td><td style='text-align: center;'>SR-O-23</td><td style='text-align: center;'>非CBTC级别下，车载ATP系统不能对站台门非安全状态进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-66</td><td style='text-align: center;'>站台门打开时，连锁未关闭进站/出站进路</td><td style='text-align: center;'>SR-S-80</td><td style='text-align: center;'>站台门打开时，联锁系统根据站型关闭对应进站/出站进路</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-3.1</td><td rowspan="5">列车撞到乘客或工作人员</td><td rowspan="2">PH-71</td><td rowspan="2">站台门打开时，列车在站台区域移动，列车撞到站台的乘客</td><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-0-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-0-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-72</td><td rowspan="3">紧急关闭按钮激活时列车在站台区域移动，列车撞到站台的乘客</td><td rowspan="3">IHA-17</td><td rowspan="3">紧急关闭按钮激活时，信号系统给出CBTC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-81</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车即将进入站台轨时，紧急关闭按钮激活，车载ATP应保证列车在站外停车或实施紧急制动</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>SR-S-82</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车进站过程中，紧急关闭按钮激活，车载ATP应实施紧急制动</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>SR-S-83</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车出站过程中且最小安全后端尚未出清站台轨，紧急关闭按钮激活，车载ATP应实施紧急制动</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-3.1</td><td rowspan="6">列车撞到乘客或工作人员</td><td rowspan="6">PH-72</td><td rowspan="6">紧急关闭按钮激活时列车在站台区域移动，列车撞到站台的乘客</td><td rowspan="4">IHA-17</td><td rowspan="4">紧急关闭按钮激活时，信号系统给出CBTC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-84</td><td style='text-align: center;'>CI监控车站紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的列车进路信号</td><td style='text-align: center;'>进路/区段锁闭、响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>SR-S-45</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集紧急关闭按钮状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-85</td><td style='text-align: center;'>紧急关闭按钮故障时联锁应能够检测到且导向安全侧</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr><tr><td rowspan="2">OSHA-19</td><td rowspan="2">紧急关闭按钮激活时，信号系统给出ITC、CI级别列车不安全的授权</td><td style='text-align: center;'>SR-O-24</td><td style='text-align: center;'>非CBTC级别下，站台紧急关闭按钮激活信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-84</td><td style='text-align: center;'>CI监控车站紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的列车进路信号</td><td style='text-align: center;'>进路/区段锁闭、响应紧急关闭按钮</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-3.1</td><td rowspan="5">列车撞到乘客或工作人员</td><td rowspan="5">PH-72</td><td rowspan="5">紧急关闭按钮激活时列车在站台区域移动，列车撞到站台的乘客</td><td rowspan="2">OSHA-19</td><td rowspan="2">紧急关闭按钮激活时，信号系统给出ITC、CI级别列车不安全的授权</td><td style='text-align: center;'>SR-S-45</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集紧急关闭按钮状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-85</td><td style='text-align: center;'>紧急关闭按钮故障时联锁应能够检测到且导向安全侧</td><td style='text-align: center;'>响应紧急关闭按钮</td></tr><tr><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能够实施紧急制动</td><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td><td style='text-align: center;'>固定速度限制防护、临时限速限制防护、列车超速防护、列车运行方向防护、退行防护、越过移动授权终点防护、移动授权更新超时防护、车门防护、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-3.1</td><td rowspan="5">列车撞到乘客或工作人员</td><td rowspan="2">PH-73</td><td rowspan="2">列车在乘客或工作人员被夹在车门与站台门之间时移动</td><td style='text-align: center;'>OSHA-20</td><td style='text-align: center;'>列车关门时，有人被夹在站台门和车门之间</td><td style='text-align: center;'>SR-O-25</td><td style='text-align: center;'>运营责任方应制定相关规则，确保乘客上下车完毕后再关闭车门</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-21</td><td style='text-align: center;'>站台门关门时，有人被夹在站台门和车门之间</td><td style='text-align: center;'>SR-O-26</td><td style='text-align: center;'>运营责任方应制定相关规则，确保乘客上下车完毕后再关闭站台门</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="3">PH-74</td><td rowspan="3">列车撞到工作人员</td><td style='text-align: center;'>OSHA-22</td><td style='text-align: center;'>列车撞到站台上的施工或维护人员</td><td style='text-align: center;'>SR-O-13</td><td style='text-align: center;'>动车调试或列车运营时，站台上的施工作业界面应清晰明确，做好切实可行的防护方案后方可进行交叉作业</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-23</td><td style='text-align: center;'>列车撞到轨道上的施工或维护人员</td><td style='text-align: center;'>SR-O-11</td><td style='text-align: center;'>制定现场施工管理细则，列车在线路上运营时，禁止运营交路涉及的站台范围的施工或维护工作进行</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-24</td><td style='text-align: center;'>列车撞到车辆段的工作人员</td><td style='text-align: center;'>SR-O-27</td><td style='text-align: center;'>运营责任方应制定车辆段作业细则，以避免列车车辆段运营或调试过程中撞到车辆段工作人员</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-4.1</td><td rowspan="4">列车失去运行方向引导</td><td rowspan="4">PH-76</td><td rowspan="4">列车失去运行方向引导</td><td style='text-align: center;'>SHA-37</td><td style='text-align: center;'>道岔未密贴且锁闭时，信号系统给出CBTC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-6</td><td style='text-align: center;'>信号开放/进路办理检查条件应符合联锁表要求</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td rowspan="2">SHA-38</td><td rowspan="2">道岔未密贴且锁闭时，信号系统给出IPC级别列车不安全的授权</td><td style='text-align: center;'>SR-S-86</td><td style='text-align: center;'>联锁控制道岔的命令必须同排列的进路中道岔的位置一致，同时锁闭道岔，联锁设备才能建立进路</td><td style='text-align: center;'>进路办理、进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-44</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集道岔的状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-39</td><td style='text-align: center;'>道岔未密贴且锁闭时，信号系统给出RM模式列车不安全的授权</td><td style='text-align: center;'>SR-S-87</td><td style='text-align: center;'>道岔子系统能给出正确的道岔状态表示</td><td style='text-align: center;'>进路办理、进路/区段锁闭</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-4.1</td><td rowspan="4">列车失去运行方向引导</td><td rowspan="3">PH-77</td><td rowspan="3">列车在道岔区域时,道岔动作导致列车脱轨</td><td rowspan="3">SHA-40</td><td rowspan="3">列车在道岔区域时,道岔动作</td><td style='text-align: center;'>SR-S-88</td><td style='text-align: center;'>道岔转换完毕后,应保证道岔固定在规定位置不再移动</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-89</td><td style='text-align: center;'>道岔受进路锁闭、区段锁闭或人工单独锁闭时,联锁须不能控制道岔移动</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-90</td><td style='text-align: center;'>只有当道岔位置与操作要求一致,并经检查自动开闭器的两组接点排的相应接点位置正确,才能构成道岔位置的正确表示</td><td style='text-align: center;'>进路办理、进路/区段锁闭</td></tr><tr><td style='text-align: center;'>PH-78</td><td style='text-align: center;'>轨道断裂导致列车脱轨</td><td style='text-align: center;'>OSHA-25</td><td style='text-align: center;'>轨道断裂导致列车脱轨</td><td style='text-align: center;'>SR-O-28</td><td style='text-align: center;'>轨道采购及维护符合轨道专业相关规定</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">Ref-4.2</td><td rowspan="2">列车运行过程中失稳</td><td rowspan="2">PH-79</td><td rowspan="2">列车在线路运行时超过安全限制速度,导致列车脱轨</td><td style='text-align: center;'>SHA-41</td><td style='text-align: center;'>信号系统为列车计算的安全限制速度超过了线路限速</td><td style='text-align: center;'>SR-S-91</td><td style='text-align: center;'>CBTC、ITC列车计算安全限速不应超过线路限速</td><td style='text-align: center;'>确定制动曲线</td></tr><tr><td style='text-align: center;'>SHA-42</td><td style='text-align: center;'>列车运行速度超过信号系统的安全限制速度时,未能够实施紧急制动</td><td style='text-align: center;'>SR-S-27</td><td style='text-align: center;'>车载ATP将实际速度与当前EBI进行比较,如果实际速度≥监控速度,应输出紧急制动命令</td><td style='text-align: center;'>列车超速防护、列车速度测定、测速误差补偿</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-4.2</td><td rowspan="6">列车运行过程中失稳</td><td rowspan="6">PH-79</td><td rowspan="6">列车在线路运行时超过安全限制速度，导致列车脱轨</td><td rowspan="3">IHA-18</td><td rowspan="3">本线线路临时限速未传递到他线车载ATP系统</td><td style='text-align: center;'>SR-I-17</td><td style='text-align: center;'>ZC-I-17接口信息包含临时限速信息</td><td style='text-align: center;'>V0BC-ZC接口规范“临时限速信息”</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td><td style='text-align: center;'>V0BC-ZC接口规范“安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-O-2</td><td style='text-align: center;'>非CBTC级别下，临时限速信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定临时限速操作规程，确保临时限速信息及时传递到司机</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>IHA-19</td><td style='text-align: center;'>他线车载ATP收到本线临时限速后，紧急制动曲线计算未正确采用</td><td style='text-align: center;'>SR-S-46</td><td style='text-align: center;'>CBTC级别下，车载ATP计算EBI曲线时，应包含互联互通临时限速</td><td style='text-align: center;'>列车超速防护、确定制动曲线</td></tr><tr><td rowspan="2">IHA-20</td><td rowspan="2">本线为他线车载提供了错误的线路限速数据</td><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-4.2</td><td rowspan="4">列车运行过程中失稳</td><td rowspan="3">PH-79</td><td rowspan="3">列车在线路运行时超过安全限制速度，导致列车脱轨</td><td style='text-align: center;'>IHA-21</td><td style='text-align: center;'>他线车载ATP错误地使用了本线线路数据</td><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td><td style='text-align: center;'>SR-O-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td><td style='text-align: center;'>SR-O-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-80</td><td style='text-align: center;'>车轮或车轴断裂导致列车脱轨</td><td style='text-align: center;'>OSHA-26</td><td style='text-align: center;'>车轮或车轴断裂导致列车脱轨</td><td style='text-align: center;'>SR-O-3</td><td style='text-align: center;'>车辆采购及维护符合车辆专业相关规定，并满足信号系统输出的安全要求</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">Ref-4.3</td><td rowspan="2">列车脱轨侵入其他轨道</td><td rowspan="2">PH-81</td><td style='text-align: center;'>列车脱轨侵入其他轨道撞击正在行驶列车</td><td style='text-align: center;'>OSHA-27</td><td style='text-align: center;'>列车脱轨侵入其他轨道撞击正在行驶列车</td><td style='text-align: center;'>SR-O-29</td><td style='text-align: center;'>列车脱轨后，信号系统无法提供其安全防护，运营责任方应制定列车脱轨应急预案，避免或减轻事故影响</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>列车撞击脱轨入侵的列车</td><td style='text-align: center;'>OSHA-28</td><td style='text-align: center;'>列车撞击脱轨入侵的列车</td><td style='text-align: center;'>SR-O-29</td><td style='text-align: center;'>列车脱轨后，信号系统无法提供其安全防护，运营责任方应制定列车脱轨应急预案，避免或减轻事故影响</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-5.1</td><td rowspan="5">人员从站台跌入轨道区域</td><td rowspan="5">PH-82</td><td rowspan="5">站台门不安全地开启，乘客落入站台</td><td style='text-align: center;'>OSHA-29</td><td style='text-align: center;'>站台屏蔽系统错误，不安全开启站台门</td><td style='text-align: center;'>SR-O-30</td><td style='text-align: center;'>站台门采购及维护符合站台门专业相关规定</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="4">OSHA-30</td><td rowspan="4">站台人员不安全开启站台门</td><td style='text-align: center;'>SR-S-75</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车即将进入站台轨时，站台门打开，车载ATP应保证列车在站外停车或实施紧急制动</td><td style='text-align: center;'>站台门防护、越过移动授权终点防护、移动授权更新超时防护</td></tr><tr><td style='text-align: center;'>SR-S-77</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，进站过程中，站台门打开，车载ATP应实施紧急制动</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>SR-S-78</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车出站过程中且最小安全后端尚未出清站台轨，站台门打开，车载ATP应实施紧急制动</td><td style='text-align: center;'>站台门防护</td></tr><tr><td style='text-align: center;'>SR-O-23</td><td style='text-align: center;'>非CBTC级别下，车载ATP系统不能对站台门非安全状态进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-5.1</td><td rowspan="6">人员从站台跌入轨道区域</td><td rowspan="6">PH-82</td><td rowspan="6">站台门不安全地开启，乘客落入站台</td><td rowspan="3">OSHA-30</td><td rowspan="3">站台人员不安全开启站台门</td><td style='text-align: center;'>SR-S-92</td><td style='text-align: center;'>CI监控站台门的开启和关闭状态，如果站台门打开，应关闭与该屏蔽门相关联的进路</td><td style='text-align: center;'>进路/区段锁闭、站台门防护</td></tr><tr><td style='text-align: center;'>SR-O-31</td><td style='text-align: center;'>运营责任方制定规则，明确站台门紧急开启操作细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-O-32</td><td style='text-align: center;'>站台门人工开启开关应避免站台非工作人员误操作</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>IHA-22</td><td style='text-align: center;'>通信中断或者阻塞，信号系统开关门命令延时发送，导致站台门错误开启</td><td style='text-align: center;'>SR-I-30</td><td style='text-align: center;'>规范互联互通V0BC-CI接口开关门命令有效时效，超时命令无效</td><td style='text-align: center;'>V0BC-CI接口规范“RSSP-Ⅱ标准安全通信协议”</td></tr><tr><td rowspan="2">IHA-23</td><td rowspan="2">CI收到错误开关站台门信息</td><td style='text-align: center;'>SR-S-93</td><td style='text-align: center;'>地面设备提供商应保证线路站台对应的站台门ID、开门侧数据正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-I-31</td><td style='text-align: center;'>车载ATP系统应保证发送的PSD的数量、开关门侧、开门码正确，保证车门与站台门联动的一致性</td><td style='text-align: center;'>V0BC-CI接口规范“PSD_1控制信息”、“PSD_2控制信息”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="6">Ref-5.1</td><td rowspan="6">人员从站台跌入轨道区域</td><td rowspan="6">PH-82</td><td rowspan="6">站台门不安全地开启,乘客落入站台</td><td rowspan="4">IHA-23</td><td rowspan="4">CI收到错误开关站台门信息</td><td style='text-align: center;'>SR-1-32</td><td style='text-align: center;'>V0BC-33接口信息应包含开关站台门码信息</td><td style='text-align: center;'>V0BC-C接口规范“PSD_1控制信息”“PSD_2控制信息”</td></tr><tr><td style='text-align: center;'>SR-1-33</td><td style='text-align: center;'>V0BC-34接口信息应包含开关站台门控制信息</td><td style='text-align: center;'>V0BC-CI接口规范“PSD_1控制信息”、“PSD_2控制信息”</td></tr><tr><td style='text-align: center;'>SR-I-41</td><td style='text-align: center;'>本线CI系统应丢弃他线V0BC-CI的自定义包</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-34</td><td style='text-align: center;'>V0BC-35接口信息应包含开关站台门数量信息,联锁保证站台门开关数量与车门一致</td><td style='text-align: center;'>V0BC-CI接口规范“N_PSD”</td></tr><tr><td rowspan="2">IHA-24</td><td rowspan="2">站台门状态信息错误,导致列车不安全启动</td><td style='text-align: center;'>SR-I-13</td><td style='text-align: center;'>CI采用安全继电器或其他安全接口技术采集站台门状态信息</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-24</td><td style='text-align: center;'>V0BC和CI间通信采用RSSP-Ⅱ标准安全通信协议</td><td style='text-align: center;'>V0BC-CI接口规范“RSSP-Ⅱ标准安全通信协议”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-5.1</td><td rowspan="5">人员从站台跌入轨道区域</td><td rowspan="3">PH-82</td><td rowspan="3">站台门不安全地开启，乘客落入站台</td><td rowspan="3">IHA-25</td><td rowspan="3">互联互通接口错误，导致开关门信息错误</td><td style='text-align: center;'>SR-I-30</td><td style='text-align: center;'>规范互联互通V0BC-CI接口开关门命令有效时效，超时命令无效</td><td style='text-align: center;'>V0BC-CI接口规范“RSSP-II标准安全通信协议”</td></tr><tr><td style='text-align: center;'>SR-I-35</td><td style='text-align: center;'>本线ZC系统应丢弃他线列车V0BC弃他线的自定义包</td><td style='text-align: center;'>V0BC-ZC接口规范“ZC厂商自定义帧”</td></tr><tr><td style='text-align: center;'>SR-I-36</td><td style='text-align: center;'>他线列车应丢弃本线ZC列车应丢弃的自定义包</td><td style='text-align: center;'>V0BC-ZC接口规范“V0BC厂商自定义帧”</td></tr><tr><td rowspan="2">PH-83</td><td rowspan="2">车门与站台门数量不匹配时，错误地开启车门或站台门</td><td rowspan="2">IHA-28</td><td rowspan="2">V0BC输出不匹配的开门码信息，开启站台门错误侧</td><td style='text-align: center;'>SR-S-42</td><td style='text-align: center;'>地面设备提供商应保证列车在各站台开关站台门信息数据正确</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-I-32</td><td style='text-align: center;'>V0BC-33接口信息应包含开关站台门码信息</td><td style='text-align: center;'>V0BC-CI接口规范“PSD_1控制信息”、“PSD_2控制信息”</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="7">Ref-5.1</td><td rowspan="7">人员从站台跌入轨道区域</td><td rowspan="7">PH-83</td><td rowspan="7">车门与站台门数量不匹配时,错误地开启车门或站台门</td><td rowspan="3">IHA-28</td><td rowspan="3">V0BC输出不匹配的开门码信息,开启站台门错误侧</td><td style='text-align: center;'>SR-I-33</td><td style='text-align: center;'>V0BC-34接口信息应包含开关站台门控制信息</td><td style='text-align: center;'>V0BC-CI接口规范“PSD_1控制信息”、“PSD_2控制信息”</td></tr><tr><td style='text-align: center;'>SR-I-42</td><td style='text-align: center;'>他线列车应丢弃本线CI-V0BC的自定义包</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-34</td><td style='text-align: center;'>V0BC-CI接口信息应包含列车编组信息,联锁保证站台门开关数量与车门一致</td><td style='text-align: center;'>V0BC-CI接口规范“N_PSD”</td></tr><tr><td style='text-align: center;'>OSHA-32</td><td style='text-align: center;'>单侧客室车门数量多于站台门数量的列车进入站台且开门</td><td style='text-align: center;'>SR-0-33</td><td style='text-align: center;'>互联互通所有站台门数量大于或等于列车客室</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">IHA-29</td><td rowspan="3">车门与站台门开启数量或位置不对应</td><td style='text-align: center;'>SR-0-33</td><td style='text-align: center;'>互联互通所有站台门数量大于或等于列车客室</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-I-34</td><td style='text-align: center;'>V0BC-35接口信息应包含开关站台门数量信息,联锁保证站台门开关数量与车门一致</td><td style='text-align: center;'>V0BC-CI接口规范“N_PSD”</td></tr><tr><td style='text-align: center;'>SR-S-42</td><td style='text-align: center;'>地面设备提供商应保证列车在各站台开关站台门信息数据正确</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="5">Ref-5.2</td><td rowspan="5">人员从列车跌入轨道区域</td><td rowspan="5">PH-84</td><td rowspan="5">列车车门不安全地开启，导致乘客坠入路轨</td><td rowspan="2">IHA-26</td><td rowspan="2">列车在车门开启时移动</td><td style='text-align: center;'>SR-S-94</td><td style='text-align: center;'>车载ATP设备监控列车车门状态，列车运行过程中，车门打开后车载ATP需切断牵引、紧急制动或正常运行至下站站台</td><td style='text-align: center;'>车门防护</td></tr><tr><td style='text-align: center;'>SR-O-34</td><td style='text-align: center;'>运营责任方应统一列车运行过程中车门不安全打开应急处理预案，避免或减轻该场景下的事故影响</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>IHA-27</td><td style='text-align: center;'>列车移动过程中车门不安全开启，车载ATP未能采集到</td><td style='text-align: center;'>SR-I-37</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术采集列车车门锁闭及解锁状态信息</td><td style='text-align: center;'>车载ATO/ATP与车辆接口“列车车门锁闭状态”</td></tr><tr><td rowspan="2">IHA-31</td><td rowspan="2">列车车门开借侧导致乘客落入轨道</td><td style='text-align: center;'>SR-I-43</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术驱动列车车门开启及锁闭，车载ATP两侧车门的使能命令应相互独立</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-42</td><td style='text-align: center;'>地面设备提供商应保证列车在各站台开关站台门信息数据正确</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-5.3</td><td rowspan="4">人员被夹在列车与站台的间隙中</td><td rowspan="4">PH-85</td><td rowspan="4">列车在乘客上下车过程中移动，导致乘客被困列车与站台的间隙中</td><td style='text-align: center;'>SHA-43</td><td style='text-align: center;'>列车停车过程中不安全开启站台门</td><td style='text-align: center;'>SR-S-95</td><td style='text-align: center;'>列车进站停准停稳，车载ATP系统应确保列车不会错误移动后，输出门使能命令，联动站台门</td><td style='text-align: center;'>车门防护、车门允许、站台门控制、站台门防护</td></tr><tr><td style='text-align: center;'>SHA-44</td><td style='text-align: center;'>列车未对标停准，不安全开启车门或站台门</td><td style='text-align: center;'>SR-S-95</td><td style='text-align: center;'>运营责任方应制定切除ATP或非装备列车开关站台门操作细则</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-31</td><td style='text-align: center;'>乘客正在上下车时，列车车门不安全关闭</td><td style='text-align: center;'>SR-O-25</td><td style='text-align: center;'>列车进站停准停稳，车载ATP系统应确保列车不会错误移动后，输出门使能命令，联动站台门</td><td style='text-align: center;'>车门防护、车门允许、站台门控制、站台门防护</td></tr><tr><td style='text-align: center;'>OSHA-32</td><td style='text-align: center;'>乘客正在上下车时，站台门不安全关闭</td><td style='text-align: center;'>SR-O-26</td><td style='text-align: center;'>运营责任方应制定相关规则，确保乘客上下车完毕后再关闭车门</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td style='text-align: center;'>Ref-5.3</td><td style='text-align: center;'>人员被夹在列车与站台的间隙中</td><td style='text-align: center;'>PH-85</td><td style='text-align: center;'>列车在乘客上下车过程中移动，导致乘客被困列车与站台的间隙中</td><td style='text-align: center;'>OSHA-45</td><td style='text-align: center;'>互联互通自动折返实现方式不一致，司机在下车过程中，列车启动导致司机摔倒</td><td style='text-align: center;'>SR-0-36</td><td style='text-align: center;'>运营责任方应制定互联互通列车自动折返操作细则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">Ref-6.1</td><td rowspan="3">乘客在列车客室跌倒</td><td style='text-align: center;'>PH-86</td><td style='text-align: center;'>列车紧急制动过程中，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>OSHA-34</td><td style='text-align: center;'>列车紧急制动过程中，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>SR-0-37</td><td style='text-align: center;'>信号系统紧急制动是为了保障列车行车安全，最大程度避免或减轻行车事故发生，由此引发客室、司机室人员跌倒事故，信号系统无法提供防护</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-87</td><td style='text-align: center;'>ATO控车牵引、制动过程中，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>SHA-67</td><td style='text-align: center;'>ATO控车牵引/制动过程中，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>SR-0-38</td><td style='text-align: center;'>车载应有广播和信息提醒乘客/司机在启动、停车和运行过程中扶好站稳</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>PH-88</td><td style='text-align: center;'>RM、EUM模式下，司机控车牵引/制动，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>OSHA-46</td><td style='text-align: center;'>RM、EUM模式下，司机控车牵引/制动，导致司机等员工在司机室跌倒</td><td style='text-align: center;'>SR-0-38</td><td style='text-align: center;'>车载应有广播和信息提醒乘客/司机在启动、停车和运行过程中扶好站稳</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-6.2</td><td rowspan="4">司机等员工在司机室跌倒</td><td style='text-align: center;'>PH-89</td><td style='text-align: center;'>列车紧急制动过程中，导致乘客在列车客室跌倒</td><td style='text-align: center;'>OSHA-35</td><td style='text-align: center;'>列车紧急制动过程中，导致乘客在列车客室跌倒</td><td style='text-align: center;'>SR-O-37</td><td style='text-align: center;'>信号系统紧急制动是为了保障列车行车安全，最大程度避免或减轻行车事故发生，由此引发客室、司机室人员跌倒事故，信号系统无法提供防护</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>PH-90</td><td style='text-align: center;'>ATO控车牵引、制动过程中，导致乘客在列车客室跌倒</td><td style='text-align: center;'>SHA-67</td><td style='text-align: center;'>ATO控车牵引、制动过程中，导致乘客在列车客室跌倒</td><td style='text-align: center;'>SR-O-38</td><td style='text-align: center;'>车载应有广播和信息提醒乘客/司机在启动、停车和运行过程中扶好站稳</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>PH-91</td><td style='text-align: center;'>RM、EUM模式下，司机控车牵引/制动，导致乘客在列车客室跌倒</td><td style='text-align: center;'>OSHA-46</td><td style='text-align: center;'>RM、EUM模式下，司机控车牵引/制动，导致乘客在列车客室跌倒</td><td style='text-align: center;'>SR-O-38</td><td style='text-align: center;'>车载应有广播和信息提醒乘客/司机在启动、停车和运行过程中扶好站稳</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>PH-92</td><td style='text-align: center;'>互联互通自动折返互联互通自动折返实现方式不一致，司机在司机室时列车非预期启动，导致司机跌倒</td><td style='text-align: center;'>OSHA-47</td><td style='text-align: center;'>互联互通自动折返司机操作流程不一致，司机在司机室列车非预期启动，导致司机跌倒</td><td style='text-align: center;'>SR-O-36</td><td style='text-align: center;'>运营责任方应制定互联互通列车自动折返操作细则</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="3">Ref-7</td><td rowspan="3">触电</td><td rowspan="3">PH-93</td><td rowspan="3">触电</td><td style='text-align: center;'>IHA-30</td><td style='text-align: center;'>人员可以直接接触到车厢内的车载设备</td><td style='text-align: center;'>SR-I-38</td><td style='text-align: center;'>车辆为车载信号设备提供封闭的安装空间，只有专业人员采用专业工具才能打开</td><td style='text-align: center;'>车载ATO/ATP与车辆接口“机械接口”</td></tr><tr><td style='text-align: center;'>SHA-45</td><td style='text-align: center;'>车载设备漏电，导致乘客触电</td><td style='text-align: center;'>SR-S-97</td><td style='text-align: center;'>车载设备硬件结构设计应满足防触电要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-36</td><td style='text-align: center;'>进行信号系统维护时人员触电</td><td style='text-align: center;'>SR-O-39</td><td style='text-align: center;'>维护责任方制定信号系统维护作业细则</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">Ref-8</td><td rowspan="2">火灾</td><td rowspan="2">PH-94</td><td rowspan="2">火灾</td><td style='text-align: center;'>SHA-46</td><td style='text-align: center;'>信号设备着火引起火灾</td><td style='text-align: center;'>SR-S-98</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用易燃材料</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>OSHA-37</td><td style='text-align: center;'>发生火灾时，运营人员未按照火灾应急预案执行</td><td style='text-align: center;'>SR-O-40</td><td style='text-align: center;'>运营责任方，制定火灾应急预案</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>Ref-9</td><td style='text-align: center;'>有毒物质或气体</td><td style='text-align: center;'>PH-95</td><td style='text-align: center;'>有毒物质或气体</td><td style='text-align: center;'>SHA-47</td><td style='text-align: center;'>信号设备散发有毒物质或气体</td><td style='text-align: center;'>SR-S-99</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用有毒物质</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>Ref-10</td><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>PH-96</td><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>SHA-48</td><td style='text-align: center;'>信号设备着火引起爆炸</td><td style='text-align: center;'>SR-S-100</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用易爆材料</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害
编号</td><td rowspan="2">互联互通信号系
统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td style='text-align: center;'>Ref-10</td><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>PH-96</td><td style='text-align: center;'>爆炸</td><td style='text-align: center;'>OSHA-38</td><td style='text-align: center;'>发生爆炸
时,运营人员
未按照爆炸应
急预案执行</td><td style='text-align: center;'>SR-O-41</td><td style='text-align: center;'>运营责任方,制定爆炸应急预案</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-11</td><td style='text-align: center;'>辐射</td><td style='text-align: center;'>PH-97</td><td style='text-align: center;'>辐射</td><td style='text-align: center;'>SHA-49</td><td style='text-align: center;'>信号设备辐
射过大</td><td style='text-align: center;'>SR-S-101</td><td style='text-align: center;'>信号设备的硬件、机械结构零
部件不能含有辐射物质</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="3">Ref-12</td><td rowspan="3">电磁
干扰导
致信号
系统功
能失效</td><td rowspan="3">PH-98</td><td rowspan="3">电磁干扰
导致信号系
统功能失效</td><td style='text-align: center;'>SHA-50</td><td style='text-align: center;'>信号设备抗
干扰能力未满
足应用环境要
求,导致系统功
能失效</td><td style='text-align: center;'>SR-S-102</td><td style='text-align: center;'>信号系统设备应通对应运用
环境EMC测试</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>OSHA-39</td><td style='text-align: center;'>信号系统应
用环境干扰源
超标</td><td style='text-align: center;'>SR-O-42</td><td style='text-align: center;'>运营单位确保信号系统运营
环境电磁环境正常</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-51</td><td style='text-align: center;'>电磁干扰导
致系统失效未
导向安全侧</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故
障导向安全原则</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-13</td><td style='text-align: center;'>信号
系统电
磁干扰
超标</td><td style='text-align: center;'>PH-99</td><td style='text-align: center;'>信号系统
电磁干扰导
致佩戴医疗
设备的乘
客/工作人
员医疗设备
失效</td><td style='text-align: center;'>SHA-52</td><td style='text-align: center;'>信号系统对
使用环境电磁
干扰超标</td><td style='text-align: center;'>SR-S-102</td><td style='text-align: center;'>信号系统设备应通对应运用
环境EMC测试</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="2">Ref-14</td><td rowspan="2">雷击导致系统功能失效</td><td rowspan="2">PH-100</td><td rowspan="2">雷击导致系统功能失效</td><td style='text-align: center;'>SHA-53</td><td style='text-align: center;'>信号系统抗雷击能力未满足应用应用环境要求，导致系统功能失效</td><td style='text-align: center;'>SR-S-104</td><td style='text-align: center;'>信号系统设备应通对应运用环境防雷测试</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-54</td><td style='text-align: center;'>雷击导致信号系统失效未导向安全侧</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="4">Ref-15</td><td rowspan="4">系统网络受到外部入侵</td><td rowspan="4">PH-101</td><td rowspan="4">系统网络受到外部入侵</td><td rowspan="2">SHA-55</td><td rowspan="2">信号系统有线网络被入侵者访问</td><td style='text-align: center;'>SR-S-105</td><td style='text-align: center;'>信号系统有线网络在物理上与其他网络完全隔离</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SR-S-106</td><td style='text-align: center;'>信号系统各安全关键设备间网络通信需采用安全通信协议</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-56</td><td style='text-align: center;'>信号系统无线通信被外界干扰</td><td style='text-align: center;'>SR-S-107</td><td style='text-align: center;'>信号系统无线通信网络采用专有频段</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-57</td><td style='text-align: center;'>信号系统无线网络被非法入侵</td><td style='text-align: center;'>SR-S-106</td><td style='text-align: center;'>信号系统各安全关键设备间网络通信需采用安全通信协议</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>Ref-16</td><td style='text-align: center;'>气候条件导致信号系统失效</td><td style='text-align: center;'>PH-102</td><td style='text-align: center;'>气候条件导致信号系统失效</td><td style='text-align: center;'>SHA-58</td><td style='text-align: center;'>信号系统气候适应未满足应用环境要求，导致信号系统功能失效</td><td style='text-align: center;'>SR-S-108</td><td style='text-align: center;'>信号系统硬件设备应满足应用环境的气候条件</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="2">Ref-16</td><td rowspan="2">气候条件导致信号系统失效</td><td rowspan="2">PH-102</td><td rowspan="2">气候条件导致信号系统失效</td><td style='text-align: center;'>SHA-59</td><td style='text-align: center;'>气候原因、加速信号系统老化从而导致系统功能失效</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-60</td><td style='text-align: center;'>气候导致信号系统失效未导向安全侧</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">Ref-17</td><td rowspan="2">振动导致信号系统失效</td><td rowspan="2">PH-103</td><td rowspan="2">振动条件导致信号系统失效</td><td style='text-align: center;'>SHA-61</td><td style='text-align: center;'>信号系统抗振动性能未满足应用环境要求，导致信号系统功能失效</td><td style='text-align: center;'>SR-S-109</td><td style='text-align: center;'>信号系统硬件设备抗震性能满足其运用环境振动要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-62</td><td style='text-align: center;'>振动导致信号系统失效未导向安全侧</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td><td style='text-align: center;'>-</td></tr><tr><td rowspan="2">Ref-18</td><td rowspan="2">海拔条件导致信号系统失效</td><td rowspan="2">PH-104</td><td rowspan="2">海拔条件导致信号系统失效</td><td style='text-align: center;'>SHA-63</td><td style='text-align: center;'>信号系统海拔运用性能未满足应用环境要求，导致信号系统功能失效</td><td style='text-align: center;'>SR-S-15</td><td style='text-align: center;'>信号系统硬件设备运用海拔高度应满足互联互通项目海拔高度要求</td><td style='text-align: center;'>-</td></tr><tr><td style='text-align: center;'>SHA-64</td><td style='text-align: center;'>信号系统硬件故障未导向安全侧</td><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td><td style='text-align: center;'>-</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td style='text-align: center;'>Ref-19</td><td style='text-align: center;'>人为恶意破坏</td><td style='text-align: center;'>PH-105</td><td style='text-align: center;'>人为恶意破坏</td><td style='text-align: center;'>OSHA-40</td><td style='text-align: center;'>人为恶意破坏</td><td style='text-align: center;'>SR-0-43</td><td style='text-align: center;'>信号系统无法检测或防护人为恶意破坏，运营责任方应制定人为恶意破坏应急预案，避免或减轻事故影响</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>Ref-20</td><td style='text-align: center;'>洪水/地震/强风</td><td style='text-align: center;'>PH-106</td><td style='text-align: center;'>洪水/地震/强风</td><td style='text-align: center;'>OSHA-41</td><td style='text-align: center;'>洪水/地震/强风</td><td style='text-align: center;'>SR-0-44</td><td style='text-align: center;'>信号系统无法检测或防护洪水/地震/强风等自然灾害引发行车事故，运营责任方应制定自然灾害应急预案，避免或减轻事故影响</td><td style='text-align: center;'>—</td></tr><tr><td rowspan="2">Ref-21.1</td><td rowspan="2">基础措施超负荷承载</td><td rowspan="2">PH-107</td><td rowspan="2">基础措施超负荷承载</td><td rowspan="2">SHA-65</td><td rowspan="2">桥梁同时存在列车数量超出设计载荷造成桥梁损坏，导致行车事故</td><td style='text-align: center;'>SR-S-24</td><td style='text-align: center;'>信号系统应保证同时存在于桥梁的列车少于等于桥梁允许运营载荷要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>SR-0-45</td><td style='text-align: center;'>信号系统失效后，运营责任方应制定运营细则，保证同时存在于桥梁的列车少于等于桥梁允许运营载荷要求</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>Ref-22.1</td><td style='text-align: center;'>基础设施沉降导致列车脱轨</td><td style='text-align: center;'>PH-108</td><td style='text-align: center;'>基础设施沉降导致列车脱轨</td><td style='text-align: center;'>OSHA-42</td><td style='text-align: center;'>基础设施沉降导致列车脱轨</td><td style='text-align: center;'>SR-0-46</td><td style='text-align: center;'>信号系统无法检测或防护基础措施沉降，运营责任方应及时检测基础措施沉降情况，并将沉降导致的临时限速变化值反馈至信号系统</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>事故场景</td><td style='text-align: center;'>编号</td><td style='text-align: center;'>互联互通</td><td style='text-align: center;'>危害</td><td style='text-align: center;'>互联互通信号系统</td><td style='text-align: center;'>安全要求</td><td style='text-align: center;'>系统功能</td></tr><tr><td style='text-align: center;'>Ref-23</td><td style='text-align: center;'>基础设施坍塌</td><td style='text-align: center;'>PH-109</td><td style='text-align: center;'>基础设施坍塌</td><td style='text-align: center;'>OSHA-43</td><td style='text-align: center;'>基础设施坍塌</td><td style='text-align: center;'>SR-0-47</td><td style='text-align: center;'>信号系统无法检测或防护基础设施坍塌导致行车事故，运营责任方应运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响</td></tr><tr><td rowspan="2">Ref-24.1</td><td rowspan="2">道路作业造成维护人员伤亡</td><td rowspan="2">PH-110</td><td rowspan="2">道路作业造成维护人员伤亡</td><td style='text-align: center;'>OSHA-48</td><td style='text-align: center;'>道路作业造成维护人员伤亡</td><td style='text-align: center;'>SR-0-39</td><td style='text-align: center;'>运营责任方制定信号系统维护作业细则</td></tr><tr><td style='text-align: center;'>OSHA-49</td><td style='text-align: center;'>道路作业造成维护人员伤亡</td><td style='text-align: center;'>SR-0-48</td><td style='text-align: center;'>运营责任方针对联络线轨旁设备维护作业细则</td></tr><tr><td rowspan="2">Ref-24.2</td><td rowspan="2">列车撞到现场维护人员</td><td rowspan="2">PH-111</td><td rowspan="2">列车撞到现场维护人员</td><td style='text-align: center;'>OSHA-50</td><td style='text-align: center;'>列车撞到本线线路上维护人员</td><td style='text-align: center;'>SR-0-39</td><td style='text-align: center;'>运营责任方制定信号系统维护作业细则</td></tr><tr><td style='text-align: center;'>OSHA-51</td><td style='text-align: center;'>列车撞到联络线上维护人员</td><td style='text-align: center;'>SR-0-48</td><td style='text-align: center;'>运营责任方针对联络线轨旁设备维护作业细则</td></tr><tr><td rowspan="2">Ref-25</td><td rowspan="2">救援与疏散过程中，造成人员伤亡</td><td rowspan="2">PH-112</td><td rowspan="2">救援与疏散过程中，造成人员伤亡</td><td style='text-align: center;'>OSHA-52</td><td style='text-align: center;'>救援与疏散过程中，造成人员伤亡</td><td style='text-align: center;'>SR-0-49</td><td style='text-align: center;'>运营责任方制定救援与疏散作业细则</td></tr><tr><td style='text-align: center;'>OSHA-53</td><td style='text-align: center;'>救援与疏散过程中，造成人员伤亡</td><td style='text-align: center;'>SR-0-50</td><td style='text-align: center;'>运营责任方针对跨线救援与疏散制定作业细则</td></tr></table>

---

### 6.4 危害结果

根据表4分析结果，得出互联互通信号系统初步危害分析的系统基本危害清单（见表5）、接口危害清单（见表6）、运营危害清单（见表7）。

<div style="text-align: center;">表 5 系统危害清单</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td></tr><tr><td style='text-align: center;'>SHA-1</td><td style='text-align: center;'>列车在前后追踪运行时，ZC子系统为CBTC车计算了不安全的MA</td></tr><tr><td style='text-align: center;'>SHA-2</td><td style='text-align: center;'>后车MA计算未计算前车最大退行停车距离</td></tr><tr><td style='text-align: center;'>SHA-3</td><td style='text-align: center;'>列车动作违反了信号系统授权时，车载ATP没有有效输出紧急制动</td></tr><tr><td style='text-align: center;'>SHA-4</td><td style='text-align: center;'>车载ATP紧急制动输出故障</td></tr><tr><td style='text-align: center;'>SHA-5</td><td style='text-align: center;'>CBTC列车无限制地退行</td></tr><tr><td style='text-align: center;'>SHA-6</td><td style='text-align: center;'>后车MA计算未包含前车最大后溜停车距离，最大后溜停车距离未统一</td></tr><tr><td style='text-align: center;'>SHA-7</td><td style='text-align: center;'>ZC计算MA未包含前车最大后溜距离</td></tr><tr><td style='text-align: center;'>SHA-8</td><td style='text-align: center;'>CBTC列车无限制地向后溜车</td></tr><tr><td style='text-align: center;'>SHA-9</td><td style='text-align: center;'>ITC列车VOBC计算MA（防护点）未包含前车最大退行距离</td></tr><tr><td style='text-align: center;'>SHA-10</td><td style='text-align: center;'>计轴区段设计过短</td></tr><tr><td style='text-align: center;'>SHA-11</td><td style='text-align: center;'>ITC列车无限制地退行</td></tr><tr><td style='text-align: center;'>SHA-12</td><td style='text-align: center;'>ITC列车无限制地向后溜车</td></tr><tr><td style='text-align: center;'>SHA-13</td><td style='text-align: center;'>RM模式列车司机未按联锁信号行车</td></tr><tr><td style='text-align: center;'>SHA-14</td><td style='text-align: center;'>联络线交接时，由于通信延迟导致列车在本线丢失</td></tr><tr><td style='text-align: center;'>SHA-15</td><td style='text-align: center;'>列车位置计算错误，导致当前位置EBI计算过高</td></tr><tr><td style='text-align: center;'>SHA-16</td><td style='text-align: center;'>线路数据错误导致EBI计算错误</td></tr><tr><td style='text-align: center;'>SHA-17</td><td style='text-align: center;'>线路障碍物状态信息错误导致EBI计算错误</td></tr><tr><td style='text-align: center;'>SHA-18</td><td style='text-align: center;'>CBTC级别下，临时限速未正确传输至车载ATP系统</td></tr><tr><td style='text-align: center;'>SHA-19</td><td style='text-align: center;'>ITC级别下，车载MA计算错误</td></tr><tr><td style='text-align: center;'>SHA-20</td><td style='text-align: center;'>运行方向错误导致ZCMA计算错误，从而导致行车事故</td></tr></table>

---

<div style="text-align: center;">表 5 系统危害清单(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td></tr><tr><td style='text-align: center;'>SHA-21</td><td style='text-align: center;'>列车折返过程中，ATP错误输出激活端信息，导致ZC错误控制列车</td></tr><tr><td style='text-align: center;'>SHA-22</td><td style='text-align: center;'>列车安全位置输出错误，导致地面ZC为该列车或追踪该列车的其他列车MA计算错误</td></tr><tr><td style='text-align: center;'>SHA-23</td><td style='text-align: center;'>列车运行控制级别、驾驶模式传输错误，导致地面ZC为该列车或追踪该列车的其他列车MA计算错误</td></tr><tr><td style='text-align: center;'>SHA-24</td><td style='text-align: center;'>列车停车保证计算错误</td></tr><tr><td style='text-align: center;'>SHA-25</td><td style='text-align: center;'>列车输出保护区段允许解锁信息后，列车不安全启动</td></tr><tr><td style='text-align: center;'>SHA-26</td><td style='text-align: center;'>跨线进路设计时，不符合跨线进路信号开放要求</td></tr><tr><td style='text-align: center;'>SHA-27</td><td style='text-align: center;'>联络线计轴点设置不满足侧防安全距离</td></tr><tr><td style='text-align: center;'>SHA-28</td><td style='text-align: center;'>联络线列车反向运行时，ZC子系统为CBTC车计算了不安全的MA</td></tr><tr><td style='text-align: center;'>SHA-29</td><td style='text-align: center;'>列车的动作违反了信号系统的授权时，未能实施紧急制动</td></tr><tr><td style='text-align: center;'>SHA-30</td><td style='text-align: center;'>联络线列车反向运行时，信号系统给出IPC级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>SHA-31</td><td style='text-align: center;'>列车反向运行时，信号系统给出RM模式列车不安全的授权</td></tr><tr><td style='text-align: center;'>SHA-32</td><td style='text-align: center;'>车载ATP对列车解体没有防护</td></tr><tr><td style='text-align: center;'>SHA-33</td><td style='text-align: center;'>车载ATP紧急制动输出故障</td></tr><tr><td style='text-align: center;'>SHA-34</td><td style='text-align: center;'>信号系统给CBTC级别列车的授权超出了线路边界</td></tr><tr><td style='text-align: center;'>SHA-35</td><td style='text-align: center;'>信号系统给ITC级别列车的授权超出了线路边界</td></tr><tr><td style='text-align: center;'>SHA-36</td><td style='text-align: center;'>信号系统给RM模式列车的授权超出了线路边界</td></tr><tr><td style='text-align: center;'>SHA-37</td><td style='text-align: center;'>道岔未密贴且锁闭时，信号系统给出CBTC级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>SHA-38</td><td style='text-align: center;'>道岔未密贴且锁闭时，信号系统给出ITC级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>SHA-39</td><td style='text-align: center;'>道岔未密贴且锁闭时，信号系统给出RM模式列车不安全的授权</td></tr><tr><td style='text-align: center;'>SHA-40</td><td style='text-align: center;'>列车在道岔区域时，道岔动作</td></tr><tr><td style='text-align: center;'>SHA-41</td><td style='text-align: center;'>信号系统为列车计算的安全限制速度超过了线路限速</td></tr><tr><td style='text-align: center;'>SHA-42</td><td style='text-align: center;'>列车运行速度超过信号系统的安全限制速度时，未能够实施紧急制动</td></tr><tr><td style='text-align: center;'>SHA-43</td><td style='text-align: center;'>列车停车过程中不安全开启站台门</td></tr></table>

---

<div style="text-align: center;">表 5 系统危害清单(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td></tr><tr><td style='text-align: center;'>SHA-44</td><td style='text-align: center;'>列车未对标停准，不安全开启车门或站台门</td></tr><tr><td style='text-align: center;'>SHA-45</td><td style='text-align: center;'>车载设备漏电，导致乘客触电</td></tr><tr><td style='text-align: center;'>SHA-46</td><td style='text-align: center;'>信号设备着火引起火灾</td></tr><tr><td style='text-align: center;'>SHA-47</td><td style='text-align: center;'>信号设备散发有毒物质或气体</td></tr><tr><td style='text-align: center;'>SHA-48</td><td style='text-align: center;'>信号设备着火引起爆炸</td></tr><tr><td style='text-align: center;'>SHA-49</td><td style='text-align: center;'>信号设备辐射过大</td></tr><tr><td style='text-align: center;'>SHA-50</td><td style='text-align: center;'>信号设备抗干扰能力未满足应用环境要求，导致系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-51</td><td style='text-align: center;'>电磁干扰导致系统失效未导向安全侧</td></tr><tr><td style='text-align: center;'>SHA-52</td><td style='text-align: center;'>信号系统对使用环境电磁干扰超标</td></tr><tr><td style='text-align: center;'>SHA-53</td><td style='text-align: center;'>信号系统抗雷击能力未满足应用环境要求，导致系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-54</td><td style='text-align: center;'>雷击导致信号系统失效未导向安全侧</td></tr><tr><td style='text-align: center;'>SHA-55</td><td style='text-align: center;'>信号系统有线网络被入侵者访问</td></tr><tr><td style='text-align: center;'>SHA-56</td><td style='text-align: center;'>信号系统无线通信被外界干扰</td></tr><tr><td style='text-align: center;'>SHA-57</td><td style='text-align: center;'>信号系统无线网络被非法入侵</td></tr><tr><td style='text-align: center;'>SHA-58</td><td style='text-align: center;'>信号系统气候适应未满足应用环境要求，导致信号系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-59</td><td style='text-align: center;'>气候原因，加速信号系统老化从而导致系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-60</td><td style='text-align: center;'>气候导致信号系统失效未导向安全侧</td></tr><tr><td style='text-align: center;'>SHA-61</td><td style='text-align: center;'>信号系统抗振动性能未满足应用环境要求，导致信号系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-62</td><td style='text-align: center;'>振动导致信号系统失效未导向安全侧</td></tr><tr><td style='text-align: center;'>SHA-63</td><td style='text-align: center;'>信号系统海拔运用性能未满足应用环境要求，导致信号系统功能失效</td></tr><tr><td style='text-align: center;'>SHA-64</td><td style='text-align: center;'>信号系统硬件故障未导向安全侧</td></tr><tr><td style='text-align: center;'>SHA-65</td><td style='text-align: center;'>桥梁同时存在列车数量超出设计载荷造成桥梁损坏，导致行车事故</td></tr><tr><td style='text-align: center;'>SHA-66</td><td style='text-align: center;'>站台门打开时，连锁未关闭进站/出站进路</td></tr><tr><td style='text-align: center;'>SHA-67</td><td style='text-align: center;'>ATO控车牵引/制动过程中，导致司机等员工在司机室跌倒</td></tr></table>

---

<div style="text-align: center;">表 6 接口危害清单</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td></tr><tr><td style='text-align: center;'>IHA-1</td><td style='text-align: center;'>列车编组信息与车长不匹配</td></tr><tr><td style='text-align: center;'>IHA-2</td><td style='text-align: center;'>联络线交接时，通信延时导致列车在本线丢失</td></tr><tr><td style='text-align: center;'>IHA-3</td><td style='text-align: center;'>联络线交接时，通信延时导致列车在他线丢失</td></tr><tr><td style='text-align: center;'>IHA-4</td><td style='text-align: center;'>联络线ZC-ZC接口信息传输错误</td></tr><tr><td style='text-align: center;'>IHA-5</td><td style='text-align: center;'>联络线CI-CI接口信息传输错误</td></tr><tr><td style='text-align: center;'>IHA-6</td><td style='text-align: center;'>互联互通车载电子地图错误</td></tr><tr><td style='text-align: center;'>IHA-7</td><td style='text-align: center;'>共线V0BC-ZC通信故障判断不及时，导致应回撤的MA未及时回撤</td></tr><tr><td style='text-align: center;'>IHA-8</td><td style='text-align: center;'>共线车地应答器通信故障</td></tr><tr><td style='text-align: center;'>IHA-9</td><td style='text-align: center;'>ZC向V0BC发送紧急停车命令不成功</td></tr><tr><td style='text-align: center;'>IHA-10</td><td style='text-align: center;'>车载ATP对列车解体采集信息失效</td></tr><tr><td style='text-align: center;'>IHA-11</td><td style='text-align: center;'>车辆没有正确采集车载ATP的紧急制动信息</td></tr><tr><td style='text-align: center;'>IHA-12</td><td style='text-align: center;'>信号系统未检测到防淹门关闭，ZC为CBTC、ITC列车计算MA越过防淹门</td></tr><tr><td style='text-align: center;'>IHA-13</td><td style='text-align: center;'>信号系统未检测到防淹门关闭，联锁系统为RM列车开放不安全进路</td></tr><tr><td style='text-align: center;'>IHA-14</td><td style='text-align: center;'>列车正在通过防淹门时，防淹关闭，列车撞上防淹门</td></tr><tr><td style='text-align: center;'>IHA-15</td><td style='text-align: center;'>列车即将进入防淹门所在进路时防淹关闭，列车撞上防淹门</td></tr><tr><td style='text-align: center;'>IHA-16</td><td style='text-align: center;'>站台门打开时，信号系统给出CBTC级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>IHA-17</td><td style='text-align: center;'>紧急关闭按钮激活时，信号系统给出CBTC级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>IHA-18</td><td style='text-align: center;'>本线线路临时限速未传递到他线车载ATP系统</td></tr><tr><td style='text-align: center;'>IHA-19</td><td style='text-align: center;'>他线车载ATP收到本线临时限速后，紧急制动曲线计算未正确采用</td></tr><tr><td style='text-align: center;'>IHA-20</td><td style='text-align: center;'>本线为他线车载提供了错误的线路限速数据</td></tr><tr><td style='text-align: center;'>IHA-21</td><td style='text-align: center;'>他线车载ATP错误地使用了本线线路数据</td></tr><tr><td style='text-align: center;'>IHA-22</td><td style='text-align: center;'>通信中断或者阻塞，信号系统开关门命令延时发送，导致站台门错误开启</td></tr></table>

---

<div style="text-align: center;">表 6 接口危害清单(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统场景危害分解</td></tr><tr><td style='text-align: center;'>IHA-23</td><td style='text-align: center;'>CI收到错误开关站台门信息</td></tr><tr><td style='text-align: center;'>IHA-24</td><td style='text-align: center;'>站台门状态信息错误，导致列车不安全启动</td></tr><tr><td style='text-align: center;'>IHA-25</td><td style='text-align: center;'>互联互通接口错误，导致开关门信息错误</td></tr><tr><td style='text-align: center;'>IHA-26</td><td style='text-align: center;'>列车在车门开启时移动</td></tr><tr><td style='text-align: center;'>IHA-27</td><td style='text-align: center;'>列车移动过程中车门不安全开启，车载ATP未能采集到</td></tr><tr><td style='text-align: center;'>IHA-28</td><td style='text-align: center;'>VOBC输出不匹配的开门码信息，开启站台门错误侧</td></tr><tr><td style='text-align: center;'>IHA-29</td><td style='text-align: center;'>车门与站台门开启数量或位置不对应</td></tr><tr><td style='text-align: center;'>IHA-30</td><td style='text-align: center;'>人员可以直接接触到车厢内的车载设备</td></tr><tr><td style='text-align: center;'>IHA-31</td><td style='text-align: center;'>列车车门开错侧导致乘客落入轨道</td></tr></table>

<div style="text-align: center;">表 7 运营危害清单</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统运营危害清单危害分解</td></tr><tr><td style='text-align: center;'>OSHA-1</td><td style='text-align: center;'>车辆紧急制动系统失效</td></tr><tr><td style='text-align: center;'>OSHA-2</td><td style='text-align: center;'>联锁级别下，司机无限制地退行</td></tr><tr><td style='text-align: center;'>OSHA-3</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机未按规定行车</td></tr><tr><td style='text-align: center;'>OSHA-4</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车司机无限制地退行</td></tr><tr><td style='text-align: center;'>OSHA-5</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车无限制后溜</td></tr><tr><td style='text-align: center;'>OSHA-6</td><td style='text-align: center;'>RM模式列车无限制后溜</td></tr><tr><td style='text-align: center;'>OSHA-7</td><td style='text-align: center;'>车辆紧急制动系统失效</td></tr><tr><td style='text-align: center;'>OSHA-8</td><td style='text-align: center;'>解体列车的某部分已经完全与车载ATP物理隔离，无法收到ATP紧急制动的信息</td></tr><tr><td style='text-align: center;'>OSHA-9</td><td style='text-align: center;'>ZC系统未处理解体列车信息，导致后续列车与解体列车相撞</td></tr><tr><td style='text-align: center;'>OSHA-10</td><td style='text-align: center;'>列车撞到轨道（含联络线）上施工或维护的工具或材料</td></tr><tr><td style='text-align: center;'>OSHA-11</td><td style='text-align: center;'>列车撞到站台上施工或维护遗落的工具或材料</td></tr></table>

---

<div style="text-align: center;">表 7 运营危害清单(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统运营危害清单危害分解</td></tr><tr><td style='text-align: center;'>OSHA-12</td><td style='text-align: center;'>列车与轨道上的信号设备相撞</td></tr><tr><td style='text-align: center;'>OSHA-13</td><td style='text-align: center;'>列车与跌落在轨道上的其他物体相撞</td></tr><tr><td style='text-align: center;'>OSHA-14</td><td style='text-align: center;'>列车与车辆段平交道口的汽车或其他机动车相撞</td></tr><tr><td style='text-align: center;'>OSHA-15</td><td style='text-align: center;'>列车与掉落在车辆段平交道口区域的物体（从其他交通工具掉落的物体）相撞</td></tr><tr><td style='text-align: center;'>OSHA-16</td><td style='text-align: center;'>不能被信号系统识别的列车上线安全事故导致</td></tr><tr><td style='text-align: center;'>OSHA-17</td><td style='text-align: center;'>信号系统与防淹门无接口信息，列车行车安全信号系统无法防护</td></tr><tr><td style='text-align: center;'>OSHA-18</td><td style='text-align: center;'>站台门打开时，信号系统输出ITC-CI级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>OSHA-19</td><td style='text-align: center;'>紧急关闭按钮激活时，信号系统给出ITC-CI级别列车不安全的授权</td></tr><tr><td style='text-align: center;'>OSHA-20</td><td style='text-align: center;'>列车关门时，有人被夹在站台门和车门之间</td></tr><tr><td style='text-align: center;'>OSHA-21</td><td style='text-align: center;'>站台门关门时，有人被夹在站台门和车门之间</td></tr><tr><td style='text-align: center;'>OSHA-22</td><td style='text-align: center;'>列车撞到站台上的施工或维护人员</td></tr><tr><td style='text-align: center;'>OSHA-23</td><td style='text-align: center;'>列车撞到轨道上的施工或维护人员</td></tr><tr><td style='text-align: center;'>OSHA-24</td><td style='text-align: center;'>列车撞到车辆段的工作人员</td></tr><tr><td style='text-align: center;'>OSHA-25</td><td style='text-align: center;'>轨道断裂导致列车脱轨</td></tr><tr><td style='text-align: center;'>OSHA-26</td><td style='text-align: center;'>车轮或车轴断裂导致列车脱轨</td></tr><tr><td style='text-align: center;'>OSHA-27</td><td style='text-align: center;'>列车脱轨侵入其他轨道撞击正在行驶列车</td></tr><tr><td style='text-align: center;'>OSHA-28</td><td style='text-align: center;'>列车撞击脱轨入侵的列车</td></tr><tr><td style='text-align: center;'>OSHA-29</td><td style='text-align: center;'>站台屏蔽系统错误，不安全开启站台门</td></tr><tr><td style='text-align: center;'>OSHA-30</td><td style='text-align: center;'>站台人员不安全开启站台门</td></tr><tr><td style='text-align: center;'>OSHA-31</td><td style='text-align: center;'>乘客正在上下车时，列车车门不安全关闭</td></tr><tr><td style='text-align: center;'>OSHA-32</td><td style='text-align: center;'>乘客正在上下车时，站台门不安全关闭</td></tr></table>

---

<div style="text-align: center;">表 7 运营危害清单(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>危害编号</td><td style='text-align: center;'>互联互通信号系统运营危害清单危害分解</td></tr><tr><td style='text-align: center;'>OSHA-33</td><td style='text-align: center;'>单侧客室车门数量多于站台门数量的列车进入站台且开门</td></tr><tr><td style='text-align: center;'>OSHA-34</td><td style='text-align: center;'>列车紧急制动过程中，导致司机等员工在司机室跌倒</td></tr><tr><td style='text-align: center;'>OSHA-35</td><td style='text-align: center;'>列车紧急制动过程中，导致乘客在列车客室跌倒</td></tr><tr><td style='text-align: center;'>OSHA-36</td><td style='text-align: center;'>进行信号系统维护时人员触电</td></tr><tr><td style='text-align: center;'>OSHA-37</td><td style='text-align: center;'>发生火灾时，运营人员未按照火灾应急预案执行</td></tr><tr><td style='text-align: center;'>OSHA-38</td><td style='text-align: center;'>发生爆炸时，运营人员未按照爆炸应急预案执行</td></tr><tr><td style='text-align: center;'>OSHA-39</td><td style='text-align: center;'>信号系统应用环境干扰源超标</td></tr><tr><td style='text-align: center;'>OSHA-40</td><td style='text-align: center;'>人为恶意破坏</td></tr><tr><td style='text-align: center;'>OSHA-41</td><td style='text-align: center;'>洪水/地震/强风</td></tr><tr><td style='text-align: center;'>OSHA-42</td><td style='text-align: center;'>基础设施沉降导致列车脱轨</td></tr><tr><td style='text-align: center;'>OSHA-43</td><td style='text-align: center;'>基础设施坍塌</td></tr><tr><td style='text-align: center;'>OSHA-44</td><td style='text-align: center;'>信号系统与人防门无接口信息，列车行车安全信号系统无法防护</td></tr><tr><td style='text-align: center;'>OSHA-45</td><td style='text-align: center;'>互联互通自动折返实现方式不一致，司机在下车过程中，列车启动导致司机摔倒</td></tr><tr><td style='text-align: center;'>OSHA-46</td><td style='text-align: center;'>RM、EUM模式下，司机控车牵引/制动，导致司机等员工在司机室跌倒</td></tr><tr><td style='text-align: center;'>OSHA-47</td><td style='text-align: center;'>互联互通自动折返司机操作流程不一致，司机在司机室列车非预期启动，导致司机跌倒</td></tr><tr><td style='text-align: center;'>OSHA-48</td><td style='text-align: center;'>道岔动作造成维护人员伤亡</td></tr><tr><td style='text-align: center;'>OSHA-49</td><td style='text-align: center;'>联锁线道岔维护时，道岔动作造成维护人员伤亡</td></tr><tr><td style='text-align: center;'>OSHA-50</td><td style='text-align: center;'>互联互通列车撞到本线线路上维护人员</td></tr><tr><td style='text-align: center;'>OSHA-51</td><td style='text-align: center;'>互联互通列车撞到联络线上维护人员</td></tr><tr><td style='text-align: center;'>OSHA-52</td><td style='text-align: center;'>救援与疏散过程中，造成人员伤亡</td></tr><tr><td style='text-align: center;'>OSHA-53</td><td style='text-align: center;'>跨线救援与疏散过程中，造成人员伤亡</td></tr></table>

---

## 7 安全要求

### 7.1 系统需求

通过对危害进行分析，互联互通信号初步系统危害安全要求如下。

#### 7.1.1 车载 ATP 系统

车载 ATP 系统安全要求内容见表 8。

<div style="text-align: center;">表 8 车载 ATP 系统安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-1</td><td style='text-align: center;'>在CBTC、ITC级别下，车载ATP应根据当前列车运行速度限制条件进行紧急制动触发速度（EBI）的计算，列车当前速度≥EBI速度时，ATP实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-2</td><td style='text-align: center;'>车载ATP系统测速测距精度满足控车要求，且满足安装环境下的振动和气候要求，如雨雪、温度的要求。车载ATP测速测距故障时，系统应对列车实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-19</td><td style='text-align: center;'>联络线车辆交接时，车载ATP应能正确处理他线ZC发送的MA</td></tr><tr><td style='text-align: center;'>SR-S-20</td><td style='text-align: center;'>联络线车辆交接失败时，车载ATP应保证列车在当前ZC分界点前停车或紧急停车</td></tr><tr><td style='text-align: center;'>SR-S-23</td><td style='text-align: center;'>车载ATP系统应保证所有互联互通公有电子地图版本的正确性和兼容性，共线、跨线运行时，如果发现车载ATP与ZC、CI和ATS版本不一致或不兼容时，对应车地通信无效，对应接口命令不执行</td></tr><tr><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td></tr><tr><td style='text-align: center;'>SR-S-27</td><td style='text-align: center;'>车载ATP将实际速度与当前EBI进行比较，如果实际速度≥监控速度，应输出紧急制动命令</td></tr><tr><td style='text-align: center;'>SR-S-28</td><td style='text-align: center;'>车载ATP系统监督列车地退行速度和退行距离，列车退行超过允许退行速度或最大退行EB触发距离后，将实施紧急制动</td></tr></table>

---

<div style="text-align: center;">表 8 车载 ATP 系统安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-29</td><td style='text-align: center;'>车载ATP系统监督列车的后溜速度和后溜距离，列车后溜超过允许后溜速度或最大后溜EB触发距离后，列车将实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-30</td><td style='text-align: center;'>在车辆保证紧急制动力正常的前提下，车载ATP向车辆输出的紧急制动命令须能保证列车在安全制动距离范围完全停稳</td></tr><tr><td style='text-align: center;'>SR-S-31</td><td style='text-align: center;'>车载ATP一旦开始向车辆输出紧急制动命令，在紧急制动触发条件解除前，ATP不能自行缓解紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-36</td><td style='text-align: center;'>ATP计算列车安全包络时，应包含列车当前速度、加速度、测速测距误差、轨旁设备安装误差及通信延时时间（速度信号生成至车载ATP位置计算完成时间）</td></tr><tr><td style='text-align: center;'>SR-S-46</td><td style='text-align: center;'>CBTC级别下，车载ATP计算EBI曲线时，应包含互联互通临时限速</td></tr><tr><td style='text-align: center;'>SR-S-53</td><td style='text-align: center;'>如应答器实际位置与电子地图位置偏差超出安全距离，车辆ATP系统应能判断出，并导向安全侧处理</td></tr><tr><td style='text-align: center;'>SR-S-57</td><td style='text-align: center;'>列车折返换端过程中，车载ATP应保证列车不能移动</td></tr><tr><td style='text-align: center;'>SR-S-58</td><td style='text-align: center;'>列车测速测距系统应能准确判断出列车的速度和方向</td></tr><tr><td style='text-align: center;'>SR-S-59</td><td style='text-align: center;'>车载ATP应能正确判断出列车停准停稳状态</td></tr><tr><td style='text-align: center;'>SR-S-62</td><td style='text-align: center;'>车载ATP系统停车保证功能，应包含列车当前位置、速度、安全防护距离</td></tr><tr><td style='text-align: center;'>SR-S-63</td><td style='text-align: center;'>列车仅在保证列车不会进入前方保护区段后，才能发出保护区段允许解锁</td></tr><tr><td style='text-align: center;'>SR-S-65</td><td style='text-align: center;'>V0BC发送“允许解锁”信息后，应保证列车不会进入前方保护区段，直至前方进路重新开放</td></tr></table>

---

<div style="text-align: center;">表 8 车载 ATP 系统安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-71</td><td style='text-align: center;'>CBTC、ITC列车的动作违反了信号系统的授权时，ATP实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-72</td><td style='text-align: center;'>在CBTC级别、ITC级别和RM模式下，车载ATP应能够持续监督车辆发送的列车完整性状态，若采集到列车完整性丢失，ATP应向车辆持续输出紧急制动命令</td></tr><tr><td style='text-align: center;'>SR-S-76</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车即将进入站台轨时，站台门打开，车载ATP应保证列车在站外停车或实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-77</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，进站过程中，站台门打开，车载ATP应实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-78</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控站台门的开启和关闭状态，列车出站过程中且最小安全后端尚未出清站台轨，站台门打开，车载ATP应实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-81</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车即将进入站台轨时，紧急关闭按钮激活，车载ATP应保证列车在站外停车或实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-82</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车进站过程中，紧急关闭按钮激活，车载ATP应实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-83</td><td style='text-align: center;'>CBTC级别下，车载ATP设备监控紧急关闭按钮状态，列车出站过程中且最小安全后端尚未出清站台轨，紧急关闭按钮激活，车载ATP应实施紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-91</td><td style='text-align: center;'>CBTC、ITC列车计算安全限速不应超过线路限速</td></tr><tr><td style='text-align: center;'>SR-S-94</td><td style='text-align: center;'>车载ATP设备监控列车车门状态，列车运行过程中，车门打开后车载ATP需切断牵引、紧急制动或正常运行至下站站台</td></tr><tr><td style='text-align: center;'>SR-S-95</td><td style='text-align: center;'>列车进站停准停稳，车载ATP系统应确保列车不会错误移动后，输出门使能命令，联动站台门</td></tr><tr><td style='text-align: center;'>SR-S-96</td><td style='text-align: center;'>互联互通线路应规范各信号系统间通信延时时间，V0BC-ZC通信延时超时应判断为通信中断，若此时列车处于CBTC级别下，车载ATP应输出紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-97</td><td style='text-align: center;'>车载设备硬件结构设计应满足防触电要求</td></tr></table>

---

#### 7.1.2 ZC 系统

ZC 系统安全要求的内容见表 9。

<div style="text-align: center;">表 9 ZC 系统安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-3</td><td style='text-align: center;'>在CBTC控制级别下，ZC确定列车的运行方向和列车的运行权限，并保证前行列车和追踪列车间的安全间隔</td></tr><tr><td style='text-align: center;'>SR-S-12</td><td style='text-align: center;'>互联互通联络线ZC交接时，本线ZC应保证为他线CBTC列车计算正确的MA</td></tr><tr><td style='text-align: center;'>SR-S-16</td><td style='text-align: center;'>ZC应对管辖范围内的列车进行识别和跟踪，保证列车序列正确，并根据列车安全位置及进路信息，为CBTC级别列车计算MA</td></tr><tr><td style='text-align: center;'>SR-S-17</td><td style='text-align: center;'>ZC应对管辖范围内的所有共线、跨线运营列车ID进行管理，对各CBTC列车ID进行唯一检查。发现本ZC管辖范围重复ID时，重复ID列车降级运行；发现向接管ZC申请授权列车重复ID时，ZC则拒绝该车的报文，不让成功建链</td></tr><tr><td style='text-align: center;'>SR-S-18</td><td style='text-align: center;'>联络线车辆交接时，ZC应能正确识别他线进入的列车</td></tr><tr><td style='text-align: center;'>SR-S-24</td><td style='text-align: center;'>信号系统应保证同时存在于桥梁的列车≤桥梁允许运营载荷要求</td></tr><tr><td style='text-align: center;'>SR-S-26</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大退行停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大退行停车距离</td></tr><tr><td style='text-align: center;'>SR-S-32</td><td style='text-align: center;'>CBTC级别下，ZC计算MA时，应包含运行前方列车最大后溜停车距离；ITC级别下，车载ATP计算MA时，应包含运行前方列车最大后溜停车距离</td></tr><tr><td style='text-align: center;'>SR-S-35</td><td style='text-align: center;'>互联互通线路应规范ZC-ZC间通信延时时间，超时应判断为通信中断，ZC回缩移动授权至ZC边界前一计轴入口点撤回一个最大允许安装误差处</td></tr><tr><td style='text-align: center;'>SR-S-36</td><td style='text-align: center;'>ATP计算列车安全包络时，应包含列车当前速度、加速度、测速测距误差、轨旁设备安装误差及通信延时时间（速度信号生成至车载ATP位置计算完成时间）</td></tr><tr><td style='text-align: center;'>SR-S-56</td><td style='text-align: center;'>ZC计算列车MA时，应检查列车运行方向和进路的一致性</td></tr><tr><td style='text-align: center;'>SR-S-60</td><td style='text-align: center;'>ZC系统应对在线运行列车控制级别或驾驶模式进行管理</td></tr></table>

---

<div style="text-align: center;">表 9 ZC 系统安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-61</td><td style='text-align: center;'>ZC系统为CBTC列车计算MA时，应识别前车运行级别及其后端安全包络</td></tr><tr><td style='text-align: center;'>SR-S-79</td><td style='text-align: center;'>CBTC级别下，ZC设备监控站台门的开启、关闭和未知状态，并实时传递给车载ATP系统</td></tr></table>

#### 7.1.3 联锁系统

联锁系统安全要求的内容见表10。

<div style="text-align: center;">表 10 联锁系统安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-4</td><td style='text-align: center;'>联络线联锁设备建立进路时，敌对进路应相互照查</td></tr><tr><td style='text-align: center;'>SR-S-5</td><td style='text-align: center;'>联络线联锁设备需保证建立的进路为锁闭状态，不能迎面解锁列车运行前方的部分进路</td></tr><tr><td style='text-align: center;'>SR-S-6</td><td style='text-align: center;'>信号开放/进路办理检查条件应符合联锁表要求</td></tr><tr><td style='text-align: center;'>SR-S-7</td><td style='text-align: center;'>单列或多列列车在同一区段内运行时，轨道占用检测设备应能正确判断计轴区段的占用/出清状态，符合故障导向安全原则</td></tr><tr><td style='text-align: center;'>SR-S-8</td><td style='text-align: center;'>计轴复位命令需经过二次确认</td></tr><tr><td style='text-align: center;'>SR-S-9</td><td style='text-align: center;'>应采用安全继电器或其他安全接口技术传输轨道的占用状态信息</td></tr><tr><td style='text-align: center;'>SR-S-24</td><td style='text-align: center;'>信号系统应保证同时存在于桥梁的列车≤桥梁允许运营载荷要求</td></tr><tr><td style='text-align: center;'>SR-S-34</td><td style='text-align: center;'>互联互通计轴区段设计时应计算侵线计轴、列车悬垂距离、通信延迟、列车最大退行/后溜停车距离</td></tr><tr><td style='text-align: center;'>SR-S-44</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集道岔的状态信息</td></tr><tr><td style='text-align: center;'>SR-S-45</td><td style='text-align: center;'>采用安全继电器或其他安全接口技术采集紧急关闭按钮状态信息</td></tr><tr><td style='text-align: center;'>SR-S-64</td><td style='text-align: center;'>在联锁无法接收ATP发送的停稳信息时，采用计时方式判定停稳，计时时间应根据列车停稳计算取最大值</td></tr><tr><td style='text-align: center;'>SR-S-66</td><td style='text-align: center;'>CBTC级别下，互联互通车载ATP收到ZC列车控制信息紧急制动命令或有紧急制动命令报文的特殊命令，应立即执行紧急制动</td></tr></table>

---

<div style="text-align: center;">表 10 联锁系统安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-67</td><td style='text-align: center;'>互联互通跨线进路应遵循统一原则，保证进路正确</td></tr><tr><td style='text-align: center;'>SR-S-68</td><td style='text-align: center;'>统一侧防最小安全距离，线路条件允许时，联络线及其相邻计轴点及其停车点设计满足侧防要求</td></tr><tr><td style='text-align: center;'>SR-S-69</td><td style='text-align: center;'>由于线路限制，联络线计轴点及其停车点不满足超限设计时，系统应按照侵限设计</td></tr><tr><td style='text-align: center;'>SR-S-70</td><td style='text-align: center;'>信号系统具备CBTC、ITC、联锁级别下双方向运行的安全防护功能，联络线方向运行进路建立后，敌对进路不能建立</td></tr><tr><td style='text-align: center;'>SR-S-74</td><td style='text-align: center;'>运营线路终端的信号机应该常亮红灯显示</td></tr><tr><td style='text-align: center;'>SR-S-80</td><td style='text-align: center;'>站台门打开时，联锁系统根据站型关闭对应进站/出站进路</td></tr><tr><td style='text-align: center;'>SR-S-84</td><td style='text-align: center;'>CI监控车站紧急关闭按钮的状态，一旦检测到按钮被按下，立即关闭相应的列车进路信号</td></tr><tr><td style='text-align: center;'>SR-S-85</td><td style='text-align: center;'>紧急关闭按钮故障时联锁应能够检测到且导向安全侧</td></tr><tr><td style='text-align: center;'>SR-S-86</td><td style='text-align: center;'>联锁控制道岔的命令必须同排列的进路中道岔的位置一致，同时锁闭道岔，联锁设备才能建立进路</td></tr><tr><td style='text-align: center;'>SR-S-87</td><td style='text-align: center;'>道岔子系统能给出正确的道岔状态表示</td></tr><tr><td style='text-align: center;'>SR-S-88</td><td style='text-align: center;'>道岔转换完毕后，应保证道岔固定在规定位置不再移动，直至下次联锁或人工转换道岔命令下达</td></tr><tr><td style='text-align: center;'>SR-S-89</td><td style='text-align: center;'>道岔受进路锁闭、区段锁闭或人工单独锁闭时，联锁须不能控制道岔移动</td></tr><tr><td style='text-align: center;'>SR-S-90</td><td style='text-align: center;'>只有当道岔位置与操作要求一致，并经检查自动开闭器的两组接点排的相应接点位置正确，才能构成道岔位置的正确表示</td></tr><tr><td style='text-align: center;'>SR-S-92</td><td style='text-align: center;'>CI监控站台门的开启和关闭状态，如果站台门打开，应关闭与该屏蔽门相关联的进路</td></tr></table>

---

#### 7.1.4 数据准备

数据准备安全要求的内容见表11。

<div style="text-align: center;">表 11 数据准备安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-10</td><td style='text-align: center;'>互联互通公用电子地图应包含车载ATP计算EBI的所有线路数据，包含线路静态限速、坡度信息、道岔</td></tr><tr><td style='text-align: center;'>SR-S-11</td><td style='text-align: center;'>系统线路数据准备过程应被定义流程规范，确保数据全面、正确，该过程应进行安全分析和安全评估</td></tr><tr><td style='text-align: center;'>SR-S-13</td><td style='text-align: center;'>车辆提供方应保证互联互通列车编组信息配置正确</td></tr><tr><td style='text-align: center;'>SR-S-14</td><td style='text-align: center;'>V0BC-ZC接口信息应包含互联互通列车车长信息</td></tr><tr><td style='text-align: center;'>SR-S-21</td><td style='text-align: center;'>统一互联互通公有数据，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-S-22</td><td style='text-align: center;'>互联互通用数据版本应进行配置管理，确保现场使用数据正确性</td></tr><tr><td style='text-align: center;'>SR-S-25</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-33</td><td style='text-align: center;'>互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动</td></tr><tr><td style='text-align: center;'>SR-S-37</td><td style='text-align: center;'>地面设备提供商应保证线路限速数据（弯道、站台、线路最高限速）正确</td></tr><tr><td style='text-align: center;'>SR-S-38</td><td style='text-align: center;'>地面设备提供商应保证线路坡度数据正确</td></tr><tr><td style='text-align: center;'>SR-S-39</td><td style='text-align: center;'>地面设备提供商应保证道岔限速数据正确</td></tr><tr><td style='text-align: center;'>SR-S-40</td><td style='text-align: center;'>车载设备提供方应保证列车构造速度数据正确</td></tr><tr><td style='text-align: center;'>SR-S-41</td><td style='text-align: center;'>地面设备提供商应保证线路道岔位置数据正确</td></tr><tr><td style='text-align: center;'>SR-S-42</td><td style='text-align: center;'>地面设备提供商应保证列车在各站台开关站台门信息数据正确</td></tr><tr><td style='text-align: center;'>SR-S-43</td><td style='text-align: center;'>地面设备提供商应保证线路紧急关闭按钮信息正确</td></tr><tr><td style='text-align: center;'>SR-S-48</td><td style='text-align: center;'>ITC车载ATP计算MA终点时，应回撤安全防护距离</td></tr><tr><td style='text-align: center;'>SR-S-93</td><td style='text-align: center;'>地面设备提供商应保证线路站台对应的站台门ID、开门侧数据正确</td></tr></table>

---

#### 7.1.5 应答器系统

应答器系统安全要求的内容见表12。

<div style="text-align: center;">表 12 应答器系统安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-47</td><td style='text-align: center;'>统一互联互通应答器报文格式，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-S-48</td><td style='text-align: center;'>ITC车载ATP计算MA终点时，应回撤安全防护距离</td></tr><tr><td style='text-align: center;'>SR-S-49</td><td style='text-align: center;'>地面设备提供商应保证主应答器报文数据的正确性</td></tr><tr><td style='text-align: center;'>SR-S-50</td><td style='text-align: center;'>主应答器报文应包含道岔状态信息</td></tr><tr><td style='text-align: center;'>SR-S-51</td><td style='text-align: center;'>主应答器报文应包含联锁与LEU通信状态信息</td></tr><tr><td style='text-align: center;'>SR-S-52</td><td style='text-align: center;'>主应答器报文应包含LEU与应答器通信状态信息</td></tr><tr><td style='text-align: center;'>SR-S-53</td><td style='text-align: center;'>如应答器实际位置与电子地图位置偏差超出安全距离，车辆ATP系统应能判断出，并导向安全侧处理</td></tr><tr><td style='text-align: center;'>SR-S-54</td><td style='text-align: center;'>他线列车应丢弃本线应答器报文自定义包</td></tr><tr><td style='text-align: center;'>SR-S-55</td><td style='text-align: center;'>在应答器开窗范围内，未能完成本轮通信，应判定应答器丢失</td></tr><tr><td style='text-align: center;'>SR-S-73</td><td style='text-align: center;'>车地应答器通信应满足欧标要求</td></tr></table>

#### 7.1.6 其他

其他安全要求的内容见表13。

<div style="text-align: center;">表 13 其他安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-15</td><td style='text-align: center;'>信号系统硬件设备运用海拔高度应满足互联互通项目海拔高度要求</td></tr><tr><td style='text-align: center;'>SR-S-75</td><td style='text-align: center;'>信号系统应保证CBTC列车在防淹门进路停稳，方可允许关闭防淹门</td></tr><tr><td style='text-align: center;'>SR-S-98</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用易燃材料</td></tr><tr><td style='text-align: center;'>SR-S-99</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用有毒物质</td></tr></table>

---

<div style="text-align: center;">表 13 其他安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-S-100</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用易爆材料</td></tr><tr><td style='text-align: center;'>SR-S-101</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能含有辐射物质</td></tr><tr><td style='text-align: center;'>SR-S-102</td><td style='text-align: center;'>信号系统设备应通过应用环境EMC测试</td></tr><tr><td style='text-align: center;'>SR-S-103</td><td style='text-align: center;'>信号设备硬件设计应满足故障导向安全原则</td></tr><tr><td style='text-align: center;'>SR-S-104</td><td style='text-align: center;'>信号系统设备应通过应用环境防雷测试</td></tr><tr><td style='text-align: center;'>SR-S-105</td><td style='text-align: center;'>信号系统有线网络在物理上与其他网络完全隔离</td></tr><tr><td style='text-align: center;'>SR-S-106</td><td style='text-align: center;'>信号系统各安全关键设备间网络通信需采用安全通信协议</td></tr><tr><td style='text-align: center;'>SR-S-107</td><td style='text-align: center;'>信号系统无线通信网络采用专有频段</td></tr><tr><td style='text-align: center;'>SR-S-108</td><td style='text-align: center;'>信号系统硬件设备应满足应用环境的气候条件</td></tr><tr><td style='text-align: center;'>SR-S-109</td><td style='text-align: center;'>信号系统硬件设备抗振性能满足其运用环境振动要求</td></tr></table>

### 7.2 互联互通接口需求

通过对危害进行分析，互联互通信号系统接口危害安全要求见表14。

<div style="text-align: center;">表 14 互联互通接口安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-I-1</td><td style='text-align: center;'>CBTC级别下，车载ATP系统计算EBI时正确使用临时限速</td></tr><tr><td style='text-align: center;'>SR-I-2</td><td style='text-align: center;'>V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议</td></tr><tr><td style='text-align: center;'>SR-I-3</td><td style='text-align: center;'>列车交接过程中，ZC-ZC通信中断时，车载ATP应保证列车在当前ZC分界点停车或紧急停车</td></tr><tr><td style='text-align: center;'>SR-I-4</td><td style='text-align: center;'>互联互通联络线ZC交接时，应保证列车不丢失</td></tr><tr><td style='text-align: center;'>SR-I-5</td><td style='text-align: center;'>互联互通ZC-ZC接口协议应采用RSSP-Ⅰ铁路信号安全通信协议</td></tr><tr><td style='text-align: center;'>SR-I-6</td><td style='text-align: center;'>统一互联互通ZC-ZC接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-I-7</td><td style='text-align: center;'>互联互通CI-CI接口协议应采用RSSP-Ⅰ安全协议</td></tr><tr><td style='text-align: center;'>SR-I-8</td><td style='text-align: center;'>统一互联互通CI-CI接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-I-9</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术传输车辆实施紧急制动命令及采集紧急制动状态信息</td></tr></table>

---

<div style="text-align: center;">表 14 互联互通接口安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-I-10</td><td style='text-align: center;'>统一互联互通 ZC-V0BC 接口，保证接口数据全面、正确</td></tr><tr><td style='text-align: center;'>SR-I-11</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车前后端安全包络信息</td></tr><tr><td style='text-align: center;'>SR-I-12</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车当前速度及速度方向</td></tr><tr><td style='text-align: center;'>SR-I-13</td><td style='text-align: center;'>CI 采用安全继电器或其他安全接口技术采集站台门状态信息</td></tr><tr><td style='text-align: center;'>SR-I-14</td><td style='text-align: center;'>ZC-V0BC 接口信息包含道岔状态信息</td></tr><tr><td style='text-align: center;'>SR-I-15</td><td style='text-align: center;'>ZC-V0BC 接口信息包含站台门状态信息</td></tr><tr><td style='text-align: center;'>SR-I-16</td><td style='text-align: center;'>ZC-V0BC 接口信息包含紧急关闭按钮状态信息</td></tr><tr><td style='text-align: center;'>SR-I-17</td><td style='text-align: center;'>ZC-V0BC 接口信息包含临时限速信息</td></tr><tr><td style='text-align: center;'>SR-I-18</td><td style='text-align: center;'>V0BC-ZC 通信中断判断时间应统一，并满足本团体标准要求</td></tr><tr><td style='text-align: center;'>SR-I-19</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车退行距离</td></tr><tr><td style='text-align: center;'>SR-I-20</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车后溜距离</td></tr><tr><td style='text-align: center;'>SR-I-21</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车停准停稳信息</td></tr><tr><td style='text-align: center;'>SR-I-22</td><td style='text-align: center;'>V0BC-ZC 接口信息包含列车列车控制级别、驾驶模式</td></tr><tr><td style='text-align: center;'>SR-I-23</td><td style='text-align: center;'>V0BC-CI 接口信息应包含保护区段允许解锁信息</td></tr><tr><td style='text-align: center;'>SR-I-24</td><td style='text-align: center;'>V0BC 和 CI 间通信采用 RSSP-Ⅱ标准安全通信协议</td></tr><tr><td style='text-align: center;'>SR-I-25</td><td style='text-align: center;'>ZC-V0BC 接口信息包含紧急制动命令信息</td></tr><tr><td style='text-align: center;'>SR-I-26</td><td style='text-align: center;'>车载 ATP 采用安全继电器或其他安全接口技术采集列车完整性信息</td></tr><tr><td style='text-align: center;'>SR-I-27</td><td style='text-align: center;'>联锁系统与防淹门接口采用安全继电器或其他安全接口技术</td></tr><tr><td style='text-align: center;'>SR-I-28</td><td style='text-align: center;'>联锁系统除非采集到防淹门完全开启且锁定状态，否则防淹门所在进路不允许开放</td></tr><tr><td style='text-align: center;'>SR-I-29</td><td style='text-align: center;'>防淹门关闭前，应向联锁系统发送请求关闭命令，联锁系统确定对应区间无列车占用或即将占用，方可允许关闭防淹门</td></tr><tr><td style='text-align: center;'>SR-I-30</td><td style='text-align: center;'>规范互联互通 V0BC-CI 接口开关门命令有效时效，超时命令无效</td></tr><tr><td style='text-align: center;'>SR-I-31</td><td style='text-align: center;'>车载 ATP 系统应保证发送的 PSD 的数量、开关门侧、开门码正确，保证车门与站台门联动的一致性</td></tr></table>

---

<div style="text-align: center;">表 14 互联互通接口安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-I-32</td><td style='text-align: center;'>V0BC-CI接口信息应包含开关站台门码信息</td></tr><tr><td style='text-align: center;'>SR-I-33</td><td style='text-align: center;'>V0BC-CI接口信息应包含开关站台门控制信息</td></tr><tr><td style='text-align: center;'>SR-I-34</td><td style='text-align: center;'>V0BC-CI接口信息应包含列车编组信息，联锁保证站台门开关数量与车门一致</td></tr><tr><td style='text-align: center;'>SR-I-35</td><td style='text-align: center;'>本线ZC系统应丢弃他线列车V0BC-ZC的自定义包</td></tr><tr><td style='text-align: center;'>SR-I-36</td><td style='text-align: center;'>他线列车应丢弃本线ZC-V0BC的自定义包</td></tr><tr><td style='text-align: center;'>SR-I-37</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术采集列车车门锁闭及解锁状态信息</td></tr><tr><td style='text-align: center;'>SR-I-38</td><td style='text-align: center;'>车辆为车载信号设备提供封闭的安装空间，只有专业人员采用专业工具才能打开</td></tr><tr><td style='text-align: center;'>SR-I-39</td><td style='text-align: center;'>ZC子系统应能识别车载ATP系统通信中断故障，并提供防护</td></tr><tr><td style='text-align: center;'>SR-I-40</td><td style='text-align: center;'>CBTC控制级别下，临时限速应被正确设置。ZC子系统应能正确处理并正确传输给车载ATP</td></tr><tr><td style='text-align: center;'>SR-I-41</td><td style='text-align: center;'>本线CI系统应丢弃他线V0BC→CI的自定义包</td></tr><tr><td style='text-align: center;'>SR-I-42</td><td style='text-align: center;'>他线列车应丢弃本线CI→V0BC的自定义包</td></tr><tr><td style='text-align: center;'>SR-I-43</td><td style='text-align: center;'>车载ATP采用安全继电器或其他安全接口技术驱动列车车门开启及锁闭，车载ATP两侧车门的使能命令应相互独立</td></tr></table>

### 7.3 建设运营维护

通过对危害进行分析，互联互通信号建设运营维护危害安全要求见表15。

<div style="text-align: center;">表 15 互联互通建设运营维护安全要求列表</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-0-1</td><td style='text-align: center;'>营运责任方制定计轴直接复位的操作规范，运营人员必须确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作</td></tr></table>

---

<div style="text-align: center;">表 15 互联互通建设运营维护安全要求列表(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-0-2</td><td style='text-align: center;'>非CBTC级别下，临时限速信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定临时限速操作规程，确保临时限速信息及时传递到司机</td></tr><tr><td style='text-align: center;'>SR-0-3</td><td style='text-align: center;'>车辆采购及维护符合车辆专业相关规定，并满足信号系统输出的安全要求</td></tr><tr><td style='text-align: center;'>SR-0-4</td><td style='text-align: center;'>RM/EUM模式下，列车司机按照联锁信号行车</td></tr><tr><td style='text-align: center;'>SR-0-5</td><td style='text-align: center;'>统一RM/EUM模式最大退行距离及退行作业细则</td></tr><tr><td style='text-align: center;'>SR-0-6</td><td style='text-align: center;'>切除ATP列车或未装备ATP列车，司机按照联锁信号或人工调度行车，行车安全由司机保障</td></tr><tr><td style='text-align: center;'>SR-0-7</td><td style='text-align: center;'>统一EUM模式列车后溜防护细则</td></tr><tr><td style='text-align: center;'>SR-0-8</td><td style='text-align: center;'>V0BC-ZC通信判断中断过程中，由于信号系统故障或其他突发事件导致MA回撤，V0BC未能及时接收从而导致的行车风险无法通过信号系统防护</td></tr><tr><td style='text-align: center;'>SR-0-9</td><td style='text-align: center;'>解体列车的某部分已经完全与车载ATP物理隔离，无法收到ATP紧急制动的信息 该危害信号系统无法减轻或消除</td></tr><tr><td style='text-align: center;'>SR-0-10</td><td style='text-align: center;'>信号系统无法检测到解体后列车具体位置，车载ATP系统无法提供安全防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-11</td><td style='text-align: center;'>制定现场施工管理细则，列车在线路上运营时，禁止运营交路涉及的站台范围的施工或维护工作进行</td></tr><tr><td style='text-align: center;'>SR-0-12</td><td style='text-align: center;'>制定现场施工管理细则，作业责任方应完成施工材料、工具、废弃物清除，严禁遗漏在轨道上或其他形式的侵限限界</td></tr><tr><td style='text-align: center;'>SR-0-13</td><td style='text-align: center;'>动车调试或列车运营时，站台上的施工作业界面应清晰明确，做好确实可行的防护方案后方可进行交叉作业</td></tr><tr><td style='text-align: center;'>SR-0-14</td><td style='text-align: center;'>信号设备安装满足设备限界要求</td></tr><tr><td style='text-align: center;'>SR-0-15</td><td style='text-align: center;'>列车运营线路应实施全面防护</td></tr><tr><td style='text-align: center;'>SR-0-16</td><td style='text-align: center;'>每天开始正式运营前，运营责任方应组织当天所有可能涉及线路的压道作业，确认线路无障碍物，方可进入运营</td></tr></table>

---

<div style="text-align: center;">表 15 互联互通建设运营维护安全要求列表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-0-17</td><td style='text-align: center;'>运营责任方应该制定相关规则，防止列车与车辆段里的汽车、行人、其他机动车相撞</td></tr><tr><td style='text-align: center;'>SR-0-18</td><td style='text-align: center;'>运营责任方应该制定相关规则，防止列车与车辆段里掉落在平交道口区域的物体相撞</td></tr><tr><td style='text-align: center;'>SR-0-19</td><td style='text-align: center;'>运营责任方应该制定相关规则，确保不能被信号系统识别的列车上线行驶安全及安全退出线路</td></tr><tr><td style='text-align: center;'>SR-0-20</td><td style='text-align: center;'>防淹门关闭信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-21</td><td style='text-align: center;'>信号系统与防淹门无接口情况下，运营责任方应制定防淹门关闭、开启应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-22</td><td style='text-align: center;'>信号系统与人防门无接口情况下，运营责任方应制定人防门关闭、开启应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-23</td><td style='text-align: center;'>非CBTC级别下，车载ATP系统不能对站台门非安全状态进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-24</td><td style='text-align: center;'>非CBTC级别下，站台紧急关闭按钮激活信息不能通过信号系统传递到车载ATP系统进行防护，运营责任方应制定该情况下应急预案，避免或减轻事故</td></tr><tr><td style='text-align: center;'>SR-0-25</td><td style='text-align: center;'>运营责任方应制定相关规则，确保乘客上下车完毕后再关闭车门</td></tr><tr><td style='text-align: center;'>SR-0-26</td><td style='text-align: center;'>运营责任方应制定相关规则，确保乘客上下车完毕后再关闭站台门</td></tr><tr><td style='text-align: center;'>SR-0-27</td><td style='text-align: center;'>运营责任方应制定车辆段作业细则，以避免列车车辆段运营或调试过程中撞到车辆段工作人员</td></tr><tr><td style='text-align: center;'>SR-0-28</td><td style='text-align: center;'>轨道采购及维护符合轨道专业相关规定</td></tr><tr><td style='text-align: center;'>SR-0-29</td><td style='text-align: center;'>列车脱轨后，信号系统无法提供其安全防护，运营责任方应制定列车脱轨应急预案，避免或减轻事故影响</td></tr><tr><td style='text-align: center;'>SR-0-30</td><td style='text-align: center;'>站台门采购及维护符合站台门专业相关规定</td></tr><tr><td style='text-align: center;'>SR-0-31</td><td style='text-align: center;'>运营责任方制定规则，明确站台门紧急开启操作细则</td></tr><tr><td style='text-align: center;'>SR-0-32</td><td style='text-align: center;'>站台门人工开启开关应避免站台非工作人员误操作</td></tr></table>

---

<div style="text-align: center;">表 15 互联互通建设运营维护安全要求列表（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>SR-0-33</td><td style='text-align: center;'>互联互通所有站台门数量应≥列车客室</td></tr><tr><td style='text-align: center;'>SR-0-34</td><td style='text-align: center;'>运营责任方应统一列车运行过程中车门不安全打开应急处理预案，避免或减轻该场景下的事故影响</td></tr><tr><td style='text-align: center;'>SR-0-35</td><td style='text-align: center;'>运营责任方应制定切除ATP或非装备列车开关站台门操作细则</td></tr><tr><td style='text-align: center;'>SR-0-36</td><td style='text-align: center;'>运营责任方应制定互联互通列车自动折返操作细则</td></tr><tr><td style='text-align: center;'>SR-0-37</td><td style='text-align: center;'>信号系统紧急制动是为了保障列车行车安全，最大程度避免或减轻行车事故发生，由此引发客室、司机室人员跌倒事故信号系统无法提供防护</td></tr><tr><td style='text-align: center;'>SR-0-38</td><td style='text-align: center;'>车载应有广播和信息提醒乘客/司机在启动、停车和运行过程中扶好站稳</td></tr><tr><td style='text-align: center;'>SR-0-39</td><td style='text-align: center;'>维护责任方制定信号系统维护作业细则</td></tr><tr><td style='text-align: center;'>SR-0-40</td><td style='text-align: center;'>运营责任方应制定火灾应急预案</td></tr><tr><td style='text-align: center;'>SR-0-41</td><td style='text-align: center;'>运营责任方应制定爆炸应急预案</td></tr><tr><td style='text-align: center;'>SR-0-42</td><td style='text-align: center;'>运营单位确保信号系统运营环境、电磁环境正常</td></tr><tr><td style='text-align: center;'>SR-0-43</td><td style='text-align: center;'>信号系统无法检测或防护人为恶意破坏，运营责任方应制定人为恶意破坏应急预案，避免或减轻事故影响</td></tr><tr><td style='text-align: center;'>SR-0-44</td><td style='text-align: center;'>信号系统无法检测或防护洪水/地震/强风等自然灾害引发的行车事故，运营责任方应制定自然灾害应急预案，避免或减轻事故影响</td></tr><tr><td style='text-align: center;'>SR-0-45</td><td style='text-align: center;'>信号系统失效后，运营责任方应制定运营细则，保证同时存在于桥梁的列车≤桥梁允许运营载荷要求</td></tr><tr><td style='text-align: center;'>SR-0-46</td><td style='text-align: center;'>信号系统无法检测或防护基础措施沉降，运营责任方应及时检测基础措施沉降情况，并将沉降导致的临时限速变化值反馈至信号系统</td></tr><tr><td style='text-align: center;'>SR-0-47</td><td style='text-align: center;'>信号系统无法检测或防护基础设施坍塌导致的行车事故，运营责任方应运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响</td></tr><tr><td style='text-align: center;'>SR-0-48</td><td style='text-align: center;'>维护责任方针对联络线轨旁设备制定维护作业细则</td></tr><tr><td style='text-align: center;'>SR-0-49</td><td style='text-align: center;'>运营责任方制定救援与疏散作业细则</td></tr><tr><td style='text-align: center;'>SR-0-50</td><td style='text-align: center;'>运营责任方针对跨线救援与疏散制定作业细则</td></tr></table>

---

## 参考文献

[1] GB 50578—2010 城市轨道交通信号工程施工质量验收规范

[2] DB11/T 311.2—2008 城市轨道交通工程质量验收规范

[3] GB 50157—2013 地铁设计规范

[4] GB/T 12758—2004 城市轨道交通信号系统通用技术条件

[5] 铁运 2010[149] 号 铁路信号联锁试验暂行办法

[6] GB/T 22239—2008 信息安全技术 信息系统安全等级保护基本要求

[7] GB/T 28808—2012 轨道交通通信、信号和处理系统控制和防护系统软件

[8] GB/T 28809—2012 轨道交通通信、信号和处理系统信号用安全相关电子系统

[9] CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

[10] TB/T 2615—1994 铁路信号故障-安全原则

[11] TB/T 3027—2015 计算机联锁技术条件

[12] GB/T 21562—2008 轨道交通可靠性、可用性、可维护性和安全性规范及示例(IEC 62278:2002 IDT)

[13] EN 50126-2—2007 铁路行业可靠性、可用性、可维护性标准

[14] GB/T 1.1—2009 标准化工作导则 第1部分：标准的结构和编写

---

# 中国城市轨道交通协会团体标准   城市轨道交通基于通信的列车运行   控制系统（CBTC）互联互通系统规范   第4部分：互联互通危害分析   T/CAMET 04010.4—2018

中国铁道出版社有限公司出版发行  

(100054, 北京市西城区右安门西街 8 号)  

出版社网址：http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本：880 mm × 1230 mm 1/32 印张：5 字数：139 千  

2019 年 5 月第 1 版 2019 年 5 月第 1 次印刷

书号：15113·5672 定价：40.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本社发行部联系调换。发行部电话：路（021）73174，市（010）51873174