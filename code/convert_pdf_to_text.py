from PyPDF2 import PdfReader

reader = PdfReader("Merger_pdf.pdf")
with open("output.txt", "w", encoding="utf-8") as f:
    
    for page in reader.pages:
        t = page.extract_text()
        if t:
            f.write(t + '\n\n\n\n')