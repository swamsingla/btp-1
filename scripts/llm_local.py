#!/usr/bin/env python3
"""
Local LLaMA-8B inference helper
================================
Wraps HuggingFace transformers to provide a single `generate()` function
with the same call signature used across topic_ingestion.py,
graph_builder.py, and content_planner.py.

Model: meta-llama/Meta-Llama-3.1-8B-Instruct
Expected location: /ssd_scratch/models/llama-8b
(run download_llama.py once to place it there)

Usage:
    from llm_local import LocalLLM
    llm = LocalLLM()          # loads model on first call, cached thereafter
    text = llm.generate(system="You are ...", user="List topics for ...")
"""

import logging
import os
from pathlib import Path

log = logging.getLogger(__name__)

# ─── Model path ───────────────────────────────────────────────────────────────
DEFAULT_MODEL_PATH = os.environ.get(
    "LLAMA_MODEL_PATH",
    "/ssd_scratch/models/llama-8b",
)

# ─── Generation defaults ──────────────────────────────────────────────────────
DEFAULT_MAX_NEW_TOKENS = 4096
DEFAULT_TEMPERATURE = 0.2
DEFAULT_DO_SAMPLE = True


class LocalLLM:
    """
    Singleton-style wrapper around LLaMA-8B loaded via HuggingFace transformers.
    The model is loaded once and reused for all calls within a process.
    """

    _instance: "LocalLLM | None" = None
    _pipeline = None

    def __new__(cls, model_path: str = DEFAULT_MODEL_PATH) -> "LocalLLM":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._model_path = model_path
            cls._instance._pipeline = None
        return cls._instance

    def _load(self) -> None:
        """Load the model and tokenizer (called lazily on first generate())."""
        if self._pipeline is not None:
            return

        # Import here so the module can be imported even without GPU packages
        import torch
        from transformers import pipeline

        model_path = self._model_path
        if not Path(model_path).exists():
            raise FileNotFoundError(
                f"LLaMA model not found at {model_path}.\n"
                f"Run:  python3 scripts/download_llama.py\n"
                f"Or set LLAMA_MODEL_PATH env var to the correct path."
            )

        log.info("Loading LLaMA model from %s …", model_path)
        self._pipeline = pipeline(
            "text-generation",
            model=model_path,
            model_kwargs={
                "torch_dtype": torch.bfloat16,
            },
            device_map="auto",          # distributes across all available GPUs
        )
        log.info("LLaMA model loaded ✓")

    def generate(
        self,
        system: str,
        user: str,
        temperature: float = DEFAULT_TEMPERATURE,
        max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
    ) -> str:
        """
        Generate a response for a system+user message pair.

        Args:
            system: The system prompt (role instructions).
            user:   The user message (actual task/question).
            temperature: Sampling temperature (lower = more deterministic).
            max_new_tokens: Maximum number of tokens to generate.

        Returns:
            The assistant's reply as a plain string.
        """
        self._load()

        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

        outputs = self._pipeline(
            messages,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=DEFAULT_DO_SAMPLE,
        )

        # The pipeline returns a list; the generated text is in the last message
        generated = outputs[0]["generated_text"]
        if isinstance(generated, list):
            # Chat format: last element is the assistant turn
            return generated[-1]["content"].strip()
        # Fallback: raw string output
        return str(generated).strip()


# ─── Convenience function (drop-in for the old llm_call pattern) ──────────────

_default_llm: LocalLLM | None = None


def llm_call(
    system: str,
    user: str,
    temperature: float = DEFAULT_TEMPERATURE,
    max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
    model_path: str = DEFAULT_MODEL_PATH,
) -> str:
    """
    Module-level convenience wrapper.  Loads the model on first call.

    Example:
        from llm_local import llm_call
        response = llm_call(system="...", user="...")
    """
    global _default_llm
    if _default_llm is None:
        _default_llm = LocalLLM(model_path=model_path)
    return _default_llm.generate(system=system, user=user,
                                  temperature=temperature,
                                  max_new_tokens=max_new_tokens)
