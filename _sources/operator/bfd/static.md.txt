# 独立会话


```text
bfd
bfd TO-P2 bind peer-ip 10.0.12.2 source-ip 10.0.12.1 interface Vlanif 12
 log-session-changes
```

多跳会话需要显式指定 `source-ip`，VPN场景可追加 `vpn-instance BLUE`。


## 被动模式与重启

静态会话视图中的 `passive-mode` 让本端等待对端开始发送控制报文，不能将两端都设为被动后期待它们主动建立。撤销使用 `undo passive-mode`。重新进入已有静态会话时，使用原来的完整 `bfd NAME bind ...` 入口。

默认计时为 1000/1000/3，检测超时由协商后的有效参数决定。使用 display bfd session 核对双方状态；reset service bfd 会中断检测，应在维护窗口使用，等待配置回放后重新确认会话 Up。

删除会话时先撤销引用并提交，再查询会话清单确认目标不再存在。删除检测配置不会自动撤销静态路由；需要路由联动时使用相应协议绑定。

[默认计时](../bfd.md) · [双端案例](../../examples/bfd.md)


## 会话表的列

`display bfd session` 使用 `Peer` 和 `VPN` 表头，各列按实际值对齐：

| 列 | 含义 |
| --- | --- |
| Name | 静态会话名称；协议自动会话显示 dynamic |
| Peer | 对端 IP 地址 |
| Local / Remote | 本端、对端协商的会话标识，不是接口地址 |
| VPN | 会话所属路由域，default 为默认路由域 |
| Interface | 绑定接口；未显式绑定时显示 - |
| Mode | 单跳或多跳 |
| State | 后端实际状态；Pending 表示尚无对应运行会话 |

使用 `display bfd session TO-P2` 查看指定会话时，按本机 `?` 列出的参数形式输入。名称、IPv6 地址或 VPN 名称较长时，相应列会扩展，不截断内容。静态 `bind peer-ip` 入口目前使用 IPv4；动态路由协议的 IPv6 BFD 按对应协议章节配置。
