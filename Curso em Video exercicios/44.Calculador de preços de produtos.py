print("""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartâo: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
\n""")

while True:
    try:
        price = float(input("Digite o preço do produto:R$"))
        break
    except ValueError:
        print("Não digite letras e simbólos.")

print()

pag = [
    "À vista dinheiro/cheque: 10% de desconto",
    "À vista no cartão: 5% de desconto",
    "Em até 2x no cartão: preço normal",
    "3x ou mais no cartão: 20% de juros"
]

for i, option in enumerate(pag, start=1):
    print(f"Aperte {i} para pagar {option}")

print()

while True:
    try:
        option = int(input("Escolha a opção: "))
        while option < 0 or option > 4:
            print("Digite um número válido.")
            option = int(input("Escolha a opção: "))
        break
    except ValueError:
        print("Digite um número válido.")

verify = [
    (lambda p: price - (price * 0.10)),    
    (lambda p: price - (price * 0.05)),   
    (lambda p: price),          
    (lambda p: price + (price * 0.20))     
]

final_price = verify[option - 1](price)

print()

print(f"""O preço do produto é: R${price:.2f}
Metódo de pagamento escolhido: {pag[option - 1]}
Preço final do produto: R${final_price:.2f}""")


input("\nAperte qualquer coisa para fechar...")