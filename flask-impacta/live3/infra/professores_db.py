"""
Cria e inicia o banco
"""

# Importar o sqlite3
import sqlite3

# String de criação da tabela
db_name = './professores.db'
table_name = 'professor'
sql_create_table = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY, nome text NOT NULL)'

# método cretae table
def create_table(cursor, sql):
    cursor.execute(sql)


# método popoular db
def popular_db(cursor, id, nome):
    sql = f'INSERT INTO {table_name} (id, nome) VALUES (?, ?)'
    cursor.execute(sql, (id, nome))


# método de inicialização do banco
def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    create_table(cursor, sql_create_table)
    # try:
    #     popular_db(cursor, 1, 'Amauri Rossetti')
    #     popular_db(cursor, 2, 'Rossetti Giovani')
    # except Exception:
    #     pass
    cursor.close()
    connection.commit()
    connection.close()
