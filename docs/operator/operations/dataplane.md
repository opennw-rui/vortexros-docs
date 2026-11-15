# 数据面恢复

## VPP恢复

```text
display vpp api compatibility verbose
display vpp interface-ownership verbose
display vpp takeover transaction
reset service vpp
```

VPP接管阶段只检查核心API、startup中的全部预期物理接口及对应LCP。该门槛未通过时会恢复全部Linux接口；门槛通过后，FRR、策略或隧道等后续收敛失败只进入degraded并重试，不再回绑驱动。


[目录](../09-operations.md)
