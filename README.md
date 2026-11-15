# VortexROS 公开文档

当前文档基线为 VortexROS 开发分支 v0.29-dev；尚未发布的变更不代表已有对应公开软件标签。正文使用 Markdown，Sphinx 和 Read the Docs 主题生成静态站点。新版本发布后，更新当前基线以及版本页，并从对应版本的 CLI Registry 生成命令参考。

## 预览和构建

    python -m pip install -r requirements.txt
    sphinx-build -W -d .cache/doctrees -b dirhtml docs site

使用 Python 3.12 或更新版本。在本地用 python -m http.server --directory site 预览。GitHub Pages 从 gh-pages 根目录发布生成结果，保留 .nojekyll。

## 维护边界

用户手册、配置案例和命令参考统一在本仓库维护并发布，VortexROS 安装包不再内置手册。产品仓库保留实现、架构、开发和验证记录，不保留用户手册副本。命令参考应与目标版本的 CLI Registry 对照；正式文档从0.29-dev开始，移除此前试验版本档案。沿用的功能证据和最终包新验收分别记录，不将旧测试重标为本轮执行。

## 从产品 Registry 核对命令

在对应产品分支执行 `make docs DOCS_REFERENCE=/tmp/vortexros-commands.md`，然后在本仓执行 `python tools/check-commands.py /tmp/vortexros-commands.md`。产品构建只检查自身元数据；命令参考的路径、视图和语法在文档侧与导出文件核对。

需要检查手册配置和 CLI 示例时，在产品仓库执行 `make docs-examples DOCS_ROOT=/path/to/vortexros-docs`。这是显式文档集成检查，不是普通产品构建的前提。
