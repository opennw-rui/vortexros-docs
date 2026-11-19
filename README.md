# VortexROS 公开文档

当前文档基线为 VortexROS v0.30-dev-debug1；安装包及发布说明以 v0.30-dev-debug1 Release 为准。正文使用 Markdown，Sphinx 和 Read the Docs 主题生成静态站点。新版本发布后，更新当前基线以及版本页，并从对应版本的 CLI Registry 生成命令参考。

## 预览和构建

    python -m pip install -r requirements.txt
    sphinx-build -W -d .cache/doctrees -b dirhtml docs site

使用 Python 3.12 或更新版本。在本地用 python -m http.server --directory site 预览。GitHub Pages 从 gh-pages 根目录发布生成结果，保留 .nojekyll。

## 维护边界

用户手册、配置案例和命令参考统一在本仓库维护并发布，VortexROS 安装包不再内置手册。产品仓库保留实现、架构、开发和验证记录，不保留用户手册副本。命令参考应与目标版本的 CLI Registry 对照；正式文档从0.29-dev开始，移除此前试验版本档案。沿用的功能证据和最终包新验收分别记录，不将旧测试重标为本轮执行。

## 从产品 Registry 核对命令

在对应产品分支执行 `make docs DOCS_REFERENCE=/tmp/vortexros-commands.md`，然后在本仓执行 `python tools/check-commands.py /tmp/vortexros-commands.md`。产品构建只检查自身元数据；命令参考的路径、视图和语法在文档侧与导出文件核对。

需要检查手册配置和 CLI 示例时，在产品仓库执行 `make docs-examples DOCS_ROOT=/path/to/vortexros-docs`。这是显式文档集成检查，不是普通产品构建的前提。

## 用户手册写作约定

每个网络案例的 CE、PE、P 和路由对端均使用 VortexROS CLI；接口采用每台设备本地的 Ethernet 编号。安装系统、Bash/sudo 和救援操作单独说明，不把 Linux 网络命令混入业务组网。外部监控平台、列表发布服务和业务应用仅说明接入要求，不伪造产品未提供的客户端命令。

功能页说明用途、前提、参数、默认行为、影响和限制；案例按拓扑、逐设备配置、查询与业务检查、撤销及保存组织。不得依赖未说明的历史实验状态。显示输出按案例命名整理后标注为示例，不称为未经改动的原始终端记录。缺少公开配置入口的能力应明确说明，不从后端命令推导产品支持。

开发服务器名称、进程 PID、故障注入过程及测试次数不进入用户操作步骤。历史命令输入清单保存在 validation，仅用于维护追踪，不由站点发布，也不等同于逐功能通过证明。
