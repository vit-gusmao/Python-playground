print("""Escreva um programa que leia um número inteiro qualquer  e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal\n""")

num = int(input("Digite um número: "))
conv = int(input("""Selecione a conversão: 
- 1 para binário
- 2 para octal
- 3 para hexadecimal

Selecione: """))
while conv < 0 or conv > 3:
    print(f'{conv} não é uma opção válida.')
    conv = int(input("""Selecione a conversão: 
    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal 
    
Selecione: """))

if conv == 3:
    print(f'convertendo o número "{num}" para hexadecimal:"{hex(num)}"')
elif conv == 2:
    print(f'convertendo o número "{num}" para octal:"{oct(num)}"')
else:
    print(f'convertendo o número "{num}" para octal:"{oct(num)}"')

input("\n Aperte qualquer coisa para fechar o programa...")