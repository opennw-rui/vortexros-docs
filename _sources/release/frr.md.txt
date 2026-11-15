# 配套 FRR

0.29-dev使用 **10.7.1-vortexros-1.7-dev**。本轮打包复用原包和版本，没有新增FRR源码修改。

## 纳入的修复和语义

- 默认BGP实例恢复的EVPN状态修复采用上游[#23851](https://github.com/FRRouting/frr/pull/23851)固定提交6c068bfd707e及关联10.7回移。原记录中该补丁采用时仍处于上游审查，不能改称当时已正式发布。
- IS-IS在线改变Level时的邻接计数采用上游[5e8b2440](https://github.com/FRRouting/frr/commit/5e8b2440a0c29befe10d8199e6adaf0b3ce6d980)。
- OSPFv3 AS-External事件合并调度采用上游[5a2c00cf](https://github.com/FRRouting/frr/commit/5a2c00cf71450003f0643036766f599c20984ad3)。
- 自有ZAPI静态路由保留所有权实例标记，并在Zebra枚举及OSPF导入按类型选择static策略；E2 cost37保持实际配置。
- IS-IS L1/L2默认distance15，RIP/RIPng100；显式配置仍按实际值下发。
- RIP在接口删除前按ifindex释放旧多播成员，包含先删地址的路径，不提高内核上限或周期重启。
- Zebra重连重放采用上游3c9a369699d9197d65d6328f56d49ab0ca0db01a。

## 证据与边界

既有真实终端和协议报文记录覆盖邻接、LSDB、路由及流量；RIP保持进程不变重建接口后恢复，环回增删时socket资源144→192→144。独立default/red实例只重启Zebra、没有新邻居更新，两张路由表恢复，各探测3/3。后者是原生FRR/内核实验，产品CLI结果另列。

本轮6PE使用FRR已有的IPv6显式空标签选项，修正控制层投影，没有为此修改FRR。没有新增FRR吞吐或收敛时延结论。详见[6PE](../examples/mpls/6pe.md)及[最终包验证](cli-validation.md)。
