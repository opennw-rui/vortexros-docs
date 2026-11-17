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

在非管理业务口执行 shutdown、commit，平台应收到对应接口的 linkDown；undo shutdown 并提交后应收到 linkUp。核对通知源 IP、接口索引和状态。标准链路通知每 60 秒采样接口状态，可能晚于 display 中的变化；短于采样周期的抖动不保证逐次通知。不要把 Trap 到达时间当作链路故障收敛时间。

检查完成后恢复接口，撤销本例通知目标、Trap 源和 standard 开关，保留其他监控使用的对象；提交并按需 save。

[功能目录](../snmp.md) · [命令参数](../reference/snmp.md)

## 目标地址限制

当前 Trap 接收目标与 trap source 使用 IPv4；目标可以使用 SNMPv2c 或 SNMPv3 authPriv。源接口须有主 IPv4 地址，并属于所选 SNMP VPN。IPv6 目标不会被接受，不能配置后期待通知自动经 IPv6 发送。SNMPv3 接收平台需为发送设备的 engine ID 配置相应 SHA-256/AES128 用户，避免将认证或解密失败误认为设备未发送。

## SNMPv3 接收结果

启用 SHA-256/AES128 的 authPriv 目标后，接收平台能解密以下链路通知。此处接口索引用于关联同一接口，部署时以本设备实际索引为准。

```text
源地址          通知       ifIndex    AdminStatus  OperStatus
192.0.2.65      linkDown   503735162  down(2)      down(2)
192.0.2.65      linkUp     503735162  up(1)        up(1)
```

两条通知对应同一接口的 shutdown 和 undo shutdown。若平台未显示通知，先核对 engine ID、用户名、认证和加密算法，再核对目标可达性与通知源地址。撤销 target-host 并提交后，display snmp-agent target-host 显示 Total: 0；这只删除通知目标，不会关闭其他 SNMP 查询。
