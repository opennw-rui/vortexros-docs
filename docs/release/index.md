# 发布与验证

正式手册从v0.29-dev开始维护。文档站已公开不等于候选软件已经公开发布；本轮只发布手册，不推送软件仓库或部署真机。

| 组件 | 当前候选包 |
|---|---|
| VortexROS | 0.29~dev+run1 |
| VPP | 26.10.7+vortexros-vpp |
| FRR | 10.7.1-vortexros-1.7-dev |
| Kea | 3.0.3-1+vortexros1 |

单文件名为vortexros-0.29-dev-run1-amd64.run，SHA-256为d0ab84f64269ae9fc81aa8db5fced008daf3e5ee0dc8bccc90c2fc4a04949fe0。同一文件已在开发服务器QEMU完成相关定向验证，实际安装和功能结果见下方记录；文件校验本身不证明安装或转发成功。

~~~{toctree}
:maxdepth: 2

vortexros
vpp
frr
performance
cli-validation
manual-coverage
~~~
