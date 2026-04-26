print('Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".\n')

nome = input("Digite o nome da cidade: ").strip().title()
while not nome.replace(" ", "").isalpha():
    print("cidades não possui números.")
    nome = input("Digite o nome da cidade: ").strip().title()

if nome.startswith("Santo"):
    print(f'A cidade "{nome}" começa com "Santo"')
else:
    print(f'A cidade "{nome}" não começa com "Santo"')

input("\nAperte qualquer coisa para fechar...")