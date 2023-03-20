# CREATE
""" CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    email VARCHAR(100),
    senha VARCHAR(50)
    
) """

#ALTER

""" ALTER TABLE usuarios ADD data_nacimento VARCHAR(10) """

#INSERT
""" INSERT INTO usuarios(nome,email,senha,data_nacimento) VALUES("joão", "joao@gmail.com", "123456", "21/05/2000") """

#SELECT

""" SELECT * FROM  usuarios """


#UPDATE

""" UPDATE usuarios SET senha = " 12345678"  WHERE nome="joão" """

#DELETE

"""DELETE FROM usuarios WHERE nome="joão" """

#PESQUISA DE USUARIOS FILTRO DE NOME E EMAIL

"""SELECT * FROM usuarios WHERE nome="Ana" AND email="aninha@gmail.com" """

#ORDENAR

""" SELECT * FROM usuarios ORDER BY nome DESC """


