import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#ALTER comando para add nova coluna
c.execute(""" ALTER TABLE usuarios ADD data_nacimento VARCHAR(10) """)

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")