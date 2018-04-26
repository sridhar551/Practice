import PyPDF2, os

pdfFiles = []

for filename in os.listdir('/media/sree/E87E40977E406084/Downloads'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.upper)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


    for pageNum in range(1,pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
pdfOutput = open('allpages.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()