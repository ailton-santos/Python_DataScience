#14. Faça uma função que receba uma temperatura em graus Celsius,
#  calcule e escreva o valor correspondente em graus Fahrenheit através da fórmula:
# °F = °C* 1.8+32

def temperatura(cels):

    temp = float(cels*1.8 +32 )

    print(f"A temperatura em celsius é igua : {cels} °C")
    print(f"A temperatura em Fahrenheit é igua : {temp} °F")



A = float(input("digite a temperatura em Celsius: "))


temperatura(A)