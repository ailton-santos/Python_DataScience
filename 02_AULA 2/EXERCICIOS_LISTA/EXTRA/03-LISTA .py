from this import d

#3. Faça uma função que receba a idade de uma pessoa em anos,
#meses e dias e retorna essa idade expressa em dias.
ano1=365
mes1=30
def Iddias():

    anos=int(input("digite quantos anos vc tem:"))
    mes=int(input("digite quantos meses vc tem:"))
    dias=int(input("digite quantos dias vc tem:"))

    anos=anos*ano1
    mes=mes*mes1

    soma=anos+mes+dias

    print(f"Sua idade em dias é igual a : {soma}")

Iddias()