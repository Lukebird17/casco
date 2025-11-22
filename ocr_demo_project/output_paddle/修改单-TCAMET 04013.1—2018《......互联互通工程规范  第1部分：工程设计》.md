# 中国城市轨道交通协会 《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通工程规范 第1部分：工程设计》(T/CAMET 04013.1—2018) 团体标准第1号修改单

本修改单经中国城市轨道交通协会于2024年09月03日批准发布，自2024年09月10日起实施。

## 一、 编辑性修改

1. 将第 3.1.10 条术语“保护区段 overlap section”修改为：“保护区段 overlap”。

2. 将第 3.1.13 条术语“安全保护距离 safe protection distance”修改为：“安全保护距离 safety margin”。

3. 将第 3.1.16 条术语“共线运行 mix operation”修改为：“共线运行 mixed operation”。

4. 将第3.1.18条术语“物理区段 physical track section，物理区段由安装在轨旁的计轴传感器进行分割，也称为计轴区段”修改为：“计轴区段 axle track section，由安装在轨旁的计轴传感器进行分割”。

5. 将第3.1.19条术语“逻辑区段是将较长的物理区段在逻辑上划分为若干个虚拟区段，作为CBTC系统中检测列车占用出清的最小单元。”修改为：“将较长的计轴区段在逻辑上划分为若干虚拟区段，作为CBTC系统中检测列车占用出清的最小单元。”

6. 增加第 3.2 条缩略语“SB: 有源应答器 (Switchable Balise)”

---

7. 将第5.2条应答器安装精度要求中“折返轨/存车线内应答器：±2 cm”修改为：“折返轨/存车线精确停车应答器：±2 cm”

8. 将第 12.2 条 ATS、CI 重叠区设置原则中“ATS、CI 重叠区的长度应不小于进路触发区段的长度”修改为：“ATS 重叠区的长度应不小于进路触发区段的长度”。

9. 将第14条临时限速区段划分原则中“临时限速区段划分应遵循如下原则：a) 在无岔区段中，按照逻辑区段进行划分；b) 在道岔区段内，按照三段式轨道区段进行划分。”修改为：“轨道区段划分应遵循如下原则：a) 在无岔区段中，按照计轴区段进行划分；b) 在道岔区段内，按照三段式进行划分。”

## 二、 技术性修改

1. 在第4.1条“区段划分原则”中：

1）将“a) 物理区段分界点（计轴点）应为轨道区段的分界点”修改为：“a) 计轴区段分界点（计轴点）应为轨道区段的分界点”

2）将“c)无岔物理区段内，轨道区段的边界点应为逻辑区段分界点”修改为：“c)无岔计轴区段内，轨道区段的边界点应为逻辑区段分界点”

3）将“e)单个物理区段内轨道区段总个数:不超过12个”修改为“e)单个计轴区段内轨道区段总个数:不超过12个。”

2. 将第 5.3 b) 条中“本规范中车站站台精确停车的位置，不同编组列车以站台两端对标停车”修改为：“本文件中车站站台精确停车的位置，不同编组均采用正方向运行站台端头停车的原则”。

3. 将第 5.4 条“车辆段/停车场与正线转换应答器布置原则”中“当车辆由车辆段/停车场进入正线时，需要在转换轨前布置两个轮径校正应答器，用于实现列车的轮径校准及列车初始定位。应答器布置间距为 20 米至 60 米（视工程项目具体情况确定）”，修改为：“当车辆由车辆段/停车场进入正线时，应在转换轨前布置至少两个轮径校正应答器，用于实现列车的轮径校准及列车初始定位。应答器布置间距为 20 米至 60 米（视

---

工程项目具体情况确定）。

4. 在第 5.5.2 条“有效站台(140 米)应答器布置原则”中：

1）将 a)“站台内 ATO 位置校正应答器距离出站方向的停车标的距离应符合表 1 的规定”修改为：“站台内 ATO 位置校正应答器距离出站方向的停车标的距离参考值如表 1 所示，工程项目根据具体情况确定”；

2）将表1标题“ATO校正应答器布置间距”修改为：“ATO校正应答器布置间距参考值”；

(3) 修改表 1 中长度值，表 1 修改为：

<div style="text-align: center;">表 1 ATO 校正应答器布置间距参考值（单位为米）</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>应答器间距</td><td style='text-align: center;'>长  度</td></tr><tr><td style='text-align: center;'>S1</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>S2</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S3</td><td style='text-align: center;'>站台中心点到FB2的距离±5</td></tr><tr><td style='text-align: center;'>S4</td><td style='text-align: center;'>站台边缘到FB3的距离±20</td></tr></table>

4）将b)“应用于双方向精确停车的应答器参考5.5.2的1)布置”修改为：“应用于双方向精确停车的应答器参考5.5.2的a)布置”；

5）将“站台内 ATO 位置校正应答器的距离应符合表 2 的规定”修改为：“站台内 ATO 位置校正应答器的距离参考值如表 2 所示，工程项目根据具体情况确定”；

6）将表 2 标题“双向 ATO 校正应答器布置间距”修改为：“双向 ATO 校正应答器布置间距参考值”；

7）修改表2中长度值，表2修改为：

---

<div style="text-align: center;">表 2 双向 ATO 校正应答器布置间距参考值(单位为米)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考点</td><td style='text-align: center;'>长度</td></tr><tr><td style='text-align: center;'>S1</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>S2</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S3</td><td style='text-align: center;'>0.5 * 短编组列车长度 - S1 - S2 ± 5</td></tr><tr><td style='text-align: center;'>S4</td><td style='text-align: center;'>0.5 * 短编组列车长度 - S1 - S2 ± 5</td></tr><tr><td style='text-align: center;'>S5</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S6</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>S7</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S8</td><td style='text-align: center;'>5</td></tr></table>

5. 在第 5.5.3 条“有效站台(120 米)应答器布置原则”中：

1）将 a)“站台内位置校正应答器距离出站方向的停车标的距离应符合表 3 的规定”修改为：“站台内位置校正应答器距离出站方向的停车标的距离参考值如表 3 所示，工程项目根据具体情况确定”；

2）将表3标题“ATO校正应答器布置间距”修改为：“ATO校正应答器布置间距参考值”；

3）修改表3中长度值，表3修改为：

<div style="text-align: center;">表 3 ATO 校正应答器布置间距参考值(单位为米)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参 考 点</td><td style='text-align: center;'>长 度</td></tr><tr><td style='text-align: center;'>S1</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>S2</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S3</td><td style='text-align: center;'>站台中心点到FB2的距离±5</td></tr><tr><td style='text-align: center;'>S4</td><td style='text-align: center;'>站台边缘到FB3的距离±20</td></tr></table>

---

4）将 b）“站台内位置校正应答器的距离应符合表 4 的规定”修改为：“站台内位置校正应答器的距离参考值如表 4 所示，工程项目根据具体情况确定”；

5）将表4标题“双向停车站台精确停车应答器布置”修改为：“双向停车站台精确停车应答器布置间距参考值”；

6）修改表4中长度值，表4修改为：

<div style="text-align: center;">表 4 双向停车站台精确停车应答器布置间距参考值(单位为米)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>参考点</td><td style='text-align: center;'>长度</td></tr><tr><td style='text-align: center;'>S1、S1&#x27;</td><td style='text-align: center;'>5</td></tr><tr><td style='text-align: center;'>S2、S2&#x27;</td><td style='text-align: center;'>10</td></tr><tr><td style='text-align: center;'>S3、S3&#x27;</td><td style='text-align: center;'>站台中心点到FB2、FB4的距离±5</td></tr></table>