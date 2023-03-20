import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#Carregar as informações do usuario
id_usuario = 1
p_nome = "astrogildo"
p_email = "astro@gmail.com"
p_senha= "senha"
p_data_de_nacimento= "01/01/0001"


#execute o cadastro no db
c.execute(""" UPDATE usuarios SET nome=?, email=?, senha=?, data_nacimento=? WHERE id=? """,(p_nome,p_email,p_senha,p_data_de_nacimento,id_usuario))

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")