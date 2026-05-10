<#
.SYNOPSIS
    Check status of running processes and graph quality on the compute node.
.EXAMPLE
    .\scripts\ada_check.ps1
#>

$jumpHost = "shubhamcvit@ada.iiit.ac.in"
$computeNode = "shubhamcvit@gnode048"

$checkScript = @'
echo "========== RUNNING PYTHON PROCESSES =========="
ps aux | grep '[p]ython.*graph_builder\|[p]ython.*topic_ingestion\|[p]ython.*content_planner\|[p]ython.*generate_pages' || echo "(none running)"

echo ""
echo "========== GPU USAGE =========="
nvidia-smi --query-gpu=name,utilization.gpu,memory.used,memory.total --format=csv,noheader 2>/dev/null || echo "(no GPU / nvidia-smi not available)"

echo ""
echo "========== GRAPH FILES =========="
for f in /ssd_scratch/btp-1/data/knowledge_graph/graph_by_subject/*.json; do
    if [ -f "$f" ]; then
        subj=$(basename "$f" .json)
        stats=$(python3 -c "import json; d=json.load(open('$f')); print(f'concepts={d[\"total_concepts\"]} edges={d[\"total_edges\"]}')" 2>/dev/null)
        echo "  $subj: $stats"
    fi
done
[ ! -d /ssd_scratch/btp-1/data/knowledge_graph/graph_by_subject ] && echo "  (no graph files yet)"

echo ""
echo "========== EDGE CHECKPOINTS =========="
for f in /ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_edges_grade*.json; do
    if [ -f "$f" ]; then
        grade=$(basename "$f" .json | sed 's/maths_edges_//')
        stats=$(python3 -c "
import json
d=json.load(open('$f'))
total_prereqs=sum(len(e.get('prerequisites',[])) for e in d)
print(f'records={len(d)} prereq_links={total_prereqs}')
" 2>/dev/null)
        echo "  $grade: $stats"
    fi
done

echo ""
echo "========== RECENT LOGS (last 20 lines) =========="
latest_log=$(ls -t /ssd_scratch/btp-1/logs/*.log 2>/dev/null | head -1)
if [ -n "$latest_log" ]; then
    echo "  File: $latest_log"
    tail -20 "$latest_log"
else
    echo "  (no logs found)"
fi
'@

Write-Host ">>> Checking status on $computeNode ..." -ForegroundColor Cyan
Write-Host ""

ssh -o StrictHostKeyChecking=no -J $jumpHost $computeNode $checkScript
