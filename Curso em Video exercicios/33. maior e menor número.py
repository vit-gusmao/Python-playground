print("Faça um programa que leia três números e mostre qual é o maior e qual é o menor número.")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"o maior valor digitado é {n1}")
elif n2 > n1 and n2 > n3:
    print(f"o maior valor digitado é {n2}")
else:
    print(f"o maior valor digitado é {n3}")

if n1 < n2 and n1 < n3:
    print(f"o menor valor digitado é {n1}")
elif n2 < n1 and n2 < n3:
    print(f"o menor valor digitado é {n2}")
else:
    print(f"o menor valor digitado é {n3}")

input("\nAperte qualquer tecla para fechar...")