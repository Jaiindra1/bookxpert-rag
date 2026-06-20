from pypdf import PdfReader

reader = PdfReader("Jai_Indra_Teja_Resume-Final-2.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

chunk_size = 1000
overlap = 200

chunks = []

start = 0

while start < len(text):
    end = start + chunk_size

    chunks.append(text[start:end])

    start += chunk_size - overlap

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n===== CHUNK {i+1} =====")
    print(chunk[:200])