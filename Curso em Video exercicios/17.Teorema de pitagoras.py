import math

print("Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.\n")

ops = int(input("Digite o valor do comprimento do cateto oposto do triângulo retângulo: "))
adj = int(input("Digite o valor do comprimento do cateto adjacente do triângulo retângulo: "))
hip = math.sqrt(ops ** 2 + adj ** 2)

print(f"A hipotenusa é: {hip:.2f}")

input("\nAperte qualquer coisa para fechar...")