import os
from pathlib import Path

import chromadb
import ollama
from dotenv import load_dotenv
from google import genai

load_dotenv()

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="university_policy")
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

rag_prompt = """
You are an HR assistant for Westbrook University.
Answer the user's question using only the context provided below.
If the answer is not in the context, say you don't know.
"""


def create_database():
    print("Vectorizing Documents...")
    docs_folder = Path("documents")  # your subfolder name
    ids, documents, metadatas = [], [], []
    for file in docs_folder.glob("*.md"):  # change to *.txt if needed
        text = file.read_text(encoding="utf-8")
        ids.append(file.stem)  # filename without extension, e.g. "employee_handbook"
        documents.append(text)
        metadatas.append({"filename": file.name})
    collection.add(ids=ids, documents=documents, metadatas=metadatas)
    print("Done Vectorizing Documents...")


def query_genai(user_question: str):
    # 1. Retrieve relevant chunks from ChromaDB
    results = collection.query(
        query_texts=[user_question],
        n_results=3,
    )

    # 2. Build context string from retrieved documents
    retrieved_docs = results["documents"][0]  # list of doc strings
    context = "\n\n---\n\n".join(retrieved_docs)

    # 3. Send to Gemini with context injected into the prompt
    prompt = f"""
    {rag_prompt}

    Context:
    {context}

    Question: {user_question}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    print(f"\nAnswer: {response.text}")

    # Optional: see which documents were used
    print(f"\nSources: {[m['filename'] for m in results['metadatas'][0]]}")


def query_local(user_question: str):
    # 1. Retrieve relevant chunks from ChromaDB
    results = collection.query(query_texts=[user_question], n_results=3)
    context = "\n\n---\n\n".join(results["documents"][0])

    # 3. Send to Gemini with context injected into the prompt
    prompt = f"""
    {rag_prompt}

    Context:
    {context}

    Question: {user_question}
    """
    print("Prompting model...")
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )
    print(response["message"]["content"])

    # Optional: see which documents were used
    print(f"\nSources: {[m['filename'] for m in results['metadatas'][0]]}")


create_database()
qry = input("Query: ")

# UPDATE for the method you wish to use
query_local(qry)
# query_genai(qry)
