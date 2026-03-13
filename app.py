from config import (
    PDF_PATH,
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    LLM_MODEL_NAME,
)

from app.loader import extract_text_from_pdf
from app.chunker import split_text
from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore
from app.query_engine import QueryEngine


def main():
    print("Loading PDF...")
    text = extract_text_from_pdf(PDF_PATH)

    print("Splitting text into chunks...")
    chunks = split_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)
    print(f"Total chunks created: {len(chunks)}")

    print("Loading embedding model...")
    embedding_model = EmbeddingModel(EMBEDDING_MODEL_NAME)

    print("Encoding chunks...")
    chunk_embeddings = embedding_model.encode_texts(chunks)

    print("Initializing vector store...")
    vector_store = VectorStore(CHROMA_PATH, COLLECTION_NAME)

    print("Storing chunks in vector database...")
    vector_store.add_documents(chunks, chunk_embeddings)

    print("Initializing query engine...")
    query_engine = QueryEngine(embedding_model, vector_store, LLM_MODEL_NAME)

    while True:
        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() == "exit":
            break

        answer = query_engine.ask(question, top_k=TOP_K)
        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()