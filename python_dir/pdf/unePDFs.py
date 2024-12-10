# Necessário instalar o PyPDF2
# pip install PyPDF2

# Esse script gera um novo arquivo unindo o conteúdo de
# cada arquivo PDF contido nessa pasta por ordem alfabética

# OS ARQUIVOS EXISTENTES DESSA PASTA NÃO SERÃO ALTERADOS OU EXCLUÍDOS

"""
Como usar:
Coloque todos os arquivos PDF e também esse script em uma pasta separada
Execute esse script. Será solicitado um nome para o arquivo PDF a ser criado
"""

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

pdfWriter = PdfFileWriter()
filename = 'arquivo.pdf'
pdfFileObj = PdfFileReader(open(filename, 'rb'))
# pdfFileObj.isEncrypted
pdfFileObj.decrypt('senha')
pdfReader = PdfFileReader(pdfFileObj)
for pagenum in range(pdfReader.numPages):
    pageobj = pdfReader.getPage(pagenum)
    pdfWriter.addPage(pageobj)

nome_arquivo = input("Digite um nome para criar o arquivo PDF: ")
if not nome_arquivo.endswith('.pdf'):
    nome_arquivo += '.pdf'
with open(nome_arquivo, 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
