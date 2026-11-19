# 接口

按接口类型和用途选择章节。物理接口不能通过 `undo interface` 删除；逻辑接口可在系统视图删除。

## 接口范围

CLI 使用 VPP 已接管的接口、VortexROS 创建的逻辑接口，以及通过 `interface user-defined NAME` 提前声明的接口。仅由 Linux 独立管理的无线网卡、宿主网桥等设备不会自动进入接口库存、`?` 或 Tab 补全。接口列表、描述、统计及 IP 简表使用相同范围。

`user-defined` 用于在数据面接口尚未创建时提前配置。名称必须与后续 VPP 接口名称一致，例如 dataplane 设备命名为 `Ethernet0` 时，可以先配置：

```text
system-view
interface user-defined Ethernet0
 description Uplink
 ip address 192.0.2.1 255.255.255.0
#
```

预配置接口可通过名称进入视图并参与补全；预配置本身不表示数据面接口已经创建或链路已经 Up。完成 dataplane 配置并激活后，运行显示使用同名 VPP 接口的实际状态。当前配置仍渲染为 `interface Ethernet0`，不增加第二个长期接口对象。

```text
display interface brief
display interface Ethernet0
display current-configuration interface Ethernet0
```

需要撤销仍未创建的预配置接口时，使用 `undo interface Ethernet0`。VPP 已接管的物理接口不能用该命令删除；其设备归属通过 dataplane 配置管理。


删除逻辑接口时，其接口配置、地址、NAT 绑定、Proxy ARP 范围及 DHCP 接口配置一并撤销。全局 NAT 策略、地址池等共享对象保留，其他接口的业务配置不受影响。若其他独立对象仍引用该接口，先解除这些引用；命令被拒绝时，本次候选配置不发生部分删除。

执行 `commit` 后，删除才会作用于运行状态；需要在重启后保留结果时，再执行 `save`。

~~~{toctree}
:maxdepth: 1

ethernet
interface-processing
offload
flow-steering
dataplane
link-aggregation
subinterfaces
vlan
qinq
bridge-domains
mac-table
neighbors
proxy-arp
~~~
