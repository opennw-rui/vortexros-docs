# SNMPv2c

提供只读查询，不提供SET。community作为访问凭据，应限制管理路径和配置读取权限；它不具备v3的加密认证能力。

SNMPv2c 示例：

```text
snmp-agent
snmp-agent sys-info version v2c
snmp-agent sys-info contact Network Operations
snmp-agent sys-info location IDC-A
snmp-agent protocol source-interface LoopBack0
snmp-agent community read monitor
snmp-agent trap source LoopBack0
snmp-agent target-host trap address udp-domain 192.0.2.50 udp-port 162 params securityname monitor v2c
snmp-agent trap enable standard
commit
save
```


[完整NMS配置、真实输出与撤销](../../examples/snmp.md) · [监听范围](source.md) · [检查与限制](monitoring.md)
