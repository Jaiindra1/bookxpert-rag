from pypdf import PdfReader
import chromadb

reader = PdfReader("Jai_Indra_Teja_Resume-Final-2.pdf")

text = ""

for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(text):
    end = min(start + chunk_size, len(text))

    chunks.append(text[start:end])

    start += chunk_size - overlap

client = chromadb.PersistentClient(path="./db")

collection = client.get_or_create_collection(
    name="resume_rag"
)

# Clear old data if rerunning
try:
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])
except:
    pass

collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(f"Stored {len(chunks)} chunks")