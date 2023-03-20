#15. Faça um programa que leia 3 valores representando os lados de um triangulo.
# a) determine se os valores digitados formam ou não um triângulo(Para formar um triângulo, um lado deve ser menor que a soma dos outros dois)
# b) Se for triangulo, classifique em:
# -Três lados iguais -triangulo equilátero
# -Dois lados iguais -triangulo isósceles
# -Três lados diferentes -triangulo escaleno



def triangulo(A, B, C):

    if A == 0 or  B == 0 or C == 0:
        print("Não é um Triangulo")
        
    elif A == B and B == C :

        print("Esse triangulo é classificado como : Três lados iguais Triangulo Equilátero")

    elif A != B and B != C :

        print("Esse triangulo é classificado como : Três lados diferentes Triangulo Escaleno")
    
    else:
        print("Esse triangulo é classificado como : Dois lados iguais Triangulo isósceles")
    

a = float(input("digite a dimensão do primeiro lado do triangulo: "))
b = float(input("digite a dimensão do segundo lado do triangulo: "))
c = float(input("digite a dimensão do terceiro lado do triangulo: "))





triangulo(a, b, c)

