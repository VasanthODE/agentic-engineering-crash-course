# AI Agent Engineering — Interactive Course

A complete, self-contained course on building production AI agents — 8 lessons,
each with interactive demos and an end-of-lesson quiz, plus runnable Python examples.

## How to use
Open **`course.html`** in any browser (no internet needed). It's a guided pipeline:
work through Lesson 1 → 8 in order. Each lesson embeds its interactive companion,
then ends with a short quiz. Quiz answer positions are shuffled on every load.

## Contents
- `course.html` ............. the master course (start here)
- `lessons/` ............... the 8 standalone interactive lessons + capstone index
- `examples/` ............. runnable Python illustrations (one per key lesson)

## Running the Python examples
    pip install -r examples/requirements.txt
    export ANTHROPIC_API_KEY=sk-...        # for examples that call the API
    python examples/04_react_loop.py

Examples 06 and 07 (routing, guardrails) and 08 (tracing/eval) run with no API key.

## The 8 steps
1. LLM Fundamentals · 2. Context Engineering · 3. Memory · 4. Agentic Workflows
5. MCP & Tools · 6. AI Gateways · 7. Guardrails & Safety · 8. Observability & Evaluation
