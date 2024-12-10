from datetime import datetime
from random import randint

from django.shortcuts import render, redirect
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import barcode
import csv


def index(request):
    return HttpResponse('Controle de estoque')


def generate_pdf(request):
    '''
    TODO Criar essa função recebendo os parâmetros para a criação do PDF
    '''
    # nome_pdf = 'teste.pdf'
    # lista = {'Rafaela': '19', 'Jose': '15', 'Maria': '22', 'Eduardo': '24'}
    nome_pdf = f"Pedido#{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    lista = []
    with open('meu_arquivo.csv') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=',')
        for coluna in leitor:
            lista.append(coluna)
    buffer = io.BytesIO()
    try:
        pdf = canvas.Canvas(buffer)
        y = 720
        for item in lista:
            for key, value in item.items():
                y -= 20
                pdf.setFont("Helvetica", 14)
                pdf.drawString(247, y, f'{key} : {value}')
            pdf.setTitle(nome_pdf)
            pdf.setFont("Helvetica-Oblique", 14)
            pdf.drawString(245, 750, 'Solicitação de compra para os itens abaixo')
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(245, 724, 'Lista de Itens')
        pdf.save()
        buffer.seek(0)
    # print('{}.pdf criado com sucesso!'.format(nome_pdf))
        return FileResponse(buffer, as_attachment=True, filename=nome_pdf)
    except:
        return HttpResponse(f'Erro ao gerar {nome_pdf}')
    # return HttpResponse(content_type='application/pdf')


def generate_barcode(request):
    '''
    TODO Criar essa função recebendo o número após ser checado no DB se o mesmo não existe
    Se não encontrar esse code_id no DB atribui o code_id ao produto
    Exemplo:
    obj = get_object_or_404(MyModel, pk=code_id)
    Se já existir gera outro code_id
    '''
    code_id = str(randint(100000000000, 999999999999))
    ean = barcode.get('ean13', code_id)
    ean.save(code_id)
    # return HttpResponse('Código de barras criado com sucesso!')
    return redirect('index')
