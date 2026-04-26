print("Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.\n")

while True:
    try:
        sal = float(input("Digite o salário: "))
        break
    except ValueError:
        print("Valor inválido.")

aum = sal * 0.15
aumSal = sal + aum

print(f"O novo salário com aumento será de R${aumSal:.2f}")

input("\nAperte qualquer coisa para fechar...")