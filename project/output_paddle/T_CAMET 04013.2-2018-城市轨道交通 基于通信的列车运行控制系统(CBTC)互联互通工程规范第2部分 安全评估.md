ICS 45.020 S 63

# 中国城市轨道交通协会团体标准

T/CAMET 04013.2—2018

# 城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范 第2部分：安全评估

# Urban rail transit — Engineering specification for interoperability of communication based train control system Part 2: Safety assessment

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
4 安全评估 …… 3    
4.1 评估原则 …… 3    
4.2 一般要求 …… 4    
4.3 互联互通安全评估相互认可 …… 4    
4.4 互联互通安全评估过程及活动 …… 5

---

## 前言

T/CAMET 04013《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》分为以下三个部分：

——第1部分:工程设计;

——第2部分:安全评估;

——第3部分：交付基本条件。

本部分是 TCAME/T 04013 的第 2 部分。

本部分按照 GB/T 1.1—2009 给出的规则起草。

请注意本部分的某些内容可能涉及专利，本部分的发布机构不承担识别这些专利的责任。

本部分由中国城市轨道交通协会技术装备专业委员会提出。

本部分由中国城市轨道交通协会归口。

本部分起草单位：中铁检验认证中心、北京英华经纶交通运输技术服务有限公司、莱茵技术（上海）有限公司、中国铁道科学研究院集团有限公司通信信号研究所、交控科技股份有限公司、北京全路通信信号研究设计院集团有限公司、浙江众合科技股份有限公司。

本部分主要起草人：编写组：孙超、赵天时、郎学伟、陈建国、陈光智、刘正东、卿松、王成国、朱胜远、师秀霞、方力一、唐凯琳、李兆龄、吴炳昊、张扬、张伟。审查组：李中浩、朱翔、赵炜、郑生全、张艳兵、张良、张琼燕、段晨宁、李新文、李德堂、文成祥、任敬、肖利君、张守芝、朱东飞、刘新平、王道敏、徐鼎。

---

## 引言

为促进中国城市轨道交通建设，实现并满足城市轨道交通互联互通的需要，达到经济适用、资源共享、技术先进及可持续发展的目标，制定城市轨道交通基于通信的列车运行控制系统（CBTC）互联互通系列团体标准。

该系列规范包括《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通系统规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通接口规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通测试规范》《城市轨道交通 基于通信的列车运行控制系统（CBTC）互联互通工程规范》4个规范（17个部分）。

---

# 城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通工程规范 第 2 部分: 安全评估

## 1 范围

本部分规定了 CBTC 信号系统互联互通工程安全评估原则、活动、流程、交互物及版本升级评估等内容。

本部分适用于城市轨道交通 CBTC 信号系统（以下简称“信号系统”）互联互通安全评估活动及相关流程，并确定信号系统互联互通安全评估各相关方工作内容及职责。

## 2 规范性引用文件

中

下列文件对于本部分的应用是必不可少的。凡是注日期的引用文件，仅所注日期的版本适用于本部分。凡是不注日期的引用文件，其最新版本（包括所有的修改单）适用于本部分。

GB/T 21562—2008 轨道交通 可靠性、可用性、可维修性和安全性规范及示例(IEC 62278:2002, IDT)

GB/T 21562.2—2015 轨道交通 可靠性、可用性、可维修性和安全性规范及示例 第2部分：安全性的应用指南

GB/T 28808—2012 轨道交通 通信、信号和处理系统 控制和防护系统软件(IEC 62279:2002, IDT)

GB/T 28809—2012 轨道交通 通信、信号和处理系统 信号用安全相关电子系统(IEC 62425:2007, IDT)

GB 50157—2013 地铁设计规范

CJ/T 407—2012 城市轨道交通基于通信的列车自动控制系统技术要求

---

T/CAMET 04010.1 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 1 部分: 系统总体要求

T/CAMET 04010.2 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 2 部分: 系统架构和功能分配

T/CAMET 04010.4 城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 4 部分: 互联互通危害分析

CLC/TR 50506-1 轨道交通 通信、信号和处理系统 EN 50129 的应用指南 第1部分：相互认可（Railway applications—Communication, signalling and processing systems—Application guide for EN 50129）

EN 50128 - 2011 轨道交通 通信信号及处理系统 铁路控制和防护系统软件（Railway applications—Communication, signaling and processing systems—Software for railway control and protection systems）

## 3 术语和缩略语

### 3.1 术语

GB 50157—2013、CJ/T 407—2012、T/CAMET 04010.1、T/CAMET 04010.2 和 T/CAMET 04010.4 界定的及下列术语和缩略语适用于本部分。

3.1.1

本线 local line

指由单个集成商所负责的轨旁信号设备所对应的线路。

[T/CAMET 04010.4,术语 3.1.11]

3.1.2

他线 other line

与本线互联互通的其他线路。

[T/CAMET 04010.4,术语3.1.12]

#### 3.1.3 

源数据 source data

能直接提供信号系统原始或具体数据的自足性数据。

---

#### 3.1.4 

## 跨线运行 overline operation

运营列车在两条或两条以上制式相同或兼容的线路中，由一条线路进入另外一条线路进行共线运行的方式。

[T/CAMET 04010.1,术语3.1.14]

#### 3.1.5 

## 共线运行 mix operation

装备不同厂家车载信号设备的列车可以在装备同一厂家轨旁信号设备线路上支持以点式列车控制级别和连续式列车控制级别无缝安全可靠运营。

[T/CAMET 04010.2, 定义 3.1.18]

### 3.2 缩略语

CBTC: 基于通信的列车控制 (Communication Based Train Control)

## 4 安全评估

### 4.1 评估原则

互联互通各参与方应遵循如下原则：

a）互联互通安全评估以各安全评估相关方的相互认可工作为基础。

b）本线评估方负责本线地面设备和车载设备的安全评估。

c）他线列车进入本线时，他线信号集成商提供证据，证明他线车载设备安全功能满足互联互通车载设备的安全需求。







d）他线列车进入本线时，本线提供线路数据，并负责源数据的准确性。本线评估方负责源数据安全评估。他线负责输入数据的转化、数据测试及其安全评估。

e）本线评估方出具的评估报告/授权/证书的授权范围应包含在本线运营的所有集成商的车载设备。

f) 各阶段授权/证书应体现本线列车适合进入他线跨线调试、试运行、试运营和运营；允许他线列车进入本线调试、试运行、试运营和运营。

g）各承包商（集成商）/供应商信号系统设计应满足互联互通要

---

求，如工程接口协议、行车控制参数（如退行、后溜防护距离处理，安全防护距离等关键参数）等。

### 4.2 一般要求

互联互通安全相关产品应满足互联互通相关规范的要求，并通过通用产品或通用应用层互联互通安全评估。

### 4.3 互联互通安全评估相互认可

互联互通通用产品/通用应用指按照互联互通规范开发、设计及生产的信号系统或产品。

互联互通特定应用是指装备了互联互通信号系统或产品、在特定信号系统工程上进行互联互通共线和/或跨线运营的应用。

互联互通特定应用安全评估包含本线特定应用的安全评估、互联互通通用产品/通用应用安全评估的相互认可和对他线信号系统互联互通特定应用安全评估的相互认可。其中，本线特定应用指属于同一设备集成商的信号系统在工程项目中集成及运营的活动。

## a）通用应用或通用产品安全评估的相互认可

通用产品或通用应用的相互认可是互联互通评估方对本线相关产品已评估证据的接收，该通用产品或通用应用的既有评估证据，在满足CLC-TR50506-1或等同标准的前提下，无需进一步评估就可被互联互通评估方所接收。

在通用产品或通用应用原有互联互通安全评估证据的基础上，互联互通特定应用安全评估方应对通用产品或通用应用开展相互认可评估活动，以判断通用产品或通用应用是否满足特定工程应用的要求。

信号系统承包商（集成商）/供应商应对已经评估过的原有通用产品或通用应用与特定工程应用的差异进行分析，互联互通特定工程应用评估方须评估差异分析文档，差异分析的评估主要关注如下内容：

——原有的通用产品或通用应用的应用环境、功能和性能、安全和接口需求，以及RAM $ ^{1} $  指标和THR $ ^{2} $  是否满足特定应用要求；

---

——差异分析是否充分；

——相关差异是否会带来通用产品或通用应用的变更；

——由于差异引起的风险是否已经被控制。

互联互通相互认可评估活动应依据 CLC/TR 50506-1 或等同标准要求开展。

## b）信号系统互联互通特定应用安全评估的相互认可

信号系统互联互通的相互认可是本线互联互通评估方对他线信号系统互联互通评估证据的接收，在满足CLC-TR50506-1或等同标准的前提下，该评估证据无需进一步评估就可被本线互联互通评估方所接收，接收方案如下：

他线列车进入本线；他线评估方应出具允许他线列车进入本线的安全授权；本线评估方应出具本线信号设备具备共线/跨线调试、试运营及试运行的安全授权，授权范围应包含在本线的所有集成商的车载设备。授权目的应明确，包括单车动车调试、多动车调试、试运行、试运营等。

### 4.4 互联互通安全评估过程及活动

#### 4.4.1 互联互通安全评估主要过程和活动

基于 GB/T 21562.2、GB/T 28808 适用时，采用 EN 50128-2011 及 GB/T 28809 标准，安全评估方在开展互联互通特定应用安全评估过程中，主要安全评估活动包括但不限于：

——生命周期阶段文档审核；

——测试见证；

——现场质量安全审核。

## a）生命周期阶段文档审核

表1 主要描述在互联互通特定应用安全评估各生命周期阶段承包商（集成商）/供应商需提交的文档及安全评估方所开展的安全评估活动，该表仅是工程阶段、提交文档和评估活动的建议，承包商（集成商）/供应商可根据实际情况调整工程阶段和提交文档。

---

<div style="text-align: center;">表 1 工程阶段、提交文档和评估活动</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>工程阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="12">计划及定义阶段</td><td style='text-align: center;'>用户需求</td><td rowspan="12">主要关注如下：——评估系统边界、构成、接口及运行环境；——评估人员资质、人员独立性及风险接收准则；——评估测试方法、验证方法及确认方法的合理性；——评估测试、验证及确认活动的充分性；——评估各生命周期阶段的开发活动是否合理计划；——评估公有数据版本是否有统一的配置及变更管理；——评估质量管理、配置管理、安全管理活动计划是否合理评估计划阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>项目计划</td></tr><tr><td style='text-align: center;'>安全计划</td></tr><tr><td style='text-align: center;'>RAM计划</td></tr><tr><td style='text-align: center;'>质量管理计划</td></tr><tr><td style='text-align: center;'>验证计划</td></tr><tr><td style='text-align: center;'>确认计划</td></tr><tr><td style='text-align: center;'>配置管理计划</td></tr><tr><td style='text-align: center;'>数据准备计划</td></tr><tr><td style='text-align: center;'>测试计划</td></tr><tr><td style='text-align: center;'>制造和安装计划</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr><tr><td rowspan="5">危害识别和风险分析阶段</td><td style='text-align: center;'>初步危害分析报告</td><td rowspan="5">主要关注如下：——评估危害分类是否满足危害可容忍准则要求；——评估风险分析方法及流程；——评估危害控制措施是否恰当；——评估各设备商是否基于相同的危害源进行风险分析；——评估各设备商实现的差异是否会带来风险；——评估危害控制措施的防护是否满足互联互通要求；——评估危害更新情况；——评估本阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>系统危害分析和风险评估报告</td></tr><tr><td style='text-align: center;'>接口危害分析</td></tr><tr><td style='text-align: center;'>危害日志</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr></table>

---

<div style="text-align: center;">表 1 工程阶段、提交文档和评估活动(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>工程阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="6">系统需求阶段</td><td style='text-align: center;'>系统需求规范</td><td rowspan="6">主要关注如下：——评估安全计划中本阶段流程、技术、方法的应用；——评估系统RAM和安全需求，主要考虑可测性、完整性、唯一性、标准符合性、可追溯性等；——评估接口和环境需求是否被定义；——评估工程数据准备流程是否满足数据准备手册要求；——评估数据准备是否满足产品的要求；——评估公有数据地图是否按照统一的数据准备执行；——评估各设备商安全需求及需求分配是否一致；——评估测试案例及验证方法是否充分、完整、可执行；——评估本阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>安全需求规范</td></tr><tr><td style='text-align: center;'>数据准备程序</td></tr><tr><td style='text-align: center;'>系统需求测试规范及测试案例</td></tr><tr><td style='text-align: center;'>安全需求测试规范及测试案例</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr><tr><td rowspan="7">系统设计阶段</td><td style='text-align: center;'>工程初步设计</td><td rowspan="7">主要关注如下：——评估安全计划中本阶段流程、技术、方法的应用；——评估需求分配的充分性及合理性；——评估差异分析是否引起通用产品或通用应用变更；——评估识别的新的风险是否被记录；——评估信号设计是否满足互联互通要求；——评估系统定义、系统需求中的接口是否被合理设计；——评估设计和集成测试的追溯；——评估本阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>系统接口设计规范</td></tr><tr><td style='text-align: center;'>各子系统需求规范</td></tr><tr><td style='text-align: center;'>差异性分析</td></tr><tr><td style='text-align: center;'>子系统需求测试规范及测试案例</td></tr><tr><td style='text-align: center;'>系统集成测试规范及测试案例</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr></table>

---

<div style="text-align: center;">表 1 工程阶段、提交文档和评估活动（续）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>工程阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="5">制造和安装阶段</td><td style='text-align: center;'>安装手册</td><td rowspan="5">主要关注如下：
——评估安全计划中本阶段流程、技术、方法的应用；
——评估质量计划的要求已经被应用；
——安全相关应用条件已经被应用；
——评估安装及信号设计是否满足互联互通要求实施；
——评估通用产品或通用应用对安装和制造的要求是否已经转移到相关手册；
——评审安装是否满足设备商要求；
——评估本阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>现场安装流程</td></tr><tr><td style='text-align: center;'>工程配置图</td></tr><tr><td style='text-align: center;'>现场数据准备手册</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr><tr><td rowspan="15">系统确认阶段</td><td style='text-align: center;'>系统集成测试报告</td><td rowspan="15">主要关注如下：
——评估测试案例执行的充分性；
——评估不符合项被记录，并按照不符合项管理；
——评估安全相关故障被描述，且风险被控制在可接受范围；
——评估运营过程中考虑安全相关应用条件；
——评估运营过程中所有的风险已经被考虑、控制及管理；
——运营及维护人员已经被足够培训；
——评估RAM是否满足相关要求；
——评估本阶段验证活动是否充分</td></tr><tr><td style='text-align: center;'>各子系统室内外测试案例</td></tr><tr><td style='text-align: center;'>单车动车测试规范及案例</td></tr><tr><td style='text-align: center;'>多车动车测试规范及案例</td></tr><tr><td style='text-align: center;'>试运行测试规范及案例</td></tr><tr><td style='text-align: center;'>各子系统室内外测试报告</td></tr><tr><td style='text-align: center;'>系统需求测试报告</td></tr><tr><td style='text-align: center;'>单车动车测试报告</td></tr><tr><td style='text-align: center;'>多车动车测试报告</td></tr><tr><td style='text-align: center;'>试运行测试报告</td></tr><tr><td style='text-align: center;'>运营和维护手册</td></tr><tr><td style='text-align: center;'>RAM报告</td></tr><tr><td style='text-align: center;'>FRACAS</td></tr><tr><td style='text-align: center;'>子系统测试报告</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr></table>

---

<div style="text-align: center;">表 1 工程阶段、提交文档和评估活动(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>工程阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="5">系统验收阶段</td><td style='text-align: center;'>安全相关应用条件</td><td rowspan="5">主要关注如下：——评估危害日志中的危害是否都被合理处置；——评估每个安全需求已经被测试、验证及实现；——质量及安全审核；——评估项目中使用的所有工具满足标准分类要求；——评估验证及确认方法的适宜性；——评估安全例证已经完成，并提供了系统运行的判决；——审核通用代码或通用应用安全相关应用条件是否在工程阶段已经考虑；——互联互通安全相关应用条件是否已经考虑；——特定应用的安全相关应用条件已经输出，并培训；——本阶段验证活动</td></tr><tr><td style='text-align: center;'>发布清单</td></tr><tr><td style='text-align: center;'>安全例证</td></tr><tr><td style='text-align: center;'>系统确认报告</td></tr><tr><td style='text-align: center;'>本阶段验证报告</td></tr><tr><td rowspan="4">试运营及维护阶段</td><td style='text-align: center;'>FRACAS记录</td><td rowspan="4">主要关注如下：——评估运营过程中考虑安全相关应用条件；——评估运营过程中所有的风险已经被考虑、控制及管理；——运营及维护人员已经被足够培训；——评估本阶段验证及确认活动是否充分</td></tr><tr><td style='text-align: center;'>安全相关应用条件</td></tr><tr><td style='text-align: center;'>操作与维护手册</td></tr><tr><td style='text-align: center;'>本阶段验证及确认报告</td></tr></table>

## b) 互联互通测试活动及评估

为了不同承包商(集成商)/供应商的信号系统满足互联互通的要求,各承包商(集成商)/供应商需要开展如下测试工作:

——互联互通实验室测试；

——本线信号系统静态调试；

——本线列车单车调试；

---

——本线系统联调和空载试运行；

——互联互通共线调试；

——互联互通跨线调试；

——互联互通多车共线调试；

——互联互通空载试运行。

表 2 主要描述在互联互通特定应用测试阶段各承包商（集成商）/供应商需提交的文档及安全评估方所开展的安全评估活动，该表仅是测试阶段、提交文档和评估活动的建议，承包商（集成商）/供应商可根据实际情况调整测试阶段、提交文档和评估活动。

<div style="text-align: center;">表 2 互联互通测试活动及评估</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>测试阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="3">互联互通
实验室测试</td><td style='text-align: center;'>互联互通测试计划</td><td rowspan="3">1)文档审核；
2)测试见证</td></tr><tr><td style='text-align: center;'>互联互通实验室测试规范及案例</td></tr><tr><td style='text-align: center;'>互联互通实验室测试报告</td></tr><tr><td rowspan="4">本线信号
系统静态
试验</td><td style='text-align: center;'>地面设备/子系统调试规范及
案例</td><td rowspan="4">文档审核，主要关注以下内容：
——信号设备/子系统/系统功能测试；
——一致性试验；
——牵引、制动功能试验</td></tr><tr><td style='text-align: center;'>地面设备/子系统调试报告</td></tr><tr><td style='text-align: center;'>车载设备/子系统调试规范及
案例</td></tr><tr><td style='text-align: center;'>车载设备/子系统调试报告</td></tr><tr><td rowspan="3">本线列车
单车调试</td><td style='text-align: center;'>本线线路数据</td><td rowspan="3">1)本线单车动车授权。
2)文档审核，主要关注以下
内容：
——信号系统功能试验；
——信号系统运行试验；
——牵引、制动功能测试；
——移动授权；
——停车点防护；
——列车定位。
3)测试见证</td></tr><tr><td style='text-align: center;'>本线列车单车测试规范及案例</td></tr><tr><td style='text-align: center;'>本线列车单车测试报告</td></tr></table>

---

<div style="text-align: center;">表 2 互联互通测试活动及评估(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>测试阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="3">本线系统联调和空载试运行</td><td style='text-align: center;'>本线线路数据</td><td rowspan="3">1)文档审核,主要关注以下内容:
——信号系统功能试验;
——信号系统运行试验;
——牵引、制动功能试验;
——列车追踪;
——移动授权;
——停车点防护;
——列车定位。
2)多车动车授权。
3)测试见证</td></tr><tr><td style='text-align: center;'>本线系统联调和空载试运行测试规范及案例</td></tr><tr><td style='text-align: center;'>本线系统联调和空载试运行测试报告</td></tr><tr><td rowspan="4">互联互通单车共线调试</td><td style='text-align: center;'>公共电子地图</td><td rowspan="4">1)文档审核,主要关注以下内容:
——线路数据验证及确认;
——信号系统运行试验;
——移动授权;
——停车点防护;
——列车定位。
2)本线列车进入他线授权。
3)测试见证</td></tr><tr><td style='text-align: center;'>车载设备共线调试授权</td></tr><tr><td style='text-align: center;'>互联互通实验室相应测试规范大纲</td></tr><tr><td style='text-align: center;'>互联互通实验室相应测试报告</td></tr><tr><td rowspan="4">互联互通跨线调试</td><td style='text-align: center;'>他线线路数据</td><td rowspan="4">1)文档审核,主要关注以下内容:
——信号系统功能试验;
——信号系统运行试验;
——牵引、制动功能测试;
——移动授权;
——停车点防护;
——列车定位。
2)跨线数据验证。
3)本线列车进入他线授权。
4)测试见证</td></tr><tr><td style='text-align: center;'>车载设备跨线调试授权</td></tr><tr><td style='text-align: center;'>互联互通跨线测试规范及案例</td></tr><tr><td style='text-align: center;'>互联互通跨线测试报告</td></tr></table>

---

<div style="text-align: center;">表 2 互联互通测试活动及评估(续)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>测试阶段</td><td style='text-align: center;'>提交文档</td><td style='text-align: center;'>评估活动</td></tr><tr><td rowspan="5">互联互通多车共线调试</td><td style='text-align: center;'>本线线路数据</td><td rowspan="5">1)文档审核,主要关注以下内容:——跨线数据验证;——多车混跑追踪;——跨线信号系统功能试验;——跨线信号系统运行试验;——牵引、制动功能试验;——移动授权;——停车点防护;——列车定位。2)互联互通多车共线调试授权。3)测试见证</td></tr><tr><td style='text-align: center;'>本线车载CBTC试运行授权</td></tr><tr><td style='text-align: center;'>他线线路数据</td></tr><tr><td style='text-align: center;'>互联互通多车共线测试规范及案例</td></tr><tr><td style='text-align: center;'>互联互通多车共线测试报告</td></tr><tr><td rowspan="2">互联互通空载试运行</td><td style='text-align: center;'>空载试运行图</td><td rowspan="2">1)文档审核;2)互联互通空载试运行授权</td></tr><tr><td style='text-align: center;'>运行故障记录</td></tr></table>

## c） 现场质量安全审核

现场质量安全审核主要包含对承包商（集成商）/供应商的质量、安全管理审核。质量管理审核包括：质量管理体系、组织机构、质量管理系统、文件控制、采购生产及运行维护管理、不合格控制、质量记录、配置管理以及分包商管理等；安全管理审核包括：安全计划实施、安全组织结构、安全分析活动、系统危害记录、变更控制管理以及安全培训等。

#### 4.4.2 互联互通安全评估主要交付

互联互通安全评估主要交付包括下列安全评估工作文档：

——安全评估计划；

——现场质量安全审核计划/报告；

——现场测试见证计划/报告；

——单车动车调试安全授权；

——跨线调试安全授权；

---

——允许他线单车进入本线共线调试安全授权；

——多车动车调试安全授权；

一互联互通多车共线调试安全授权；

——本线空载试运行安全授权；

——互联互通共线空载试运行安全授权；

——最终安全评估报告/证书。



#### 4.4.3 版本升级评估

互联互通各信号设备版本的变更应遵循如下要求：

a）互联互通授权前，涉及互联互通相关变更，本线应及时通知他线变更内容，并向他线提交“变更影响分析报告”。

b) 互联互通授权后的本线地面设备变更，本线应向他线提交“变更影响分析报告”，各互联互通线路厂家对变更影响进行分析，形成是否影响他线的结论。假如变更不涉及互联互通安全、互联互通接口或互联互通数据，他线车载不需要更新相关授权；假如变更涉及互联互通安全、互联互通接口或互联互通数据，须与互联互通他线及各评估方达成一致，完成互联互通工厂和现场测试，且通过各自第三方安全评估

c) 互联互通授权后车载设备的变更，本线应向他线提交“变更影响分析报告”；假如变更涉及互联互通安全、互联互通接口或互联互通数据，须与互联互通他线及各评估方达成一致，完成互联互通工厂和现场测试，且通过各自第三方安全评估；假如变更不涉及互联互通安全、互联互通接口或互联互通数据，他线车载不需要更新相关授权，但地面总的授权应该更新。

d）涉及通用产品/通用应用安全相关功能的变更，本线需要向评估方提供产品第三方对应评估证据。

---

# 中国城市轨道交通协会团体标准   城市轨道交通 基于通信的列车运行   控制系统(CBTC)互联互通工程规范   第2部分:安全评估   T/CAMET 04013.2—2018

中国铁道出版社有限公司出版发行

（100054，北京市西城区右安门西街8号）

公司网址：http://www.tdpress.com

北京铭成印刷有限公司印刷

开本：880 mm×1230 mm 1/32 印张：0.75 字数：17千

2019年5月第1版 2019年5月第1次印刷

书号：15113·5710 定价：15.00 元

版权所有 侵权必究

凡购买铁道版图书，如有印制质量问题，请与本公司发行部联系调换。发行部电话：路（021）73174，市（010）51873174

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//22cca3f7-b48f-4914-ad4c-2a787f378d24/markdown_0/imgs/img_in_image_box_591_950_760_1081.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A37%3A17Z%2F-1%2F%2F6ce3f0badcf6be0fcdc6c8a08fa70ccbc2abb208a979b92593e8319631f2cc53" alt="Image" width="20%" /></div>


定价：15.00 元