# 子接口

子接口将同一父端口上的不同 VLAN 流量分开。先根据用途选择模式，再配置对应封装，不能将两种模式的命令混用。

| 用途 | 创建方式 | 封装命令 | IP 地址位置 |
| --- | --- | --- | --- |
| L3 路由接口 | `interface Ethernet 1.100` | `vlan-type dot1q 100` | 子接口本身 |
| L2 桥接成员 | `interface Ethernet 1.100 mode l2` | `encapsulation dot1q vid 100` | 所属桥域的 Vbdif |

```{toctree}
:maxdepth: 1

subinterfaces-l3
subinterfaces-l2
```

[接口命令参考](reference/interfaces.md) · [桥域](bridge-domains.md) · [QinQ](qinq.md)

父端口必须存在。子接口编号用于接口身份，VLAN ID 用于报文分类，两者不要求相同。已有子接口不能通过重复进入时改写 `mode` 来切换二层/三层角色；先撤销引用并删除，再按目标模式创建。创建后必须补齐封装，未完成的对象会在提交校验时被拒绝。
