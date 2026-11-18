# GRE Key

## `gre key`

**功能**：为GRE封装配置可选的32位Key。
**命令格式**：`gre key KEY`
**视图**：`tunnel-protocol gre`的Tunnel接口视图。
**缺省情况**：不携带GRE Key。
**注意事项**：两端Key必须一致；该命令不适用于IP-in-IP、WireGuard或AmneziaWG。
**撤销命令**：`undo gre key`。


[功能目录](../tunnel-settings.md) · [命令参数](../reference/tunnels.md)

## 修改影响

修改 key 或执行 undo gre key 后，只有 commit 才会生效。提交时会重建相应 GRE 隧道，接口可能短暂 Up → Down → Up，经过该隧道的业务会受到影响。请协调两端修改；未修改的端点、VPN 和接口配置由系统保留，无需重新输入。
