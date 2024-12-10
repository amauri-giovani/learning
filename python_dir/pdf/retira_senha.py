#! python3
# Se o arquivo PDF possuir uma senha, a informa para acessá-lo.

import PyPDF2


pasta = '/home/amauri/Downloads'
arquivo = 'Proposta de Contratacao Protecao Residencial.pdf'
senha = '1174'

pdfReader = PyPDF2.PdfFileReader(open('/'.join([pasta, arquivo]), 'rb'))
pdfReader.decrypt(senha)
pdfWriter = PyPDF2.PdfFileWriter()

for pagenum in range(pdfReader.numPages):
    pageobj = pdfReader.getPage(pagenum)
    pdfWriter.addPage(pageobj)

nome_arquivo = input("Digite um nome para criar o arquivo PDF: ")
if not nome_arquivo.endswith('.pdf'):
    nome_arquivo += '.pdf'
with open(nome_arquivo, 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
