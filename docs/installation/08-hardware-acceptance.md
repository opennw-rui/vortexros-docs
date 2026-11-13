# 真机首次验收

本章用于新硬件首次投入测试。验收期间应使用带外管理口或独立Linux管理接口，
不要直接承载生产流量。VortexROS不会把虚拟机结果当作真实NIC、IOMMU或NUMA验收结果。

## 1. 启动前检查

```bash
sudo vortexros-bootstrap check --verbose
systemctl is-enabled frr.service
systemctl is-active frr.service
systemctl status vortexros.target --no-pager
```

要求：

- 检查结果没有`FAIL`；
- startup中声明的PCI设备具有IOMMU group或文档明确支持的驱动恢复路径；
- 发行版`frr.service`为`masked/inactive`；
- Linux SSH管理地址和明细路由已经验证，另一个终端能够重新连接。

## 2. 首次启动

```bash
sudo systemctl enable --now vortexros.target
sudo vortexros
```

进入CLI后执行：

```text
display service verbose
display health verbose
display alarm active
display vpp api compatibility verbose
display vpp interface-ownership verbose
display interface brief
display ip interface brief
```

只有以下条件全部满足才能继续：VPP API兼容、startup中的物理接口均可见、
LCP pair完整、FRR pathspace ready、Running与Actual generation一致、无critical告警。

## 3. 配置和重启恢复

完成一组最小配置并保存：

```text
system-view
interface eth1
 description hardware-acceptance
quit
commit
save
```

依次验证：

```bash
sudo systemctl restart vortexrosd.service
sudo systemctl restart vortexros-vpp.service
sudo systemctl restart vortexros-frr.service
sudo reboot
```

每次恢复后都重新检查service、health、alarm、接口、邻居和路由。VPP重启时：

- DPDK/VFIO设备必须按PCI恢复台账重新出现并重建LCP；
- AF_PACKET等未解绑Linux驱动的数据面不应要求PCI恢复台账；
- FRR或策略后端暂时失败只能进入degraded重试，不能错误回绑已经由VPP拥有的PCI设备。

## 4. 接管失败回滚

在维护窗口内故意让一个startup PCI设备无法被VPP识别，然后执行`reset dataplane`。
系统必须拒绝本次接管、停止VPP、恢复全部原生Linux驱动、接口名、MAC、MTU、
地址、VRF和路由。任何接口同时不受Linux和VPP识别都属于验收失败。

恢复后检查：

```bash
ip -d link show
ip address show
ip route show table all
sudo vortexros
```

```text
display vpp takeover transaction
display vpp interface-ownership verbose
display alarm active
```

## 5. 稳定性观察

正式开放测试前至少完成：

- 10次冷启动及`save`恢复；
- 反复重启VPP、FRR和vortexrosd，均能恢复接口、路由和策略；
- 24小时以上持续运行，期间进行接口flap、动态路由邻居变化及配置增删；
- 在目标报文长度和功能组合下记录NDR/PDR、丢包、CPU、内存和告警；
- 备份当前CFG、VPP startup、FRR pathspace及驱动恢复信息。

某项失败时不要继续生产接入。保留`journalctl`、`display health verbose`、
`display alarm history`和接管事务输出，先恢复Linux管理路径再排障。
