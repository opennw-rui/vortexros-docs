# 授权与试用

默认安装包在设备首次启动 VortexROS 时自动开启 **72 小时试用**。试用期间可按账号权限配置设备。关机期间计时继续，重启和升级沿用原到期时间。

在用户视图执行：

~~~text
display license
~~~

首次试用通常显示 `License type` 为 `trial`、`License ID` 为 `built-in-trial`，且 `Configuration access` 为 `enabled`。`Activated at` 和 `Expires at` 使用 UTC，`Remaining seconds` 表示剩余秒数。

## 申请和导入授权

由设备管理员在用户视图生成本机的加密申请：

~~~text
license request export router01.vreq
~~~

相对文件名以设备上的 `/VortexROS/license/` 为基准，也可指定本机绝对路径。导出禁止覆盖同名文件。将 `router01.vreq` 交给授权提供方，注明所需授权类型。

收到本机的 `router01.vlic` 后，将其放入设备的 `/VortexROS/license/`。使用独立的传输文件名，系统使用的固定文件名为 `license.vlic`。

~~~text
license import router01.vlic
display license
~~~

导入成功后，`License status` 应为 `active`，`Configuration access` 应为 `enabled`。永久授权的 `Expires at` 显示 `Never`。配置权限随授权导入即时更新，无需重启。开发授权显示为 `internal`，正式永久授权为 `permanent`。

## 升级回退与换机

授权绑定设备的 Node ID 和主机身份。同一设备保留 `/VortexROS/license/` 下的设备身份、激活状态及已安装授权，且目标版本信任同一签发公钥时，升降级无需重新申请。升级前后核对 Node ID 和授权类型，版本相关的配置与后端要求见[升级与回退](07-upgrade-uninstall.md)。

更换设备、重新创建虚机或重装系统导致主机身份变化时，应在目标设备重新导出申请。备份已有授权时，保留整个授权目录及其权限。

## 到期和异常状态

| 状态 | 用户操作 |
| --- | --- |
| `active` | 试用用户按 `Expires at` 安排正式授权。已导入永久授权的设备显示 `Never`。 |
| `unlicensed` | 配置只读。导出本机申请并导入签发授权。 |
| `expired` | 已提交的配置与既有转发继续生效，普通配置修改受限。仍可查询、诊断、导出申请和导入授权。 |
| `clock-rollback` | 配置只读。核对系统时间后重新检查状态。 |
| `invalid` | 根据 `Detail` 检查授权和设备是否匹配。如需换机，在目标设备重新申请。 |
| `unconfigured` | 将软件版本和授权状态交给授权提供方核对安装包。 |

联系授权支持时可提供 `License status`、`License type`、`Node ID`、`License ID` 和 `Detail`。命令定义见[系统命令参考](../operator/reference/system.md#display-license)。
