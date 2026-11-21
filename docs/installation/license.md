# 设备授权

VortexROS 使用单设备离线授权。首次配置前，先在设备导出申请，把申请文件发送给授权提供方，再把收到的授权文件导入同一台设备。设备导出和导入时无需访问互联网。

## 授权类型

| CLI 显示 | 用途 | 有效期和作用 |
| --- | --- | --- |
| `trial` | 评估、测试和验收 | 首次成功激活后可配置 72 小时。请在授权提供方给出的首次导入截止时间之前激活。 |
| `permanent` | 客户设备长期使用 | 激活后显示 `Never`。授权在对应设备上启用配置操作。 |
| `internal` | 内部测试或交付验证 | 激活后显示 `Never`，在对应测试设备上启用配置操作。客户长期使用时申请 `permanent`。 |

授权类型决定使用场景与配置有效期。每份文件对应一台设备。试用期间导入正式授权可以继续进行配置，已经提交的业务配置无需重新输入。重复导入同一试用文件和再次申请试用均沿用首次激活时间；试用授权也不能覆盖已有的永久或内部授权。

## 申请并导入

1. 在设备的 Linux 控制台进入 VortexROS CLI。授权导出和导入使用管理员账号，在用户视图执行。

   ~~~bash
   sudo vortexros
   ~~~

2. 检查当前状态并导出申请。下面的示例在 `/VortexROS/license` 下创建 `site-a-request.vreq`。再次导出时使用新文件名。

   ~~~text
   display license
   license request export site-a-request.vreq
   ~~~

3. 将 `site-a-request.vreq` 发送给授权提供方，并注明需要试用还是正式授权。收到授权文件后，通过已有的管理文件传输方式放入设备上的 `/VortexROS/license`，确保设备管理员可读取。以下使用 `site-a-activation.vlic` 作为传输文件名。

   ~~~text
   license import site-a-activation.vlic
   display license
   ~~~

4. 确认 `License status` 为 `active`、`Configuration access` 为 `enabled`。试用设备同时核对 `Expires at` 和 `Remaining seconds`。永久授权的 `Expires at` 显示 `Never`。

省略绝对路径时，申请和授权文件均相对于 `/VortexROS/license`。设备本地已有绝对路径时也可直接使用，例如 `license import /root/site-a-activation.vlic`。请选择独立的传输名，避免使用设备管理的固定文件名 `license.vlic`。

## 试用到期、更换设备与状态查询

| 状态 | 设备行为及操作 |
| --- | --- |
| `active` | 按账号角色使用配置与运维。对试用设备，按显示的 UTC 到期时间安排导入正式授权。 |
| `unlicensed` | 配置只读。导出申请并导入对应设备的有效授权。 |
| `expired` | 已提交的转发配置和自动恢复继续运行；配置修改及提交受限。导入正式授权后重新检查配置权限。 |
| `clock-rollback` | 配置只读。核对设备时间，必要时向授权提供方提交当前状态。 |
| `invalid` | 根据 `Detail` 核对设备和授权文件。若文件来自另一台设备，在目标设备重新导出申请。 |
| `unconfigured` | 将版本和授权状态交给交付方核对所安装的软件包。 |

更换设备或重新创建虚机时，在目标设备重新导出申请，并联系授权提供方办理。已有授权设备仍可通过 `display license` 查看状态。需要支持时，可提供 `License status`、`License type`、`Node ID`、`License ID` 和 `Detail`。

[授权命令参考](../operator/reference/license.md) · [首次启动](06-first-start.md)
