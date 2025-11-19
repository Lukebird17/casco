# 中国城市轨道交通协会团体标准

T/CAMET 04011.8—2018

# 城市轨道交通 基于通信的列车运行 控制系统（CBTC）互联互通接口规范 第8部分：车载人机界面

# Urban rail transit — Interface specification for interoperability of communication based train control system Part 8: Onboard man machine interface

2018-09-10 发布

2018-12-31 实施

中国城市轨道交通协会 发布

---

## 目 次

前言 …… VII    
引言 …… IX    
1 范围 …… 1    
2 规范性引用文件 …… 1    
3 术语和缩略语 …… 1    
3.1 术语 …… 2    
3.2 缩略语 …… 3    
4 总体要求描述 …… 3    
5 车载人机界面要求 …… 3    
5.1 总体要求 …… 3    
5.2 主要颜色值定义 …… 5    
5.3 MMI 显示图例要求 …… 6    
5.4 车载 ATP 切除或 ATP 未激活显示 …… 25    
5.5 整体效果图 …… 26    
5.6 司机室按钮、开关、指示灯设置要求 …… 27    
5.7 声音报警 …… 28

---

## 前言

T/CAMET 04011《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

——第1部分：应答器报文；

——第 2 部分: CBTC 系统车地连续通信协议;

——第3部分:车载列车自动保护(ATP)/列车自动运行(ATO)系统与车辆的接口;

——第 4 部分: 区域控制器 (ZC) 间接口;

——第5部分：计算机联锁(CI)间接口；

——第6部分：列车自动监控系统（ATS）间接口；

——第7部分:信号各子系统与维护支持系统(MSS)间接口;

——第8部分：车载人机界面。

本部分是 T/CAMET 04011 的第 8 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、浙江众合科技股份有限公司、株洲中车时代电气股份有限公司。

本部分主要起草人：编写组：张强、夏夕盛、秦雪梅、李紫时、刘鲁鹏、郑伟、李博、吴苏娇、周在福、杨晓荣、张涛。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通接口规范 第 8 部分: 车载人机界面

## 1 范围

T/CAMET 04011 的本部分定义了互联互通中车载人机界面及操作方式，包括车载人机界面的显示示例、主要颜色值定义和司机室按钮、开关、指示灯设置要求等。

本部分适用于国内采用基于通信的列车运行控制(CBTC)系统的新建、更新改造及扩建的城市轨道交通线路建设，用于指导信号系统的系统设计、产品设计、设备招标、工程建设。

## 2 规范性引用文件

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 12758—2004 城市轨道交通信号系统通用技术条件

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

## 3 术语和缩略语

GB/T 12758—2004 和 CJ/T 407—2012 界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

---

### 3.1 术语

#### 3.1.1 

城市轨道交通信号 urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T 12758—2004, 术语与定义 3.1]

#### 3.1.2 

基于通信的列车控制 communication based train control (CBTC)

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的车载和地面处理器而构建的连续式列车自动控制系统。

[CJ/T 407—2012, 定义 3.1.1]

#### 3.1.3 

## 目标速度 target speed

列车运行至前方目标地点应达到的允许速度。

[GB/T 12758—2004, 术语与定义 3.13]

#### 3.1.4 

目标距离 target distance

列车运行至前方日标地点的走行距离。

[GB/T 12758—2004, 术语与定义 3.14]

#### 3.1.5 

安全保护距离 safe protection distance

列车自动防护系统中，列车超速防护实施安全停车控制时，为防止停车位置离散性可能造成的危险，而设置的自预定停车位置至目标地点的安全距离。

[GB/T 12758—2004, 术语与定义 3.15]

#### 3.1.6 

移动授权 movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

---

[CJ/T 407—2012, 定义 3.1.7]

### 3.2 缩略语

AM:列车自动驾驶模式(Automatic Manual Train Operating Mode)

ATC: 列车自动控制 (Automatic Train Control)

ATO:列车自动运行(Automatic Train Operation)

ATP: 列车自动防护(Automatic Train Protection)

ATS:列车自动监控(Automatic Train Supervision)

CBTC: 基于通信的列车控制（Communication Based Train Control）

CM: 列车自动防护模式 (Code Train Operating Mode)

CI: 计算机联锁 (Computer Interlocking)

DCS: 数据通信系统 (Data Communication System)

MMI: 人机接口 (Man Machine Interface)

RGB: RGB 色彩模式工业界的一种颜色标准，通过对红（R）、绿（G）、蓝（B）三个颜色通道的变化及其相互之间的叠加来得到各式各样的颜色（RGB 即是代表红、绿、蓝三个通道的颜色）

RM:限制人工驾驶模式(Restricted Train Operating Mode)

## 4 总体要求描述

本规范对通用性的互联互通车载人机界面进行定义，可根据工程项目具体情况，对人机界面显示内容进行扩展。

## 5 车载人机界面要求

### 5.1 总体要求

车载人机界面是司机与 ATP/ATO 设备交互的接口，一方面用于向司机显示来自 ATP/ATO 设备的信息，另一方面接收司机输入操作。

MMI 显示屏尺寸宜为 12 英寸，分辨率宜为  $ 1024 \times 768 $ （单位：ppi）。本文以 12 英寸和  $ 1024 \times 768 $ （单位：ppi）分辨率为例介绍，若实际项目中屏幕尺寸变化，分辨率及图片、文字大小应等比例缩放。主界面分为 25 个主显示区，如图 1 所示。

---

<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>1区</td><td style='text-align: center;'>8区</td><td rowspan="6" colspan="2">9区</td><td colspan="2">10区</td></tr><tr><td rowspan="5">2区</td><td rowspan="5" colspan="3">3区</td><td style='text-align: center;'>11区</td><td style='text-align: center;'>12区</td></tr><tr><td style='text-align: center;'>13区</td><td style='text-align: center;'>14区</td></tr><tr><td style='text-align: center;'>15区</td><td style='text-align: center;'>16区</td></tr><tr><td style='text-align: center;'>17区</td><td style='text-align: center;'>18区</td></tr><tr><td style='text-align: center;'>19区</td><td style='text-align: center;'>20区</td></tr><tr><td style='text-align: center;'>4区</td><td style='text-align: center;'>5区</td><td style='text-align: center;'>6区</td><td style='text-align: center;'>7区</td><td style='text-align: center;'>21区</td><td style='text-align: center;'>22区</td></tr><tr><td style='text-align: center;'>23区</td><td colspan="3">24区</td><td colspan="2">25区</td></tr></table>

<div style="text-align: center;">图 1 显示屏分区示意图</div>


各个区域的功能和大小分别为（横坐标像素×纵坐标像素）见表1。

<div style="text-align: center;">表 1 各个区域的功能和大小</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>各区域编号</td><td style='text-align: center;'>功能</td><td style='text-align: center;'>横坐标像素×纵坐标像素/ppi</td></tr><tr><td style='text-align: center;'>1区</td><td style='text-align: center;'>超速报警及输出紧急制动显示</td><td style='text-align: center;'>128×95</td></tr><tr><td style='text-align: center;'>2区</td><td style='text-align: center;'>目标速度及目标距离显示</td><td style='text-align: center;'>128×440</td></tr><tr><td style='text-align: center;'>3区</td><td style='text-align: center;'>速度表盘</td><td style='text-align: center;'>542×440</td></tr><tr><td style='text-align: center;'>4区</td><td style='text-align: center;'>牵引制动状态显示</td><td style='text-align: center;'>157×88</td></tr><tr><td style='text-align: center;'>5区</td><td style='text-align: center;'>最高可用驾驶模式显示</td><td style='text-align: center;'>167×88</td></tr><tr><td style='text-align: center;'>6区</td><td style='text-align: center;'>列车完整性显示</td><td style='text-align: center;'>179×88</td></tr><tr><td style='text-align: center;'>7区</td><td style='text-align: center;'>列车头尾设备状态显示</td><td style='text-align: center;'>167×88</td></tr><tr><td style='text-align: center;'>8区</td><td style='text-align: center;'>终点站显示</td><td style='text-align: center;'>295×95</td></tr><tr><td style='text-align: center;'>9区</td><td style='text-align: center;'>下一站显示</td><td style='text-align: center;'>295×95</td></tr><tr><td style='text-align: center;'>10区</td><td style='text-align: center;'>车次显示</td><td style='text-align: center;'>306×95</td></tr></table>

---

<div style="text-align: center;">表 1 各个区域的功能和大小(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>各区域编号</td><td style='text-align: center;'>功能</td><td style='text-align: center;'>横坐标像素×纵坐标像素/ppi</td></tr><tr><td style='text-align: center;'>11区</td><td style='text-align: center;'>跳停扣车显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>12区</td><td style='text-align: center;'>菜单按钮显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>13区</td><td style='text-align: center;'>当前驾驶模式显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>14区</td><td style='text-align: center;'>当前运行等级显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>15区</td><td style='text-align: center;'>折返状态显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>16区</td><td style='text-align: center;'>列车进入停车窗显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>17区</td><td style='text-align: center;'>门状态及门允许命令显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>18区</td><td style='text-align: center;'>发车信息显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>19区</td><td style='text-align: center;'>客室门控制模式显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>20区</td><td style='text-align: center;'>车辆及站台门状态显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>21区</td><td style='text-align: center;'>设备故障显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>22区</td><td style='text-align: center;'>车轴段的转换区显示</td><td style='text-align: center;'>177×88</td></tr><tr><td style='text-align: center;'>23区</td><td style='text-align: center;'>时间显示</td><td style='text-align: center;'>216×145</td></tr><tr><td style='text-align: center;'>24区</td><td style='text-align: center;'>自定义显示</td><td style='text-align: center;'>439×145</td></tr><tr><td style='text-align: center;'>25区</td><td style='text-align: center;'>自定义显示</td><td style='text-align: center;'>369×145</td></tr></table>

### 5.2 主要颜色值定义

在 MMI 显示界面中,不同区域不同条件下,使用不同的颜色进行显示,主要使用的颜色定义推荐值见表 2。

<div style="text-align: center;">表 2 主要颜色值定义推荐值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>颜色</td><td style='text-align: center;'>RGB 值</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>白色</td><td style='text-align: center;'>RGB（255, 255, 255）</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>黑色</td><td style='text-align: center;'>RGB（0, 12, 25）</td></tr></table>

---

<div style="text-align: center;">表 2 主要颜色值定义推荐值(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>颜色</td><td style='text-align: center;'>RGB值</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>红色</td><td style='text-align: center;'>RGB(189,0,0)</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>黄色</td><td style='text-align: center;'>RGB(255,242,0)</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>浅灰色</td><td style='text-align: center;'>RGB(212,212,212)</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>RGB(45,144,51)</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>橙色</td><td style='text-align: center;'>RGB(234,145,0)</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>深蓝色</td><td style='text-align: center;'>RGB(37,151,230)</td></tr></table>

### 5.3 MMI 显示图例要求

#### 5.3.1 1区超速报警及输出紧急制动显示

超速报警及输出紧急制动显示是根据预计超越速度限制的时间及距离，对驾驶员显示警报，示意可能发生的意外状况。初始状态1区显示图标如表3所示。各图片居中显示。

<div style="text-align: center;">表 3 1 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bd878584-ec47-4379-8706-725c4fe57253/markdown_0/imgs/img_in_image_box_192_778_348_889.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A51%3A32Z%2F-1%2F%2Fa27a4284d4d6f0f7b1db0ffbb1912ded215ee3c439fbf0c35ad9377807456811" ></td><td style='text-align: center;'>118×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bd878584-ec47-4379-8706-725c4fe57253/markdown_0/imgs/img_in_image_box_189_935_347_1049.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A51%3A32Z%2F-1%2F%2Ffd5dc49ed873e3a678717f666e08668971506c5346c5af2bd07a9b081ae5aebd" ></td><td style='text-align: center;'>118×83 橙色</td><td style='text-align: center;'>列车当前速度超过 推荐速度，驾驶员宜 施加制动，以防止列 车触发紧急制动</td></tr></table>

---

<div style="text-align: center;">表 3 1 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'></td><td style='text-align: center;'>118×83 红色</td><td style='text-align: center;'>已输出紧急制动</td></tr></table>

#### 5.3.2 2区目标速度及目标距离信息显示

目标速度及目标距离信息是显示到下一限制点的距离及目标速度，两者均受最受限的 ATP 条件决定。

目标距离使用两种方法表示：柱状光带表示法和数字表示法。柱状光带的最大尺寸为 $ 15 \times 400 $ 像素，颜色根据目标速度和目标距离的数值变化，见表4。柱状光带的左侧为坐标系刻度，该坐标系采用对数坐标，颜色为浅灰，其最高端所对应的最远距离为750m，最低端固定。光带正下方为数字表示区，单位为米。字体大小为10磅，颜色为白色。如果目标距离大于750，则柱状光带显示750m，光带正下方为数字按实际距离显示。

<div style="text-align: center;">表 4 柱状光带颜色定义</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">目标速度 (km/h)</td><td colspan="3">目标距离(m)</td></tr><tr><td style='text-align: center;'>s&gt;300</td><td style='text-align: center;'>150≤s≤300</td><td style='text-align: center;'>s&lt;150</td></tr><tr><td style='text-align: center;'>v≥60</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>淡绿色</td></tr><tr><td style='text-align: center;'>25≤v&lt;60</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>黄色</td></tr><tr><td style='text-align: center;'>0&lt;v&gt;淡绿色</td><td style='text-align: center;'>黄色</td><td style='text-align: center;'>黄色</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>v=0</td><td style='text-align: center;'>淡绿色</td><td style='text-align: center;'>黄色</td><td style='text-align: center;'>红色</td></tr></table>

目标速度根据目标距离得出，在目标距离上方以数字形式显示，单位为千米每小时（km/h）。字体大小为16磅，颜色为白色。

---

目标速度及目标距离信息显示如图 2 所示。

<table border=1 style='margin: auto; width: max-content;'>
  <thead><tr><th style='text-align: center;'>项目</th><th style='text-align: center;'>数值</th></tr></thead>
  <tbody>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>750</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>500</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>200</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>100</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>50</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>20</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>10</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>5</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>2</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>1</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>0</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-1</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-2</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-3</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-4</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-5</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-6</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-7</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-8</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-9</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-10</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-11</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-12</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-13</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-14</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-15</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-16</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-17</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-18</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-19</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-20</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-21</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-22</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-23</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-24</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-25</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-26</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-27</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-28</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-29</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-30</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-31</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-32</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-33</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-34</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-35</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-36</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-37</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-38</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-39</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-40</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-41</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-42</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-43</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-44</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-45</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-46</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-47</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-48</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-49</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-50</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-51</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-52</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-53</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-54</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-55</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-56</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-57</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-58</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-59</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-60</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-61</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-62</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-63</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-64</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-65</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-66</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-67</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-68</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-69</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-70</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-71</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-72</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-73</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-74</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-75</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-76</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-77</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-78</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-79</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-80</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-81</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-82</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-83</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-84</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-85</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-86</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-87</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-88</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-89</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-90</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-91</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-92</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-93</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-94</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-95</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-96</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-97</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-98</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-99</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-100</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-101</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-102</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-103</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-104</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-105</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-106</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-107</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-108</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-109</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-110</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-111</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-112</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-113</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-114</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-115</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-116</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-117</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-118</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-119</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-120</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-121</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-122</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-123</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-124</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-125</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-126</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-127</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-128</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-129</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-130</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-131</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-132</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-133</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-134</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-135</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-136</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-137</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-138</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-139</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-140</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-141</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-142</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-143</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-144</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-145</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-146</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-147</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-148</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-149</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-150</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-151</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-152</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-153</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-154</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-155</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-156</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-157</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-158</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-159</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-160</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-161</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-162</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-163</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-164</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-165</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-166</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-167</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-168</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-169</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-170</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-171</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-172</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-173</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-174</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-175</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-176</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-177</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-178</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-179</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-180</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-181</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-182</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-183</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-184</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-185</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-186</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-187</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-188</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-189</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-190</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-191</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-192</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-193</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-194</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-195</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-196</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-197</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-198</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-199</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-200</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-201</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-202</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-203</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-204</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-205</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-206</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-207</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-208</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-209</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-210</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-211</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-212</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-213</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-214</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-215</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-216</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-217</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-218</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-219</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-220</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-221</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-222</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-223</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-224</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-225</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-226</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-227</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-228</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-229</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-230</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-231</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-232</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-233</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-234</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-235</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-236</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-237</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-238</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-239</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-240</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-241</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-242</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-243</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-244</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-245</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-246</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-247</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-248</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-249</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-250</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-251</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-252</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-253</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-254</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-255</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-256</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-257</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-258</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-259</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-260</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-261</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-262</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-263</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-264</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-265</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-266</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-267</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-268</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-269</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-270</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-271</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-272</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-273</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-274</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-275</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-276</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-277</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-278</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-279</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-280</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-281</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-282</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-283</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-284</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-285</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-286</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-287</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-288</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-289</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-290</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-291</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-292</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-293</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-294</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-295</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-296</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-297</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-298</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-299</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-300</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-301</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-302</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-303</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-304</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-305</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-306</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-307</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-308</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-309</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-310</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-311</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-312</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-313</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-314</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-315</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-316</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-317</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-318</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-319</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-320</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-321</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-322</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-323</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-324</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-325</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-326</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-327</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-328</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-329</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-330</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-331</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-332</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-333</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-334</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-335</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-336</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-337</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-338</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-339</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-340</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-341</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-342</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-343</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-344</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-345</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-346</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-347</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-348</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-349</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-350</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-351</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-352</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-353</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-354</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-355</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-356</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-357</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-358</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-359</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-360</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-361</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-362</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-363</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-364</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-365</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-366</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-367</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-368</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-369</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-370</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-371</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-372</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-373</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-374</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-375</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-376</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-377</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-378</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-379</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-380</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-381</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-382</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-383</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-384</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-385</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-386</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-387</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-388</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-389</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-390</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-391</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-392</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-393</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-394</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-395</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-396</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-397</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-398</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-399</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-400</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-401</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-402</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-403</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-404</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-405</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-406</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-407</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-408</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-409</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-410</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-411</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-412</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-413</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-414</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-415</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-416</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-417</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-418</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-419</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-420</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-421</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-422</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-423</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-424</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-425</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-426</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-427</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-428</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-429</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-430</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-431</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-432</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-433</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-434</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-435</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-436</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-437</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-438</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-439</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-440</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-441</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-442</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-443</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-444</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-445</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-446</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-447</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-448</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-449</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-450</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-451</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-452</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-453</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-454</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-455</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-456</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-457</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-458</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-459</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-460</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-461</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-462</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-463</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-464</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-465</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-466</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-467</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-468</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-469</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-470</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-471</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-472</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-473</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-474</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-475</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-476</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-477</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-478</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-479</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-480</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-481</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-482</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-483</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-484</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-485</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-486</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-487</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-488</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-489</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-490</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-491</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-492</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-493</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-494</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-495</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-496</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-497</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-498</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-499</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-500</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-501</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-502</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-503</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-504</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-505</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-506</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-507</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-508</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-509</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-510</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-511</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-512</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-513</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-514</td></tr>
    <tr><td style='text-align: center;'>目标距离</td><td style='text-align: center;'>-515</td></tr>
    <tr><td style='text-align: center;'>目标距离</td></tr>
  </tbody>
</table>

<div style="text-align: center;">图 2 目标速度及目标距离信息</div>


#### 5.3.3 3区速度表盘显示

##### 5.3.3.1 速度表盘

速度表盘的尺寸为 $ 411\ mm \times 411\ mm $ ，中心点坐标为(399,309)。

列车速度采用双备份显示。一种方式是速度表，刻度按照5 km/h进行显示，刻度的颜色为浅灰色，长刻度线的宽度为3像素，长度为28像素。短刻度线的宽度为2像素，长度为15像素。每10 km/h做一个数字标志，数字的颜色为浅灰色，字体大小为13磅。表盘的速度范围可根据工程配置，最大为160 km/h。另一种方式是数字，在速度表的中间显示列车速度值。

沿着度表盘的外边界，显示环形边框，边框的颜色为红色，宽度为3像素。红色边框的半径为204像素。仪表盘从刻度0到最大刻度的扇形弧度为310°。以垂直向上作为0°，-155°的角度显示0 km/h，155°的角度显示最大速度。文字距离中心点的半径为168像素。刻度到刻度值之间为3像素。速度表盘显示如图3所示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9f58c270-2592-4066-b4ca-7d5a75af1382/markdown_0/imgs/img_in_image_box_127_128_662_426.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A03Z%2F-1%2F%2Fa2b9e63b8162cf8e055bf22fe7b96fa58b2b38982b2aefec665fdc5e19818dd2" alt="Image" width="63%" /></div>


<div style="text-align: center;">图 3 A 速度表盘</div>


在速度表盘上以黄色三角形显示推荐速度，三角形的中线与该速度处的半径在一条直线上。该中线通过的顶点朝向速度表的圆心。无推荐速度时，不显示此三角形。此三角形为等边三角形，边长为15像素，如图4所示。

在速度表盘上以红色等边三角形显示紧急制动干预速度，三角形的中线与该速度处的半径在一条直线上，该中线通过的顶点朝向速度表的圆心。此三角形为等边三角形，边长为15像素，如图5所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9f58c270-2592-4066-b4ca-7d5a75af1382/markdown_0/imgs/img_in_image_box_207_719_274_777.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A03Z%2F-1%2F%2Fa6611e1c2bfec29d432966a6b965a7df1d086e7def8af632040e9927caae1660" alt="Image" width="7%" /></div>


<div style="text-align: center;">图 4 推荐速度</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9f58c270-2592-4066-b4ca-7d5a75af1382/markdown_0/imgs/img_in_image_box_513_719_582_777.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A03Z%2F-1%2F%2F4fb943cc63da98ce962f47a526baf213b53eab9a923af97933b4e54f56e0ec40" alt="Image" width="8%" /></div>


<div style="text-align: center;">图 5 紧急制动干预速度</div>


##### 5.3.3.2 数字方式显示的列车速度

列车速度指针由指针和指针始端的圆圈组成，这两部分的颜色均为白色。速度指针的形状如图6所示，指针的长度不应触到速度表盘的刻度条。在指针始端的圆圈中，以数字方式显示当前速度，数字的颜色为白色，字体大小为18像素，圆盘半径41像素，指针半径165像素。列车测速无效通过统一文本信息显示、图形自定义显示。

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b3a51ed1-d04f-4c8c-8a28-9b973d1e4237/markdown_0/imgs/img_in_image_box_348_96_560_424.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A12Z%2F-1%2F%2F1676be961865e7d5c152106a2a7eaafea2c969ae606991d34565817878236c51" alt="Image" width="25%" /></div>


<div style="text-align: center;">图 6 速度指针(单位:mm)</div>


#### 5.3.4 4区牵引制动状态显示

牵引制动状态信息表示在 ATO 模式下牵引和制动情况，如果没有输入信息将显示初始状态，显示图标及对应含义如表 5 所示。

<div style="text-align: center;">表 5 4 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b3a51ed1-d04f-4c8c-8a28-9b973d1e4237/markdown_0/imgs/img_in_image_box_197_766_344_855.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A13Z%2F-1%2F%2F2559d71e56b2be23669c40313e19fb5030f46c6ee8b26b80dce4167aa4c825fe" ></td><td style='text-align: center;'>139×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//b3a51ed1-d04f-4c8c-8a28-9b973d1e4237/markdown_0/imgs/img_in_image_box_197_933_343_1019.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A13Z%2F-1%2F%2F742b9f9b8cadabf9d3a5c174058e91b9b82522a125f90549159ad60b15b5597a" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>牵引状态</td></tr></table>

---

<div style="text-align: center;">表 5 4 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7db60d96-a375-46d3-99c5-bae2eeac26c3/markdown_0/imgs/img_in_image_box_193_231_338_315.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A15Z%2F-1%2F%2F5fd0c6b02d0da27deb49e7b2002a39ba69b3f11f4632cfb639ff8becd78578c1" ></td><td style='text-align: center;'>139×83黑色/浅灰色</td><td style='text-align: center;'>惰行状态</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7db60d96-a375-46d3-99c5-bae2eeac26c3/markdown_0/imgs/img_in_image_box_192_365_338_452.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A15Z%2F-1%2F%2F5341b995ddf8f8a4119f53b5c367b1115602f325706b516bed7f4d9ea05edf97" ></td><td style='text-align: center;'>139×83黑色/浅灰色</td><td style='text-align: center;'>制动状态</td></tr></table>

#### 5.3.5 5区最高可用驾驶模式显示

最高可用驾驶模式信息显示最高的可用模式级别，如果没有输入信息将显示初始状态，显示图标及对应含义如表6所示。

<div style="text-align: center;">表 6 5 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7db60d96-a375-46d3-99c5-bae2eeac26c3/markdown_0/imgs/img_in_image_box_192_731_334_819.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A15Z%2F-1%2F%2F3ccbd9ca084b80d66368614e792c22d938b15878845c62541bb849528c677649" ></td><td style='text-align: center;'>139×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7db60d96-a375-46d3-99c5-bae2eeac26c3/markdown_0/imgs/img_in_image_box_190_850_333_935.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A16Z%2F-1%2F%2F258e6e8b06a63cea1bd14dd1aa85e95dd60baa7e1c1130815c3526eb2ca4f842" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>限制人工驾驶模式</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//7db60d96-a375-46d3-99c5-bae2eeac26c3/markdown_0/imgs/img_in_image_box_189_966_333_1051.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A16Z%2F-1%2F%2Fb8a6e98d3bf45d5df42da2b059159154d732bf5ff90f9edef93b3c3c0352372e" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>点式监督模式</td></tr></table>

---

<div style="text-align: center;">表 6 5 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9fd7aa8e-d247-4c3a-93d6-fcff2a444f50/markdown_0/imgs/img_in_image_box_130_213_282_297.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A19Z%2F-1%2F%2F63b18bf8d0b9a8e2deee7791549a28fe2bedd9394c36f12024fbcd6d6f97c25d" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>连续式监督模式</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9fd7aa8e-d247-4c3a-93d6-fcff2a444f50/markdown_0/imgs/img_in_image_box_130_327_281_410.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A19Z%2F-1%2F%2F31b9f81a094d698d1c0075fe083a27cf06338d5c87dd900006d077c011dde703" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>点式自动驾驶模式</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9fd7aa8e-d247-4c3a-93d6-fcff2a444f50/markdown_0/imgs/img_in_image_box_128_441_282_526.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A19Z%2F-1%2F%2F21439ae5827bb44e543c8e7671140b3d9266faa2a1e651ae259bd3836d391332" ></td><td style='text-align: center;'>139×83 黑色/浅灰色</td><td style='text-align: center;'>连续式自动驾驶模式</td></tr></table>

#### 5.3.6 6 区列车完整性显示

列车完整性信息显示列车的完整性状态,显示图标及对应含义如表7所示。

<div style="text-align: center;">表 7 6 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9fd7aa8e-d247-4c3a-93d6-fcff2a444f50/markdown_0/imgs/img_in_image_box_128_808_321_894.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A19Z%2F-1%2F%2Ffe619204a4d74f82b41ac86874f85798c0ab5b09cfb0681a0faa51b1991e2d62" ></td><td style='text-align: center;'>177×83 黑色/淡绿色</td><td style='text-align: center;'>列车完整性正常</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//9fd7aa8e-d247-4c3a-93d6-fcff2a444f50/markdown_0/imgs/img_in_image_box_126_953_322_1041.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A19Z%2F-1%2F%2Fda41d013781796e2f3f37287dffdde2882a08cbeaa22db8711c1060aa0806221" ></td><td style='text-align: center;'>177×83 黑色/红色</td><td style='text-align: center;'>列车完整性丢失</td></tr></table>

---

#### 5.3.7 7 区列车头尾设备状态显示

该信息表示列车头尾设备的状态，显示图标及对应含义如表8所示。

<div style="text-align: center;">表 8 7 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//98ba42bf-ea40-4b06-bb08-b8615aa30f3a/markdown_0/imgs/img_in_image_box_166_313_261_396.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A22Z%2F-1%2F%2Fb912ecd5f73874e06a019949df03729047f391d774e6096714f9cb949127d25c" ></td><td style='text-align: center;'>94×83黑色/淡绿色/浅灰色/白色</td><td style='text-align: center;'>本端车载ATC设备激活，另一端车载ATC设备待机</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//98ba42bf-ea40-4b06-bb08-b8615aa30f3a/markdown_0/imgs/img_in_image_box_167_428_262_514.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A22Z%2F-1%2F%2Fdf5f5e46e78518e1996f670e10c15f3137e194d17a9a0089e2c6eccf17f42c05" ></td><td style='text-align: center;'>黑色/淡绿色/浅灰色/红色</td><td style='text-align: center;'>本端车载ATC设备激活，另一端车载ATC设备故障</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//98ba42bf-ea40-4b06-bb08-b8615aa30f3a/markdown_0/imgs/img_in_image_box_165_545_262_631.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A22Z%2F-1%2F%2Fce47d99f93a81dacfc3e158379122204872b0a0d54b9438f71fe3940d1bf8a79" ></td><td style='text-align: center;'>黑色/淡绿色/浅灰色/红色</td><td style='text-align: center;'>本端车载ATC设备故障，另一端车载ATC设备激活</td></tr></table>

#### 5.3.8 8区终点站显示

该信息显示列车的终点站，以“终点站”为名，车站名称的形式显示，无输入信息时车站名称显示初始状态。字体大小为18像素，显示1~6个文字站名，深蓝色，左对齐显示。若站名超过6个文字，可通过换行或者缩小字体的方式显示。显示图标及对应含义如表9所示。

<div style="text-align: center;">表 9 8 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>终点站:</td><td style='text-align: center;'>284×85 黑色/深蓝色</td><td style='text-align: center;'>无输入信息时</td></tr></table>

---

<div style="text-align: center;">表 9 8 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>终点站:站台名称</td><td style='text-align: center;'>284×85 黑色/深蓝色</td><td style='text-align: center;'>有输入信息时</td></tr></table>

#### 5.3.9 9区下一站显示

该信息显示列车的下一站，以“下一站：车站名称”的形式显示，无输入信息时车站名称显示初始状态。字体大小为18像素，显示1~6个文字站名，深蓝色，左对齐显示。若站名超过6个文字，可通过换行或者缩小字体的方式显示。显示图标及对应含义如表10所示。

<div style="text-align: center;">表 10 9 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>下一站:</td><td style='text-align: center;'>284×85 黑色/深蓝色</td><td style='text-align: center;'>无输入信息时</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>下一站:站台名称</td><td style='text-align: center;'>284×85 黑色/深蓝色</td><td style='text-align: center;'>有输入信息时</td></tr></table>

#### 5.3.10 10区车次显示

该信息显示列车的车次号，以 TXXXXXXX 的形式显示，X 为数字 1~9，显示 1~5 位数字。无输入信息时车次号显示初始状态。字体大小为 18 像素，颜色为浅灰色，左对齐显示。若车次号超过 5 个数字，可通过

---

换行或者缩小字体的方式显示。显示图标及对应含义如表11所示。

<div style="text-align: center;">表 11 10 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>298×85黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>T53214</td><td style='text-align: center;'>298×85黑色/浅灰色</td><td style='text-align: center;'>车次号显示</td></tr></table>

#### 5.3.11 11区跳停、扣车显示

该信息表示列车当前的跳停、扣车状态，根据 ATS 的命令显示。显示图标及对应含义如表 12 所示。

<div style="text-align: center;">表 12 11 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5d9d4036-901f-46d6-8f85-8f4c08febeaf/markdown_0/imgs/img_in_image_box_175_737_378_834.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A28Z%2F-1%2F%2F326bfc4ae3c67e9eac015f0acc02e6d2a55591155ff6e3ec12956601f190fbe8" ></td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5d9d4036-901f-46d6-8f85-8f4c08febeaf/markdown_0/imgs/img_in_image_box_172_856_379_957.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A28Z%2F-1%2F%2F1613d56558ceeb25187b42e3aea72c0873a86b5e84984fd3f88041ff27a7e4ff" ></td><td style='text-align: center;'>177×83黑色/浅灰色/黄色</td><td style='text-align: center;'>跳停</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5d9d4036-901f-46d6-8f85-8f4c08febeaf/markdown_0/imgs/img_in_image_box_170_985_379_1084.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A28Z%2F-1%2F%2Fbdff24eda22d0ffd1d44c7a7c54758fad00095345fe9883189205b5abceaa860" ></td><td style='text-align: center;'>177×83黑色/浅灰色/红色</td><td style='text-align: center;'>扣车</td></tr></table>

---

#### 5.3.12 12 区菜单按钮显示

按下该按钮后，将激活弹出菜单。弹出菜单内容各家不作统一处理。显示图标及对应含义如表13所示。

<div style="text-align: center;">表 13 12 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a7a1cf4f-f5af-43de-b7a8-37d1f093db6e/markdown_0/imgs/img_in_image_box_140_353_358_461.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A31Z%2F-1%2F%2F9794834cef2ff872f3f3e31a18da3e5c08d56bd7c4778de13e5aca942c7f9923" ></td><td style='text-align: center;'>177×83 黑色/白色</td><td style='text-align: center;'>菜单设置按钮可用</td></tr></table>

#### 5.3.13 13 区当前驾驶模式显示

该信息表示列车当前的驾驶模式，如果没有输入信息则显示初始状态。显示图标及对应含义如表14所示。

<div style="text-align: center;">表 14 13 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//a7a1cf4f-f5af-43de-b7a8-37d1f093db6e/markdown_0/imgs/img_in_image_box_151_730_336_819.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A31Z%2F-1%2F%2F333daf3d33ec36bb428b1e925f27ffa9e16a050077b10cdeba26b9d3e11457c1" ></td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>AM</td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>ATO模式</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>监督模式</td></tr></table>

---

<div style="text-align: center;">表 14 13 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8bdd4d94-5fae-4445-bfdd-a7bfb7037d2e/markdown_0/imgs/img_in_image_box_188_222_368_307.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A34Z%2F-1%2F%2F29933ccece617a1c01f13c416609cecc019a5f44560a8384770936d6c18fbfe6" ></td><td style='text-align: center;'>177×83 黑色/浅灰色</td><td style='text-align: center;'>受限模式</td></tr></table>

#### 5.3.14 14区当前运行等级显示

该信息表示列车当前的运行等级,如果没有输入信息则显示初始状态。显示图标及对应含义如表 15 所示。

<div style="text-align: center;">表 15.014 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>图</td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8bdd4d94-5fae-4445-bfdd-a7bfb7037d2e/markdown_0/imgs/img_in_image_box_182_692_356_776.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A35Z%2F-1%2F%2F0e300a0b96bcb0f6a4e9e5c593e3534145f70132024e93d18251eec7ecc0a509" ></td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>联锁控制级别</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8bdd4d94-5fae-4445-bfdd-a7bfb7037d2e/markdown_0/imgs/img_in_image_box_179_818_355_900.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A35Z%2F-1%2F%2F6b6be900cf9bd87726a926e5e6d4d504b28978dac84d33c303b339cb262c8c3c" ></td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>点式列车控制级别</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8bdd4d94-5fae-4445-bfdd-a7bfb7037d2e/markdown_0/imgs/img_in_image_box_172_943_352_1029.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A35Z%2F-1%2F%2F95fa5a2e705ba64df35486857e00fdd8f4f1d3dff9d82638bb9c9d39facee864" ></td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>连续式列车控制级别</td></tr></table>

---

#### 5.3.15 15区折返状态显示

该信息显示列车折返的状态,无输入信息时显示初始状态。显示图标及对应含义如表16所示。

<div style="text-align: center;">表 16 15 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0c808c08-21b9-4c00-a022-72545ce17161/markdown_0/imgs/img_in_image_box_123_348_309_433.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A38Z%2F-1%2F%2F7dfd9980a027146c861b70ec7ae37b3a56d62a3c46bf3006a121521f55a46608" ></td><td style='text-align: center;'>177×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0c808c08-21b9-4c00-a022-72545ce17161/markdown_0/imgs/img_in_image_box_120_472_308_558.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A38Z%2F-1%2F%2F8f2737343bafea0fa9ed5ab9a783d8db01be98a40b655c9251e14fa721a4b070" ></td><td style='text-align: center;'>177×83 黑色/淡绿色</td><td style='text-align: center;'>满足折返条件后,闪烁,闪烁的频率推荐值为1 Hz</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0c808c08-21b9-4c00-a022-72545ce17161/markdown_0/imgs/img_in_image_box_120_598_306_683.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A38Z%2F-1%2F%2Fcb0993af83bef8e83345f9cff4783b66aff938497875761666d6600ae102ca68" ></td><td style='text-align: center;'>177×83 黑色/黄色</td><td style='text-align: center;'>常亮,表示折返激活</td></tr></table>

#### 5.3.16 16 区列车进入停车窗显示

该信息显示列车在站内停车的情况，无输入信息时显示初始状态。显示图标及对应含义如表17所示。

<div style="text-align: center;">表 17 16 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0c808c08-21b9-4c00-a022-72545ce17161/markdown_0/imgs/img_in_image_box_127_966_315_1054.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A38Z%2F-1%2F%2Fbdd662cd58c29f219d3db4742463e79c0fd4e9426d443b309d83e8a105d7514f" ></td><td style='text-align: center;'>177×83 黑色</td><td style='text-align: center;'>初始状态</td></tr></table>

---

<div style="text-align: center;">表 17 16 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d957e08-905d-4bfa-ba13-1c2932df685e/markdown_0/imgs/img_in_image_box_172_234_347_317.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A44Z%2F-1%2F%2F4d698c4a7e8a02d009c615232043783faa1d2ae66820507bf61f63c13a2ef877" ></td><td style='text-align: center;'>177×83 黑色/红色</td><td style='text-align: center;'>列车进入停车区域但 未进入停车窗</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d957e08-905d-4bfa-ba13-1c2932df685e/markdown_0/imgs/img_in_image_box_172_352_351_434.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A44Z%2F-1%2F%2F9b1bac6953d616607a1802bf28cc5a45275f061e6e498aa327739ead38bb3bf4" ></td><td style='text-align: center;'>177×83 黑色/淡绿色</td><td style='text-align: center;'>列车进入停车区域且 进入停车窗</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d957e08-905d-4bfa-ba13-1c2932df685e/markdown_0/imgs/img_in_image_box_172_471_352_556.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A44Z%2F-1%2F%2F9746bdf993fe0680ca1f626e0919ff6353ba1ef61b670e3473de5b22b435bc16" ></td><td style='text-align: center;'>177×83 黑色/黄色</td><td style='text-align: center;'>列车位于退行激活窗</td></tr></table>

#### 5.3.17 17 区门状态及门允许命令显示

该信息显示门状态及门允许命令，无输入信息时显示初始状态。6、7、8、9级别相同，优先级最高；3、4、5级别相同，优先级次之；2优先级最低（可选，根据工程需求配置）。显示图标及对应含义如表18所示。

<div style="text-align: center;">表 18 17 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d957e08-905d-4bfa-ba13-1c2932df685e/markdown_0/imgs/img_in_image_box_161_863_349_954.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A44Z%2F-1%2F%2F5063ef48e83da767d141a3b1a4f0ffe3939cd3147eb9e58a48cbb6869faa440a" ></td><td style='text-align: center;'>177×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//8d957e08-905d-4bfa-ba13-1c2932df685e/markdown_0/imgs/img_in_image_box_158_987_347_1077.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A45Z%2F-1%2F%2F6ed2737d6e567dc6450f044eb393fedd1e27c2cf4937fdf1b8f188865f604e7b" ></td><td style='text-align: center;'>177×83 黑色/红色/浅灰色</td><td style='text-align: center;'>强制门允许</td></tr></table>

---

<div style="text-align: center;">表 18 17 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_108_234_312_315.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A47Z%2F-1%2F%2F9eaa93c01b77af26592342acd5f8b8858f8762e3888e8bf29781fc928390e9bb" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>允许左右两侧车门同时开启</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_104_349_311_434.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A47Z%2F-1%2F%2F26734123431aee9b947927e1d603cb0fe040d26d569b1d3783b5e2d47d1eb1fa" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>允许左侧车门开启</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_102_471_310_555.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A48Z%2F-1%2F%2F58256986657e2039920f3a317fb5f1775b393d290a4545085415b1f944a46561" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>允许右侧车门开启</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_99_593_310_678.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A48Z%2F-1%2F%2F2ea6e5787c02e8256d7d7fe68b519f3e1ff09ecb446cfac4626c8384c60f07db" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>左侧车门打开</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_101_714_310_802.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A48Z%2F-1%2F%2F52fa58451db10c3be573150ebf55bc6f21764eb11ac7027208f9017ea6d1860a" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>右侧车门打开</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_101_842_311_927.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A48Z%2F-1%2F%2Fb797903f3e7b2300e7dee23b87a97a4a9d4cd3c93f18d1bb7e35ded4d0d384af" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>左右侧车门均打开</td></tr><tr><td style='text-align: center;'>9</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//c905f766-4d8a-4899-b629-a15a0841cd1c/markdown_0/imgs/img_in_image_box_102_971_314_1059.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A48Z%2F-1%2F%2F8c53d11c8af31c2e4dbaec7185b04d9edc2f78582afab93e0ef1e99fd7ee0cf1" ></td><td style='text-align: center;'>177×83黑色/黄色/浅灰色</td><td style='text-align: center;'>无门允许情况下车门打开</td></tr></table>

---

#### 5.3.18 18 区发车信息显示

该信息显示发车提示信息,无输入信息时显示初始状态。显示图标及对应含义如表19所示。

<div style="text-align: center;">表 19 18 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//cc478687-c153-43cb-ae87-0b4c7f0634bc/markdown_0/imgs/img_in_image_box_181_344_361_430.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A51Z%2F-1%2F%2F3d9b9f9d4452a695a445b51aa47402be675fd43107d767f9f98e899650f45229" ></td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>有列车发车请求时</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>177×83黑色/浅灰色/蓝色</td><td style='text-align: center;'>177×83黑色/浅灰色/蓝色</td><td style='text-align: center;'>关车门提示</td></tr></table>

#### 5.3.19 19 区客室门控制模式显示

该信息显示客室门的控制模式,无输入信息时显示初始状态。显示图标及对应含义如表20所示。

<div style="text-align: center;">表 20 19 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>177×83 黑色</td><td style='text-align: center;'>初始状态</td></tr></table>

---

<div style="text-align: center;">表 20 19 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5216b960-4658-4c40-8e6c-a60580bbf252/markdown_0/imgs/img_in_image_box_130_229_315_312.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A54Z%2F-1%2F%2F60d06b74e452ae1a6a8d03cd3065e7731d812a205275059aa55ef99600967b88" ></td><td style='text-align: center;'>177×83 黑色/浅灰色</td><td style='text-align: center;'>人工开门,人工关门</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5216b960-4658-4c40-8e6c-a60580bbf252/markdown_0/imgs/img_in_image_box_127_349_314_433.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A54Z%2F-1%2F%2Fa97607a6ff0bf79dbd406efe0e053945a958e385c0beacdcf4dc0b59143c6592" ></td><td style='text-align: center;'>177×83 黑色/浅灰色</td><td style='text-align: center;'>自动开门,人工关门</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5216b960-4658-4c40-8e6c-a60580bbf252/markdown_0/imgs/img_in_image_box_124_467_313_554.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A54Z%2F-1%2F%2F828453cb8341af7a99b1ea8cf2170d8ef6e5258aa45f95dd80e0e0f4da341766" ></td><td style='text-align: center;'>177×83 黑色/浅灰色</td><td style='text-align: center;'>自动开门,自动关门</td></tr></table>

#### 5.3.20 20区车辆及站台门状态显示

该信息显示车辆空转/打滑及站台门的状态，无输入信息时显示初始状态。列车车轮打滑优先级最高，站台门未关闭次之。显示图标及对应含义如表21所示。

<div style="text-align: center;">表 21 20 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5216b960-4658-4c40-8e6c-a60580bbf252/markdown_0/imgs/img_in_image_box_121_864_313_951.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A54Z%2F-1%2F%2F12c6cd64e14c5249ab906ef357646c171fbcd18f23273122f93b199cfa105351" ></td><td style='text-align: center;'>177×83 黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//5216b960-4658-4c40-8e6c-a60580bbf252/markdown_0/imgs/img_in_image_box_119_981_314_1074.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A54Z%2F-1%2F%2Fcaf9f5ea601b06fe47829c23406393ecc296326c9e89379d973d07d1c4e473ad" ></td><td style='text-align: center;'>177×83 黑色/红色</td><td style='text-align: center;'>车轮空转/打滑</td></tr></table>

---

<div style="text-align: center;">表 21 20 区的显示图标(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm) 颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//00712f5e-8704-4f46-acdb-02a087a76fe0/markdown_0/imgs/img_in_image_box_172_232_351_318.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A58Z%2F-1%2F%2Fc406a589359bddf0ac3549305cd3a94a107d5b2a63614ef39b7cb62d95df268f" ></td><td style='text-align: center;'>177×83 黑色/黄色</td><td style='text-align: center;'>站台门未关闭</td></tr></table>

#### 5.3.21 21 区设备故障显示

该信息显示发生的故障情况，无输入信息时显示初始状态。ATP 故障优先级最高，ATO 故障优先级次之，RAD 故障优先级最低。显示图标及对应含义如表 22 所示。除下表介绍图标外，厂商可自定义图标显示。

<div style="text-align: center;">表 22 21 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//00712f5e-8704-4f46-acdb-02a087a76fe0/markdown_0/imgs/img_in_image_box_165_606_343_688.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A58Z%2F-1%2F%2Fce06e97a847c6a5e2d9b9960c042260ffc2edd1d203b42072d94c0952d3f15a6" ></td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//00712f5e-8704-4f46-acdb-02a087a76fe0/markdown_0/imgs/img_in_image_box_164_722_342_805.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A58Z%2F-1%2F%2F1a79223d0b9f7331c42785d83ca76794d0dd1682a610ccf2ef19aa7cfbef1d8c" ></td><td style='text-align: center;'>177×83黑色/浅灰色/红色</td><td style='text-align: center;'>无线设备通信故障时显示</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//00712f5e-8704-4f46-acdb-02a087a76fe0/markdown_0/imgs/img_in_image_box_161_841_342_923.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A58Z%2F-1%2F%2Ff4ce11a63a4209db5df60665bff7479b0d5a0cfcceace8c73479f8f2210a5faa" ></td><td style='text-align: center;'>177×83黑色/浅灰色/红色</td><td style='text-align: center;'>ATP故障时显示</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//00712f5e-8704-4f46-acdb-02a087a76fe0/markdown_0/imgs/img_in_image_box_158_960_340_1046.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A52%3A58Z%2F-1%2F%2F3a77c22e568504e4bdece0bea1ad345132b266f9e3380ccfbfe80c1636002efd" ></td><td style='text-align: center;'>177×83黑色/浅灰色/红色</td><td style='text-align: center;'>若为单系ATO,故障时显示;若为冗余ATO,两系均故障时显示</td></tr></table>

---

#### 5.3.22 22 区车辆段的转换区显示

该信息显示车辆段信息,无输入信息时显示初始状态。显示图标及对应含义如表23所示。

<div style="text-align: center;">表 23 22 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//deb52f05-23da-4688-a320-e93d4929d6ab/markdown_0/imgs/img_in_image_box_103_343_303_429.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A01Z%2F-1%2F%2Fe7f753af0e4c93300c4eaa44283391f4773a696ab2d19c64613feea90ffa515b" ></td><td style='text-align: center;'>177×83黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//deb52f05-23da-4688-a320-e93d4929d6ab/markdown_0/imgs/img_in_image_box_99_469_300_553.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A02Z%2F-1%2F%2F2a1d6a1c77025dad98f52fd7d7204ce381f49fb6cb86bf7f581533096e493394" ></td><td style='text-align: center;'>177×83黑色/浅灰色/黄色</td><td style='text-align: center;'>列车进入车辆段</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//deb52f05-23da-4688-a320-e93d4929d6ab/markdown_0/imgs/img_in_image_box_95_596_297_681.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A02Z%2F-1%2F%2F9ef2843d95d8db10c0dd79be0c3b2b03cb242d852e2a06e68c9c7657ee426e9b" ></td><td style='text-align: center;'>177×83黑色/浅灰色/淡绿色</td><td style='text-align: center;'>列车进入库线,无自动车辆段时不显示</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//deb52f05-23da-4688-a320-e93d4929d6ab/markdown_0/imgs/img_in_image_box_93_721_296_806.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A02Z%2F-1%2F%2Fcb78822d1de71db76530225bcff3ee0e45d5a541d8a1dbcc639c384b78de1648" ></td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>列车丢失定位或在车辆段内行驶</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//deb52f05-23da-4688-a320-e93d4929d6ab/markdown_0/imgs/img_in_image_box_93_846_294_930.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A02Z%2F-1%2F%2Fe4ede3c3e53850a14fe862a8e16bead6f9670b17388dc728edb62a462c127eff" ></td><td style='text-align: center;'>177×83黑色/浅灰色</td><td style='text-align: center;'>开口模式下,司机已确认前方信号开放</td></tr></table>

#### 5.3.23 23 区时间显示

该信息显示系统时间,无输入信息时显示初始状态。字体大小为21像素,居中显示。显示图标及对应含义如表24所示。

---

<div style="text-align: center;">表 24 23 区的显示图标</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图 标</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//bdabf10e-e051-4eff-8ad1-842599a8675c/markdown_0/imgs/img_in_image_box_173_235_413_297.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A07Z%2F-1%2F%2F1aaf3003f82402d25e43a6591a2a4bad17f061a07da8d8b727b6cb75e1cbff55" ></td><td style='text-align: center;'>211×133黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>16:06:33</td><td style='text-align: center;'>211×133黑色/浅灰色</td><td style='text-align: center;'>系统时间</td></tr></table>

#### 5.3.24 自定义 24 区确认信息显示

该信息显示要求驾驶员确认的信息或者提示信息，由各厂商自定义，无输入信息时显示初始状态。显示图标及对应含义如表 25 所示。

表 25 24 区的显示图标


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>图</td><td style='text-align: center;'>尺寸(mm×mm)颜色</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'></td><td style='text-align: center;'>439×133黑色</td><td style='text-align: center;'>初始状态</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>请确认前方信号开放</td><td style='text-align: center;'>439×133黑色/白色/黄色</td><td style='text-align: center;'>示例</td></tr></table>

#### 5.3.25 自定义 25 区文字或图标信息显示

文字或图标信息显示区域，由各厂商自定义。

### 5.4 车载 ATP 切除或 ATP 未激活显示

当前 ATP 切除或未激活时，显示黑屏，同时在屏幕中心显示时间。

---

显示时间的文字字体大小为 62 像素，颜色为浅灰色。如图 7 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0e20d746-2a1e-44b3-8ea5-93138f56149b/markdown_0/imgs/img_in_image_box_289_150_537_337.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A11Z%2F-1%2F%2F9f562eac05ee2428cf537103d6680a7331f9271ac85ac39ca4334168ab35f671" alt="Image" width="29%" /></div>


<div style="text-align: center;">图 7 黑屏显示示意图</div>


### 5.5 整体效果图

5.4 中图标按照分区显示在尺寸为 12 英寸、分辨率为  $ 1024 \times 768 $  的 MMI 显示屏后，整体效果图如图 8 所示。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//0e20d746-2a1e-44b3-8ea5-93138f56149b/markdown_0/imgs/img_in_image_box_10_531_760_1070.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T15%3A53%3A11Z%2F-1%2F%2F6c0a1585b089e9bd3e647d28162ae87904fc805ca41ea0a3b7201568f1211c1b" alt="Image" width="89%" /></div>


<div style="text-align: center;">图 8 整体效果图</div>

---

### 5.6 司机室按钮、开关、指示灯设置要求

为了配合完成第 5.4 条 MMI 界面显示信息设置或确认，在司机室应配置以下按钮、开关和指示灯。

#### 5.6.1 按钮、开关、指示灯布置

司机室按钮、开关、指示灯布置区域如表26所示。

<div style="text-align: center;">表 26 按钮、开关、指示灯布置</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>名称</td><td style='text-align: center;'>相关显示区</td><td style='text-align: center;'>备注</td></tr><tr><td style='text-align: center;'>1</td><td style='text-align: center;'>强制门允许按钮</td><td style='text-align: center;'>17区,门状态及门允许命令显示</td><td style='text-align: center;'>自复式按钮(可选,根据工程需求)</td></tr><tr><td style='text-align: center;'>2</td><td style='text-align: center;'>ATO启动按钮</td><td style='text-align: center;'>13区,当前驾驶模式显示;14区,当前运行等级显示</td><td style='text-align: center;'>自复式指示灯按钮</td></tr><tr><td style='text-align: center;'>3</td><td style='text-align: center;'>驾驶模式降级按钮</td><td style='text-align: center;'>5区,最高可用驾驶模式显示</td><td style='text-align: center;'>自复式指示灯按钮</td></tr><tr><td style='text-align: center;'>4</td><td style='text-align: center;'>驾驶模式升级按钮</td><td style='text-align: center;'>5区,最高可用驾驶模式显示</td><td style='text-align: center;'>自复式指示灯按钮</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>确认按钮</td><td style='text-align: center;'>24区,确认信息显示22区,车辆段的转换区显示</td><td style='text-align: center;'>自复式指示灯按钮</td></tr><tr><td style='text-align: center;'>6</td><td style='text-align: center;'>自动折返按钮</td><td style='text-align: center;'>15区,折返状态显示</td><td style='text-align: center;'>自复式指示灯按钮</td></tr><tr><td style='text-align: center;'>7</td><td style='text-align: center;'>门模式开关</td><td style='text-align: center;'>19区,客室门控制模式显示</td><td style='text-align: center;'>旋转开关</td></tr><tr><td style='text-align: center;'>8</td><td style='text-align: center;'>ATP切除开关</td><td style='text-align: center;'>5.5节,当前端车载ATP切除或ATP未激活显示</td><td style='text-align: center;'>旋转开关</td></tr></table>

#### 5.6.2 功能介绍

##### 5.6.2.1 强制门允许按钮

按下该按钮后，可强制输出门使能信号，同时在17区显示强制门允许图标。车门打开后，在17区显示门使能和门打开图标。根据工程需求设置。

---

##### 5.6.2.2 ATO 启动按钮

满足 ATO 启动条件时,两个按钮指示灯同时闪烁,闪烁的频率推荐值为 1 Hz;同时按下两个按钮后,ATO 启动指示灯常亮。

##### 5.6.2.3 驾驶模式升级按钮

实现对预选模式升级选择，每按下一次在当前预选模式基础上升一挡，同时在5区显示当前选择的最高可用驾驶模式。选择完毕后，应按确认按钮（序号5）进行确认，确认后当前的最高可用驾驶模式才可生效。

##### 5.6.2.4 驾驶模式降级按钮

实现对预选模式降级选择，每按下一次在当前预选模式基础上降一挡，同时在5区显示当前选择的最高可用驾驶模式。选择完毕后，应按确认按钮（序号5）进行确认，确认后当前的最高可用驾驶模式才可生效。

##### 5.6.2.5 确认按钮

该按钮对24区弹出的待司机确认信息进行确认，司机按下该按钮后，24区原有提示信息消失。同时，该按钮用于对驾驶模式降级按钮和驾驶模式升级按钮设置的最高预设驾驶模式等信息进行确认。

##### 5.6.2.6 自动折返按钮

该按钮对折返过程中司机的操作进行提示和确认，与15区图标显示对应。

##### 5.6.2.7 门模式开关

该开关用于选择列车门控模式，具有 MM、AM 和 AA 三种挡位，与 19 区客室门控制模式显示的三种模式图标对应。

##### 5.6.2.8 ATP 切除开关

该开关用于切除 ATP，当 ATP 切除后，MMI 显示 5.5 条的黑屏状态。

### 5.7 声音报警

当列车超过推荐速度等特定场景下（包括但不限于），MMI 应发出“滴、滴……”报警声（报警持续时间在工程中统一）。

---

# 中国城市轨道交通协会团体标准   城市轨道交通 基于通信的列车运行   控制系统(CBTC)互联互通接口规范   第8部分:车载人机界面   T/CAMET 04011.8—2018

中国铁道出版社有限公司出版发行  

(100054, 北京市西城区右安门西街 8 号)  

公司网址: http://www.tdpress.com  

北京铭成印刷有限公司印刷  

开本: 880 mm × 1230 mm 1/32 印张: 1.25 字数: 31 千  

2019 年 5 月第 1 版 2019 年 5 月第 1 次印刷

书号：15113·5734 定价：15.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。

发行部电话：路（021）73174，市（010）51873174