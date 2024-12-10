import psycopg2
from pprint import pprint

connection = psycopg2.connect(
    host="localhost",
    database="gostack_gobarber",
    user="postgres",
    password="docker",
)

cursor = connection.cursor()

sel = cursor.execute("SELECT * FROM users")
print(sel)

sel_fetchall = cursor.fetchall()
for registro in sel_fetchall:
    pprint(registro)