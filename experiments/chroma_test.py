import chromadb

client = chromadb.PersistentClient(path="./db")

collection = client.get_or_create_collection(
    name="resume_collection"
)

collection.add(
    documents=[
        "Jai has 10 months experience in Full Stack Development",
        "Jai worked with React and Node.js",
        "Jai built a College Management System"
    ],
    ids=["1", "2", "3"]
)

results = collection.query(
    query_texts=["What experience does Jai have?"],
    n_results=2
)

print(results)