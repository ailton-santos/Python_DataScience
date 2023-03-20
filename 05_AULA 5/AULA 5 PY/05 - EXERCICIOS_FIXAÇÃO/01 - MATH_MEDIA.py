


lista_de_dados = [23,6565,52,58655,25555,559556,56454,51145]

#função retorna o valor da media
def media(lista):
    total_soma = 0
    n_dados = 0
#somatoria e conta numero de dados
    for i in lista:
        total_soma += i
        n_dados += 1
        print(i)
#Retorna a somatoria e divide pelo numero de dados
    return total_soma/n_dados


print(media(lista_de_dados))



