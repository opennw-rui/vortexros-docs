# 路由通用命令

(cmd-abr-summary)=
## `abr-summary`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：configure an OSPFv3 area summary；configure an area summary
- 合法语法：

  ```text
  abr-summary X.X.X.X X.X.X.X [not-advertise]
  ```
  ```text
  abr-summary X:X::X:X INTEGER<0-128> [not-advertise]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | summary network | 输入值 |
| X.X.X.X | `X.X.X.X` | summary mask | 输入值 |
| X.X.X.X | `not-advertise` | suppress this summary | 可选 |

**适用视图：`ospfv3-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X:X` | IPv6 summary prefix | 输入值 |
| X:X::X:X | `INTEGER<0-128>` | prefix length | 输入值 |
| INTEGER<0-128> | `not-advertise` | suppress this summary | 可选 |

## `aggregate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：configure a BGP aggregate route
- 合法语法：

  ```text
  aggregate ADDRESS MASK [as-set] [detail-suppressed]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 aggregate address | 输入值 |
| X.X.X.X | `X.X.X.X` | mask or prefix length | 输入值 |
| INTEGER<0-128> / X.X.X.X | `as-set` | retain component AS path information | 可选、可组合 |
| INTEGER<0-128> / X.X.X.X | `detail-suppressed` | advertise only the aggregate route | 可选、可组合 |
| 命令后 | `X:X::X` | IPv6 aggregate address | 输入值 |
| X:X::X | `INTEGER<0-128>` | IPv6 prefix length | 输入值 |

(cmd-area)=
## `area`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`OSPF视图`、`ospfv3-area`、`ospfv3`
- CLI 帮助：enter an OSPF area view；enter an OSPFv3 area view
- 合法语法：

  ```text
  area X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf, ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | OSPF area ID | 输入值 |

**适用视图：`ospfv3, ospfv3-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | OSPFv3 area ID | 输入值 |

## `auto-cost reference-bandwidth`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：set the OSPF reference bandwidth
- 合法语法：

  ```text
  auto-cost reference-bandwidth INTEGER<1-4294967>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967>` | Reference bandwidth in Mbit/s | 输入值 |

## `default-metric`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：set default metric；set the default metric for redistributed OSPF routes
- 合法语法：

  ```text
  default-metric INTEGER<1-16777214>
  ```
  ```text
  default-metric INTEGER<1-16>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-16777214>` | Default metric | 输入值 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-16>` | default metric | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-16>` | default metric | 输入值 |

## `default-route originate`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：originate a default route
- 合法语法：

  ```text
  default-route originate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `default-route-advertise`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`ospfv3`
- CLI 帮助：originate a default route into OSPF；originate an IPv6 default route into OSPFv3
- 合法语法：

  ```text
  default-route-advertise [always]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `always` | advertise even without a default route | 输入值、可选 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `always` | originate without an installed default route | 可选 |

## `graceful-restart`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart role
- 合法语法：

  ```text
  graceful-restart {enable|helper-only|disable}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `enable` | act as a graceful-restart speaker | 关键字 |
| 命令后 | `helper-only` | retain routes for restarting peers | 关键字 |
| 命令后 | `disable` | disable graceful restart | 关键字 |

## `graceful-restart timer restart`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart restart timer
- 合法语法：

  ```text
  graceful-restart timer restart INTEGER<0-4095>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-4095>` | seconds | 输入值 |

## `graceful-restart timer wait-for-rib`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：set BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  graceful-restart timer wait-for-rib INTEGER<1-4095>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4095>` | seconds | 输入值 |

(cmd-import-route)=
## `import-route`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：redistribute IPv6 routes into OSPFv3；redistribute routes into BGP；redistribute routes into IS-IS；redistribute routes into OSPF；redistribute routes into RIP
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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| bgp / direct / isis / rip / static | `route-policy NAME` | filter redistributed routes；route-policy name | 可选、可组合 |
| bgp / direct / isis / rip / static | `cost INTEGER<0-4294967295>` | set the external route metric；route metric | 可选、可组合 |
| bgp / direct / isis / rip / static | `type` | set the OSPF external metric type | 可选、可组合 |
| type | `1` | OSPF type-1 external route | 关键字 |
| type | `2` | OSPF type-2 external route | 关键字 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `bgp` | bgp routes | 关键字 |
| 命令后 | `isis` | isis routes | 关键字 |
| 命令后 | `rip` | rip routes | 关键字 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| bgp / direct / isis / ripng / static | `route-policy NAME` | filter redistributed routes；route-policy name | 可选、可组合 |
| bgp / direct / isis / ripng / static | `cost INTEGER<0-4294967295>` | set the external route metric；route metric | 可选、可组合 |
| bgp / direct / isis / ripng / static | `type` | set the OSPF external metric type | 可选、可组合 |
| type | `1` | OSPF type-1 external route | 关键字 |
| type | `2` | OSPF type-2 external route | 关键字 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `bgp` | bgp routes | 关键字 |
| 命令后 | `isis` | isis routes | 关键字 |
| 命令后 | `ripng` | ripng routes | 关键字 |

**适用视图：`bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| direct / isis / ospf / ospfv3 / rip / ripng / static | `route-policy NAME` | filter redistributed routes；route-policy name | 可选、可组合 |
| direct / isis / ospf / ospfv3 / rip / ripng / static | `cost INTEGER<0-4294967295>` | set the external route metric；route metric | 可选、可组合 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `ospf` | ospf routes | 关键字 |
| 命令后 | `ospfv3` | ospfv3 routes | 关键字 |
| 命令后 | `isis` | isis routes | 关键字 |
| 命令后 | `rip` | rip routes | 关键字 |
| 命令后 | `ripng` | ripng routes | 关键字 |

**适用视图：`rip, ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `ospf` | OSPF routes | 关键字 |
| 命令后 | `bgp` | BGP routes | 关键字 |
| 命令后 | `isis` | IS-IS routes | 关键字 |

**适用视图：`isis`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct | 关键字 |
| 命令后 | `static` | static | 关键字 |
| 命令后 | `ospf` | ospf | 关键字 |
| 命令后 | `bgp` | bgp | 关键字 |

## `log-adjacency-changes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`、`OSPF视图`
- CLI 帮助：log IS-IS adjacency changes；log OSPF adjacency changes
- 合法语法：

  ```text
  log-adjacency-changes
  ```
  ```text
  log-adjacency-changes [detail]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `detail` | log all adjacency state changes | 可选 |

**适用视图：`isis`**

此形式没有额外参数。

## `maximum load-balancing`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：set the maximum OSPFv3 ECMP paths；set the maximum number of BGP equal-cost paths；set the maximum number of RIP equal-cost paths
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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-6>` | maximum paths | 输入值 |

**适用视图：`bgp, bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| ebgp / ibgp / 命令后 | `INTEGER<1-256>` | Number of paths | 输入值 |
| 命令后 | `ebgp` | EBGP paths | 关键字 |
| 命令后 | `ibgp` | IBGP paths | 关键字 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-32>` | Maximum number of equal-cost paths | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-32>` | Maximum number of equal-cost paths | 输入值 |

(cmd-network)=
## `network`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：add an OSPF network；advertise a RIPng network；advertise a classful RIP network；configure the IPv4 pool network；originate a BGP network
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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ip-pool`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 network | 输入值 |
| X.X.X.X | `mask` | network mask | 关键字 |
| mask | `MASK` | IPv4 mask or prefix length | 输入值 |

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | network address | 输入值 |
| X.X.X.X | `X.X.X.X` | wildcard mask | 输入值 |
| X.X.X.X | `description` | network description | 可选 |
| description | `DESCRIPTION` | description text | 输入值、后续文本 |

**适用视图：`bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 network address | 输入值 |
| X.X.X.X | `X.X.X.X` | mask or prefix length | 输入值 |
| INTEGER<0-128> / X.X.X.X | `route-policy` | route policy | 可选 |
| route-policy | `ROUTE-POLICY` | Name of the route policy | 输入值 |
| 命令后 | `X:X::X` | IPv6 network address | 输入值 |
| X:X::X | `INTEGER<0-128>` | IPv6 prefix length | 输入值 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | Classful network address | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 network prefix | 输入值 |

## `passive-interface default`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：make all RIP interfaces passive
- 合法语法：

  ```text
  passive-interface default
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`rip`**

此形式没有额外参数。

**适用视图：`ripng`**

此形式没有额外参数。

## `passive-mode`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：passive-mode
- 合法语法：

  ```text
  passive-mode
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `preference`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：set RIP route preference
- 合法语法：

  ```text
  preference INTEGER<1-255>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-255>` | Preference value | 输入值 |

(cmd-router-id)=
## `router-id`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- CLI 帮助：set BGP router ID；set OSPF router ID；set the OSPFv3 router ID
- 合法语法：

  ```text
  router-id X.X.X.X
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | OSPF Private router ID value | 输入值 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | OSPFv3 router ID | 输入值 |

**适用视图：`bgp, bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 router ID | 输入值 |

## `silent-interface`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：suppress OSPF Hellos on an interface；suppress OSPFv3 Hellos on an interface；suppress RIP updates on an interface
- 合法语法：

  ```text
  silent-interface INTERFACE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

## `undo abr-summary`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF Area视图`、`ospfv3-area`
- CLI 帮助：delete an area summary；remove an OSPFv3 area summary
- 合法语法：

  ```text
  undo abr-summary X.X.X.X X.X.X.X
  ```
  ```text
  undo abr-summary X:X::X:X INTEGER<0-128>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | summary network | 输入值 |
| X.X.X.X | `X.X.X.X` | summary mask | 输入值 |

**适用视图：`ospfv3-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X:X` | IPv6 summary prefix | 输入值 |
| X:X::X:X | `INTEGER<0-128>` | prefix length | 输入值 |

## `undo aggregate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：delete a BGP aggregate route
- 合法语法：

  ```text
  undo aggregate ADDRESS MASK
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 network address | 输入值 |
| X.X.X.X | `X.X.X.X` | mask or prefix length | 输入值 |
| 命令后 | `X:X::X` | IPv6 network address | 输入值 |
| X:X::X | `INTEGER<0-128>` | IPv6 prefix length | 输入值 |

## `undo auto-cost reference-bandwidth`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`
- CLI 帮助：restore the OSPF reference bandwidth
- 合法语法：

  ```text
  undo auto-cost reference-bandwidth
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo default-metric`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：restore default metric；restore the default OSPF redistribution metric
- 合法语法：

  ```text
  undo default-metric
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

此形式没有额外参数。

**适用视图：`rip`**

此形式没有额外参数。

**适用视图：`ripng`**

此形式没有额外参数。

## `undo default-route originate`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：stop originating a default route
- 合法语法：

  ```text
  undo default-route originate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo default-route-advertise`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`ospfv3`
- CLI 帮助：remove OSPF default route advertisement；stop originating an IPv6 default route
- 合法语法：

  ```text
  undo default-route-advertise
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

此形式没有额外参数。

**适用视图：`ospfv3`**

此形式没有额外参数。

## `undo graceful-restart`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore the default BGP graceful-restart helper role
- 合法语法：

  ```text
  undo graceful-restart
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo graceful-restart timer restart`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore BGP graceful-restart restart timer
- 合法语法：

  ```text
  undo graceful-restart timer restart
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo graceful-restart timer wait-for-rib`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP视图`
- CLI 帮助：restore BGP graceful-restart wait-for-rib timer
- 合法语法：

  ```text
  undo graceful-restart timer wait-for-rib
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo import-route`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IS-IS视图`、`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：stop redistributing routes into BGP；stop redistributing routes into IS-IS；stop redistributing routes into OSPF；stop redistributing routes into OSPFv3；stop redistributing routes into RIP
- 合法语法：

  ```text
  undo import-route PROTOCOL
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `PROTOCOL` | route protocol | 输入值 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `bgp` | BGP routes | 关键字 |
| 命令后 | `isis` | IS-IS routes | 关键字 |
| 命令后 | `ripng` | RIPng routes | 关键字 |

**适用视图：`bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| direct / isis / ospf / ospfv3 / rip / ripng / static | `route-policy NAME` | filter redistributed routes；route-policy name | 可选、可组合 |
| direct / isis / ospf / ospfv3 / rip / ripng / static | `cost INTEGER<0-4294967295>` | set the external route metric；route metric | 可选、可组合 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `ospf` | ospf routes | 关键字 |
| 命令后 | `ospfv3` | ospfv3 routes | 关键字 |
| 命令后 | `isis` | isis routes | 关键字 |
| 命令后 | `rip` | rip routes | 关键字 |
| 命令后 | `ripng` | ripng routes | 关键字 |

**适用视图：`rip, ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct routes | 关键字 |
| 命令后 | `static` | static routes | 关键字 |
| 命令后 | `ospf` | OSPF routes | 关键字 |
| 命令后 | `bgp` | BGP routes | 关键字 |
| 命令后 | `isis` | IS-IS routes | 关键字 |

**适用视图：`isis`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `direct` | direct | 关键字 |
| 命令后 | `static` | static | 关键字 |
| 命令后 | `ospf` | ospf | 关键字 |
| 命令后 | `bgp` | bgp | 关键字 |

## `undo log-adjacency-changes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`IS-IS视图`、`OSPF视图`
- CLI 帮助：stop logging IS-IS adjacency changes；stop logging OSPF adjacency changes
- 合法语法：

  ```text
  undo log-adjacency-changes
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

此形式没有额外参数。

**适用视图：`isis`**

此形式没有额外参数。

## `undo maximum load-balancing`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：restore RIP path default；restore the OSPFv3 ECMP path limit；restore the default BGP equal-cost path count
- 合法语法：

  ```text
  undo maximum load-balancing
  ```
  ```text
  undo maximum load-balancing [ebgp|ibgp]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospfv3`**

此形式没有额外参数。

**适用视图：`bgp, bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `ebgp` | restore EBGP path count | 可选 |
| 命令后 | `ibgp` | restore IBGP path count | 可选 |

**适用视图：`rip`**

此形式没有额外参数。

**适用视图：`ripng`**

此形式没有额外参数。

## `undo network`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`IPv4地址池视图`、`OSPF Area视图`、`RIPng视图`、`RIP视图`
- CLI 帮助：remove a BGP network；remove a RIP network；remove a RIPng network；remove an OSPF network；remove the IPv4 pool network
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

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ip-pool`**

此形式没有额外参数。

**适用视图：`ospf-area`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | network address | 输入值 |
| X.X.X.X | `X.X.X.X` | wildcard mask | 输入值 |

**适用视图：`bgp-family`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | IPv4 network address | 输入值 |
| X.X.X.X | `X.X.X.X` | mask or prefix length | 输入值 |
| 命令后 | `X:X::X` | IPv6 network address | 输入值 |
| X:X::X | `INTEGER<0-128>` | IPv6 prefix length | 输入值 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X.X.X.X` | Classful network address | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `X:X::X/M` | IPv6 network prefix | 输入值 |

## `undo passive-interface default`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIPng视图`、`RIP视图`
- CLI 帮助：restore passive interface default
- 合法语法：

  ```text
  undo passive-interface default
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`rip`**

此形式没有额外参数。

**适用视图：`ripng`**

此形式没有额外参数。

## `undo passive-mode`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BFD会话视图`
- CLI 帮助：undo passive-mode
- 合法语法：

  ```text
  undo passive-mode
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo preference`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：restore RIP route preference
- 合法语法：

  ```text
  undo preference
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo router-id`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`、`BGP视图`、`OSPF视图`、`ospfv3`
- CLI 帮助：remove BGP router ID；remove OSPF router ID；remove the OSPFv3 router ID
- 合法语法：

  ```text
  undo router-id
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

此形式没有额外参数。

**适用视图：`ospfv3`**

此形式没有额外参数。

**适用视图：`bgp, bgp-family`**

此形式没有额外参数。

## `undo silent-interface`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`OSPF视图`、`RIPng视图`、`RIP视图`、`ospfv3`
- CLI 帮助：enable RIP updates on an interface；restore OSPF Hellos on an interface；restore OSPFv3 Hellos on an interface
- 合法语法：

  ```text
  undo silent-interface INTERFACE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

**适用视图：`ospf`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`ospfv3`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`rip`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

**适用视图：`ripng`**

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

## `version`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`RIP视图`
- CLI 帮助：set RIP version
- 合法语法：

  ```text
  version {1|2}
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `1` | RIP version 1 | 关键字 |
| 命令后 | `2` | RIP version 2 | 关键字 |

## `default-route imported`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：allow default routes selected by import-route
- 合法语法：

  ```text
  default-route imported
  ```

允许通过 `import-route` 引入 IPv4 或 IPv6 的缺省路由。用于 BGP 对应地址族，包括命名 VPN。需先配置相应的路由引入，只有被选中的缺省路由才会发布。

## `undo default-route imported`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`BGP地址族视图`
- CLI 帮助：exclude default routes from import-route
- 合法语法：

  ```text
  undo default-route imported
  ```

停止引入本地址族的缺省路由。已引入的普通前缀仍按现有策略发布。
