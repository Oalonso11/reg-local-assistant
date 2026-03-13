import os
import fitz

def load_pdf_pages(path: str) -> list[dict]:
    document = fitz.open(path)
    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text().strip()

        if text:
            pages.append(
                {
                    "source": os.path.basename(path),
                    "page": page_number,
                    "text": text,
                }
            )

    return pages