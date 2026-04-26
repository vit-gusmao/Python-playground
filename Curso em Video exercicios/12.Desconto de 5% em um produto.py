print("Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n")

while True:
    try:
        price = float(input("Digite o preço do produto: "))
        break
    except ValueError:
        print("Valor inválido.")

desc = price * 0.05
descPrice = price - desc

print(f"seu produto com desconto será de R${descPrice:.2f}")

input("\nAperte qualquer coisa para fechar...")