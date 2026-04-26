print("Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.\n")

while True:
        try:
            num = float(input("Digite um número inteiro para mostrar a tabuada: "))
            while not num.is_integer():
                print("Valor inválido.")
            break
        except ValueError:
            print(f'Valor Inválido.')          

print(f"A tabuada do número {num} é:")
for i in range(10):
    print(f"{num} x {i + 1} = {num * (i + 1)}")
