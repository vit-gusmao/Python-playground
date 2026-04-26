import math

print("Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.\n")

while True:
    try:
        ops = float(input("Digite o valor do comprimento do cateto oposto do triângulo retângulo: "))
        adj = float(input("Digite o valor do comprimento do cateto adjacente do triângulo retângulo: "))
        break
    except ValueError:
        print("Valor inválido.")

hip = math.sqrt(ops ** 2 + adj ** 2)

print(f"A hipotenusa é: {hip:.2f}")

input("\nAperte qualquer coisa para fechar...")