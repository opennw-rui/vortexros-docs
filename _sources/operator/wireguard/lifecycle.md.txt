# 修改与删除

## 修改和删除

- 新增或删除peer只影响该peer；
- 修改密钥、目的地址或监听参数时，相关Tunnel可能短暂重新建立；
- profile仍被Tunnel引用时不能删除；
- 修改peer underlay、source或destination后，应重新检查对应VPN中到公网地址的路由。

```text
interface Tunnel 10
 undo wireguard-profile WG-PROFILE
 undo source
undo wireguard profile WG-PROFILE
commit
```


[功能目录](../wireguard.md) · [命令参数](../reference/wireguard.md)
