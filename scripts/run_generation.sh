#!/bin/bash
# Run content generation for grades 9-12 maths chapter 1
# Usage: nohup bash run_generation.sh &> generation.log &

set -e
cd /ssd_scratch/shubhamcvit/btp
PYTHON=/ssd_scratch/shubhamcvit/venv/bin/python3
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export HF_HOME=/ssd_scratch/shubhamcvit/hf_cache
export TRANSFORMERS_CACHE=/ssd_scratch/shubhamcvit/hf_cache

echo "============================================"
echo "Starting content generation: $(date)"
echo "Host: $(hostname)"
nvidia-smi --query-gpu=name,memory.total --format=csv
echo "============================================"

# Grade 9 - Chapter 1: NUMBER SYSTEMS (5 topics)
echo ""
echo ">>> GRADE 9 - Chapter 1 <<<"
$PYTHON scripts/content_gen_qwen.py chunks/grade9/maths/chapter1/_all_chunks.json output/grade9/maths/chapter1/
echo ">>> GRADE 9 DONE: $(date) <<<"
touch /tmp/grade9_done

# Grade 10 - Chapter 1: Real Numbers (3 topics)
echo ""
echo ">>> GRADE 10 - Chapter 1 <<<"
$PYTHON scripts/content_gen_qwen.py chunks/grade10/maths/chapter1/_all_chunks.json output/grade10/maths/chapter1/
echo ">>> GRADE 10 DONE: $(date) <<<"

# Grade 11 - Chapter 1: SETS (15 topics)
echo ""
echo ">>> GRADE 11 - Chapter 1 <<<"
$PYTHON scripts/content_gen_qwen.py chunks/grade11/maths/chapter1/_all_chunks.json output/grade11/maths/chapter1/
echo ">>> GRADE 11 DONE: $(date) <<<"

# Grade 12 - Chapter 1: Relations and Functions (4 topics)
echo ""
echo ">>> GRADE 12 - Chapter 1 <<<"
$PYTHON scripts/content_gen_qwen.py chunks/grade12/maths/chapter1/_all_chunks.json output/grade12/maths/chapter1/
echo ">>> GRADE 12 DONE: $(date) <<<"

echo ""
echo "============================================"
echo "ALL GENERATIONS COMPLETE: $(date)"
echo "============================================"
