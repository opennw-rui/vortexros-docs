# 安装后端依赖

以下命令是管理员手工操作示例。只读`check`不会执行；经过预演和确认后，`vortexros-bootstrap install`可执行相同的运行依赖安装。软件源和包签名策略由部署环境负责。

## 通用工具

```bash
sudo apt update
sudo apt install -y ca-certificates curl nftables ethtool pciutils iproute2 iputils-ping traceroute mtr-tiny busybox isc-dhcp-relay kea-dhcp4-server kea-dhcp6-server snmpd snmp
```

执行效果：安装诊断、nftables、DHCP和SNMP运行依赖，但不会自动把它们纳入VortexROS管理。发行版服务可能被自动启用，必须按[冲突服务](04-system-services.md)检查。 在启用 AppArmor 的系统上，VortexROS 安装包为 Kea 加载托管实例所需的文件规则。

## VortexROS-VPP

只安装项目发布页提供的VortexROS-VPP `26.10.x`系列配套包。控制层不固定`~N-g<commit>`构建修订号，但`vpp`、`libvppinfra`、`vpp-plugin-core`、`vpp-plugin-dpdk`和`vpp-crypto-engines`必须来自同一次构建并保持完整版本一致；启动时还会逐项验证Binary API兼容性。安装后验证：

```bash
vpp -v
find /usr/share/vpp/api -name '*.api.json' | head
```

必须同时存在 core API 及已使用的 nat-policy、MQC、WireGuard API。版本或 schema 不匹配时不要启动数据面。

## FRR

安装VortexROS维护的FRR `10.7.1-vortexros-1.x-dev`系列且不低于`1.4-dev`，并确保提供：`mgmtd`、`zebra`、`staticd`、`bgpd`、`ospfd`、`ospf6d`、`isisd`、`ripd`、`ripngd`、`bfdd`。该最低修订包含控制层默认加载的EVPN多归属模块，较旧修订不能与本版本配套使用。

```bash
/usr/lib/frr/zebra --version
for d in mgmtd zebra staticd bgpd ospfd ospf6d isisd ripd ripngd bfdd; do test -x "/usr/lib/frr/$d" || echo "missing $d"; done
```

VortexROS 使用独立 pathspace；不要让发行版 `frr.service` 同时管理同一配置。

## 能力检查

完成安装后运行：

```bash
sudo deploy/first-install.sh --plan --verbose
```

除VPP必须精确匹配、FRR必须满足受支持版本区间和daemon能力外，其他组件不锁定发行版小版本。系统DNS、时间同步、时区和日志组件由Linux管理员自行选择，不属于VortexROS依赖。
