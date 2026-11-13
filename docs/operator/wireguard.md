# WireGuard

用密钥认证的三层隧道互连站点。

[命令参考](reference/wireguard.md) · [配置案例](../examples/wireguard.md)

## 配置

Profile保存peer及其各自的外层source、destination和underlay VPN；Tunnel保存private key、兼容用的默认underlay、监听端口和profile引用。peer未指定underlay时继承Tunnel默认值。

```text
wireguard profile WG-PROFILE
 peer SITE-B
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.20.0.0 16
  source 192.0.2.1
  destination vpn-instance default 198.51.100.2 port 51820
  keepalive 25
#
interface Tunnel 10
 tunnel-protocol wireguard
 privatekey auto
 source vpn-instance default
 wireguard-profile WG-PROFILE
 mtu 1500
 ip address 10.255.0.1 255.255.255.252
```

WG/AWG profile和peer名称是区分大小写的单个CLI token，长度为1至64个字符，不允许空白、引号或命令分隔符。为兼容旧版已经保存且能够无歧义重放的配置，字母、数字、`_`、`-`、`.`和`:`均可使用；命令关键字本身仍不区分大小写。

peer下的`destination vpn-instance NAME [IP port PORT]`选择该peer的underlay VPN；`source IP`可选地固定该peer的外层源地址。未配置peer source时，VPP先使用该peer经过认证报文学习到的本地外层地址，再按endpoint和underlay路由自动选源；兼容配置中的Tunnel source只作为旧配置默认值。客户端省略`source-port`，每次创建接口时使用随机临时源端口。只有作为监听端的服务端才配置固定`source-port`。CFG中始终先输出peer `source`，再输出`destination`。

`privatekey auto`生成后，配置规范化为实际privatekey，并追加public key。WG/AWG的privatekey、presharedkey和header-protection key在Running、Candidate和CFG中均以明文保存，display也显示原值。因此必须保持`/VortexROS/config`、备份、审计采集和root终端的最小权限。旧版`cipher`行仅在启动回放时受理，daemon会将它一次性迁移为明文CFG；新配置不再生成密文。

Allowed IP限制该peer允许收发的地址范围，并参与Tunnel接口内的最长前缀peer选择。Tunnel使用点到点三层接口语义，路由可以只指定WG/AWG出接口而不写下一跳；数据面按报文最终内层目的地址选择peer，不依赖创建该邻接时偶然选中的peer，也不需要ARP。Allowed IP不会为任意业务网段自动创建系统路由；业务前缀仍需静态或动态路由。

每个peer的显式source与destination必须属于同一外层地址族；不同peer可以使用不同underlay VPN及不同外层地址族。IPv6 overlay可以与IPv4或IPv6 underlay组合，需为peer配置相应IPv6 `allowd-ip`。未配置任何`allowd-ip`表示该peer不匹配任何业务地址，不再隐式扩展成`0.0.0.0/0`。不同peer可以配置嵌套前缀，数据面按最长前缀选择；完全相同的前缀不能由两个peer同时拥有。

VortexROS默认启用WG和AWG异步加密。加密、解密和post节点可由VPP加密调度器分配到其他worker，发送和接收方向也可在不同核心执行；控制层每次收敛相关隧道时都会显式恢复该默认值，若切换失败则停止继续修改，避免配置成功但实际仍落在非预期执行模式。

服务端peer可以不配置`destination`，首个通过认证的报文会学习并更新该peer的漫游endpoint；这种模式必须在Tunnel上配置固定监听端口：

```text
wireguard profile WG-SERVER
 peer ROAMING-CLIENT
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.40.0.0 24
  destination vpn-instance default
#
interface Tunnel 11
 tunnel-protocol wireguard
 privatekey auto
 source vpn-instance default
 source-port 51820
 wireguard-profile WG-SERVER
 ip address 10.40.0.1 255.255.255.0
```

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

## 验证

```text
display wireguard interface Tunnel 10
display interface Tunnel 10
display ip routing-table
ping -vpn-instance BLUE 10.255.0.2
```

除接口状态外，还应从对端确认握手、收发计数和业务路由。只有Tunnel地址可达而业务前缀没有路由时，WireGuard不会自动补充路由。
