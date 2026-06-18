"""Lesson 8 — Observability + Evaluation: @trace spans and an eval gate."""
import time, functools, uuid

_TRACE = {"id": None, "spans": []}

def trace(fn):
    @functools.wraps(fn)
    def wrap(*a, **k):
        if _TRACE["id"] is None:
            _TRACE["id"] = uuid.uuid4().hex[:6]
        t0 = time.time(); status = "ok"
        try:
            return fn(*a, **k)
        except Exception:
            status = "error"; raise
        finally:
            _TRACE["spans"].append(
                {"name": fn.__name__, "ms": int((time.time()-t0)*1000),
                 "status": status, "trace_id": _TRACE["id"]})
    return wrap

@trace
def calc_refund(order_id, reason):
    return 50.0 if reason == "damaged" else 0.0

# --- eval suite: golden cases + grader + pass-rate gate ---
CASES = [
    {"input": (1234, "damaged"),   "expected": 50.0},
    {"input": (1234, "no_reason"), "expected": 0.0}]

def evaluate(threshold=0.95):
    passed = sum(calc_refund(*c["input"]) == c["expected"] for c in CASES)
    rate = passed / len(CASES)
    print(f"pass_rate={rate:.2f}  {'DEPLOY' if rate>=threshold else 'BLOCKED'}")
    return rate >= threshold

if __name__ == "__main__":
    evaluate()
    print("trace:", _TRACE)
