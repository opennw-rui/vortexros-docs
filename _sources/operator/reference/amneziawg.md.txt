# AmneziaWG

[配置指南](../amneziawg.md)

共用命令：[`allowd-ip`](tunnels.md#cmd-allowd-ip)、[`keepalive`](tunnels.md#cmd-keepalive)、[`peer`](tunnels.md#cmd-peer)、[`presharedkey`](tunnels.md#cmd-presharedkey)、[`publickey`](tunnels.md#cmd-publickey)、[`privatekey`](tunnels.md#cmd-privatekey)、[`source-port`](tunnels.md#cmd-source-port)。

## `amneziawg profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`系统视图`（也可从其他配置视图直接调用）
- CLI 帮助：enter an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `AMNEZIAWG-PROFILE` | AmneziaWG profile name | 输入值 |

## `amneziawg-profile`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：bind an AmneziaWG profile
- 合法语法：

  ```text
  amneziawg-profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `AMNEZIAWG-PROFILE` | AmneziaWG profile name | 输入值 |

## `disable-cookies enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable cookie replies disabled
- 合法语法：

  ```text
  disable-cookies enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `display amneziawg`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display AmneziaWG configuration and runtime
- 合法语法：

  ```text
  display amneziawg { profile [NAME] | peer [PROFILE [PEER]] | interface [TUNNEL] }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `profile` | profiles | 关键字 |
| peer / profile | `AMNEZIAWG-PROFILE` | profile name | 输入值、可选 |
| 命令后 | `peer` | peers | 关键字 |
| AMNEZIAWG-PROFILE | `AMNEZIAWG-PEER` | peer name | 输入值、可选 |
| 命令后 | `interface` | interfaces | 关键字 |
| interface | `TUNNEL-IF` | Tunnel interface | 输入值、可选 |

## `header cookie`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set cookie message header range
- 合法语法：

  ```text
  header cookie LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | lowest header | 输入值 |
| INTEGER<1-4294967295> | `INTEGER<1-4294967295>` | highest header | 输入值 |

## `header init`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set init message header range
- 合法语法：

  ```text
  header init LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | lowest header | 输入值 |
| INTEGER<1-4294967295> | `INTEGER<1-4294967295>` | highest header | 输入值 |

## `header response`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set response message header range
- 合法语法：

  ```text
  header response LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | lowest header | 输入值 |
| INTEGER<1-4294967295> | `INTEGER<1-4294967295>` | highest header | 输入值 |

## `header transport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set transport message header range
- 合法语法：

  ```text
  header transport LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-4294967295>` | lowest header | 输入值 |
| INTEGER<1-4294967295> | `INTEGER<1-4294967295>` | highest header | 输入值 |

## `header-protection`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable ChaCha20 message header protection
- 合法语法：

  ```text
  header-protection { KEY | cipher CIPHERTEXT }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | base64 32-byte key | 输入值 |
| 命令后 | `cipher` | device-encrypted key | 关键字 |
| cipher | `CIPHERTEXT` | encrypted key material | 输入值 |

## `junk count`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set random junk packet count
- 合法语法：

  ```text
  junk count INTEGER<0-128>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-128>` | junk packet count | 输入值 |

## `junk size`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set random junk packet size range
- 合法语法：

  ```text
  junk size MIN MAX
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum bytes | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum bytes | 输入值 |

## `junk-packet`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set a raw or dynamic handshake signature packet
- 合法语法：

  ```text
  junk-packet SLOT { BASE64 | expression EXPRESSION }
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-5>` | slot | 输入值 |
| INTEGER<1-5> | `BASE64` | raw payload, maximum 512 bytes | 输入值 |
| INTEGER<1-5> | `expression` | dynamic signature expression | 关键字 |
| expression | `STRING<1-4096>` | quoted sequence of b/c/t/r/rc/rd tags | 输入值 |

## `padding content`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set decrypted content padding range
- 合法语法：

  ```text
  padding content MIN MAX
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum bytes | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum bytes | 输入值 |

## `padding cookie`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set cookie reply fixed padding
- 合法语法：

  ```text
  padding cookie INTEGER<0-1024>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-1024>` | padding bytes | 输入值 |

## `padding init`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set handshake initiation fixed padding
- 合法语法：

  ```text
  padding init INTEGER<0-1024>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-1024>` | padding bytes | 输入值 |

## `padding response`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set handshake response fixed padding
- 合法语法：

  ```text
  padding response INTEGER<0-1024>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-1024>` | padding bytes | 输入值 |

## `padding transport`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set transport packet fixed padding
- 合法语法：

  ```text
  padding transport INTEGER<0-1024>
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-1024>` | padding bytes | 输入值 |

## `random-trailers enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：enable random packet trailers
- 合法语法：

  ```text
  random-trailers enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `timing keepalive`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set keepalive random range
- 合法语法：

  ```text
  timing keepalive LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum | 输入值 |

## `timing max-handshakes`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set max-handshakes random range
- 合法语法：

  ```text
  timing max-handshakes LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum | 输入值 |

## `timing reject-after`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set reject-after random range
- 合法语法：

  ```text
  timing reject-after LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum | 输入值 |

## `timing rekey-after`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set rekey-after random range
- 合法语法：

  ```text
  timing rekey-after LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum | 输入值 |

## `timing rekey-timeout`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：set rekey-timeout random range
- 合法语法：

  ```text
  timing rekey-timeout LOW HIGH
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<0-65535>` | minimum | 输入值 |
| INTEGER<0-65535> | `INTEGER<0-65535>` | maximum | 输入值 |

## `undo amneziawg profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`系统视图`
- CLI 帮助：delete an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg profile NAME
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `AMNEZIAWG-PROFILE` | AmneziaWG profile name | 输入值 |

## `undo amneziawg-profile`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：unbind an AmneziaWG profile
- 合法语法：

  ```text
  undo amneziawg-profile
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：隧道
接口类别：AmneziaWG 隧道
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。

## `undo disable-cookies enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable cookie replies disabled
- 合法语法：

  ```text
  undo disable-cookies enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo header cookie`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default cookie message header
- 合法语法：

  ```text
  undo header cookie
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo header init`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default init message header
- 合法语法：

  ```text
  undo header init
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo header response`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default response message header
- 合法语法：

  ```text
  undo header response
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo header transport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default transport message header
- 合法语法：

  ```text
  undo header transport
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo header-protection`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable message header protection
- 合法语法：

  ```text
  undo header-protection
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo junk count`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default junk packet count
- 合法语法：

  ```text
  undo junk count
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo junk size`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default junk packet size
- 合法语法：

  ```text
  undo junk size
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo junk-packet`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：delete a raw junk UDP payload slot
- 合法语法：

  ```text
  undo junk-packet SLOT
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTEGER<1-5>` | slot | 输入值 |

## `undo padding content`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default content padding
- 合法语法：

  ```text
  undo padding content
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo padding cookie`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default cookie reply padding
- 合法语法：

  ```text
  undo padding cookie
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo padding init`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default handshake initiation padding
- 合法语法：

  ```text
  undo padding init
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo padding response`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default handshake response padding
- 合法语法：

  ```text
  undo padding response
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo padding transport`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default transport packet padding
- 合法语法：

  ```text
  undo padding transport
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo random-trailers enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：disable random packet trailers
- 合法语法：

  ```text
  undo random-trailers enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timing keepalive`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default keepalive timing
- 合法语法：

  ```text
  undo timing keepalive
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timing max-handshakes`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default max-handshakes timing
- 合法语法：

  ```text
  undo timing max-handshakes
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timing reject-after`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default reject-after timing
- 合法语法：

  ```text
  undo timing reject-after
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timing rekey-after`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default rekey-after timing
- 合法语法：

  ```text
  undo timing rekey-after
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo timing rekey-timeout`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`amneziawg-profile`
- CLI 帮助：restore the default rekey-timeout timing
- 合法语法：

  ```text
  undo timing rekey-timeout
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
