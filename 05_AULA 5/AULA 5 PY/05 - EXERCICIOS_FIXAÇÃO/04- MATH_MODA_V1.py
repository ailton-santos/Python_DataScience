#import numpy as np
#import random as rd
#lista_ale =[10]



lista_de_dados = [  7,21,34,15,23,46,23,54,49,49,75,15,83,41,25,
                    5,43,75,55,581,85,85,45,58,7,85,452,28,45,48,
                    7,82,58,2,5,2,7,8,6,5,75,5,24,24,2,45,752,5,8,
                    752,8,2,57,45,56,5,3,52,4,2,4,52,557,52,7,52,
                    7,52,7,2,7532,2,5,27,25,7,2,7,57,52,87,53,6,7 ]

#encontrar a amostragem com a repetição
def encontrar (lista):
    amostra = []

    for a in lista:
        if(a not in amostra):
            amostra.append(a)

    return amostra
def contarnumerodevezes(lista):
    lista_com_contagem = []

    for i in lista:
        lista_com_contagem.append(0)

    count = 0

    for o in lista:
        for i in lista_de_dados:
            if(o == i):
                lista_com_contagem[count] +=1
        count += 1

    return lista_com_contagem

def encontar_moda(lista1, lista2):

    valorinicial = lista2[0]
    indicemoda = 0
    count = 0

    for o in lista2:
        if(valorinicial <= o):
            valorinicial = o
        count += 1

    return lista1[indicemoda]


lista_amostra = encontrar (lista_de_dados)

print(f" lista de amostra -> {lista_de_dados}")

lista_com_contagem = contarnumerodevezes(lista_de_dados)

print(f" lista de contagem -> {lista_com_contagem}")

moda = encontar_moda(lista_amostra, lista_com_contagem)
print(f" A moda é -> {moda}")
