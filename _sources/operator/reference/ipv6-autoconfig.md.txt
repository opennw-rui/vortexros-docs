# RA 与 SLAAC

[配置指南](../ipv6-autoconfig.md)

## `ipv6 address auto global default`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive global IPv6 addresses and the default route from router advertisements
- 合法语法：

  ```text
  ipv6 address auto global default
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv6 nd ra default-route enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：install default routes learned from router advertisements
- 合法语法：

  ```text
  ipv6 nd ra default-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 address auto global default`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable automatic global IPv6 addresses and RA default routes
- 合法语法：

  ```text
  undo ipv6 address auto global default
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `undo ipv6 nd ra default-route enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable install default routes learned from router advertisements
- 合法语法：

  ```text
  undo ipv6 nd ra default-route enable
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `ipv6 address auto global`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  ipv6 address auto global
  ```

## `ipv6 address auto link-local`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：generate a link-local address without a global address
- 合法语法：

  ```text
  ipv6 address auto link-local
  ```

## `ipv6 enable`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：enable IPv6 on this Layer 3 interface
- 合法语法：

  ```text
  ipv6 enable
  ```

## `ipv6 nd autoconfig managed-address-flag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the RA managed-address flag
- 合法语法：

  ```text
  ipv6 nd autoconfig managed-address-flag
  ```

## `ipv6 nd autoconfig other-flag`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the RA other-configuration flag
- 合法语法：

  ```text
  ipv6 nd autoconfig other-flag
  ```

## `ipv6 nd ra halt`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：suppress router advertisements (default)
- 合法语法：

  ```text
  ipv6 nd ra halt
  ```

## `ipv6 nd ra lifetime`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：set the advertised router lifetime
- 合法语法：

  ```text
  ipv6 nd ra lifetime SECONDS
  ```

## `ipv6 nd ra prefix`

- 类别：配置命令
- 执行效果：修改当前会话配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：configure a prefix advertised in RA
- 合法语法：

  ```text
  ipv6 nd ra prefix IP PREFIXLEN VALID PREFERRED [no-autoconfig] [off-link]
  ```

## `undo ipv6 address auto global`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable derive IPv6 addresses from router advertisements
- 合法语法：

  ```text
  undo ipv6 address auto global
  ```

## `undo ipv6 address auto link-local`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove explicit link-local-only address generation
- 合法语法：

  ```text
  undo ipv6 address auto link-local
  ```

## `undo ipv6 enable`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：disable IPv6 after removing its dependent configuration
- 合法语法：

  ```text
  undo ipv6 enable
  ```

## `undo ipv6 nd autoconfig managed-address-flag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clear the RA managed-address flag
- 合法语法：

  ```text
  undo ipv6 nd autoconfig managed-address-flag
  ```

## `undo ipv6 nd autoconfig other-flag`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：clear the RA other-configuration flag
- 合法语法：

  ```text
  undo ipv6 nd autoconfig other-flag
  ```

## `undo ipv6 nd ra halt`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：send router advertisements
- 合法语法：

  ```text
  undo ipv6 nd ra halt
  ```

## `undo ipv6 nd ra lifetime`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：restore the default 1800-second router lifetime
- 合法语法：

  ```text
  undo ipv6 nd ra lifetime
  ```

## `undo ipv6 nd ra prefix`

- 类别：配置命令
- 执行效果：在当前会话中撤销对应配置；执行 commit 成功后生效。
- 视图：`接口视图`
- CLI 帮助：remove an advertised prefix or all explicit RA prefixes
- 合法语法：

  ```text
  undo ipv6 nd ra prefix [IP PREFIXLEN]
  ```

## `display ipv6 interface`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display IPv6 interface state and addresses
- 合法语法：

  ```text
  display ipv6 interface [IF | TYPE N]
  ```
