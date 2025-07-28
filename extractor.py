import fitz
import re
def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        headings = re.findall(r'(?m)^(?:Chapter|Section|[A-Z][^\n]{1,100})$', text)
        chunks = text.split('\n\n')
        for chunk in chunks:
            sections.append({
                "page": i+1,
                "text": chunk.strip()[:1000],
                "section_title": chunk.strip().split('\n')[0][:50]
            })
    return sections
