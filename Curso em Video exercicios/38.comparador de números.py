print("""Escreva um programa que leia dois números inteiros  e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais\n""")

num = []
while True:
    try:
        num = []
        for i in range(2):
            n = float(input(f"Digite o {i + 1}° número: "))
            num.append(n)
        break
    except ValueError:
        print("Digite somente números.")

numf = [int(n) if n.is_integer() else n for n in num]

if numf[0] > numf[1]:
    print(f'O número "{numf[0]}" é maior que "{numf[1]}"')
elif numf[0] < numf[1]:
    print(f'O número "{numf[1]}" é maior que "{numf[0]}"')
else:
    print(f'O número "{numf[0]}" é igual a "{numf[1]}"')

input("\n Aperte qualquer coisa para fechar...")