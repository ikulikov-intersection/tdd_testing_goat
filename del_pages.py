from PyPDF2 import PdfFileWriter, PdfFileReader

startd = 0
stopd = input("delete to:")


list_to_delete=[]

for a in range(int(startd), int(stopd)):
    list_to_delete.append(a)
infile = PdfFileReader("TDD_withPython.pdf", "rb")
output = PdfFileWriter()
for i in range(infile.getNumPages()):
    if i not in list_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open("TDD_withPython.pdf", "wb") as f:
    output.write(f)

    


    
