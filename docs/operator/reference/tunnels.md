# GRE、IP-in-IP、VXLAN、WireGuard 与 AmneziaWG


## `allowd-ip`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：add an allowed IP selector (longest prefix selects the peer)
- 合法语法：

  ```text
  allowd-ip IP LENGTH
  ```

## `disable-cookies enable`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：enable cookie replies disabled
- 合法语法：

  ```text
  disable-cookies enable
  ```

## `display amneziawg`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display AmneziaWG configuration and runtime
- 合法语法：

  ```text
  display amneziawg { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

## `display vxlan statistics`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display VXLAN tunnel traffic statistics
- 合法语法：

  ```text
  display vxlan statistics source IP peer IP [vni VNI]
  ```

## `display vxlan tunnel`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display static VXLAN tunnels (from NVE peer-list)
- 合法语法：

  ```text
  display vxlan tunnel [ID]
  ```

## `display wireguard`

- 类别：只读显示命令
- 视图：`任意允许视图`
- 用途（设备帮助）：display WireGuard configuration and runtime
- 合法语法：

  ```text
  display wireguard { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

## `evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：enable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  evpn-overlay enable
  ```

## `header cookie`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set cookie message header range
- 合法语法：

  ```text
  header cookie LOW HIGH
  ```

## `header init`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set init message header range
- 合法语法：

  ```text
  header init LOW HIGH
  ```

## `header response`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set response message header range
- 合法语法：

  ```text
  header response LOW HIGH
  ```

## `header transport`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set transport message header range
- 合法语法：

  ```text
  header transport LOW HIGH
  ```

## `header-protection`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：enable ChaCha20 message header protection
- 合法语法：

  ```text
  header-protection { KEY | cipher CIPHERTEXT }
  ```

## `junk count`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set random junk packet count
- 合法语法：

  ```text
  junk count INTEGER<0-128>
  ```

## `junk size`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set random junk packet size range
- 合法语法：

  ```text
  junk size MIN MAX
  ```

## `junk-packet`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set a raw or dynamic handshake signature packet
- 合法语法：

  ```text
  junk-packet SLOT { BASE64 | expression EXPRESSION }
  ```

## `keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set persistent keepalive
- 合法语法：

  ```text
  keepalive SECONDS
  ```

## `padding content`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set decrypted content padding range
- 合法语法：

  ```text
  padding content MIN MAX
  ```

## `padding cookie`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set cookie reply fixed padding
- 合法语法：

  ```text
  padding cookie INTEGER<0-1024>
  ```

## `padding init`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set handshake initiation fixed padding
- 合法语法：

  ```text
  padding init INTEGER<0-1024>
  ```

## `padding response`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set handshake response fixed padding
- 合法语法：

  ```text
  padding response INTEGER<0-1024>
  ```

## `padding transport`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set transport packet fixed padding
- 合法语法：

  ```text
  padding transport INTEGER<0-1024>
  ```

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

## `presharedkey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set AmneziaWG peer presharedkey；set WireGuard peer presharedkey
- 合法语法：

  ```text
  presharedkey { KEY | cipher CIPHERTEXT }
  ```

## `publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：set AmneziaWG peer publickey；set WireGuard peer publickey；validate the derived AmneziaWG public key during configuration replay；validate the derived WireGuard public key during configuration replay
- 合法语法：

  ```text
  publickey KEY
  ```

## `random-trailers enable`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：enable random packet trailers
- 合法语法：

  ```text
  random-trailers enable
  ```

## `timing keepalive`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set keepalive random range
- 合法语法：

  ```text
  timing keepalive LOW HIGH
  ```

## `timing max-handshakes`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set max-handshakes random range
- 合法语法：

  ```text
  timing max-handshakes LOW HIGH
  ```

## `timing reject-after`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set reject-after random range
- 合法语法：

  ```text
  timing reject-after LOW HIGH
  ```

## `timing rekey-after`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set rekey-after random range
- 合法语法：

  ```text
  timing rekey-after LOW HIGH
  ```

## `timing rekey-timeout`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：set rekey-timeout random range
- 合法语法：

  ```text
  timing rekey-timeout LOW HIGH
  ```

## `undo allowd-ip`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：remove an allowed IP selector
- 合法语法：

  ```text
  undo allowd-ip IP LENGTH
  ```

## `undo amneziawg profile`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg profile NAME
  ```

## `undo disable-cookies enable`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：disable cookie replies disabled
- 合法语法：

  ```text
  undo disable-cookies enable
  ```

## `undo evpn-overlay`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：disable EVPN as the VXLAN overlay control plane
- 合法语法：

  ```text
  undo evpn-overlay enable
  ```

## `undo header cookie`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default cookie message header
- 合法语法：

  ```text
  undo header cookie
  ```

## `undo header init`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default init message header
- 合法语法：

  ```text
  undo header init
  ```

## `undo header response`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default response message header
- 合法语法：

  ```text
  undo header response
  ```

## `undo header transport`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default transport message header
- 合法语法：

  ```text
  undo header transport
  ```

## `undo header-protection`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：disable message header protection
- 合法语法：

  ```text
  undo header-protection
  ```

## `undo junk count`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default junk packet count
- 合法语法：

  ```text
  undo junk count
  ```

## `undo junk size`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default junk packet size
- 合法语法：

  ```text
  undo junk size
  ```

## `undo junk-packet`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：delete a raw junk UDP payload slot
- 合法语法：

  ```text
  undo junk-packet SLOT
  ```

## `undo keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear persistent keepalive
- 合法语法：

  ```text
  undo keepalive
  ```

## `undo padding content`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default content padding
- 合法语法：

  ```text
  undo padding content
  ```

## `undo padding cookie`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default cookie reply padding
- 合法语法：

  ```text
  undo padding cookie
  ```

## `undo padding init`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default handshake initiation padding
- 合法语法：

  ```text
  undo padding init
  ```

## `undo padding response`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default handshake response padding
- 合法语法：

  ```text
  undo padding response
  ```

## `undo padding transport`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default transport packet padding
- 合法语法：

  ```text
  undo padding transport
  ```

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

## `undo presharedkey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear AmneziaWG peer presharedkey；clear WireGuard peer presharedkey
- 合法语法：

  ```text
  undo presharedkey
  ```

## `undo publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear AmneziaWG peer publickey；clear WireGuard peer publickey
- 合法语法：

  ```text
  undo publickey
  ```

## `undo random-trailers enable`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：disable random packet trailers
- 合法语法：

  ```text
  undo random-trailers enable
  ```

## `undo timing keepalive`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default keepalive timing
- 合法语法：

  ```text
  undo timing keepalive
  ```

## `undo timing max-handshakes`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default max-handshakes timing
- 合法语法：

  ```text
  undo timing max-handshakes
  ```

## `undo timing reject-after`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default reject-after timing
- 合法语法：

  ```text
  undo timing reject-after
  ```

## `undo timing rekey-after`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default rekey-after timing
- 合法语法：

  ```text
  undo timing rekey-after
  ```

## `undo timing rekey-timeout`

- 类别：配置命令
- 视图：`amneziawg-profile`
- 用途（设备帮助）：restore the default rekey-timeout timing
- 合法语法：

  ```text
  undo timing rekey-timeout
  ```

## `undo wireguard profile`

- 类别：配置命令
- 视图：`系统视图`
- 用途（设备帮助）：delete a WireGuard profile
- 合法语法：

  ```text
  undo wireguard profile NAME
  ```
