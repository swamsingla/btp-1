#!/bin/bash
# Setup and run content generation on gnode047
# Run from ada: ssh gnode047 'bash /home2/shubhamcvit/btp/scripts/setup_and_run.sh'

SCRATCH=/ssd_scratch/shubhamcvit
BTP=$SCRATCH/btp
VENV=$SCRATCH/venv
HOME_BTP=/home2/shubhamcvit/btp

echo "=== Setting up BTP on gnode047 ==="
echo "Host: $(hostname)"
echo "Date: $(date)"

# Create directories
mkdir -p $BTP/scripts $BTP/chunks/grade9/maths/chapter1 $BTP/chunks/grade10/maths/chapter1 $BTP/chunks/grade11/maths/chapter1 $BTP/chunks/grade12/maths/chapter1 $BTP/output/grade9/maths/chapter1 $BTP/output/grade10/maths/chapter1 $BTP/output/grade11/maths/chapter1 $BTP/output/grade12/maths/chapter1

# Copy files from ada home to scratch
echo "Copying files from ada home to scratch..."
cp -v $HOME_BTP/scripts/content_gen_qwen.py $BTP/scripts/
cp -v $HOME_BTP/scripts/run_generation.sh $BTP/scripts/
cp -v $HOME_BTP/scripts/test_gpu.py $BTP/scripts/
cp -v $HOME_BTP/chunks/grade9/maths/chapter1/_all_chunks.json $BTP/chunks/grade9/maths/chapter1/
cp -v $HOME_BTP/chunks/grade10/maths/chapter1/_all_chunks.json $BTP/chunks/grade10/maths/chapter1/
cp -v $HOME_BTP/chunks/grade11/maths/chapter1/_all_chunks.json $BTP/chunks/grade11/maths/chapter1/
cp -v $HOME_BTP/chunks/grade12/maths/chapter1/_all_chunks.json $BTP/chunks/grade12/maths/chapter1/

echo ""
echo "=== Testing Python environment ==="
$VENV/bin/python3 -c "
import torch
import transformers
print(f'torch={torch.__version__}')
print(f'transformers={transformers.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
print(f'GPU count: {torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    name = torch.cuda.get_device_name(i)
    mem = torch.cuda.get_device_properties(i).total_mem // 1024**2
    print(f'  GPU {i}: {name} ({mem} MB)')
"

echo ""
echo "=== Files ready ==="
ls -la $BTP/scripts/content_gen_qwen.py
ls -la $BTP/chunks/*/maths/chapter1/_all_chunks.json
echo ""
echo "SETUP_COMPLETE"
