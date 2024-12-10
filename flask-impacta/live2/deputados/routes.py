import json
import requests
from flask import render_template, Blueprint

bp_deputados = Blueprint('deputados', __name__, url_prefix="/deputados", template_folder='templates')

@bp_deputados.route('/')
def index():
    url = "https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=56&ordem=ASC&ordenarPor=nome"
    header = {"accept": "application/json"}
    response = requests.get(url, headers=header)
    dados = json.loads(response.content)['dados']
    return render_template('index.html', deputados=dados)
