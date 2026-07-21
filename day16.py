from pypdf import PdfWriter

pdfs = [
    "Commonly Used Short Keys(Word).pdf",
    "Ch 3.pdf",
    "Ch2.pdf"

]

merged = PdfWriter()

for pdf in pdfs:
    merged.append(pdf)

merged.write("final.pdf")
merged.close()

print("All files converted into pdf")
