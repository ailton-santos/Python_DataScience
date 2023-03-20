#2. Faça uma função que receba por parâmetro o raio de uma
#esfera. Calcule e retorne seu volume através da fórmula:
#V = 4/3*π * raio³
#Referencia https://www.w3schools.com/python/module_math.asp

import math
from math import *

def Volume(raio):
    
    print("valor do Volume da esfera pelo raio :")
    print(4/3*math.pi*math.pow(raio, 3))



r = float(input("digite o valor do raio em mm:"))


Volume(r)