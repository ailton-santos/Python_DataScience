#2. Classe Bola: Crie uma classe que modele uma bola:
#• Atributos: Cor, circunferência, material
#• Métodos: trocaCor e mostraCor

#criação do objeto
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__matrial = material

    def trocarcor(self,novacor):
       # novacor = str(input("digite a nova cor:"))
     
       self.__cor = novacor  

    
    def mostrarcor(self):
        print(self.__cor)

#cadastro
bola = Bola("branca", 45, "borracha nitrilica")

#executa as funções de modificação
bola.mostrarcor()
bola.trocarcor("azul")
bola.mostrarcor()


