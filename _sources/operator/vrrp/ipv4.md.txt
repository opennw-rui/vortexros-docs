# IPv4 网关

## IPv4完整示例

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


## 配置

VRRP用于让两台或多台设备共享一个网关地址。VRRP只能配置在真实的三层Ethernet、Eth-Trunk、子接口、Vlanif或Vbdif上；接口必须处于路由模式。


[功能目录](../vrrp.md) · [命令参数](../reference/vrrp.md)
