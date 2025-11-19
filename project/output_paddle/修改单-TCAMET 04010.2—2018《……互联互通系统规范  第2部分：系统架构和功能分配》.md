# 中国城市轨道交通协会

# 《城市轨道交通 基于通信的列车运行控制系统 (CBTC) 互联互通系统规范 第 2 部分：系统架构和功能分配》(T/CAMET 04010.2—2018) 团体标准第 1 号修改单

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//ee150d56-5b30-4459-b2b6-20f19c664b8b/markdown_0/imgs/img_in_image_box_111_419_231_504.jpg?authorization=bce-auth-v1%2F5cfe9a5e1454405eb2a975c43eace6ec%2F2025-11-16T16%3A21%3A45Z%2F-1%2F%2F24515fc4c5b9a37e718be0d0d646eb5b134fb17c853c070065f71f0b54e32f6e" alt="Image" width="13%" /></div>


本修改单经中国城市轨道交通协会于2024年09月03日批准发布，自2024年09月10日起实施。

## 一、 编辑性修改

1. 在 3.1.9 中，增加来源信息 $$ T/CAMET 04010.1，定义 3.1.8 $$ 。

2. 将 3.1.10 中“保护区段 overlap section”修改为“保护区段 overlap”。

3. 将 3.1.13 的“安全保护距离 safe protection distance”修改为“安全保护距离 safety margin”。

4. 将 3.1.18 的“共线运行 mix operation”修改为“共线运行 mixed operation”。

5. 将 3.2 的“CM:列车自动防护模式(Code Train Operating Mode)”修改为“CM:列车自动防护模式(Coded Train Operating Mode)”。

6. 将表1中的“序号”为“70”所对应的“总体要求中的功能点名称”列中的“进路解锁及取消”修改为“进路/区段锁闭和解锁”。

7. 将图 3 中的“6.2.4 列车轮径校正”修改为“6.2.3.6 列车轮径校正”；将“6.2.4.2 确定列车停站位置”修改为“6.2.3.8 确定列车停站位”

---

置”；将“6.2.3.3 前方 CBTC 列车位置”修改为“6.3.2.2 前方 CBTC 列车位置”。

8. 将图 4 中的“6.2.4 列车轮径校正”修改为“6.2.3.6 列车轮径校正”。将“6.2.4.2 确定列车停站位置”修改为“6.2.3.8 确定列车停站位置”；将“6.2.3.3 前方 CBTC 列车位置”修改为“6.3.2.2 前方 CBTC 列车位置”。

9. 将表 3 的标题名称“进从设备故障中恢复的 CBTC 列车完成位置初始化”修改为：“从设备故障中恢复的 CBTC 列车完成位置初始化”。

10. 将表6的标题名称“确定CBT列车位置”修改为：“确定CBTC列车位置”。

11. 将图 5 中的“6.2.3.3 前方 CBTC 列车位置”修改为“6.3.2.2 前方 CBTC 列车位置”；将“6.3.2.3 安全进路的限定”的虚线框修改为实线框。

12. 将 6.3.2.2 标题名称“CBTC 列车前方位置”修改为“前方 CBTC 列车位置”。

13. 将表 18 的标题名称“CBTC 列车前方位置”修改为“前方 CBTC 列车位置”。

14. 将6.4.3.1的描述“表28规定了临时限速限制防护问题”修改为：“表28规定了临时限速防护功能”。

15. 将6.7.3.3的描述“当退行距离和退行速度超过允许值”修改为：“当退行距离或退行速度超过允许值”。

16. 将6.8.2.2的条件d)项“保持制动已施加”修改为：“保持制动或紧急制动已施加”。

17. 将6.8.2.3的条件d)项“保持制动已施加”修改为：“保持制动或紧急制动已施加”。

18. 将6.8.3.3的描述“系统方允许列车移动CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；”修改为：“系统方允许列车移动。CBTC等级下，当站台门锁闭状态丢失时，还未进站的列车应根据接收到的移动授权，控制列车在站台前停车；”。

---

19. 将表 49 的标题名称“车门防护”修改为：“站台门防护”。

20. 将7.2.1的描述“CBTC系统应为列车确定ATO曲线ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行、减速和制动的合理控制。”修改为：“CBTC系统应为列车确定ATO曲线。ATO子系统在ATP子系统的保护下，根据ATS子系统的命令，实现对列车的自动驾驶、列车在区间运行的自动调整，并可实现列车的节能运行控制。ATO子系统可控制列车按运行图规定的区间走行时分行车，自动完成对列车的启动、加速、巡航、惰行和制动的合理控制。”

### 21. 将表 66 的描述


<table border=1 style='margin: auto; width: max-content;'><tr><td colspan="4">子功能 #7.3.2.2: 关闭站台门CBTC 系统应能自动或者人工关闭站台门</td></tr><tr><td colspan="4">功能分配:</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

修改为：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CI</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>

---

22. 将8.2.2的描述“列车识别号应由列车表号、车次号、车组号、目的地号组成。”修改为：“列车识别号宜由列车表号、车次号、车组号、目的地号组成。”

23. 将8.3的描述“列车的前后位置应该依据CBTC列车位置报告来进行追踪并显示在ATS用户界面上列车在车辆段/停车场内运行时应具有车组号的跟踪、显示功能。”修改为：“列车的前后位置应依据CBTC列车位置报告进行追踪，并显示在ATS用户界面上。列车在车辆段/停车场内运行时，应具有车组号的跟踪、显示功能”。

24. 将8.6.4的描述“在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号列车进路控制权的优先级为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制。”修改为：“在紧急情况下，车站值班员可在控制工作站上强行取得控制权，控制车站的进路和信号。列车进路控制权的优先级为本地控制优先于中央控制；在本地控制或中央控制时，人工控制优先于自动控制。”

25. 将 8.7 的标题“控制列车运行”修改为“临时限速”。

26. 将8.10.1的描述“a)精确的和区域相关的信息；”修改为：“a)区域相关的信息；”将“d)被控列车运行相关的信息，如防护区段信息、锁闭的进路/区段以及临时限速极限和限速值”修改为：“d)被控列车运行相关的信息，如防护区段信息、锁闭的进路/区段以及临时限速值。”

27. 将8.10.2.3的描述“ATS子系统可将自身的报警信息、ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站。”修改为：“ATS子系统应将自身的报警信息、宜将ATP车载子系统、ATO子系统、CI子系统的报警信息传至控制中心维护工作站、车站维护工作站、综合维修中心的信号监测报警工作站。”

## 二、 技术性修改

1. 删除6.7.3.3的描述“退行距离超过限制，车载设备应丢失定位”。

---

### 2. 将表 50 的描述


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC 车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr></table>

修改为：


<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>功能分配</td><td style='text-align: center;'>输入</td><td style='text-align: center;'>实现</td><td style='text-align: center;'>输出</td></tr><tr><td style='text-align: center;'>ATS</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC轨旁</td><td style='text-align: center;'></td><td style='text-align: center;'></td><td style='text-align: center;'></td></tr><tr><td style='text-align: center;'>CBTC车载</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td><td style='text-align: center;'>X</td></tr><tr><td style='text-align: center;'>车辆(外部接口)</td><td style='text-align: center;'>X</td><td style='text-align: center;'></td><td style='text-align: center;'>X</td></tr></table>