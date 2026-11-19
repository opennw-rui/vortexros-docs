# 服务日志

## 用途与范围

`display logbuffer` 将 VortexROS 受管服务的日志按时间合并显示，用于关联配置提交、协议建邻、路由同步和服务恢复过程。记录包含时间、服务或进程标识及消息正文。

日志来自系统 journal；此命令不建立第二份日志库，也不改变服务日志级别或保存期限。
查询不会修改配置、重启服务或清除记录。三种本地 AAA 角色均可查询，`network-operator` 保持只读，无需进入 Bash 或使用 sudo。

## 命令与默认值

~~~text
display logbuffer [service SERVICE] [last N] [since MINUTES]
~~~

| 参数 | 作用 | 范围与默认值 |
|---|---|---|
| 不带参数 | 合并查询所有 VortexROS 受管服务 | 本次系统启动，最近100条 |
| `service SERVICE` | 仅查询指定服务或服务组 | 省略时查询全部受管服务 |
| `last N` | 最多返回最近N条匹配日志，按时间先后显示 | 1–1000；默认100 |
| `since MINUTES` | 只查询最近若干分钟，仍限于本次启动 | 1–1440；省略时不追加时间限制 |

三个筛选参数可以交换顺序，同一参数只能出现一次。可在用户视图、系统视图及其他允许 display 的视图执行；缩写必须唯一。

| SERVICE | 日志范围 |
|---|---|
| `control` | 配置与状态恢复 |
| `vpp` | VPP 数据面 |
| `frr` | FRR 路由协议；多个协议共享服务日志 |
| `route-zapi` | 路由同步 |
| `switchd` | 二层状态同步 |
| `dhcp` | DHCPv4/DHCPv6 服务端、客户端和中继 |
| `snmp` | SNMP 代理与监听服务 |
| `aaa` | 本地账号应用 |

## 查询与定位

先查看故障时间附近的受管服务日志，再缩小到具体服务：

~~~text
display logbuffer since 15 last 200
display logbuffer service frr since 15 last 50
display logbuffer service control last 20
display logbuffer service dhcp last 50
~~~

FRR 查询的实际显示示例：

~~~text
<VortexROS> display logbuffer service frr last 2
Thu 2026-11-19 00:57:59 UTC vortexros-frr.service[18004]:  * Started watchfrr
Thu 2026-11-19 00:58:00 UTC init.scope[1]: Started vortexros-frr.service - VortexROS routing protocol pathspace.
~~~

其中 `init.scope[1]` 是系统服务管理器产生的启动或停止记录；消息正文指出关联服务。时间与时区随设备的系统设置显示。

沿用[输出修饰符](../cli/help.md)筛选正文。例如：

~~~text
display logbuffer service control since 15 last 200 | include ALARM
display logbuffer service frr last 100 | exclude Started
~~~

`last` 和 `since` 先限定日志查询范围，`include`、`exclude` 再处理返回的文本。
因此，“最近100条中未匹配”不等于更早日志中没有该事件。需要时扩大条数或时间范围。

## 结果判断与限制

没有匹配记录时显示：

~~~text
-- No entries --
~~~

这表示查询成功且当前范围为空，不表示服务从未运行。非法条数或时间参数会报错；journal 无法读取时报告查询失败，不将其显示为“没有日志”。

本命令只显示已经送入 journal 的受管服务记录。服务单独写入文件的日志、其他软件的日志以及内核日志不自动包含；服务自身日志级别也会影响可见内容。系统重启前的记录和实时持续跟踪不在本命令的查询范围内。

日志可能包含地址、账号名和业务标识，导出给他人前应检查内容。日志查询没有保存、撤销步骤；按[故障定位](troubleshooting.md)结合服务状态和告警判断原因，不要仅凭一条历史日志判定当前仍有故障。
