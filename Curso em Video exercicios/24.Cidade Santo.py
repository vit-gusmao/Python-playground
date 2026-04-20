print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".\n')

nome = input("Digite o nome da cidade: ").capitalize()
if nome.find("Santo") != 0:
    print('A cidade que você digitou não começa com "Santo"')
else:
    print('A cidade que você digitou começa com "Santo"')

    input("\nAperte qualquer coisa para fechar...")