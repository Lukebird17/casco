# 中国城市轨道交通协会

# 《城市轨道交通 基于通信的列车运行控制系统(CBTC)互联互通系统规范 第3部分:车载电子地图》(T/CAMET 04010.3—2018)团体标准第1号修改单

本修改单经中国城市轨道交通协会于2024年09月03日批准发布，自2024年09月10日起实施。

## 一、 编辑性修改

1. 第2章中，将“运基信号 $$ 2010 $$ 267号文件《RSSP-Ⅱ铁路信号安全通信协议》”，修改为：“TB/T 3528.2 铁路信号安全通信协议 第2部分：Ⅱ型协议”。

2. 部分字段取值长度有误，根据字段字节长度要求修改。包括：

1）5.3.1, 表 3 中, 序号 12, “轨道区段属性” 行, “含义” 列修改取值。将

<div style="text-align: center;">表 3 轨道区段数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>轨道区段属性</td><td style='text-align: center;'>NID_TRPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x000001:普通上行轨道区段0x000002,普通下行轨道区段0x000004,上行转换轨</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>轨道区段属性</td><td style='text-align: center;'>NID_TRPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x000008,下行转换轨0x000010,站台0x000020,道岔0x000040,上行车档0x000080,下行车档0x000100,上行线路终点0x000200,下行线路终点0x000400,上行灯泡线边界0x000800,下行灯泡线边界0x040000,CI通信轨道区段0x100000,联络线(预留)参见5.3.5。</td></tr></table>

修改为：

<div style="text-align: center;">表 3 轨道区段数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>轨道
区段
属性</td><td style='text-align: center;'>NID_
TRPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,
0无效</td><td style='text-align: center;'>0x00000001:普通上行轨道区段
0x00000002,普通下行轨道区段
0x00000004,上行转换轨
0x00000008,下行转换轨
0x00000010,站台
0x00000020,道岔
0x00000040,上行车档
0x00000080,下行车档</td></tr></table>

---

<div style="text-align: center;">表 3 轨道区段数据结构(续表)</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含 义</td></tr><tr><td style='text-align: center;'>12</td><td style='text-align: center;'>轨道
区段
属性</td><td style='text-align: center;'>NID_
TRPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,
0无效</td><td style='text-align: center;'>0x00000100, 上行线路终点
0x00000200, 下行线路终点
0x00000400, 上行灯泡线边界
0x00000800, 下行灯泡线边界
0x00040000, CI通信轨道区段
0x00100000, 联络线(预留)
参见5.3.5。</td></tr></table>

2）5.3.5.1 中，将“例如，某轨道区段既为普通上行轨道区段（属性取值为 0x000001），又为上行转换轨（属性取值为 0x000004），无其他属性，则轨道区段属性取值应为：0x000005（0x000001 + 0x000004）”，修改为：“例如，某轨道区段既为普通上行轨道区段（属性取值为 0x00000001），又为上行转换轨（属性取值为 0x00000004），无其他属性，则轨道区段属性取值应为：0x00000005（0x00000001 + 0x00000004）。”

3）5.4.1, 表10中, 序号5,“折返区域属性”行,“含义”列修改取值。将

<div style="text-align: center;">表 10 折返区域数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>折返区域属性</td><td style='text-align: center;'>NID_TPPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x001000,上行折返换端区域0x002000,下行折返换端区域0x004000,上行无人折返发车区域0x008000,下行无人折返发车区域0x010000,上行无人折返停车区域0x020000,下行无人折返停车区域参见5.4.3。</td></tr></table>

---

## 修改为：

<div style="text-align: center;">表 10 折返区域数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>折返
区域
属性</td><td style='text-align: center;'>NID_
TPPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,
0无效</td><td style='text-align: center;'>0x00001000,上行折返换端区域
0x00002000,下行折返换端区域
0x00004000,上行无人折返发车
区域
0x00008000,下行无人折返发车
区域
0x00010000,上行无人折返停车
区域
0x00020000,下行无人折返停车
区域
参见5.4.3。</td></tr></table>

4）5.4.3.1中，将“例如，某折返区域既为上行折返换端区域（属性取值为0x000001），又为上行无人折返发车区域（属性取值为0x000004），无其他属性，则折返区域属性取值应为：0x000005（0x000001+0x000004）”，修改为：“例如，某折返区域既为上行折返换端区域（属性取值为0x00001000），又为上行无人折返发车区域（属性取值为0x00004000），无其他属性，则折返区域属性取值应为：0x00005000（0x00001000+0x00004000）”

5）5.5.1，表12中，序号5，“应答器属性”行，“含义”列修改取值。将

---

<div style="text-align: center;">表 12 应答器数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>应答器属性</td><td style='text-align: center;'>NID_BALPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,0无效</td><td style='text-align: center;'>0x0001:上行站台精确停车应答器0x0002:下行站台精确停车应答器0x0004:上行轮径校准应答器0x0008:下行轮径校准应答器0x0010:上行填充应答器0x0020:下行填充应答器0x0040:上行主应答器0x0080:下行主应答器0x0100:其他固定应答器0x0200:兼预告的主应答器参见5.5.2。</td></tr></table>

修改为：

<div style="text-align: center;">表 12 应答器数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含   义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>应答
器
属性</td><td style='text-align: center;'>NID_
BALPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFF
FFF,0无效</td><td style='text-align: center;'>0x0000001:上行站台精确停车应答器
0x0000002:下行站台精确停车应答器
0x0000004:上行轮径校准应答器
0x0000008:下行轮径校准应答器
0x0000010:上行填充应答器
0x0000020:下行填充应答器
0x0000040:上行主应答器
0x0000080:下行主应答器
0x0000100:其他固定应答器
0x0000200:兼预告的主应答器
参见5.5.2。</td></tr></table>

---

6）5.5.2.1 中，将“例如，某应答器既为上行站台精确停车应答器（属性取值为 0x0001），又为下行站台精确停车应答器（属性取值为 0x0002），无其他属性，则应答器属性取值应为：0x0003（0x0001 + 0x0002），修改为：“例如，某应答器既为上行站台精确停车应答器（属性取值为 0x00000001），又为下行站台精确停车应答器（属性取值为 0x00000002），无其他属性，则应答器属性取值应为：0x00000003（0x00000001 + 0x00000002）”。

7）5.6.1，表13中，序号5，“信号机属性”行，“含义”列修改取值。将

<div style="text-align: center;">表 13 信号机数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含  义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>信号
机
属性</td><td style='text-align: center;'>NID_
SIGPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,
0无效</td><td style='text-align: center;'>0x0001:进站信号机;
0x0002:出站信号机;
0x0004:出站兼道岔防护信号机;
0x0008:道岔防护信号机;
0x0010:区间间隔信号机;
0x0020:进段/进场信号机;
0x0040:出段/出场信号机;
0x0080:出库信号机;
0x0100:入库信号机;
0x0200:终端信号机;
0x0400:调车信号机;
0x0800:阻挡信号机。
参见5.6.3。</td></tr></table>

修改为：

---

<div style="text-align: center;">表 13 信号机数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名
定义</td><td style='text-align: center;'>数据
长度
(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含
义</td></tr><tr><td style='text-align: center;'>5</td><td style='text-align: center;'>信号
机
属性</td><td style='text-align: center;'>NID_
SIGPROPERTY</td><td style='text-align: center;'>4</td><td style='text-align: center;'>1~0xFFFFFFF,
0无效</td><td style='text-align: center;'>0x00000001:进站信号机;
0x00000002:出站信号机;
0x00000004:出站兼道岔防护信号机;
0x00000008:道岔防护信号机;
0x00000010:区间间隔信号机;
0x00000020:进段/进场信号机;
0x00000040:出段/出场信号机;
0x00000080:出库信号机;
0x00000100:入库信号机;
0x00000200:终端信号机;
0x00000400:调车信号机;
0x00000800:阻挡信号机。
参见5.6.3。</td></tr></table>

8）5.6.3.1 中，将“例如，某信号机为出站兼防护信号机，则其必具备的属性为：出站信号机（属性取值为 0x0002）、出站兼道岔防护信号机（属性取值为 0x0004）、道岔防护信号机（属性取值为 0x0008），若该信号机无其他属性，则信号机属性取值应为：0x000E（0x0002 + 0x0004 + 0x0008），修改为：“例如，某信号机为出站兼防护信号机，则其必具备的属性为：出站信号机（属性取值为 0x00000002）、出站兼道岔防护信号机（属性取值为 0x00000004）、道岔防护信号机（属性取值为 0x00000008），若该信号机无其他属性，则信号机属性取值应为：0x0000000E（0x00000002 + 0x00000004 + 0x00000008）”。

9）5.13，表20中，序号10，“ALE层Tcon定时器超时值”行，“数据范围”列修改取值。将

---

<div style="text-align: center;">表 20 安全通信协议栈数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>ALE层Tcon定时器超时值</td><td style='text-align: center;'>M_ALE_Tcon</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFF，单位：毫秒</td><td style='text-align: center;'>ALE层Tcon定时器超时值配置值</td></tr></table>

修改为：

<div style="text-align: center;">表 20 安全通信协议栈数据结构</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>序号</td><td style='text-align: center;'>定义</td><td style='text-align: center;'>变量名定义</td><td style='text-align: center;'>数据长度(字节)</td><td style='text-align: center;'>数据范围</td><td style='text-align: center;'>含义</td></tr><tr><td style='text-align: center;'>10</td><td style='text-align: center;'>ALE层Tcon定时器超时值</td><td style='text-align: center;'>M_ALE_Tcon</td><td style='text-align: center;'>4</td><td style='text-align: center;'>0~0xFFFFFFF,单位:ms</td><td style='text-align: center;'>ALE层Tcon定时器超时值配置值</td></tr></table>

## 二、 技术性修改

1. 将5.3.5.6条中“若轨道区段上有车挡，则车挡的‘上/下行’应与作为普通轨道区段的‘上/下行’一致”，修改为：“若轨道区段上有车挡，列车沿电子地图上/下行方向行驶时将被该车挡防护，则该轨道区段应具有“上/下行车档”属性”。

---

2. 将5.3.5.7条中“若轨道区段为线路终点（指线路尽头）轨道区段，则线路终点的‘上/下行’应与作为普通轨道区段的‘上/下行’一致”，修改为：“若轨道区段为线路终点（指线路尽头）轨道区段，则线路终点的‘上/下行’应与该轨道向非电子地图配置轨道延伸的方向一致”。