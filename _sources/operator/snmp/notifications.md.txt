# 计数与通知

## 接口计数

使用监控平台连续采样 ifHCInOctets / ifHCOutOctets，发送业务后检查累计值增加，再按采样间隔计算速率。包长、封装和后台协议会影响字节增量，不应把固定字节差作为所有接口的期望值。

计数器清零、接口重建或数据面重启后，结合 ifCounterDiscontinuityTime 重建采样基线。接口 description、管理状态与监听地址分别核对，不要仅根据平台历史曲线推断当前状态。

## 标准链路通知

按[SNMP 参数](../reference/snmp.md)配置 target-host，指定 trap source，并启用 snmp-agent trap enable standard。通知源接口与监听 VPN 应满足同一实例约束；切换 VPN 时先解除旧 Trap 源，再配置新源。

| 通知 | OID |
| --- | --- |
| linkDown | 1.3.6.1.6.3.1.1.5.3 |
| linkUp | 1.3.6.1.6.3.1.1.5.4 |

在非管理业务口执行 shutdown、commit，平台应收到对应接口的 linkDown；undo shutdown 并提交后应收到 linkUp。核对通知源 IP、接口索引和状态。通知按状态监视周期发送，可能晚于 display 中的变化，不是即时故障收敛时延保证。

检查完成后恢复接口，撤销本例通知目标、Trap 源和 standard 开关，保留其他监控使用的对象；提交并按需 save。

[功能目录](../snmp.md) · [命令参数](../reference/snmp.md)
