"""4. Classe Retangulo: Crie uma classe que modele um retangulo:
• Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e 
Altura, a escolher)
• Métodos: Mudar o valor dos Lados, Retornar valor do Lado, calcular
Área e calcular Perímetro
• Crie um programa que utilize esta classe. Ele deve pedir ao usuário 
que informe as medidades de um local. Depois, deve criar um objeto 
com as medidas e calcular a quantidade de pisos e de rodapés 
necessárias para o local"""
#ctrl+shift+l = muda o nome da mesma variavel em todas as posições
from ast import Return


class Piso:
    def __init__(self, LA , LB):
        
        self.__LA = LA
        self.__LB = LB
    
    
    def Returno(self):
        print(f"O valor do lado A é : {self.__LA}")
        print(f"O valor do lado B é : {self.__LB}")

    def Mudar(self, novoLA, novoLB):
        self.__LA = novoLA
        self.__LB = novoLB

    def Area(self):
        area1 = float(self.__LA * self.__LB)
        print(f"O valor da area calculada é: {area1}")
        
    def Perimetro(self):
        perimetro1 = float(self.__LA * 2 + self.__LB * 2)
        print(f"O valor do perimetro calculado é: {perimetro1}")

def uni():
    unidadespiso = float((LA*LB)/(LC*LD))
    print(f"A quantidade de pisos para usar na obra é: {unidadespiso} uni")


print("informe as informações do local em metros: ")
LA = float(input("Digite o valor do primeiro lado:  "))
LB = float(input("Digite o valor do segundo lado:  ")) 
local = Piso(LA, LB)
print("voce quer mudar algum valor? ")
mud = str(input("resonda S=sim N=não"))
if mud == "S" :
    LE = float(input("Digite o valor do primeiro lado:  "))
    LF = float(input("Digite o valor do segundo lado:  ")) 
    local.Mudar(LE, LF)
    local.Returno()
    local.Area()
    local.Perimetro()

else:

    local.Returno()
    local.Area()
    local.Perimetro()



print("informe as informações da peça de piso para instalação em metros: ")
LC = float(input("Digite o valor do primeiro lado:  "))
LD = float(input("Digite o valor do segundo lado:  ")) 
peças = Piso(LC, LD)
print("voce quer mudar algum valor? ")
mud = str(input("resonda S=sim N=não"))
if mud == "S" :
    LE = float(input("Digite o valor do primeiro lado:  "))
    LF = float(input("Digite o valor do segundo lado:  ")) 
    local.Mudar(LE, LF)
    peças.Returno()
    peças.Area()
    peças.Perimetro()
else:
    peças.Returno()
    peças.Area()
    peças.Perimetro()

uni()

""" print("voce quer mudar algum valor? ")
mud = str(input("resonda S=sim N=não"))

if mud == "S" :
    LE = float(input("Digite o valor do primeiro lado:  "))
    LF = float(input("Digite o valor do segundo lado:  ")) 
    local.Mudar(LE, LF) """

