import requests
from core.celery import app
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from celery_basic.models import Arquivo
from core.utils import create_file


@csrf_exempt
def upload_file(request):
    if request.FILES:
        create_file(
            nome=request.POST['nome'],
            arquivo=request.FILES['arquivo_upload']
        )
    return HttpResponse()
    # return HttpResponseRedirect("/")

'''
def test_cria_arquivo():
     with open("file-amauri.csv") as file_upload:
         resp = requests.post(
             "http://localhost:8000/upload/",
             files={"arquivo_upload": file_upload},
             data={"nome": "file-amauri.csv"})
     return resp
'''
