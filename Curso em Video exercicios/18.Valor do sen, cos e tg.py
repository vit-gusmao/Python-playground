from math import sin, cos, tan, radians

print("Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n")

while True:
    try:
        ang = float(input("Digite um ângulo em graus: "))
        break
    except ValueError:
        print("Valor inválido.")

rad = radians(ang)

print(f"Seno: {sin(rad):.2f}")
print(f"Cosseno: {cos(rad):.2f}")
print(f"Tangente: {tan(rad):.2f}\n")

input("\nAperte qualquer coisa para fechar...")