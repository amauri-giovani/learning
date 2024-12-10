# -*- coding: utf-8 -*-

import PyPDF2, os


pdfFiles = []

dirname = "/home/amauri/Downloads/"
name = "Matrícula"
filepath = "".join([dirname, name])
os.chdir(filepath)

for filename in os.listdir("."):
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

pdfOutput = open(f"{name}.pdf", 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

