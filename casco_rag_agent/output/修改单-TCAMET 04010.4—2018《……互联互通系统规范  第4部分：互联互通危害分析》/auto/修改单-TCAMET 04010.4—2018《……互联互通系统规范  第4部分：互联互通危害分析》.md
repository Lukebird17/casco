# 中国城市轨道交通协会

# 《城市轨道交通基于通信的列车运行控制系统(CBTC)互联互通系统规范第4部分：互联互通危害分析》(T/CAMIET04010.4—2018)团体标准第1号修改单

本修改单经中国城市轨道交通协会于2024 年09 月03日批准发布，自2024年09月10日起实施。

# 一、编辑性修改

1．将第2章中的“GB/T32588.1—2016轨道交通自动化的城市轨道交通（AUGT）安全要求第1部分：总则（IEC6227：2009，MOD）”修改为：“GB/T32588.1—2016轨道交通自动化的城市轨道交通（AUGT）安全要求第1部分：总则（IEC62267:2009，MOD） '

2.术语修改：

a) 将术语3.1.6“跨线运行overline operation”修改为：“跨线运行cros-ine operatio  
b) 将术语3.1.8“共线运行mix operation”修改为：“共线运行mixed oprtion"  
c ) 删除术语3.1.9“上线测试running test:装备不同厂家车载设备的列车在本线进行动车测试”。  
d) 删除术语3.1. 10“互联互通试运营 interoperabetrial operation:装备不同厂家车载设备的列车可以在装备不同厂家轨旁设备的多条轨道交通线路上满足互联互通功能要求，且系统性能满足工程要求，开始载客运营。”

e）将术语 3.1.11“本线local line”修改为：“本线/单线 local line”。

f） 删除术语3.1.13“单线 single line”。

3.缩略语修改:

a) 将3.2 缩略语中的“VOBC:车载控制器(Vehicle On-Board Controller)”修改为“VOBC:车载控制器（Vehicle Onboard Controller)”;

b）在3.2 缩略语中增加“MSS:维护支持系统(Maintenance Support System)”。

3.将4.2.2 图4 及图5 中应答器作为外部设备与“计算机联锁”通信，将图4中与计算机联锁接口设备中第二个“轨道电路”修改为：“站台紧急停车按钮”。更换图4和图5为：

![](images/6031496d7b94329b16d9b8d838518db9b036c7fdbe02d82efbb620a0f5d8b463.jpg)  
图4单线CBTC 系统架构示意图

4.完善表1、表2、表3和表4中细节描述：

a) 将4.2.3表1“信号系统接口”列第三项“防淹门”修改为：“信号系统与防淹门接口”。

b）将4.2.4表2修改为：

![](images/9f95a304a9a263201f405ef250d4062a2fe2c0c373610a2a0b51c990da2f3d5a.jpg)

<table><tr><td rowspan=2 colspan=2>C列车运行基本功能</td><td rowspan=1 colspan=1>非限制人工驾驶模式</td><td rowspan=1 colspan=1>限制人工驾驶模式</td><td rowspan=1 colspan=1>列车自动防护下的人工驾驶模式</td><td rowspan=1 colspan=1>列车自动驾驶模式</td></tr><tr><td rowspan=1 colspan=1>EUM</td><td rowspan=1 colspan=1>RM</td><td rowspan=1 colspan=1>CM</td><td rowspan=1 colspan=1>AM</td></tr><tr><td rowspan=3 colspan=1>确保列车安全运行</td><td rowspan=1 colspan=1>确保安全进路</td><td rowspan=1 colspan=1>H并S（道岔控制由系统实现）</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>确保列车安全间隔</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>确保安全速度（包含：EBI、临时限速、牵引切除及恢复)</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>H并S</td></tr><tr><td rowspan=1 colspan=1>驾驶列车运行</td><td rowspan=1 colspan=1>控制牵引和制动（含ATP、ATO)</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=2 colspan=1>轨道监控</td><td rowspan=1 colspan=1>防止和障碍物碰撞</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td></tr><tr><td rowspan=1 colspan=1>防止和人员碰撞</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td></tr><tr><td rowspan=3 colspan=1>乘客乘降监控</td><td rowspan=1 colspan=1>控制乘客通行的车门</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>台与列车之间的人员伤亡</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>确保安全发车条件</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>H并S</td></tr></table>

<table><tr><td rowspan=2 colspan=2>列车运行基本功能</td><td rowspan=1 colspan=1>非限制人工驾驶模式</td><td rowspan=1 colspan=1>限制人工驾驶模式</td><td rowspan=1 colspan=1>列车自动防护下的人工驾驶模式</td><td rowspan=1 colspan=1>列车自动驾驶模式</td></tr><tr><td rowspan=1 colspan=1>EUM</td><td rowspan=1 colspan=1>RM</td><td rowspan=1 colspan=1>CM</td><td rowspan=1 colspan=1>AM</td></tr><tr><td rowspan=2 colspan=1>列车运行控制</td><td rowspan=1 colspan=1>投入或退出运营</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>H并S</td><td rowspan=1 colspan=1>H并S</td></tr><tr><td rowspan=1 colspan=1>监控列车状态（包含列车完整性、紧急制动实施、车门状态）</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>S</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>S</td></tr><tr><td rowspan=1 colspan=1>确保紧急情况的检测和管理</td><td rowspan=1 colspan=1>列车性能诊断，烟/火检测，紧急情况处理(呼叫/疏散，监控)</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>H</td></tr><tr><td rowspan=1 colspan=6>注：H=运营人员职责S=由信号系统实现0并：运营人员和系统共同实现安全功能。</td></tr></table>

c ) 将6.2表3“事故场景初步分解”列、“1级编号”为“Ref-21”行的“基础措施过度承载”修改为：“基础设施过度承载”。表3修改部分如下：

<table><tr><td rowspan=1 colspan=1>事故</td><td rowspan=1 colspan=1>1级编号</td><td rowspan=1 colspan=1>事故场景初步分解</td><td rowspan=1 colspan=1>2级编号</td><td rowspan=1 colspan=1>事故场景细化分解</td></tr><tr><td rowspan=1 colspan=1>灾难</td><td rowspan=1 colspan=1>Ref-20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1>基础建设损坏</td><td rowspan=1 colspan=1>Ref-21</td><td rowspan=1 colspan=1>X基础设施过度承载</td><td rowspan=1 colspan=1>Ref-21.1</td><td rowspan=1 colspan=1>桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故</td></tr><tr><td rowspan=1 colspan=1>Ref-22</td><td rowspan=1 colspan=1>。</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·</td></tr></table>

d) 将6.3表4（第126页）“事故场景”列、“编号”为“Ref-21.1”行的“基础措施超负荷承载”修改为：“桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故”。将“互联互通”列、“编号”为“Ref-21.1”行的“基础措施超负荷承载”修改为：“桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车事故”。表4修改部分如下：

5．完善安全要求的描述：

a）在6.3表4(第19页)和7.3表15（第145页)中，将建设运营维护需求SR-O-1“营运责任方制定计轴直接复位的操作规范，运营人员必须确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作”修改为：“运营责任方制定计轴直接复位的操作规范，运营人员应确定该计轴区段确实无列车或者其他障碍物占用或接近，方可进行直接复位操作”。

b）在6.3表4(第102页)和7.1.6表13(第142页）中，将系统需求 SR-S-75“信号系统应保证CBTC列车在防淹门进路停稳，方可允许关闭防淹门”修改为：“信号系统应保证CBTC列车在防淹门所属进路的进路外方停稳，方可允许关闭防淹门”。

<table><tr><td rowspan=2 colspan=1>编号</td><td rowspan=2 colspan=1>事故场景</td><td rowspan=2 colspan=1>编号</td><td rowspan=2 colspan=1>互联互通</td><td rowspan=2 colspan=1>危害编号</td><td rowspan=2 colspan=1>互联互通信号系统场景危害分解</td><td rowspan=1 colspan=2>安全要求</td><td rowspan=2 colspan=1>系统功能</td></tr><tr><td rowspan=1 colspan=1>编号</td><td rowspan=1 colspan=1>安全要求/运用限制条件</td></tr><tr><td rowspan=1 colspan=1>Ref-20</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>.</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>…</td></tr><tr><td rowspan=2 colspan=1>Ref-21.1</td><td rowspan=2 colspan=1>公2桥梁同时存在列车数量过多，导致桥PH-107梁损坏，从而导致行车事故</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>桥梁同时存在列车数量过多，导致桥梁损坏，从而导致行车</td><td rowspan=2 colspan=1>SHA-69</td><td rowspan=2 colspan=1>桥梁同时存在列车数量超出设计载荷造成桥梁损坏，导致行车事故</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>信号系统应保证同时存在于桥梁的</td><td rowspan=1 colspan=1>1</td></tr><tr><td rowspan=1 colspan=1>SR-0-48</td><td rowspan=1 colspan=1>信号系统失效后,运营责任方应制定运营细则，保证同时存在于桥梁的列车少于等于桥梁允许运营载荷要求</td><td rowspan=1 colspan=1>/</td></tr><tr><td rowspan=1 colspan=1>Ref-22.1</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>··.</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1>·····</td><td rowspan=1 colspan=1>…</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>·····</td></tr></table>

c）在6.3表4(第123页)和7.3表15(第148页）中，将建设运营维护需求SR-O-42“运营单位确保信号系统运营环境、电磁环境正常”修改为：“运营责任方确保信号系统运营环境、电磁环境正常”。

d）在6.3表4(第127页)和7.3表15(第148页)中,将建设运营维护需求SR-O-47“信号系统无法检测或防护基础设施坍塌导致行车事故，运营责任方应运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响”修改为：“信号系统无法检测或防护基础设施坍塌导致行车事故，运营责任方应制定基础设施坍塌应急预案，避免或减轻事故影响”。

6.参考文献删除“[12GB/T 21562—2008 轨道交通可靠性、可用性、可维护性和安全性规范及示例（IEC 62278:2002 IDT）”。

# 二、技术性修改

1．在第2 章中增加“TB/T 3485—2017 应答器传输系统技术条件”。

2.修改安全要求的描述：

a）在6.3表4（第20、49、55、57（两处）、100、106和111页）和7.2表14（第143页）中，将互联互通接口需求SR-I-2“VOBC和ZC间通信采用RSSP-Ⅱ安全通信协议”修改为：“VOBC和ZC间通信采用RSSP-I或RSSP-II安全通信协议”。

b）在6.3表4（第24、26、27、28、29（两处）、32、33、35、37、40（两处）、41和135页）和7.1.4表11（第141页）中，将系统需求SR-S-25“互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应 $\geqslant$ 各厂商本线的最大退行停车距离；列车退行超过互联互通最大退行停车距离时，车载ATP 输出紧急制动”修改为：“互联互通列车在CBTC、ITC级别下移动授权防护中最大退行停车距离应大于或等于各厂商本线的最大退行停车距离；列车退行超过所运行线路最大退行EB触发距离时，车载ATP输出紧急制动”。 K

c）在6.3表4（第26、27、30、31（两处）、32、34（两处）、36、37、39、41、42和136页）和7.1.4表11（第141页）中，将系统需求SR-S-33“互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应≥各厂商本线的最大后溜停车距离；列车后溜超过互联互通最大后溜停车距离时，车载ATP 输出紧急制动”修改为：“互联互通列车在CBTC、ITC级别下移动授权防护中最大后溜停车距离应大于或等于各厂商本线的最大后溜停车距离;列车后溜超过所运行线路最大后溜 EB 触发距离时，车载ATP输出紧急制动”。

d）在6.3表4(第56和115页)和7.2表14(第144页)中,将互联互通接口需求SR-I-24“VOBC和CI间通信采用RSSP-ⅡI安全通信协议”修改为：“VOBC和CI间通信采用RSSP-I或RSSP-ⅡI安全通信协议”。

e)在6.3表4(第100页)和7.1.5表12(第142页)中，将系统需求SR-S-73“车地应答器通信应满足欧标要求”修改为：“车地应答器通信应满足TB/T3485的要求”。

3.在6.3表4（第110页）危害编号“SHA-40”对应的“安全需求”中增加 SR-0-51,并在7.3表15（第148页)中,增加运营维护安全要求 SR-0-51“道岔维护符合道岔专业相关规定（如道岔安装/维护后进行密贴检查）”。表4修改部分和表15修改部分如下：

4.在7.1.3表10(第140 页)中,删除安全需求编号为SR-S-87、SR-S-88和SR-S-90的行;在7.1.6表13(第142页)中，增加安全需求SR-S-87、SR-S-88 和SR-S-90。表10修改部分和表13修改部分如下：

<table><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>编号事故场景</td><td rowspan=2 colspan=1>编号</td><td rowspan=2 colspan=1>互联互通</td><td rowspan=2 colspan=1>危害编号</td><td rowspan=2 colspan=1>互联互通信号系统场景危害分解</td><td rowspan=1 colspan=2>安全要求</td><td rowspan=2 colspan=1>系统功能</td></tr><tr><td rowspan=1 colspan=1>编号</td><td rowspan=1 colspan=1>安全要求/运用限制条件</td></tr><tr><td rowspan=4 colspan=1>Ref-4.1</td><td rowspan=4 colspan=1>列车失去运行方向引导</td><td rowspan=4 colspan=1></td><td rowspan=4 colspan=1>PH-77域时，道岔动作导致列车脱轨示通協管</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>道岔转换完毕后，应保证道岔固定在规定位置不再移动</td><td rowspan=1 colspan=1>进路/区段锁闭</td></tr><tr><td rowspan=1 colspan=1>SR- S-89</td><td rowspan=1 colspan=1>道岔受进路锁闭、区段锁闭、人工单独锁闭或区段占用时，联锁须不能控制道岔移动</td><td rowspan=1 colspan=1>进路/区段锁闭</td></tr><tr><td rowspan=2 colspan=1>SHA-40</td><td rowspan=2 colspan=1>列车在道岔区域时,道岔动作</td><td rowspan=1 colspan=1>SR-S-90</td><td rowspan=1 colspan=1>只有当道岔位置与操作要求一致，并经检查自动开闭器的两组接点排的相应接点位置正确，才能构成道岔位置的正确表示</td><td rowspan=1 colspan=1>进路办理、进路/区段锁闭</td></tr><tr><td rowspan=1 colspan=1>SR-0-51</td><td rowspan=1 colspan=1>道岔维护符合道岔专业相关规定（如道岔安装/维护后进行密贴检查）</td><td rowspan=1 colspan=1>R一</td></tr></table>

<table><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>编号事故场景</td><td rowspan=2 colspan=1>编号</td><td rowspan=2 colspan=1>互联互通</td><td rowspan=2 colspan=1>危害编号</td><td rowspan=2 colspan=1>互联互通信号系统场景危害分解</td><td rowspan=1 colspan=2>安全要求</td><td rowspan=2 colspan=1>系统功能</td></tr><tr><td rowspan=1 colspan=1>编号</td><td rowspan=1 colspan=1>安全要求/运用限制条件</td></tr><tr><td rowspan=1 colspan=1>Ref-4.1</td><td rowspan=1 colspan=1>列车失去运行方向引导</td><td rowspan=1 colspan=1>PH-78</td><td rowspan=1 colspan=1>轨道断裂导致列车脱轨</td><td rowspan=1 colspan=1>OSHA-25</td><td rowspan=1 colspan=1>轨道断裂导致列车脱轨</td><td rowspan=1 colspan=1>SR-0-28</td><td rowspan=1 colspan=1>轨道采购及维护符合轨道专业相关规定</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

<table><tr><td>安全要求编号</td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td>SR- 0-50</td><td>运营责任方针对跨线救援与疏散制定作业细则</td><td></td></tr><tr><td></td><td></td><td></td></tr></table>

# 表10联锁系统安全要求列表(续表)

<table><tr><td rowspan=1 colspan=1>安全要求编号</td><td rowspan=1 colspan=1>安全要求                 S</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>00</td></tr><tr><td rowspan=1 colspan=1>SR-S-86</td><td rowspan=1 colspan=1>联锁控制道岔的命令必须同排列的进路中道岔的位置一致，同时锁闭道岔，联锁设备才能建立进路</td></tr><tr><td rowspan=1 colspan=1>SR-S-89</td><td rowspan=1 colspan=1>道岔受进路锁闭、区段锁闭、人工单独锁闭或区段占用时，联锁须不能控制道岔移动</td></tr><tr><td rowspan=1 colspan=1>SR-S-92</td><td rowspan=1 colspan=1>CI监控站台门的开启和关闭状态，如果站台门打开，应关闭与该屏蔽门相关联的进路</td></tr></table>

![](images/16d2ab55a5f58a2065c07fb7b0bbcd6df7ddb30a7d0deb8115ca7fda71a089fb.jpg)

# 表13其他安全要求列表(续表）

<table><tr><td rowspan=1 colspan=1>安全要求编号</td><td rowspan=1 colspan=1>安全要求</td></tr><tr><td rowspan=1 colspan=1>··</td><td rowspan=1 colspan=1>····</td></tr><tr><td rowspan=1 colspan=1>SR-S-75</td><td rowspan=1 colspan=1>信号系统应保证CBTC列车在防淹门所属进路的进路外方停稳，方可允许关闭防淹门</td></tr><tr><td rowspan=1 colspan=1>SR-S-87</td><td rowspan=1 colspan=1>道岔子系统能给出正确的道岔状态表示             K</td></tr><tr><td rowspan=1 colspan=1>SR-S-88</td><td rowspan=1 colspan=1>道岔转换完毕后，应保证道岔固定在规定位置不再移动直至下次联锁或人工转换道岔命令下达</td></tr><tr><td rowspan=1 colspan=1>SR-S-90</td><td rowspan=1 colspan=1>只有当道岔位置与操作要求一致，并经检查自动开闭器的两组接点排的相应接点位置正确，才能构成道岔位置的正确表示</td></tr><tr><td rowspan=1 colspan=1>SR-S-98</td><td rowspan=1 colspan=1>信号设备的硬件、机械结构零部件不能使用易燃材料</td></tr></table>