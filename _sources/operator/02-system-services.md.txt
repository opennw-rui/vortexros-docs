# 系统管理

本地账号、SSH、角色、首次改密及失败恢复见[本地账号与 SSH](aaa.md)。Linux 救援入口继续使用 `sudo vortexros`，受管账号按已提交的 AAA 角色进入 CLI。

## 检查服务

```text
display service
display service verbose
```

输出区分configured、running、ready和converged。某个后端未收敛时，转发面不会被伪报为正常；需要结合健康与告警继续定位。

## 检查健康和告警

```text
display health
display health verbose
display alarm active
display alarm history last 100
```

`display health`汇总VPP API、FRR、Linux运行态审计和最近一次配置收敛结果。`display alarm active`只列出尚未清除的告警；历史告警用于确认故障首次发生、最近发生和累计次数。

## 内存与缓冲池

在 CLI 中执行以下命令查询运行数据。

~~~text
display memory-usage
~~~

Heap 分区显示 VPP 各堆的容量、已用量和空闲量。Process RSS 是进程常驻内存，Process VSZ 是虚拟地址空间大小，二者分别读取 Linux 进程状态。

Buffer pools 的 Available、Used、Cached 以缓冲区个数计量，分别表示池内可分配、已使用及线程缓存的缓冲区。三项之和等于该池的缓冲区总数。查询通过 VPP Binary API 的只读命令取得实时池状态，配套 VPP 的 gauge 计数不会被转换为虚构的零值。后端不可用时显示采集失败原因。

## 日志

VortexROS各服务写入标准journald。查看daemon日志示例：

```text
journalctl -u vortexrosd.service
journalctl -u vortexros-route-zapi.service
```

日志保留、轮转和远端转发均由Linux日志策略统一管理。VortexROS CLI不提供另一套日志级别或日志文件目录。

## 重置后端服务

管理员可在CLI内使用对应的`reset service`命令重启受管后端，再通过`display service verbose`和`display health verbose`确认恢复。重启服务不会替代`commit`或`save`。

`reset service frr` 重启整套受管 FRR。命令成功时，Running 已回放并通过配置回读验证。路由邻居和业务流量会随协议重新收敛。用对应的路由表查询和 `ping` 确认业务恢复。

~~~{toctree}
:maxdepth: 1

aaa
~~~
