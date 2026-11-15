# Tunnel 通用命令

[配置指南](../tunnel-settings.md)

(cmd-allowd-ip)=
## `allowd-ip`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：add an allowed IP selector (longest prefix selects the peer)
- 合法语法：

  ```text
  allowd-ip IP LENGTH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 or IPv6 address | 输入值 |
| IP | `INTEGER<0-128>` | prefix length | 输入值 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 or IPv6 address | 输入值 |
| IP | `INTEGER<0-128>` | prefix length | 输入值 |

## `destination`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：set the peer endpoint and outer VPN；set the tunnel destination and optional underlay VPN
- 合法语法：

  ```text
  destination IP [vpn-instance NAME]
  ```
  ```text
  destination [vpn-instance VPN] [IP port PORT]
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：GRE 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | Destination IP address | 输入值 |
| IP | `vpn-instance` | Underlay VPN instance | 可选 |
| vpn-instance | `NAME` | VPN instance name | 输入值 |

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | peer endpoint address | 输入值 |
| IP | `port` | UDP port | 关键字 |
| port | `INTEGER<1-65535>` | UDP port | 输入值 |
| 命令后 | `vpn-instance` | outer VPN instance | 关键字 |
| vpn-instance | `VPN` | VPN instance | 输入值 |
| VPN | `IP` | optional peer endpoint | 输入值、可选 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | peer endpoint address | 输入值 |
| IP | `port` | UDP port | 关键字 |
| port | `INTEGER<1-65535>` | UDP port | 输入值 |
| 命令后 | `vpn-instance` | outer VPN instance | 关键字 |
| vpn-instance | `VPN` | VPN instance | 输入值 |
| VPN | `IP` | optional peer endpoint | 输入值、可选 |

(cmd-keepalive)=
## `keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set persistent keepalive
- 合法语法：

  ```text
  keepalive SECONDS
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | interval in seconds | 输入值 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | interval in seconds | 输入值 |

(cmd-peer)=
## `peer`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`WireGuard Profile视图`、`amneziawg-profile`
- 用途（设备帮助）：configure a BGP neighbor；enter a WireGuard peer；enter an AmneziaWG peer
- 合法语法：

  ```text
  peer NAME
  ```
  ```text
  peer X.X.X.X [option ...]
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-profile`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `WIREGUARD-PEER` | WireGuard peer name | 输入值 |

**适用视图：`amneziawg-profile`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `AMNEZIAWG-PEER` | AmneziaWG peer name | 输入值 |

**适用视图：`bgp, bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `BGP-PEER` | Neighbor IP address or case-sensitive peer-group name | 输入值 |
| BGP-PEER | `as-number` | AS number | 关键字 |
| as-number | `INTEGER<1-4294967295>` | AS number in asplain format (number<1-4294967295>) | 输入值 |
| as-number | `STRING<3-11>` | AS number in asdot format (number<1-65535>.number<0-65535>) | 输入值 |
| BGP-PEER | `fake-as` | Use a local AS number for this EBGP peer | 关键字 |
| fake-as | `INTEGER<1-4294967295>` | Fake local AS number | 输入值 |
| INTEGER<1-4294967295> / prepend-global-as | `dual-as` | Accept the global or fake AS during session establishment | 可选 |
| INTEGER<1-4294967295> / dual-as | `prepend-global-as` | Also prepend the global AS to advertised routes | 可选 |
| BGP-PEER | `group` | Add this neighbor to a peer-group | 关键字 |
| group | `BGP-GROUP` | Case-sensitive peer-group name | 输入值 |
| BGP-PEER | `password` | Configure TCP MD5 authentication | 关键字 |
| password | `simple` | Use a plaintext password | 关键字 |
| simple | `STRING<1-80>` | TCP MD5 password | 输入值 |
| BGP-PEER | `connect-interface` | Set interface name used as session output | 关键字 |
| connect-interface | `INTERFACE` | Interface name | 输入值 |
| BGP-PEER | `description` | Configure description information | 关键字 |
| description | `DESCRIPTION` | description text | 输入值、后续文本 |
| BGP-PEER | `enable` | Enable peer | 关键字 |
| BGP-PEER | `label-route-capability` | Enable labeled IPv6 route exchange for 6PE | 关键字 |
| BGP-PEER | `reflect-client` | Configure a peer as a route reflector client | 关键字 |
| BGP-PEER | `next-hop-local` | Specify local address as the next hop | 关键字 |
| BGP-PEER | `allow-as-loop` | Permit local AS in received paths | 关键字 |
| allow-as-loop | `INTEGER<1-10>` | Number of occurrences | 输入值 |
| BGP-PEER | `ebgp-max-hop` | EBGP multihop TTL | 关键字 |
| ebgp-max-hop | `INTEGER<1-255>` | Maximum hop count | 输入值 |
| BGP-PEER | `valid-ttl-hops` | Enable GTSM for the peer | 关键字 |
| valid-ttl-hops | `INTEGER<1-255>` | Valid hop count | 输入值 |
| BGP-PEER | `timer` | Configure peer timers | 关键字 |
| timer | `keepalive` | Keepalive time | 关键字 |
| keepalive | `INTEGER<0-21845>` | seconds | 输入值 |
| INTEGER<0-21845> | `hold` | Hold time | 关键字 |
| hold | `INTEGER<0-65535>` | seconds | 输入值 |
| timer | `connect-retry` | Connection retry time | 关键字 |
| connect-retry | `INTEGER<1-65535>` | seconds | 输入值 |
| BGP-PEER | `graceful-restart` | Configure peer graceful-restart role | 关键字 |
| graceful-restart | `enable` | Act as a restarting speaker | 关键字 |
| graceful-restart | `helper-only` | Help a restarting peer | 关键字 |
| graceful-restart | `disable` | Disable graceful restart | 关键字 |
| BGP-PEER | `default-route-advertise` | Advertise a default route to this peer | 关键字 |
| BGP-PEER | `route-limit` | Maximum accepted routes | 关键字 |
| route-limit | `INTEGER<1-4294967295>` | Maximum prefix count | 输入值 |
| BGP-PEER | `ignore` | Suspend the peer session | 关键字 |
| BGP-PEER | `advertise-community` | Send community attributes | 关键字 |
| BGP-PEER | `public-as-only` | Remove private AS numbers from updates | 关键字 |
| BGP-PEER | `substitute-as` | Replace the peer AS with the local AS in advertised routes | 关键字 |
| BGP-PEER | `preferred-value` | Set the preferred value for routes from this peer | 关键字 |
| preferred-value | `INTEGER<0-65535>` | Preferred value | 输入值 |
| BGP-PEER | `add-path` | Advertise multiple paths | 关键字 |
| add-path | `send` | Best paths to send | 关键字 |
| send | `INTEGER<1-6>` | Number of paths | 输入值 |
| BGP-PEER | `keep-all-routes` | Retain received routes rejected by inbound policy | 关键字 |
| BGP-PEER | `connected-check-ignore` | Ignore the connected check | 关键字 |
| BGP-PEER | `bfd` | Bidirectional forwarding detection | 关键字 |
| bfd | `enable` | Explicitly enable BFD for this peer | 关键字 |
| bfd | `disable` | Explicitly disable peer-group BFD inheritance for this peer | 关键字 |
| bfd | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| min-tx-interval | `INTEGER<100-1000>` | Minimum transmit interval in milliseconds | 输入值 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval | `INTEGER<100-1000>` | Minimum receive interval in milliseconds | 输入值 |
| INTEGER<100-1000> | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| detect-multiplier | `INTEGER<3-50>` | Detection multiplier | 输入值 |
| bfd | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| INTEGER<100-1000> / INTEGER<3-50> | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| bfd | `detect-multiplier` | BFD detection multiplier | 关键字 |
| BGP-PEER | `route-policy` | Apply routing policy | 关键字 |
| route-policy | `ROUTE-POLICY` | Name of the route policy | 输入值 |
| ROUTE-POLICY | `import` | apply to imported routes | 关键字 |
| ROUTE-POLICY | `export` | apply to exported routes | 关键字 |

(cmd-presharedkey)=
## `presharedkey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set AmneziaWG peer presharedkey；set WireGuard peer presharedkey
- 合法语法：

  ```text
  presharedkey { KEY | cipher CIPHERTEXT }
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | base64 32-byte key | 输入值 |
| 命令后 | `cipher` | device-encrypted key | 关键字 |
| cipher | `CIPHERTEXT` | encrypted key material | 输入值 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | base64 32-byte key | 输入值 |
| 命令后 | `cipher` | device-encrypted key | 关键字 |
| cipher | `CIPHERTEXT` | encrypted key material | 输入值 |

(cmd-privatekey)=
## `privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set or generate the AmneziaWG private key；set or generate the WireGuard private key
- 合法语法：

  ```text
  privatekey { STRING<44> | auto | cipher CIPHERTEXT }
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `auto` | Automatically generate a private key | 关键字 |
| 命令后 | `cipher` | device-encrypted private key | 关键字 |
| cipher | `CIPHERTEXT` | encrypted key material | 输入值 |
| 命令后 | `STRING<44>` | Base64-encoded 32-byte private key | 输入值 |

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `auto` | automatically generate a private key | 关键字 |
| 命令后 | `cipher` | device-encrypted private key | 关键字 |
| cipher | `CIPHERTEXT` | encrypted key material | 输入值 |
| 命令后 | `STRING<44>` | base64-encoded 32-byte private key | 输入值 |

(cmd-publickey)=
## `publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：set AmneziaWG peer publickey；set WireGuard peer publickey；validate the derived AmneziaWG public key during configuration replay；validate the derived WireGuard public key during configuration replay
- 合法语法：

  ```text
  publickey KEY
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | base64 32-byte key | 输入值 |

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | derived base64 public key | 输入值 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | base64 32-byte key | 输入值 |

## `source`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：pin the peer outer source address；set AmneziaWG source and underlay VPN；set NVE source VTEP address and optional underlay VPN；set WireGuard source and underlay VPN；set the tunnel source IP address
- 合法语法：

  ```text
  source IP
  ```
  ```text
  source IP [vpn-instance NAME]
  ```
  ```text
  source vpn-instance NAME [IP]
  ```


<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：GRE 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | Source IP address | 输入值 |

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | fixed outer source address | 输入值 |

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `vpn-instance` | underlay VPN | 关键字 |
| vpn-instance | `VRF` | VPN instance | 输入值 |
| VRF | `IP` | optional source address | 输入值、可选 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | fixed outer source address | 输入值 |

**适用视图：`interface`**
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | Source IP address | 输入值 |
| IP | `vpn-instance` | Underlay VPN instance | 可选 |
| vpn-instance | `NAME` | VPN instance name | 输入值 |

(cmd-source-port)=
## `source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set fixed AmneziaWG server listen port；set fixed WireGuard server listen port
- 合法语法：

  ```text
  source-port PORT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-65535>` | UDP port | 输入值 |

## `tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the tunnel encapsulation protocol
- 合法语法：

  ```text
  tunnel-protocol { gre | ipv4-ipv4 | ipv6-ipv4 | ipv4-ipv6 | ipv6-ipv6 | wireguard | amneziawg }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `gre` | GRE tunnel | 关键字 |
| 命令后 | `ipv4-ipv4` | IPv4 over IPv4 manual tunnel | 关键字 |
| 命令后 | `ipv6-ipv4` | IPv6 over IPv4 manual tunnel | 关键字 |
| 命令后 | `ipv4-ipv6` | IPv4 over IPv6 manual tunnel | 关键字 |
| 命令后 | `ipv6-ipv6` | IPv6 over IPv6 manual tunnel | 关键字 |
| 命令后 | `wireguard` | WireGuard tunnel | 关键字 |
| 命令后 | `amneziawg` | AmneziaWG tunnel | 关键字 |

## `undo allowd-ip`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：remove an allowed IP selector
- 合法语法：

  ```text
  undo allowd-ip IP LENGTH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 or IPv6 address | 输入值 |
| IP | `INTEGER<0-128>` | prefix length | 输入值 |

**适用视图：`amneziawg-peer`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `IP` | IPv4 or IPv6 address | 输入值 |
| IP | `INTEGER<0-128>` | prefix length | 输入值 |

## `undo destination`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear the peer endpoint；clear the tunnel destination IP address
- 合法语法：

  ```text
  undo destination
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：GRE 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

**适用视图：`wireguard-peer`**

此形式没有额外参数。

**适用视图：`amneziawg-peer`**

此形式没有额外参数。

## `undo keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear persistent keepalive
- 合法语法：

  ```text
  undo keepalive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

此形式没有额外参数。

**适用视图：`amneziawg-peer`**

此形式没有额外参数。

## `undo peer`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`WireGuard Profile视图`、`amneziawg-profile`
- 用途（设备帮助）：delete a WireGuard peer；delete an AmneziaWG peer；remove or reset a BGP neighbor or peer-group
- 合法语法：

  ```text
  undo peer NAME
  ```
  ```text
  undo peer PEER [option]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-profile`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `WIREGUARD-PEER` | WireGuard peer name | 输入值 |

**适用视图：`amneziawg-profile`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `AMNEZIAWG-PEER` | AmneziaWG peer name | 输入值 |

**适用视图：`bgp, bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `BGP-PEER` | neighbor IP address or case-sensitive peer-group name | 输入值 |
| BGP-PEER | `group` | Remove the peer-group membership | 可选、可组合 |
| group | `BGP-GROUP` | Case-sensitive peer-group name | 输入值 |
| BGP-PEER | `password` | Remove TCP MD5 authentication | 可选、可组合 |
| BGP-PEER | `connect-interface` | Remove the session output interface | 可选、可组合 |
| BGP-PEER | `description` | Remove description information | 可选、可组合 |
| BGP-PEER | `enable` | Enable peer | 可选、可组合 |
| BGP-PEER | `label-route-capability` | Disable labeled IPv6 route exchange for 6PE | 可选、可组合 |
| BGP-PEER | `reflect-client` | Disable route reflector client | 可选、可组合 |
| BGP-PEER | `next-hop-local` | Restore next-hop processing | 可选、可组合 |
| BGP-PEER | `allow-as-loop` | Remove allow-as-loop | 可选、可组合 |
| BGP-PEER | `fake-as` | Remove the fake local AS | 可选、可组合 |
| BGP-PEER | `ebgp-max-hop` | Restore single-hop EBGP | 可选、可组合 |
| BGP-PEER | `valid-ttl-hops` | Disable GTSM | 可选、可组合 |
| BGP-PEER | `timer` | Restore peer timers | 可选、可组合 |
| timer | `keepalive` | restore keepalive/hold timers | 关键字 |
| timer | `connect-retry` | restore connection retry timer | 关键字 |
| BGP-PEER | `graceful-restart` | Restore inherited graceful-restart role | 可选、可组合 |
| BGP-PEER | `default-route-advertise` | Stop advertising a default route | 可选、可组合 |
| BGP-PEER | `route-limit` | Remove route limit | 可选、可组合 |
| BGP-PEER | `ignore` | Resume the peer session | 可选、可组合 |
| BGP-PEER | `advertise-community` | Stop sending community attributes | 可选、可组合 |
| BGP-PEER | `public-as-only` | Keep private AS numbers | 可选、可组合 |
| BGP-PEER | `substitute-as` | Stop substituting the peer AS | 可选、可组合 |
| BGP-PEER | `preferred-value` | Remove the preferred value | 可选、可组合 |
| BGP-PEER | `add-path` | Restore Add-Path transmission | 可选、可组合 |
| BGP-PEER | `keep-all-routes` | Stop retaining rejected inbound routes | 可选、可组合 |
| BGP-PEER | `connected-check-ignore` | Restore connected check | 可选、可组合 |
| BGP-PEER | `bfd` | Restore BFD inheritance or BFD timers for this peer | 可选、可组合 |
| bfd | `enable` | Restore peer-group BFD enable inheritance | 可选 |
| bfd | `disable` | Restore peer-group BFD enable inheritance | 可选 |
| bfd | `min-tx-interval` | Minimum transmit interval in milliseconds | 关键字 |
| detect-multiplier / min-tx-interval | `min-rx-interval` | Minimum receive interval in milliseconds | 可选、可组合 |
| min-rx-interval / min-tx-interval | `detect-multiplier` | BFD detection multiplier | 可选、可组合 |
| bfd | `min-rx-interval` | Minimum receive interval in milliseconds | 关键字 |
| detect-multiplier / min-rx-interval | `min-tx-interval` | Minimum transmit interval in milliseconds | 可选、可组合 |
| bfd | `detect-multiplier` | BFD detection multiplier | 关键字 |
| BGP-PEER | `route-policy` | Remove routing policy | 可选、可组合 |
| route-policy | `ROUTE-POLICY` | Name of the route policy | 输入值 |
| ROUTE-POLICY | `import` | remove from imported routes | 关键字 |
| ROUTE-POLICY | `export` | remove from exported routes | 关键字 |

## `undo presharedkey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear AmneziaWG peer presharedkey；clear WireGuard peer presharedkey
- 合法语法：

  ```text
  undo presharedkey
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

此形式没有额外参数。

**适用视图：`amneziawg-peer`**

此形式没有额外参数。

## `undo privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear AmneziaWG key；clear WireGuard key
- 合法语法：

  ```text
  undo privatekey
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear AmneziaWG peer publickey；clear WireGuard peer publickey
- 合法语法：

  ```text
  undo publickey
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`wireguard-peer`**

此形式没有额外参数。

**适用视图：`amneziawg-peer`**

此形式没有额外参数。

## `undo source`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear AmneziaWG source；clear NVE source address；clear WireGuard source；clear the tunnel source IP address；use automatic peer source selection
- 合法语法：

  ```text
  undo source
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：GRE 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

**适用视图：`wireguard-peer`**

此形式没有额外参数。

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

**适用视图：`amneziawg-peer`**

此形式没有额外参数。

**适用视图：`interface`**
接口类别：NVE
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：use a dynamic AmneziaWG client source port；use a dynamic WireGuard client source port
- 合法语法：

  ```text
  undo source-port
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`interface`**
接口类别：隧道
接口类别：WireGuard 隧道、AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear the tunnel encapsulation protocol
- 合法语法：

  ```text
  undo tunnel-protocol
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：尚未选择协议的隧道、GRE 隧道、WireGuard 隧道、AmneziaWG 隧道

此形式没有额外参数。
