import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#Lista com os dados dos novos usuarios
lista = [
    ('Pablo','pablo@gmail.com','123','01/01/2022'),
    ('Pablo1','pablo1@gmail.com','1234','02/01/2022'),
    ('Pablo2','pablo2@gmail.com','1235','03/01/2022'),
    ('Pablo3','pablo3@gmail.com','1236','04/01/2022'),

]

#INSERT comando para add novos valores na nossa coluna
c.executemany(""" INSERT INTO usuarios(nome,email,senha,data_nacimento) 
            VALUES(?,?,?,?) 
""",lista)


# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")