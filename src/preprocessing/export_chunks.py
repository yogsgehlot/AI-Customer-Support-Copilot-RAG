import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
all_chunks = []
raw_folder = Path("data/raw")
chunk_id = 0
for pdf in raw_folder.glob("*.pdf"):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    chunks = splitter.split_text(text)

    for chunk in chunks:
        all_chunks.append({"chunk_id": chunk_id,"source": pdf.name,"content": chunk})
        chunk_id += 1

output_folder = Path("data/processed")
output_folder.mkdir(exist_ok=True,parents=True)

with open(output_folder / "chunks.json","w",encoding="utf-8") as file:
    json.dump(all_chunks,file,indent=4,ensure_ascii=False)

print(f"Saved {len(all_chunks)} chunks")