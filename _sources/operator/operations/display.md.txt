# 状态与版本

## Display

推荐从摘要逐级深入：

```text
display service verbose
display health verbose
display alarm active
display interface brief
display ip routing-table
display current-configuration
```

`display version`按照NOS运行身份、硬件平台和后端组件分区显示信息，包括产品版本、作者、源码提交、构建时间、Debian包版本、系统名、系统时间、操作系统、内核、CPU、内存、控制面状态、VPP、DPDK和FRR。产品版本行只显示版本号，构建阶段和提交号使用独立字段。登录CLI时在等宽边框内居中显示NOS标题、纯版本号、版权和作者，不查询运行状态；完整信息以`display version`为准。


## `display version`

**功能**：显示设备软硬件版本、运行平台及转发/路由组件身份。
**命令格式**：`display version`
**视图**：所有视图。
**缺省情况**：无。
**输出说明**：`VortexROS`段用于确认产品版本、源码提交和构建时间；`System`段显示主机、内核、平台、序列号、CPU和内存；`VPP`、`DPDK`及`FRRouting`段来自当前运行组件。字段无法读取时显示`-`或`unavailable`，不以猜测值替代。
**使用建议**：升级、故障上报和兼容性核对时应保存完整输出；不要只根据登录横幅判断所有后端已经收敛。

命令错误只显示一次错误位置和原因，不重复回显整条命令，也不会附加与用户无关的内部读取错误。

自动化安装、升级和发布验收必须使用严格健康检查，而不是把 systemd
`READY=1` 或 `display health` 的可读输出当作已经收敛：

```text
health check --wait --timeout 2m --json
```

该命令仅在 Running/Actual generation一致、reconcile为`in-sync`、没有活动告警且所有必需VPP API组可用时返回0。`--timeout`会自动启用等待；超时或未收敛返回非零。`--json`只输出一次最终快照，适合作为安装程序的稳定接口。


[目录](../09-operations.md)
