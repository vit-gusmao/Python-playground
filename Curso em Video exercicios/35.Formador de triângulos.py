print("Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.\n")

reta1 = float(input("Digite a primeira reta: "))
reta2 = float(input("Digite a segunda reta: "))
reta3 = float(input("Digite a terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("As retas PODEM formar um triângulo")
else:
    print("As retas NÃO podem formar um triângulo")

input("\nAperte qualquer tecla para fechar...")