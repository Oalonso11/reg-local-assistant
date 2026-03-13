def split_pages_into_chunks(
    pages: list[dict],
    chunk_size: int,
    overlap: int,
) -> list[dict]:
    chunks = []

    for page_data in pages:
        text = page_data["text"]
        source = page_data["source"]
        page = page_data["page"]

        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    {
                        "text": chunk_text,
                        "source": source,
                        "page": page,
                        "chunk_index": chunk_index,
                    }
                )

            start += chunk_size - overlap
            chunk_index += 1

    return chunks