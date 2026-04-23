#!/bin/bash
# ============================================================
#  SLURM Job Script — BTP-1 Knowledge Graph Pipeline
#  Stages 1-3: LLaMA-8B (4-bit) on GPU
#  Stage 4:    Sarvam-30B API (no GPU needed)
# ============================================================
#SBATCH --job-name=btp_pipeline
#SBATCH --output=/home2/shubhamcvit/btp-1/logs/slurm_%j.log
#SBATCH --error=/home2/shubhamcvit/btp-1/logs/slurm_%j.err
#SBATCH --gres=gpu:1
#SBATCH --mem=48G
#SBATCH --cpus-per-task=8
#SBATCH --time=05:55:00          # 5h55m — leaves buffer before 6h wall-clock limit

# ─── Paths ───────────────────────────────────────────────────────────────────
HOME_DIR="/home2/shubhamcvit"
HOME_BTP="${HOME_DIR}/btp-1"
SCRATCH_BTP="/ssd_scratch/btp-1"
MODEL_HOME="${HOME_DIR}/models/llama-8b"
MODEL_SCRATCH="/ssd_scratch/models/llama-8b"
LOGS_DIR="${HOME_BTP}/logs"

# ─── Make sure log dir exists ─────────────────────────────────────────────────
mkdir -p "${LOGS_DIR}"

echo "=== BTP Pipeline Job ==="
echo "Job ID: ${SLURM_JOB_ID}"
echo "Node:   $(hostname)"
echo "GPU:    $(nvidia-smi --query-gpu=name --format=csv,noheader | head -1)"
echo "Start:  $(date)"
echo "==============================="

# ─── Trap: sync results back to HOME before the job ends ─────────────────────
# This runs even if the job is killed by the time limit.
cleanup() {
    echo ""
    echo "=== [cleanup] Syncing results back to HOME at $(date) ==="
    rsync -az --update "${SCRATCH_BTP}/data/" "${HOME_BTP}/data/"
    echo "=== [cleanup] Sync complete ==="
}
trap cleanup EXIT

# ─── Step 1: Prepare fast SSD scratch ────────────────────────────────────────
echo ""
echo "--- Copying code + data to /ssd_scratch ---"
mkdir -p "${SCRATCH_BTP}"
rsync -az --update "${HOME_BTP}/scripts/" "${SCRATCH_BTP}/scripts/"
rsync -az --update "${HOME_BTP}/data/"    "${SCRATCH_BTP}/data/"

# ─── Step 2: Copy model to SSD scratch (fast local I/O during inference) ─────
echo ""
echo "--- Copying LLaMA model to SSD scratch ---"
if [ ! -d "${MODEL_SCRATCH}" ]; then
    mkdir -p "${MODEL_SCRATCH}"
    rsync -az --update "${MODEL_HOME}/" "${MODEL_SCRATCH}/"
    echo "    Model copied."
else
    echo "    Model already on scratch, skipping copy."
fi

# ─── Environment ─────────────────────────────────────────────────────────────
export LLAMA_MODEL_PATH="${MODEL_SCRATCH}"
export SARVAM_API_KEY="${SARVAM_API_KEY:-}"   # Set externally: export SARVAM_API_KEY=...
export PYTHONPATH="${SCRATCH_BTP}/scripts:${PYTHONPATH}"

# Activate conda env (adjust name if different)
source /opt/conda/etc/profile.d/conda.sh 2>/dev/null || true
conda activate btp 2>/dev/null || true

cd "${SCRATCH_BTP}"

# ─── Stage 1: Topic Ingestion ─────────────────────────────────────────────────
echo ""
echo "=== Stage 1: Topic Ingestion ($(date)) ==="
python3 scripts/topic_ingestion.py \
    --model-path "${LLAMA_MODEL_PATH}" \
    --skip-existing \
    2>&1 | tee -a "${LOGS_DIR}/stage1_${SLURM_JOB_ID}.log"

# ─── Stage 2: Knowledge Graph Builder ────────────────────────────────────────
echo ""
echo "=== Stage 2: Graph Builder ($(date)) ==="
python3 scripts/graph_builder.py \
    --model-path "${LLAMA_MODEL_PATH}" \
    --skip-existing \
    2>&1 | tee -a "${LOGS_DIR}/stage2_${SLURM_JOB_ID}.log"

# ─── Stage 3: Content Planner ─────────────────────────────────────────────────
echo ""
echo "=== Stage 3: Content Planner ($(date)) ==="
python3 scripts/content_planner.py \
    --model-path "${LLAMA_MODEL_PATH}" \
    --skip-existing \
    2>&1 | tee -a "${LOGS_DIR}/stage3_${SLURM_JOB_ID}.log"

# ─── Stage 4: Page Generation (Sarvam API — no GPU needed) ───────────────────
echo ""
echo "=== Stage 4: Page Generation ($(date)) ==="
python3 scripts/generate_pages.py \
    --skip-existing \
    2>&1 | tee -a "${LOGS_DIR}/stage4_${SLURM_JOB_ID}.log"

echo ""
echo "=== Pipeline complete at $(date) ==="
# Cleanup/sync runs automatically via trap EXIT
