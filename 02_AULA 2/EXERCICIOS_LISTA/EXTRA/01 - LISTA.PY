#Referencia https://www.w3schools.com/python/module_math.asp

#1. Faça uma função que receba por parâmetro o raio de uma 
# esfera. Calcule e retorne sua área através da fórmula:
# A = 4*π* raio²
from cmath import pi
import math


def Area(raio,diametro):
    
    print(4*pi*raio**2)
    print(pi*diametro**2)


r = float(input("digite o valor do raio em mm:"))
D = int(input("digite o valor do diametro em mm:"))
Area(r,D)