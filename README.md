# VortexROS 公开文档

当前基线为 VortexROS 发布分支 debug9，软件标签 v0.28-dev-debug9。正文使用 Markdown，Sphinx 和 Read the Docs 主题生成静态站点。新版本发布后，更新当前基线以及版本页，并从对应版本的 CLI Registry 生成命令参考。

## 预览和构建

    python -m pip install -r requirements.txt
    sphinx-build -W -d .cache/doctrees -b dirhtml docs site

使用 Python 3.12 或更新版本。在本地用 python -m http.server --directory site 预览。GitHub Pages 从 gh-pages 根目录发布生成结果，保留 .nojekyll。

## 维护边界

用户手册、配置案例和命令参考统一在本仓库维护并发布，VortexROS 安装包不再内置手册。产品仓库保留实现、研发文档和历史验证材料。命令参考应与目标版本的 CLI Registry 对照；页面中的历史实测结果保留原版本，不作为当前版本的重新验收。
