#!/bin/bash
# ============================================================
#  Rebuild Maths Knowledge Graph Edges
#  Run ON the compute node (gnode048) after fixing graph_builder.py
#
#  Usage: bash /ssd_scratch/btp-1/scripts/rebuild_edges.sh [--subject maths]
# ============================================================
set -e

SUBJECT="${1:---subject}"
SUBJECT_VAL="${2:-maths}"
BTP_DIR="/ssd_scratch/btp-1"
CKPT_DIR="${BTP_DIR}/data/knowledge_graph/.checkpoints"
KG_DIR="${BTP_DIR}/data/knowledge_graph"
LOGS_DIR="${BTP_DIR}/logs"

mkdir -p "${LOGS_DIR}"

echo "=== Rebuild Edges for ${SUBJECT_VAL} ==="
echo "Time: $(date)"
echo ""

# 1. Kill any existing graph_builder process
echo "--- Step 1: Killing existing graph_builder processes ---"
pkill -f "python.*graph_builder" 2>/dev/null && echo "  Killed existing process" || echo "  No existing process"
sleep 2

# 2. Delete ONLY the edge checkpoints (keep concept checkpoints!)
echo ""
echo "--- Step 2: Deleting stale edge checkpoints ---"
for f in ${CKPT_DIR}/${SUBJECT_VAL}_edges_grade*.json; do
    if [ -f "$f" ]; then
        echo "  rm $f"
        rm "$f"
    fi
done

# 3. Delete the stale subject graph (so it gets rebuilt)
echo ""
echo "--- Step 3: Deleting stale graph output ---"
rm -f "${KG_DIR}/graph_by_subject/${SUBJECT_VAL}.json"
rm -f "${KG_DIR}/graph.json"
rm -f ${KG_DIR}/graph_by_grade/grade*_${SUBJECT_VAL}.json

# 4. Re-run graph_builder for this subject
echo ""
echo "--- Step 4: Running graph_builder.py --subject ${SUBJECT_VAL} --no-skip-existing ---"
export LLAMA_MODEL_PATH="/ssd_scratch/models/llama-8b"
export PYTHONPATH="${BTP_DIR}/scripts:${PYTHONPATH}"

cd "${BTP_DIR}"
/usr/bin/python3 scripts/graph_builder.py \
    --subject "${SUBJECT_VAL}" \
    --no-skip-existing \
    --validate \
    2>&1 | tee "${LOGS_DIR}/rebuild_edges_${SUBJECT_VAL}_$(date +%Y%m%d_%H%M%S).log"

echo ""
echo "=== Done at $(date) ==="

# 5. Quick quality check
echo ""
echo "--- Quality check ---"
/usr/bin/python3 scripts/check_graph_quality.py --subject "${SUBJECT_VAL}"
