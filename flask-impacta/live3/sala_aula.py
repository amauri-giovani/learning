"""
Arquivo ponto de entrada onde tem:
a rota principal que leva para o index.html
carrega e inicializa o banco de dados
carrega os blueprints das outras rotas que são APIs
"""

# Importação de módulos
import requests
from flask import Flask, jsonify, render_template, request
from professores_api import professores_app
import infra.professores_db as prof_db

# Criar apps e registrar blueprints
app = Flask(__name__)
app.register_blueprint(professores_app)

# Criar rota principal
app.route('/')
def index():
    professores = requests.get('http://localhost:5000/professores').json()
    return render_template('index.html', professores=professores)


# Iniciar banco de dados
prof_db.init()


# Rodar servidor
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
