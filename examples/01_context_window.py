"""Lesson 2 — Context Engineering: the message array IS the agent's world."""
import anthropic
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

SYSTEM = "You are a concise banking support agent. Only answer account questions."

def ask(history, user_msg):
    history.append({"role": "user", "content": user_msg})
    resp = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=512,
        system=SYSTEM, messages=history)
    text = resp.content[0].text
    history.append({"role": "assistant", "content": text})
    return text  # note: history grows every turn -> token cost climbs

if __name__ == "__main__":
    h = []
    print(ask(h, "What's my balance?"))
