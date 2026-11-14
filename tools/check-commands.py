"""核对分功能命令参考与产品 Registry 导出的路径、视图和语法。"""
from pathlib import Path
import re
import sys


def entries(text, level):
    return {m[1]: m[2] for m in re.finditer(
        rf"^{level} `([^`]+)`\n(.*?)(?=^#{{2,3}} |\Z)", text, re.M | re.S)}


def signature(text):
    views = re.search(r"^- 视图：(.*)$", text, re.M)
    syntax = re.findall(r"^  ```text\n(.*?)^  ```", text, re.M | re.S)
    return views[1].strip() if views else None, [x.strip() for x in syntax]


root = Path(__file__).resolve().parents[1]
exported = entries(Path(sys.argv[1]).read_text(), "###")
actual = {}
for path in (root / "docs/operator/reference").glob("*.md"):
    for name, body in entries(path.read_text(), "##").items():
        if name in actual:
            raise SystemExit(f"duplicate command: {name}")
        actual[name] = body
if actual.keys() != exported.keys():
    raise SystemExit(f"missing={sorted(exported.keys()-actual.keys())}; obsolete={sorted(actual.keys()-exported.keys())}")
for name, body in exported.items():
    if signature(body) != signature(actual[name]):
        raise SystemExit(f"outdated views or syntax: {name}")
for path in (root / "docs/installation").glob("*.md"):
    for block in re.findall(r"(?:```|~~~)[^\n]*\n(.*?)(?:```|~~~)", path.read_text(), re.S):
        for action in ("first-install.sh --apply", "vortexros-bootstrap apply", "vortexros-bootstrap restore-system-services"):
            if action in block:
                raise SystemExit(f"{path}: executable example uses removed action {action}")
print(f"COMMAND_REFERENCE_OK {len(actual)} canonical paths, views and syntax match")
