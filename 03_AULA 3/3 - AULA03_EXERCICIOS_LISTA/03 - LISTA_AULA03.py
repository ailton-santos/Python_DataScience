#3. Classe Quadrado: Crie uma classe que modele um quadrado:
#• Atributos: Tamanho do lado
#• Métodos: Mudar o valor do Lado, Retornar valor do Lado e calcular Área

#criação do objeto
class Quadrado:
    def __init__(self, lado):
        self.__lado = lado

#função de retorno de cadastro e calculo
    def mostrar_area(self):
        print(f"O valor do lado é : {self.__lado}")
        area = float(self.__lado ** 2)
        print(f"A area desse quadrado é: {area}")

#função de modificação de objeto para um novo calculo
    def Mudar_lado (self, novolado):
        self.__lado = novolado
        print(f"O valor do novo lado é {self.__lado}")
        area = float(self.__lado ** 2)
        print(f"A area desse quadrado é: {area}")

lado1 = float(input("digite o valor do lado do seu quadrado : "))
quadrado = Quadrado(lado1)

quadrado.mostrar_area()

lado2 = float(input("digite o valor do novo lado do seu quadrado : "))
quadrado.Mudar_lado(lado2)
        
        