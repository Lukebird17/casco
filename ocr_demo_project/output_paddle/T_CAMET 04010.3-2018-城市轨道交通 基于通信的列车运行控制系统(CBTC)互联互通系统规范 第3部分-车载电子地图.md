# 中国城市轨道交通协会团体标准

T/CAMET 04010.3—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范 第3部分：车载电子地图

# Urban rail transit — System specification for interoperability of communication based train control system Part 3: Onboard electronic map

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
3.2 缩略语 …… 4    
4 总体描述 …… 5    
4.1 总体要求 …… 5    
4.2 基本定义 …… 6    
5 电子地图元素数据结构 …… 9    
5.1 说明 …… 9    
5.2 线路 …… 9    
5.3 轨道区段 …… 14    
5.4 折返区域 …… 50    
5.5 应答器 …… 55    
5.6 信号机 …… 55    
5.7 车挡 …… 60    
5.8 区域控制器（ZC） …… 60    
5.9 计算机联锁（CI） …… 64    
5.10 列车自动监控（ATS） …… 64    
5.11 维护支持子系统（MSS） …… 64

---

5.12 数据服务单元(DSU) …… 64  
5.13 安全通信协议栈 …… 64  
6 电子地图二进制文件整体数据结构 …… 78  
附录 A（规范性附录） 线路关键元素取值范围 …… 80

---

## 前言

T/CAMET 04010《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》分为以下四个部分：

——第1部分：系统总体要求；

——第2部分：系统架构和功能分配；

——第3部分：车载电子地图；

——第4部分：互联互通危害分析。

本部分是 T/CAMET 04010 的第 3 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：北京全路通信信号研究设计院集团有限公司、交控科技股份有限公司、中国铁道科学研究院集团有限公司通信信号研究所、株洲中车时代电气股份有限公司、浙江众合科技股份有限公司、北京交通大学。

本部分主要起草人：编写组：刘鲁鹏、王佳、李紫时、杨旭文、张春雨、孙旺、姜庆阳、任颖、田昌宇、刘爱军、胡顺定、黄友能、王悉、刘键。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车 运行控制系统(CBTC)互联互通系统规范 第3部分:车载电子地图

## 1 范围

T/CAMET 04010 的本部分规定了满足互联互通的统一的车载电子地图的数据格式，为数据编制、管理、测试提供依据，为数据编制提供统一的车载电子地图数据输入及导出格式。本规范对电子地图数据的管理、升级及数据校验不进行约束。设备 ID 编码规则等本规范未规定的内容应在后续规范或工程实施中完成。

本部分适用于国内采用基于通信的列车运行控制系统（CBTC）的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

## 轨道

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

运基信号 $$ 2010 $$ 267号 RSSP-Ⅱ铁路信号安全通信协议

## 3 术语和缩略语

GB 50157—2013、CJ/T 407—2012 和 T/CAMET 04010.1 界定的以及

---

下列术语和缩略语适用于本部分：为了便于使用，以下重复列出了其中的主要相关术语。

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

列车自动控制 automatic train control

信号系统自动实现列车监控、安全防护和运行控制等技术的总称。

[GB 50157—2013, 定义 2.0.37]

#### 3.1.4 

## 列车自动监控 automatic train supervision

根据列车时刻表为列车运行自动设定进路、指挥行车、实施列车运行管理等技术的总称。

[GB 50157—2013, 定义 2.0.38]

#### 3.1.5 

列车自动防护 automatic train protection

自动实现列车运行间隔、超速防护、进路安全和车门等监控技术的总称。

[GB 50157—2013, 定义 2.0.39]

#### 3.1.6 

列车自动运行 automatic train operation

自动实现列车加速、调速、停车和车门开闭、提示等控制技术的总称。

---

[GB 50157—2013, 定义 2.0.40]

#### 3.1.7 

## 计算机联锁 computer interlocking

以计算机技术为核心，自动实现进路、道岔、信号机等防护技术的总称。

[CJ/T 407—2012, 定义 3.1.6]

#### 3.1.8 

## 维护支持系统 maintenance support system

监测记录系统内其他各子系统维护信息，辅助系统故障分析，用于系统日常运营维护。

[T/CAMET 04010.1,术语3.1.8]

#### 3.1.9 

## 危险点 danger point

列车运行前方不允许列车任何部位越过的特定点。

[T/CAMET 04010.1,术语3.1.10]

#### 3.1.10 

## 移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

#### [CJ/T 407—2012, 定义 3.1.7]

#### 3.1.11 

## 装备列车 CBTC-equipped trains

装备了 CBTC 系统车载设备且设备处于工作状态的列车。

[T/CAMET 04010.1,术语3.1.11]

#### 3.1.12 

## 非装备列车 Non-CBTC-equipped trains

没有装备 CBTC 系统车载设备或者 CBTC 系统车载设备处于不工作状态的列车。

[T/CAMET 04010.1,术语3.1.12]

---

#### 3.1.13 

## 转换轨 transfer track

指车辆段/停车场与正线的连接轨，运营列车在驶入/驶出转换轨过程中，当条件具备时，进行列车运行控制级别及驾驶模式转换。

[T/CAMET 04010.1,术语3.1.13]

#### 3.1.14 

## 跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，山一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 04010.1,术语3.1.14]

#### 3.1.15 

## 互联互通 interoperability

装备不同信号厂家车载设备的列车可以在装备不同信号厂家轨旁设备的一条轨道交通线路内或多条轨道交通线路上无缝互通、安全可靠运营。

##### [T/CAMET 04010.1,术语3.1.16]

#### 3.1.16 

## 轨道区段 track section

轨道区段作为线路拓扑的基本构成单元，按照线路元素特征进行区段划分，划分原则不依赖于线路物理分界点，用于描述线路基本信息。

#### 3.1.17 

## 道岔区段 switch section

道岔区段为属性为道岔的轨道区段，描述了线路拓扑中道岔区域的线路数据信息。

### 3.2 缩略语

AM: 列车自动驾驶模式 (Automatic Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO: 列车自动运行(Automatic Train Operation)

ATP: 列车自动防护(Automatic Train Protection)

ATS: 列车自动监控 (Automatic Train Supervision)

---

CBTC:基于通信的列车控制(Communication Based Train Control)

CI: 计算机联锁 (Computer Interlocking)

CM:列车自动防护模式(Coded Train Operating Mode)

DCS: 数据通信系统 (Data Communication System)

EUM: 非限制人工驾驶模式 (Emergency Unrestricted Train Operating Mode)

MA:移动授权(Movement Authority)

MSS:维护支持系统(Maintenance Support System)

PIS:乘客信息系统(Passenger Information System)

PSD:站台门(Platform Screen Door)

RM:限制人工驾驶模式(Restricted Train Operating Mode)

TSR: 临时限速(Temporary Speed Restriction)

TMS:列车管理系统(Train Management System)

V0BC:车载控制器(Vehicle On-Board Controller)

ZC: 区域控制器 (Zone Controller)

## 4 总体描述

### 4.1 总体要求

4.1.1 CBTC 系统中, VOBC 应通过车载本地存储数据的方式获取线路信息。车载本地存储的数据称为车载电子地图(以下简称电子地图)。

4.1.2 电子地图数据可分为以下几类：

a）线路数据：与运行线路相关的数据；

b）轨道区段数据：线路轨道区段元素数据；

c) 轨旁设备数据: 应答器、信号机、车挡、ZC、ATS、CI、DSU、MSS 等数据;

d） 安全通信协议数据。

4.1.3 若地图中不存在某类数据，则该数据对应的整个表在电子地图中不存在。例如，若某线路中没有 DSU 设备，则该线路电子地图中应不存在 DSU 数据表。

---

4.1.4 电子地图以二进制文件方式描述。对多字节字段，字节序均为高字节在前（大端编码方式）。

4.1.5 电子地图数据结构中的变量名定义的前缀定义见表1.

<div style="text-align: center;">表 1 车载电子地图变量名前缀定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>前  级</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>D_</td><td style='text-align: center;'>距离</td></tr><tr><td style='text-align: center;'>G_</td><td style='text-align: center;'>坡度/弧度</td></tr><tr><td style='text-align: center;'>L_</td><td style='text-align: center;'>长度</td></tr><tr><td style='text-align: center;'>M_</td><td style='text-align: center;'>其他</td></tr><tr><td style='text-align: center;'>N_</td><td style='text-align: center;'>编号/数量</td></tr><tr><td style='text-align: center;'>NID_</td><td style='text-align: center;'>识别号</td></tr><tr><td style='text-align: center;'>Q_</td><td style='text-align: center;'>限定</td></tr><tr><td style='text-align: center;'>V_</td><td style='text-align: center;'>速度</td></tr><tr><td style='text-align: center;'>NC_</td><td style='text-align: center;'>等级编号</td></tr></table>

电子地图数据结构中的变量名是唯一的，每一个变量只有一种含义，具有相同含义的变量具有相同的变量名。

### 4.2 基本定义

#### 4.2.1 轨道区段及划分原则

线路拓扑以轨道区段及轨道区段间的链接关系描述。

道岔区段内轨道区段划分示例如图1和图2所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//dbc24b24-6406-474c-b26e-1c5483c03779/markdown_0/imgs/img_in_image_box_258_835_624_1000.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A00Z%2F-1%2F%2Ff496d992128f2ea1b53647a150edf00e3fb3a76724e379a686e3e2a39fe66c91" alt="Image" width="43%" /></div>


说明：

除物理区段边界点1、2、3外，岔尖A位置也应作为轨道区段边界，故此区域内轨道区段应划分为1A、A3、A2三段。

<div style="text-align: center;">图 1 单个道岔轨道区段划分</div>

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6985c419-7e58-4179-a5a0-f34441cb3b2b/markdown_0/imgs/img_in_image_box_226_125_619_334.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A03Z%2F-1%2F%2F505d93daf5e1bdbbcf2323111d434017fdc5cdffd1e6ca51e886974eb14e1321" alt="Image" width="46%" /></div>


说明：

除物理区段边界点1、2、3、4外，岔尖A、B位置也应作为轨道区段边界，C点为根据厂商需要，在A、B间增设的轨道区段边界点 $ ^{[注]} $ 。故此区域内，轨道区段应划分为1A、2A、AC、CB、B3、B4六段。

注：C点是否存在，可由线路所属厂商自行定义。

<div style="text-align: center;">图 2 物理区段内有多个道岔时的轨道区段划分</div>


#### 4.2.2 电子地图方向

电子地图方向以上下行描述。其中，上行方向定义为：信号平面图的从左到右方向，下行方向定义为：信号平面图的从右到左方向，如图3所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6985c419-7e58-4179-a5a0-f34441cb3b2b/markdown_0/imgs/img_in_image_box_85_669_784_968.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A03Z%2F-1%2F%2Fec6a9cc6be1a8e6d28a6085d16fad55674bd2b589dd3985c4dbf5fa5f2c8d368" alt="Image" width="82%" /></div>


图中为电子地图对应的信号平面图，则电子地图上行方向定义即为图中从左至右的方向。

<div style="text-align: center;">图 3 电子地图方向示意</div>

---

#### 4.2.3 坐标点位置

电子地图中描述坐标点位置统一以“所在轨道区段+偏移量”方式描述。其中，偏移量为沿电子地图上行方向，从所在轨道区段起点到坐标点的距离，即从轨道区段左端到坐标点距离。

#### 4.2.4 CRC 校验

车载电子地图数据中，对32位的CRC校验，对应多项式采用0x4C11DB7 $ \left(X^{32}+X^{26}+X^{23}+X^{22}+X^{16}+X^{12}+X^{11}+X^{10}+X^{8}+X^{7}+X^{5}+X^{4}+X^{2}+X+1\right) $ ，初始值为0xFFFFFFFF。对16位的CRC校验，对应多项式为0x11021 $ \left(X^{16}+X^{12}+X^{5}+1\right) $ ，初始值为0x0。

#### 4.2.5 道岔区域定义

为便于描述，对道岔区域进行定义。

将道岔区域分为岔前区域、岔后定位区域、岔后反位区域进行描述，如图4所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9c6a9dcf-49d9-426b-9334-44cd6f12ac48/markdown_0/imgs/img_in_image_box_246_570_631_719.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A08Z%2F-1%2F%2Fb237e016c80b9955ba8729dff27db975a94f0b0a8afe505eda44e15864e54961" alt="Image" width="45%" /></div>


说明：

对道岔 D1,1—A 为道岔的岔前区域；A—2 为道岔的岔后定位区域；A—3 为道岔的岔后反位区域。

<div style="text-align: center;">图 4 道岔区域定义（单个道岔）</div>


推广到物理区段内有多个道岔的情况，如图5所示。

#### 4.2.6 顺向/对向道岔

从某指定点按照某方向沿某路径搜索到道岔，若该方向与从该道岔的岔前区域到岔后区域的方向相同，则该道岔为对向道岔；若该方向与从该道岔的岔后区域到岔前区域的方向相同，则该道岔为顺向道岔。

以图 5 为例, 从计轴边界点 1 开始, 按照电子地图上行方向, 沿轨道区段 14 搜索道岔, 则 D1、D4 为对向道岔, D2、D3 为顺向道岔。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//eb086ef5-d90c-4b19-ae6e-95abdc2113a0/markdown_0/imgs/img_in_image_box_102_150_744_366.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A11Z%2F-1%2F%2Fd9ac58fe81ebb1efa514b882527eb01dafe2dae850e906ad2815ec87546a7038" alt="Image" width="76%" /></div>


说明：

对道岔 D1、1—A 为道岔的岔前区域；A—B 为道岔的岔后定位区域；A—2 为道岔的岔后反位区域。

对道岔 D2, B—C 为道岔的岔前区域；A—B 为道岔的岔后定位区域；6—B 为道岔的岔后反位区域。

对道岔 D3、C—D 为道岔的岔前区域；B—C 为道岔的岔后定位区域；3—C 为道岔的岔后反位区域。

对道岔 D4、C-D 为道岔的岔前区域；D-4 为道岔的岔后定位区域；D-5 为道岔的岔后反位区域。

注：对不同道岔，区域可能有重叠，例如图5中，B—C既为道岔D2的岔前区域，又为道岔D3的岔后定位区域

<div style="text-align: center;">图 5 道岔区域定义（物理区段内有多个道岔）</div>


## 5 电子地图元素数据结构

### 5.1 说明

各电子地图元素数据结构中，单个元素字段的数据长度均为定值。涉及字段内存在多个元素的情况，若无特殊说明，则若个数不足，则数量不足的字段中填写全0。

### 5.2 线路

#### 5.2.1 线路数据结构

线路数据结构见表2。

---

<div style="text-align: center;">表 2 线路数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>线路数据整体结构</td><td style='text-align: center;'>M_STRUCT_LINE</td><td style='text-align: center;'>N</td><td style='text-align: center;'></td><td style='text-align: center;'>线路数据整体的数据结构定义。N代表序号1~22字段的数据长度总和</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路在线网内的唯一编号。具体编号工程阶段约定</td></tr><tr><td rowspan="3">2</td><td rowspan="3">本线路地图版本</td><td rowspan="3">M_VERSION</td><td style='text-align: center;'>1</td><td style='text-align: center;'>X:0~0xFF</td><td rowspan="3">按照VX.Y.Z编制地图版本号,具体X、Y、Z编号规则在工程阶段约定</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>Y:0~0xFF</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>Z:0~0xFFFF</td></tr><tr><td rowspan="6">3</td><td rowspan="6">可转线路编号列表</td><td rowspan="6">NID_LT</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路1</td><td style='text-align: center;'>本线路可连接到的线路1的编号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路2</td><td style='text-align: center;'>本线路可连接到的线路2的编号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路3</td><td style='text-align: center;'>本线路可连接到的线路3的编号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路4</td><td style='text-align: center;'>本线路可连接到的线路4的编号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路5</td><td style='text-align: center;'>本线路可连接到的线路5的编号</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无可连接的线路6</td><td style='text-align: center;'>本线路可连接到的线路6的编号</td></tr></table>

---

<div style="text-align: center;">表 2 线路数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>线路最高允许速度</td><td style='text-align: center;'>V_LMTmax</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路最大的允许速度,单位:km/h,ATP应限制列车运行时不可突破此速度值</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>本线最高运营控制模式</td><td style='text-align: center;'>M_SYSMODE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>CBTC:0x01ITC:0x02ILC:0x03其他无效</td><td style='text-align: center;'>本线允许的最高运营控制模式</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>停准窗口大小</td><td style='text-align: center;'>M_ACCWin</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>停准窗的大小,单位:cm.V0BC判断列车停准时使用.参见5.2.2</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>站台ATP允许开门窗口大小</td><td style='text-align: center;'>M_ATP_ALWDoor</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>ATP允许开门窗口的大小,单位:cm.ATP判断输出列车开门允许时使用.参见5.2.2</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>站台ATO允许开门窗口大小</td><td style='text-align: center;'>M_ATO_ALWDoor</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>ATO允许开门窗口大小,单位:cm.ATO判断是否可开门时使用.参见5.2.2</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>退行允许距离</td><td style='text-align: center;'>D_REVERSE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~65 534,其他值无效</td><td style='text-align: center;'>ATP允许列车退行的最大距离,单位:cm.ATP判断允许列车退行时,不触发紧急制动的最大距离</td></tr></table>

---

<div style="text-align: center;">表 2 线路数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>退行允许速度</td><td style='text-align: center;'>V_REVERSE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>ATP允许列车退行的最大速度,单位:km/h.ATP判断允许列车退行时,不触发紧急制动的最大速度</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>全线轨道区段数量</td><td style='text-align: center;'>N_TRACK</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~0xFFFF,0无效</td><td style='text-align: center;'>本线路内轨道区段的总数</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>全线折返区域数量</td><td style='text-align: center;'>N_AR_AREA</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0~0xFFFF</td><td style='text-align: center;'>本线路内折返区域的总数</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>全线应答器数量</td><td style='text-align: center;'>N_BALISE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~0xFFFF,0无效</td><td style='text-align: center;'>本线路内应答器的总个数。参见5.2.3</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>全线信号机数量</td><td style='text-align: center;'>N_SIGNAL</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~0xFFFF,0无效</td><td style='text-align: center;'>本线路内信号机的总个数。参见5.2.3</td></tr><tr><td style='text-align: center;'>15</td><td style='text-align: center;'>全线车挡数量</td><td style='text-align: center;'>N_SHELTER</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF</td><td style='text-align: center;'>本线路内车挡的总个数</td></tr><tr><td style='text-align: center;'>16</td><td style='text-align: center;'>全线ZC数量</td><td style='text-align: center;'>N_ZC</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF</td><td style='text-align: center;'>本线路内ZC的总个数</td></tr><tr><td style='text-align: center;'>17</td><td style='text-align: center;'>全线CI数量</td><td style='text-align: center;'>N_CI</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF</td><td style='text-align: center;'>本线路内CI的总个数</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>全线ATS数量</td><td style='text-align: center;'>N_ATS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF</td><td style='text-align: center;'>本线路内ATS的总个数</td></tr><tr><td style='text-align: center;'>19</td><td style='text-align: center;'>全线MSS数量</td><td style='text-align: center;'>N_MSS</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF</td><td style='text-align: center;'>本线路内MSS的总个数</td></tr></table>

---

<div style="text-align: center;">表 2 线路数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度（字节）</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>20</td><td style='text-align: center;'>全线 DSU 数量</td><td style='text-align: center;'>N_DSU</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0 ~ 0xFF</td><td style='text-align: center;'>本线路内 DSU 的总个数</td></tr><tr><td style='text-align: center;'>21</td><td style='text-align: center;'>全线 RSSP - Ⅱ 地面设备种类数量</td><td style='text-align: center;'>N_Type</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0 ~ 7</td><td style='text-align: center;'>全线采用 RSSP - Ⅱ 安全通信协议与 VOBC 通信的地面设备种类总数。参见 5.2.4</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>CRC 校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0 ~ 0xFFFFFFF</td><td style='text-align: center;'>线路数据整体 CRC</td></tr><tr><td colspan="6">注: 表中的数据元素按照表格中的数据顺序存放, 后续进行数据实体定义时需严格遵循表格中的数据顺序。后文各数据表也应遵循此原则。</td></tr></table>

---

#### 5.2.2 窗口大小

此处窗口均指针对轨道区段停车点(参见5.3.10)所开的窗口。

窗口大小指停车点到对应窗边界的距离，示意如图6所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//3bce98a1-6238-42d9-a702-01f6ec47100b/markdown_0/imgs/img_in_image_box_196_245_704_367.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A39%3A33Z%2F-1%2F%2F379d829d0d8255f00ed1bc4a1bc1cc1714d53108445ba730b925f4a8f2c9a780" alt="Image" width="60%" /></div>


<div style="text-align: center;">图 6 窗口大小示意图</div>


#### 5.2.3 N_BALISE/N_SIGNAL(全线应答器/信号机数量)

本线路内应答器/信号机的总数。

此处的“本线路内应答器/信号机”指物理位置位于本线路内的应答器/信号机。例如跨线边界离去处信号机及其对应的主应答器/预告应答器，由相邻线路地面设备管理，但物理位置位于本线路内，故对本线路计算本字段时也应包含在内。而对相邻线路，计算时则应不包含该信号机/应答器。

#### 5.2.4 N Type(全线 RSSP - II 地面设备种类数量)

全线采用 RSSP - Ⅱ 安全通信协议与 VOBC 通信的地面设备种类总数。

目前 CBTC 系统中规定，ZC、CI、ATS、DSU 与 VOBC 通信时采用 RSSP-Ⅱ安全通信协议，满足运基信号 $$ 2010 $$ 267 号《RSSP-Ⅱ铁路信号安全通信协议》标准要求。N_Type 取值为线路中包含上述设备的种类总数。例如，若线路内有 ZC、CI、ATS，无 DSU，则 N_Type 取值为 3；若线路内有 ZC、CI、ATS、DSU，则 N_Type 取值为 4。

### 5.3 轨道区段

#### 5.3.1 轨道区段数据结构

轨道区段数据结构构成见表3。

---

<div style="text-align: center;">表 3 轨道区段数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>轨道区段
数据整体结构</td><td style='text-align: center;'>M_STRUCT_
TRACK</td><td style='text-align: center;'>N_
TRACK*
N+4</td><td style='text-align: center;'></td><td style='text-align: center;'>轨道区段数据整体的数据结构定义:
轨道区段数据整体结构由N_TRACK个
长度为N的轨道区段数据构成(N表示序
号1~29的数据长度总和),并增加4字节
的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>轨道区段编号</td><td style='text-align: center;'>NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0
无效</td><td style='text-align: center;'>轨道区段在线网内的唯一编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>所属线路编号值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>所属
ZC编号</td><td style='text-align: center;'>NID_
ZCaffiliation</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0
表示无所属ZC</td><td style='text-align: center;'>所属管辖范围的ZC编号</td></tr><tr><td rowspan="4">4</td><td rowspan="4">所属接管
ZC编号列表
(参见5.3.2)</td><td rowspan="4">NID_ZCadapter</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0
表示无所属接管ZC1</td><td style='text-align: center;'>所属接管ZC1编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0
表示无所属接管ZC2</td><td style='text-align: center;'>所属接管ZC2编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0
表示无所属接管ZC3</td><td style='text-align: center;'>所属接管ZC3编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0
表示无所属接管ZC4</td><td style='text-align: center;'>所属接管ZC4编号</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">5</td><td rowspan="4">接管ZC连接方向列表</td><td rowspan="4">Q_ZCaffDir</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0:无所属接管ZC1其他无效</td><td style='text-align: center;'>所属接管ZC1的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0:无所属接管ZC2其他无效</td><td style='text-align: center;'>所属接管ZC2的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0:无所属接管ZC3其他无效</td><td style='text-align: center;'>所属接管ZC3的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0:无所属接管ZC4其他无效</td><td style='text-align: center;'>所属接管ZC4的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>所属CI编号</td><td style='text-align: center;'>NID_CI</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属CI</td><td style='text-align: center;'>所属管辖范围的CI编号</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>所属ATS编号</td><td style='text-align: center;'>NID_ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属ATS</td><td style='text-align: center;'>所属管辖范围的ATS编号</td></tr><tr><td rowspan="4">8</td><td rowspan="4">所属接管ATS编号(参见5.3.2)</td><td rowspan="4">NID_ATSadapter</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属接管ATS1</td><td style='text-align: center;'>所属接管ATS1编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属接管ATS2</td><td style='text-align: center;'>所属接管ATS2编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属接管ATS3</td><td style='text-align: center;'>所属接管ATS3编号</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无所属接管ATS4</td><td style='text-align: center;'>所属接管ATS4编号</td></tr><tr><td rowspan="2">9</td><td rowspan="2">接管ATS连接方向列表</td><td rowspan="2">Q_ATSaffDir</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0表示无所属接管ATS1其他无效</td><td style='text-align: center;'>所属接管ATS1的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0表示无所属接管ATS2其他无效</td><td style='text-align: center;'>所属接管ASTS2的连接方向。参见5.3.3</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">9</td><td rowspan="2">接管ATS连接方向列表</td><td rowspan="2">Q_ATSuffDir</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0表示无所属接管ATS3其他无效</td><td style='text-align: center;'>所属接管ATS3的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行0表示无所属接管ATS4其他无效</td><td style='text-align: center;'>所属接管ATS4的连接方向。参见5.3.3</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>运营方向与轨道区段描述默认方向的对应关系</td><td style='text-align: center;'>M_DIR_REF</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:方向一致0xAA:方向相反其他无效</td><td style='text-align: center;'>方向一致:在信号平面图上,该轨道区段上,运营方向为从左到右表示上行;方向相反:在信号平面图上,该轨道区段上,运营方向为从左到右表示下行。参见5.3.4</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>轨道区段长度</td><td style='text-align: center;'>I_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>轨道区段的长度,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>轨道区段属性</td><td style='text-align: center;'>NID_TRPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x000001:普通上行轨道区段0x000002:普通下行轨道区段0x000004:上行转换轨0x000008:下行转换轨0x000010:站台0x000020:道岔0x000040:上行车挡0x000080:下行车挡0x000100:上行线路终点0x000200:下行线路终点0x000400:上行灯泡线边界0x000800:下行灯泡线边界0x040000:CI通信轨道区段0x100000:联络线(预留)参见5.3.5</td></tr><tr><td style='text-align: center;'>13</td><td style='text-align: center;'>上行方向链接轨道区段编号</td><td style='text-align: center;'>NID_TRUPLINK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无上行链接轨道区段</td><td style='text-align: center;'>上行方向上相邻链接的轨道区段编号参见5.3.6</td></tr><tr><td style='text-align: center;'>14</td><td style='text-align: center;'>下行方向链接轨道区段编号</td><td style='text-align: center;'>NID_TRDOWNLINK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无下行链接轨道区段</td><td style='text-align: center;'>下行方向上相邻链接的轨道区段编号参见5.3.6</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">15</td><td rowspan="2">链接道岔所属轨道区段编号</td><td rowspan="2">NID_SWITCHLINK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无上行链接道岔1</td><td style='text-align: center;'>上行方向链接道岔所属轨道区段编号。参见5.3.7</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无下行链接道岔1</td><td style='text-align: center;'>下行方向链接道岔所属轨道区段编号。参见5.3.7</td></tr><tr><td rowspan="2">16</td><td rowspan="2">链接道岔的ID编号</td><td rowspan="2">NID_ID_SWITCHLINK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无上行链接道岔</td><td style='text-align: center;'>上行方向链接道岔的ID编号。参见5.3.8</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无下行链接道岔</td><td style='text-align: center;'>下行方向链接道岔的ID编号。参见5.3.8</td></tr><tr><td rowspan="3">17</td><td rowspan="3">轨道区段应答器(参见5.3.9)</td><td style='text-align: center;'>N_ITERUB</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~16,其他无效</td><td style='text-align: center;'>轨道区段上的应答器数量,最大值16</td></tr><tr><td rowspan="2">NID_BALISE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无应答器1</td><td style='text-align: center;'>轨道区段上的应答器1所属线路编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0~16383,0表示无应答器1,其他无效</td><td style='text-align: center;'>轨道区段上的应答器1编号</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td rowspan="5">17</td><td rowspan="5">轨道区段
应答器
(参见5.3.9)</td><td rowspan="5">NID_BALISE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无
应答器2</td><td style='text-align: center;'>轨道区段上的应答器2所属线路编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0~16383,0表示无
应答器2,其他无效</td><td style='text-align: center;'>轨道区段上的应答器2编号</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0表示无
应答器16</td><td style='text-align: center;'>轨道区段上的应答器16所属线路编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0~16383,0表示无
应答器16,其他无效</td><td style='text-align: center;'>轨道区段上的应答器16编号</td></tr><tr><td style='text-align: center;'>18</td><td style='text-align: center;'>目的地号</td><td style='text-align: center;'>NID_TARGET</td><td style='text-align: center;'>4</td><td style='text-align: center;'>ASCⅡ码,0000表示此轨道区段无对应
目的地号</td><td style='text-align: center;'>轨道区段对应目的地号的全线统一编号,
为ASCⅡ码定义</td></tr><tr><td rowspan="2">19</td><td rowspan="2">轨道区段
停车点</td><td rowspan="2">D_STOPPINGPOINT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,
0xFFFFFFF表示无
上行方向停车点1</td><td style='text-align: center;'>上行方向停车点1偏移量,单位cm。
参见5.3.10</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,
0xFFFFFFF表示无
上行方向停车点2</td><td style='text-align: center;'>上行方向停车点2偏移量,单位cm。
参见5.3.10</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">19</td><td rowspan="2">轨道区段停车点</td><td rowspan="2">D_STOPPINGPOINT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无下行方向停车点1</td><td style='text-align: center;'>下行方向停车点1偏移量,单位cm。参见5.3.10</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无下行方向停车点2</td><td style='text-align: center;'>下行方向停车点2偏移量,单位cm。参见5.3.10</td></tr><tr><td rowspan="2">20</td><td rowspan="2">轨道区段停车点属性</td><td style='text-align: center;'>M_STOPPING_UP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x01:折返停车点0x02:运营停车点0x03:兼折返停车点及运营停车点0:无上行停车点其他无效</td><td style='text-align: center;'>上行方向轨道区段停车点属性,参见5.3.11</td></tr><tr><td style='text-align: center;'>M_STOPPING_DOWN</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x01:折返停车点0x02:运营停车点0x03:兼折返停车点及运营停车点0:无下行停车点其他无效</td><td style='text-align: center;'>下行方向轨道区段停车点属性,参见5.3.11</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">21</td><td rowspan="4" colspan="2">参考停车点</td><td rowspan="4">D_REF_STOPPOINT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无上行参考停车点1</td><td style='text-align: center;'>上行参考停车点1偏移量,单位:cm。参见5.3.12</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无上行参考停车点2</td><td style='text-align: center;'>上行参考停车点2偏移量,单位:cm。参见5.3.12</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无下行参考停车点1</td><td style='text-align: center;'>下行参考停车点1偏移量,单位:cm。参见5.3.12</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无下行参考停车点2</td><td style='text-align: center;'>下行参考停车点2偏移量,单位:cm。参见5.3.12</td></tr><tr><td rowspan="3">22</td><td rowspan="3">站台特有属性(参见5.3.13)</td><td rowspan="2">站台ID</td><td style='text-align: center;'>NID_STOPLEFT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无左侧站台</td><td style='text-align: center;'>轨道区段左侧的站台ID</td></tr><tr><td style='text-align: center;'>NID_STOPRIGHT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无右侧站台</td><td style='text-align: center;'>轨道区段右侧的站台ID</td></tr><tr><td style='text-align: center;'>车站名称</td><td style='text-align: center;'>Q_STATIONNAME</td><td style='text-align: center;'>12</td><td style='text-align: center;'></td><td style='text-align: center;'>字符串,长度不超过6个汉字,字库编码采用GB18030字库。若不足6个汉字,以“\n”作为结束标志</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">22</td><td rowspan="4">站台特有属性(参见5.3.13)</td><td rowspan="2">默认站停时间(参见5.3.13.3)</td><td style='text-align: center;'>T_STOPREVERUP</td><td style='text-align: center;'>2</td><td style='text-align: center;'>15~1800,其他无效</td><td style='text-align: center;'>上行默认站停时间,单位:s</td></tr><tr><td style='text-align: center;'>T_STOPREVERDOWN</td><td style='text-align: center;'>2</td><td style='text-align: center;'>15~1800,其他无效</td><td style='text-align: center;'>下行默认站停时间,单位:s</td></tr><tr><td style='text-align: center;'>开门侧信息</td><td style='text-align: center;'>Q_DOORDIR</td><td style='text-align: center;'>1</td><td style='text-align: center;'>门侧信息:0x01:左门0x02:右门0x03:左右门其他非法</td><td style='text-align: center;'>站台侧车门信息。用于ATP判断是否给出该侧车门允许。参见5.3.13.4</td></tr><tr><td style='text-align: center;'>默认开门顺序(参见5.3.13.5)</td><td style='text-align: center;'>Q_DOORSEQUP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开左门,之后关左门:0x55;开右门,之后关右门:0xCC;同时开双侧门,之后同时关双侧门:0xAA;</td><td style='text-align: center;'>默认上行开关门顺序</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>站台特有属性(参见5.3.13)</td><td style='text-align: center;'>默认开门顺序(参见5.3.13.5)</td><td style='text-align: center;'>Q_DOORSEQUP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>先开左门再开右门之后同时关双侧门:0x11;先开右门再开右门之后同时关双侧门:0x22;不开车门,始终关闭双侧车门:0x88;先开左门再关左门再开右门再关右门:0x33;先开右门再关右门再开左门再关左门:0x44;默认值:0xFF。站台为双侧门时填写非默认值,单侧门时填写默认值。其他无效</td><td style='text-align: center;'>默认上行开关门顺序</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>22</td><td style='text-align: center;'>站台特有属性(参见5.3.13)</td><td style='text-align: center;'>默认开门顺序(参见5.3.13.5)</td><td style='text-align: center;'>Q_DOORSEQDOWN</td><td style='text-align: center;'>1</td><td style='text-align: center;'>开左门,之后关左门:0x55;开右门,之后关右门:0xCC;同时开双侧门,之后同时关双侧门:0xAA;先开左门再开右门之后同时关双侧门:0x11;先开右门再开左门之后同时关双侧门:0x22;不开车门,始终关闭双侧车门:0x88;先开左门再关左门再开右门再关右门:0x33;先开右门再关右门再开左门再关左门:0x44;默认值:0xFF。站台为双侧门时填写非默认值,单侧门时填写默认值。其他无效</td><td style='text-align: center;'>默认下行开关门顺序</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">22</td><td rowspan="4">站台特有属性(参见5.3.13)</td><td rowspan="2">站台门ID(参见5.3.13.4)</td><td style='text-align: center;'>NID_PSDLEFT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无左侧站台门</td><td style='text-align: center;'>左侧站台门ID</td></tr><tr><td style='text-align: center;'>NID_PSDRIGHT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无右侧站台门</td><td style='text-align: center;'>右侧站台门ID</td></tr><tr><td rowspan="2">紧急按钮ID</td><td rowspan="2">NID_EMG</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无紧急停车按钮1</td><td style='text-align: center;'>紧急停车按钮1ID</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无紧急停车按钮2</td><td style='text-align: center;'>紧急停车按钮2ID</td></tr><tr><td rowspan="5">23</td><td rowspan="5">风井(参见5.3.14)</td><td style='text-align: center;'>风井数量</td><td style='text-align: center;'>N_AIR_SHAFT</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~8,其他无效,0表示无风井</td><td style='text-align: center;'>轨道区段上风井的数量</td></tr><tr><td rowspan="4">风井偏移量</td><td rowspan="4">D_AIR_SHAFT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFF表示无风井1</td><td style='text-align: center;'>风井1相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFF表示无风井2</td><td style='text-align: center;'>风井2相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFF表示无风井8</td><td style='text-align: center;'>风井8相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="9">24</td><td rowspan="9">防淹门(参见5.3.14)</td><td style='text-align: center;'>防淹门数量</td><td style='text-align: center;'>N_FLOOD_GATE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~8,其他无效,0表示无防淹门</td><td style='text-align: center;'>轨道区段上防淹门的数量</td></tr><tr><td rowspan="4">防淹门ID</td><td rowspan="4">NID_FLOOD_GATE</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无防淹门1</td><td style='text-align: center;'>防淹门1ID</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无防淹门2</td><td style='text-align: center;'>防淹门2ID</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无防淹门8</td><td style='text-align: center;'>防淹门8ID</td></tr><tr><td rowspan="4">防淹门区域长度</td><td rowspan="4">D_AREA_FLOODG</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0~0xFFFF,0表示无防淹门1</td><td style='text-align: center;'>防淹门1的区域长度,单位:cm</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0~0xFFFF,0表示无防淹门2</td><td style='text-align: center;'>防淹门2的区域长度,单位:cm</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>0~0xFFFF,0表示无防淹门8</td><td style='text-align: center;'>防淹门8的区域长度,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="3">24</td><td rowspan="3">防淹门(参见5.3.14)</td><td rowspan="3">防淹门偏移量</td><td rowspan="3">D_FLOOD_GATE</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无防淹门1</td><td style='text-align: center;'>防淹门1相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无防淹门2</td><td style='text-align: center;'>防淹门2相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无防淹门8</td><td style='text-align: center;'>防淹门8相对于轨道区段起点的偏移量(相对于电子地图上行方向),单位:cm</td></tr><tr><td rowspan="3">25</td><td rowspan="3">分段限速(参见5.3.15)</td><td style='text-align: center;'>分段限速数量</td><td style='text-align: center;'>N_ITERLmtV</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~32,其他无效</td><td style='text-align: center;'>1~32,轨道区段上分段限速的数量,最大为32</td></tr><tr><td rowspan="2">分段限速1</td><td style='text-align: center;'>D_IMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,其他无效</td><td style='text-align: center;'>分段限速1相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_LMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,其他无效</td><td style='text-align: center;'>分段限速1的长度,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="8">25</td><td rowspan="8">分段限速(参见5.3.15)</td><td style='text-align: center;'>分段限速1</td><td style='text-align: center;'>V_LMT</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFE,其他无效</td><td style='text-align: center;'>分段限速1的限速值,单位:km/h</td></tr><tr><td rowspan="3">分段限速2</td><td style='text-align: center;'>D_LMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无分段限速2</td><td style='text-align: center;'>分段限速2相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_LMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无分段限速2</td><td style='text-align: center;'>分段限速2的长度,单位:cm</td></tr><tr><td style='text-align: center;'>V_LMT</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0xFF表示无分段限速2</td><td style='text-align: center;'>分段限速2的限速值,单位:km/h</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'></td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td rowspan="3">分段限速32</td><td style='text-align: center;'>D_LMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无分段限速32</td><td style='text-align: center;'>分段限速32相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_LMTV</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无分段限速32</td><td style='text-align: center;'>分段限速32的长度,单位:cm</td></tr><tr><td style='text-align: center;'>V_LMT</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~0xFF,0xFF表示无分段限速32</td><td style='text-align: center;'>分段限速32的限速值,单位:km/h</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="7">26</td><td rowspan="7">坡度(参见S.151)</td><td style='text-align: center;'>分段坡度数量</td><td style='text-align: center;'>N_ITERG</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~32,其他无效</td><td style='text-align: center;'>1~32,轨道区段上分段坡度的数量,最大为32</td></tr><tr><td rowspan="3">分段坡度1</td><td style='text-align: center;'>D_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,其他无效</td><td style='text-align: center;'>分段坡度1相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFFF,其他无效</td><td style='text-align: center;'>分段坡度1的长度,单位:cm</td></tr><tr><td style='text-align: center;'>G_RAMP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>-127~127,有符号数,其他无效</td><td style='text-align: center;'>分段坡度1的坡度值,单位:‰。按照电子地图上行方向上坡时该值为正值,下坡时为负值</td></tr><tr><td style='text-align: center;'>竖曲线半径1</td><td style='text-align: center;'>G_CR_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>分段坡度1坡度变化处等效的曲线半径,单位cm。参见5.3.15.2</td></tr><tr><td rowspan="2">分段坡度2</td><td style='text-align: center;'>D_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0xFFFFFFFF表示无分段坡度2</td><td style='text-align: center;'>分段坡度2相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无分段坡度2</td><td style='text-align: center;'>分段坡度2的长度,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="7">26</td><td rowspan="7">坡度(参见5.3.15)</td><td style='text-align: center;'>分段坡度2</td><td style='text-align: center;'>G_RAMP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>-128~127,有符号数,-128表示无分段坡度2</td><td style='text-align: center;'>分段坡度2的坡度值,单位:‰。按照电子地图上行方向上坡时该值为正值,下坡时为负值</td></tr><tr><td style='text-align: center;'>竖曲线半径2</td><td style='text-align: center;'>G_CR_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>分段坡度2坡度变化处等效的曲线半径,单位cm。参见5.3.15.2</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td rowspan="3">分段坡度32</td><td style='text-align: center;'>D_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0xFFFFFFFF表示无分段坡度32</td><td style='text-align: center;'>分段坡度32相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无分段坡度32</td><td style='text-align: center;'>分段坡度32的长度,单位:cm</td></tr><tr><td style='text-align: center;'>G_RAMP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>-128~127,有符号数,-128表示无分段坡度32</td><td style='text-align: center;'>分段坡度32的坡度值,单位:‰。按照电子地图上行方向上坡时该值为正值,下坡时为负值</td></tr><tr><td style='text-align: center;'>竖曲线半径32</td><td style='text-align: center;'>G_CR_RAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>分段坡度32坡度变化处等效的曲线半径,单位cm。参见5.3.15.2</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="7">27</td><td rowspan="7">曲率(参见5.3.15)</td><td style='text-align: center;'>分段曲率数量</td><td style='text-align: center;'>N_ITERCR</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~32,其他无效</td><td style='text-align: center;'>1~32,轨道区段上分段曲率的数量,最大为32</td></tr><tr><td rowspan="3">分段曲率1</td><td style='text-align: center;'>D_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,其他无效</td><td style='text-align: center;'>分段曲率1相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>I_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,其他无效</td><td style='text-align: center;'>分段曲率1的长度,单位:cm</td></tr><tr><td style='text-align: center;'>G_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0xFFFFFFF表示曲率为0</td><td style='text-align: center;'>分段曲率1的曲率半径,单位:cm。参见5.3.15.3</td></tr><tr><td rowspan="3">分段曲率2</td><td style='text-align: center;'>D_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无分段曲率2</td><td style='text-align: center;'>分段曲率2相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无分段曲率2</td><td style='text-align: center;'>分段曲率2的长度,单位:cm</td></tr><tr><td style='text-align: center;'>G_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示曲率为0,0表示无分段曲率2</td><td style='text-align: center;'>分段曲率2的曲率半径,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">27</td><td rowspan="4">曲率(参见5.3.15)</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td rowspan="3">分段曲率32</td><td style='text-align: center;'>D_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无分段曲率32</td><td style='text-align: center;'>分段曲率32相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无分段曲率32</td><td style='text-align: center;'>分段曲率32的长度,单位:cm</td></tr><tr><td style='text-align: center;'>G_CRAMP</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示曲率为0,0表示无分段曲率32</td><td style='text-align: center;'>分段曲率32的曲率半径,单位:cm</td></tr><tr><td rowspan="3">28</td><td rowspan="3">隧道信息(参见5.3.15)</td><td style='text-align: center;'>隧道信息数量</td><td style='text-align: center;'>N_TUNNEL</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~32,其他无效</td><td style='text-align: center;'>1~32,轨道区段上隧道信息的数量,最大为32</td></tr><tr><td rowspan="2">隧道信息1</td><td style='text-align: center;'>M_TUNNEL</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:是隧道0x00:非隧道其他无效</td><td style='text-align: center;'>隧道信息1是否隧道</td></tr><tr><td style='text-align: center;'>D_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,其他无效</td><td style='text-align: center;'>隧道信息1起点相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="8">28</td><td rowspan="8">隧道信息(参见5.3.15)</td><td style='text-align: center;'>隧道信息1</td><td style='text-align: center;'>L_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,其他无效</td><td style='text-align: center;'>隧道信息1的长度,单位:cm</td></tr><tr><td rowspan="4">隧道信息2</td><td style='text-align: center;'>M_TUNNEL</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:是隧道0x00:非隧道0:无隧道信息2其他无效</td><td style='text-align: center;'>隧道信息2是否隧道</td></tr><tr><td style='text-align: center;'>D_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无隧道信息2</td><td style='text-align: center;'>隧道信息2起点相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无隧道信息2</td><td style='text-align: center;'>隧道信息2的长度,单位:cm</td></tr><tr><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td></tr><tr><td rowspan="3">隧道信息32</td><td style='text-align: center;'>M_TUNNEL</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:是隧道0x00:非隧道0:无隧道信息32其他无效</td><td style='text-align: center;'>隧道信息32是否隧道</td></tr><tr><td style='text-align: center;'>D_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无隧道信息32</td><td style='text-align: center;'>隧道信息32起点相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>L_TUNNEL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无隧道信息32</td><td style='text-align: center;'>隧道信息32的长度,单位:cm</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td colspan="2">定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="5">29</td><td rowspan="5">无电区信息(参见5.3.14)</td><td style='text-align: center;'>无电区数量</td><td style='text-align: center;'>N_NEUTRAL</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0~16,其他无效</td><td style='text-align: center;'>0~16,轨道区段上无电区的数量,最大为16</td></tr><tr><td style='text-align: center;'>无电区1起点在轨道区段内偏移量</td><td style='text-align: center;'>D_NEUTRALINIT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无电区1</td><td style='text-align: center;'>描述无电区1的起点在所属轨道区段内的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>无电区1长度</td><td style='text-align: center;'>L_NEUTRAL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无无电区1</td><td style='text-align: center;'>描述无电区1起点到终点的距离,单位:cm</td></tr><tr><td style='text-align: center;'>无电区16起点在轨道区段内偏移量</td><td style='text-align: center;'>D_NEUTRALINIT</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0xFFFFFFF表示无电区16</td><td style='text-align: center;'>描述无电区16的起点在所属轨道区段内的偏移量,按照电子地图上行方向进行偏移量计算,单位:cm</td></tr><tr><td style='text-align: center;'>无电区16长度</td><td style='text-align: center;'>L_NEUTRAL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,0表示无无电区16</td><td style='text-align: center;'>描述无电区16起点到终点的距离,单位:cm</td></tr><tr><td style='text-align: center;'>30</td><td style='text-align: center;'></td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>轨道区段数据整体CRC。参见5.3.16</td></tr></table>

---

线路关键元素取值范围参见附录 A。部分字段说明详见 5.3.2～5.3.16。

#### 5.3.2 多个接管 ZC/ATS

当一个 ZC/ATS 连接多个 ZC/ATS 时，各 ZC/ATS 重叠区可能有重叠部分。故可能存在轨道区段属于多个接管 ZC/ATS 的情况，如图 7 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c8d75a36-41bd-44cc-8969-e60ff1f26453/markdown_0/imgs/img_in_image_box_145_304_710_511.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A40%3A51Z%2F-1%2F%2F9f38c9a9fa3184e51aa0b00ed30966b315b52ff5ce719dbdc1f23da6299fce2e" alt="Image" width="67%" /></div>


说明：

ZC1 连接 ZC2、ZC3，红线部分为 ZC1 与 ZC2 的重叠区在 ZC1 内的部分，绿线部分为 ZC1 与 ZC3 的重叠区在 ZC1 内的部分。轨道区段 1 既属于 ZC1 与 ZC2 的重叠区，又属于 ZC1 与 ZC3 的重叠区，故 ZC2、ZC3 同为轨道区段 1 的接管 ZC。

## 图7 多个接管ZC示意图

#### 5.3.3 Q_ZcaffDir/Q_ATSaffDir（接管 ZC/ATS 连接方向列表）

接管 ZC/ATS 的连接方向，以上下行描述。确定原则为：若轨道区段属于接管 ZC/ATS 的重叠区，则若列车从此轨道区段上沿电子地图的上行方向运行可进入该接管 ZC/ATS，则该 ZC/ATS 的连接方向为上行；若列车从此轨道区段上沿电子地图的下行方向运行可进入该接管 ZC/ATS，则该 ZC/ATS 的连接方向为下行。

#### 5.3.4 M DIR REF（运营方向与轨道区段描述默认方向的对应关系）

车地通信协议中，V0BC向地面设备发送的信息、地面设备向V0BC发送的消息中，涉及方向的字段均以运营方向的上下行描述。通常情况下，制作电子地图时，会考虑令电子地图的上下行与运营方向的上下行一致，但某些特殊情况下，可能无法实现，故此，需要明确电子地图中的上下行定义与运营方向的上下行定义的对向关系，如图8所示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0f89288f-be69-4a7b-8f8e-77944a238d11/markdown_0/imgs/img_in_image_box_85_121_799_495.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A40%3A55Z%2F-1%2F%2F261d85f9ebee8a039cf395596625f47fd6e125a530e8b53f7e23944e0c00562a" alt="Image" width="84%" /></div>


说明：

图中为制作电子地图采用的信号平面图。按照电子地图上下行定义，从左到右定义为电子地图上行方向，从右向左定义为电子地图下行方向，见红色圈出的方向。由于运营要求等情况，线路运营方向定义为：从左到右定义为运营方向的下行方向，从右到左定义为运营方向的上行方向，见绿色圈出的方向。此种情况下，相关轨道区段的 M_DIR_REF 字段取值为“方向相反”。

<div style="text-align: center;">图 8 电子地图上下行定义与运营方向上下行不一致</div>


由于线路内可能存在灯泡线等情况，线路内各轨道区段的运营方向定义可能发生变化，故 M_DIR_REF 定义为轨道区段属性而非线路属性。

#### 5.3.5 NID TRPROPERTY(轨道区段属性)

##### 5.3.5.1 说明

对同一轨道区段，各类轨道区段属性可能共存。当同一轨道区段上各类属性共存时，属性取值为具有的各属性取值之和。

例如，某轨道区段既为普通上行轨道区段（属性取值为0x000001），又为上行转换轨（属性取值为0x000004），无其他属性，则轨道区段属性取值应为：0x000005（0x000001 + 0x000004）。

##### 5.3.5.2 普通上/下行轨道区段

若正常运营时，列车在轨道区段上的运行方向为沿电子地图的

---

上行方向，则该轨道区段为上行轨道区段；若正常运营时，列车在轨道区段上的运行方向为沿电子地图的下行方向，则该轨道区段为下行轨道区段。正常运营时列车在轨道区段上的运行方向可在工程阶段确定，普通上、下行轨道区段在同一轨道区段属性内不可兼容，如图9所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//22756c37-404c-4bef-9f5f-63c9a31cf510/markdown_0/imgs/img_in_image_box_77_304_777_562.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A40%3A59Z%2F-1%2F%2F34f287a11121862395e6ac0bde85d61db17f2ef63f5a90ca409e29565788e1d1" alt="Image" width="83%" /></div>


工程阶段确定：正常运营时，列车在轨道区段 G03 上从右向左运行。故轨道区段 G03 的属性为“普通下行轨道区段”。

<div style="text-align: center;">图 9 普通上/下行轨道区段定义示例</div>


##### 5.3.5.3 上/下行转换轨

若轨道区段可作为转换轨，则转换轨的“上/下行”应与作为普通轨道区段的“上/下行”一致。

##### 5.3.5.4 站台

若轨道区段与站台区域有重叠，则该轨道区段具有站台属性，否则，该轨道区段不具有站台属性。

##### 5.3.5.5 道岔

若轨道区段包含任一道岔的岔后反位区域，则该轨道区段具有道岔属性，否则，该轨道区段不具有道岔属性。

以图 5 为例，各轨道区段的道岔属性见表 4。

---

<div style="text-align: center;">表 4 轨道区段的道岔属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>道岔属性</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1-A</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A-2</td><td style='text-align: center;'>有</td><td style='text-align: center;'>包含D1岔后反位区域</td></tr><tr><td style='text-align: center;'>A-B</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>6-B</td><td style='text-align: center;'>有</td><td style='text-align: center;'>包含D2岔后反位区域</td></tr><tr><td style='text-align: center;'>B-C</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>3-C</td><td style='text-align: center;'>有</td><td style='text-align: center;'>包含D3岔后反位区域</td></tr><tr><td style='text-align: center;'>C-D</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>D-4</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>D-5</td><td style='text-align: center;'>有</td><td style='text-align: center;'>包含D4岔后反位区域</td></tr></table>

可能存在轨道区段对不同的道岔来说包含区域不同的情况,如图10所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a50383ed-9e0b-49e8-b24e-dab166c4f130/markdown_0/imgs/img_in_image_box_231_675_660_919.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A02Z%2F-1%2F%2Fc3a40feded2202521943d1698e69af13ed2c037785c1dfc218c5d749c0569f01" alt="Image" width="50%" /></div>


说明：

轨道区段 B—C 为道岔 D2 的岔后反位区域，同时为道岔 D3 的岔前区域。按照定义，B—C 包含道岔（D2）的岔后反位区域，故应具有道岔属性。

<div style="text-align: center;">图 10 轨道区段对不同道岔包含不同区域</div>

---

##### 5.3.5.6 上/下行车挡

若轨道区段上有车挡，则车挡的“上/下行”应与作为普通轨道区段的“上/下行”一致。

##### 5.3.5.7 上/下行线路终点

若轨道区段为线路终点（指线路尽头）轨道区段，则线路终点的“上/下行”应与作为普通轨道区段的“上/下行”一致。

##### 5.3.5.8 上下行灯泡线边界

若轨道区段的上行链接轨道区段的上行链接轨道区段(参见5.3.6)为本轨道区段,则该轨道区段应具有上行灯泡线边界属性。

若轨道区段的下行链接轨道区段的下行链接轨道区段为本轨道区段，则该轨道区段应具有下行灯泡线边界属性。如图 11 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//4b69eb63-96df-41de-9c13-328b71744c27/markdown_0/imgs/img_in_image_box_208_491_650_681.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A06Z%2F-1%2F%2Fc4255313b8b768cdd0a4fd8063f069bf27245e9e60e764db69bc9052884db0bf" alt="Image" width="52%" /></div>


说明：

轨道区段1—2的下行链接轨道区段为轨道区段1—5，轨道区段1—5的下行链接轨道区段为轨道区段1—2，故轨道区段1—2、1—5应具有下行灯泡线边界属性；同理，轨道区段3—4、6—4应具有上行灯泡线边界属性，轨道区段2—3、5—6不具有灯泡线属性。

注：电子地图中描述的灯泡线属性为按照电子地图方向确定的灯泡线属性，与按照运营方向确定的灯泡线属性不同。

<div style="text-align: center;">图 11 灯泡线边界示意图</div>


##### 5.3.5.9 CI通信轨道区段

根据工程阶段定义需求，若 VOBC 需向 CI 发送该轨道区段 ID，则该轨道区段具有 CI 通信轨道区段属性。否则，该轨道区段不具有 CI 通信轨道区段属性。

---

#### 5.3.6 NID_TRUPLINK/NID_TRDOWNLINK（上/下行方向链接轨道区段编号）

从轨道区段沿上行方向搜索，找到相邻的轨道区段，对相邻轨道区段进行判断：

a）若只存在一个相邻轨道区段，则该相邻轨道区段为该轨道区段的上行链接轨道区段；

b）若存在多个相邻轨道区段，则该轨道区段沿上行方向末端必为道岔岔尖，将该道岔岔后定位区域所在的相邻轨道区段作为该轨道区段的上行链接轨道区段。

从轨道区段沿下行方向搜索，找到相邻的轨道区段，对相邻轨道区段进行判断：

a）若只存在一个相邻轨道区段，则该相邻轨道区段为该轨道区段的下行链接轨道区段；

b）若存在多个相邻轨道区段，则该轨道区段沿下行方向末端必为道岔岔尖，将该道岔岔后定位区域所在的相邻轨道区段作为该轨道区段的下行链接轨道区段。

以图 5 为例，相关轨道区段的上/下行链接轨道区段见表 5。

<div style="text-align: center;">表 5 轨道区段的链接轨道区段</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>上行链接轨道区段</td><td style='text-align: center;'>下行链接轨道区段</td></tr><tr><td style='text-align: center;'>1—A</td><td style='text-align: center;'>A—B</td><td style='text-align: center;'>不在该道岔区域内</td></tr><tr><td style='text-align: center;'>A—2</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>1—A</td></tr><tr><td style='text-align: center;'>A—B</td><td style='text-align: center;'>B—C</td><td style='text-align: center;'>1—A</td></tr><tr><td style='text-align: center;'>6—B</td><td style='text-align: center;'>B—C</td><td style='text-align: center;'>不在该道岔区域内</td></tr><tr><td style='text-align: center;'>B—C</td><td style='text-align: center;'>C—D</td><td style='text-align: center;'>A—B</td></tr><tr><td style='text-align: center;'>3—C</td><td style='text-align: center;'>C—D</td><td style='text-align: center;'>不在该道岔区域内</td></tr><tr><td style='text-align: center;'>C—D</td><td style='text-align: center;'>D—4</td><td style='text-align: center;'>B—C</td></tr><tr><td style='text-align: center;'>D—4</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>C—D</td></tr></table>

---

<div style="text-align: center;">表 5 轨道区段的链接轨道区段(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>上行链接轨道区段</td><td style='text-align: center;'>下行链接轨道区段</td></tr><tr><td style='text-align: center;'>D-5</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>C-D</td></tr><tr><td style='text-align: center;'>1之外</td><td style='text-align: center;'>1-A</td><td style='text-align: center;'>不在该道岔区域内</td></tr><tr><td style='text-align: center;'>2之外</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>A-2</td></tr><tr><td style='text-align: center;'>3之外</td><td style='text-align: center;'>3-C</td><td style='text-align: center;'>不在该道岔区域内</td></tr><tr><td style='text-align: center;'>4之外</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>D-4</td></tr><tr><td style='text-align: center;'>5之外</td><td style='text-align: center;'>不在该道岔区域内</td><td style='text-align: center;'>D-5</td></tr><tr><td style='text-align: center;'>6之外</td><td style='text-align: center;'>6-B</td><td style='text-align: center;'>不在该道岔区域内</td></tr></table>

应注意，若轨道区段为线路边界处轨道区段，则该轨道区段向相邻线路方向的链接轨道应为相邻线路的轨道区段。

#### 5.3.7 NID_SWITCHLINK(轨道区段链接道岔所属轨道区段)

轨道区段链接道岔确定原则参见5.3.8。

轨道区段链接道岔所属轨道区段确定原则为：确定轨道区段及链接道岔后，则该链接道岔的岔后反位区域所在轨道区段为该轨道区段的该链接道岔的所属轨道区段。以图5为例，各轨道区段的链接道岔所属轨道区段见表6。

<div style="text-align: center;">表 6 轨道区段链接道岔所属轨道区段</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>上行链接道岔及所属轨道区段</td><td style='text-align: center;'>下行链接道岔及所属轨道区段</td></tr><tr><td style='text-align: center;'>1-A</td><td style='text-align: center;'>DI(A-2)</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A-2</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A-B</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>6-B</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>B-C</td><td style='text-align: center;'>无</td><td style='text-align: center;'>D2(6-B)</td></tr><tr><td style='text-align: center;'>3-C</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr></table>

---

<div style="text-align: center;">表 6 轨道区段链接道岔所属轨道区段（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>上行链接道岔及所属轨道区段</td><td style='text-align: center;'>下行链接道岔及所属轨道区段</td></tr><tr><td style='text-align: center;'>C—D</td><td style='text-align: center;'>D4(D—5)</td><td style='text-align: center;'>D3(3—C)</td></tr><tr><td style='text-align: center;'>D—4</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>D—5</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr></table>

#### 5.3.8 NID_ID_SWITCHLINK(轨道区段链接道岔)

##### 5.3.8.1 轨道区段链接道岔确定原则

若道岔的岔前区域在轨道区段上，则该道岔是该轨道区段的链接道岔。以图5为例，各轨道区段的链接道岔见表7。

<div style="text-align: center;">表 7 轨道区段的链接道岔</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>链接道岔</td></tr><tr><td style='text-align: center;'>1—A</td><td style='text-align: center;'>D1</td></tr><tr><td style='text-align: center;'>A—2</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A—B</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>6—B</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>B—C</td><td style='text-align: center;'>D2</td></tr><tr><td style='text-align: center;'>3—C</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>C—D</td><td style='text-align: center;'>D3, D4</td></tr><tr><td style='text-align: center;'>D—4</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>D—5</td><td style='text-align: center;'>无</td></tr></table>

##### 5.3.8.2 轨道区段链接道岔方向确定原则

从轨道区段左端开始，沿电子地图上行方向搜索该轨道区段的链接道岔，其中对向链接道岔为上行道岔，顺向道岔为下行道岔。上/下行道岔 N 表示按照上述方法搜索到的第 N 个上/下行道岔。

以图 5 为例, 链接道岔的方向见表 8。

---

<div style="text-align: center;">表 8 链接道岔方向</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段</td><td style='text-align: center;'>上行链接道岔</td><td style='text-align: center;'>下行链接道岔</td></tr><tr><td style='text-align: center;'>1—A</td><td style='text-align: center;'>D1</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A—2</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>A—B</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>6—B</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>B—C</td><td style='text-align: center;'>无</td><td style='text-align: center;'>D2</td></tr><tr><td style='text-align: center;'>3—C</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>C—D</td><td style='text-align: center;'>D4</td><td style='text-align: center;'>D3</td></tr><tr><td style='text-align: center;'>D—4</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr><tr><td style='text-align: center;'>D—5</td><td style='text-align: center;'>无</td><td style='text-align: center;'>无</td></tr></table>

#### 5.3.9 轨道区段应答器

N_ITERUB 为本轨道区段内应答器的总数。此处的“本轨道区段内应答器”指物理位置位于本轨道区段内的应答器。例如跨线边界处信号机对应的主应答器/预告应答器，由相邻线路地面设备管理，但位于本轨道区段内，在计算本字段时也应包含在内。

轨道区段内的应答器顺序按照电子地图上行方向排列。

NID_BALISE 字段中，“应答器所属线路编号”指应答器实际所属的线路而非物理位置所在线路，例如跨线边界处信号机对应的主应答器/预告应答器，由相邻线路地面设备管理，故其所属线路编号应填写相邻线路的线路编号。

#### 5.3.10 D STOPPINGPOINT(轨道区段停车点)

若轨道区段具有站台属性或在上/下行无人折返停车区域内(参见5.4)，则可配置轨道区段停车点。

停车点在轨道区段内对应位置，以停车点距轨道区段左端起点偏移量描述。

停车点位置应为列车在指定停车位置停车时，列车头端第一个客室门中心线对应的位置。

上/下行停车点表示列车沿电子地图上/下行方向在轨道区段内运行

---

停车时使用的停车点。

上行停车点序号按照上行停车点在轨道区段内的位置从右向左增大，靠近轨道区段右端终点的上行停车点为上行停车点1，远离轨道区段右端终点的上行停车点为上行停车点2。

下行停车点序号按照下行停车点在轨道区段内的位置从左向右增大，靠近轨道区段左端起点的下行停车点为下行停车点1，远离轨道区段左端起点的下行停车点为下行停车点2。

停车点示意如图 12 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//97fdd8a2-d5a0-43e5-bc2b-990fa9d3a583/markdown_0/imgs/img_in_image_box_130_400_761_470.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A22Z%2F-1%2F%2Fd2d2e567006140d21b005f62e934120c003069350681df19ef7e09412f6ea4e2" alt="Image" width="74%" /></div>


<div style="text-align: center;">图 12 停车点示意图</div>


轨道区段停车点的具体设置原则在工程中约定。

#### 5.3.11 M_STOPPING_UP/M_STOPPING_DOWN(上/下行轨道区段停车点属性)

折返停车点：列车进行折返换端作业时，换端前车头使用的停车点。无人自动折返时应使用该停车点，有人折返时可使用该停车点。列车是否在折返停车点停准，可不影响折返功能。

运营停车点：列车经过时必须停车的停车点。

若轨道区段内有多个上/下行停车点，则多个上/下行停车点的属性应一致。

折返换端区域内(参见5.4.3.2)应对换端前车头配置停车时使用的轨道区段停车点，若无运营停车点，则配置折返停车点。

#### 5.3.12 D REF STOPPOINT(参考停车点)

参考停车点为供 ATO 在区间停车时参考的停车点，在区间信号机所在轨道区段上配置该停车点。列车沿规定运营方向进入该轨道区段，且需要在该轨道区段沿运营方向尽头的区间信号机前停车时，可考虑使用该停车点。

参考停车点在轨道区段内对应位置，以该参考停车点距轨道区段左

---

端起点偏移量描述。

参考停车点与轨道区段运营停车点在同一轨道区段内的同一方向上不应同时存在。

参考停车点与轨道区段折返停车点在同一轨道区段内的同一方向上可同时存在。若无人自动折返停车点与停车参考点位置重复，则应分别配置，即在轨道区段停车点、停车参考点字段中均有该方向停车点信息，且偏移量相同。

上/下行参考停车点表示列车沿电子地图上/下行方向在轨道区段内运行停车时使用的参考停车点。

上行参考停车点序号按照上行参考停车点在轨道区段内的位置从右向左增大，靠近轨道区段右端终点的上行参考停车点为上行参考停车点1，远离轨道区段右端终点的上行参考停车点为上行参考停车点2。

下行参考停车点序号按照下行参考停车点在轨道区段内的位置从左向右增大，靠近轨道区段左端起点的下行参考停车点为下行参考停车点1，远离轨道区段左端起点的下行参考停车点为下行参考停车点2。

参考停车点示意如图 13 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//f1d645bd-5a20-4815-b395-1ba325359496/markdown_0/imgs/img_in_image_box_122_662_742_732.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A27Z%2F-1%2F%2F0ebccc5aa44a0404f92cd3d6fa5c5e2f3cc695871c7c3a5290e76f6ef6e14a92" alt="Image" width="73%" /></div>


<div style="text-align: center;">图 13 参考停车点示意图</div>


参考停车点的具体设置原则在工程中约定。

#### 5.3.13 站台特有属性

##### 5.3.13.1 非站台处理

若轨道区段无对应站台，则相关字段填写全0。

##### 5.3.13.2 左右侧定义

若轨道区段属性为上行，则沿电子地图上行方向确定“站台特有属性”范围内相关的左右侧。

若轨道区段属性为下行，则沿电子地图下行方向确定“站台特有属性”范围内相关的左右侧。

---

##### 5.3.13.3 默认站停时间

上行默认站停时间，指列车按照电子地图上行方向进站停车后，在此轨道区段对应站台的默认站停时间；下行默认站停时间，指列车按照电子地图下行方向进站停车后，在此轨道区段对应站台的默认站停时间。

站停时间在工程阶段确定。

对于双侧开关门的站台，默认的左右侧开关门时间各取对应默认站停时间的均分。

##### 5.3.13.4 Q_DOORDIR(开门侧信息)/站台门ID

站台门 ID 应与开门侧信息匹配。即：若有站台门 ID 则必须有对应开门侧。

由于存在站台上无站台门的情况，故开门侧可不存在站台门ID。

##### 5.3.13.5 默认开门顺序

上行默认开门顺序，指列车按照电子地图上行方向进站停车后，在此轨道区段对应站台需采用的默认开门顺序；下行默认开门顺序，指列车按照电子地图下行方向进站停车后，在此轨道区段对应站台需采用的默认开门顺序。

应注意，左右门的定义为按照轨道区段属性中的上行/下行规定，故“默认开门顺序”中的左右门与列车停车时实际的左右门可能不一致。例如，轨道区段属性为上行轨道区段，下行默认开门顺序为“先开关左门再开关右门”，则列车按电子地图下行方向进站停车时，实际应实现的开门顺序为先开关右侧车门再开关左侧车门。

#### 5.3.14 风井/防淹门/无电区

轨道区段上的风井/防淹门/无电区顺序应按照电子地图上行方向排列。

#### 5.3.15 分段限速/坡度/曲率/隧道

##### 5.3.15.1 说明

各分段限速/坡度/曲率/隧道区域应不存在重合部分。

轨道区段内所有分段限速/坡度/曲率/隧道区域的集合应为该轨道区段区域。

分段限速/坡度/曲率/隧道区域顺序应按照电子地图上行方向排列。

对于坡度变化较多的区段,如果定义的数量不能满足时,可采取对坡度向安全侧取整后合并的策略,以满足定义数量。

---

##### 5.3.15.2 竖曲线半径

两个坡度间的竖曲线半径信息应填写在两个坡度之间。

若竖曲线半径对应的变坡处为轨道区段边界点，则竖曲线半径应填写在按电子地图上行方向上的前一个轨道区段内。若变坡处轨道区段边界点位于电子地图灯泡线边界（无法确定电子地图上行方向上的前一个），则可在相邻的两个轨道区段内任选其一填写。

如果信号平面图没有标出竖曲线半径，则填0。

竖曲线半径示意如图 14 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5179a63d-c1fd-4d34-b515-ed51aab85c5e/markdown_0/imgs/img_in_image_box_91_381_767_565.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A35Z%2F-1%2F%2Faa25e0edc66d095fcf82bfea56d22f1883418f89a54abf92265b5e4d8b9b808f" alt="Image" width="80%" /></div>


说明：

轨道区段1、2、3，涉及的坡度包括A—B、B—C、C—D、D—E，B1为轨道区段1、2的分界点，D为轨道区段2、3的分界点。

若 D 点非灯泡线边界，则轨道区段 1 上应填写的坡度信息应为 A—B、B—B1，轨道区段 2 上应填写的坡度信息为 B1—C、C—D，轨道区段 3 上应填写的坡度信息为 D—E、E—F。竖曲线半径值 1 信息应填写在轨道区段 1 的坡度信息 A—B、B—B1 之间；竖曲线半径值 2 信息应填写在轨道区段 2 的坡度信息 B1—C、C—D 之间；竖曲线半径值 3 应填写在轨道区段 2 的坡度信息 C—D 之后。

若 D 点为上行灯泡线边界，则轨道区段 1 上应填写的坡度信息应为 A—B、B—B1，轨道区段 2 上应填写的坡度信息为 B1—C、C—D，轨道区段 3 上应填写的坡度信息为 E—F、D—E。竖曲线半径值 1 信息应填写在轨道区段 1 的坡度信息 A—B、B—B1 之间；竖曲线半径值 2 信息应填写在轨道区段 2 的坡度信息 B1—C、C—D 之间；竖曲线半径值 3 可在轨道区段 2 的坡度信息 C—D 之后，或轨道区段 3 的坡度信息 D—E 之后任选其一填写。

若 D 点为下行灯泡线边界，则 D 点为轨道区段 2、轨道区段 3 的上行起始点。为符合坡度信息的描述方式（先分段坡度再竖曲线半径），在轨道区段 2、轨道区段 3 的起始点分别增加一个虚拟的长度为 0 的分段坡度信息，然后将竖曲线半径值 3 作为这两个轨道区段的第一个竖曲线半径，在虚拟分段坡度信息之后填写。

<div style="text-align: center;">图 14 竖曲线半径示意图</div>

---

##### 5.3.15.3 曲率半径

指缓和曲线的曲率半径。

若缓和曲线有重叠部分，则填写时，重叠部分应只属于一个分段曲率，可在所属分段曲率中任选其一填写。

#### 5.3.16 L CRC(CRC 校验)

对于含有多个元素的数据结构（轨道区段、折返区域、应答器、信号机、车挡、ZC、CI、ATS、MSS、DSU），CRC为针对整个数据结构计算。例如轨道区段数据整体结构见表9。

<div style="text-align: center;">表 9 轨道区段数据整体结构示意</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>轨道区段1</td></tr><tr><td style='text-align: center;'>轨道区段2</td></tr><tr><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>轨道区段N_TRACK</td></tr><tr><td style='text-align: center;'>L_CRC</td></tr></table>

L_CRC 应根据轨道区段 1 ~ 轨道区段 N_TRACK 的所有数据计算。

### 5.4 折返区域

#### 5.4.1 折返区域数据结构

折返区域数据结构构成见表10。

#### 5.4.2 NID TRACK(折返区域包含轨道区段编号)

若折返区域内包含多个轨道区段，则按照电子地图上行方向依次填写。

#### 5.4.3 NID TPPROPERTY(折返区域属性)

##### 5.4.3.1 说明

对同一折返区域，各类折返区域属性可能共存。当同一折返区域上各类属性共存时，属性取值为具有的各属性取值之和。

例如，某折返区域既为上行折返换端区域（属性取值为0x000001），又为上行无人折返发车区域（属性取值为0x000004），无其他属性，则折返区域属性取值应为：0x000005（0x000001 + 0x000004）。

---

<div style="text-align: center;">表 10 折返区域数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>折返区域数据整体结构</td><td style='text-align: center;'>M_STRUCT_AR_AREA</td><td style='text-align: center;'>N_AR_AREA * N + 4</td><td style='text-align: center;'></td><td style='text-align: center;'>折返区域数据整体的数据结构定义: 折返区域数据整体结构由N_AR_AREA个长度为N的折返区域数据构成(N表示序号1~5的数据长度总和),并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>折返区域编号</td><td style='text-align: center;'>NID_AR_AREA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFFF,0无效</td><td style='text-align: center;'>折返区域ID</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>所属线路编号值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>折返区域包含轨道区段数量</td><td style='text-align: center;'>N_TRACK</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~4,其他无效</td><td style='text-align: center;'>折返区域内包含的轨道区段总数</td></tr><tr><td rowspan="4">4</td><td rowspan="4">折返区域包含轨道区段编号参见5.4.2</td><td rowspan="4">NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFFF,0无效</td><td style='text-align: center;'>折返区域内轨道区段1编号值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无轨道区段2</td><td style='text-align: center;'>折返区域内轨道区段2编号值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无轨道区段3</td><td style='text-align: center;'>折返区域内轨道区段3编号值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无轨道区段4</td><td style='text-align: center;'>折返区域内轨道区段4编号值</td></tr></table>

---

<div style="text-align: center;">表 10 折返区域数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>折返区域属性</td><td style='text-align: center;'>NID_TPPROP-ERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x001000:上行折返换端区域0x002000:下行折返换端区域0x004000:上行无人折返发车区域0x008000:下行无人折返发车区域0x010000:上行无人折返停车区域0x020000:下行无人折返停车区域参见5.4.3</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>折返区域数据整体CRC</td></tr></table>

---

##### 5.4.3.2 上/下行折返换端区域

若列车可在折返区域进行折返换端，则该折返区域应具有“折返换端区域”属性。

折返换端区域的方向根据列车折返前驶入折返区域的方向进行判断：若列车沿电子地图的上行方向驶入折返区域，则该折返区域为上行折返换端区域；若列车沿电子地图的下行方向驶入折返区域，则该折返区域为下行折返换端区域。上、下行折返换端区域属性在同一折返区域属性内可兼容。

以图9为例，若轨道区段G03为一个折返换端区域，若工程阶段规定，此折返区域只可进行从右向左驶入，换端后从左向右驶出的折返流程，则该折返区域为下行折返换端区域；若规定此折返区域可进行从右向左驶入，换端后从左向右驶出的折返流程也可进行从左向右驶入，换端后从右向左驶出的折返流程，则该折返区域同时具有上行折返换端区域、下行折返换端区域属性。

##### 5.4.3.3 上/下行无人折返发车区域

若折返区域可作为无人自动折返的发车区域（包括折入过程的发车区域和折出过程的发车区域），则根据列车进行无人自动折返作业时发车的方向进行判断：若列车沿电子地图的上行方面发车，则该折返区域为上行无人折返发车区域；若列车沿电子地图的下行方向发车，则该折返区域为下行无人折返发车区域。上行无人折返发车区域属性在同一折返区域属性内可兼容。

以图9为例，若轨道区段G03为一个折返区域，若工程阶段规定，此折返区域只可进行从右向左驶出的无人自动折返流程，则该折返区域为下行无人折返发车区域；若规定该折返区域可进行从右向左驶出，也可进行从左向右驶出的折返流程，则该折返区域同时具有上行无人折返发车区域、下行无人折返发车区域属性。

##### 5.4.3.4 上/下行无人折返停车区域

若折返区域可作为无人自动折返的停车区域（包括折入过程的停车区域和折出过程的停车区域），则根据列车进行无人自动折返作业时驶入该折返区域的方向进行判断：若列车沿电子地图的上行方向驶入该折

---

返区域停车，则该折返区域为上行无人折返停车区域；若列车沿电子地图的下行方向驶入该折返区域停车，则该折返区域为下行无人折返停车区域。上、下行无人折返停车区域属性在同一轨道区段属性内可兼容。

以图9为例，若轨道区段G03为一个折返区域，若工程阶段规定，此折返区域只可进行从右向左驶入停车，换端后从左向右驶出的无人自动折返流程，则该折返区域为下行无人折返停车停车；若规定该折返区域可进行从右向左驶入停车，换端后从左向右驶出的无人自动折返流程，也可进行从左向右驶入停车，换端后从右向左驶出的无人自动折返流程，则该折返区域同时具有上行无人折返停车区域、下行无人折返停车区域属性。

无人自动折返流程如图 15 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//28b45b5d-d66d-4736-b4db-bbf95f1d238c/markdown_0/imgs/img_in_image_box_82_439_812_742.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A41%3A52Z%2F-1%2F%2F6c52a7a2748da3f97a20a56acabfe35017645bdb9f953e96c71feea366e1801f" alt="Image" width="86%" /></div>


说明：

无人自动折返过程如下：列车在折返区域 G07 开始无人自动折返流程，从折返区域 G07 发车，驶入折返区域 G03，停车并自动换端，之后驶入折返区域 G06 停车，完成无人自动折返流程。根据此流程，考虑折返区域属性：无人自动折返过程中，由于列车在 G07 发车，发车方向按照电子地图下行方向，故 G07 应具有下行无人折返发车区域属性；由于列车进入 G03 停车，进入方向为电子地图下行方向，故 G03 应具有下行无人折返停车区域属性；由于列车在 G03 换端，换端前按照电子地图下行方向驶入，故 G03 应具有下行折返换端区域属性；由于列车在 G03 发车，发车方向按照电子地图上行方向，故 G03 应具有上行无人折返发车区域属性；由于列车进入 G06 停车，进入方向为电子地图上行方向，故 G06 应具有上行无人折返停车区域属性。

<div style="text-align: center;">图 15 无人自动折返流程示意</div>

---

相关折返区域属性见表11。

<div style="text-align: center;">表 11 折返区域属性</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>折返区域</td><td style='text-align: center;'>折返区域属性</td></tr><tr><td style='text-align: center;'>G07</td><td style='text-align: center;'>下行无人折返发车区域</td></tr><tr><td style='text-align: center;'>G03</td><td style='text-align: center;'>下行无人折返停车区域、下行折返换端区域、上行无人折返发车区域</td></tr><tr><td style='text-align: center;'>G06</td><td style='text-align: center;'>上行无人折返停车区域</td></tr></table>

### 5.5 应答器

#### 5.5.1 应答器数据结构

应答器数据结构构成见表12。

#### 5.5.2 NID_BALPROPERTY(应答器属性)

##### 5.5.2.1 说明

对同一应答器，各类应答器属性可能共存。当同一应答器上各类属性共存时，属性取值为具有的各属性取值之和。

例如，某应答器既为上行站台精确停车应答器（属性取值为0x0001），又为下行站台精确停车应答器（属性取值为0x0002），无其他属性，则应答器属性取值应为：0x0003（0x0001 + 0x0002）。

##### 5.5.2.2 上/下行定义

以站台精确停车应答器为例。

若列车按照电子地图上行方向经过应答器时，需将该应答器作为站台精确停车应答器使用，则该应答器属性为上行站台精确停车应答器。

若列车按照电子地图下行方向经过应答器时，需将该应答器作为站台精确停车应答器使用，则该应答器属性为下行站台精确停车应答器。

其他属性以此类推。

##### 5.5.2.3 兼预告的主应答器

若应答器具有“兼预告的主应答器”属性，则应同时具备主应答器与填充应答器属性。

### 5.6 信号机

#### 5.6.1 信号机数据结构

信号机数据结构构成见表 13。

---

<div style="text-align: center;">表 12 应答器数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>应答器数据整体结构</td><td style='text-align: center;'>M_STRUCT_BALISE</td><td style='text-align: center;'>N_BALISE*N+4</td><td style='text-align: center;'></td><td style='text-align: center;'>应答器数据整体的数据结构定义；应答器数据整体结构由N_BALISE个长度为N的应答器数据构成(N表示序号1~8的数据长度总和)，并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>应答器编号</td><td style='text-align: center;'>NID_BALISE</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~16 383，其他无效</td><td style='text-align: center;'>用于在一条线路内，唯一识别的ID，数据有效长度为14位</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF，0无效</td><td style='text-align: center;'>所属线路编号值。注：线路边界处离去信号机对应主应答器/预告应答器位置在本线路内，故需在本线路内电子地图中描述，但所属线路为相邻线路</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>应答器所在轨道区段编号</td><td style='text-align: center;'>NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF，0无效</td><td style='text-align: center;'>所在轨道区段编号值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>应答器在轨道区段内的位置</td><td style='text-align: center;'>D_BALPOSOFF</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>应答器安装位置相对于所在轨道区段起点的偏移量，按照电子地图上行方向进行偏移量计算，单位cm</td></tr></table>

---

<div style="text-align: center;">表 12 应答器数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>应答器属性</td><td style='text-align: center;'>NID_BALPROP_ERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFF,0无效</td><td style='text-align: center;'>0x0001:上行站台精确停车应答器0x0002:下行站台精确停车应答器0x0004:上行轮径校准应答器0x0008:下行轮径校准应答器0x0010:上行填充应答器0x0020:下行填充应答器0x0040:上行主应答器0x0080:下行主应答器0x0100:其他固定应答器0x0200:兼预告的主应答器参见5.5.2</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>应答器安装精度</td><td style='text-align: center;'>Q_BALLOCACC</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF.0无效</td><td style='text-align: center;'>应答器安装精度,单位:cm。不同应答器属性应满足相应要求的安装精度</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>对应的信号机编号</td><td style='text-align: center;'>NID_SIGNAL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0表示无对应信号机</td><td style='text-align: center;'>对应的信号机编号,仅当应答器具备填充应答器或主应答器属性时有效。对兼预告的主应答器,描述其作为主应答器对应的信号机编号</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>地图版本信息</td><td style='text-align: center;'>M_VERSIONBAL</td><td style='text-align: center;'>2</td><td style='text-align: center;'></td><td style='text-align: center;'>描述为本应答器所辖范围内的地图版本,具体版本定义由工程定义</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>应答器数据整体CRC</td></tr></table>

---

<div style="text-align: center;">表 13 信号机数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>信号机数据整体结构</td><td style='text-align: center;'>M_STRUCT_SIGNAL</td><td style='text-align: center;'>N_SIGNAL*N+4</td><td style='text-align: center;'></td><td style='text-align: center;'>信号机数据整体的数据结构定义：信号机数据整体结构由N_SIGNAL个长度为N的信号机数据构成(N表示序号1~7的数据长度总和)，并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>信号机编号</td><td style='text-align: center;'>NID_SIGNAL</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>信号机编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所在线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>所在线路编号值。注：线路边界离去处信号机属于相邻线路管理，但所在线路应为本线路</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>信号机所在轨道区段编号</td><td style='text-align: center;'>NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>所在轨道区段编号值。参见5.6.2</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>信号机属性</td><td style='text-align: center;'>NID_SIGPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x0001:进站信号机；0x0002:出站信号机；0x0004:出站兼道岔防护信号机；0x0008:道岔防护信号机；0x0010:区间间隔信号机；0x0020:进段/进场信号机；0x0040:出段/出场信号机；</td></tr></table>

---

<div style="text-align: center;">表 13 信号机数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>信号机属性</td><td style='text-align: center;'>NID_SIGPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x0080:出库信号机;0x0100:入库信号机;0x0200:终端信号机;0x0400:调车信号机;0x0800:阻挡信号机。参见5.6.3</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>信号机在轨道区段内的位置</td><td style='text-align: center;'>D_SIGPOSOFF</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>信号机安装位置相对于所在轨道区段起点的偏移量,按照电子地图上行方向进行偏移量计算,单位cm</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>信号机方向</td><td style='text-align: center;'>Q_SIGDIR</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:上行0xAA:下行其他无效</td><td style='text-align: center;'>信号机描述的方向。参见5.6.4</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>保护区段信息</td><td style='text-align: center;'>M_OVERLAP</td><td style='text-align: center;'>1</td><td style='text-align: center;'>0x55:有保护区段0x00:无保护区段</td><td style='text-align: center;'>信号机作为终端信号机的进路是否有外置保护区段</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>信号机数据整体CRC</td></tr></table>

---

#### 5.6.2 信号机所在轨道区段编号及偏移量

通常，信号机安装位置应在其作为始端信号机防护进路起点计轴轴头的外方。对此类信号机，应描述信号机安装位置所在的轨道区段及该信号机在该轨道区段上的偏移量。

若信号机安装位置位于轨道区段边界，则该信号机应在信号机防护进路外方的轨道区段上进行描述。

若信号机安装位置位于该信号机防护进路内，则在电子地图中，按照此信号机安装位置位于其防护进路起点计轴轴头（必然为轨道区段分界点）处理，在该信号机防护进路外方的轨道区段上描述该信号机。

#### 5.6.3 NID SIGPROPERTY(信号机属性)

##### 5.6.3.1 说明

对同一信号机，各类信号机属性可能共存。当同一信号机上各类属性共存时，属性取值为具有的各属性取值之和。

例如，某信号机为出站兼防护信号机，则其必具备的属性为：出站信号机（属性取值为0x0002）、出站兼道岔防护信号机（属性取值为0x0004）、道岔防护信号机（属性取值为0x0008），若该信号机无其他属性，则信号机属性取值应为：0x000E（0x0002 + 0x0004 + 0x0008）。

##### 5.6.3.2 出站兼道岔防护信号机

若信号机具备“出站兼道岔防护信号机”属性，则应同时具备“出站信号机”、“道岔防护信号机”属性。

#### 5.6.4 Q SIGDIR（信号机方向）

若列车按照电子地图上行方向经过信号机时，需对信号机进行防护，则该信号机方向为上行；若列车按照电子地图下行方向经过信号机时，需对信号机进行防护，则该信号机方向为下行。

### 5.7 车挡

车挡数据结构构成见表14。

### 5.8 区域控制器(ZC)

ZC 数据结构构成见表 15。

---

<div style="text-align: center;">表 14 车挡数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>车挡数据整体结构</td><td style='text-align: center;'>M_STRUCT_STBLK</td><td style='text-align: center;'>N_SHELTER*N+4</td><td style='text-align: center;'>CHINA ASSOCIATION</td><td style='text-align: center;'>车挡数据整体的数据结构定义：车挡数据整体结构由N_SHELTER个长度为N的车挡数据构成(N表示序号1~4的数据长度总和)，并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>车挡编号</td><td style='text-align: center;'>NID_STBLK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF0无效</td><td style='text-align: center;'>车挡ID</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>所属线路编号值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>车挡所属轨道区段编号</td><td style='text-align: center;'>NID_TRACK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF0无效</td><td style='text-align: center;'>车挡所在轨道区段编号值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>车挡在轨道区段内的位置</td><td style='text-align: center;'>D_STBLK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF0</td><td style='text-align: center;'>车挡相对于所在轨道区段1起点的偏移量，按照电子地图上行方向进行偏移量计算，单位cm</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF0</td><td style='text-align: center;'>车挡数据整体CRC</td></tr></table>

---

<div style="text-align: center;">表 15 ZC 数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>ZC数据整体结构</td><td style='text-align: center;'>M_STRUCT_ZC</td><td style='text-align: center;'>N_ZC*N+4</td><td style='text-align: center;'></td><td style='text-align: center;'>ZC数据整体的数据结构定义:ZC数据整体结构由N_ZC个长度为N的ZC数据构成(N表示序号1~7的数据长度总和),并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>ZC的ID</td><td style='text-align: center;'>NID_ZC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFFF,0无效</td><td style='text-align: center;'>ZC编号,全路网统一</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路编号值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>对应DSU编号</td><td style='text-align: center;'>NID_DSU</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,0表示无对应DSU</td><td style='text-align: center;'>ZC对应DSU编号,路网统一</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>ZC网络地址(A、B网)</td><td style='text-align: center;'>M_ZCIPAJ</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr></table>

---

<div style="text-align: center;">表 15 ZC 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="3">4</td><td rowspan="3">ZC 网络地址(A、B网)</td><td style='text-align: center;'>M_ZCIPB1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_ZCIPA2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_ZCIPB2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr><tr><td rowspan="2">5</td><td rowspan="2">ZC 网络子网掩码</td><td style='text-align: center;'>M_ZCMASKA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>A网的子网掩码</td></tr><tr><td style='text-align: center;'>M_ZCMASKB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>B网的子网掩码</td></tr></table>

---

<div style="text-align: center;">表 15 ZC 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">6</td><td rowspan="2">ZC网络网关</td><td style='text-align: center;'>M_ZCGTWIPA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>A网的网关</td></tr><tr><td style='text-align: center;'>M_ZCGTWIPB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>B网的网关</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>ZC管辖内电子地图数据校验信息</td><td style='text-align: center;'>M_ZCMapCHK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>该ZC管辖范围内电子地图数据校验信息(V0BC与该ZC通信时使用)</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>ZC数据整体CRC</td></tr></table>

5.9 计算机联锁(CI)

CI 数据构成见表 16。

5.10 列车自动监控(ATS)

ATS 数据结构构成见表 17。

5.11 维护支持子系统(MSS)

MSS 数据结构构成见表 18。

5.12 数据服务单元(DSU)

DSU 数据结构见表 19。

5.13 安全通信协议栈

安全通信协议栈数据结构构成见表20。

---

<div style="text-align: center;">表 16 CI 数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>CI数据整体结构</td><td style='text-align: center;'>M_STRUCT_CI</td><td style='text-align: center;'>N_CI*N+4</td><td style='text-align: center;'>CHINA ASSOCIATION</td><td style='text-align: center;'>CI数据整体的数据结构定义：CI数据整体结构由N_CI个长度为N的CI数据构成(N表示序号1~6的数据长度总和)，并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>CI的ID</td><td style='text-align: center;'>NID_CI</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFF</td><td style='text-align: center;'>CI编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路编号值</td></tr><tr><td rowspan="2">3</td><td rowspan="2">CI网络地址(A、B网)</td><td style='text-align: center;'>M_CIIPA1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255；后2字节表示端口，取值范围：0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_CIIPB1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255；后2字节表示端口，取值范围：0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr></table>

---

<div style="text-align: center;">表 16 CI 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">3</td><td rowspan="2">CI网络地址(A、B网)</td><td style='text-align: center;'>M_CIIPA2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_CIIPB2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr><tr><td rowspan="2">4</td><td rowspan="2">CI网络子网掩码</td><td style='text-align: center;'>M_CIMASKA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>A网的子网掩码</td></tr><tr><td style='text-align: center;'>M_CIMASKB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>B网的子网掩码</td></tr><tr><td rowspan="2">5</td><td rowspan="2">CI网络网关</td><td style='text-align: center;'>M_CIGTWIPA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>A网的网关</td></tr><tr><td style='text-align: center;'>M_CIGTWIPB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>B网的网关</td></tr></table>

---

<div style="text-align: center;">表 16 CI 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度（字节）</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>CI管辖内电子地图数据校验信息</td><td style='text-align: center;'>M_CIMapCHK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>该CI管辖范围内电子地图数据校验信息（V0BC与该CI通信时使用）</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>CI数据整体CRC</td></tr></table>

<div style="text-align: center;">表 17 ATS 数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>ATS 数据整体结构</td><td style='text-align: center;'>M_STRUCT_ATS</td><td style='text-align: center;'>N_ATS * N + 4</td><td style='text-align: center;'>—</td><td style='text-align: center;'>ATS 数据整体的数据结构定义:
ATS 数据整体结构由 N_ATS 个长度为 N 的 ATS 数据构成(N 表示序号 1 ~ 6 的数据长度总和), 并增加 4 字节的整体 CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>ATS 的 ID</td><td style='text-align: center;'>NID_ATS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1 ~ 0xFFFFFFF, 0 无效</td><td style='text-align: center;'>ATS 编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1 ~ 0xFF, 0 无效</td><td style='text-align: center;'>线路编号值</td></tr></table>

---

<div style="text-align: center;">表 17 ATS 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">3</td><td rowspan="4">ATS网络地址(A、B网)</td><td style='text-align: center;'>M_ATSIPA1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_ATSIPB1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_ATSIPA2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_ATSIPB2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr></table>

---

<div style="text-align: center;">表 17 ATS 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">4</td><td rowspan="2">ATS网络子网掩码</td><td style='text-align: center;'>M_ATSMASKA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK: 各字节取值范围: 0~255</td><td style='text-align: center;'>A网的子网掩码</td></tr><tr><td style='text-align: center;'>M_ATSMASKB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK: 各字节取值范围: 0~255</td><td style='text-align: center;'>B网的子网掩码</td></tr><tr><td rowspan="2">5</td><td rowspan="2">ATS网络网关</td><td style='text-align: center;'>M_ATSGTWIPA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP: 各字节取值范围: 0~255</td><td style='text-align: center;'>A网的网关</td></tr><tr><td style='text-align: center;'>M_ATSGTWIPB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP: 各字节取值范围: 0~255</td><td style='text-align: center;'>B网的网关</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>ATS管辖内电子地图数据校验信息</td><td style='text-align: center;'>M_ATSMapCHK</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>该ATS管辖范围内电子地图数据校验信息(V0BC与该ATS通信时使用)</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>ATS数据整体CRC</td></tr></table>

---

<div style="text-align: center;">表 18 MSS 数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>MSS数据整体结构</td><td style='text-align: center;'>M_STRUCT_MSS</td><td style='text-align: center;'>N_MSS*N+4</td><td style='text-align: center;'></td><td style='text-align: center;'>MSS数据整体的数据结构定义:MSS数据整体结构由N_MSS个长度为N的MSS数据构成(N表示序号1~5的数据长度总和),并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>MSS的编号</td><td style='text-align: center;'>NID_MSS</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>MSS编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路编号值</td></tr><tr><td rowspan="2">3</td><td rowspan="2">MSS地址(A、B网)</td><td style='text-align: center;'>M_MSSIPA1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_MSSIPB1</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr></table>

---

<div style="text-align: center;">表 18 MSS 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">3</td><td rowspan="2">MSS地址(A、B网)</td><td style='text-align: center;'>M_MSSIPA2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_MSSIPB2</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr><tr><td rowspan="2">4</td><td rowspan="2">MSS子网掩码</td><td style='text-align: center;'>M_MSSMASKA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>A网的子网掩码</td></tr><tr><td style='text-align: center;'>M_MSSMASKB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>B网的子网掩码</td></tr><tr><td rowspan="2">5</td><td rowspan="2">MSS网关</td><td style='text-align: center;'>M_MSSGTWIPA</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>A网的网关</td></tr><tr><td style='text-align: center;'>M_MSSGTWIPB</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>B网的网关</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>CRC校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFF</td><td style='text-align: center;'>MSS数据整体CRC</td></tr></table>

---

<div style="text-align: center;">表 19 DSU 数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>DSU数据整体结构</td><td style='text-align: center;'>M_STRUCT_DSU</td><td style='text-align: center;'>N_DSU*N+4</td><td style='text-align: center;'>—</td><td style='text-align: center;'>DSU数据整体的数据结构定义:
DSU数据整体结构由N_DSU个长度为N的DSU数据构成(N表示序号1~8的数据长度总和),并增加4字节的整体CRC</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>DSU编号</td><td style='text-align: center;'>NID_DSU</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFFF,0无效</td><td style='text-align: center;'>DSU编号</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属线路编号</td><td style='text-align: center;'>NID_LINE</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~0xFF,0无效</td><td style='text-align: center;'>线路编号值</td></tr><tr><td rowspan="2">3</td><td rowspan="2">DSU下载地址(A、B网)</td><td style='text-align: center;'>M_DSUPAI_D</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;
后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_DSUPBI_D</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;
后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr></table>

---

<div style="text-align: center;">表 19 DSU 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">3</td><td rowspan="2">DSU下载地址(A、B网)</td><td style='text-align: center;'>M_DSUIPA2_D</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_DSUIPB2_D</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr><tr><td rowspan="2">4</td><td rowspan="2">DSU下载网络子网掩码</td><td style='text-align: center;'>M_DSUMASKA1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>A网的子网掩码</td></tr><tr><td style='text-align: center;'>M_DSUMASKB1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK:各字节取值范围:0~255</td><td style='text-align: center;'>B网的子网掩码</td></tr><tr><td rowspan="2">5</td><td rowspan="2">DSU下载网络网络网关</td><td style='text-align: center;'>M_DSUGTWIPA1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>A网的网关</td></tr><tr><td style='text-align: center;'>M_DSUGTWIPB1</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP:各字节取值范围:0~255</td><td style='text-align: center;'>B网的网关</td></tr></table>

---

<div style="text-align: center;">表 19 DSU 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="4">6</td><td rowspan="4">DSU数据校验地址(A、B网)</td><td style='text-align: center;'>M_DSUIPA1_C</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>A网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_DSUIPB1_C</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF</td><td style='text-align: center;'>B网地址1+端口号</td></tr><tr><td style='text-align: center;'>M_DSUIPA2_C</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>A网地址2+端口号</td></tr><tr><td style='text-align: center;'>M_DSUIPB2_C</td><td style='text-align: center;'>4+2</td><td style='text-align: center;'>前4字节为IP:各字节0~255;后2字节表示端口,取值范围:0~0xFFFF;全0表示无此IP端口</td><td style='text-align: center;'>B网地址2+端口号</td></tr></table>

---

<div style="text-align: center;">表 19 DSU 数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td rowspan="2">7</td><td rowspan="2">DSU 数据校验网络子网掩码</td><td style='text-align: center;'>M_DSUMASKA2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK: 各字节取值范围: 0~255</td><td style='text-align: center;'>A 网的子网掩码</td></tr><tr><td style='text-align: center;'>M_DSUMASKB2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>MASK: 各字节取值范围: 0~255</td><td style='text-align: center;'>B 网的子网掩码</td></tr><tr><td rowspan="2">8</td><td rowspan="2">DSU 数据校验网络网络网关</td><td style='text-align: center;'>M_DSUGTWIPA2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP: 各字节取值范围: 0~255</td><td style='text-align: center;'>A 网的网关</td></tr><tr><td style='text-align: center;'>M_DSUGTWIPB2</td><td style='text-align: center;'>4</td><td style='text-align: center;'>IP: 各字节取值范围: 0~255</td><td style='text-align: center;'>B 网的网关</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>CRC 校验</td><td style='text-align: center;'>L_CRC</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>DSU 数据整体 CRC</td></tr></table>

<div style="text-align: center;">表 20 安全通信协议栈数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度（字节）</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>安全通信协议栈数据整体结构</td><td style='text-align: center;'>M_STRUCT_CFG</td><td style='text-align: center;'>N_Type*N+2</td><td style='text-align: center;'>—</td><td style='text-align: center;'>安全通信协议栈数据整体的数据结构定义：安全通信协议栈数据整体结构由N_Type个长度为N的安全通信协议栈数据构成（N表示序号1~11的数据长度总和），并增加2字节的整体CRC</td></tr></table>

---

<div style="text-align: center;">表 20 安全通信协议栈数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>设备类型</td><td style='text-align: center;'>M_Type</td><td style='text-align: center;'>1</td><td style='text-align: center;'>1~7</td><td style='text-align: center;'>1:ZC;
4:ATS;
5:DSU;
6:CI;
2、3、7:预留;
其他非法。
参见5.13.1</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>SAI层Tsyn定时器超时值</td><td style='text-align: center;'>M_SAI_Tsyn</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,单位:ms</td><td style='text-align: center;'>SAI层Tsyn定时器超时值配置值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>SAI层长周期回调的周期数</td><td style='text-align: center;'>M_SAI_Tdelta</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF,单位:周期数</td><td style='text-align: center;'>SAI层长周期回调的周期数配置值</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>SAI层序数号最大差值</td><td style='text-align: center;'>M_SAI_SEQ-NUM</td><td style='text-align: center;'>2</td><td style='text-align: center;'>1~0xFFFF</td><td style='text-align: center;'>SAI层序数号最大差值配置值</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>SAI层EC报警状态值</td><td style='text-align: center;'>M_SAI_ECALMSTATE</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>SAI层EC报警状态值配置值</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>SAI层EC负参数回调值</td><td style='text-align: center;'>M_SAI_EC-MAXNEG</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFFF</td><td style='text-align: center;'>SAI层EC负参数回调值配置值</td></tr></table>

---

<div style="text-align: center;">表 20 安全通信协议栈数据结构（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>SAI层连续错误最大值</td><td style='text-align: center;'>M_SAI_NMAX-ERR</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>SAI层连续错误最大值配置值</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>SAI层更新过程连续错误最大值</td><td style='text-align: center;'>M_SAI_NMAXREF</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF</td><td style='text-align: center;'>SAI层更新过程连续错误最大值配置值</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'>MASL层Test-ab定时器超时值</td><td style='text-align: center;'>M_MASL_Testab</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,单位:ms</td><td style='text-align: center;'>MASL层Testab定时器超时值配置值</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>ALE层Tcon定时器超时值</td><td style='text-align: center;'>M_ALE_Tcon</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFF,单位:ms</td><td style='text-align: center;'>ALE层Tcon定时器超时值配置值</td></tr><tr><td style='text-align: center;'>11</td><td style='text-align: center;'>ALE层TSN检查模式</td><td style='text-align: center;'>M_ALE_TSn</td><td style='text-align: center;'>1</td><td style='text-align: center;'>严格检查模式:000;非严格检查模式:0x01</td><td style='text-align: center;'>ALE层TSN检查模式配置值</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>校验码</td><td style='text-align: center;'>I_CRC</td><td style='text-align: center;'>2</td><td style='text-align: center;'>0~0xFFFF</td><td style='text-align: center;'>16位CRC校验,参见5.13.2</td></tr></table>

---

#### 5.13.1 M Type(设备类型)

安全通信协议栈数据针对不同种类的设备进行配置，电子地图中若存在 ZC、CI、ATS、DSU 设备数据（参见 5.8、5.9、5.10、5.12），则应有相应的安全通信协议栈数据。

#### 5.13.2 L_CRC(CRC 校验)

若安全通信协议栈数据中含有多个种类的设备配置，则 CRC 为针对整个数据结构计算。例如，若安全通信协议栈数据含有 ZC、CI、ATS、DSU 的配置，则数据整体结构见表 21。

<div style="text-align: center;">表 21 安全通信协议栈数据整体结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ZC 配置数据</td></tr><tr><td style='text-align: center;'>CI 配置数据</td></tr><tr><td style='text-align: center;'>ATS 配置数据</td></tr><tr><td style='text-align: center;'>DSU 配置数据</td></tr><tr><td style='text-align: center;'>I_CRC</td></tr></table>

其中，各设备类型的顺序不限制，L_CRC 应根据所有种类设备配置数据的所有数据计算。

## 6 电子地图二进制文件整体数据结构

按照章节5中电子地图元素的排列顺序，依次排列电子地图元素，并在文件末尾添加4字节的32位CRC校验。整体数据结构见表22。

<div style="text-align: center;">表 22 电子地图整体数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>项目</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>线路</td><td rowspan="5">按照章节5中对应元素数据结构，从序号1填写至该元素 CRC（即除序号0“整体数据结构”之外的所有字段）</td></tr><tr><td style='text-align: center;'>轨道区段</td></tr><tr><td style='text-align: center;'>折返区域</td></tr><tr><td style='text-align: center;'>应答器</td></tr><tr><td style='text-align: center;'>信号机</td></tr></table>

---

<div style="text-align: center;">表 22 电子地图整体数据结构(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>项 目</td><td style='text-align: center;'>备 注</td></tr><tr><td style='text-align: center;'>车挡</td><td rowspan="7">按照章节5中对应元素数据结构,从序号1填写至该元素CRC(即除序号0“整体数据结构”之外的所有字段)</td></tr><tr><td style='text-align: center;'>ZC</td></tr><tr><td style='text-align: center;'>CI</td></tr><tr><td style='text-align: center;'>ATS</td></tr><tr><td style='text-align: center;'>MSS</td></tr><tr><td style='text-align: center;'>DSU</td></tr><tr><td style='text-align: center;'>安全通信协议栈</td></tr><tr><td style='text-align: center;'>32位CRC</td><td style='text-align: center;'>电子地图整体CRC</td></tr></table>

由于“线路”元素为定长，安全通信协议栈公用配置数据为定长，且“线路”元素中规定了电子地图文件中“轨道区段”、“折返区域”、“应答器”、“信号机”、“车挡”、“ZC”、“CI”、“ATS”、“MSS”、“DSU”、“全线RSSP-Ⅱ地面设备种类数量”元素的个数，且各元素长度均为定长，故上述电子地图整体数据结构可满足解析需要。

---

附录 A

(规范性附录)

线路关键元素取值范围

线路关键元素取值范围见表 A.1。

<div style="text-align: center;">表 A.1 线路关键元素取值范围</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>取值范围</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>车载电子地图描述对标停车的类型（中间对标及站台终端对标）</td><td style='text-align: center;'>2</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>所属接管ZC、ATS编号的数量</td><td style='text-align: center;'>4</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>一个轨道区段对应的站台ID最大数量</td><td style='text-align: center;'>2</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>风井等效范围半径</td><td style='text-align: center;'>2 m</td></tr></table>

---

中国城市轨道交通协会团体标准  

城市轨道交通 基于通信的列车运行  

控制系统（CBTC）互联互通系统规范  

第3部分：车载电子地图  

T/CAMET 04010.3—2018  

中国铁道出版社有限公司出版发行  

（100054，北京市西城区右安门西街8号）  

公司网址：http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本：880 mm×1230 mm 1/32 印张：2.875 字数：78千  

2019年5月第1版 2019年5月第1次印刷

书号：15113·5658 定价：25.00元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本社发行部联系调换。

发行部电话：路（021）73174，市（010）51873174