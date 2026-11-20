# 灵活 QinQ

## 用途与原理

父接口灵活 QinQ 按客户 VLAN（C-VLAN）选择服务 VLAN（S-VLAN）。
同一客户端口可以把不同 C-VLAN 集合送入不同服务，而不必为每个客户 VLAN 配置一个子接口。

线路上的封装变化为：

~~~text
客户侧：C10 ── 接入设备 ── 网络侧：S100 + C10
客户侧：C20 ── 接入设备 ── 网络侧：S200 + C20
~~~

回程移除对应 S 标签，保留原 C 标签。它适用于多业务接入、客户 VLAN 透传及服务 VLAN 汇聚。
与整个客户端口共用一个 S-VLAN 的简单 QinQ 不同，本功能只对规则中匹配的单标签客户报文进行业务映射。

## 使用前提和默认行为

- 已激活 VPP 数据面，并启用交换功能。
- 客户侧接口使用 `port link-type hybrid`；服务 VLAN 必须先在全局创建。
- 默认没有灵活 QinQ 规则。客户 C-VLAN 只是匹配值，不要求逐个创建全局 VLAN。
- 同一端口的一个 C-VLAN 只能映射到一个 S-VLAN；相同映射重复配置不会产生重复项。
- 多条规则映射到同一 S-VLAN 时，当前配置会合并显示其客户 VLAN 集合。
- 未匹配 QinQ 规则的报文按原有端口 VLAN 配置处理；没有其他合法成员关系时丢弃。
  Hybrid 默认仍有 VLAN 1。若只允许已配置的客户业务，应显式撤销默认 VLAN 1 成员关系。
- 规则不修改端口 PVID，也不为无标签报文自动补入客户 VLAN。
- 客户接口和网络接口必须有实际链路，且业务 VLAN/桥域处于可转发状态。
  只配置规则不会替代链路、VLAN 和对端封装条件。

## 命令与参数

在客户接口视图执行：

~~~text
port vlan-stacking vlan VLAN-ID [to VLAN-ID] ... stack-vlan VLAN-ID
undo port vlan-stacking vlan VLAN-ID [to VLAN-ID] ... stack-vlan VLAN-ID
~~~

| 参数 | 含义 | 范围 |
|---|---|---|
| `vlan` 后的 VLAN-ID | 客户 VLAN，可为单值、多个值或连续范围 | 1–4094 |
| `to` | 包含起止值的连续范围 | 结束值大于起始值 |
| `stack-vlan` | 网络侧增加的服务 VLAN | 1–4094，须已创建 |

例如 `vlan 10 to 12 30 stack-vlan 100` 匹配 C10、C11、C12 和 C30。
不支持 `all`、客户 VID 0 或 4095。该命令没有额外的 enable 开关；提交规则后生效。

撤销可以只删除集合中的部分客户 VLAN。需要改变某个 C-VLAN 的服务归属时，
先撤销旧映射，再加入新映射，可以在同一次提交中完成。

## 完整配置示例

### 拓扑

~~~text
CE-A Ethernet0 ── Ethernet70 PE Ethernet72 ── Ethernet0 CE-C
CE-B Ethernet0 ── Ethernet71 PE

CE-A：C10 -> S100，C20 -> S200
CE-B：C12 -> S100
CE-C：终结 S100+C10、S100+C12 和 S200+C20
~~~

所有地址均为示例地址。三个业务分别使用不同的 IPv4 子网；S100 的两个客户集合分别限定在对应客户端口。

### 接入设备 PE

进入系统视图后配置：

~~~text
enable switch
vlan batch 100 200
#
interface Ethernet70
 portswitch
 port link-type hybrid
 port vlan-stacking vlan 10 to 11 stack-vlan 100
 port vlan-stacking vlan 20 stack-vlan 200
#
interface Ethernet71
 portswitch
 port link-type hybrid
 port vlan-stacking vlan 12 to 13 stack-vlan 100
#
interface Ethernet72
 portswitch
 port link-type trunk
 port trunk allow-pass vlan 100 200
#
~~~

执行：

~~~text
commit
save
~~~

网络侧 Trunk 按 S-VLAN 承载业务，不需要把 C10、C12 或 C20 加入它的普通允许列表。
客户口的 S-VLAN 归属由 stacking 规则建立，不要再将同一个 S-VLAN 配置为该客户口的普通 tagged/untagged 成员。

若客户侧不需要默认 VLAN 1，在配置相应 stacking 规则前执行：

~~~text
undo port hybrid untagged vlan 1
~~~

### 客户端 CE-A、CE-B

CE-A：

~~~text
interface Ethernet0.10
 vlan-type dot1q 10
 ip address 198.18.100.1 255.255.255.0
#
interface Ethernet0.20
 vlan-type dot1q 20
 ip address 198.18.200.1 255.255.255.0
#
~~~

CE-B：

~~~text
interface Ethernet0.12
 vlan-type dot1q 12
 ip address 198.18.101.1 255.255.255.0
#
~~~

两台设备分别执行 `commit` 和 `save`。

### 双标签终结端 CE-C

~~~text
interface Ethernet0.1010
 vlan-type dot1q 100 inner 10
 ip address 198.18.100.2 255.255.255.0
#
interface Ethernet0.1012
 vlan-type dot1q 100 inner 12
 ip address 198.18.101.2 255.255.255.0
#
interface Ethernet0.2020
 vlan-type dot1q 200 inner 20
 ip address 198.18.200.2 255.255.255.0
#
~~~

执行 `commit` 和 `save`。实例后缀 1010、1012、2020 用于区分接口，
实际封装由 `vlan-type` 指定；不要把实例编号误当成 S-VLAN。

## 查看配置与实际效果

在 PE 查询：

~~~text
display current-configuration interface Ethernet70
display interface Ethernet70
display vlan 100
display mac-address vlan 100
display health
~~~

接口查询的实际显示节选：

~~~text
Ethernet70 current state : UP
Line protocol current state : UP
Switch Port, Link-type : hybrid(configured),
QinQ stacking : C-VLAN 10 to 11 -> S-VLAN 100 (configured)
QinQ stacking : C-VLAN 20 -> S-VLAN 200 (configured)
~~~

MAC 查询示例节选：

~~~text
MAC Address       VLAN/VSI/BD                    Learned-From        Type
3ebb-948f-b027    100/-/-                        Ethernet72          dynamic
6243-3dcd-1ccf    100/-/-                        Ethernet70          dynamic
7ac5-1239-71d2    100/-/-                        Ethernet71          dynamic
~~~

MAC 地址随实际接口而变化。配置映射显示不等于流量已生效，还要检查两端连通性及不应放行的对照流量。

在 CE-A、CE-C 互相探测对应业务地址，并对 CE-B 的 C12 和 CE-A 的 C20 做同样检查。
上述三组封装的双向探测均取得每方向 3 发、3 收、0% 丢包的结果。
例如 CE-A 执行：

~~~text
ping -c 3 -a 198.18.100.1 198.18.100.2
~~~

实际输出节选：

~~~text
PING 198.18.100.2 (198.18.100.2) from 198.18.100.1 : 56(84) bytes of data.
3 packets transmitted, 3 received, 0% packet loss
~~~

广播和未知单播检查结果：

| 输入报文 | Ethernet70 发送 | Ethernet71 发送 |
|---|---:|---:|
| 网络侧 S100+C10 广播，发送3个 | 3 | 0 |
| 网络侧 S100+C12 广播，发送3个 | 0 | 3 |
| 网络侧 S100+C10 未知单播，发送3个 | 3 | 0 |
| 网络侧 S100+C99，发送3个 | 0 | 0 |
| 网络侧 S200+C10，发送3个 | 0 | 0 |

客户侧 C10 广播也已确认只送往对应网络侧业务；不匹配的 C99 不会获得该服务的转发权限。

## 修改、撤销与模式切换

只撤销 C11，保留同端口的 C10 和其他 S-VLAN 业务：

~~~text
interface Ethernet70
 undo port vlan-stacking vlan 11 stack-vlan 100
#
~~~

执行 `commit`，再次确认 C11 不再通过，而保留业务继续可达。
彻底删除本例的灵活 QinQ 映射：

~~~text
interface Ethernet70
 undo port vlan-stacking vlan 10 to 11 stack-vlan 100
 undo port vlan-stacking vlan 20 stack-vlan 200
#
interface Ethernet71
 undo port vlan-stacking vlan 12 to 13 stack-vlan 100
#
~~~

再执行 `commit` 和 `save`。删除规则不自动删除全局服务 VLAN，也不会替用户删除网络口的其他业务。

Access、Trunk、Hybrid 切换前，须先清理旧模式的非默认 VLAN/PVID 配置和 QinQ 规则。
撤销 VLAN 1 成员关系也属于非默认配置，不能靠 `undo ... vlan all` 把列表清空后直接切换。
恢复当前模式默认 VLAN 1，再切换。完整步骤见[端口模式](vlan/ports.md)。

## 策略、限速与服务桥域

接口 MQC 继续应用于该口承载的 QinQ 服务；已绑定策略后新增加的服务也继承该策略。
例如，下列配置阻断 Ethernet70 收到的指定 IPv4 源网段：

~~~text
traffic classifier CUSTOMER operator or
 if-match source-ip 198.18.0.0/16
#
traffic behavior BLOCK
 deny
#
traffic policy CUSTOMER-IN
 classifier CUSTOMER behavior BLOCK precedence 10
#
interface Ethernet70
 traffic-policy CUSTOMER-IN inbound
#
~~~

执行 commit 后，Ethernet70 的 C10 探测为 0/3，Ethernet71 的 C12 对照仍为 3/3。
在 Ethernet70 新增 C30→S300 后，同一策略也阻断新业务。
撤销接口绑定后，新业务恢复 3/3：

~~~text
interface Ethernet70
 undo traffic-policy inbound
#
~~~

需要完全删除示例策略时，在撤销绑定后依次执行
`undo traffic policy CUSTOMER-IN`、`undo traffic behavior BLOCK`、
`undo traffic classifier CUSTOMER`，再 commit。

服务 VLAN 也可以沿用 VLAN 视图下的限速。例如：

~~~text
vlan 100
 qos lr outbound cir 64 cbs 4096
#
~~~

该示例的 CIR 为 64 kbit/s。提交后，以 1000 个客户 C10 广播帧作为突发输入，
Ethernet70 实际收到 108 个，限速器产生丢弃计数；结果取决于突发大小、桶状态和报文长度，
不能将该单次比例视为固定丢弃率。撤销方式为 VLAN 100 下
`undo qos lr outbound`，再 commit。其他服务 VLAN 不因这条配置改变限速。

需要接入服务桥域时，将 S-VLAN 绑定到桥域，无需逐个绑定客户 C-VLAN：

~~~text
bridge-domain 500
 l2 binding vlan 100
#
~~~

提交后，本例 S100 的两个客户口及网络口共同进入该服务桥域，双向探测各 3/3。
不要在同一服务桥域同时配置与 VLAN 绑定冲突的显式子接口成员。
服务桥域默认未知单播洪泛策略与普通 VLAN 可能不同；通过
`display bridge-domain 500` 检查，保留正常 ARP/MAC 学习条件。

撤销绑定并恢复普通 VLAN 业务：

~~~text
bridge-domain 500
 undo l2 binding vlan
#
~~~

执行 commit；不再使用桥域时再执行 `undo bridge-domain 500`。
绑定和解绑均保留客户 VLAN 出口准入。

## 注意事项与限制

- 当前父口灵活 QinQ 匹配单层 0x8100 客户标签，配合当前 Trunk 的 0x8100 服务标签。
  不提供基于 MAC、IP 或 PCP 的选择规则，也不改写客户 VID。
- 同父口已有的普通 VLAN 分类和显式子接口不能与规则占用的分类冲突；冲突在提交前被拒绝。
  不同标签深度及不同匹配范围的合法子接口仍可按现有约束共存。
- 同一 S-VLAN 共享二层 MAC 学习范围。保留 C 标签和出口准入不等于建立独立的客户 MAC 表；
  需要独立学习域或允许重复 MAC 的业务，应分配不同服务 VLAN。
- 多个客户 VLAN 保留在服务中时，普通 Vlanif/Vbdif 网关不能为本机生成的裸 IP 报文自动选择 C 标签。
  需要三层终结时使用规划好的固定双标签 L3 子接口。
- 网络侧需容纳新增的服务标签开销。不要仅凭小包 Ping 成功认定最大报文长度已满足要求。
- 客户标签的 PCP/DEI 可保留；带 PCP/DEI 的有效 C10 报文已取得 3/3，非匹配客户口为 0/3。
- 规则增删可能影响对应业务的连通性和学习状态；变更前保留配置，提交后验证实际流量，再保存。
- 本功能沿用接口统计与既有策略处理。性能对比是指定报文、速率和线程布局下的观测，
  不构成所有硬件及业务组合的线速保证。

## 在一次提交中迁移客户 VLAN

同一客户口的一个 C-VLAN 只能归属一个 S-VLAN。需要从 S200 迁移 C21 到 S100 时，先在当前会话中撤销旧映射，再配置新映射，最后统一提交；不必分两次提交。

~~~text
interface Ethernet70
 undo port vlan-stacking vlan 21 stack-vlan 200
 port vlan-stacking vlan 21 stack-vlan 100
#
commit
display current-configuration interface Ethernet70
display vlan 100
display vlan 200
~~~

迁移改变 C21 的二层广播域和网络侧外层标签，涉及该客户 VLAN 的流量可能短暂中断，两端业务配置应协调修改。未迁移的客户 VLAN 保持原服务归属。两组服务之间互换客户 VLAN 时，也应先在 Candidate 中撤销两个旧归属，再添加两个新归属，然后只提交一次。

迁移验收记录：C21 迁往 S100 后，客户侧 3 个 C21 报文在网络侧均为 S100+C21；反向 3 个 S100+C21 报文恢复为 C21。未迁移的 C20 双向均为 3/3，网络侧仍为 S200+C20。随后将 C11 迁至 S200，双向均为 3/3；端口停启及保存后重载配置，C11 和 C21 各 3/3。上述结果验证归属和标签变化，不代表切换过程无丢包保证。

显式 L2 QinQ 子接口的固定外层、多内层匹配集合也可按同样原则在一次提交中迁移。仍须满足同一父接口匹配集合不重叠、标签重写及桥域的原有约束，不能同时保留两个服务对同一输入标签组合的匹配。
