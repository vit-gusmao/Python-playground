import math

print("Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.\n")

ang = float(input("Digite um ângulo em graus: "))
rad = math.radians(ang)
print(f"""Seno: {math.sin(rad):.2f}
(f"Cosseno: {math.cos(rad):.2f}
(f"Tangente: {math.tan(rad):.2f}\n""")

input("\nAperte qualquer coisa para fechar...")