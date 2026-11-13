# VortexROS 公开文档

文档基线为 VortexROS v0.28-dev-debug5。installation 与 operator 来自该版本的用户手册，命令参考沿用产品 CLI Registry 的生成结果。首页、快速入门、导航和样式在这里维护。更新文档基线时，从对应版本提取已审阅的用户手册并保留公开版的示例和链接调整。

## 本地预览

在 Python 3.11 或更新版本的虚拟环境中运行：

    python -m pip install -r requirements.txt
    zensical serve

## 发布

    zensical build --clean

GitHub Pages 使用 gh-pages 分支的根目录。将生成的 site 目录内容提交到该分支并保留 .nojekyll。main 分支保存 Markdown、主题和站点配置。
