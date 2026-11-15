# MIB 与服务检查

配置和服务检查：

```text
display snmp-agent sys-info
display snmp-agent community
display snmp-agent usm-user
display snmp-agent target-host
display health verbose
```

这些`display snmp-agent`命令显示已提交配置；`commit`后的backend读回会核对三个
服务和UDP 161监听。最终运行验收仍应从NMS执行下列标准SNMP查询，不能只以配置
存在代替协议可达。

从 NMS 验证标准 OID：

```bash
snmpget -v2c -c monitor 192.0.2.1 sysName.0
snmpget -v2c -c monitor 192.0.2.1 HOST-RESOURCES-MIB::hrSystemUptime.0
snmpget -v2c -c monitor 192.0.2.1 UCD-SNMP-MIB::memTotalReal.0
snmpwalk -v2c -c monitor 192.0.2.1 IF-MIB::ifXTable
snmpget -v3 -l authPriv -u secure-monitor -a SHA-256 -A AuthPass123 \
  -x AES -X PrivPass123 192.0.2.1 sysName.0
```

标准Linux系统、CPU、内存、存储和负载信息继续由Net-SNMP提供。IF-MIB则完全由
VortexROS/VPP提供：只显示VortexROS接口，不显示Linux `lo`、VRF master或其他
控制面netdevice；`ifAlias`显示接口description。累计字节、错误数和计数不连续时间
来自VPP数据面。每个LCP host端以`lcp-<接口名>`作为单独的诊断接口显示，其累计值
来自对应VPP host software interface，不与原接口相加。产品接口和LCP诊断接口使用
不同的稳定身份域确定性生成ifIndex，不依赖Linux ifIndex、VPP sw_if_index或额外持久化文件；
接口身份不变时，LCP/VPP重建不会改变监控索引。当前不会把总包数冒充单播、组播或广播包数。VPP重启、
接口重建或计数清零后，监控系统应依据 `ifCounterDiscontinuityTime` 重建速率基线。
同一次不连续事件的该值保持不变；只有新的计数回退、接口身份变化或VPP代次变化
才会产生新值。接口表使用固定AgentX表注册，支持标准GET、GETNEXT和GETBULK，
删除的接口行会同步撤销而不会留作历史实例。

监控平台应直接对`ifHCInOctets`/`ifHCOutOctets`做相邻采样差，不应改用32位计数，
也不应设置“低于某值视为无流量”的设备侧阈值。隧道口统计内层流量，物理口统计
线侧流量及封装开销，二者不要求相等。Vlanif和LoopBack使用VPP逻辑接口统计；当前
配套VPP的simulated Ethernet输出会重复累计一次TX，SNMP适配层只去除这项重复，
不修改数据面，也不把LCP或物理成员计数并入逻辑接口。验证新接入时至少检查system、HOST-RESOURCES、
UCD-SNMP、完整接口清单、接口description、管理/链路状态、64位计数和低速连续流量。

完整撤销会停止 UDP 161 监听并删除全部 SNMP 配置：

```text
undo snmp-agent
commit
save
```

SNMP community 和 SNMPv3 密码随 root-only CFG 以明文保存。第一版不支持 SNMP
SET、SNMPv1、企业 MIB、IPv6 监听或 trap 目标、多 network namespace context，
也不会把 VPP 统计写回 Linux `/proc`、sysfs 或 `ip -s link`。固定源接口模式下，
固定source-interface时只接受对应public或VPN路由域中的目标接口；`all-interface`
通过单socket同时覆盖public和全部具有已配置IPv4接口的VPN。接口与所选VPN不一致时在Candidate
校验阶段拒绝，不会等到服务启动后才失败。

删除被SNMP source-interface引用的VPN实例会同时撤销整套SNMP配置并关闭UDP 161，
不会把原凭据自动改成全接口监听。若仍需SNMP，应在VPN删除后显式重新配置所需
监听范围和凭据。

配置`snmp-agent trap source`后，通知报文使用该接口主IPv4作为UDP源地址；
`snmp-agent trap enable standard`启用标准`linkUp`/`linkDown`通知。设备为Net-SNMP
内部状态查询维护独立的受管身份，不会把它显示为用户USM配置，也不改变外部SNMPv3
只支持`authPriv`的产品约束。

若VPP统计仍可读但接口清单或LCP身份暂时无法确认，设备不会发布一份带当前时间的
虚假`down`/MTU 0接口快照；最后一次已验证快照在3.5秒后自然变为不可用，身份恢复
后才重新出现。


[功能目录](../snmp.md) · [命令参数](../reference/snmp.md)
