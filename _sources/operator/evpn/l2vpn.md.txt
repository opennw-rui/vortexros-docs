# L2VPN

L2VNI 把本地 VLAN/桥域映射到 VXLAN。Type-2 通告 MAC/IP，Type-3 发现泛洪成员；两端 VNI 和 RT 对应同一业务，RD 区分发布者。它扩展二层广播域，不自动提供跨 VLAN 路由。

## 配置顺序和参数

1. 配置并验证 underlay 到远端 VTEP 的路由。
2. 创建 VLAN、bridge-domain 和 L2VNI；在桥域 EVPN 视图设置 RD、RT。
3. 配置接入端口 VLAN、NVE 源地址及 BGP 动态 peer-list。
4. 建立 BGP EVPN 地址族邻居，提交。
5. 核对实际 MAC 路由、隧道和两端流量，再保存。

每个 VNI 只能由一个 NVE 拥有，静态 peer-list 与 protocol bgp 不可混用。全部 BGP VNI 使用同一个本地 NVE Source 与 underlay VPN-instance；缺省不自动建立业务。

## 验证

[双 VLAN L2VPN 案例](../../examples/evpn/l2vpn.md)列出 P1/P2/P3、主机配置及示例输出。VLAN101/VNI5010 与 VLAN102/VNI5020 独立转发：

~~~text
display bgp evpn all routing-table
display vxlan tunnel
display mac-address
display bridge-domain 101
~~~

检查两端 Type-2 MAC 路由与 Type-3 Inclusive Multicast 路由，并分别从每条客户业务发起双向探测。

## RD 和多个 RT

在桥域的 EVPN 视图配置 L2VNI 的 RD 和 RT。RD 区分路由来源；同一业务的各设备不要求使用相同 RD。导入 RT 与远端导出 RT 至少有一项匹配，才会导入该业务的路由。可以分别配置多项导入和导出 RT，两个方向的集合可以不同。

~~~text
bridge-domain 101
 evpn
  route-distinguisher 65000:101
  vpn-target 65000:50101 import-extcommunity
  vpn-target 65000:50102 import-extcommunity
  vpn-target 65000:50101 export-extcommunity
#
commit
~~~

每条命令指定一个方向；删除某个方向使用对应的 `undo vpn-target RT import-extcommunity` 或 `export-extcommunity`。新增 RT 不会撤掉现有的手动 RT，即使其值等于自动生成的 AS:VNI。撤销显式 RD 后，使用自动 RD；这会改变路由标识并重新通告，应协调维护窗口。

~~~text
bridge-domain 101
 evpn
  undo vpn-target 65000:50102 import-extcommunity
#
commit
display current-configuration configuration bridge-domain 101
display bgp evpn all routing-table mac-route
~~~

实际操作验证中，既有导入/导出 RT 保留，同时新增两方向 RT 后配置成功；撤销新增 RT 并恢复原 RD 后，普通和带 VLAN 标记客户业务均可继续通信。修改 RT 时仍需核对远端通告和客户业务，不能只依据配置存在判断业务正常。

## RD 与多个 RT

桥域 EVPN 视图可以配置多个导入和导出 RT；两种方向的集合可以不同。对端通告与本地任意一条导入 RT 匹配即可导入，删除一条匹配项后若仍有其他匹配项，业务路由仍可保留。最后一个匹配项被撤销后，对应远端路由撤出。

~~~text
bridge-domain 101
 evpn
  route-distinguisher 65000:101
  vpn-target 65000:5010 import-extcommunity
  vpn-target 65000:5010 export-extcommunity
  vpn-target 65000:6010 import-extcommunity
  vpn-target 65000:6010 export-extcommunity
#
commit
~~~

显式配置的 RT 即使恰好等于自动生成的 AS:VNI 值，也仍是用户配置；增添其他 RT 不会撤销它。在已提交的 EVPN 视图用 display this 核对当前集合，并用 MAC 路由与客户流量检查导入结果。

撤销指定方向只删除那一项，不影响其余 RT。例如 undo vpn-target 65000:6010 import-extcommunity。undo route-distinguisher 撤销显式 RD 后使用自动 RD；修改 RD 会更新该业务的路由发布身份，可能引起短暂收敛。需要固定发布身份时，两端各配置自己的唯一 RD。

## 修改和撤销

改 RT 会改变导入/导出范围，改 VNI 会改变业务映射，需协调对端。单独撤销一条 VNI 后，该业务应停止，但其他独立 VNI 应继续工作。

先撤销 NVE 中该 VNI 绑定，再清理业务端口、桥域和 RD/RT，不为单个租户关闭全局 EVPN。仍有依赖时 Candidate 会拒绝。[精确撤销](lifecycle.md)

[支持范围](../11-vxlan-evpn.md) · [命令参数](../reference/evpn.md)
