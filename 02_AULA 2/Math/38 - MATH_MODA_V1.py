lista_de_dados = [35, 37, 36, 34, 38, 35, 37, 37, 33, 36, 38, 37,35, 37, 34, 33, 37, 36, 35, 38, 36, 35, 36, 37, 38, 39, 37, 37, 36, 37, 33, 37, 35, 37, 39]

def EncontrarAmostragem(lista):
    amostragem = []

    for a in lista:
        if(a not in amostragem):
            amostragem.append(a)
            
    return amostragem

def ContarNumeroDeVezesQueAparece(lista):
    lista_com_contagem = []

    for n in lista:
        lista_com_contagem.append(0)

    count = 0

    for o in lista:

        for n in lista_de_dados:
            if (o == n):
                lista_com_contagem[count] += 1 
    
        count += 1

    return lista_com_contagem
       
def EncontrarModa(lista1,lista2):

    initialValue = lista2[0]
    indiceModa = 0
    cont = 0

    for o in lista2:

        if(initialValue <= o):
            initialValue = o
            indiceModa = cont
        
        cont += 1
        

    return lista1[indiceModa]


lista_de_amostras = EncontrarAmostragem(lista_de_dados)

print(lista_de_amostras)

lista_com_contagens = ContarNumeroDeVezesQueAparece(lista_de_amostras)

print(lista_com_contagens)

moda = EncontrarModa(lista_de_amostras,lista_com_contagens)

print(moda)
