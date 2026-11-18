# 接口启用

## 适用范围与默认行为

`ipv6 enable` 适用于三层 Ethernet、三层子接口、Eth-Trunk、Vlanif、Vbdif、LoopBack 和隧道接口。二层交换成员不能在自身配置三层 IPv6；应在对应 Vlanif/Vbdif 上配置。

仅启用协议不等于配置地址。需要跨网段转发时配置全局单播地址；配置全局单播地址或启用 IPv6 服务时，系统自动准备其所需的链路本地地址。无需每次额外输入 `ipv6 address auto link-local`。单独使用这条地址命令，可在没有全局地址时保留链路本地通信。

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 ipv6 enable
 ipv6 address 2001:db8:10::1 64
#
~~~

CLI 操作：

~~~text
commit
~~~

只需要链路本地地址时：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 1
 ipv6 enable
 ipv6 address auto link-local
#
~~~

CLI 操作：

~~~text
commit
~~~

全局单播地址不会自动开启 SLAAC、DHCPv6、RA 接收或 RA 通告。链路本地地址 `fe80::/10` 用于同链路邻居发现及协议通信，不作为公网地址，也不跨路由器转发。

## 接口 MTU

启用 IPv6 的接口 MTU 至少为 1280。接口显式设置较小 MTU 时，启用 IPv6 会被拒绝；已经启用 IPv6 时，也不能将 MTU 改到 1280 以下。失败编辑保留原 Candidate。纯 IPv4 接口仍可使用较小 MTU。

## 查询

~~~text
display ipv6 interface Ethernet 0
display ipv6 interface brief
display current-configuration interface Ethernet 0
~~~

详细显示列出实际地址，包括链路本地地址；“configured”字段表示提交的配置意图。仅配置 enable 且没有地址或 IPv6 服务时，协议状态为 Down。链路本地地址经 DAD 可用后，详细显示可报告 Up；简表仍以全局地址判断该地址族的业务状态。

## 撤销与保存

先撤销接口上的 IPv6 地址、DHCPv6、RA、静态邻居和相关协议依赖，再执行：

~~~text
system-view
~~~

配置清单：

~~~text
interface Ethernet 0
 undo ipv6 address
 undo ipv6 enable
#
~~~

CLI 操作：

~~~text
commit
save
~~~

依赖未解除时操作会被拒绝，失败编辑不修改 Candidate。对于链路本地专用配置，先执行 `undo ipv6 address auto link-local`。默认关闭项不写入配置；显式 enable 和地址配置可保存、加载及重启恢复。

## 升级注意

从未要求接口显式启用 IPv6 的旧版本升级时，旧启动文件中已有 IPv6 地址、自动获取或 IPv6 协议依赖的接口会保留其启用意图。新建接口仍默认关闭 IPv6，普通 CLI 配置 IPv6 功能前仍须执行 `ipv6 enable`。

保存后，文件会明确记录接口的 `ipv6 enable`，使用当前配置格式。应保留升级前配置备份；向旧版本回退前需核对该版本能否读取新保存的命令。

如果旧启动文件没有记录数据面激活状态，将按已有的 DPDK 设备配置恢复原归属；明确记录为 Linux 的文件不会因为存在待激活的 DPDK 配置而提前接管网卡。通过 `display dataplane` 和 `display startup` 核对实际归属与所选文件。

[华为 IPv6 技术白皮书](https://actfornet.com/ueditor/php/upload/file/20181230/1546128724502700.pdf)区分接口启用、链路本地地址和全局地址。VortexROS 保留全局能力常开，并在删除前校验依赖；不宣称与每个 VRP 型号的全部命令完全相同。
