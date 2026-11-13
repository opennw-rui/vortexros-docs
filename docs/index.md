# VortexROS 操作手册

本手册对应当前发布的 **0.28 开发版（Debug 5）**。从空白 Ubuntu 安装后，可以先在 Linux 数据面验证接口与路由，再按部署需求配置 DPDK。

| 我要做什么 | 从哪里开始 |
| --- | --- |
| 在空白 Ubuntu 上安装 | [首次安装](installation/index.md) |
| 第一次登录并验证连通性 | [从零到 Ping](quickstart.md) |
| 理解视图、提交和保存 | [CLI 使用指南](operator/01-cli.md) |
| 按场景配置接口、路由或服务 | [配置案例](examples/index.md) |
| 查询命令语法和视图 | [命令参考](operator/reference/commands.md) |
| 更新现有设备 | [升级与回退](installation/07-upgrade-uninstall.md) |

~~~{toctree}
:maxdepth: 2
:caption: 安装与入门

installation/index
quickstart
operator/01-cli
~~~

~~~{toctree}
:maxdepth: 2
:caption: 配置与运维

examples/index
operator/index
operator/09-operations
~~~

~~~{toctree}
:maxdepth: 2
:caption: 参考

operator/reference/commands
versions
~~~
