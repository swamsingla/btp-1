#!/bin/bash
cd /ssd_scratch/shubhamcvit/btp
nohup bash scripts/run_generation.sh > generation.log 2>&1 &
PID=$!
echo "Generation started with PID: $PID"
echo $PID > generation.pid
sleep 3
echo "--- First 20 lines of log ---"
head -20 generation.log 2>/dev/null || echo "Log not ready yet"
echo "---"
echo "Monitor with: tail -f /ssd_scratch/shubhamcvit/btp/generation.log"
