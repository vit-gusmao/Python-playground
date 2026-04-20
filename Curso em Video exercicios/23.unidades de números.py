print("Faça um programa que leia um número inteiro de 0 a 9999 e mostre na tela cada um dos digitos separados.\n")

num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print(f"""Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}""")

input("\nAperte qualquer coisa para fechar...")