from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(text, source):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks = splitter.split_text(text)
    results = []
    for index, chunk in enumerate(chunks):
        results.append({"chunk_id": index,"source": source,"content": chunk})

    return results