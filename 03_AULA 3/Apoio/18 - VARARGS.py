#array = vetor, grupo de informações 
#*args = varios argumentos que não preciso declarar na função


def soma(*args):
    resultado = 0

    for x in args:
        resultado += x
        # resultado = resultado + x

    print(resultado)

soma(1,5,1,5,9,14,6,4,5,1,5,4,5,1,5,47,85,1,5,4,8,4,2,1,8,47,5,1,5,4,8,1)
soma(5,5)