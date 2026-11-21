# 版本说明

本手册适用于 VortexROS 0.30-dev-debug9。正式用户手册从 0.29-dev 开始维护。

| 组件 | 配套版本 |
|---|---|
| VortexROS | 0.30-dev-debug9，Debian 包 0.30~dev.debug9 |
| VPP | 26.10.9-debug8.1+vortexros-vpp，Debian 包 26.10.9+vortexros.debug8.1-release |
| FRR | 10.7.1-vortexros-1.11-dev |
| Kea | 3.0.3-1+vortexros1 |

使用`display version`核对设备实际版本。单文件安装器包括配套组件，只更新版本或包内容有差异的组件。安装步骤见[安装](../installation/index.md)，更新和恢复见[升级与回退](../installation/07-upgrade-uninstall.md)。

软件安装包通过[项目Release](https://github.com/opennw-rui/VortexROS/releases)或项目提供的下载位置获取；文档站与软件附件分别发布。

~~~{toctree}
:maxdepth: 2

debug2
debug3
debug4
debug5
debug6
debug9
vortexros
vpp
frr
cli-validation
manual-coverage
performance
~~~
