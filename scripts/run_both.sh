#!/bin/bash
# Run Qwen3-8B and Llama-3.1-8B content generation ONE AT A TIME
# Usage: bash run_both.sh

WORK=/ssd_scratch/shubhamcvit/btp
VENV=/ssd_scratch/shubhamcvit/venv
export HF_HOME=/ssd_scratch/shubhamcvit/hf_cache
export TRANSFORMERS_CACHE=/ssd_scratch/shubhamcvit/hf_cache
export HF_TOKEN=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
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Activate venv
source $VENV/bin/activate

cd $WORK

echo "========================================"
echo "Python: $(python3 --version)"
python3 -c "import torch; print('PyTorch:', torch.__version__, 'CUDA:', torch.cuda.is_available(), 'GPUs:', torch.cuda.device_count())"
python3 -c "import transformers; print('Transformers:', transformers.__version__)"
echo "HF_HOME: $HF_HOME"
echo "HF_TOKEN: set"
echo "========================================"

# Kill any leftover GPU processes from previous runs (only our user's)
echo "Checking for leftover GPU processes..."
nvidia-smi --query-compute-apps=pid --format=csv,noheader 2>/dev/null | while read pid; do
    if [ -n "$pid" ]; then
        owner=$(ps -o user= -p $pid 2>/dev/null)
        if [ "$owner" = "shubhamcvit" ]; then
            echo "  Killing leftover GPU process: PID $pid"
            kill -9 $pid 2>/dev/null
        fi
    fi
done
sleep 2
echo "GPU status before run:"
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader
echo "========================================"

# --- Run 1: Qwen3-8B ---
echo ""
echo "========== STARTING QWEN3-8B =========="
echo "Start time: $(date)"
python3 content_gen_qwen.py _all_chunks.json output/qwen3_v2/ 2>&1 | tee qwen3_v2_gen.log
QWEN_EXIT=$?
echo "Qwen3-8B exit code: $QWEN_EXIT"
echo "Qwen3-8B finished at: $(date)"
echo "========== QWEN3-8B DONE =========="

# Clear GPU memory between models
echo ""
echo "Clearing GPU memory between model runs..."
sleep 5
nvidia-smi --query-gpu=index,memory.used,memory.free --format=csv,noheader

# --- Run 2: Llama-3.1-8B ---
echo ""
echo "========== STARTING LLAMA-3.1-8B =========="
echo "Start time: $(date)"
python3 content_gen_llama.py _all_chunks.json output/llama31/ 2>&1 | tee llama31_gen.log
LLAMA_EXIT=$?
echo "Llama-3.1-8B exit code: $LLAMA_EXIT"
echo "Llama-3.1-8B finished at: $(date)"
echo "========== LLAMA-3.1-8B DONE =========="

echo ""
echo "Both models complete!"
echo "Qwen output: $WORK/output/qwen3_v2/"
echo "Llama output: $WORK/output/llama31/"
ls -la output/qwen3_v2/ output/llama31/
