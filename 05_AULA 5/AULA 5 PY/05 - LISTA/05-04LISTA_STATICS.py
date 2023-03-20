"""
4. Crie um programa que receber a lista de valores abaixo, e mostre em tela
a VARIANCIA.

lista_de_valores = [35, 37, 36, 34, 38, 35, 37, 37, 33, 36,
38, 37,35, 37, 34, 33, 37, 36, 35, 38, 36, 35, 36, 37, 38,
39, 37, 37, 36, 37, 33, 37, 35, 37, 39]

"""

import statistics as stts

lista = [35, 37, 36, 34, 38, 35, 37, 37, 33, 36,
38, 37,35, 37, 34, 33, 37, 36, 35, 38, 36, 35, 36, 37, 38,
39, 37, 37, 36, 37, 33, 37, 35, 37, 39]

variancia = stts.pvariance(lista)

print(f"Variencia do role é :{variancia}")

