import json
import faiss
import numpy as np
from src.embeddings.embedder import generate_embeddings
from src.llm.gemini_client import generate_response

index = faiss.read_index("vector_db/faiss_index.bin")

with open("data/processed/chunks.json","r",encoding="utf-8") as file:
    chunks = json.load(file)

def retrieve_context(query, top_k=3):
    query_embedding = generate_embeddings([query])
    distances, indices = index.search(np.array(query_embedding),top_k)
    retrieved_chunks = []
    for idx in indices[0]:
        retrieved_chunks.append({"content": chunks[idx]["content"],"source": chunks[idx]["source"]})

    return retrieved_chunks

def build_prompt(query,context,history_text=""):
    prompt = f"""
                You are a customer support assistant.

                Answer ONLY using the provided context.

                If the answer is not found, say:
                "I could not find that information in the documents."

                Conversation History:

                {history_text}

                Context:

                {context}

                Question:

                {query}
            """

    return prompt

def ask_rag(question,history=None):
    history = history or []
    retrieved_docs = retrieve_context(question)
    context = "\n\n".join(doc["content"] for doc in retrieved_docs)
    history_text = "\n".join([f"{item['role']}: {item['content']}" for item in history[-6:]])
    prompt = build_prompt(query=question,context=context,history_text=history_text)
    answer = generate_response(prompt)
    sources = list(set(doc["source"] for doc in retrieved_docs))

    return {"answer": answer,"sources": sources}

if __name__ == "__main__":
    while True:
        question = input("\nAsk Question: ")
        result = ask_rag(question=question)
        print("\nAnswer:\n")
        print(result["answer"])
        print("\nSources:")
        for source in result["sources"]:
            print(f"- {source}")