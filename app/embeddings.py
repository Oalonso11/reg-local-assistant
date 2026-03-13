from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def encode_text(self, text: str) -> list[float]:
        return self.model.encode(text).tolist()

    def encode_texts(self, texts: list[str]) -> list[list[float]]:
        return self.model.encode(texts).tolist()