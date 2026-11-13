# 升级、卸载与恢复

## 升级

VortexROS提供两种有明确中断边界的软件事务：

- `control-plane`只安装VortexROS Debian包，重启`vortexros-switchd`和`vortexrosd`；仅当route-zapi二进制变化时重启`vortexros-route-zapi`，并要求VPP与FRR进程身份保持不变。
- 安装器在包管理阶段暂停发行版的自动服务重启钩子，再按事务计划重启所需的VortexROS控制进程；系统级服务管理工具不得在控制层事务中自行重启VPP或FRR。
- Debian维护脚本只在首次安装时关闭与VortexROS端口所有权冲突的发行版服务；升级和降级由安装器按事务计划管理服务，不重复执行整机服务接管。
- `package`安装一份完整系统包，其中包含VortexROS、VPP运行库及其三个插件包，并可包含FRR；该事务停止并重新启动`vortexros.target`，因此会产生受控转发中断。

两种事务都强制要求同格式的当前版本回退材料，并由独立systemd看门狗执行一次自动回退。用户CFG不属于软件包，不会因升级或降级被替换。
目标包和回退包必须直接存放在`/VortexROS/install`。安装器只复制事务执行所需的私有副本，事务结束后不会删除包库中的原文件；管理员确认不再需要某个版本后可自行删除。`display startup`显示当前包库、最近成功事务对应的安装包和回退包路径。
完整系统事务在首次停止前记录原VPP进程身份；如果目标包安装或新VPP启动失败，回退允许从VPP已停止
的状态重新安装原软件集合。只有原包精确版本、非零的新VPP PID、运行中VPP的内嵌版本、核心服务和健康门禁全部恢复后，
事务才标记为`rolled-back`。
控制层事务要求 VPP 进程在升级期间保持不变。若发生意外替换，事务记录原 PID 并进入回退，
用回退期间稳定运行的 VPP 进程检查转发服务和健康状态。


升级采用“预检→安装→就绪等待→连续稳定观察→提交”的单向状态机。预检、模拟和真实事务调用同一组校验，避免只读检查与实际安装使用不同规则。目标软件没有通过预检时，不创建升级事务、不执行apt、不重启服务，也不改变配置或数据面。

### CLI操作流程

仅更新控制面时，将目标包和当前已安装版本的Debian包复制到设备本地：

```text
<VortexROS> display version
<VortexROS> display system-software
<VortexROS> check system-software control-plane /VortexROS/install/vortexros_0.27.dev.debug14_amd64.deb rollback-package /VortexROS/install/vortexros_0.27.dev.debug13_amd64.deb
<VortexROS> simulate system-software control-plane /VortexROS/install/vortexros_0.27.dev.debug14_amd64.deb rollback-package /VortexROS/install/vortexros_0.27.dev.debug13_amd64.deb
<VortexROS> upgrade system-software control-plane /VortexROS/install/vortexros_0.27.dev.debug14_amd64.deb rollback-package /VortexROS/install/vortexros_0.27.dev.debug13_amd64.deb
Warning: The VortexROS control plane will restart; VPP forwarding will remain running. Continue? [Y/N]: y
```

从 VPP 26.06 升级到 26.10 时，必须一起更新到对应的 VortexROS 0.28 控制层。上游变化、FD.io CSIT 性能对比和 I225 真机 A/B 见 [VPP 26.10 迁移说明](https://github.com/opennw-rui/VortexROS-VPP/blob/v26.10.0%2Bvortexros-vpp/RELEASE_NOTES_v26.10.0.md)。FRR 可沿用当前支持的版本，此时升级包和回退包均不包含 FRR，并使用下文的新版通用安装器入口。常规 VPP 软件更新使用由`tools/build-system-package.sh`生成的完整系统tar归档。目标包和回退包必须包含相同的软件包集合：

```text
<VortexROS> check system-software package /VortexROS/install/vortexros-system_0.28-dev_amd64.tar rollback-package /VortexROS/install/vortexros-system_0.27-dev-debug14-run1_amd64.tar
<VortexROS> simulate system-software package /VortexROS/install/vortexros-system_0.28-dev_amd64.tar rollback-package /VortexROS/install/vortexros-system_0.27-dev-debug14-run1_amd64.tar
<VortexROS> upgrade system-software package /VortexROS/install/vortexros-system_0.28-dev_amd64.tar rollback-package /VortexROS/install/vortexros-system_0.27-dev-debug14-run1_amd64.tar
Warning: VPP and the control plane will restart, causing a forwarding interruption. Continue? [Y/N]: y
```

从 0.27 首次迁移到 0.28 时，请从目标控制层包中解出新版通用安装器，再由它执行系统包事务。安装器在 APT 操作前持久屏蔽发行版的 vpp.service 和 frr.service，系统包升级和回退后仍保持屏蔽。运行服务由 VortexROS 管理。若回退到 0.27 后需要恢复首次安装前的状态，使用新版安装器执行 --restore-install。

```bash
dpkg-deb -x ./vortexros_0.28~dev_amd64.deb ./vortexros-installer
sudo ./vortexros-installer/usr/bin/vortexros-safe-upgrade \
  --system-package /VortexROS/install/vortexros-system_0.28-dev_amd64.tar \
  --rollback-system-package /VortexROS/install/vortexros-system_0.27-dev-debug14-run1_amd64.tar
```

系统包内固定需要`vortexros`、`vpp`、`libvppinfra`、`vpp-plugin-core`、`vpp-plugin-dpdk`和`vpp-crypto-engines`，`frr`为可选项。`libvppinfra`是`vpp`的精确版本依赖，缺少它时不能完成跨VPP构建修订的离线升级。清单记录每个Debian包的精确名称、版本和SHA256；事务开始前同时验证目标、回退包以及回退包与当前安装版本的一致性。

发布工程在可信构建机上按以下方式生成系统包，不能手工修改归档内清单：

```bash
tools/build-system-package.sh /srv/release/vortexros-system_0.28-dev_amd64.tar 0.28-dev \
  vortexros_0.28~dev_amd64.deb \
  vpp_26.10.0+vortexros-vpp*_amd64.deb libvppinfra_26.10.0+vortexros-vpp*_amd64.deb \
  vpp-plugin-core_26.10.0+vortexros-vpp*_amd64.deb \
  vpp-plugin-dpdk_26.10.0+vortexros-vpp*_amd64.deb vpp-crypto-engines_26.10.0+vortexros-vpp*_amd64.deb
```

生成器会从同一组Debian包中解出VPP及其运行库，直接执行包内`vpp -v`，并要求其内嵌版本与
`vpp`包元数据完全一致。复用旧构建目录导致的旧`version.h`不会进入系统归档。

Release 使用以下交付物。仅更新控制层的版本发布 Debian 包和控制层 tar：

- `vortexros_*.deb`：可直接安装的控制层Debian包；
- `vortexros-control-plane_*.tar`：包含控制层Debian包、manifest和包内SHA256，解包后用于`control-plane`升级；
- `vortexros-system_*.tar`：包含控制层和完整VPP运行包，可直接用于`system-software package`升级。
- `vortexros-install_*.run`：内嵌完整系统包的首次安装入口，适用于空白 Ubuntu。已有设备的升级及回退使用相应 Debian 包或系统 tar。

纯控制层tar由同一固定源码包生成：

```bash
tools/build-control-package.sh /srv/release/vortexros-control-plane_0.27-dev-debug14_amd64.tar 0.27-dev-debug14 \
  vortexros_0.27.dev.debug14_amd64.deb
```

发布页的总 SHA256 清单覆盖该版本的所有安装包。纯控制层tar不改变升级事务格式；先校验并解包，再将其中的Debian包传给`upgrade system-software control-plane`。
系统包内部SHA256用于发现传输或存储损坏，不能单独证明发布者身份。当前版本尚未内置独立的软件签名信任根；管理员必须通过受信任的Release渠道取得清单，并在把包交给升级器前核对Release公布的SHA256。不要把来源不明但内部校验自洽的归档视为可信软件。

计划安装或降级的控制层包还必须提供本版本定义的离线配置校验入口。早期包如果没有该入口，预检会在停止服务前拒绝它；自动事务回退仍使用升级前保存的精确包，不依赖目标包的该入口。这样可以避免为了兼容旧工具而跳过目标版本对当前启动配置的解析验证。

命令启动独立systemd事务后立即返回。使用以下命令查看最终状态：

```text
<VortexROS> display system-software
```

`display system-software verbose` 按事务显示版本、时间、安装包路径和失败原因。使用 `clear system-software info` 可清理已完成的历史记录，保留最新成功事务、进行中的事务和回退失败记录。命令不删除包库中的文件。

`committed`表示目标版本通过连续健康观察；`rolled-back`表示目标版本失败且旧版本已经恢复；`rollback-failed`表示自动恢复也失败，必须通过带外终端处理。`installing`、`waiting-ready`、`validating`和`rolling-back`是执行中的中间状态。

升级前检查包括：

- 目标与回退包的产品身份、架构、版本、完整系统清单及SHA256；
- 回退包的版本、dpkg文件校验记录和维护脚本精确匹配当前安装的软件，目标和回退材料不是同一文件；
- dpkg没有未完成事务，apt依赖关系处于可解析状态；
- 目标包包含升级器、CLI和daemon，Debian维护脚本通过语法检查；
- 由目标版本CLI解析设备选定的启动CFG，确认下一次启动能够读取；
- 当前核心服务和VPP进程有效，Running、Actual与Saved generation均已收敛；未执行`save`的Running会被拒绝；
- 事务分区拥有目标、回退、解包、dpkg日志及固定安全余量所需空间。

回退一致性校验覆盖可执行文件、库、服务、配置和Debian维护脚本。设备清理过的`/usr/share/doc`与`/usr/share/man`不属于运行内容，不阻止使用同版本回退包。

`simulate`在上述检查后额外执行apt的只读依赖解析，并显示服务操作和回退计划。它不保证目标软件启动后的运行行为，因此不能替代自动回退与连续健康观察。

手动回滚使用同一安全事务。将旧版本作为目标，将当前已安装版本作为 `rollback-package`。完成后在 `display system-software verbose` 中确认本次事务为 `committed`，再用 `display version` 和 `health check --wait --timeout 2m --require-saved` 验证目标版本及已保存配置。若本次事务显示 `rolled-back`，则手动回滚的目标失败，安装器已恢复操作前版本。


```text
<VortexROS> rollback system-software package /VortexROS/install/vortexros-system_0.27-dev-debug14-run1_amd64.tar rollback-package /VortexROS/install/vortexros-system_0.28-dev_amd64.tar
```

### 软件命令参考

#### `check system-software control-plane`

**功能**：使用真实升级事务的同一套规则检查目标、回退材料、当前设备状态和目标版本启动CFG兼容性。
**命令格式**：`check system-software control-plane TARGET.deb rollback-package CURRENT.deb`。
**行为**：只读；不创建事务、不调用apt、不重启服务。检查失败直接返回具体原因。

#### `check system-software package`

**功能**：检查完整VortexROS/VPP系统包及精确回退软件集合，不改变设备状态。
**命令格式**：`check system-software package TARGET.tar rollback-package CURRENT.tar`。
**行为**：除控制层检查外，还验证系统包清单、各组件SHA256、VPP组件版本一致性及包集合与当前系统的匹配关系。

#### `simulate system-software control-plane`

**功能**：在完整预检后，通过apt模拟依赖解析并显示预计执行边界。
**命令格式**：`simulate system-software control-plane TARGET.deb rollback-package CURRENT.deb`。
**行为**：不安装软件、不停止或启动服务、不修改CFG和数据面。模拟通过只证明材料、依赖和当前前置条件可接受。

#### `simulate system-software package`

**功能**：模拟完整系统包的软件集合解析以及VPP/控制层重启事务。
**命令格式**：`simulate system-software package TARGET.tar rollback-package CURRENT.tar`。
**行为**：不安装软件、不停止或启动服务、不修改CFG和数据面；输出将明确提示真实事务存在转发中断。

#### `upgrade system-software control-plane`

**功能**：在线安装较新的VortexROS控制面软件，并在验证失败时自动回退。
**命令格式**：`upgrade system-software control-plane TARGET.deb rollback-package CURRENT.deb`
**视图**：用户视图。
**参数**：`TARGET.deb`为目标VortexROS包；`CURRENT.deb`必须与设备当前已安装版本一致。
**缺省情况**：无。
**注意事项**：两个文件必须是设备本地可读的VortexROS Debian包；执行前会再次执行完整预检，以覆盖检查后到确认前的状态变化；命令需要Y/N确认。事务重启switchd和vortexrosd，仅在二进制变化时重启route-zapi，不重启VPP或FRR。
**验证方法**：使用`display system-software`检查最终状态，并使用`health check --wait --timeout 2m --json`检查严格健康。

#### `upgrade system-software package`

**功能**：在维护窗口内升级VortexROS、VPP插件/核心和可选FRR，并在验证失败时恢复整个原软件包集合。
**命令格式**：`upgrade system-software package TARGET.tar rollback-package CURRENT.tar`
**视图**：用户视图。
**参数**：两个系统包必须具有相同的软件包集合；`CURRENT.tar`内每个版本必须与设备当前安装版本一致。
**注意事项**：命令会停止`vortexros.target`并重启VPP，单机部署必然有转发中断。VPP启动后由现有Running权威恢复接口、路由和协议状态；新VPP PID、所有精确包版本、运行中VPP的内嵌版本、核心服务与健康门禁全部通过后才进入稳定观察。

#### `rollback system-software control-plane|package`

**功能**：把VortexROS控制面降级到指定旧版本，并在降级验证失败时恢复操作前版本。
**命令格式**：`rollback system-software control-plane TARGET.deb rollback-package CURRENT.deb`或`rollback system-software package TARGET.tar rollback-package CURRENT.tar`
**视图**：用户视图。
**参数与限制**：与对应的`upgrade`模式相同；目标版本可以低于当前版本。
**注意事项**：软件降级不回退用户CFG。配置必须与目标软件兼容；否则健康验证失败并恢复操作前软件集合。

#### `display system-software`

**功能**：显示当前安装的软件包版本和历次软件事务状态。
**命令格式**：`display system-software [verbose]`
**视图**：所有视图。
**输出**：分别显示VortexROS、VPP组件和FRR的dpkg版本；事务表显示`control-plane`或`system-package`模式、目标版本、回退版本和状态。事务证据来自`/var/lib/vortexros/upgrades`。
**注意事项**：该命令只读，不启动、重试或清理事务。`verbose`额外显示失败阶段、原因、最近一次健康JSON以及自动回退失败原因，便于区分目标失败和恢复失败。

### 首次从旧版本升级

1. 导出并在设备外保存启动配置、startup 和接口/PCI 清单。
2. 阅读新版本兼容性清单和迁移检查结果，准备当前已安装版本的Debian包作为回退包。
3. 运行新版本只读检查，并确认带外终端可用。
4. 当前版本已经提供`/usr/bin/vortexros-safe-upgrade`时，使用独立的systemd事务执行在线控制层升级；
   不要停止或重启`vortexros.target`。从不含该工具的旧版本首次升级时，先从新包只读提取升级器：

```bash
stage=$(mktemp -d)
dpkg-deb -x /VortexROS/install/vortexros_0.25.dev.9_amd64.deb "$stage"
sudo install -m 0755 "$stage/usr/bin/vortexros-safe-upgrade" /run/vortexros-safe-upgrade
sudo rm -rf "$stage"
```

随后执行：

```bash
sudo systemd-run --unit=vortexros-safe-upgrade --collect --wait --pipe \
  /run/vortexros-safe-upgrade \
  --package /VortexROS/install/vortexros_0.25.dev.9_amd64.deb \
  --rollback-package /VortexROS/install/vortexros_0.25.dev.7_amd64.deb \
  --ready-timeout 180 \
  --stability-seconds 240
```

上述直接调用示例使用控制面模式，始终重启`vortexrosd`；只有目标包中的route-zapi二进制与当前包不同时才重启`vortexros-route-zapi`。二进制未变化时保持路由发布会话和已发布路由，避免普通CLI、文档或daemon更新造成静态路由瞬态撤销。VPP与FRR进程必须保持原PID。控制面重启后先给予
默认180秒的有界收敛时间；这段时间只允许严格健康状态尚未就绪，VPP PID或核心服务任一
丢失都会立即失败。首次达到严格健康后，才开始连续稳定观察。整个稳定观察期内，
严格健康门禁、四个核心服务和VPP PID必须连续成功。任何检查失败只执行一次包回退；
SSH会话中断或安装进程异常退出时，独立的systemd看门狗仍会执行回退。控制面模式的回退也只重启控制面，不通过
反复重启target来碰运气；系统包模式每次安装或回退各执行一次有意的target停止/启动。事务证据位于`/var/lib/vortexros/upgrades/`，最终状态只能是`committed`、
`rolled-back`或`rollback-failed`。升级器自身与两个包在启动时复制到事务私有目录，看门狗不依赖
新包是否已经完成解包；事务完成后删除大文件，只保留版本、SHA256和最终状态证据。

完整系统包可在维护窗口内升级配套VPP。它不会做双VPP实例或无损切换；需要零中断时必须由设备冗余和外部流量切换方案提供。

## 事务恢复状态

首次变更安装会在`/var/lib/vortexros/bootstrap/baseline`记录文件校验和、目录元数据、服务active/enabled状态、请求安装的软件包和所选NIC原驱动。每次安装还会创建`transaction`：普通失败自动回滚；如果进程被强制终止，下次安装会拒绝覆盖证据，先执行：

```bash
sudo vortexros-bootstrap restore --transaction --yes
```

需要回到首次变更前状态时执行：

```bash
sudo vortexros-bootstrap restore --yes
```

恢复清单和备份不一致、服务恢复失败或NIC无法重新绑定时命令返回非零，不会伪报成功。

## 旧 bootstrap 状态

旧版本可能留下：

```text
/var/lib/vortexros/bootstrap/system-services.state
/var/lib/vortexros/bootstrap/backup/
```

新检查器只报告这些文件，不自动 unmask、复制或删除。管理员应查看记录，逐项核对当前 service 和 `/etc/resolv.conf`，再按原状态人工恢复。避免把过时快照覆盖到已经发生合法变更的系统。

## 卸载

卸载控制层前先把 VPP 数据面安全切回 Linux，并确认所有接口、管理地址和路由恢复。随后：

```bash
sudo systemctl disable --now vortexros.target
sudo apt remove vortexros
```

包维护脚本先停止本项目unit，再从baseline恢复startup、GRUB、发行版服务和NIC驱动；恢复失败会中止卸载，避免丢失恢复工具。由于dpkg维护脚本不能递归调用apt，卸载会保留VPP、FRR、Kea、BusyBox、relay和nftables软件包；需要删除时应在VortexROS卸载事务完成后由管理员单独执行。设置`VORTEXROS_SKIP_HOST_RESTORE=1`只能用于已经人工完成并验证恢复的救援场景。

## 故障回滚

- VPP 接管失败：优先让自动恢复事务完成，查看 critical 告警，不要并发手工抢占 PCI。
- FRR配置结果无法确认：控制面会将FRR标记为未收敛，并按已提交配置重新下发。
- DHCP generation激活失败：保留上一代可用generation，按服务显示定位错误。
- 远程失联：通过带外控制台恢复管理明细路由或 Linux 驱动，然后再处理 Candidate。

恢复或升级后用严格门禁收口；单次成功不足以替代上述连续稳定观察：

```bash
sudo vortexros health check --wait --timeout 2m --json
```

只有`healthy:true`且进程退出码为0才算验收通过。
