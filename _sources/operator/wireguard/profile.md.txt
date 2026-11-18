# Profile 与 Peer

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

WG/AWG profile和peer名称是单个CLI token，名称保留输入形式，查找不区分大小写；长度为1至64个字符，不允许空白、引号或命令分隔符。为兼容旧版已经保存且能够无歧义重放的配置，字母、数字、`_`、`-`、`.`和`:`均可使用；命令关键字本身仍不区分大小写。

peer下的`destination vpn-instance NAME [IP port PORT]`选择该peer的underlay VPN；`source IP`可选地固定该peer的外层源地址。未配置peer source时，VPP先使用该peer经过认证报文学习到的本地外层地址，再按endpoint和underlay路由自动选源；兼容配置中的Tunnel source只作为旧配置默认值。客户端省略`source-port`，每次创建接口时使用随机临时源端口。只有作为监听端的服务端才配置固定`source-port`。CFG中始终先输出peer `source`，再输出`destination`。

`privatekey auto`生成后，配置规范化为实际privatekey，并追加public key。WG/AWG的privatekey、presharedkey和header-protection key在Running、Candidate和CFG中均以明文保存，display也显示原值。因此必须保持`/VortexROS/config`、备份、审计采集和root终端的最小权限。旧版`cipher`行仅在启动回放时受理，daemon会将它一次性迁移为明文CFG；新配置不再生成密文。

Allowed IP限制该peer允许收发的地址范围，并参与Tunnel接口内的最长前缀peer选择。Tunnel使用点到点三层接口语义，路由可以只指定WG/AWG出接口而不写下一跳；数据面按报文最终内层目的地址选择peer，不依赖创建该邻接时偶然选中的peer，也不需要ARP。Allowed IP不会为任意业务网段自动创建系统路由；业务前缀仍需静态或动态路由。

每个peer的显式source与destination必须属于同一外层地址族；不同peer可以使用不同underlay VPN及不同外层地址族。IPv6 overlay可以与IPv4或IPv6 underlay组合，需为peer配置相应IPv6 `allowd-ip`。未配置任何`allowd-ip`表示该peer不匹配任何业务地址，不会自动扩展为`0.0.0.0/0`。不同peer可以配置嵌套前缀，数据面按最长前缀选择；完全相同的前缀不能由两个peer同时拥有。

WireGuard 和 AmneziaWG 默认使用异步加密，可由多个工作线程处理加密与解密。此项无需单独配置；实际吞吐受 CPU、线程分配、报文大小和网卡能力影响。

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


[功能目录](../wireguard.md) · [命令参数](../reference/wireguard.md)

## 查看当前视图配置

提交后在 Profile 视图执行 display this，可查看该 Profile 及全部 Peer；进入某个 Peer 后，同一命令只显示该 Peer，不包含其他 Peer 或 Profile 的公共参数。它显示已提交配置；尚未提交的编辑使用 display configuration candidate 查询。

~~~text
wireguard profile WG-PROFILE
display this
peer SITE-B
display this
~~~

例如，Peer 视图中的地址范围只会列出当前对端的 allowd-ip。核对公钥、端点和允许前缀时须选对 Peer；配置输出中的密钥同样需要妥善保护。已完成的查看不需要重新建立隧道或重新发起握手。

## 查看当前视图

提交后，在 Profile 视图执行 display this 可查看该 Profile 及全部 Peer；进入某个 Peer 后，同一命令仅显示该 Peer，不包含其他 Peer 或 Profile 的协议参数。

~~~text
wireguard profile SITE
 peer PEER-B
  display this
~~~

结果包含所选 Peer 的已提交公钥、允许前缀、端点和其他非默认参数；它不展示当前会话尚未提交的修改。需要查看草稿时使用 display configuration candidate。查看配置不能替代握手、收发计数和业务探测。
