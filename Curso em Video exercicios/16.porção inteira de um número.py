import math

print("Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.\n")

num = float(input("Digite um número: "))
print(f"a porção inteira do {num} é {math.ceil(num)}")

input("\nAperte qualquer coisa para fechar...")