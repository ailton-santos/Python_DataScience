import sqlite3

#conectar ao banco db
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys comandos
c = conn.cursor()

#Carregar as informações do usuario
p_nome = input("Nome :")
p_email = input("Email :")
p_senha= input("senha :")
p_data_de_nacimento= input("Data de nascimento :")


#execute o cadastro no db
c.execute(""" INSERT INTO usuarios(nome,email,senha,data_nacimento) 
        VALUES(?,?,?,?)""", (p_nome,p_email,p_senha,p_data_de_nacimento))

# grava as informações no db
conn.commit()
print("Informações gravadas com sucesso no db")


#fecho a conexão com o db
conn.close()
print("Conexão encerrada")