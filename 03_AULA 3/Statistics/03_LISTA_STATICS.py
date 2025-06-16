"""
3.Crie um programa que irá receber a lista 
de valores abaixo, e mostre em tela a MODA
e quantas vezes ele aparece nessa lista.

lista_de_valores =[
    1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6,
     7,1, 7, 8, 0, 7, 3, 1, 6, 3, 1,
      3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 
      1, 7, 9]

"""

print("MODO 1")
import statistics as sttc
lista_de_dados =[
    1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6,
     7,1, 7, 8, 0, 7, 3, 1, 6, 3, 1,
      3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 
      1, 7, 9]


moda = sttc.mode(lista_de_dados)

print(f"A moda dessa pegua é : {moda}")

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

lista_com_contagem = contarnumerodevezes(lista_de_dados)

print(f" lista de contagem -> {lista_com_contagem}")
print('#'*100)
        
print("MODO 2")

lista =[
    1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6,
     7,1, 7, 8, 0, 7, 3, 1, 6, 3, 1,
      3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 
      1, 7, 9]

moda = sttc.mode(lista)
cont = 0
print(f"A moda dessa pegua é : {moda}")

for i in lista:
    if i == 7:
        cont+=1
print(f"A quantidade da repetição da moda foi: {cont}")

print('#'*100)
        
print("MODO 3")

dados =[
    1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6,
     7,1, 7, 8, 0, 7, 3, 1, 6, 3, 1,
      3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 
      1, 7, 9]

moda = sttc.mode(dados)
print(f"A moda dessa pegua é : {moda}")

contagem = dados.count(7)

print(f"A quantidade da repetição da moda foi: {contagem}")

