# MIB 与服务检查

## 配置与连通性

~~~text
display snmp-agent sys-info
display snmp-agent community
display snmp-agent usm-user
display snmp-agent target-host
display health verbose
~~~

这些命令核对配置及健康；最终应从监控平台执行实际 SNMP 查询。接口 ACL、VPN 归属、IPv4 回程以及平台凭据必须一致。固定 source-interface 只监听所选 VPN 中该接口的主 IPv4；all-interface 覆盖 public 及已配置 IPv4 接口的 VPN。

## 推荐监控项目

| 对象 | 用途 |
| --- | --- |
| SNMPv2-MIB::system | 系统名、位置、运行时间 |
| HOST-RESOURCES-MIB | 系统运行时间及资源 |
| UCD-SNMP-MIB | 内存、CPU、负载等系统资源 |
| IF-MIB::ifTable / ifXTable | 接口描述、管理/链路状态、64 位计数 |
| ifCounterDiscontinuityTime | 计数清零或重建后的速率基线 |

IF-MIB 以产品接口为主；lcp- 前缀的行属于控制面配对诊断接口，不应与业务接口相加。ifAlias 对应接口 description。接口名称与身份不变时，数据面重建后监控索引保持稳定。

流量速率使用 ifHCInOctets / ifHCOutOctets 的相邻采样差。发现计数不连续时重建基线；不要用 32 位计数计算高速接口速率。隧道统计内层流量，物理口还包含封装开销，两者不要求相等。缺少可靠来源的分类或错误计数不可用，不应解释成零。

## 范围与限制

支持 SNMPv2c 只读及 SNMPv3 authPriv，不支持 SET、SNMPv1、企业 MIB、IPv6 监听或 IPv6 Trap 目标。community 和 SNMPv3 密码进入受保护的配置及备份，应限制其访问权限。

删除被源接口配置引用的 VPN 会同时撤销 SNMP 配置并停止监听；需要继续监控时，在新 VPN 下显式重新配置。不会自动扩大为全接口监听。

接口清单暂时不可观测时，监控数据可能不可用；不能把查询失败当成真实 Down 或零流量。先检查 display health verbose、监听范围及接口状态。

## 撤销

按对象解除引用，或在不再需要 SNMP 时整体执行 undo snmp-agent、commit、save。再从原平台确认轮询不再返回。

[功能目录](../snmp.md) · [命令参数](../reference/snmp.md)
