#classe de criação de objetos nesse caso eu crio uma fruta com suas caracteristicas
class fruta:
#defino as caracteristicas iniciais da fruta
    def __init__(self,tipo,cor):
        self.tipo = tipo
        self.cor = cor
#defino a função para descrever as caracteristicas para o usuario
    def mostrarpropriedades(self):
        print(f"Sou um(a): {self.tipo} e tenho a cor: {self.cor} !")

#crio variaveis para o cadastro 
fruta1 = fruta("tangerina", "laranja")
fruta2 = fruta("abacate", "verde")


#vejo suas caracteristicas dessas frutas
fruta1.mostrarpropriedades()
fruta2.mostrarpropriedades()