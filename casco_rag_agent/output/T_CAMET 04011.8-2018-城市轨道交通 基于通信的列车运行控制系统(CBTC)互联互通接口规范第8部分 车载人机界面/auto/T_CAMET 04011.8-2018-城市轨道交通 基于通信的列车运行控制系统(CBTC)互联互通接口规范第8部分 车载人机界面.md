# 中国城市轨道交通协会团体标准

T/CAMET 04011.8—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范

# 第8部分：车载人机界面

Urban rail transit— Interface specification for interoperability of communication based train control system Part 8: Onboard man machine interface

# 目 次

前言  
引言 IX  
1范围 1  
2规范性引用文件 1  
3 术语和缩略语 1  
3.1 术语… 2  
3.2缩略语 3  
4总体要求描述 3  
5车载人机界面要求 3  
5.1 总体要求… 3  
5.2主要颜色值定义 5  
5.3 MMI显示图例要求 6  
5.4车载ATP切除或ATP未激活显示 25  
5.5 整体效果图… 26  
5.6司机室按钮、开关、指示灯设置要求. 27  
5.7声音报警 28

# 前 言

T/CAMET04011《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》分为以下八个部分：

第1部分：应答器报文；  
第2部分：CBTC系统车地连续通信协议；  
-第3部分：车载列车自动保护（ATP）/列车自动运行（ATO）系统与车辆的接口；  
第4部分：区域控制器（ZC）间接口；  
第5部分：计算机联锁（CI）间接口；  
-第6部分：列车自动监控系统（ATS）间接口；  
第7部分：信号各子系统与维护支持系统（MSS）间接口；  
第8部分：车载人机界面。

本部分是T/CAMET04011的第8部分。

本部分按照GB/T1.1—2009给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、中国铁道科学研究院集团有限公司通信信号研究所、浙江众合科技股份有限公司、株洲中车时代电气股份有限公司。

本部分主要起草人：编写组：张强、夏夕盛、秦雪梅、李紫时、刘鲁鹏、郑伟、李博、吴苏娇、周在福、杨晓荣、张涛。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、王道敏、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、朱东飞、肖利君、张守芝、刘新平。

# 引 言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系统规范》城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范》城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

# 城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范

# 第8部分：车载人机界面

# 1范围

T/CAMET04011的本部分定义了互联互通中车载人机界面及操作关、指示灯设置要求等

本部分适用于国 用基于通信的列车运 制（CBTC）系统的新建、更新改造及扩建的城市轨道交通线路建设，指导信号系统的系统设计、产品设计、设备招标程建设。

# 2规范性引用文件

件，下文对于本道你。凡是注期的文版本（包括所有的修改单）适用于本部分。

GB/T12758—2004城市轨道交通信号系统通用技术条件

GB50157—2013 地铁设计规范

CJ/T407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

# 3术语和缩略语

GB/T12758—2004和CJ/T4072012界定的及下列术语和缩略语适用于本部分。为了便于使用，以下重复列出了其中的主要相关术语。

# 3.1术语

3.1.1

城市轨道交通信号urban rail transit signal

应用于城市轨道交通系统中，人工或自动实现行车指挥和列车运行控制、安全间隔控制技术的总称。

[GB/T12758—2004，术语与定义3.1]

3.1.2

基于通信的列车控制communication based train control（CBTC）

通过不依赖轨旁列车占用检测设备的列车主动定位技术、连续车-地双向数据通信技术以及能够执行安全功能的乍载利地面处理器而构建的连续式列车自动控制系统。

[CJ/T407—2012，定义3.1.1]

# 3.1.3

目标速度target speed列车运行至前方目标地点应达到的允许速度。[GB/T12758—2004，术语与定义3.13]

3.1.4

目标距离target distance 列车运行至前方日标地点的走行距离。 [GB/T12758—2004，术语与定义3.14]

# 3.1.5

安全保护距离safe protection distance

列车白动防护系统中，列车超速防护实施安全停车控制时，为防止停车位置离散性可能造成的危险，而设置的自预定停车位置至日标地点的安全距离。

[GB/T12758—2004,术语与定义3.15]

3.1.6

移动授权movement authority

列车沿给定的行驶方向进入并在某一特定轨道区段内行车的许可。

[CJ/T407—2012，定义3.1.7]

# 3.2缩略语

AM：列车自动驾驶模式（Automatic Manual TrainOperatingMode）ATC：列车自动控制（Automatic Train Control）ATO：列车自动运行（Automatic Train Operation）ATP：列车自动防护（AutomaticTrain Protection）ATS：列车自动监控（Automatic Train Supervision）CBTC：基于通信的列车控制（CommunicationBased Train Control）CM:列车自动防护模式（Code TrainOperating Mode）CI：计算机联锁（Computer Interlocking）DCS:数据通信系统(Data Communication System）MMI:人机接口（Man Machine Interface）RGB：RGB色彩模式工业界的-种颜色标准，通过对红（R）、绿（G）、蓝（B）三个颜色通道的变化及其相互之间的叠加来得到各式各样的颜色（RGB即是代表红、绿、蓝三个通道的颜色）

RM：限制人工驾驶模式（Restricted Train Operating Mode）

# 4总体要求描述

本规范对通用性的互联互通车载人机界面进行定义，可根据工程项目具体情况，对人机界面显示内容进行扩展。

# 5车载人机界面要求

# 5.1 总体要求

车载人机界面是司机与ATP/ATO设备交互的接口，一方面用于向司机显示来自ATP/ATO设备的信息，另一方面接收司机输入操作。

MMI显示屏尺寸宜为12英寸，分辨率宜为 $1 \ 0 2 4 \times 7 6 8$ (单位：ppi)。本文以12英寸和 $1 \ 0 2 4 \times 7 6 8$ （单位：ppi）分辨率为例介绍，若实际项目中屏幕尺寸变化，分辨率及图片、文字大小应等比例缩放。主界面分为25个主显示区，如图1所示。

![](images/47127cbe0d3dc60b1e23fee7723d57fc1ce1090b5ba25e69cd34abf0c5d71735.jpg)  
图1显示屏分区示意图

各个区域的功能和大小分别为（横坐标像素 $\times$ 纵坐标像素）见表1。

表1各个区域的功能和大小  

<table><tr><td colspan="1" rowspan="1">各区域编号</td><td colspan="1" rowspan="1">功 能</td><td colspan="1" rowspan="1">横坐标像素×纵坐标像素/ppi</td></tr><tr><td colspan="1" rowspan="1">1区</td><td colspan="1" rowspan="1">超速报警及输出紧急制动显示</td><td colspan="1" rowspan="1">128×95</td></tr><tr><td colspan="1" rowspan="1">2X</td><td colspan="1" rowspan="1">月标速度及日标距离显示</td><td colspan="1" rowspan="1">128×440</td></tr><tr><td colspan="1" rowspan="1">3区</td><td colspan="1" rowspan="1">速度表盘</td><td colspan="1" rowspan="1">542×440</td></tr><tr><td colspan="1" rowspan="1">4区</td><td colspan="1" rowspan="1">牵引制动状态显示</td><td colspan="1" rowspan="1">157×88</td></tr><tr><td colspan="1" rowspan="1">5区</td><td colspan="1" rowspan="1">最高可用驾驶模式显示</td><td colspan="1" rowspan="1">167×88</td></tr><tr><td colspan="1" rowspan="1">6区</td><td colspan="1" rowspan="1">列车完整性显示</td><td colspan="1" rowspan="1">179×88</td></tr><tr><td colspan="1" rowspan="1">7区</td><td colspan="1" rowspan="1">列车头尾设备状态显示</td><td colspan="1" rowspan="1">167×88</td></tr><tr><td colspan="1" rowspan="1">8区</td><td colspan="1" rowspan="1">终点站显示</td><td colspan="1" rowspan="1">295×95</td></tr><tr><td colspan="1" rowspan="1">9区</td><td colspan="1" rowspan="1">下一站显示</td><td colspan="1" rowspan="1">295×95</td></tr><tr><td colspan="1" rowspan="1">10区</td><td colspan="1" rowspan="1">车次显示</td><td colspan="1" rowspan="1">306×95</td></tr><tr><td colspan="1" rowspan="1">11区</td><td colspan="1" rowspan="1">跳停扣车显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">12区</td><td colspan="1" rowspan="1">菜单按钮显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">13区</td><td colspan="1" rowspan="1">当前驾驶模式显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">14区</td><td colspan="1" rowspan="1">当前运行等级显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">15区</td><td colspan="1" rowspan="1">折返状态显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">16区</td><td colspan="1" rowspan="1">列车进入停车窗显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">17区</td><td colspan="1" rowspan="1">门状态及门允许愈令昆元。</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">18区</td><td colspan="1" rowspan="1">发车信息显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">19区</td><td colspan="1" rowspan="1">控制模式显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">20区</td><td colspan="1" rowspan="1">及站台门状态显示</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">21区</td><td colspan="1" rowspan="1">备故障</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">22区</td><td colspan="1" rowspan="1">抛段的转换区显</td><td colspan="1" rowspan="1">177×88</td></tr><tr><td colspan="1" rowspan="1">23区</td><td colspan="1" rowspan="1">市</td><td colspan="1" rowspan="1">216×145</td></tr><tr><td colspan="1" rowspan="1">24区</td><td colspan="1" rowspan="1">自定义</td><td colspan="1" rowspan="1">439×145</td></tr><tr><td colspan="1" rowspan="1">25区</td><td colspan="1" rowspan="1">自定义显示</td><td colspan="1" rowspan="1">369×145</td></tr></table>

# 5.2 主要颜色值定义

在MMI显示界面中，不同区域不同条件下，使用不同的颜色进行显示，主要使用的颜色定义推荐值见表2。

表2 主要颜色值定义推荐值  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">颜色</td><td colspan="1" rowspan="1">RGB值</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">白色</td><td colspan="1" rowspan="1">RGB(255,255,255)</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">黑色</td><td colspan="1" rowspan="1">RGB (0,12,25)</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">红色</td><td colspan="1" rowspan="1">RGB (189,0,0)</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">黄色</td><td colspan="1" rowspan="1">RGB3(255,242,0)</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1">浅灰色</td><td colspan="1" rowspan="1">RGB(212,212,212)</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1">淡绿色</td><td colspan="1" rowspan="1">RGB(45,144,51)</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1">橙色</td><td colspan="1" rowspan="1">RGB(234,145,0)</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1">深蓝色</td><td colspan="1" rowspan="1">RCB(37,151,230)</td></tr></table>

# 5.3MMI显示图例要求

# 5.3.11区超速报警及输出紧急制动显示

超速报警及输出紧急制动显示是根据预计超越速度限制的时间及距离，对驾驶员显示警报，示意可能发生的意外状况。初始状态1区显示图标如表3所示。各图片居中显示。

表31区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺小(mm ×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">118×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">118×83橙色</td><td colspan="1" rowspan="1">列车当前速度超过推荐速度，驾驶员宜施加制动，以防止列车触发紧急制动</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图 标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">118×83红色</td><td colspan="1" rowspan="1">已输出紧急制动</td></tr></table>

# 5.3.22区目标速度及目标距离信息显示

目标速度及目标距离信息是显示到下一限制点的距离及目标速度，两者均受最受限的ATP条件决定。

目标距离使用两种方法表示：柱状光带表示法和数字表示法。柱状光带的最大尺寸为 $1 5 \times 4 0 0$ 像素，颜色根据目标速度和目标距离的数值变化，见表4。柱状光带的左侧为坐标系刻度，该坐标系采用对数坐标，颜色为浅灰，其最高端所对应的最远距离为 $7 5 0 \mathrm { ~ m ~ }$ ，最低端固定。光带正下方为数字表示区，单位为米。字体大小为10磅，颜色为白色。如果目标距离大于750，则柱状光带显示 $7 5 0 \mathrm { ~ m ~ }$ ，光带正下方为数字按实际距离显示。

表4柱状光带颜色定义  

<table><tr><td rowspan=2 colspan=1>目标速度(km/h)</td><td rowspan=1 colspan=3>目标距离(m)</td></tr><tr><td rowspan=1 colspan=1>s&gt;300</td><td rowspan=1 colspan=1>150≤s≤300</td><td rowspan=1 colspan=1>s&lt;150</td></tr><tr><td rowspan=1 colspan=1>v≥60</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>淡绿色</td></tr><tr><td rowspan=1 colspan=1>25≤0&lt;60</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>黄色</td></tr><tr><td rowspan=1 colspan=1>0&lt;v&lt;25</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>黄色</td><td rowspan=1 colspan=1>黄色</td></tr><tr><td rowspan=1 colspan=1>v=0</td><td rowspan=1 colspan=1>淡绿色</td><td rowspan=1 colspan=1>黄色</td><td rowspan=1 colspan=1>红色</td></tr></table>

目标速度根据目标距离得出，在目标距离上方以数字形式显示，单位为千米每小时 $\mathbf { \ k m / h }$ )。字体大小为16磅，颜色为白色。

目标速度及目标距离信息显示如图2所示。

![](images/754a5857d3b6f1229c29c5248add0bedcc16d4af35c11172153418c44058e2f2.jpg)  
图2目标速度及目标距离信息

# 5.3.33区速度表盘显示

# 5.3.3.1速度表盘

速度表盘的尺寸为 $4 1 1 \ \mathrm { m m } \times 4 1 1 \ \mathrm { m m }$ ，中心点坐标为（399，309)。

列车速度采用双备份显示。一种方式是速度表，刻度按照 $5 ~ \mathrm { k m / h }$ 进行显示，刻度的颜色为浅灰色，长刻度线的宽度为3像素，长度为28像素。短刻度线的宽度为2像素，长度为15像素。每 $1 0 ~ \mathrm { k m / h }$ 做一个数字标志，数字的颜色为浅灰色，字体大小为13磅。表盘的速度范用可根据工程配置，最大为 $1 6 0 ~ \mathrm { k m } / \mu$ 。另一种方式是数字，在速度表的中间显示列车速度值。

沿着度表盘的外边界，显示环形边框，边框的颜色为红色，宽度为3像素。红色边框的半径为204像素。仪表盘从刻度0到最大刻度的扇形弧度为 $3 1 0 ^ { \circ }$ 。以垂直向上作为 $0 ^ { \circ } , \scriptscriptstyle - 1 5 5 ^ { \circ }$ 的角度显示 $0 ~  { \mathrm { k m } } /  { \mathrm { h } }$ , $1 5 5 ^ { \circ }$ 的角度显示最大速度。文字距离中心点的半径为168像素。刻度到刻度值之间为3像素。速度表盘显示如图3所示。

![](images/f122c406d05e43ca4cb95da4f86a9737444c8fe18bae7fbfb1e0435592b8faf1.jpg)

#

角形的中线与该速度度表的圆心。无推荐边长为15像素，如图

中线与该速度处的半条直线上，该中线的顶点朝向速度表的圆心。此三角形为等边 痛形边长为15 15像茅 ，如图5所示。

# 轨道

![](images/b6a1fd80f7de026e01f152759897eca2028e58ce2add69534ed5fa11d31e895a.jpg)  
图4 推荐速度

![](images/88fe7fde800a2485b7e3c84f3f97e940201a66b5ad8b81016c1708574d757c4b.jpg)  
图5 紧急制动干预速度

# 5.3.3.2 数字方式显示的列车速度

列车速度指针由指针和指针始端的圆圈组成，这两部分的颜色均为白色。速度指针的形状如图6所示，指针的长度不应触到速度表盘的刻度条。在指针始端的圆圈中，以数字方式显示当前速度，数字的颜色为白色，字体大小为18像素，圆盘半径41像素，指针半径165像素。列车测速无效通过统一文本信息显示、图形自定义显示。

![](images/7c189a5e6822f1c59c43b27d9cd42397fecfeeff224e3e1f998801352c52c70c.jpg)  
图6速度指针（单位：mm)

# 5.3.44区牵引制动状态显示

牵引制动状态信息表示在ATO模式下牵引和制动情况，如果没有输人信息将显示初始状态，显示图标及对应含义如表5所示。

表54区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图  标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">139×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">139×83黑色/浅灰色</td><td colspan="1" rowspan="1">牵引状态</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">-O-</td><td colspan="1" rowspan="1">139×83黑色/浅灰色</td><td colspan="1" rowspan="1">惰行状态</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">139×83黑色/浅灰色</td><td colspan="1" rowspan="1">制动状态</td></tr></table>

# 5.3.55区最高可用驾驶模式显示

最高可用驾驶模式信息显示最高的可川模式级别，如果没有输入信息将显示初始状态，显示图标及对应含义如表6所示。

表65区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>139×83黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>RM</td><td rowspan=1 colspan=1>139×83黑色/浅灰色</td><td rowspan=1 colspan=1>限制人工驾驶模式</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>CM-I</td><td rowspan=1 colspan=1>139×83黑色/浅灰色</td><td rowspan=1 colspan=1>点式监督模式</td></tr></table>

表65区的显示图标（续）  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图</td><td rowspan=1 colspan=1>尺寸(mm ×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CM-C</td><td rowspan=1 colspan=1>139×83黑色/浅灰色</td><td rowspan=1 colspan=1>连续式监督模式</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>AM-1</td><td rowspan=1 colspan=1>139×83黑色/浅灰色</td><td rowspan=1 colspan=1>点式自动驾驶模式</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>AM-C</td><td rowspan=1 colspan=1>139×83黑色/浅灰色</td><td rowspan=1 colspan=1>连续式自动驾驶模式</td></tr></table>

# 5.3.66区列车完整性显示

列车完整性信息显示列车的完整性状态，显示图标及对应含义如表7所示。

表76区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图   标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/淡绿色</td><td rowspan=1 colspan=1>列车完整性正常</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/红色</td><td rowspan=1 colspan=1>列车完整性丢失</td></tr></table>

↓

# 5.3.77区列车头尾设备状态显示

该信息表示列车头尾设备的状态，显示图标及对应含义如表8所示。

表87区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸（mm×mm)颜色</td><td rowspan=1 colspan=1>含  义</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>94×83黑色/淡绿色/浅灰色/白色端车载ATC设备待机</td><td rowspan=1 colspan=1>本端车载ATC设备激活，另一黑色/淡绿色/浅灰色/白色端车载ATC设备待机</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>黑色</td><td rowspan=1 colspan=1>本端车载ATC设备激活，另一载ATC设备故障</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>94×83黑炎绿录色/饿灰色/红色</td><td rowspan=1 colspan=1>大    载ATC设备故障，另一rC设备激活</td></tr></table>

# 5.3.8 8区终点站显示

该信息显示列车的终点霜，置零车站名称”的形式显示，无输信息时车站名称显示初始状态。字体小为18像素，显示 $1 \sim 6$ 个文字站名，深蓝色，左对齐显示。若站名超过6个文字，可通过换行或者缩小字体的方式显示。显示图标及对应含义如表9所示。

表9 8区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">终点站：</td><td colspan="1" rowspan="1">284×85黑色/深蓝色</td><td colspan="1" rowspan="1">无输入信息时</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">终点站：站台名称</td><td colspan="1" rowspan="1">284×85黑色/深蓝色</td><td colspan="1" rowspan="1">有输入信息时</td></tr></table>

# 5.3.99区下一站显示

该信息显示列车的下一站，以“下一站：车站名称”的形式显示，无输人信息时车站名称显示初始状态。字体大小为18像素，显示1\~6个文字站名，深蓝色，左对齐显示。若站名超过6个文字，可通过换行或者缩小字体的方式显示。显示图标及对应含义如表10所示。

表109区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=2 colspan=1>下一站:下一站：站台名称</td><td rowspan=1 colspan=1>284×85黑色/深蓝色</td><td rowspan=1 colspan=1>无输人信息时</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>284×85黑色/深蓝色</td><td rowspan=1 colspan=1>有输人信息时</td></tr></table>

# 5.3.1010区车次显示

该信息显示列车的车次号，以TXXXXXXXX的形式显示，X为数字$1 \sim 9$ ，显示1\~5位数字。无输入信息时车次号显示初始状态。字体大小为18像素，颜色为浅灰色，左对齐显示。若车次号超过5个数字，可通过

换行或者缩小字体的方式显示。显示图标及对应含义如表11所示。

表1110区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图   标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>298×85黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>T53214</td><td rowspan=1 colspan=1>298×85黑色/浅灰色</td><td rowspan=1 colspan=1>车次号显示</td></tr></table>

# 5.3.1111区跳停、扣车显示

该信息表示列车当前的跳停、扣车状态，根据ATS的命令显示。显示图标及对应含义如表12所示。

表1211区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/黄色</td><td rowspan=1 colspan=1>跳停</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>*</td><td rowspan=1 colspan=1>177×83黑色/浅灰色/红色</td><td rowspan=1 colspan=1>扣车</td></tr></table>

# 5.3.1212区菜单按钮显示

按下该按钮后，将激活弹出菜单。弹出菜单内容各家不作统一处理。显示图标及对应含义如表13所示。

表1312区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>菜单</td><td rowspan=1 colspan=1>177×83黑色/白色</td><td rowspan=1 colspan=1>菜单设置按钮可用</td></tr></table>

# 5.3.1313区当前驾驶模式显示

该信息表示列车当前的驾驶模式，如果没有输人信息则显示初始状态。显示图标及对应含义如表14所示。

表1413区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">AM</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">ATO模式</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">CM</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">监督模式</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">RM</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">受限模式</td></tr></table>

# 5.3.1414区当前运行等级显示

该信息表示列车当前的运行等级，如果没有输人信息则显示初始状态。显示图标及对应含义如表15所示。

# 表15004区的显示图标

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图</td><td rowspan=1 colspan=1>尺寸（mm颜色</td><td rowspan=1 colspan=1>含    义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X83</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>城市ILC</td><td rowspan=1 colspan=1>轨道     3黑色/浅灰色</td><td rowspan=1 colspan=1>联锁控制级别</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>ITC</td><td rowspan=1 colspan=1>177×83黑色/浅灰色</td><td rowspan=1 colspan=1>点式列车控制级别</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>CTC</td><td rowspan=1 colspan=1>177×83黑色/浅灰色</td><td rowspan=1 colspan=1>连续式列车控制级别</td></tr></table>

# 5.3.1515区折返状态显示

该信息显示列车折返的状态，无输入信息时显示初始状态。显示图标及对应含义如表16所示。

表1615区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/淡绿色</td><td rowspan=1 colspan=1>满足折返条件后，闪烁，闪烁的频率推荐值为1Hz</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>人</td><td rowspan=1 colspan=1>177×83黑色/黄色</td><td rowspan=1 colspan=1>常亮，表示折返激活</td></tr></table>

# 5.3.1616区列车进入停车窗显示

该信息显示列车在站内停车的情况，无输入信息时显示初始状态。显示图标及对应含义如表17所示。

表1716区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">177×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/红色</td><td colspan="1" rowspan="1">列车进入停车区域但未进人停车窗</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/淡绿色</td><td colspan="1" rowspan="1">列车进人停车区域且进人停车窗</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色</td><td colspan="1" rowspan="1">列车位于退行激活窗</td></tr></table>

# 5.3.1717区门状态及门允许命令显示

该信息显示门状态及门允许命令，无输入信息时显示初始状态。6、7、8、9级别相同，优先级最高；3、4、5级别相同，优先级次之；2优先级最低（可选，根据工程需求配置）。显示图标及对应含义如表18所示。

表1817区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺寸(mm×mn)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1">-</td><td colspan="1" rowspan="1">177×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/红色/浅灰色</td><td colspan="1" rowspan="1">强制门允许</td></tr><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">允许左右两侧车门同时开启</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">允许左侧车门开启</td></tr><tr><td colspan="1" rowspan="1">5</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">允许右侧车门开启</td></tr><tr><td colspan="1" rowspan="1">6</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">左侧车门打开</td></tr><tr><td colspan="1" rowspan="1">7</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">右侧车门打开</td></tr><tr><td colspan="1" rowspan="1">8</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">左右侧车门均打开</td></tr><tr><td colspan="1" rowspan="1">9</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色/黄色/浅灰色</td><td colspan="1" rowspan="1">无门允许情况下车门打开</td></tr></table>

# 5.3.18 18区发车信息显示

该信息显示发车提示信息，无输人信息时显示初始状态。显示图标及对应含义如表19所示。

![](images/87eddb0ef8570dfd3d987ea5d18a846159d683ccadaf4329864807a015de0b6a.jpg)

# 5.3.19 19区客室门控制模式显示

该信息显示客室门的控制模式，无输入信息时显示初始状态。显示图标及对应含义如表20所示。

表19 18区的显示图标  
表2019区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图 标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">MM</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">人T开门，人工关门</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">AM</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">自动开门，人工关门</td></tr><tr><td colspan="1" rowspan="1">4</td><td colspan="1" rowspan="1">AA</td><td colspan="1" rowspan="1">177×83黑色/浅灰色</td><td colspan="1" rowspan="1">自动开门，自动关门</td></tr></table>

# 5.3.2020区车辆及站台门状态显示

该信息显示车辆空转/打滑及站台门的状态，无输入信息时显示初始状态。列车车轮打滑优先级最高，站台门未关闭次之。显示图标及对应含义如表21所示。

表2120区的显示图标  

<table><tr><td colspan="1" rowspan="1">序号</td><td colspan="1" rowspan="1">图标</td><td colspan="1" rowspan="1">尺寸(mm×mm)颜色</td><td colspan="1" rowspan="1">含义</td></tr><tr><td colspan="1" rowspan="1">1</td><td colspan="1" rowspan="1"></td><td colspan="1" rowspan="1">177×83黑色</td><td colspan="1" rowspan="1">初始状态</td></tr><tr><td colspan="1" rowspan="1">2</td><td colspan="1" rowspan="1">0</td><td colspan="1" rowspan="1">177×83黑色/红色</td><td colspan="1" rowspan="1">车轮空转/打滑</td></tr><tr><td colspan="1" rowspan="1">3</td><td colspan="1" rowspan="1">□□</td><td colspan="1" rowspan="1">177×83黑色/黄色</td><td colspan="1" rowspan="1">站台门未关闭</td></tr></table>

# 5.3.2121区设备故障显示

该信息显示发生的故障情况，无输人信息时显示初始状态。ATP故障优先级最高，ATO故障优先级次之，RAD故障优先级最低。显示图标及对应含义如表22所示。除下表介绍图标外，厂商可白定义图标显示。

表2221区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图 标</td><td rowspan=1 colspan=1>尺小（mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/红色</td><td rowspan=1 colspan=1>无线设备通信故障时显示</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/红色</td><td rowspan=1 colspan=1>ATP故障时显示</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/红色</td><td rowspan=1 colspan=1>若为单系ATO，故障时显示；若为冗余ATO，两系均故降时显示</td></tr></table>

# 5.3.22 22区车辆段的转换区显示

该信息显示车辆段信息，无输入信息时显示初始状态。显示图标及对应含义如表23所示。

表23 22区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/黄色</td><td rowspan=1 colspan=1>列车进人车辆段</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色/淡绿色动车辆段时不显示</td><td rowspan=1 colspan=1>列车进人库线，无自黑色/浅灰色/淡绿色动车辆段时不显示</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色</td><td rowspan=1 colspan=1>列车丢失定位或在车辆段内行驶</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>177×83黑色/浅灰色</td><td rowspan=1 colspan=1>开口模式下，司机已确认前方信号开放</td></tr></table>

# 5.3.23 23区时间显示

该信息显示系统时间，无输入信息时显示初始状态。字体大小为21像素，居中显示。显示图标及对应含义如表24所示。

表2423区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图标</td><td rowspan=1 colspan=1>尺寸(mm×mm)颜色</td><td rowspan=1 colspan=1>含义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>-</td><td rowspan=1 colspan=1>211×133黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>16:06:33</td><td rowspan=1 colspan=1>211×133黑色/浅灰色</td><td rowspan=1 colspan=1>系统时间</td></tr></table>

# CIATION

# 5.3.24自定义24区确认信息显示

该信息显示要求驾驶员确认的信息或者提示信息，由各厂商定义，无输信息时显示初婚状态。显图标及对应义如表25所示。

表2524区的显示图标  

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>图   路</td><td rowspan=1 colspan=1>尺寸（mm  mn</td><td rowspan=1 colspan=1>含   义</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>439×133黑色</td><td rowspan=1 colspan=1>初始状态</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>请确认前方信号开放</td><td rowspan=1 colspan=1>439×133黑色/白色/黄色</td><td rowspan=1 colspan=1>示例</td></tr></table>

# 5.3.25自定义25区文字或图标信息显示

文字或图标信息显示区域，由各厂商自定义。

# 5.4车载ATP切除或ATP未激活显示

当前ATP切除或未激活时，显示黑屏，同时在屏幕中心显示时间。

显示时间的文字字体大小为62像素，颜色为浅灰色。如图7所示。

![](images/c982fac61505fe417efd5320dd2b4a45623277a1330a577e4f45c5833cdd1489.jpg)  
图7黑屏显示示意图

# 5.5 整体效果图

5.4中图标按照分区显示在尺寸为12英寸、分辨率为 $1 \ 0 2 4 \times 7 6 8$ 的MMI显示屏后，整体效果图如图8所示。

![](images/bdfe2b3d73fd792e8465bc18e578f26929e57ba505e47b2a32095cfd41c98a00.jpg)  
图8 整体效果图

# 5.6司机室按钮、开关、指示灯设置要求

为了配合完成第5.4条MMI界面显示信息设置或确认，在司机室应配置以下按钮、开关和指示灯。

# 5.6.1按钮、开关、指示灯布置

司机室按钮、开关、指示灯布置区域如表26所示。.

# 表26按钮、开关、指示灯布置

<table><tr><td rowspan=1 colspan=1>序号</td><td rowspan=1 colspan=1>名称</td><td rowspan=1 colspan=1>相关显示区</td><td rowspan=1 colspan=1>备注</td></tr><tr><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>强制门允许按钮</td><td rowspan=1 colspan=1>17区，门状态及门允许命令显示</td><td rowspan=1 colspan=1>白复式按钮（可选，根据工程需求）</td></tr><tr><td rowspan=1 colspan=1>2</td><td rowspan=1 colspan=1>ATO启动按钮</td><td rowspan=1 colspan=1>13区，当前驾驶模式显示；14区，当前运行等级显示</td><td rowspan=1 colspan=1>自复式指示灯按钮</td></tr><tr><td rowspan=1 colspan=1>3</td><td rowspan=1 colspan=1>驾驶模式降级按钮</td><td rowspan=1 colspan=1>5区，最高可用驾驶模式显示</td><td rowspan=1 colspan=1>自复式指示灯按钮</td></tr><tr><td rowspan=1 colspan=1>4</td><td rowspan=1 colspan=1>驾驶模式升级按钮</td><td rowspan=1 colspan=1>5区，最高可川驾驶模式显示</td><td rowspan=1 colspan=1>自复式指示灯按钮</td></tr><tr><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1>确认按钮</td><td rowspan=1 colspan=1>24区，确认信息显示22区，车辆段的转换区显示</td><td rowspan=1 colspan=1>自复式指示灯按钮</td></tr><tr><td rowspan=1 colspan=1>6</td><td rowspan=1 colspan=1>自动折返按钮</td><td rowspan=1 colspan=1>15区，折返状态显示</td><td rowspan=1 colspan=1>自复式指示灯按钮</td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>门模式开关</td><td rowspan=1 colspan=1>19区，客室门控制模式显示</td><td rowspan=1 colspan=1>旋转开关</td></tr><tr><td rowspan=1 colspan=1>8</td><td rowspan=1 colspan=1>ATP切除开关</td><td rowspan=1 colspan=1>5.5节，当前端车载ATP切除或ATP未激活显示</td><td rowspan=1 colspan=1>旋转开关</td></tr></table>

# 5.6.2功能介绍

# 5.6.2.1强制门允许按钮

按下该按钮后，可强制输出门使能信号，同时在17区显示强制门允许图标。车门打开后，在17区显示门使能和门打开图标。根据工程需求设置。

# 5.6.2.2ATO启动按钮

满足ATO启动条件时，两个按钮指示灯同时闪烁，闪烁的频率推荐值为 $1 \ \mathrm { H z }$ ；同时按下两个按钮后，ATO启动指示灯常亮。

# 5.6.2.3驾驶模式升级按钮

实现对预选模式升级选择，每按下一次在当前预选模式基础上升一挡，同时在5区显示当前选择的最高可用驾驶模式。选择完毕后，应按确认按钮（序号5）进行确认，确认后当前的最高可用驾驶模式才可生效。

# 5.6.2.4驾驶模式降级按钮

实现对预选模式降级选择，每按下一次在当前预选模式基础上降一挡，同时在5区显示当前选择的最高可用驾驶模式。选择完毕后，应按确认按钮（序号5）进行确认，确认后当前的最高可用驾驶模式才可生效。

# 5.6.2.5确认按钮

该按钮对24区弹出的待司机确认信息进行确认，司机按下该按钮后，24区原有提示信息消失。同时，该按钮用于对驾驶模式降级按钮和驾驶模式升级按钮设置的最高预设驾驶模式等信息进行确认。

# 5.6.2.6自动折返按钮

该按钮对折返过程中司机的操作进行提示和确认，与15区图标显示对应。

# 5.6.2.7门模式开关

该开关用于选择列车门控模式，具有MM、AM和AA三种挡位，与19区客室门控制模式显示的三种模式图标对应。

# 5.6.2.8ATP切除开关

该开关用于切除ATP，当ATP切除后，MMI显示5.5条的黑屏状态。

# 5.7声音报警

当列车超过推荐速度等特定场景下（包括但不限于），MMI应发出“滴、滴….”报警声（报警持续时间在工程中统一）。

中国城市轨道交通协会团体标准城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通接口规范

# 第8部分：车载人机界面

T/CAMET04011.8—2018

\*

中国铁道出版社有限公司出版发行（100054，北京市西城区右安门两街8号）公司网址：http：//www.tdpress.com北言铭成印刷有限公司印品

开本： $8 8 0 \ \mathrm { m m } \times 1 \ 2 3 0 \ \mathrm { m m }$ 1/32印张：1.25字数：31千2019年5月第1版2019年5月第1次印刷

书号： $1 5 1 1 3 \cdot 5 7 3 4$ 定价：15.00元

# 版权所有侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。