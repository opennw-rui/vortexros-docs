# 路由通用命令

(cmd-abr-summary)=
## `abr-summary`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：configure an OSPFv3 area summary；configure an area summary
- 合法语法：

  ```text
  abr-summary X.X.X.X X.X.X.X [not-advertise]
  ```
  ```text
  abr-summary X:X::X:X INTEGER<0-128> [not-advertise]
  ```

## `aggregate`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：configure a BGP aggregate route
- 合法语法：

  ```text
  aggregate ADDRESS MASK [as-set] [detail-suppressed]
  ```

(cmd-area)=
## `area`

- 类别：配置命令
- 视图：`OSPF Area视图`、`OSPF视图`、`ospfv3-area`、`ospfv3`
- 用途（设备帮助）：enter an OSPF area view；enter an OSPFv3 area view
- 合法语法：

  ```text
  area X.X.X.X
  ```

## `auto-cost reference-bandwidth`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：set the OSPF reference bandwidth
- 合法语法：

  ```text
  auto-cost reference-bandwidth INTEGER<1-4294967>
  ```

## `default-metric`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：set default metric；set the default metric for redistributed OSPF routes
- 合法语法：

  ```text
  default-metric INTEGER<1-16777214>
  ```
  ```text
  default-metric INTEGER<1-16>
  ```

## `default-route originate`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：originate a default route
- 合法语法：

  ```text
  default-route originate
  ```

## `default-route-advertise`

- 类别：配置命令
- 视图：`OSPF视图`、`ospfv3`
- 用途（设备帮助）：originate a default route into OSPF；originate an IPv6 default route into OSPFv3
- 合法语法：

  ```text
  default-route-advertise [always]
  ```

## `graceful-restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart role
- 合法语法：

  ```text
  graceful-restart {enable|helper-only|disable}
  ```

## `graceful-restart timer restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart restart timer
- 合法语法：

  ```text
  graceful-restart timer restart INTEGER<0-4095>
  ```

## `graceful-restart timer wait-for-rib`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：set BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  graceful-restart timer wait-for-rib INTEGER<1-4095>
  ```

(cmd-import-route)=
## `import-route`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：redistribute IPv6 routes into OSPFv3；redistribute routes into BGP；redistribute routes into IS-IS；redistribute routes into OSPF；redistribute routes into RIP
- 合法语法：

  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST]
  ```
  ```text
  import-route PROTOCOL [route-policy NAME] [cost COST] [type {1|2}]
  ```
  ```text
  import-route {direct|static|ospf|bgp|isis}
  ```
  ```text
  import-route {direct|static|ospf|bgp}
  ```

## `log-adjacency-changes`

- 类别：配置命令
- 视图：`IS-IS视图`、`OSPF视图`
- 用途（设备帮助）：log IS-IS adjacency changes；log OSPF adjacency changes
- 合法语法：

  ```text
  log-adjacency-changes
  ```
  ```text
  log-adjacency-changes [detail]
  ```

## `maximum load-balancing`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：set the maximum OSPFv3 ECMP paths；set the maximum number of BGP equal-cost paths；set the maximum number of RIP equal-cost paths
- 合法语法：

  ```text
  maximum load-balancing INTEGER<1-32>
  ```
  ```text
  maximum load-balancing INTEGER<1-6>
  ```
  ```text
  maximum load-balancing [ebgp|ibgp] INTEGER<1-256>
  ```

(cmd-network)=
## `network`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：add an OSPF network；advertise a RIPng network；advertise a classful RIP network；configure the IPv4 pool network；originate a BGP network
- 合法语法：

  ```text
  network ADDRESS MASK [route-policy NAME]
  ```
  ```text
  network X.X.X.X
  ```
  ```text
  network X.X.X.X X.X.X.X [description TEXT]
  ```
  ```text
  network X.X.X.X mask { X.X.X.X | INTEGER<0-32> }
  ```
  ```text
  network X:X::X/M
  ```

## `passive-interface default`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：make all RIP interfaces passive
- 合法语法：

  ```text
  passive-interface default
  ```

## `passive-mode`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：passive-mode
- 合法语法：

  ```text
  passive-mode
  ```

## `preference`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：set RIP route preference
- 合法语法：

  ```text
  preference INTEGER<1-255>
  ```

(cmd-router-id)=
## `router-id`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- 用途（设备帮助）：set BGP router ID；set OSPF router ID；set the OSPFv3 router ID
- 合法语法：

  ```text
  router-id X.X.X.X
  ```

## `silent-interface`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：suppress OSPF Hellos on an interface；suppress OSPFv3 Hellos on an interface；suppress RIP updates on an interface
- 合法语法：

  ```text
  silent-interface INTERFACE
  ```

## `undo abr-summary`

- 类别：配置命令
- 视图：`OSPF Area视图`、`ospfv3-area`
- 用途（设备帮助）：delete an area summary；remove an OSPFv3 area summary
- 合法语法：

  ```text
  undo abr-summary X.X.X.X X.X.X.X
  ```
  ```text
  undo abr-summary X:X::X:X INTEGER<0-128>
  ```

## `undo aggregate`

- 类别：配置命令
- 视图：`BGP地址族视图`
- 用途（设备帮助）：delete a BGP aggregate route
- 合法语法：

  ```text
  undo aggregate ADDRESS MASK
  ```

## `undo auto-cost reference-bandwidth`

- 类别：配置命令
- 视图：`OSPF视图`
- 用途（设备帮助）：restore the OSPF reference bandwidth
- 合法语法：

  ```text
  undo auto-cost reference-bandwidth
  ```

## `undo default-metric`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore default metric；restore the default OSPF redistribution metric
- 合法语法：

  ```text
  undo default-metric
  ```

## `undo default-route originate`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：stop originating a default route
- 合法语法：

  ```text
  undo default-route originate
  ```

## `undo default-route-advertise`

- 类别：配置命令
- 视图：`OSPF视图`、`ospfv3`
- 用途（设备帮助）：remove OSPF default route advertisement；stop originating an IPv6 default route
- 合法语法：

  ```text
  undo default-route-advertise
  ```

## `undo graceful-restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore the default BGP graceful-restart helper role
- 合法语法：

  ```text
  undo graceful-restart
  ```

## `undo graceful-restart timer restart`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP graceful-restart restart timer
- 合法语法：

  ```text
  undo graceful-restart timer restart
  ```

## `undo graceful-restart timer wait-for-rib`

- 类别：配置命令
- 视图：`BGP视图`
- 用途（设备帮助）：restore BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  undo graceful-restart timer wait-for-rib
  ```

## `undo import-route`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：stop redistributing routes into BGP；stop redistributing routes into IS-IS；stop redistributing routes into OSPF；stop redistributing routes into OSPFv3；stop redistributing routes into RIP
- 合法语法：

  ```text
  undo import-route PROTOCOL
  ```

## `undo log-adjacency-changes`

- 类别：配置命令
- 视图：`IS-IS视图`、`OSPF视图`
- 用途（设备帮助）：stop logging IS-IS adjacency changes；stop logging OSPF adjacency changes
- 合法语法：

  ```text
  undo log-adjacency-changes
  ```

## `undo maximum load-balancing`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：restore RIP path default；restore the OSPFv3 ECMP path limit；restore the default BGP equal-cost path count
- 合法语法：

  ```text
  undo maximum load-balancing
  ```
  ```text
  undo maximum load-balancing [ebgp|ibgp]
  ```

## `undo network`

- 类别：配置命令
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- 用途（设备帮助）：remove a BGP network；remove a RIP network；remove a RIPng network；remove an OSPF network；remove the IPv4 pool network
- 合法语法：

  ```text
  undo network
  ```
  ```text
  undo network ADDRESS MASK
  ```
  ```text
  undo network X.X.X.X
  ```
  ```text
  undo network X.X.X.X X.X.X.X
  ```
  ```text
  undo network X:X::X/M
  ```

## `undo passive-interface default`

- 类别：配置命令
- 视图：`RIPng视图`、`RIP视图`
- 用途（设备帮助）：restore passive interface default
- 合法语法：

  ```text
  undo passive-interface default
  ```

## `undo passive-mode`

- 类别：配置命令
- 视图：`BFD会话视图`
- 用途（设备帮助）：undo passive-mode
- 合法语法：

  ```text
  undo passive-mode
  ```

## `undo preference`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：restore RIP route preference
- 合法语法：

  ```text
  undo preference
  ```

## `undo router-id`

- 类别：配置命令
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- 用途（设备帮助）：remove BGP router ID；remove OSPF router ID；remove the OSPFv3 router ID
- 合法语法：

  ```text
  undo router-id
  ```

## `undo silent-interface`

- 类别：配置命令
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- 用途（设备帮助）：enable RIP updates on an interface；restore OSPF Hellos on an interface；restore OSPFv3 Hellos on an interface
- 合法语法：

  ```text
  undo silent-interface INTERFACE
  ```

## `version`

- 类别：配置命令
- 视图：`RIP视图`
- 用途（设备帮助）：set RIP version
- 合法语法：

  ```text
  version {1|2}
  ```
