"""
Generate an interactive HTML visualisation of maths_v2.json using vis-network.
Output: data/output/knowledge_graph/maths_v2_visual.html
"""
import json
from pathlib import Path

BASE = Path(__file__).parent.parent
SRC  = BASE / "data" / "output" / "knowledge_graph" / "maths_v2.json"
OUT  = BASE / "data" / "output" / "knowledge_graph" / "maths_v2_visual.html"

g = json.load(open(SRC, encoding="utf-8"))

# ── Colour palette by area ─────────────────────────────────────────────────
AREA_COLOUR = {
    "Number Systems":       "#4E9AF1",
    "Number Theory":        "#2E6DB4",
    "Algebra":              "#E76F51",
    "Geometry":             "#2A9D8F",
    "Mensuration":          "#57CC99",
    "Trigonometry":         "#F4A261",
    "Statistics":           "#9B5DE5",
    "Probability":          "#C77DFF",
    "Calculus":             "#EF233C",
    "Linear Algebra":       "#D62828",
    "Vectors":              "#F72585",
    "Set Theory":           "#4CC9F0",
    "Combinatorics":        "#7209B7",
    "Coordinate Geometry":  "#3A0CA3",
    "Sequences":            "#FFBE0B",
    "Patterns and Sequences": "#FFD60A",
    "Proportional Reasoning":"#06D6A0",
    "Optimisation":         "#118AB2",
}
DEFAULT_COLOUR = "#aaaaaa"

# ── Build nodes & edges for vis-network ───────────────────────────────────
nodes = []
for slug, c in g["concepts"].items():
    colour = AREA_COLOUR.get(c["area"], DEFAULT_COLOUR)
    grades_str = ", ".join(str(gr) for gr in c["grades"])
    tooltip = (f"<b>{c['canonical_name']}</b><br/>"
               f"<i>{c['area']}</i><br/>"
               f"Grades: {grades_str}<br/><br/>"
               f"{c['description']}")
    nodes.append({
        "id":    slug,
        "label": c["canonical_name"],
        "title": tooltip,
        "color": {"background": colour, "border": "#333",
                  "highlight": {"background": "#FFD700", "border": "#333"}},
        "font":  {"color": "#fff", "size": 12, "face": "Inter, Arial, sans-serif"},
        "shape": "box",
        "borderWidth": 1,
        "shadow": True,
        # for grade filter
        "grades": c["grades"],
        "area":   c["area"],
    })

edges = []
for e in g["edges"]:
    edges.append({
        "from":   e["from"],
        "to":     e["to"],
        "arrows": "to",
        "color":  {"color": "#888", "highlight": "#FFD700", "opacity": 0.7},
        "smooth": {"type": "curvedCW", "roundness": 0.1},
    })

# Collect unique areas for legend
areas = sorted({c["area"] for c in g["concepts"].values()})
legend_html = ""
for a in areas:
    col = AREA_COLOUR.get(a, DEFAULT_COLOUR)
    legend_html += (f'<div class="legend-item">'
                    f'<span class="legend-dot" style="background:{col}"></span>'
                    f'{a}</div>\n')

# All grades
all_grades = sorted({gr for c in g["concepts"].values() for gr in c["grades"]})
grade_buttons = "".join(
    f'<button class="grade-btn active" data-grade="{gr}" onclick="toggleGrade({gr}, this)">Grade {gr}</button>\n'
    for gr in all_grades
)

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>Maths Knowledge Graph — Grades 6–12</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Inter, Arial, sans-serif; background: #111; color: #eee; display: flex; flex-direction: column; height: 100vh; }}
  #header {{ padding: 12px 20px; background: #1a1a2e; border-bottom: 2px solid #333; display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }}
  #header h1 {{ font-size: 18px; color: #FFD700; white-space: nowrap; }}
  #stats {{ font-size: 13px; color: #aaa; }}
  #controls {{ display: flex; gap: 8px; flex-wrap: wrap; margin-left: auto; }}
  .grade-btn {{
    padding: 4px 10px; border-radius: 12px; border: 1.5px solid #555;
    background: #2a2a3e; color: #ccc; cursor: pointer; font-size: 12px; transition: 0.2s;
  }}
  .grade-btn.active {{ border-color: #FFD700; color: #FFD700; background: #333; }}
  button#resetBtn {{
    padding: 4px 12px; border-radius: 12px; border: 1.5px solid #F4A261;
    background: #2a2a3e; color: #F4A261; cursor: pointer; font-size: 12px;
  }}
  #main {{ display: flex; flex: 1; overflow: hidden; }}
  #legend {{
    width: 200px; min-width: 180px; background: #161625; padding: 12px;
    overflow-y: auto; border-right: 1px solid #333;
  }}
  #legend h3 {{ font-size: 13px; color: #aaa; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }}
  .legend-item {{ display: flex; align-items: center; gap: 8px; font-size: 12px; margin-bottom: 6px; }}
  .legend-dot {{ width: 12px; height: 12px; border-radius: 3px; flex-shrink: 0; }}
  #graph {{ flex: 1; }}
  #tooltip {{
    position: fixed; background: rgba(10,10,30,0.95); border: 1px solid #555;
    border-radius: 6px; padding: 10px 14px; font-size: 13px; pointer-events: none;
    max-width: 280px; line-height: 1.5; display: none; z-index: 100;
  }}
</style>
</head>
<body>
<div id="header">
  <h1>Maths Knowledge Graph</h1>
  <div id="stats">{g['total_concepts']} concepts &nbsp;|&nbsp; {g['total_edges']} prerequisite edges &nbsp;|&nbsp; Grades 6–12</div>
  <div id="controls">
    {grade_buttons}
    <button id="resetBtn" onclick="resetView()">↺ Reset</button>
  </div>
</div>
<div id="main">
  <div id="legend">
    <h3>Subject Area</h3>
    {legend_html}
  </div>
  <div id="graph"></div>
</div>
<div id="tooltip"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/standalone/umd/vis-network.min.js"></script>
<script>
const ALL_NODES = {json.dumps(nodes, ensure_ascii=False)};
const ALL_EDGES = {json.dumps(edges, ensure_ascii=False)};

let activeGrades = new Set({json.dumps(all_grades)});

const container = document.getElementById("graph");
let nodesDS = new vis.DataSet(ALL_NODES);
let edgesDS = new vis.DataSet(ALL_EDGES);

const options = {{
  layout: {{ improvedLayout: true, hierarchical: false }},
  physics: {{
    enabled: true,
    solver: "forceAtlas2Based",
    forceAtlas2Based: {{
      gravitationalConstant: -50,
      centralGravity: 0.006,
      springLength: 120,
      springConstant: 0.08,
      damping: 0.4,
    }},
    stabilization: {{ iterations: 250 }},
  }},
  interaction: {{
    hover: true,
    tooltipDelay: 200,
    navigationButtons: true,
    keyboard: true,
    zoomView: true,
  }},
  edges: {{ width: 1.2, selectionWidth: 2.5 }},
  nodes: {{ margin: 6 }},
}};

let network = new vis.Network(container, {{ nodes: nodesDS, edges: edgesDS }}, options);

function applyFilter() {{
  const visible = ALL_NODES.filter(n => n.grades.some(gr => activeGrades.has(gr)));
  const visibleIds = new Set(visible.map(n => n.id));
  const visEdges = ALL_EDGES.filter(e => visibleIds.has(e.from) && visibleIds.has(e.to));
  nodesDS.clear(); nodesDS.add(visible);
  edgesDS.clear(); edgesDS.add(visEdges);
}}

function toggleGrade(gr, btn) {{
  if (activeGrades.has(gr)) {{
    if (activeGrades.size === 1) return;   // keep at least one
    activeGrades.delete(gr);
    btn.classList.remove("active");
  }} else {{
    activeGrades.add(gr);
    btn.classList.add("active");
  }}
  applyFilter();
}}

function resetView() {{
  network.fit({{ animation: {{ duration: 800, easingFunction: "easeInOutQuad" }} }});
}}

// Highlight connected nodes on click
network.on("click", function(params) {{
  if (params.nodes.length > 0) {{
    const nodeId = params.nodes[0];
    const connected = network.getConnectedNodes(nodeId);
    const connEdges = network.getConnectedEdges(nodeId);
    nodesDS.forEach(n => {{
      nodesDS.update({{ id: n.id, opacity: (n.id === nodeId || connected.includes(n.id)) ? 1.0 : 0.15 }});
    }});
    edgesDS.forEach(e => {{
      edgesDS.update({{ id: e.id, color: {{ opacity: connEdges.includes(e.id) ? 1.0 : 0.05 }} }});
    }});
  }} else {{
    nodesDS.forEach(n => {{ nodesDS.update({{ id: n.id, opacity: 1.0 }}); }});
    edgesDS.forEach(e => {{ edgesDS.update({{ id: e.id, color: {{ opacity: 0.7 }} }}); }});
  }}
}});
</script>
</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"Written: {OUT}")
