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
    str(Path.home() / "models" / "llama-8b"),
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

        from transformers import BitsAndBytesConfig

        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,   # nested quantization → saves ~0.4 GB extra
        )

        log.info("Loading LLaMA model (4-bit NF4) from %s …", model_path)
        self._pipeline = pipeline(
            "text-generation",
            model=model_path,
            model_kwargs={
                "quantization_config": bnb_config,
            },
            device_map="auto",          # distributes across all available GPUs
        )
        log.info("LLaMA model loaded in 4-bit ✓")

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

        import concurrent.futures, threading

        result_holder: list = []
        exc_holder: list = []

        def _run():
            try:
                out = self._pipeline(
                    messages,
                    max_new_tokens=max_new_tokens,
                    temperature=temperature,
                    do_sample=DEFAULT_DO_SAMPLE,
                )
                result_holder.append(out)
            except Exception as e:
                exc_holder.append(e)

        thread = threading.Thread(target=_run, daemon=True)
        thread.start()
        # Timeout: 0.5s per token is generous; hard cap at 180s (3 min)
        timeout_secs = min(max(max_new_tokens * 0.5, 60), 180)
        thread.join(timeout=timeout_secs)

        if thread.is_alive():
            log.error("LLM generation timed out after %.0fs — returning empty string", timeout_secs)
            return ""

        if exc_holder:
            raise exc_holder[0]

        outputs = result_holder[0]
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
