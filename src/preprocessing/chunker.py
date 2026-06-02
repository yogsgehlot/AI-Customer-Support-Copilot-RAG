from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,separators=["\n\n","\n",". "," ",""])
    chunks = splitter.split_text(text)
    return chunks

if __name__ == "__main__":
    text = load_text("data/processed/all_documents.txt")
    chunks = chunk_text(text)
    print(f"Total Chunks: {len(chunks)}")
    print("\nFIRST CHUNK\n")
    print(chunks[0])