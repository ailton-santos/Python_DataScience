import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#Carregar as informações do usuario
id_usuario = "1"

#execute o cadastro no db
c.execute("""DELETE FROM usuarios WHERE id = ? """, (id_usuario))

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")