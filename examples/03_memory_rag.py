"""Lesson 3 — Memory: retrieve by meaning (RAG), then ground the answer."""
import anthropic
client = anthropic.Anthropic()

# toy "vector store": in reality use Qdrant + embeddings
DOCS = {"returns": "Returns accepted within 30 days of purchase.",
        "refunds": "Refunds processed to original payment in 5-7 days."}

def retrieve(query):  # naive keyword stand-in for semantic search
    return [v for k, v in DOCS.items() if any(w in query.lower() for w in k.split())]

def answer(query):
    ctx = "\n".join(retrieve(query)) or "(no docs found)"
    resp = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=300,
        system="Answer ONLY from the provided context. If unsupported, say so.",
        messages=[{"role": "user", "content": f"Context:\n{ctx}\n\nQ: {query}"}])
    return resp.content[0].text

if __name__ == "__main__":
    print(answer("how long do I have to return an item?"))
