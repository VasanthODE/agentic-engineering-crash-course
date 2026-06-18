"""Lesson 6 — AI Gateways: route each request to the right-sized model."""
import re
PRICING = {  # $ per million tokens (in, out) -- illustrative
    "claude-haiku-4-5":   (0.80, 4.0),
    "claude-sonnet-4-6":  (3.0, 15.0),
    "claude-opus-4-6":    (15.0, 75.0)}

def route(prompt):
    p = prompt.lower()
    if any(w in p for w in ["analyze", "contract", "reasoning", "complex"]):
        return "claude-opus-4-6"
    if any(w in p for w in ["summarize", "extract", "draft"]):
        return "claude-sonnet-4-6"
    return "claude-haiku-4-5"  # simple / classification / lookup

def cost(model, in_tok, out_tok):
    ci, co = PRICING[model]
    return (in_tok * ci + out_tok * co) / 1e6

if __name__ == "__main__":
    for q in ["What are your hours?", "Summarize this complaint",
              "Analyze this contract for liability"]:
        m = route(q)
        print(f"{m:20s} <- {q!r}  (~${cost(m,1000,300):.5f})")
