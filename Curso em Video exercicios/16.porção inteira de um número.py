from math import trunc

print("Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.\n")

while True:
    try:
        num = float(input("Digite um número decimal: "))
        break
    except ValueError:
            print("Digite somente números decimais.")

print(f"a porção inteira do {num} é {trunc(num)}")

input("\nAperte qualquer coisa para fechar...")