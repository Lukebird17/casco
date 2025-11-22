# 中国城市轨道交通协会

# 《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范 第4部分：互联互通危害分析》(T/CAMET04010.4—2018) 团体标准第1号修改单

本修改单经中国城市轨道交通协会于2024年09月03日批准发布，自2024年09月10日起实施。

## 一、 编辑性修改

1. 将第2章中的“GB/T 32588.1—2016 轨道交通 自动化的城市轨道交通(AUGT) 安全要求 第1部分: 总则(IEC 6227:2009, MOD)”修改为: “GB/T 32588.1—2016 轨道交通 自动化的城市轨道交通(AUGT) 安全要求 第1部分: 总则(IEC 62267:2009, MOD)”

### 2. 术语修改：

a） 将术语 3.1.6 “跨线运行 overline operation” 修改为：“跨线运行 cross-line operation”。

b） 将术语 3.1.8 “共线运行 mix operation” 修改为：“共线运行 mixed operation”。

c） 删除术语 3.1.9 “上线测试 running test: 装备不同厂家车载设备的列车在本线进行动车测试”。

d) 删除术语 3.1.10“互联互通试运营 interoperational operation: 装备不同厂家车载设备的列车可以在装备不同厂家轨旁设备的多条轨道交通线路上满足互联互通功能要求，且系统性能满足工程要求，开始载客运营。”

---

e） 将术语 3.1.11 “本线 local line” 修改为：“本线/单线 local line”。

f） 删除术语 3.1.13“单线 single line”。

3. 缩略语修改：

a）将3.2缩略语中的“V0BC:车载控制器(Vehicle On-Board Controller)”修改为“V0BC:车载控制器(Vehicle Onboard Controller)”；

b） 在3.2 缩略语中增加“MSS:维护支持系统(Maintenance Support System)”。

3. 将 4.2.2 图 4 及图 5 中应答器作为外部设备与“计算机联锁”通信，将图 4 中与计算机联锁接口设备中第二个“轨道电路”修改为：“站台紧急停车按钮”。更换图 4 和图 5 为：

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//681f31ea-9b59-4e83-9264-fc13691c08cd/markdown_0/imgs/img_in_image_box_135_405_642_896.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A00%3A05Z%2F-1%2F%2F9aeab554fd950dae504204e3be2744a0099e376b6294b4f12f194e7105a00809" alt="Image" width="58%" /></div>


<div style="text-align: center;">图 4 单线 CBTC 系统架构示意图</div>


4. 完善表1、表2、表3和表4中细节描述：

a）将4.2.3表1“信号系统接口”列第三项“防淹门”修改为：“信号系统与防淹门接口”。

b）将4.2.4表2修改为：

---

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//87d7480b-99a4-42d4-99ce-ad7adb06709a/markdown_0/imgs/img_in_image_box_169_159_1175_748.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A00%3A02Z%2F-1%2F%2Fdf600fe05faf6e575baa37cc34b974c8a1e11da3758adf164ea4ae785d6f7af7" alt="Image" width="82%" /></div>


<div style="text-align: center;">图 5 互联互通 CBTC 系统架构示意图</div>

---

<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2" colspan="2">列车运行基本功能</td><td style='text-align: center;'>非限制人工驾驶模式</td><td style='text-align: center;'>限制人工驾驶模式</td><td style='text-align: center;'>列车自动防护下的人工驾驶模式</td><td style='text-align: center;'>列车自动驾驶模式</td></tr><tr><td style='text-align: center;'>EUM</td><td style='text-align: center;'>RM</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>AM</td></tr><tr><td rowspan="3">确保列车安全运行</td><td style='text-align: center;'>确保安全进路</td><td style='text-align: center;'>H并S(道岔控制由系统实现)</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保列车安全间隔</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保安全速度(包含:EBI、临时限速、牵引切除及恢复)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>驾驶列车运行</td><td style='text-align: center;'>控制牵引和制动(含ATP、ATO)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>S</td></tr><tr><td rowspan="2">轨道监控</td><td style='text-align: center;'>防止和障碍物碰撞</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td style='text-align: center;'>防止和人员碰撞</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td rowspan="3">乘客乘降监控</td><td style='text-align: center;'>控制乘客通行的车门</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>防止车体之间或站台与列车之间的人员伤亡</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td style='text-align: center;'>确保安全发车条件</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr></table>

---

## (续表)


<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2" colspan="2">列车运行基本功能</td><td style='text-align: center;'>非限制人工驾驶模式</td><td style='text-align: center;'>限制人工驾驶模式</td><td style='text-align: center;'>列车自动防护下的人工驾驶模式</td><td style='text-align: center;'>列车自动驾驶模式</td></tr><tr><td style='text-align: center;'>EUM</td><td style='text-align: center;'>RM</td><td style='text-align: center;'>CM</td><td style='text-align: center;'>AM</td></tr><tr><td rowspan="2">列车运行控制</td><td style='text-align: center;'>投入或退出运营</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td><td style='text-align: center;'>H并S</td></tr><tr><td style='text-align: center;'>监控列车状态(包含列车完整性、紧急制动实施、车门状态)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td><td style='text-align: center;'>S</td></tr><tr><td style='text-align: center;'>确保紧急情况的检测和管理</td><td style='text-align: center;'>列车性能诊断,烟/火检测,紧急情况处理(呼叫/疏散,监控)</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td><td style='text-align: center;'>H</td></tr><tr><td colspan="6">注:
H=运营人员职责
S=由信号系统实现
并:运营人员和系统共同实现安全功能。</td></tr></table>

---

c) 将6.2表3“事故场景初步分解”列、“1级编号”为“Ref-21”行的“基础措施过度承载”修改为：“基础设施过度承载”。表3修改部分如下：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>事故</td><td style='text-align: center;'>1级编号</td><td style='text-align: center;'>事故场景初步分解</td><td style='text-align: center;'>2级编号</td><td style='text-align: center;'>事故场景细化分解</td></tr><tr><td style='text-align: center;'>灾难</td><td style='text-align: center;'>Ref-20</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td rowspan="2">基础建设损坏</td><td style='text-align: center;'>Ref-21</td><td style='text-align: center;'>基础设施过度承载</td><td style='text-align: center;'>Ref-21.1</td><td style='text-align: center;'>桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故</td></tr><tr><td style='text-align: center;'>Ref-22</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr></table>

d) 将6.3表4（第126页）“事故场景”列、“编号”为“Ref-21.1”行的“基础措施超负荷承载”修改为：“桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故”。将“互联互通”列、“编号”为“Ref-21.1”行的“基础措施超负荷承载”修改为：“桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故”。表4修改部分如下：

5. 完善安全要求的描述：

a）在6.3表4（第19页）和7.3表15（第145页）中，将建设运营维护需求SR-O-1“营运责任方制定计轴直接复位的操作规范，运营人员必须确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作”修改为：“运营责任方制定计轴直接复位的操作规范，运营人员应确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作”。



b) 在6.3表4（第102页）和7.1.6表13（第142页）中，将系统需求SR-S-75“信号系统应保证CBTC列车在防淹门进路停稳，方可允许关闭防淹门”修改为：“信号系统应保证CBTC列车在防淹门所属进路的进路外方停稳，方可允许关闭防淹门”。

---

<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td style='text-align: center;'>Ref-20</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td rowspan="2">Ref-21.1</td><td rowspan="2">桥梁同时存在列车数量过多,导致桥梁损坏,从而导致行车事故</td><td rowspan="2">PH-107</td><td rowspan="2">桥梁同时存在列车数量过多,导致桥梁损坏,从而导致行车事故</td><td rowspan="2">SHA-69</td><td rowspan="2">桥梁同时存在列车数量超出设计载荷造成桥梁损坏,导致行车事故</td><td style='text-align: center;'>SR-S-111</td><td style='text-align: center;'>信号系统应保证同时存在于桥梁的列车少于等于桥梁允许运营载荷要求</td><td style='text-align: center;'>/</td></tr><tr><td style='text-align: center;'>SR-O-48</td><td style='text-align: center;'>信号系统失效后,运营责任方应制定运营细则,保证同时存在于桥梁的列车少于等于桥梁允许运营载荷要求</td><td style='text-align: center;'>/</td></tr><tr><td style='text-align: center;'>Ref-22.1</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr></table>

---

c) 在6.3表4(第123页)和7.3表15(第148页)中，将建设运营维护需求SR-O-42“运营单位确保信号系统运营环境、电磁环境正常”修改为：“运营责任方确保信号系统运营环境、电磁环境正常”。

d) 在6.3表4（第127页）和7.3表15（第148页）中，将建设运营维护需求SR-O-47“信号系统无法检测或防护基础设施坍塌导致行车事故，运营责任方应运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响”修改为：“信号系统无法检测或防护基础设施坍塌导致行车事故，运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响”。

6. 参考文献删除“ $$ 12 $$  GB/T 21562—2008 轨道交通可靠性、可用性、可维护性和安全性规范及示例（IEC 62278:2002 IDT）”。

## 二、 技术性修改

1. 在第 2 章中增加“TB/T 3485—2017 应答器传输系统技术条件”。

2. 修改安全要求的描述：

a）在6.3表4（第20、49、55、57（两处）、100、106和111页）和7.2表14（第143页）中，将互联互通接口需求SR-I-2“V0BC和ZC间通信采用RSSP-Ⅱ安全通信协议”修改为：“V0BC和ZC间通信采用RSSP-I或RSSP-Ⅱ安全通信协议”。

b) 在6.3表4（第24、26、27、28、29（两处）、32、33、35、37、40（两处）、41和135页）和7.1.4表I1（第141页）中，将系统需求SR-S-25“互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应≥各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP输出紧急制动”修改为：“互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应大于或等于各厂商本线的最大

---

退行停车距离；列车退行超过所运行线路最大退行EB触发距离时，车载ATP输出紧急制动”。

在6.3表4（第26、27、30、31（两处）、32、34（两处）、36、37、39、41、42和136页）和7.1.4表11（第141页）中，将系统需求SR-S-33“互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP输出紧急制动”修改为：“互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应大于或等于各厂商本线的最大后溜停车距离；列车后溜超过所运行线路最大后溜EB触发距离时，车载ATP输出紧急制动”。

d）在6.3表4（第56和115页）和7.2表14（第144页）中，将互联互通接口需求SR-I-24“VOBC和CI间通信采用RSSP-II安全通信协议”修改为：“VOBC和CI间通信采用RSSP-I或RSSP-II安全通信协议”。

e) 在 6.3 表 4（第 100 页）和 7.1.5 表 12（第 142 页）中，将系统需求 SR-S-73“车地应答器通信应满足欧标要求”修改为：“车地应答器通信应满足 TB/T 3485 的要求”。

3. 在6.3表4（第110页）危害编号“SHA-40”对应的“安全需求”中增加SR-O-51，并在7.3表15（第148页）中，增加运营维护安全要求SR-O-51“道岔维护符合道岔专业相关规定（如道岔安装/维护后进行密贴检查）”。表4修改部分和表15修改部分如下：

4. 在 7.1.3 表 10（第 140 页）中，删除安全需求编号为 SR-S-87、SR-S-88 和 SR-S-90 的行；在 7.1.6 表 13（第 142 页）中，增加安全需求 SR-S-87、SR-S-88 和 SR-S-90。表 10 修改部分和表 13 修改部分如下：

---

<div style="text-align: center;">表 4 互联互通危害分析(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td rowspan="4">Ref-4.1</td><td rowspan="4">列车失去运行方向引导</td><td rowspan="4">PH-77</td><td rowspan="4">列车在道岔区域时，道岔动作导致列车脱轨</td><td rowspan="4">SHA-40</td><td rowspan="4">列车在道岔区域时，道岔动作</td><td style='text-align: center;'>SR-S-88</td><td style='text-align: center;'>道岔转换完毕后，应保证道岔固定在规定位置不再移动</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-89</td><td style='text-align: center;'>道岔受进路锁闭、区段锁闭、人工单独锁闭或区段占用时，联锁须不能控制道岔移动</td><td style='text-align: center;'>进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-S-90</td><td style='text-align: center;'>只有当道岔位置与操作要求一致，并经检查自动开闭器的两组接点排的相应接点位置正确，才能构成道岔位置的正确表示</td><td style='text-align: center;'>进路办理、进路/区段锁闭</td></tr><tr><td style='text-align: center;'>SR-O-51</td><td style='text-align: center;'>道岔维护符合道岔专业相关规定（如道岔安装/维护后进行密贴检查）</td><td style='text-align: center;'>—</td></tr></table>

---

<div style="text-align: center;">表 4 互联互通危害分析(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">编号</td><td rowspan="2">事故场景</td><td rowspan="2">编号</td><td rowspan="2">互联互通</td><td rowspan="2">危害编号</td><td rowspan="2">互联互通信号系统场景危害分解</td><td colspan="2">安全要求</td><td rowspan="2">系统功能</td></tr><tr><td style='text-align: center;'>编号</td><td style='text-align: center;'>安全要求/运用限制条件</td></tr><tr><td style='text-align: center;'>Ref-4.1</td><td style='text-align: center;'>列车失去运行方向引导</td><td style='text-align: center;'>PH-78</td><td style='text-align: center;'>轨道断裂导致列车脱轨</td><td style='text-align: center;'>OSHA-25</td><td style='text-align: center;'>轨道断裂导致列车脱轨</td><td style='text-align: center;'>SR-O-28</td><td style='text-align: center;'>轨道采购及维护符合轨道专业相关规定</td><td style='text-align: center;'>—</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr></table>

<div style="text-align: center;">表 15 互联互通建设运营维护安全要求列表(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>SR-O-50</td><td style='text-align: center;'>运营责任方针对跨线救援与疏散制定作业细则</td></tr><tr><td style='text-align: center;'>SR-O-51</td><td style='text-align: center;'>道岔维护符合道岔专业相关规定（如道岔安装/维护后进行密贴检查）</td></tr></table>

---

<div style="text-align: center;">表 10 联锁系统安全要求列表(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>……</td><td style='text-align: center;'>……</td></tr><tr><td style='text-align: center;'>SR-S-86</td><td style='text-align: center;'>联锁控制道岔的命令必须同排列的进路中道岔的位置一致，同时锁闭道岔，联锁设备才能建立进路</td></tr><tr><td style='text-align: center;'>SR-S-89</td><td style='text-align: center;'>道岔受进路锁闭、区段锁闭、人工单独锁闭或区段占用时，联锁须不能控制道岔移动</td></tr><tr><td style='text-align: center;'>SR-S-92</td><td style='text-align: center;'>CI监控站台门的开启和关闭状态，如果站台门打开，应关闭与该屏蔽门相关联的进路</td></tr></table>

<div style="text-align: center;">表 13 其他安全要求列表(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>安全要求编号</td><td style='text-align: center;'>安全要求</td></tr><tr><td style='text-align: center;'>......</td><td style='text-align: center;'>......</td></tr><tr><td style='text-align: center;'>SR-S-75</td><td style='text-align: center;'>信号系统应保证CBTC列车在防淹门所属进路的进路外方停稳，方可允许关闭防淹门</td></tr><tr><td style='text-align: center;'>SR-S-87</td><td style='text-align: center;'>道岔子系统能给出正确的道岔状态表示</td></tr><tr><td style='text-align: center;'>SR-S-88</td><td style='text-align: center;'>道岔转换完毕后，应保证道岔固定在规定位置不再移动直至下次联锁或人工转换道岔命令下达</td></tr><tr><td style='text-align: center;'>SR-S-90</td><td style='text-align: center;'>只有当道岔位置与操作要求一致，并经检查自动开闭器的两组接点排的相应接点位置正确，才能构成道岔位置的正确表示</td></tr><tr><td style='text-align: center;'>SR-S-98</td><td style='text-align: center;'>信号设备的硬件、机械结构零部件不能使用易燃材料</td></tr></table>