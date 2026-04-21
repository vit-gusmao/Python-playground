print("'type' mostra a classe da variavel\n")
algo = input("Digite algo: ")
print(f"{algo} é da classe: {type(algo)}")

numero = int(input("Digite um número: "))
print(f"{numero} é da classe: {type(numero)}")

#############################################################################

print("\n'isnumeric()' mostra se a variavel é numérica\n")
algo = input("Digite algo: ")
print(f"{algo} é numérico: {algo.isnumeric()}")

print("\n'isdigit()' mostra se a variavel contém apenas dígitos\n")
algo = input("Digite algo: ")
print(f"{algo} contém apenas dígitos: {algo.isdigit()}")

print("\n'isdecimal()' mostra se a variavel é um número decimal (mais restrito)\n")
algo = input("Digite algo: ")
print(f"{algo} é decimal: {algo.isdecimal()}")

#############################################################################

print("\n'isalpha()' mostra se a variavel é alfabética\n")
algo = input("Digite algo: ")
print(f"{algo} é alfabético: {algo.isalpha()}")

print("\n'isalnum()' mostra se a variavel é alfanumérica\n")
algo = input("Digite algo: ")
print(f"{algo} é alfanumérico: {algo.isalnum()}")

print("\n'isspace()' mostra se a variavel contém apenas espaços\n")
algo = input("Digite algo: ")
print(f"{algo} contém apenas espaços: {algo.isspace()}")

#############################################################################

print("\n'isupper()' mostra se há somente letras maiúsculas\n")
algo = input("Digite algo: ")
print(f"{algo} há somente letras maiúsculas: {algo.isupper()}")

print("\n'islower()' mostra se há somente letras minúsculas\n")
algo = input("Digite algo: ")
print(f"{algo} há somente letras minúsculas: {algo.islower()}")

print("\n'istitle()' verifica se cada palavra começa com maiúscula\n")
algo = input("Digite algo: ")
print(f"{algo} está no formato de título: {algo.istitle()}")

#############################################################################

print("\n'startswith()' verifica como a string começa\n")
algo = input("Digite algo: ")
inicio = input("Começa com: ")
print(f"{algo} começa com '{inicio}': {algo.startswith(inicio)}")

print("\n'endswith()' verifica como a string termina\n")
algo = input("Digite algo: ")
final = input("Termina com: ")
print(f"{algo} termina com '{final}': {algo.endswith(final)}")

#############################################################################

print("\n'len()' mostra o tamanho da string\n")
algo = input("Digite algo: ")
print(f"{algo} tem {len(algo)} caracteres")

#############################################################################

print("\n'upper()', 'lower()', 'title()', 'capitalize()'\n")
algo = input("Digite algo: ")
print(f"""Original: {algo}
Maiúsculo: {algo.upper()}
Minúsculo: {algo.lower()}
Título: {algo.title()}
Capitalizado: {algo.capitalize()}
""")

#############################################################################

print("\n'strip()', 'lstrip()', 'rstrip()' removem espaços\n")
algo = input("Digite algo (com espaços): ")
print(f"""Original: [{algo}]
strip(): [{algo.strip()}]
lstrip(): [{algo.lstrip()}]
rstrip(): [{algo.rstrip()}]
""")

#############################################################################

print("\n'replace()' substitui partes da string\n")
algo = input("Digite algo: ")
velho = input("O que deseja substituir: ")
novo = input("Por: ")
print(f"Resultado: {algo.replace(velho, novo)}")

#############################################################################

print("\n'split()' divide a string em partes\n")
algo = input("Digite algo: ")
print(f"Dividido: {algo.split()}")

#############################################################################

input("\nAperte qualquer coisa para fechar...")