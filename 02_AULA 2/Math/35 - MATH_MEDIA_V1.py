
list_de_dados = [28,30,29,31,32,33,34]

def media(lista):
    total_das_somatorias = 0
    n_de_dados = 0
    
    for n in lista:
        total_das_somatorias += n
        n_de_dados += 1
    
    return total_das_somatorias/n_de_dados

print(media(list_de_dados))