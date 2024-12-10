import psycopg2

connection = psycopg2.connect(host='localhost', port=5432, user='postgres', password='postgres')
cursor = connection.cursor()


def compara(item):
    for column_type in ["char", "varchar", "text", "bool", "smallint", "int", "bigint", "numeric", "real"]:
        str_sql = f"SELECT pg_column_size({item}::{column_type});"
        if isinstance(item, str):
            str_sql = str_sql.replace(f"{item}", f"'{item}'")
        try:
            cursor.execute(str_sql)
            dados = cursor.fetchone()[0]
            # print(str_sql)
            print(f"{column_type} = {dados}")
            # print()
        except Exception as error:
            connection.rollback()
            print(f"{column_type} não permitido")


compara(192789)
connection.close()
