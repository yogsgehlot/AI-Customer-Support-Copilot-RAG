from pathlib import Path
from pypdf import PdfReader

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def build_corpus():
    raw_folder = Path("data/raw")
    corpus = ""
    for pdf in raw_folder.glob("*.pdf"):
        print(f"Processing {pdf.name}")
        text = extract_text(pdf)
        corpus += "\n\n"
        corpus += "=" * 100
        corpus += "\n"
        corpus += pdf.name
        corpus += "\n"
        corpus += "=" * 100
        corpus += "\n\n"
        corpus += text

    output = Path("data/processed")
    output.mkdir(parents=True,exist_ok=True)
    with open(output / "all_documents.txt","w",encoding="utf-8") as file:
        file.write(corpus)

    print("\nCorpus created successfully")


if __name__ == "__main__":
    build_corpus()