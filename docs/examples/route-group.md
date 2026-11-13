# 路由组

**目标**：让两个目的前缀共用一个网关，后续增删成员时无需重复写下一跳。

**前提**：实验设备能直接到达 192.0.2.1，且目标前缀没有与本例冲突的同路径配置。

## 配置

~~~text
system-view
route-static group name LAB
 route 198.51.100.0/25
 route 203.0.113.0/25
 quit
ip route-static-group LAB 192.0.2.1 preference 60
commit
~~~

组定义管理成员；绑定决定下一跳。未绑定的组不会单独安装路由。参见[静态路由组](../operator/route-groups.md)。

## 验证

用 `display route-static group name LAB verbose` 检查成员，用 `display ip routing-table-group name LAB verbose` 检查应用结果。再查询目标前缀和下一跳，并从实验网发起探测。

## 撤销

先用 `undo ip route-static-group LAB 192.0.2.1` 去掉该绑定，再用 `undo route-static group name LAB` 删除已无引用的组，最后提交。确认仅该组路径被撤销。
