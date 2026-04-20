print("Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n")

price = float(input("Digite o preço do produto: "))
desc = price * 0.05
descPrice = price - desc

print(f"seu produto com desconto será de R${descPrice:.2f}")

input("\nAperte qualquer coisa para fechar...")