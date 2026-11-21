# 设备授权命令

通过用户视图申请或导入授权，用状态查询确认配置权限。完整操作见[设备授权](../../installation/license.md)。

## `display license`

- 类别：只读显示命令
- 执行效果：显示设备配置或运行状态，不修改配置。
- 视图：`任意允许视图`
- CLI 帮助：display local license and configuration access status
- 合法语法：

  ```text
  display license
  ```

## `license request export`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：export an encrypted offline license request
- 合法语法：

  ```text
  license request export FILE
  ```

## `license import`

- 类别：即时运维命令
- 执行效果：立即执行受权限控制的运维动作，不写入配置。
- 视图：`用户视图`
- CLI 帮助：verify and install an offline node license
- 合法语法：

  ```text
  license import FILE
  ```
