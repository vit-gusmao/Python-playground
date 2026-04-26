print('''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
      "considere:\n US$1,00 = R$3,27"\n"''')

while True:
    try:
        rs = float(input("Digite o valor do seu dinheiro em real: "))
        break
    except ValueError:
        print("Não digite palavras ou simbolos.")

us = 3.27
buy = rs / us
print(f"Você pode comprar {buy:.2f} dólares")

input("\nAperte qualquer coisa para fechar...")