"""
Classes que vão mexer na tabela Professor
Faz o model professor.db acessar o banco
"""

#  Importar sqlite, modelo e contextlib
import sqlite3
from model.professor import Professor

# Já abre e fecha a conexão automaticamente
from contextlib import closing

# variáveis gerais
db_name = './professores.db'
model_name = 'professor'

# conexão
def con():
    """Para economizar escrita na chamada de connect"""
    return sqlite3.connect(db_name)

# método listar() -> list(Professor)
def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM {model_name}')
        rows = cursor.fetchall()
        registros = []
        for id, nome in rows:
            registros.append(Professor.criar({'id': id, 'nome': nome}))
        return registros


# método consultar(id) -> professor
def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM {model_name} WHERE id = ?', (int(id),))
        row = cursor.fetchone()
        if row is None:
            return None
        return Professor.criar({'id': row[0], 'nome': row[1]})


# método cadastrar(Professor) -> dict or None
def cadastrar(professor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f'INSERT INTO {model_name} (id, nome) VALUES (?, ?)'
        result = cursor.execute(sql, (professor.id, professor.nome))
        connection.commit()
        if cursor.lastrowid:
            return professor.__dict__()
        else:
            return None

# método alterar(Professor) -> None
def alterar(professor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f'UPDATE {model_name} SET nome = ? WHERE id = ?'
        cursor.execute(sql, (professor.nome, professor.id))
        connection.commit()


# método remover(Professor) -> NOne
def remover(professor):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f'DELETE FROM {model_name} WHERE id = ?'
        cursor.execute(sql, F'{professor.id}')
        connection.commit()


