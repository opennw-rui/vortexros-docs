# 系统管理

VortexROS只负责VPP、FRR和网络功能的控制面。用户、SSH、sudo、系统时间、DNS以及日志持久化由Linux管理员维护，不在设备配置中重复定义。

## 进入CLI

先通过Linux OpenSSH登录，再执行：

```text
sudo vortexros
```

`vortexrosd`的管理Socket只允许UID 0连接。非root直接执行`vortexros`会被拒绝；程序不使用setuid，也不会把Linux账号投影成设备账号。

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

Buffer pools 的 Available、Used、Cached 以缓冲区个数计量，分别表示池内可分配、已使用及线程缓存的缓冲区。三项之和等于该池的缓冲区总数。查询通过 VPP Binary API 的只读命令取得实时池状态，配套 VPP 26.06 的 gauge 计数不会被转换为虚构的零值。后端不可用时显示采集失败原因。

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
