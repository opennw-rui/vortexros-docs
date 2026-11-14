# VortexROS 更新

**当前版本：0.28-dev-debug9。** [完整发布说明与安装包](https://github.com/opennw-rui/VortexROS/releases/tag/v0.28-dev-debug9)

对应控制层提交 `338800076ffc1de0201428c1fa19b641612ef607`，配套 VPP 26.10.4 和 FRR 10.7.1-vortexros-1.5-dev。

## Debug 9

- **V028D8R-001：** 首次改密的 CFG 和 Running 已接受，但 Linux 凭据投影失败时，旧临时密码不能获得普通 CLI 权限。只有完整投影成功、凭据快照一致，才授权受管 CLI；新 sudo 授权在成功后发布。
- **V028D8R-B01：** 安装器逐项检查关键服务，最后一次严格健康采样后再次核对服务和数据面不变量。服务已经停止而 daemon 健康快照尚未更新时，也能拒绝提交。
- 复用已有 AAA 告警、自动收敛和安装器回退机制，没有新增服务、角色或配置格式；VPP、FRR 源码和版本保持不变。

使用与排障见[本地账号与 SSH](../operator/aaa.md)、[升级与回退](../installation/07-upgrade-uninstall.md)。

## 最终包定向验证

验收包为 `vortexros_0.28-dev-debug9_amd64.run`，SHA-256：

~~~text
69d1b7dc9b41bb7183202c84d11c43b70421040d732643bcc51c453a5e55a734
~~~

| 环境 | 实际验证 |
| --- | --- |
| QEMU，Linux-only Debug 8 基线 | 同一个最终包正常升级；分别停止 FRR、route-zapi、switchd 后自动进入回退，恢复 Debug 8；原 CFG 字节和后端版本不变，VPP 保持停止 |
| QEMU，真实 SSH 与产品 CLI | 准备文件写入失败、chpasswd 失败、部分投影后失败均保留 CLI 限制；解除故障自动恢复；新密码登录、旧密码失效、公钥登录及控制服务重启通过 |
| VPP 模式设备 | 同包预检、模拟、正式升级及默认稳定观察通过；仅更新控制层，VPP、FRR、route-zapi 进程保持；原配置与 SSH AllowUsers 保留 |
| VPP 模式设备的临时账号 | 真实 SSH、Bash、密码验证的 sudo 返回 root 身份；清理测试账号后，原启动 CFG 字节不变，严格健康 ready、零告警 |

服务停止故障保持至安装器自动进入回退，再解除人为注入，随后验证旧版本恢复和默认 90 秒回退观察。正常升级使用默认 180 秒稳定观察。故障注入只在隔离 QEMU 执行。未运行全量测试、CI 或新的性能测试；本次文档同步没有重复运行上述产品验收。

## 从 Debug 5 到当前版本

| 版本 | 已交付变化 |
| --- | --- |
| Debug 5 | Candidate 按变更域复制、跨会话增量同步及显式刷新；路由组在精确旧基线拒绝后使用同一目标完整镜像完成发布 |
| Debug 6 | Running 快照与对应代号一致；LCP 删除不存在端口的 FDB 待处理记录；DHCPv6 IA_NA/IA_TA/IA_PD 类型解码 |
| Debug 7 / 7.1 / 7.2 | 三种本地 AAA 角色、首次改密、用户视图与 active 状态、密码哈希显示、Tab 与 Bash 返回修复；Kea 正常空租约及多实例汇总；统一 .run 比较组件版本 |
| Debug 8 | Linux-only 升级回退、无需预建安装目录、首次改密 CFG 已替换后的持久性处理、AAA 失败告警与自动收敛，以及普通 commit 等待提示 |

上述历史测试仍按其原版本归属，[性能数据](performance.md)没有改标为 Debug 9 的新测试。

## 手册维护

当前手册统一在 [vortexros-docs](https://github.com/opennw-rui/vortexros-docs) 维护。产品仓库的文档入口和后续构建的安装布局已改为在线手册；已发布的 Debug 9 `.run` 保持原附件及校验值，其附带的历史手册不作为当前使用入口。本次仅发布文档，没有重新打包或部署软件。
