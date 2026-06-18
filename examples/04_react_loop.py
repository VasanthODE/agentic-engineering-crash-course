"""Lesson 4 — Agentic Workflows: the ReAct loop (reason -> act -> observe)."""
import anthropic, json
client = anthropic.Anthropic()

TOOLS = [{"name": "get_order", "description": "Look up an order by id.",
          "input_schema": {"type": "object",
              "properties": {"order_id": {"type": "integer"}},
              "required": ["order_id"]}}]

def run_tool(name, args):
    if name == "get_order":
        return {"order_id": args["order_id"], "status": "delivered", "damaged": True}
    return {"error": "unknown tool"}

def agent(user_msg, max_steps=5):
    msgs = [{"role": "user", "content": user_msg}]
    for _ in range(max_steps):
        resp = client.messages.create(model="claude-sonnet-4-6",
            max_tokens=512, tools=TOOLS, messages=msgs)
        # CRITICAL: check stop_reason BEFORE appending
        if resp.stop_reason != "tool_use":
            return resp.content[0].text
        msgs.append({"role": "assistant", "content": resp.content})
        results = []
        for block in resp.content:
            if block.type == "tool_use":
                out = run_tool(block.name, block.input)
                results.append({"type": "tool_result",
                    "tool_use_id": block.id,  # echo the id back
                    "content": json.dumps(out)})
        msgs.append({"role": "user", "content": results})
    return "(max steps reached)"

if __name__ == "__main__":
    print(agent("Is order 1234 eligible for a refund?"))
