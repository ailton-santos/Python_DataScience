"""
> 5.Classe Pessoa:Crie uma classe que modele uma pessoa:
• Atributos: nome, idade, peso e altura
•Métodos:Envelhecer,engordar,emagrecer,crescer.
Obs:Porpadrão,acadaanoquenossapessoaenvelhece,sendoaidadedelamaior
que21anos,eladevecrescer0,5cm.
"""




class pessoa():
    def __init__ (self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def lista (self):
        print(f" O(a) {self.nome} , tem  {self.idade} anos,seu peso {self.peso}, sua altura é {self.altura} em metros")       
    
    def paciente():
        nome = input("Digite seu primeiro nome: ")
        idade = input("Digite sua idade: ")
        peso = input("Digite seu peso em kg: ")
        altura = input("Digite sua altura em metros: ")
        humano = cadastro(nome,idade,peso,altura)
        humano.lista()
    def envelhecer():
        idade = input("Digite sua idade do envelhecimento: ")
        humano = cadastro(idade)
        

class cadastro(pessoa):
    def __init__(self,nome,idade,peso,altura):
        super().__init__(nome,idade,peso,altura)
        
i = 'S'

while i == 'S':
    print("Bem vindo ao cadastro de paciente!!!")
    
    i = str(input("Para iniciar o cadstro digite: S=sim / N=não     ")).upper()
    if i =='S':
        pessoa.paciente()
        menu=str( input("Escolha dentre as seguintes opções: 1=envelhecer/2=engordar/3=emagrecer/4=crescer "))
        if menu==1:
            pessoa.envelhecer()

    
    
    else:
        break

