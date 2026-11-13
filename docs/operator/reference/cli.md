# CLI、Candidate 与配置管理


## `commit`

校验依赖并接受 Candidate。应用阶段可能改变路由、接口或策略。若返回已接受但未收敛，用 display health 查看后端。

- 类别：即时运维命令
- 执行效果：检查并应用当前登录会话中尚未提交的配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：validate and apply the current session configuration
- 合法语法：

  ```text
  commit
  ```

## `end`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- 用途（设备帮助）：return to the user view
- 合法语法：

  ```text
  end
  ```

## `export configuration`

- 类别：配置文件/恢复命令
- 执行效果：把已提交配置导出到指定文件，不改变设备状态。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：export protected committed configuration in CLI language
- 合法语法：

  ```text
  export configuration FILE
  ```

## `load configuration`

- 类别：Candidate管理命令
- 执行效果：检查配置文件并载入当前会话；执行 commit 前不会改变设备当前配置。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：parse CLI-language configuration into candidate
- 合法语法：

  ```text
  load configuration FILE
  ```

## `quit`

- 类别：视图导航命令
- 执行效果：退出当前视图或用户会话；不会进入Linux shell。
- 视图：`任意允许视图`
- 用途（设备帮助）：return to the previous view
- 合法语法：

  ```text
  quit
  ```

## `refresh configuration candidate`

适用于其他会话已经提交且本会话仍在编辑的情况。发生冲突或依赖缺失时，保留原 Candidate。

- 类别：Candidate管理命令
- 执行效果：在保留本会话修改的前提下同步其他会话已经提交的配置；发生冲突时提示具体对象。
- 视图：`任意允许视图`
- 用途（设备帮助）：rebase the private candidate onto the latest running configuration
- 合法语法：

  ```text
  refresh configuration candidate
  ```

## `refresh nat-policy interface-pat`

- 类别：配置命令
- 视图：`任意允许视图`
- 用途（设备帮助）：refresh dynamic PAT state after an interface address change
- 合法语法：

  ```text
  refresh nat-policy interface-pat INTERFACE
  ```

## `restore factory-configuration`

- 类别：配置文件/恢复命令
- 执行效果：确认后恢复出厂配置并重启相关网络服务；业务和管理连接可能中断。
- 视图：`用户视图`、`系统视图`
- 用途（设备帮助）：erase running and saved configuration, reset managed services, then restart VPP
- 合法语法：

  ```text
  restore factory-configuration
  ```

## `return`

- 类别：视图导航命令
- 执行效果：返回系统/用户视图；若存在未提交配置则按交互提示处理。
- 视图：`任意允许视图`
- 用途（设备帮助）：return to the user view
- 合法语法：

  ```text
  return
  ```

## `save`

将当前 Running 写入启动 CFG，按提示确认。本命令不提交当前会话的 Candidate。

- 类别：配置文件/恢复命令
- 执行效果：将已经提交并生效的配置保存为下次启动配置，不包含其他会话尚未提交的修改。
- 视图：`任意允许视图`
- 用途（设备帮助）：render the committed running configuration to a .cfg file
- 合法语法：

  ```text
  save [FILE.cfg]
  ```

## `startup saved-configuration`

- 类别：配置文件/恢复命令
- 执行效果：选择设备下次启动时读取的配置文件，不改变当前运行配置。
- 视图：`任意允许视图`
- 用途（设备帮助）：select a .cfg file as the next startup configuration
- 合法语法：

  ```text
  startup saved-configuration FILE.cfg
  ```

## `system-view`

- 类别：视图导航命令
- 执行效果：进入系统视图，本命令本身不修改配置。
- 视图：`用户视图`
- 用途（设备帮助）：enter the system view
- 合法语法：

  ```text
  system-view
  ```
