# variaveis locais so podem ser acessadas dentro da função ou seja não consigo usar essa variavel por outra função

def escrevefrase():
    nome = "jose"
    print(f"{nome} esta na aula!")

def escreveinf():
    nome = "maria"
    print(f"{nome} esta na aula de python")

escrevefrase()
escreveinf()
