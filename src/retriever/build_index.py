import json
from pathlib import Path
import faiss
import numpy as np
from src.embeddings.embedder import generate_embeddings


with open("data/processed/chunks.json","r",encoding="utf-8") as file:
    chunks = json.load(file)

texts = [chunk["content"] for chunk in chunks]
embeddings = generate_embeddings(texts)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

Path("vector_db").mkdir(exist_ok=True)
faiss.write_index(index,"vector_db/faiss_index.bin")

print(f"Stored {index.ntotal} vectors")