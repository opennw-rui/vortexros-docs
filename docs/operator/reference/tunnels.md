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

(cmd-keepalive)=
## `keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set persistent keepalive
- 合法语法：

  ```text
  keepalive SECONDS
  ```

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

(cmd-presharedkey)=
## `presharedkey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：set AmneziaWG peer presharedkey；set WireGuard peer presharedkey
- 合法语法：

  ```text
  presharedkey { KEY | cipher CIPHERTEXT }
  ```

(cmd-privatekey)=
## `privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set or generate the AmneziaWG private key；set or generate the WireGuard private key
- 合法语法：

  ```text
  privatekey { STRING<44> | auto | cipher CIPHERTEXT }
  ```

(cmd-publickey)=
## `publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：set AmneziaWG peer publickey；set WireGuard peer publickey；validate the derived AmneziaWG public key during configuration replay；validate the derived WireGuard public key during configuration replay
- 合法语法：

  ```text
  publickey KEY
  ```

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

(cmd-source-port)=
## `source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set fixed AmneziaWG server listen port；set fixed WireGuard server listen port
- 合法语法：

  ```text
  source-port PORT
  ```

## `tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the tunnel encapsulation protocol
- 合法语法：

  ```text
  tunnel-protocol { gre | ipv4-ipv4 | ipv6-ipv4 | ipv4-ipv6 | ipv6-ipv6 | wireguard | amneziawg }
  ```

## `undo allowd-ip`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：remove an allowed IP selector
- 合法语法：

  ```text
  undo allowd-ip IP LENGTH
  ```

## `undo destination`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear the peer endpoint；clear the tunnel destination IP address
- 合法语法：

  ```text
  undo destination
  ```

## `undo keepalive`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear persistent keepalive
- 合法语法：

  ```text
  undo keepalive
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

## `undo privatekey`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear AmneziaWG key；clear WireGuard key
- 合法语法：

  ```text
  undo privatekey
  ```

## `undo publickey`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`
- 用途（设备帮助）：clear AmneziaWG peer publickey；clear WireGuard peer publickey
- 合法语法：

  ```text
  undo publickey
  ```

## `undo source`

- 类别：配置命令
- 视图：`WireGuard Peer视图`、`amneziawg-peer`、`接口视图`
- 用途（设备帮助）：clear AmneziaWG source；clear NVE source address；clear WireGuard source；clear the tunnel source IP address；use automatic peer source selection
- 合法语法：

  ```text
  undo source
  ```

## `undo source-port`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：use a dynamic AmneziaWG client source port；use a dynamic WireGuard client source port
- 合法语法：

  ```text
  undo source-port
  ```

## `undo tunnel-protocol`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear the tunnel encapsulation protocol
- 合法语法：

  ```text
  undo tunnel-protocol
  ```
