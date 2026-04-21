print("Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.\n")
nome = input("Digite seu nome: ")
while not nome.isalpha():
    print(f'"{nome}" não é um nome.')
    nome = input("Digite seu nome: ").capitalize()

print(f"Olá {nome.capitalize()}! Prazer em te conhecer!")

input("\nAperte qualquer coisa para fechar...")