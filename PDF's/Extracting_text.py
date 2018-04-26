import PyPDF2

pdfFileObj = open('/home/sree/Documents/Invoice1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)
print(pageObj.extractText())