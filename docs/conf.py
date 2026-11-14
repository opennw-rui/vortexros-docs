project = "VortexROS 文档"
copyright = "VortexROS 项目"
version = "0.28"
release = "v0.28-dev-debug9"
language = "zh_CN"
extensions = ["myst_parser"]
source_suffix = {".md": "markdown"}
root_doc = "index"
myst_heading_anchors = 4
html_theme = "sphinx_rtd_theme"
html_theme_options = {"collapse_navigation": True, "navigation_depth": 3, "style_external_links": True, "titles_only": True}
html_baseurl = "https://opennw-rui.github.io/vortexros-docs/"
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["manual.css"]
html_js_files = ["copy.js"]
html_show_sourcelink = False
exclude_patterns = ["_static", "_templates"]
pygments_style = "sphinx"
highlight_language = "none"

# Keep the browser query tokenizer and the build-time index in agreement.
import re
from sphinx.search.en import SearchEnglish


class SearchVortexROS(SearchEnglish):
    lang = "vortexros"
    language_name = "VortexROS Chinese and CLI"
    js_splitter_code = """
var splitQuery = (query) => (query.match(/\\p{Script=Han}+|[a-zA-Z0-9_]+/gu) || [])
  .flatMap((word) => {
    if (!/^\\p{Script=Han}{2,}$/u.test(word)) return [word];
    const chars = [...word];
    return chars.slice(1).map((char, i) => chars[i] + char);
  });
"""

    def split(self, text):
        words = []
        for word in re.findall(r"[\u3400-\u9fff]+|[a-zA-Z0-9_]+", text):
            if len(word) > 1 and "\u3400" <= word[0] <= "\u9fff":
                words.extend(word[i:i+2] for i in range(len(word)-1))
            else:
                words.append(word)
        return words


html_search_language = "vortexros"


def setup(app):
    from pygments.lexers.special import TextLexer
    app.add_search_language(SearchVortexROS)
    app.add_lexer("vortexros-config", TextLexer)
