# Flow Steering

将物理入口的流分配给 VPP 转发线程。

[命令参考](reference/interfaces.md)

## 配置与验证

当网卡不能按PPPoE、MPLS、L2TP、GRE、VXLAN或IP-in-IP内层流进行硬件RSS时，可以在物理入口启用flow steering。功能按接口生效，使用一套固定的产品参数，不创建或绑定profile，也不向用户暴露VPP内部调试开关：

```text
system-view
 interface Ethernet 1
  flow-steering enable
 commit
display flow-steering interface Ethernet 1
```

该功能只在VPP配置了两个或更多转发worker时激活；单worker设备保留配置但运行状态显示`inactive/single-worker`。解析最多检查256字节、4层封装、4个IPv6扩展头和8层MPLS标签，无法完整识别时使用稳定的外层会话散列，不丢包、不改变协议语义。它只决定入口worker，不替代Zebra、VPP FIB、ECMP或网卡本身已经提供的RSS。撤销接口绑定：

```text
interface Ethernet 1
 undo flow-steering enable
commit
```


## 查看运行状态

用 display flow-steering interface Ethernet1 检查实际状态。active/inner-flow 表示内层流分配已激活；inactive/single-worker 表示配置保留，但当前只有一个 worker。需要至少两个 worker 才能观察跨线程分配。

启用前后用相同业务检查往返和丢弃计数；计数还可能包含后台协议报文，不能直接当成测试报文数。撤销后确认该接口不再启用此功能。功能只改变线程分配，不提供固定吞吐或无损保证。
