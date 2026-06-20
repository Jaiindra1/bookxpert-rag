import os
from dotenv import load_dotenv
import chromadb
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load ChromaDB
client = chromadb.PersistentClient(path="./db")

collection = client.get_collection("resume_collection")

# User Question
question = "What experience does Jai have?"

# Retrieve context
results = collection.query(
    query_texts=[question],
    n_results=2
)

context = "\n".join(results["documents"][0])

print("\nRetrieved Context:")
print(context)

# Gemini
model = genai.GenerativeModel("models/gemini-2.5-flash")

prompt = f"""
Answer using only the provided context.

Context:
{context}

Question:
{question}
"""

response = model.generate_content(prompt)

print("\nAnswer:")
print(response.text)