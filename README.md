# VortexROS 公开文档

当前基线为 VortexROS 发布分支 debug5，软件标签 v0.28-dev-debug5。正文使用 Markdown，Sphinx 和 Read the Docs 主题生成静态站点。新版本发布后，更新当前基线以及版本页，并从对应版本的 CLI Registry 生成命令参考。

## 预览和构建

    python -m pip install -r requirements.txt
    sphinx-build -W -b dirhtml docs site

使用 Python 3.12 或更新版本。在本地用 python -m http.server --directory site 预览。GitHub Pages 从 gh-pages 根目录发布生成结果，保留 .nojekyll。
