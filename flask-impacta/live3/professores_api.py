"""
Onde estão as rotas relativas a API dos professores (CRUD)
"""

# Importação de módulos
from flask import Blueprint, jsonify, request


# Criar blueprint
professores_app = Blueprint('professores_app', __name__)


# rota para listar
@professores_app.route('/professores', methods=['GET'])
def listar():
    return jsonify([{'id': 1, 'nome': 'Amauri'}, {'id': 2, 'nome': 'Rossetti'}])


# rota para ler



# rota para criar



# rota para deletar



# rota para atualizar


