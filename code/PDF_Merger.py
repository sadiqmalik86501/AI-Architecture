from PyPDF2 import PdfWriter

merger=PdfWriter()

pdf1=[]

n=int(input("How Many Pdf Do You Want to merger"))

for i in range(0,n):
    name=input(f"Enter The Pdf Name of pdf {i+1}:")
    pdf1.append(name)

for pdf in pdf1:
    merger.append(pdf)

merger.write("Merger_pdf.pdf")
merger.close()

print("Pdf Merged Successfully:")