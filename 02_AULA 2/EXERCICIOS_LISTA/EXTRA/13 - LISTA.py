"""13. Faça uma função que receba uma temperatura em graus Fahrenheit, calcule e escreva o valor correspondente em graus Celsius através da fórmula:
conversão de grau fahrenheit para grau celsius °C = °F - 32 / 1.8"""

def temperatura(fahr):

    temp = float(( fahr - 32) / 1.8)

    print(f"A temperatura em Fahrenheit é igua : {fahr} °F")
    print(f"A temperatura em celsius é igua : {temp} °C")



A = float(input("digite a temperatura em Fahrenheit: "))


temperatura(A)