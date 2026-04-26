print("Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.\n")

while True:
        try:
            n = float(input("digite um número: "))
            break
        except ValueError:
            print("Digite somente números.")

num = int(n) if n.is_integer() else n

suc = num + 1
ant = num - 1

print(f"o antecessor do número {num} é {ant} e o sucessor é {suc}")

input("\nAperte qualquer coisa para fechar...")