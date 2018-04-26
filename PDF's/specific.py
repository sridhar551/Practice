import PyPDF2

pdf1File = PyPDF2.PdfFileReader(open('/media/sree/E87E40977E406084/python3handson.pdf', 'rb'))
pdf2File = PyPDF2.PdfFileReader(open('/media/sree/E87E40977E406084/javascript_tutorial.pdf', 'rb'))

#pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
#pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

pdfWriter.addBlankPage(612,792)

for x,y in zip(pdf1File.pages, pdf2File.pages):
    pdfWriter.addPage(x)
    pdfWriter.addPage(y)

while pdfWriter.getNumPages() % 3:
    pdfWriter.addBlankPage()

with open('/media/sree/E87E40977E406084/all.pdf', 'wb') as f:
    pdfWriter.write(f)