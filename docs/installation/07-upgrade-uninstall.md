# 升级与回退

将目标包与**当前已安装版本的回退包**放到 /VortexROS/install。保存并验证当前业务后启动升级。

| 更新范围 | 材料 | 影响 |
| --- | --- | --- |
| 只更新控制层 | 目标与当前版本各自的 Debian 包 | 重启控制层，VPP 继续转发 |
| 同时更新 VPP | 两份系统 tar，软件包集合一致 | 重启 VPP 和控制服务，业务和管理路径可能短暂中断 |

## 执行升级

以下 NEW.tar 与 CURRENT.tar 是示例名。换成实际下载的文件：

~~~bash
sudo vortexros-safe-upgrade \
  --system-package /VortexROS/install/NEW.tar \
  --rollback-system-package /VortexROS/install/CURRENT.tar
~~~

只更新控制层时使用 --package 和 --rollback-package，并提供两份 Debian 包的完整路径。安装器会检查版本、当前配置与设备健康。需要提前查看软件包计划时，可在同一命令加 --simulate。

## 确认或恢复

进入 CLI 执行 display system-software verbose。committed 表示已完成连续健康观察。升级失败时安装器尝试恢复原软件，恢复成功显示 rolled-back。rollback-failed 表示需要通过恢复通道排查。系统包升级保留现有启动 CFG。

主动降级时，按同一入口传入旧目标包与当前版本回退材料。若需恢复首次安装前的状态，且尚未执行数据面重置，可用 sudo vortexros-safe-upgrade --restore-install。

更多 CLI 操作见[系统命令参考](../operator/reference/system.md)。
