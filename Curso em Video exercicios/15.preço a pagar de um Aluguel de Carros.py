print("Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por cada carro.\n")

km = float(input("Digite a quantidade de Km percorridos: "))
dia = int(input("Digite a quantidade de dias que o carro foi alugado: "))
Cdia = dia * 60
Ckm = km * 0.15
price = Ckm + Cdia

print(f"o preço a pagar é R${price:.2f}")

input("\nAperte qualquer coisa para fechar...")