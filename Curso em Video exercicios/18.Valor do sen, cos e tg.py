import math

print("Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n")

while True:
    try:
        ang = float(input("Digite um ângulo em graus: "))
        break
    except ValueError:
        print("Valor inválido.")

rad = math.radians(ang)

print(f"Seno: {math.sin(rad):.2f}")
print(f"Cosseno: {math.cos(rad):.2f}")
print(f"Tangente: {math.tan(rad):.2f}\n")

input("\nAperte qualquer coisa para fechar...")