print("""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo e qual é o tipo do triângulo que será formado:
-Equilátero: todos os lados iguais
-Isóceles: dois lados iguais
-Escaleno: todos os lados diferentes\n""")

reta1 = float(input("Digite o tamanho da reta 1: "))
while reta1 <= 0:
    print(f'o valor "{reta1}" é inválido para ser uma reta, o valor deve ser positivo')
    reta1 = float(input("Digite o tamanho da reta 1: "))

reta2 = float(input("Digite o tamanho da reta 2: "))
while reta2 <= 0:
    print(f'o valor "{reta2}" é inválido para ser uma reta, o valor deve ser positivo')
    reta2 = float(input("Digite o tamanho da reta 2: "))

reta3 = float(input("Digite o tamanho da reta 3: "))
while reta3 <= 0:
    print(f'o valor "{reta3}" é inválido para ser uma reta, o valor deve ser positivo')
    reta3 = float(input("Digite o tamanho da reta 3: "))

tri = reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2

if tri:
    print(f'As retas "{reta1}", "{reta2}" e "{reta3}" formam um triângulo.')
    if reta1 == reta2 == reta3:
        print("Triângulo equilátero")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print(f'As retas {reta1}, {reta2} e {reta3} não formam um triângulo.')

input("\nAperte qualquer tecla para fechar...")