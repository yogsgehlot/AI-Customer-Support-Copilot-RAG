import json
import faiss
import numpy as np
from src.embeddings.embedder import generate_embeddings
index = faiss.read_index("vector_db/faiss_index.bin")

with open("data/processed/chunks.json","r",encoding="utf-8") as file:
    chunks = json.load(file)

def search(query, top_k=3):
    query_embedding = generate_embeddings([query])
    distances, indices = index.search(np.array(query_embedding),top_k)
    results = []
    for idx in indices[0]:
        results.append(chunks[idx])
    return results

if __name__ == "__main__":
    query = input("Ask a question: ")
    results = search(query)
    for item in results:
        print("\n" + "=" * 80)
        print(item["source"])
        print(item["content"][:500])