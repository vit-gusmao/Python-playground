print("Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR")

while True:
    try:
        n1 = int(input("Digite um Número inteiro: "))
        break
    except ValueError:
        print("Número inválido.")

if n1 % 2 == 0:
    print(f"O número {n1} é par")
else:
    print(f"O número {n1} é impar")