# GRE Key

## `gre key`

**功能**：为GRE封装配置可选的32位Key。
**命令格式**：`gre key KEY`
**视图**：`tunnel-protocol gre`的Tunnel接口视图。
**缺省情况**：不携带GRE Key。
**注意事项**：两端Key必须一致；该命令不适用于IP-in-IP、WireGuard或AmneziaWG。
**撤销命令**：`undo gre key`。


[功能目录](../tunnel-settings.md) · [命令参数](../reference/tunnels.md)
