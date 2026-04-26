print("""Crie um programa que leia o nome completo de uma pessoa e mostre:
 o primeiro e o último nome separado
 o nome com todas as letras maiúsculas
 quantas letras ao todo (sem considerar espaços)
 Quantas letras tem o primeiro nome
 se possui "Silva" no nome\n""")

while True:
    nome = input("Digite seu nome completo: ").strip()
    if not nome.replace(" ", "").isalpha():
        print("Nomes não tem letras.")
    elif len(nome.split()) < 2:
        print("Nomes completos tem mais de um nome.")
    else:
        break    


print(f'''Seu nome é "{nome.title()}"
seu nome possui {len(nome.replace(" ", ""))} letras
seu primeiro nome é "{nome.split()[0]}" e possui {len(nome.split()[0])} letras
seu último nome é "{nome.split()[-1]}" e possui {len(nome.split()[-1])} letras
seu nome com todas as letras maiúsculas: "{nome.upper()}"
seu nome com todas as letras minúsculas: "{nome.lower()}"\n''')
if "Silva" in nome == True:
    print(f'o nome "{nome}" possui "Silva"')
else:
    print(f'o nome "{nome}" não possui "Silva"')


input("\n Aperte qualquer coisa para fechar...")
