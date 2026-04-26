print("""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER\n""")

while True:
    try:
        nome = input("Digite o nome do atleta: ").strip().title()
        while not nome.replace(" ", "").isalpha():
            print("Nomes possuem somente letras.")
            nome = input("Digite o nome do atleta: ").strip().title()
        
        idd = int(input("Digite a idade do atleta: "))
        break
    except ValueError:
        print("Opção inválida. Digite a idade como número inteiro.")

verify = [
    ("MIRIM", idd <= 9)
    ("INFANTIL", idd <= 14)
    ("JUNIOR", idd <= 19)
    ("SÊNIOR", idd <= 20)
    ("MASTER", idd > 20)
]

for status, condition in verify:
    print(f"O Atleta {nome} possui {idd} e está na categoria {status}")

input("\nAperte qualquer coisa para fechar...")