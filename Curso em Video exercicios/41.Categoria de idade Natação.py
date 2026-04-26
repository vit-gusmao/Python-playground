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

if idd <= 9:
    print(f"Categoria do atleta {nome}: MIRIM")
elif idd <= 14:
    print(f"Categoria do atleta {nome}: INFANTIL")
elif idd <= 19:
    print(f"Categoria do atleta {nome}: JUNIOR")
elif idd <= 20:
    print(f"Categoria do atleta {nome}: SÊNIOR")
else:
    print(f"Categoria do atleta {nome}: MASTER")

input("\nAperte qualquer coisa para fechar...") 