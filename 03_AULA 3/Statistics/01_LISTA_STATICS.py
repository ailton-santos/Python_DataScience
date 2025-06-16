#1. Crie um programa onde o usuário irá digitar 4 notas,
#  exiba em tela as notas digitadas,
#  a média das notas e se ele está APROVADO,
#  em RECUPERAÇÂO, ou REPROVADO:
#   • OBS : Não importar nenhuma biblioteca nesse exercicio<> 
# Media abaixo de 5 -> REPROVADO
# <> Média entre 5 e 6.9 -> RECUPERACAO
# <> Média acima de 7 -> APROVADO

nota1=float(input("digite a sua 1° nota:"))
nota2=float(input("digite a sua 2° nota:"))
nota3=float(input("digite a sua 3° nota:"))
nota4=float(input("digite a sua 4° nota:"))

print(f"Sua 1° nota foi: {nota1}")
print(f"Sua 2° nota foi: {nota2}")
print(f"Sua 3° nota foi: {nota3}")
print(f"Sua 4° nota foi: {nota4}")

finalmedia = (nota1+nota2+nota3+nota4)/4

print(f"Sua media final Foi de: {finalmedia}")

if finalmedia > 7:
    print("APROVADO") 
elif finalmedia < 5:
    print("REPROVADO")
elif finalmedia >=5 and finalmedia <= 6.9:
    print("RECULPERAÇÃO")


    
