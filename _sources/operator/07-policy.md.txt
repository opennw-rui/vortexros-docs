# 流量策略

按业务需要选择限速、流量分类或 TCP MSS 调整。报文过滤和地址转换分别见 [ACL](acl.md) 和 [NAT](nat.md)。

~~~{toctree}
:maxdepth: 1

qos
mqc
mss
~~~

## 策略继承

配置在二层物理接口或VLAN上的ACL、QoS、MQC和nat-policy会作用到相应的trunk业务流量。Eth-Trunk成员使用聚合接口的二层/三层属性，成员接口下不重复显示父接口配置。

## 组合验证

| 顺序 | 验证点 |
|---|---|
| ACL | 分类与丢弃计数正确 |
| 输出MSS | 只修改超限SYN |
| MQC | classifier、CAR、remark、redirect均生效 |
| nat-policy | 新会话、普通回程、NAT回流、PAT和统计开关正确 |
| 输出 | 无重复TTL/Hop-Limit递减或循环 |

组合策略验证完成后，再使用各功能的统计命令确认命中顺序和计数与业务流量一致。
