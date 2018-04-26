import PyPDF2

pdfFile = open('/home/sree/Documents/Invoice10.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('1234')
resultPdf = open('/home/sree/Documents/encrypted.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
pdfFile.close()