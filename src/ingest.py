import os
import chromadb

from config import (
    DATA_FOLDER,
    DB_PATH,
    COLLECTION_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)

from utils import extract_pdf_pages


def chunk_text(text, chunk_size=1000, overlap=200):

    chunks = []

    start = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


def main():

    print("Starting document ingestion...\n")

    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    # Clear existing collection data
    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(ids=existing["ids"])

            print("Old data removed.\n")

    except Exception:
        pass

    documents = []
    metadatas = []
    ids = []

    chunk_counter = 0

    for file_name in os.listdir(DATA_FOLDER):

        if not file_name.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(DATA_FOLDER, file_name)

        print(f"Processing: {file_name}")

        pages = extract_pdf_pages(file_path)

        for page_data in pages:

            page_num = page_data["page"]

            text = page_data["text"]

            chunks = chunk_text(
                text,
                CHUNK_SIZE,
                CHUNK_OVERLAP
            )

            for chunk in chunks:

                documents.append(chunk)

                metadatas.append(
                    {
                        "source": file_name,
                        "page": page_num
                    }
                )

                ids.append(f"chunk_{chunk_counter}")

                chunk_counter += 1

    print(f"\nTotal Chunks: {len(documents)}")

    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    print("Indexing completed successfully!")


if __name__ == "__main__":
    main()