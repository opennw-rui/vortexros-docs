# 版本与兼容

本页对应 0.29-dev-debug1 的配套 AmneziaWG 插件。协议版本、客户端应用版本与 VPP 软件版本是不同编号，不能互相替代。设备实际版本以 display version 为准；开发版本新增参数不应推定旧安装包也已支持。

## 当前支持范围

VortexROS 没有单独的 AmneziaWG version 命令，按 Profile 的参数选择报文格式，也不会自动协商或降级格式。当前具备基础混淆、S1–S4、消息头范围、签名包，以及 Header Protection、内容填充和时序等参数。

| 协议参数集合 | 配置选择 | 当前证据 |
|---|---|---|
| WireGuard 兼容格式 | 不启用混淆，H1–H4 使用默认 1、2、3、4 | 已验证 VortexROS 的 AmneziaWG 与独立 WireGuard 隧道双栈互通；第三方客户端兼容性尚未确认 |
| 1.0 / Legacy 基础格式 | Jc/Jmin/Jmax、S1/S2、四个固定 H 值；其余机制关闭 | 固定头值与 S1/S2 模式已取得本机双端双栈 1/1；第三方 Legacy 客户端兼容性尚未确认 |
| 1.5 签名格式 | 基础格式加 I1–I5 对应的签名槽位 | 静态和动态签名包已实测；第三方 1.5 客户端需按具体参数核对兼容性 |
| 2.0 参数集合 | S1–S4，加 H1–H4 非重叠范围 | 四类填充和随机头值已抓包，本机双栈各 1/1；第三方客户端兼容性尚未确认 |
| 3.1 参数集合 | 按需加入头保护、内容填充、随机尾部、时序和 Cookie 发送控制 | VortexROS 双端组合已取得 IPv4/IPv6 各方向 2/2；未认证全部官方客户端 |

版本差异按[官方协议说明](https://docs.amnezia.org/documentation/amnezia-wg/)核对。官方应用的自动部署、配置文件导入能力还取决于应用版本；例如其 3.1 部署指南使用 AmneziaVPN 5.0.2.1 或更高版本。这是官方部署流程的要求，不是已在 VortexROS 上逐一验证的客户端清单。[官方迁移指南](https://docs.amnezia.org/documentation/instructions/new-amneziawg-selfhosted/)

## 参数对照

下表用于将对端的协议参数换成 VortexROS 配置，不是把整份客户端文件直接粘贴进 CLI。

| 对端参数 | VortexROS Profile 命令 | 配置关系 |
|---|---|---|
| Jc | junk count N | 本端发送数量，可与对端不同 |
| Jmin、Jmax | junk size LOW HIGH | 本端垃圾包长度，可与对端不同 |
| S1、S2、S3、S4 | padding init / response / cookie / transport N | 对应报文格式须匹配 |
| H1、H2、H3、H4 | header init / response / cookie / transport LOW HIGH | 四类范围不重叠；双方收发范围须兼容 |
| I1–I5 | junk-packet SLOT expression EXPRESSION | 本端签名包模板，不要求对端配置相同模板 |
| HeaderProtectionKey | header-protection KEY | 双方一致的独立 32 字节密钥 |
| ContentPaddingAddition | padding content LOW HIGH | 本端内容填充范围 |
| RekeyAfterTime | timing rekey-after LOW HIGH | 本端重协商时序 |
| RekeyTimeout | timing rekey-timeout LOW HIGH | 本端握手重试间隔 |
| RejectAfterTime | timing reject-after LOW HIGH | 本端过期密钥拒绝时序 |
| KeepaliveTimeout | timing keepalive LOW HIGH | 协议保活时序，与 peer keepalive 区分 |
| MaxHandshakeAttempts | timing max-handshakes LOW HIGH | 握手重试预算阈值，见计时说明 |
| RandomTrailers | random-trailers enable | 变长尾部，双方须能识别相应格式 |
| DisableCookies | disable-cookies enable | 只控制本端 Cookie Reply 发送 |

peer keepalive 设置持续保活的秒数；目前不接受官方部分实现提供的持续保活随机范围。presharedkey 与 HeaderProtectionKey 不同：前者参与 peer 密钥协商，后者用于消息头保护，应使用不同密钥。[官方参数定义](https://github.com/amnezia-vpn/amneziawg-go#configuration)

## Legacy 配置方式

在基础互连案例的两端，为相应 Profile 选择固定消息头值，S3/S4 和新增机制保持默认。下列清单用于新建独立 Profile，不要直接叠加到已有的高级 Profile：

```text
amneziawg profile AWG-LEGACY
 junk count 3
 junk size 16 48
 padding init 24
 padding response 28
 header init 100 100
 header response 200 200
 header cookie 300 300
 header transport 400 400
#
```

peer、公钥、地址、端口及 Tunnel 绑定按[完整互连案例](../../examples/amneziawg.md)补齐。固定值在 CLI 中用相同的 LOW、HIGH 表示。对端不支持的字段不要加入其配置文件。

## 1.5 签名配置方式

在固定头值的 Profile 中按需要增加签名槽位：

```text
amneziawg profile AWG-LEGACY
 junk-packet 1 expression "<b 0x160301><t><r 32>"
#
```

此字节串只示范语法，不代表任何实际业务协议，也不保证与某种流量外观相同。VortexROS 的原始 Base64 槽位和动态表达式会在本机生成 UDP 报文。通用表达式标签包括 b、t、r、rc、rd；c 计数标签是本实现额外接受的模板语法，不能据此认定外部客户端也接受 c。

## 2.0 配置方式

在新的 Profile 中使用四类前置填充和随机头范围，不配置 3.1 机制：

```text
amneziawg profile AWG-V2
 junk count 3
 junk size 16 48
 padding init 24
 padding response 28
 padding cookie 20
 padding transport 16
 header init 100 110
 header response 200 210
 header cookie 300 310
 header transport 400 410
#
```

四类消息头范围互不重叠，接收方必须使用兼容范围和对应的填充长度。只修改一端可能使握手或数据报文无法识别。

## 3.1 配置方式

以下是使用头保护的新 Profile。SHARED_HEADER_KEY 需要替换成双方一致的独立密钥：

```text
amneziawg profile AWG-V31
 padding init 24
 padding response 24
 padding cookie 24
 padding transport 24
 header-protection SHARED_HEADER_KEY
 padding content 4 16
 random-trailers enable
 timing rekey-after 90 120
 timing rekey-timeout 4 6
 timing reject-after 170 190
 timing keepalive 8 10
 timing max-handshakes 14 18
#
```

H1–H4 保持默认 1、2、3、4，遵循官方对头保护模式的建议。头保护要求四类前置填充均不少于 12 字节。Cookie Reply 默认仍开启；只有明确需要改变本端 Cookie 发送行为时才加入 disable-cookies enable。完整双端参数、真实显示与业务验证见[高级参数案例](../../examples/amneziawg.md#高级参数配置)。

## 版本切换和检查

修改协议字段可能重建相关 peer，并使旧会话短暂中断。先确认对端支持哪些参数，再协调两端修改、提交、验证及保存。旧 Profile 中已启用的头保护、内容填充、随机尾部、时序及 S3/S4 不会因为改了 Profile 名称自动清除；切换到 Legacy 格式时必须显式撤销这些字段，或建立新的独立 Profile。撤销头保护时，应先执行 undo header-protection，再将任一前置填充降到 12 字节以下；相反顺序会被依赖校验拒绝，原字段保留。

CLI 操作：

```text
display amneziawg profile
display amneziawg peer
display amneziawg interface
display interface Tunnel 20
ping -c 3 -t 1500 198.51.100.42
```

Profile 查询是已提交参数，不是外部客户端版本检测。握手成功也不能替代业务流量验证；两端均应检查实际地址、路由、Allowed IP、接口计数和双向通信。不得仅按客户端显示的版本名称判断报文格式兼容。
