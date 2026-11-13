# VRRP

在多台设备之间提供冗余的 IPv4 或 IPv6 网关。

[命令参考](reference/vrrp.md) · [配置案例](../examples/vrrp.md)

## 配置

VRRP用于让两台或多台设备共享一个网关地址。VRRP只能配置在真实的三层Ethernet、Eth-Trunk、子接口、Vlanif或Vbdif上；接口必须处于路由模式。

### IPv4完整示例

假设P1与P2都连接到VLAN 100，客户端使用 `10.100.0.254`作为默认网关。P1优先级120作为Master，P2保持默认优先级100作为Backup。

P1：

```text
interface Vlanif 100
 ip address 10.100.0.1 255.255.255.0
 vrrp vrid 10 version-3 send-packet-mode v3-only
 vrrp vrid 10 virtual-ip 10.100.0.254
 vrrp vrid 10 priority 120
 vrrp vrid 10 timer advertise 1
 vrrp vrid 10 track interface Vlanif 200 reduced 30
```

P2：

```text
interface Vlanif 100
 ip address 10.100.0.2 255.255.255.0
 vrrp vrid 10 version-3 send-packet-mode v3-only
 vrrp vrid 10 virtual-ip 10.100.0.254
 vrrp vrid 10 timer advertise 1
```

IPv4必须先输入 `version-3 send-packet-mode v3-only`，再配置虚拟IP或其他参数。默认优先级为100、通告间隔为1秒、抢占开启。P1的Vlanif200 down后，运行优先级降低30；若低于P2，P2接管虚拟网关。

虚拟IP可以与接口自身地址相同。此时设备是该虚拟地址的地址拥有者，运行优先级自动为255；配置中仍保留用户输入的优先级，状态显示以运行优先级为准。

### IPv6示例

```text
interface Vlanif 100
 ipv6 address 2001:db8:100::1 64
 vrrp6 vrid 20 virtual-ip 2001:db8:100::fe
 vrrp6 vrid 20 priority 120
 vrrp6 vrid 20 timer advertise 1
```

IPv6组使用 `vrrp6`，无需单独输入IPv4的版本命令。

### 查看状态和效果

```text
display vrrp brief
display vrrp interface Vlanif 100
display vrrp 10
display vrrp statistics
display vrrp6 brief
```

brief输出示例：

```text
VRID  State   Interface  Type  Virtual IP      Priority  RunPri  Adv
10    Master  Vlanif100  IPv4  10.100.0.254   120       120     1.00s
```

详细输出会显示状态、版本、地址族、虚拟IP、配置优先级、运行优先级、虚拟MAC、通告间隔和抢占状态。配置已经提交但VRRP组尚未创建时，State显示 `Pending (not created in dataplane)`，应检查接口模式、地址和服务健康状态。

数据面遵循VRRPv3规范：IPv4通告校验和只覆盖VRRP消息，IPv6通告使用IPv6伪首部；Master收到优先级低于或等于本机的通告时会立即发送一次自身通告，并继续保持Master状态。此行为可缩短错误Master出现后的收敛时间，不需要额外CLI配置。

业务验证应包括：客户端持续ping虚拟IP和外部地址；关闭Master的上联或被跟踪接口；确认Backup接管、ARP/ND更新且业务恢复；再恢复接口并观察抢占行为。

### 修改和删除

```text
interface Vlanif 100
 undo vrrp vrid 10 track interface Vlanif 200
 undo vrrp vrid 10 priority
 undo vrrp vrid 10 timer advertise
 undo vrrp vrid 10 virtual-ip 10.100.0.254
 undo vrrp vrid 10
```

`undo priority`恢复100，`undo timer advertise`恢复1秒，`undo preempt-mode`恢复抢占。`undo vrrp vrid 10`删除整个IPv4组；IPv6使用对应的 `undo vrrp6 vrid 20 ...`。
