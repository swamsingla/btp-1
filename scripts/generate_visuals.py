#!/usr/bin/env python3
"""
Generate professional knowledge graph visualizations for presentation.
Produces standalone HTML files with vis-network, dark theme, grade/area filters,
search, and a click-to-inspect detail panel.
"""

import json
import colorsys
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def hsl_to_hex(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def generate_colors(n):
    """Generate n visually distinct colors on a dark background."""
    colors = []
    for i in range(n):
        h = (i * 360 / n + 10) % 360
        # Avoid muddy yellows/browns
        s = 72 if (30 < h < 70) else 80
        l = 62 if (30 < h < 70) else 58
        colors.append(hsl_to_hex(h, s, l))
    return colors


def build_html(graph_data: dict, subject: str) -> str:
    concepts = graph_data["concepts"]
    edges_raw = graph_data["edges"]

    areas = sorted(set(v["area"] for v in concepts.values()))
    palette = generate_colors(len(areas))
    area_color = dict(zip(areas, palette))

    # Node degree for sizing
    degree: dict[str, int] = {s: 0 for s in concepts}
    for e in edges_raw:
        degree[e["from"]] = degree.get(e["from"], 0) + 1
        degree[e["to"]] = degree.get(e["to"], 0) + 1

    vis_nodes = []
    for slug, c in concepts.items():
        col = area_color[c["area"]]
        size = 10 + min(degree.get(slug, 0) * 2, 24)
        prereqs = c.get("prerequisites", [])
        leads = c.get("leads_to", [])
        vis_nodes.append(
            {
                "id": slug,
                "label": c["canonical_name"],
                "area": c["area"],
                "grades": c["grades"],
                "description": c.get("description", ""),
                "prerequisites": prereqs,
                "leads_to": leads,
                "color": {
                    "background": col,
                    "border": col,
                    "highlight": {"background": "#ffffff", "border": col},
                    "hover": {"background": "#e2e8f0", "border": col},
                },
                "size": size,
                "font": {"color": "#f1f5f9", "size": 11, "face": "Inter"},
                "borderWidth": 0,
                "borderWidthSelected": 3,
            }
        )

    vis_edges = []
    for e in edges_raw:
        vis_edges.append(
            {
                "from": e["from"],
                "to": e["to"],
                "arrows": {"to": {"enabled": True, "scaleFactor": 0.45}},
                "color": {"color": "#2d3f55", "highlight": "#818cf8", "opacity": 0.8},
                "smooth": {"type": "curvedCW", "roundness": 0.12},
                "width": 1.2,
            }
        )

    all_grades = sorted(set(g for c in concepts.values() for g in c["grades"]))
    total_c = graph_data["total_concepts"]
    total_e = graph_data["total_edges"]
    num_areas = len(areas)

    nodes_json = json.dumps(vis_nodes, ensure_ascii=False)
    edges_json = json.dumps(vis_edges, ensure_ascii=False)
    area_color_json = json.dumps(area_color, ensure_ascii=False)

    grade_options = "".join(
        f'<label class="grade-chip active" data-grade="{g}" onclick="toggleGrade(this)">{g}</label>\n'
        for g in all_grades
    )

    legend_html = "".join(
        f'<div class="legend-row active" data-area="{a}" onclick="toggleArea(this)">'
        f'<span class="ldot" style="background:{c}"></span>'
        f'<span class="lname">{a}</span></div>\n'
        for a, c in area_color.items()
    )

    title_color = "#818cf8" if subject == "Mathematics" else "#34d399"
    icon = "∑" if subject == "Mathematics" else "⚛"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{subject} Knowledge Graph</title>
<!-- standalone build bundles its own CSS and exposes the global `vis` -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/standalone/umd/vis-network.min.js"
  integrity="sha512-iTgTmIgxyA2YehKNVbzLJx4j9SnuC5ihtRrtxVkXH/9nF3vXBN5YeNQp+6wufBWKD3u+roHVNOvWBMufQnBbug=="
  crossorigin="anonymous"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
  rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#0b1120;--surface:#111827;--surface2:#1e293b;--border:#1e3a5f;
  --text:#e2e8f0;--muted:#64748b;--accent:{title_color};
  --sidebar:280px;--topbar:56px;
}}
html,body{{height:100%;overflow:hidden;font-family:'Inter',sans-serif;background:var(--bg);color:var(--text)}}
/* ── TOP BAR ── */
#topbar{{
  position:fixed;top:0;left:0;right:0;height:var(--topbar);
  background:var(--surface);border-bottom:1px solid var(--border);
  display:flex;align-items:center;padding:0 20px;gap:16px;z-index:100;
}}
#topbar .icon{{font-size:22px;color:var(--accent)}}
#topbar h1{{font-size:17px;font-weight:600;color:var(--text);letter-spacing:.02em}}
#topbar h1 span{{color:var(--accent)}}
.stat-pill{{
  background:var(--surface2);border:1px solid var(--border);
  border-radius:20px;padding:4px 12px;font-size:12px;color:var(--muted);
  white-space:nowrap;
}}
.stat-pill b{{color:var(--text);font-weight:600}}
#topbar .spacer{{flex:1}}
#search-wrap{{position:relative;display:flex;align-items:center}}
#search{{
  background:var(--surface2);border:1px solid var(--border);
  color:var(--text);font-family:inherit;font-size:13px;
  padding:7px 12px 7px 34px;border-radius:8px;outline:none;width:220px;
  transition:border-color .2s;
}}
#search:focus{{border-color:var(--accent)}}
#search::placeholder{{color:var(--muted)}}
#search-wrap::before{{
  content:"🔍";position:absolute;left:10px;font-size:13px;pointer-events:none;
}}
#reset-btn{{
  background:var(--surface2);border:1px solid var(--border);color:var(--muted);
  font-family:inherit;font-size:12px;padding:7px 12px;border-radius:8px;
  cursor:pointer;transition:all .2s;white-space:nowrap;
}}
#reset-btn:hover{{border-color:var(--accent);color:var(--text)}}

/* ── SIDEBAR ── */
#sidebar{{
  position:fixed;top:var(--topbar);left:0;bottom:0;width:var(--sidebar);
  background:var(--surface);border-right:1px solid var(--border);
  overflow-y:auto;z-index:50;display:flex;flex-direction:column;
}}
.sidebar-section{{padding:14px 16px;border-bottom:1px solid var(--border)}}
.sidebar-section h3{{font-size:11px;font-weight:600;text-transform:uppercase;
  letter-spacing:.1em;color:var(--muted);margin-bottom:10px}}
/* grade chips */
.grade-chips{{display:flex;flex-wrap:wrap;gap:6px}}
.grade-chip{{
  background:var(--surface2);border:1px solid var(--border);
  color:var(--muted);font-size:12px;font-weight:500;padding:4px 10px;
  border-radius:6px;cursor:pointer;transition:all .15s;user-select:none;
}}
.grade-chip.active{{background:var(--accent);border-color:var(--accent);color:#fff}}
/* legend */
.legend-row{{
  display:flex;align-items:center;gap:8px;padding:4px 0;cursor:pointer;
  border-radius:6px;transition:opacity .15s;
}}
.legend-row:not(.active){{opacity:.3}}
.legend-row:hover{{opacity:1}}
.ldot{{width:10px;height:10px;border-radius:50%;flex-shrink:0}}
.lname{{font-size:12px;color:var(--text);line-height:1.3}}

/* ── CANVAS ── */
#canvas-wrap{{
  position:fixed;top:var(--topbar);left:var(--sidebar);right:0;bottom:0;
}}
#graph{{width:100%;height:100%}}

/* ── DETAIL PANEL ── */
#detail{{
  position:fixed;top:calc(var(--topbar)+12px);right:12px;bottom:12px;
  width:300px;background:var(--surface);border:1px solid var(--border);
  border-radius:12px;z-index:200;display:flex;flex-direction:column;
  opacity:0;pointer-events:none;transform:translateX(20px);
  transition:opacity .25s,transform .25s;overflow:hidden;
}}
#detail.open{{opacity:1;pointer-events:auto;transform:translateX(0)}}
#detail-header{{
  padding:16px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:flex-start;
}}
#detail-title{{font-size:15px;font-weight:600;line-height:1.3;flex:1;padding-right:8px}}
#detail-close{{
  background:none;border:none;color:var(--muted);cursor:pointer;font-size:18px;
  line-height:1;padding:2px;
}}
#detail-close:hover{{color:var(--text)}}
#detail-body{{padding:16px;overflow-y:auto;flex:1;font-size:13px;line-height:1.6}}
.detail-meta{{
  display:flex;gap:6px;flex-wrap:wrap;margin-bottom:14px;
}}
.badge{{
  background:var(--surface2);border:1px solid var(--border);
  border-radius:20px;padding:2px 10px;font-size:11px;color:var(--muted);
}}
.badge.area{{color:var(--accent);border-color:var(--accent)}}
#detail-desc{{color:#94a3b8;margin-bottom:14px}}
.rel-section h4{{font-size:11px;font-weight:600;text-transform:uppercase;
  letter-spacing:.08em;color:var(--muted);margin-bottom:6px}}
.rel-chips{{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:12px}}
.rel-chip{{
  background:var(--surface2);border:1px solid var(--border);
  border-radius:6px;padding:3px 9px;font-size:11px;color:var(--text);
  cursor:pointer;transition:border-color .15s;
}}
.rel-chip:hover{{border-color:var(--accent)}}

/* ── PHYSICS TOGGLE ── */
#phy-btn{{
  position:fixed;bottom:16px;left:calc(var(--sidebar)+16px);
  background:var(--surface2);border:1px solid var(--border);color:var(--muted);
  font-family:inherit;font-size:12px;padding:7px 14px;border-radius:8px;
  cursor:pointer;z-index:60;transition:all .2s;
}}
#phy-btn:hover{{border-color:var(--accent);color:var(--text)}}
#phy-btn.on{{border-color:var(--accent);color:var(--accent)}}

/* ── LOADING OVERLAY ── */
#loading{{
  position:fixed;inset:0;background:var(--bg);z-index:9999;
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;
}}
#loading h2{{font-size:20px;font-weight:600;color:var(--text)}}
#loading p{{color:var(--muted);font-size:14px}}
.spinner{{
  width:48px;height:48px;border:3px solid var(--border);
  border-top-color:var(--accent);border-radius:50%;
  animation:spin .7s linear infinite;
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
#progress-bar{{
  width:240px;height:4px;background:var(--border);border-radius:2px;overflow:hidden;
}}
#progress-fill{{
  height:100%;background:var(--accent);border-radius:2px;width:0%;
  transition:width .1s;
}}

/* scrollbar */
::-webkit-scrollbar{{width:5px}}
::-webkit-scrollbar-track{{background:transparent}}
::-webkit-scrollbar-thumb{{background:var(--border);border-radius:3px}}
::-webkit-scrollbar-thumb:hover{{background:var(--muted)}}
</style>
</head>
<body>

<!-- Loading -->
<div id="loading">
  <div class="spinner"></div>
  <h2>{icon} {subject} Knowledge Graph</h2>
  <p>Stabilising {total_c} concepts and {total_e} edges…</p>
  <div id="progress-bar"><div id="progress-fill"></div></div>
</div>

<!-- Top Bar -->
<div id="topbar">
  <span class="icon">{icon}</span>
  <h1><span>{subject}</span> Knowledge Graph</h1>
  <div class="stat-pill"><b>{total_c}</b> concepts</div>
  <div class="stat-pill"><b>{total_e}</b> prerequisite edges</div>
  <div class="stat-pill"><b>{num_areas}</b> subject areas</div>
  <div class="stat-pill"><b>Grades 6–12</b></div>
  <div class="spacer"></div>
  <div id="search-wrap">
    <input id="search" type="text" placeholder="Search concepts…" oninput="onSearch(this.value)">
  </div>
  <button id="reset-btn" onclick="resetAll()">Reset View</button>
</div>

<!-- Sidebar -->
<div id="sidebar">
  <div class="sidebar-section">
    <h3>Filter by Grade</h3>
    <div class="grade-chips">
{grade_options}    </div>
  </div>
  <div class="sidebar-section" style="flex:1">
    <h3>Subject Areas — click to toggle</h3>
    <div id="legend">
{legend_html}    </div>
  </div>
</div>

<!-- Graph Canvas -->
<div id="canvas-wrap">
  <div id="graph"></div>
</div>

<!-- Physics toggle -->
<button id="phy-btn" class="on" onclick="togglePhysics()">⚡ Physics: ON</button>

<!-- Detail Panel -->
<div id="detail">
  <div id="detail-header">
    <div id="detail-title">—</div>
    <button id="detail-close" onclick="closeDetail()">✕</button>
  </div>
  <div id="detail-body">
    <div class="detail-meta" id="detail-meta"></div>
    <p id="detail-desc"></p>
    <div id="detail-prereqs"></div>
    <div id="detail-leads"></div>
  </div>
</div>

<script>
const ALL_NODES_DATA = {nodes_json};
const ALL_EDGES_DATA = {edges_json};
const AREA_COLORS = {area_color_json};

// ── State ──
let activeGrades = new Set({json.dumps(all_grades)});
let activeAreas  = new Set(Object.keys(AREA_COLORS));
let physicsOn    = true;
let network, nodesDS, edgesDS;
let selectedNode = null;

// ── Build filtered datasets ──
function filteredNodes() {{
  return ALL_NODES_DATA.filter(n =>
    activeAreas.has(n.area) &&
    n.grades.some(g => activeGrades.has(g))
  );
}}
function filteredEdges(nodeIds) {{
  const s = new Set(nodeIds);
  return ALL_EDGES_DATA.filter(e => s.has(e.from) && s.has(e.to));
}}

// ── Init vis-network ──
function initNetwork() {{
  const container = document.getElementById("graph");
  const fn = filteredNodes();
  const ids = fn.map(n => n.id);
  const fe = filteredEdges(ids);

  nodesDS = new vis.DataSet(fn);
  edgesDS = new vis.DataSet(fe);

  const options = {{
    physics: {{
      enabled: true,
      solver: "barnesHut",
      barnesHut: {{
        gravitationalConstant: -22000,
        centralGravity: 0.25,
        springLength: 130,
        springConstant: 0.04,
        damping: 0.09,
        avoidOverlap: 0.15,
      }},
      stabilization: {{
        enabled: true,
        iterations: 500,
        updateInterval: 8,
        fit: true,
      }},
    }},
    interaction: {{
      hover: true,
      tooltipDelay: 200,
      navigationButtons: false,
      keyboard: true,
    }},
    nodes: {{
      shape: "dot",
      scaling: {{min: 8, max: 32}},
    }},
    edges: {{
      width: 1.2,
      hoverWidth: 2.5,
      selectionWidth: 3,
    }},
    layout: {{
      improvedLayout: true,
    }},
  }};

  network = new vis.Network(container, {{nodes: nodesDS, edges: edgesDS}}, options);

  network.on("stabilizationProgress", p => {{
    document.getElementById("progress-fill").style.width =
      (p.iterations / p.total * 100) + "%";
  }});

  network.on("stabilizationIterationsDone", () => {{
    document.getElementById("loading").style.display = "none";
    document.getElementById("progress-fill").style.width = "100%";
  }});

  network.on("click", params => {{
    if (params.nodes.length > 0) {{
      showDetail(params.nodes[0]);
    }} else {{
      closeDetail();
    }}
  }});
}}

// ── Detail panel ──
function showDetail(nodeId) {{
  selectedNode = nodeId;
  const n = ALL_NODES_DATA.find(x => x.id === nodeId);
  if (!n) return;

  document.getElementById("detail-title").textContent = n.label;
  document.getElementById("detail-meta").innerHTML =
    `<span class="badge area">${{n.area}}</span>` +
    n.grades.map(g => `<span class="badge">Grade ${{g}}</span>`).join("");

  document.getElementById("detail-desc").textContent = n.description || "";

  const prereqEl = document.getElementById("detail-prereqs");
  if (n.prerequisites.length > 0) {{
    prereqEl.innerHTML = `<div class="rel-section"><h4>Prerequisites</h4><div class="rel-chips">${{
      n.prerequisites.map(p => {{
        const nd = ALL_NODES_DATA.find(x => x.id === p);
        return `<span class="rel-chip" onclick="showDetail('${{p}}')">${{nd ? nd.label : p}}</span>`;
      }}).join("")
    }}</div></div>`;
  }} else prereqEl.innerHTML = "";

  const leadsEl = document.getElementById("detail-leads");
  if (n.leads_to.length > 0) {{
    leadsEl.innerHTML = `<div class="rel-section"><h4>Leads To</h4><div class="rel-chips">${{
      n.leads_to.map(p => {{
        const nd = ALL_NODES_DATA.find(x => x.id === p);
        return `<span class="rel-chip" onclick="showDetail('${{p}}')">${{nd ? nd.label : p}}</span>`;
      }}).join("")
    }}</div></div>`;
  }} else leadsEl.innerHTML = "";

  document.getElementById("detail").classList.add("open");

  // Highlight in graph
  if (network) {{
    network.selectNodes([nodeId]);
    network.focus(nodeId, {{scale: 1.2, animation: {{duration: 600, easingFunction: "easeInOutQuad"}}}});
  }}
}}

function closeDetail() {{
  document.getElementById("detail").classList.remove("open");
  selectedNode = null;
  if (network) network.unselectAll();
}}

// ── Grade toggle ──
function toggleGrade(el) {{
  const g = parseInt(el.dataset.grade);
  if (activeGrades.has(g)) {{
    if (activeGrades.size === 1) return; // keep at least one
    activeGrades.delete(g);
    el.classList.remove("active");
  }} else {{
    activeGrades.add(g);
    el.classList.add("active");
  }}
  applyFilters();
}}

// ── Area toggle ──
function toggleArea(el) {{
  const a = el.dataset.area;
  if (activeAreas.has(a)) {{
    if (activeAreas.size === 1) return;
    activeAreas.delete(a);
    el.classList.remove("active");
  }} else {{
    activeAreas.add(a);
    el.classList.add("active");
  }}
  applyFilters();
}}

// ── Apply filters ──
function applyFilters() {{
  if (!network) return;
  const fn = filteredNodes();
  const ids = fn.map(n => n.id);
  const fe = filteredEdges(ids);
  nodesDS.clear(); nodesDS.add(fn);
  edgesDS.clear(); edgesDS.add(fe);
}}

// ── Search ──
function onSearch(q) {{
  if (!network) return;
  q = q.trim().toLowerCase();
  if (!q) {{
    // reset all node styles
    nodesDS.update(nodesDS.getIds().map(id => {{
      const n = ALL_NODES_DATA.find(x => x.id === id);
      return {{id, color: n.color, opacity: 1, font: n.font}};
    }}));
    return;
  }}
  const matches = nodesDS.getIds().filter(id => {{
    const n = ALL_NODES_DATA.find(x => x.id === id);
    return n && n.label.toLowerCase().includes(q);
  }});
  nodesDS.update(nodesDS.getIds().map(id => {{
    const hit = matches.includes(id);
    return {{
      id,
      opacity: hit ? 1 : 0.08,
    }};
  }}));
  if (matches.length === 1) showDetail(matches[0]);
}}

// ── Physics toggle ──
function togglePhysics() {{
  physicsOn = !physicsOn;
  network.setOptions({{physics: {{enabled: physicsOn}}}});
  const btn = document.getElementById("phy-btn");
  btn.textContent = physicsOn ? "⚡ Physics: ON" : "⚡ Physics: OFF";
  btn.classList.toggle("on", physicsOn);
}}

// ── Reset ──
function resetAll() {{
  activeGrades = new Set({json.dumps(all_grades)});
  activeAreas  = new Set(Object.keys(AREA_COLORS));
  document.querySelectorAll(".grade-chip").forEach(el => el.classList.add("active"));
  document.querySelectorAll(".legend-row").forEach(el => el.classList.add("active"));
  document.getElementById("search").value = "";
  applyFilters();
  onSearch("");
  network.fit({{animation: true}});
  closeDetail();
}}

// ── Start ──
window.addEventListener("load", initNetwork);
</script>
</body>
</html>"""
    return html


def main():
    subjects = [
        ("maths", "Mathematics"),
        ("science", "Science"),
    ]
    for folder, subject in subjects:
        graph_path = os.path.join(BASE, "data", "knowledge_graph", folder, "graph.json")
        out_path = os.path.join(
            BASE, "data", "knowledge_graph", folder, f"{folder}_visual.html"
        )
        print(f"Loading {graph_path}…")
        with open(graph_path, encoding="utf-8") as f:
            data = json.load(f)
        html = build_html(data, subject)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = os.path.getsize(out_path) // 1024
        print(f"  ✓ Written {out_path} ({size_kb} KB)")


if __name__ == "__main__":
    main()
