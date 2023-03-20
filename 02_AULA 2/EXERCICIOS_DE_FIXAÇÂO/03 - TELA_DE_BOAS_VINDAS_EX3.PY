nome = input("Qual é seu nome???")

def escreven(Caractere, quant: int):
    uva = ""
    for n in range (quant) :
        uva+=Caractere

    return uva


print(escreven("=",30))
