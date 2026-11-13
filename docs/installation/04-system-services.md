# 处理冲突系统服务

只读检查不会停用系统服务。管理员可按本页手工处理，也可在确认计划后执行`vortexros-bootstrap install`统一停止并禁用冲突服务。

## 必须避免并行管理

| 系统 unit | 冲突原因 | 建议人工动作 | 恢复动作 |
|---|---|---|---|
| `vpp.service` | 与 `vortexros-vpp.service` 争用 API、PCI 和 startup | `sudo systemctl disable --now vpp.service` | `sudo systemctl enable --now vpp.service` |
| `frr.service` | 与独立 FRR pathspace 重复管理路由进程 | 见下方“停用发行版FRR实例” | `sudo systemctl unmask frr.service && sudo systemctl enable --now frr.service` |
| `kea-dhcp4-server.service` / `kea-dhcp6-server.service` | 与 VortexROS 实例争用接口和端口 | `disable --now` | 按原状态恢复 |
| `isc-dhcp-server.service` / `isc-dhcp-server6.service` | 与 VortexROS 实例争用接口和端口 | `disable --now` | 按原状态恢复 |
| `isc-dhcp-relay.service` / `isc-dhcp-relay6.service` | 与 VortexROS relay实例争用接口和端口 | `disable --now` | 按原状态恢复 |
| `snmpd.service` | 与 `vortexros-snmpd.service`重复管理SNMP master并可能争用UDP 161 | `sudo systemctl disable --now snmpd.service` | `sudo systemctl enable --now snmpd.service` |

不要全局停用 Linux SSH、防火墙或 NetworkManager，除非已确认它们确实管理 VortexROS 接管对象且有替代管理路径。

VortexROS不修改`/etc/resolv.conf`、系统时区或Linux时间同步服务。`systemd-resolved`、
`systemd-timesyncd`、Chrony以及系统日志保留策略均由Linux管理员维护。

## 停用发行版FRR实例

VortexROS使用独立的`vortexros` pathspace。发行版默认`frr.service`不能和它同时
管理接口、VRF和路由。先备份原配置并记录状态：

```bash
sudo install -d -m 0700 /root/vortexros-backup
sudo cp -a /etc/frr /root/vortexros-backup/frr-before-vortexros
systemctl is-enabled frr.service
systemctl is-active frr.service
```

确认业务已经迁移后，停止并禁止开机启动：

```bash
sudo systemctl disable --now frr.service
systemctl is-enabled frr.service       # 应显示 disabled
systemctl is-active frr.service        # 应显示 inactive
```

不要停用`frr@vortexros.service`或`vortexros-frr.service`。它们属于VortexROS后端。
需要退回发行版FRR时，先停止`vortexros.target`，再执行：

```bash
sudo systemctl enable --now frr.service
```

## 验证

```bash
sudo vortexros-bootstrap check --verbose
```

检查器只报告冲突及人工建议，不执行表中的命令。变更安装会把每个unit原来的`LoadState`、`is-enabled`和`is-active`结果记录到root-only恢复清单，卸载前按清单恢复；仍建议在设备外保留一份变更记录。
