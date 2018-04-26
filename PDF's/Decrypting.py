import PyPDF2
pdfReader = PyPDF2.PdfFileReader('/home/sree/Downloads/FCLFL1302201803.pdf','rb')
print(pdfReader.isEncrypted)
pdfReader.getPage(0)
pdfReader.decrypt('916010064529089')
pageObj = pdfReader.getPage(0)
print(pageObj)