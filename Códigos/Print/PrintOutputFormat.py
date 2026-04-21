#formas de formatação de saída com print()

print('""" """ permite escrever textos em múltiplas linhas.\n')
texto = input("Digite uma mensagem para se repetir em múltiplas linhas: ")
print(f"""Você digitou:
{texto}
{texto}
{texto}
{texto}
Isso está em múltiplas linhas.\n""")
###################################################################################

print("Quebra de linha")

print('"\\n" é usado para pular uma linha no texto.\n')
texto = input("Digite algo: ")
print(f'Primeira linha\nSegunda linha com: {texto}\n')

##############################################################################

print("Aspas dentro de strings")

print('"\\"" é usado para mostrar aspas dentro de uma string.\n')
texto = input("Digite algo: ")
print(f'Você disse: "{texto}" (com aspas incluídas)\n')

print("Também é possível usar aspas simples e duplas para evitar conflitos.")
texto = input("Digite algo: ")
print(f'''Usando aspas simples fora: '{texto}'
Usando aspas duplas fora: "{texto}"''')

input("\nAperte qualquer coisa para fechar...")


