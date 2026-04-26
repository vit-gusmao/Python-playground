print("""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.\n""")

while True:
    try:
        casa = float(input("Digite o valor da casa: R$"))
        sal = float(input("Digite o valor do salário do comprador: R$"))
        year = int(input("Digite em quantos anos a casa será paga: "))
        break
    except ValueError:
        print("Número inválido, por favor digite valores numéricos válidos.")


Pmensal = casa / (year * 12)
sal30 = sal * 0.30

if Pmensal > sal30:
    print("empréstimo negado, o valor excede 30% do seu atual salário")
else:
    print(f"empréstimo concedido, a prestação mensal será R${Pmensal:.2f}")

input("\n Aperte qualquer coisa para fechar o programa...")