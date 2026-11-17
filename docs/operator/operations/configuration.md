# 运行配置重置

已提交且没有待提交 Candidate 时，数据面异常或接口恢复不会阻止保存当前 Running。save 只写入启动配置，成功保存不表示业务已经恢复；核对保存结果后，再按提示执行 reset dataplane。若仍有未提交 Candidate，应先提交或撤销。

## Clear与Reset

- `clear`清理计数或当前Candidate；
- `reset`清理动态ARP/MAC表项，或执行服务重启、远端列表刷新和协议会话重置；
- 二者都是即时运维命令，不进入配置；
- 对外部连接、路由邻居或转发有影响的操作需要管理员权限和明确确认。

示例：

```text
reset ip arp
reset ip arp interface Vlanif 20 ip 192.0.2.10
reset mac-address
reset mac-address interface Ethernet 1 mac-address 00-11-22-33-44-55
clear interface Ethernet 1 counter
clear nat-policy counters
reset service vpp
reset service bgp
reset route-static group name CDN
```

`reset ip arp`只删除Linux LCP接口上的动态IPv4邻居，可按三层接口、IPv4地址或两者同时过滤；不指定接口时使用当前VPP LCP清单，覆盖自动物理LCP和配置型LCP。删除事件由LCP同步至VPP，在二层接口上执行会明确报错。`reset mac-address`由switchd删除Linux控制FDB中的动态外部学习项，再由LCP同步至VPP；可按二层接口、MAC地址或两者同时过滤，在三层接口上执行会明确报错。两条命令都保留静态配置，并由vortexrosd与commit串行执行。

clear interface <接口> counter 将接口详情、速率窗口及标准 SNMP 接口计数重新从零累计；可用的 CRC/FCS 计数同时清零。它只影响查询计数，不改变接口状态、配置或转发表，也不清除网卡自身计数。VPP 或控制服务重启后重新开始计数，SNMP 采集端应识别计数不连续。


## 清除 Running 并恢复已保存配置

`reset running-configuration` 经确认后立即清除 Running 中的业务配置。启用 VPP 时，设备重启 VPP 并按清除后的 Running 重建转发状态，业务会中断。VPP 启用状态、VPP 启动文件设置和已保存的启动 CFG 均保留。

清除前用 `display startup` 确认所选 CFG。恢复同一份已保存业务配置时，在系统视图将该文件载入 Candidate，然后提交：

~~~text
display startup
system-view
load configuration config.cfg
commit
display health
display interface brief
~~~

将 `config.cfg` 换成实际选中的文件名。此恢复方法适用于数据面归属未改变的情形；从 Linux 模式重新接管 DPDK 接口，应按[数据面切换流程](dataplane.md)操作，不能用普通 commit 跨过接管步骤。

一次双端二层验证中，两端接口 MTU 均为 9706。清空 Running 后接口回到三层默认 MTU 1500、原二层业务停止，Saved 文件保持不变；重新载入并提交后，MTU 恢复为 9706，端到端探测 3/3。重建仅发生在命令要求的阶段，不应在命令完成后持续重复重启。

## 清除启动配置

~~~text
reset saved-configuration backup.cfg
reset saved-configuration
display saved-configuration
~~~

第一条只清除指定的命名 CFG；不带文件名时清除当前选中的启动 CFG。两者都要求确认，不立即清除 Running，也不应重启数据面。清除后，后续启动使用该空配置；不要在唯一管理配置没有备份时执行。

实际验证中，命名 CFG 和选中 CFG 分别清空后，当前 VLAN、静态 MAC 与 BFD 业务继续运行，二层探测 2/2，数据面进程保持不变。需要重新保存当前业务时执行 `save`。

`display saved-configuration` 展示所选 CFG 解析后的规范配置，并非原文件的逐字节内容。系统生成的格式说明和分隔符可能重新显示；删除文件里的说明行不等于修改业务配置。查询路径可用 `display startup` 核对。

## 恢复出厂配置

`restore factory-configuration` 清除 Running 和所选 Saved，并恢复受管服务。它与只清除 Saved 的命令不同：原接口地址、路由、二层表项及受管账号等业务会被撤销，数据面回到出厂归属，远程管理可能中断。执行前保留可用的独立管理入口。

~~~text
restore factory-configuration
display health
display current-configuration
display saved-configuration
~~~

按提示确认后检查配置及实际接口。不能只凭命令返回成功就认为业务配置已经撤销；还应确认原邻居、动态路由和转发表项已消失。

恢复出厂前，可把当前已提交配置另存为一个命名备份。恢复出厂会清除当前选中的启动文件；
命名备份不要使用该文件名：

```text
display startup
save backup.cfg
```

恢复备份时，导入和提交先恢复配置，数据面归属保持当前状态。若备份使用 DPDK，
再通过 `reset dataplane` 明确执行网卡接管；不能把备份中的启动归属标记当作普通提交的接管命令：

```text
system-view
load configuration backup.cfg
display configuration candidate
commit
save
display dataplane
reset dataplane
display health
display interface brief
display dataplane verbose
```

按提示确认数据面切换，核对接口、地址、路由及实际业务恢复情况，再检查当前配置和启动配置。
从 Linux 切换到 DPDK 会改变网卡驱动并重建接口，业务与通过这些网卡建立的管理连接可能短暂中断；
应使用独立管理入口完成恢复。



[目录](../09-operations.md)
