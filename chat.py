from config import (
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL_NAME,
    LLM_MODEL_NAME,
    TOP_K,
)

from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore
from app.query_engine import QueryEngine

def main():
    print("Loading embedding model...")
    embedding_model = EmbeddingModel(EMBEDDING_MODEL_NAME)

    print("Connecting to vector store...")
    vector_store = VectorStore(CHROMA_PATH, COLLECTION_NAME)

    print("Initializing query engine...")
    query_engine = QueryEngine(embedding_model, vector_store, LLM_MODEL_NAME)

    while True:
        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() == "exit":
            break

        result = query_engine.ask(question, top_k=TOP_K)

        print("\nAnswer:")
        print(result["answer"])

        print("\nSources:")
        for source in result["sources"]:
            print(
                f"- {source['source']} | page {source['page']} | chunk {source['chunk_index']}"
            )


if __name__ == "__main__":
    main()