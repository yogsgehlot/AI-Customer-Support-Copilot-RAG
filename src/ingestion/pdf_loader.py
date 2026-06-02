from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


if __name__ == "__main__":
    pdf_folder = Path("data/raw")
    for pdf_file in pdf_folder.glob("*.pdf"):
        print(f"\nReading {pdf_file.name}")
        text = extract_text_from_pdf(pdf_file)
        print(text[:1000])