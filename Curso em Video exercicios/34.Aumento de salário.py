print('''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%.\n''')

print("Se seu salário for superior a R$1250,00 você receberá um aumento de 10%, se for inferior, receberá um aumento de 15%")

while True:
    try:
        sal = float(input("Digite o seu salário atual:R$ "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número válido para o salário.")

aum10 = sal * 0.10 + sal
aum15 = sal * 0.15 + sal

if sal > 1250.00:
    print(f"Seu salário é superior a R$1250,00 e recebeu um aumento de 10% e agora seu salário novo é R${aum10:.2f}")
elif sal <= 1250.00:
    print(f"Seu salário é inferior ou igual a R$1250,00 e recebeu um aumento de 15% e agora seu salário novo é R${aum15:.2f}")

input("\nAperte qualquer tecla para fechar...")