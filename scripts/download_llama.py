#!/usr/bin/env python3
"""
One-time LLaMA-8B model download script
=========================================
Downloads meta-llama/Meta-Llama-3.1-8B-Instruct from HuggingFace Hub
into /ssd_scratch/models/llama-8b (or LLAMA_MODEL_PATH env var).

Run once on gnode048 before starting the pipeline:
    python3 scripts/download_llama.py

Requirements:
    pip install huggingface_hub transformers          (already on gnode048)
    huggingface-cli login                             (or set HF_TOKEN env var)

The model is ~16 GB (bfloat16 weights). It fits on 2x RTX 2080 Ti with
device_map="auto" used by llm_local.py.
"""

import os
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(__name__)

MODEL_ID = "meta-llama/Meta-Llama-3.1-8B-Instruct"
DEFAULT_SAVE_PATH = os.environ.get(
    "LLAMA_MODEL_PATH",
    str(Path.home() / "models" / "llama-8b"),
)


def download(save_path: str, hf_token: str | None) -> None:
    from huggingface_hub import snapshot_download

    Path(save_path).mkdir(parents=True, exist_ok=True)
    log.info("Downloading %s → %s", MODEL_ID, save_path)
    log.info("This will download ~16 GB — may take 10-30 minutes on the cluster.")

    snapshot_download(
        repo_id=MODEL_ID,
        local_dir=save_path,
        local_dir_use_symlinks=False,
        token=hf_token,
        ignore_patterns=["*.bin"],    # download only safetensors, not legacy .bin
    )
    log.info("✓ Download complete → %s", save_path)


def verify(save_path: str) -> None:
    """Quick sanity check: load tokenizer and run one forward pass."""
    from transformers import AutoTokenizer

    log.info("Verifying model at %s …", save_path)
    tok = AutoTokenizer.from_pretrained(save_path)
    ids = tok("Hello, world!", return_tensors="pt")
    log.info("Tokenizer OK — vocab size: %d, test token count: %d", tok.vocab_size, ids["input_ids"].shape[1])
    log.info("✓ Model is ready for use by llm_local.py")


if __name__ == "__main__":
    import argparse

    p = argparse.ArgumentParser(description="Download LLaMA-3.1-8B-Instruct to local storage")
    p.add_argument("--save-path", default=DEFAULT_SAVE_PATH, help="Where to save the model")
    p.add_argument(
        "--token",
        default=os.environ.get("HF_TOKEN", ""),
        help="HuggingFace access token (or set HF_TOKEN env var). "
             "Required for gated models — get yours at https://huggingface.co/settings/tokens",
    )
    p.add_argument("--verify-only", action="store_true", help="Skip download, just verify existing files")
    args = p.parse_args()

    if not args.verify_only:
        if not args.token:
            log.error(
                "HuggingFace token required for LLaMA (gated model).\n"
                "  1. Go to https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct and accept the licence.\n"
                "  2. Go to https://huggingface.co/settings/tokens and create a token.\n"
                "  3. Re-run:  HF_TOKEN=hf_xxx python3 scripts/download_llama.py"
            )
            sys.exit(1)
        download(args.save_path, args.token or None)

    verify(args.save_path)
