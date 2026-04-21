print("""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento

Seu Programa também deverá mostrar o tempo que falta ou que passou do prazo.\n""")

year = int(input("Digite o ano de nascimento: "))
idd = 2025 - year
iddA = 18 - idd

if idd < 18:
    print(f'Ainda vai se alistar ao serviço militar, falta {iddA} anos para o alistamento')
elif idd > 18:
    print(f'Passou do tempo do alistamento')
else:
    print(f'Hora de se alistar.')

input("\nAperte qualquer coisa para fechar...")