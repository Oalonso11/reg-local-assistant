import os

from config import (
    DATA_DIR,
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from app.loader import load_pdf_pages
from app.chunker import split_pages_into_chunks
from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore

def get_pdf_files(data_dir: str) -> list[str]:
    pdf_files = []

    for file_name in os.listdir(data_dir):
        if file_name.lower().endswith(".pdf"):
            pdf_files.append(os.path.join(data_dir, file_name))

    return pdf_files

def main():
    pdf_files = get_pdf_files(DATA_DIR)

    if not pdf_files:
        print("No PDF files found in the data directory.")
        return

    print(f"PDF files found: {len(pdf_files)}")

    all_pages = []

    for pdf_path in pdf_files:
        print(f"Loading pages from: {pdf_path}")
        pages = load_pdf_pages(pdf_path)
        all_pages.extend(pages)

    print(f"Total pages loaded: {len(all_pages)}")

    print("Splitting pages into chunks...")
    chunks = split_pages_into_chunks(
        all_pages,
        chunk_size=CHUNK_SIZE,
        overlap=CHUNK_OVERLAP,
    )
    print(f"Total chunks created: {len(chunks)}")

    print("Loading embedding model...")
    embedding_model = EmbeddingModel(EMBEDDING_MODEL_NAME)

    print("Encoding chunks...")
    chunk_texts = [chunk["text"] for chunk in chunks]
    chunk_embeddings = embedding_model.encode_texts(chunk_texts)

    print("Initializing vector store...")
    vector_store = VectorStore(CHROMA_PATH, COLLECTION_NAME)

    print("Resetting collection before indexing...")
    vector_store.reset_collection()

    print("Storing chunks in vector database...")
    vector_store.add_documents(chunks, chunk_embeddings)

    
    print("Indexing completed successfully.")
    


if __name__ == "__main__":
    main()