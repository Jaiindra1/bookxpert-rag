import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

result = genai.embed_content(
    model="models/gemini-embedding-001",
    content="Full Stack Developer with React and Node.js"
)

print("Length:", len(result["embedding"]))
print(result["embedding"][:10])