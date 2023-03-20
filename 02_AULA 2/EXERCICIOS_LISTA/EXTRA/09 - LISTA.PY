"""Faça uma função que receba por parâmetros os coeficientes 
de uma equação do 2º grau, sendo: a, b e c. Calcule e retorne o 
valor de seu discriminante (delta), através da fórmula:
Δ=b²-4*a*c."""

def raiz(a,b,c):
    print("Δ=b²-4*a*c")
    delta = ((b**2)-(4*a*c))
    delta = abs(delta)
    print(delta)
    
    
a = float(input("digite o valor do termo a:"))
b = float(input("digite o valor do termo b:"))
c = float(input("digite o valor do termo c:"))

raiz(a,b,c)


