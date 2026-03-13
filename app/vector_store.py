import chromadb

class VectorStore:
    def __init__(self, db_path: str, collection_name: str):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection_name = collection_name
        self.collection = self.client.get_or_create_collection(name=collection_name)
        print(f"Vector DB path: {db_path}")

    def reset_collection(self) -> None:
        try:
            self.client.delete_collection(name=self.collection_name)
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(name=self.collection_name)

    def add_documents(self, chunks: list[dict], embeddings: list[list[float]]) -> None:
        ids = [
            f"{chunk['source']}_p{chunk['page']}_c{chunk['chunk_index']}"
            for chunk in chunks
        ]

        documents = [chunk["text"] for chunk in chunks]

        metadatas = [
            {
                "source": chunk["source"],
                "page": chunk["page"],
                "chunk_index": chunk["chunk_index"],
            }
            for chunk in chunks
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def query(self, query_embedding: list[float], top_k: int = 3) -> dict:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        return {
            "documents": results["documents"][0],
            "metadatas": results["metadatas"][0],
            "ids": results["ids"][0],
        }