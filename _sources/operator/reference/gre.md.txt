# GRE

[配置指南](../gre.md)

## `gre key`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：set the GRE key (optional)
- 合法语法：

  ```text
  gre key KEY
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：tunnel
适用分区：interface/tunnel-gre
还受当前对象/配置条件限制；以本视图 ? 为准

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `KEY` | GRE key | 输入值 |

## `undo gre key`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clear the GRE key
- 合法语法：

  ```text
  undo gre key
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。
接口类别：tunnel
适用分区：interface/tunnel-gre
还受当前对象/配置条件限制；以本视图 ? 为准

此形式没有额外参数。
