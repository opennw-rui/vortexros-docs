document.addEventListener("DOMContentLoaded", () => {
  if (!navigator.clipboard) return;
  for (const block of document.querySelectorAll(".rst-content div.highlight")) {
    const code = block.querySelector("pre");
    if (!code) continue;
    const button = document.createElement("button");
    button.type = "button";
    button.className = "manual-copy";
    button.textContent = "复制";
    button.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(code.textContent.trimEnd());
        button.textContent = "已复制";
      } catch {
        button.textContent = "请手动复制";
      }
    });
    block.append(button);
  }
});
