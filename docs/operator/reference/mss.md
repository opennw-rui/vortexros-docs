# TCP MSS

[配置指南](../mss.md)

## `tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：clamp TCP SYN MSS on this L3 interface
- 合法语法：

  ```text
  tcp mss { clamp | MSS }
  ```

## `undo tcp mss`

- 类别：配置命令
- 视图：`接口视图`
- 用途（设备帮助）：remove TCP MSS clamping from the interface
- 合法语法：

  ```text
  undo tcp mss
  ```
