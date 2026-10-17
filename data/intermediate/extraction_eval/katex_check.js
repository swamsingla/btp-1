// Usage: node check.js file.md  -> prints JSON {inline, display, failures:[...]}
const fs = require("fs");
const katex = require("katex");

const text = fs.readFileSync(process.argv[2], "utf8");
const found = [];

// Display math first: $$...$$ or \[...\]
const DISPLAY = /\$\$([\s\S]+?)\$\$|\\\[([\s\S]+?)\\\]/g;
// Inline math: $...$ (single line) or \(...\)
const INLINE = /(?<!\\)\$([^$\n]+?)(?<!\\)\$|\\\(([\s\S]+?)\\\)/g;

const rest = text.replace(DISPLAY, (m, a, b) => {
  found.push({ tex: a ?? b, display: true });
  return " ";
});
rest.replace(INLINE, (m, a, b) => {
  found.push({ tex: a ?? b, display: false });
  return " ";
});

const failures = [];
for (const f of found) {
  try {
    katex.renderToString(f.tex, { displayMode: f.display, throwOnError: true, strict: "ignore" });
  } catch (e) {
    failures.push({ tex: f.tex.slice(0, 120), error: String(e.message).slice(0, 120) });
  }
}

console.log(JSON.stringify({
  inline: found.filter((f) => !f.display).length,
  display: found.filter((f) => f.display).length,
  failures,
}));
