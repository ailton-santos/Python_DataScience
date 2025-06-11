import sqlite3
from sys import displayhook
from tkinter.tix import DisplayStyle

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#Executar select para mostrar os cadastros
c.execute(""" SELECT * FROM usuarios """)

for linha in c.fetchall():
    print(linha)

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")

#fecho a conexão com o db
conn.close()
print("Conexão encerrada")