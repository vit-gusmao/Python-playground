from xml import dom

print('''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "A"
Em qual posição ela aparece a primeira vez
Em que posição ela aparece a última vez''')

frase = input('Digite uma frase com a letra "A": ').upper()

while frase.count("A") == 0:
    print("Sua frase não possui letra A")
    frase = input('Digite uma frase com a letra "A": ').upper()

print(f'Quantidade de "A": {frase.count("A")}')
print(f'Primeira posição: {frase.find("A")}')
print(f'Última posição: {frase.rfind("A")}')

input('\nPressione Qualquer coisa para sair...')