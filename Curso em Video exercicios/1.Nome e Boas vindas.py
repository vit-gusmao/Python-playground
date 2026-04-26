print("Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.\n")


nome = input("Digite seu nome: ").strip()
while not nome.replace(" ", "").isalpha():
    print(f'Nomes possui somente letras.')
    nome = input("Digite seu nome: ").strip()

print(f"Olá {nome.title()}! Prazer em te conhecer!")

input("\nAperte qualquer coisa para fechar...")