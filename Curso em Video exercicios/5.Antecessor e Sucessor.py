print("Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.\n")

def suc_ant():
    while True:
        try:
            num = float(input("digite um número: "))
            suc = num + 1
            ant = num - 1
            return num, ant, suc
        except ValueError:
            print("Digite somente números.")
num, ant, suc = suc_ant()

print(f"o antecessor do número {num} é {ant} e o sucessor é {suc}")

input("\nAperte qualquer coisa para fechar...")