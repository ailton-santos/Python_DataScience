

var = 10

def parada():
    for i in range(var):

        print(f"valor de I = {i}")
        if(i == 5):
            break


print("digite a função desejada:")

ent  = str(input("digite p para iniciar a parada:"))

if (ent == "p"):
    parada()
