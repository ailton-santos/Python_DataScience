#criação da estrutura 
class animal():
    def __init__(self, nome, cor, comida):
        self.__nome = nome
        self.__cor = cor
        self.__comida = comida
#função para expor o cadastro    
    def comer(self):
        print(f" O {self.__nome} , tem a cor {self.__cor},se alimenta de {self.__comida}")

    #def carac(self):
      # print(f" O {self.__nome} tem a cor {self.__cor} ") 

    #def alimento(self):
     #   print(f"O {self.__nome} se alimenta de {self.__comida}")
#criação dos animais
class Gato(animal):
    def __init__(self, nome, cor, comida):
        super().__init__(nome, cor, comida)
class Cachorro(animal):
    def __init__(self, nome, cor, comida):
        super().__init__(nome, cor, comida)
class Papagaio(animal):
    def __init__(self, nome, cor, comida):
        super().__init__(nome, cor, comida)
class Cavalo(animal):
    def __init__(self, nome, cor, comida):
        super().__init__(nome, cor, comida)
class Lontra(animal):
    def __init__(self, nome, cor, comida):
        super().__init__(nome, cor, comida)


#cadastro das caracteristicas
gato = Gato("goku", "branco", "rato")
cachorro = Cachorro("Sirius black", "preto", "osso")
papagaio = Papagaio("Loro","verde", "girasol") 
cavalo = Cavalo("Pé de pano", "branco", "capim")
lontra = Lontra("LULA","marrom","peixe")

#chamei o feedback para o usuario
gato.comer()
cachorro.comer()
papagaio.comer()
cavalo.comer()
lontra.comer()










