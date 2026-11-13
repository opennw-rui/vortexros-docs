# VortexROS 0.28 完整安装手册

本页包含从空白 Ubuntu 26.04 x86_64 主机到首次启动、验收、回退所需的全部步骤。安装命令会改变软件包、systemd服务、GRUB和VPP启动配置；远程设备必须先保护管理连接。

## 1. 兼容版本

| 组件 | 要求 |
|---|---|
| VortexROS | 0.28 系列 |
| VortexROS-VPP | `26.10.x`系列；同一组VPP软件包的完整版本必须一致，构建修订号不受控制层固定限制，Binary API仍须通过兼容检查 |
| FRR | VortexROS维护的`10.7.1-vortexros-1.x-dev`系列且不低于`1.4-dev`，并包含mgmtd、zebra、staticd及已支持的协议进程 |
| 操作系统 | Ubuntu 26.04 x86_64 |
| DHCP、SNMP及诊断组件 | 使用系统软件源的兼容版本，不锁定小版本；VortexROS 包会安装 Net-SNMP master、客户端及 AgentX 运行依赖 |

VPP必须使用项目发布的配套包。不要使用系统源中的通用VPP包代替。

## 2. 安装前规划和管理保护

记录每个物理接口的Linux名称、PCI BDF、MAC、驱动、MTU、地址和路由：

```bash
ip -br link
ip -br address
ip route show table all
ip -6 route show table all
lspci -Dnnk | less
```

保留一个 Linux OpenSSH 会话，并从另一个会话验证能够重新登录。首次安装启动 VortexROS 控制服务，保留 Linux SSH 和网卡驱动，持久屏蔽发行版的 vpp.service 和 frr.service，并停用冲突的独立 DHCP 服务。现有业务迁移后再执行安装。

如果设备只有一个接口，先保持Linux数据面，在CLI中完成地址和路由配置并保存；确认串口或其他带外恢复通道可用后，再选择业务口的 DPDK 模式并执行 `reset dataplane`。

## 通用安装器首次安装

在空白 Ubuntu 26.04 amd64 上，下载同版本的单文件安装器后，在 Linux 终端执行：

```bash
sudo sh ./vortexros-install_0.28-dev-debug5_amd64.run
```

安装器刷新现有 Ubuntu APT 源索引，通过系统源补齐必要依赖，优先沿用兼容的已安装版本，
并跳过 APT 推荐包。从内嵌系统包安装配套 VPP、FRR 和 VortexROS，然后启动 Linux 数据面和控制服务。执行完成后可用 `sudo vortexros`
进入 CLI。业务口的 DPDK 模式通过[数据面设备配置](../operator/03-interfaces-l2.md#数据面设备配置)
设置，再执行 `reset dataplane` 生效。

发布时，将包含配套 FRR 的系统归档封装为同一份单文件安装器：

```bash
tools/build-run-installer.sh vortexros-install_0.28-dev_amd64.run \
  vortexros-system_0.28-dev_amd64.tar
```

如需单独预演，可从同版本 Debian 包解出通用安装器，使用原系统归档：

```bash
dpkg-deb -x ./vortexros_VERSION_amd64.deb ./vortexros-installer
sudo ./vortexros-installer/usr/bin/vortexros-safe-upgrade --first-install --system-package ./vortexros-system_VERSION_amd64.tar --simulate
```

通用安装器记录首次安装前的软件、服务和文件状态，安装失败时执行恢复。已安装的设备
在执行 `reset dataplane` 前，可用 `sudo vortexros-safe-upgrade --restore-install`
恢复首次安装前的状态。该入口执行实际恢复。

## 3. 安装配套VPP和VortexROS

在同一次apt事务中安装发布页下载的精确VPP包和VortexROS控制层：

```bash
sudo apt install ./vpp_26.10.*_amd64.deb \
  ./libvppinfra_26.10.*_amd64.deb \
  ./vpp-plugin-core_26.10.*_amd64.deb \
  ./vpp-plugin-dpdk_26.10.*_amd64.deb \
  ./vpp-crypto-engines_26.10.*_amd64.deb \
  ./frr_10.7.1-vortexros-1.5-dev_amd64.deb \
  ./vortexros_0.28~dev_amd64.deb
vpp -v
find /usr/share/vpp/api -name '*.api.json' | head
```

从 0.27 和 VPP 26.06 升级时，将 VortexROS 0.28 与配套 VPP 26.10 一起交给[系统包升级流程](07-upgrade-uninstall.md#cli操作流程)。回退包也需同时包含当前的控制层和完整 VPP 组件。

VortexROS deb会声明ELF实际依赖、FRR版本区间和四个VPP组件包，`vpp`包还会精确依赖同构建版本的`libvppinfra`；任一包缺失或版本不一致时，apt必须拒绝安装。不要使用`dpkg -i --force-depends`绕过门禁。

也可以从源码安装：

```bash
make
sudo make install
```

源码安装与deb使用同一份静态文件清单；DHCP event helper固定安装为`/usr/libexec/vortexros/dhcp-event -> /usr/bin/vortexros-helper`。

## 4. 预览自动安装计划

先执行只读检查和安装预演：

```bash
sudo vortexros-bootstrap check --verbose
sudo vortexros-bootstrap install --dry-run
sudo vortexros-bootstrap install --dry-run --nic 0000:03:00.0 --nic 0000:03:00.1
```

`check`永远只读。无`--nic`的`install --dry-run`只做全量硬件盘点；带`--nic`的预演才代表本次允许写入startup的精确PCI白名单。两种预演都只打印CPU/队列分配、hugepage、理论链路上限及拟执行命令。

硬件选择规则：

- 从`/sys/class/net`读取接口类型、设备父节点和无线属性，不根据`eth`、`enp`等名称猜测；
- 只把有PCI父设备的有线Ethernet物理口写入DPDK设备列表；无线、纯虚拟和非PCI接口会被跳过并报告；
- 正式安装必须至少给出一个`--nic PCI-BDF`；不在白名单内的物理口不会进入生成配置；
- 选择当前SSH路径或默认路由使用的网卡会被拒绝。仅在已建立带外管理且明确承担风险时才可加`--allow-management-nic`；
- 已被VFIO/DPDK持有、因而没有Linux netdev的Ethernet设备按PCI class识别，并只复用现有startup中的可信接口名；名称无法确认时拒绝替换startup；
- 在线CPU为4个时使用CPU 2作为main、CPU 3作为worker；更多CPU使用后半部分，首个为main，其余为worker；
- 每个接口队列数不超过worker数以及内核暴露的RX/TX队列数；
- 生成的 VPP 启动文件显式启用 `linux_cp_plugin.so` 与 `linux_nl_plugin.so`，为接口镜像和 Netlink 同步提供 `linux-cp` 配置段所需的插件。
- 默认MTU为9000并保留multi-segment，不使用与巨帧冲突的`no-multi-seg`；
- hugepage按内存比例生成，同时为Linux、FRR和控制面保留普通内存；
- 性能估计是根据端口速率计算的理论线速上限，不是实际VPP吞吐承诺。

## 5. 执行安装和系统准备

确认预演结果后执行：

```bash
sudo vortexros-bootstrap install --nic 0000:03:00.0 --nic 0000:03:00.1
```

无人值守执行：

```bash
sudo vortexros-bootstrap install --yes --nic 0000:03:00.0 --nic 0000:03:00.1
```

已有`/VortexROS/startup.conf`默认保留。确认需要按照当前硬件重新生成时使用：

```bash
sudo vortexros-bootstrap install --replace-startup --nic 0000:03:00.0 --nic 0000:03:00.1
```

该命令在第一次变更前把配置校验和、服务状态、请求安装的软件包和所选NIC原驱动写入`/var/lib/vortexros/bootstrap/baseline`，再原子替换配置。每次执行另有`transaction`快照；失败会自动恢复，进程被强制终止后可执行`vortexros-bootstrap restore --transaction --yes`。

安装器执行以下操作：

1. 安装OpenSSH、FRR、Kea、BusyBox DHCP client、relay、nftables和诊断依赖；
2. 停止并禁用发行版`frr.service`、`vpp.service`、Kea、ISC DHCP server以及`isc-dhcp-relay.service`/`isc-dhcp-relay6.service`，避免双重所有权；
3. 创建`/VortexROS`、运行目录、DHCP状态目录和路由组目录；
4. 在配置不存在时创建Linux数据面模式的默认配置；
5. 从真实sysfs/PCI/CPU/内存信息生成`/VortexROS/startup.conf`；
6. 写入`/etc/default/grub.d/60-vortexros.cfg`，启用IOMMU、2MiB hugepage和VPP CPU隔离；
7. 执行`update-grub`。

安装器不会启用或启动`vortexros.target`，不会修改接口地址、路由、Linux SSH、DNS、时间或默认网关。

## 6. 检查生成结果并重启

```bash
sudo sed -n '1,240p' /VortexROS/startup.conf
sudo cat /etc/default/grub.d/60-vortexros.cfg
systemctl is-active frr.service vpp.service
```

确认CPU、PCI设备和接口名正确后重启：

```bash
sudo reboot
```

重启后检查IOMMU和hugepage：

```bash
find /sys/kernel/iommu_groups -mindepth 1 -maxdepth 2 -type l | head
grep -E 'HugePages|Hugepagesize|Hugetlb' /proc/meminfo
sudo vortexros-bootstrap check --verbose
```

所有必需项应为`PASS`。FRR必须属于`10.7.1-vortexros-1.x-dev`维护系列且不低于`1.4-dev`；更高的同系列修订保持兼容。其他上游系列、较旧修订或缺少协议进程时，必须先安装VortexROS维护的兼容版本。

## 7. 首次启动

显式启动控制面：

```bash
sudo systemctl enable --now vortexros.target
sudo systemctl status vortexros.target vortexrosd.service vortexros-frr.service --no-pager -l
sudo vortexros
```

CLI中验证：

```text
display service verbose
display health verbose
display alarm active
display vpp api compatibility verbose
display current-configuration
```

自动化或安装窗口必须使用严格健康门禁；未就绪、未收敛、Running/Actual generation不一致、存在活动告警或缺少必需VPP API时命令返回非零：

```bash
sudo vortexros health check --wait --timeout 2m --json
```

VPP默认尚未接管时，可以配置Linux物理接口、提交并保存。接管命令为：

```text
dataplane
 device 0000:03:00.0 name Ethernet 0
  mode dpdk
 quit
quit
commit
save
reset dataplane
```

成功条件是startup列出的所有物理设备均可在VPP中识别且LCP pair回读成功。失败时接管事务恢复原Linux驱动、接口、地址和路由，已保存的意图保留，运行状态继续显示 Linux。

### Ubuntu 上的 FRR AppArmor 路径

VortexROS 控制包安装 `/etc/apparmor.d/abstractions/frr.d/vortexros-pathspace`，
首次配置时重载已启用的 AppArmor。该规则授权 FRR 在 `/run/frr/vortexros/` 中创建运行所需的
PID 和 socket 文件。Ubuntu 26.04 的 FRR 抽象会自动加载该目录中的规则。

## 8. 首次验收

```text
display vpp interface-ownership verbose
display interface brief
display ip interface brief
display ipv6 interface brief
display ip routing-table
display service verbose
display health verbose
```

至少验证：

- Linux OpenSSH能够重新连接；
- 所有预期物理口、PCI和LCP身份一致；
- 接口MTU、MAC、地址、VRF和路由正确；
- FRR pathspace进程存在，发行版`frr.service`保持inactive；
- `commit`后运行态收敛，`save`后重启可恢复；
- DHCP、动态路由、策略和隧道只在实际使用时逐项验收。

## 9. 回退

在CLI中正常退出VPP所有权：

```text
dataplane
 device 0000:03:00.0 name Ethernet 0
  undo mode
 quit
quit
commit
save
reset dataplane
```

确认物理接口已回到Linux后停止产品服务：

```bash
sudo systemctl disable --now vortexros.target
```

如需恢复安装前记录的后端、startup、GRUB和所选NIC驱动：

```bash
sudo vortexros-bootstrap restore --yes
```

恢复按清单回到原来的active/enabled状态，包括两个ISC relay unit；清单校验失败会停止并返回非零。不要在VPP仍持有PCI设备时直接启动发行版VPP或FRR。

## 10. 常见故障

- `no IOMMU group`：固件未开启IOMMU或GRUB尚未生效；不要改用不安全的UIO回退。
- `Cannot allocate memory`：hugepage、main heap、buffer和普通内存比例不合理；重新运行预演并核对`/proc/meminfo`。
- VPP未发现接口：核对startup中的BDF、驱动绑定和VPP日志；接管事务应自动恢复Linux。
- FRR配置为空：确认`vortexros-frr.service`和独立pathspace，不要启动发行版`frr.service`。
- 远程失联：通过带外终端恢复Linux接口，检查接管事务和告警，禁止反复强制绑定驱动。

VPP参数语义可查阅[官方配置参考](https://docs.fd.io/vpp/25.06/configuration/reference.html)；hugepage与运行要求见[官方运行说明](https://docs.fd.io/vpp/25.10/gettingstarted/running/index.html)。
