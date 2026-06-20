import os
import chromadb
import google.generativeai as genai

from dotenv import load_dotenv

from config import (
    GEMINI_API_KEY,
    DB_PATH,
    COLLECTION_NAME,
    TOP_K
)

load_dotenv()

genai.configure(api_key=GEMINI_API_KEY)

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(
    name=COLLECTION_NAME
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)


def ask_question(question):

    results = collection.query(
        query_texts=[question],
        n_results=TOP_K
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]

    print("\nRetrieved Chunks")
    print("=" * 60)

    for i, doc in enumerate(documents):

        source = metadata[i]["source"]
        page = metadata[i]["page"]

        print(f"\nSource: {source}")
        print(f"Page: {page}")

        print(doc[:300])
        print("-" * 60)

    context = "\n\n".join(documents)

    citations = []

    for item in metadata:

        citations.append(
            f"{item['source']} (Page {item['page']})"
        )

    prompt = f"""
You are a document question answering assistant.

Rules:
1. Use ONLY the provided context.
2. If answer is not found, say:
   "I cannot find the answer in the provided documents."
3. Include citations when answering.

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    print("\nAnswer")
    print("=" * 60)

    print(response.text)

    print("\nSources")

    unique_sources = list(set(citations))

    for source in unique_sources:
        print(f"- {source}")


while True:

    question = input("\nAsk a question (or type exit): ")

    if question.lower() == "exit":
        break

    ask_question(question)