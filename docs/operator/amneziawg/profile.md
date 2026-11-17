# 配置与混淆

## 配置与验证

AmneziaWG使用独立的隧道、接口和peer对象，不替换WireGuard；两类隧道可以同时配置。Profile除peer外，还保存握手前垃圾包、报文前置填充、消息头范围、内容填充、随机尾部和定时参数。两端的消息头和前置填充须兼容，头保护密钥必须相同；垃圾包、签名包和本端计时可按版本能力分别配置。参见[版本与兼容](versions.md)。

下面示例启用3个随机垃圾包、不同消息头范围和固定前置填充。启用header protection时，四类报文的前置填充都必须不少于12字节。

```text
amneziawg profile AWG-PROFILE
 junk size 16 48
 junk count 3
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
 padding content 4 16
 timing rekey-timeout 4 6
 header-protection BASE64-32-BYTE-KEY
 random-trailers enable
 junk-packet 1 expression "<b 0x160301><c><t><r 32><rc 16><rd 8>"
 #
 peer SITE-B
  publickey BASE64-PUBLIC-KEY
  allowd-ip 10.30.0.0 16
  source 192.0.2.1
  destination vpn-instance default 198.51.100.2 port 51820
  keepalive 25
#
interface Tunnel 20
 tunnel-protocol amneziawg
 privatekey auto
 source vpn-instance default
 amneziawg-profile AWG-PROFILE
 mtu 1500
 ip address 10.255.20.1 255.255.255.252
```

CLI 操作：

```text
commit
```

`junk-packet SLOT BASE64`用于配置1至5号静态原始报文槽位；`junk-packet SLOT expression "EXPRESSION"`用于动态生成握手前报文。表达式支持：`<b 0x...>`固定字节、`<c>`每次握手随机起始且逐槽递增的32位网络序计数、`<t>`当前Unix秒、`<r N>`随机字节、`<rc N>`随机英文字母和`<rd N>`随机数字。表达式最多4096字节，展开后的单个报文最多4096字节，动态标签最多128个；错误表达式在进入Candidate前拒绝。Jc/Jmin/Jmax产生的随机垃圾包与这些槽位相互独立。

Allowed IP、underlay VPN、动态客户端源端口、固定服务端监听端口和漫游endpoint的语义与 [WireGuard](../wireguard.md) 相同。Tunnel直连前缀会按Allowed IP最长前缀映射到peer，非直连业务网段仍由路由配置决定。修改协议参数时，已存在的peer会被最小化重建；修改单个peer只影响该peer。

验证命令：

```text
display amneziawg profile AWG-PROFILE
display amneziawg peer AWG-PROFILE SITE-B
display amneziawg interface Tunnel 20
display interface Tunnel 20
ping 10.255.20.2
```

完整停用时先撤销依赖的业务路由，再删除 Tunnel，最后删除 profile。仅解除绑定会使 Tunnel 不完整，必须在同次提交前删除该 Tunnel 或改绑完整的新 profile：

```text
undo interface Tunnel 20
undo amneziawg profile AWG-PROFILE
```

CLI 操作：

```text
commit
```

当前版本已经验证IPv4与IPv6 overlay、IPv4 underlay、header protection、内容填充、随机尾部、cookie关闭、静态/动态垃圾包以及peer反复增删。动态表达式采用上述明确语法，非法或超过边界的输入不会部分生效。


[功能目录](../amneziawg.md) · [命令参数](../reference/amneziawg.md)

## 查看当前视图配置

提交后在 Profile 视图执行 display this，可查看该 Profile 及全部 Peer；进入某个 Peer 后，同一命令只显示该 Peer，不包含其他 Peer 或 Profile 的公共参数。它显示已提交配置；尚未提交的编辑使用 display configuration candidate 查询。

~~~text
amneziawg profile AWG-PROFILE
display this
peer SITE-B
display this
~~~

例如，Peer 视图中的地址范围只会列出当前对端的 allowd-ip。核对公钥、端点和允许前缀时须选对 Peer；配置输出中的密钥同样需要妥善保护。已完成的查看不需要重新建立隧道或重新发起握手。

## 查看当前视图

提交后，在 Profile 视图执行 display this 可查看该 Profile 及全部 Peer；进入某个 Peer 后，同一命令仅显示该 Peer，不包含其他 Peer 或 Profile 的协议参数。

~~~text
amneziawg profile SITE
 peer PEER-B
  display this
~~~

结果包含所选 Peer 的已提交公钥、允许前缀、端点和其他非默认参数；它不展示当前会话尚未提交的修改。需要查看草稿时使用 display configuration candidate。查看配置不能替代握手、收发计数和业务探测。
