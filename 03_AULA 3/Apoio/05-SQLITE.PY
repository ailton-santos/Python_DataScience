import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

# criação da estrutura do db
c.execute(""" CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    email VARCHAR(100),
    senha VARCHAR(50)
    

) """)

#msg para verificar a criação da tabela
print("tabela de usuarios criada com sucesso")

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")


