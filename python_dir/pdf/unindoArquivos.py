# -*- coding: utf-8 -*-

import PyPDF2, os


pdfFiles = []

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)
pdfFiles.sort()
pdfWriter = PyPDF2.PdfFileWriter()
print(pdfFiles)

for filename in pdfFiles:
	pdfFileObj = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(0)
	# pageObj = pdfReader.getPage(0).rotateClockwise(270)
	# pageObj.rotateClockwise(270)
	pdfWriter.addPage(pageObj)

pdfOutput = open('Sinpeem - Precatórios.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

