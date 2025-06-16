"""
5. Crie um programa que receber a lista de valores abaixo, e mostre em tela
a VARIANCIA e o DESVIO PADRÃO.

lista_de_valores = [1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6, 7,1, 7,
8, 0, 7, 3, 1, 6, 3, 1, 3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 1, 7,
9]

"""


import statistics as stts

lista = [1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6, 7,1, 7,
8, 0, 7, 3, 1, 6, 3, 1, 3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 1, 7,
9]

variancia = stts.pvariance(lista)
dp = stts.pstdev(lista)

print(f"O desvio padrao da lista é : {dp}")

print(f"Variencia do role é :{variancia}")



