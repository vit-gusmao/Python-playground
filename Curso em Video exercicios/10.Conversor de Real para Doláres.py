print('''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
      "considere:\n US$1,00 = R$3,27"\n"''')

rs = float(input("Digite o valor do seu dinheiro em real: "))
us = 3,27
buy = rs / 3,27
print(f"Você pode comprar {buy:.2f} doláres")

input("\nAperte qualquer coisa para fechar...")