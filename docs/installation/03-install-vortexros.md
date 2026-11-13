# 安装 VortexROS 控制层

## 使用 Debian 包

```bash
sudo apt install ./vortexros_0.27.dev.debug14_amd64.deb
```

包只安装：

- `/usr/bin/vortexros`、`vortexrosd`、`vortexros-helper`、`vortexros-route-zapi`和`vortexros-bootstrap`；
- systemd unit；
- VortexROS自有目录；
- 安装手册、操作手册和生成的命令参考。

包不会安装第三方后端、修改网络、禁用系统服务，也不会启用或启动 `vortexros.target`。

## 从源码安装

构建需要 Go、C 编译器、FRR 开发头文件和 `pkg-config`。构建完成后：

```bash
sudo make install
```

`make install`先运行只读 preflight。若依赖不满足会停止；它只安装本项目产物，不代替管理员配置系统服务。

## 安装结果

```bash
ls -l /usr/bin/vortexros*
systemctl cat vortexros.target
test -r /usr/share/vortexros/docs/operator/README.md
test -r /usr/share/vortexros/docs/operator/reference/commands.md
test -d /VortexROS/route-static-groupd
```

`/VortexROS/route-static-groupd`权限为`root:root 0750`。管理员放入该目录顶层的CIDR文件可由CLI的`source file`引用；URL路由组下载的受管物化文件也保存在该目录的内部子目录中。

此时服务仍应保持未启动。若安装前已有旧版本正在运行，升级章节中的受控停止/恢复步骤优先。
