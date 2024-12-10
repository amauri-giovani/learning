#!/usr/bin/env python_dir
# -*- coding: utf-8 -*-
#Cria um arquivo unindo o conteúdo de dois outros arquivos.

import PyPDF2, binascii		#importa o módulo PyPDF2.

pdfFile = open('/home/amauri/Downloads/boleto-recovery.pdf', 'rb')				#abre o arquivo do tipo binário em modo leitura.
pdfReader = PyPDF2.PdfFileReader(pdfFile)				#obtém o objeto PdfFileReader para leitura em pdfReader para representar esse PDF.
pdfWriter = PyPDF2.PdfFileWriter()						#obtém o objeto PdfFileWriter em pdfWriter para escrever posteriormente.
print(pdfReader.numPages)									#calcula o número de páginas do arquivo.
pageObj = pdfReader.getPage(1)						#obtém um objeto Page para representar uma página, no caso, 0 corresponde à 1ª página.
pdfWriter.addPage(pageObj)							#adiciona a página no objeto pdfWriter.
#print(pageObj.extractText())						#extrai o texto da página expecificada. 
pdfOutputFile = open('Certidão de Casamento.pdf', 'wb')		#cria um arquivo do tipo binário em modo escrita.
pdfWriter.write(pdfOutputFile)							#escreve o conteúdo de pdfWriter no arquivo.

pdfOutputFile.close()									#fecha o arquivo
pdfFile.close()										#fecha o arquivo


