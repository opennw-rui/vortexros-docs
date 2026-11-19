# Flow Steering

将物理入口的流分配给 VPP 转发线程。

[命令参考](reference/interfaces.md)

## 工作原理与适用场景

网卡 RSS 通常按可识别的报文头将流分配到接收队列，封装较深时可能只看到相同外层地址。Flow Steering 在入口识别支持的内层会话，把不同流分配给转发 worker，适合外层集中、内层业务较多的隧道流量。

该功能不增加链路带宽，不替代路由 ECMP，也不保证单条流跨多个核心提速。选择 worker、接收队列及 CPU 时还应考虑 NUMA 和物理核心关系；两个逻辑 CPU 可能共享同一物理核心。

只在多 worker 的实际场景评估分布与总 CPU 开销。单 worker 不能用来观察多核分流收益，吞吐也会受到报文大小、封装、网卡及流量组成影响。

## 配置与验证

当网卡无法按 PPPoE、MPLS、L2TP、GRE、VXLAN 或 IP-in-IP 的内层流进行硬件 RSS 时，可以在物理入口启用 flow steering，将不同业务流分配给工作线程。此功能按接口配置，无需创建 profile：

```text
system-view
```

配置清单：

```text
 interface Ethernet 1
  flow-steering enable
```

CLI 操作：

```text
 commit
display flow-steering interface Ethernet 1
```

该功能只在VPP配置了两个或更多转发worker时激活；单worker设备保留配置但运行状态显示`inactive/single-worker`。解析最多检查256字节、4层封装、4个IPv6扩展头和8层MPLS标签，无法完整识别时使用稳定的外层会话散列，不丢包、不改变协议语义。它只决定入口worker，不替代Zebra、VPP FIB、ECMP或网卡本身已经提供的RSS。撤销接口绑定：

```text
interface Ethernet 1
 undo flow-steering enable
```

CLI 操作：

```text
commit
```


## 查看运行状态

用 display flow-steering interface Ethernet1 检查实际状态。active/inner-flow 表示内层流分配已激活；inactive/single-worker 表示配置保留，但当前只有一个 worker。需要至少两个 worker 才能观察跨线程分配。

启用前后用相同业务检查往返和丢弃计数；计数还可能包含后台协议报文，不能直接当成测试报文数。撤销后确认该接口不再启用此功能。功能只改变线程分配，不提供固定吞吐或无损保证。
