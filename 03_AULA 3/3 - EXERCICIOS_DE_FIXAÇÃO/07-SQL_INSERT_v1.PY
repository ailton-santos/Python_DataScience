import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#INSERT comando para add novos valores na nossa coluna
c.execute(""" INSERT INTO usuarios(nome,email,senha,data_nacimento) 
            VALUES('joão', 'joao@gmail.com', '12345', '20/05/2000') 
""")
c.execute(""" INSERT INTO usuarios(nome,email,senha,data_nacimento) 
            VALUES('maria', 'maria@gmail.com', '123456', '21/05/2000') 
""")
c.execute(""" INSERT INTO usuarios(nome,email,senha,data_nacimento) 
            VALUES('pé de feijão', 'pedefeijao@gmail.com', '1234567', '22/05/2000') 
""")

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")