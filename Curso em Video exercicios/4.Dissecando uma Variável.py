print("Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.\n")
algo = input("Digite algo: ")
print(f"""\n{algo} é da classe:{type(algo)}
{algo} é númerico:{algo.isnumeric()}
{algo} é alfabético:{algo.isalpha()}
{algo} é alfanumérico:{algo.isalnum()}
{algo} há somente letras maiusculas:{algo.isupper()}
{algo} há somente letras maiusculas:{algo.islower()}
{algo} as Primeiras letra de cada palavra é maiúscula e o resto das letras são minúsculas:{algo.istitle()}""")

input("\nAperte qualquer coisa para fechar...")
