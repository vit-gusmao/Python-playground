print("Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR")

while True:
    try:
        n1 = float(input("Digite um Número inteiro: "))
        if not n1.is_integer():
            print("Não digite números decimais.")
            continue
        n1 = int(n1)
        break
    except ValueError:
        print("Número inválido.")

if n1 % 2 == 0:
    print(f"O número {n1} é par")
else:
    print(f"O número {n1} é impar")