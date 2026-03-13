import ollama

class QueryEngine:
    def __init__(self, embedding_model, vector_store, llm_model_name: str):
        self.embedding_model = embedding_model
        self.vector_store = vector_store
        self.llm_model_name = llm_model_name

    def ask(self, question: str, top_k: int = 3) -> dict:
        question_embedding = self.embedding_model.encode_text(question)
        results = self.vector_store.query(question_embedding, top_k=top_k)

        context_chunks = results["documents"]
        metadatas = results["metadatas"]

        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a helpful assistant.
Answer the question using only the provided context.
If the answer is not in the context, say that clearly.

Context:
{context}

Question:
{question}
"""

        response = ollama.chat(
            model=self.llm_model_name,
            messages=[{"role": "user", "content": prompt}],
        )

        return {
            "answer": response["message"]["content"],
            "sources": metadatas,
        }