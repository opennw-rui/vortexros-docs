# CLI

[配置指南](../01-cli.md)

## `commit`

- 类别：即时运维命令
- 执行效果：检查并应用当前登录会话中尚未提交的配置。
- 视图：`任意允许视图`
- CLI 帮助：validate and apply the current session configuration
- 合法语法：

  ```text
  commit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `end`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- CLI 帮助：return to the user view
- 合法语法：

  ```text
  end
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `export configuration`

- 类别：配置文件/恢复命令
- 执行效果：把已提交配置导出到指定文件，不改变设备状态。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：export protected committed configuration in CLI language
- 合法语法：

  ```text
  export configuration FILE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | protected .cfg file name in the configuration directory | 输入值 |

## `load configuration`

- 类别：Candidate管理命令
- 执行效果：检查配置文件并载入当前会话；执行 commit 前不会改变设备当前配置。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：parse CLI-language configuration into candidate
- 合法语法：

  ```text
  load configuration FILE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | input path | 输入值 |

## `quit`

- 类别：视图导航命令
- 执行效果：退出当前视图或用户会话；不会进入Linux shell。
- 视图：`任意允许视图`
- CLI 帮助：return to the previous view
- 合法语法：

  ```text
  quit
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `refresh configuration candidate`

- 类别：Candidate管理命令
- 执行效果：在保留本会话修改的前提下同步其他会话已经提交的配置；发生冲突时提示具体对象。
- 视图：`任意允许视图`
- CLI 帮助：rebase the private candidate onto the latest running configuration
- 合法语法：

  ```text
  refresh configuration candidate
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `refresh nat-policy interface-pat`

- 类别：即时运维命令
- 执行效果：立即根据接口当前 IPv4 地址刷新 PAT 分配，不修改 Candidate 或 Saved。
- 视图：`任意允许视图`
- CLI 帮助：refresh dynamic PAT state after an interface address change
- 合法语法：

  ```text
  refresh nat-policy interface-pat INTERFACE
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：接口当前运行地址和 PAT 运行状态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `INTERFACE` | interface name | 输入值 |

## `restore factory-configuration`

- 类别：配置文件/恢复命令
- 执行效果：确认后恢复出厂配置并重启相关网络服务；业务和管理连接可能中断。
- 视图：`用户视图`、`系统视图`
- CLI 帮助：erase running and saved configuration, reset managed services, then restart VPP
- 合法语法：

  ```text
  restore factory-configuration
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

此形式没有额外参数。

## `return`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- CLI 帮助：return to the user view
- 合法语法：

  ```text
  return
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。

## `save`

- 类别：配置文件/恢复命令
- 执行效果：将已经提交并生效的配置保存为下次启动配置，不包含其他会话尚未提交的修改。
- 视图：`任意允许视图`
- CLI 帮助：render the committed running configuration to a .cfg file
- 合法语法：

  ```text
  save [FILE.cfg]
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | configuration file name under the config directory | 输入值、可选 |

## `startup saved-configuration`

- 类别：配置文件/恢复命令
- 执行效果：选择设备下次启动时读取的配置文件，不改变当前运行配置。
- 视图：`任意允许视图`
- CLI 帮助：select a .cfg file as the next startup configuration
- 合法语法：

  ```text
  startup saved-configuration FILE.cfg
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：后端运行态。

| 参数位置 | 关键字 / 参数 | CLI 帮助含义 | 输入方式 |
|---|---|---|---|
| 命令后 | `FILE` | existing configuration file name | 输入值 |

## `system-view`

- 类别：视图导航命令
- 执行效果：进入系统视图，本命令本身不修改配置。
- 视图：`用户视图`
- CLI 帮助：enter the system view
- 合法语法：

  ```text
  system-view
  ```

<!-- registry-parameters -->

**参数与子命令**

- 数据来源：Candidate（本会话待提交配置）。

此形式没有额外参数。
