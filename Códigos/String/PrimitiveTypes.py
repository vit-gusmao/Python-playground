print("'type' mostra a classe da variável\n")
algo = input("Digite algo: ")
print(f"{algo} é da classe: {type(algo)}")

numero = int(input("Digite um número inteiro: "))
print(f"{numero} é da classe: {type(numero)}")

#############################################################################
print("\n'len()' mostra o tamanho da string\n")
algo = input("Digite algo: ")
print(f"{algo} tem {len(algo)} caracteres")

#############################################################################

print("\n'isnumeric()' verifica se a string representa um número (mais amplo)\n")
algo = input("Digite algo: ")
print(f"{algo} é numérico: {algo.isnumeric()}")

print("\n'isdigit()' verifica se contém apenas dígitos\n")
algo = input("Digite algo: ")
print(f"{algo} contém apenas dígitos: {algo.isdigit()}")

print("\n'isdecimal()' verifica se contém apenas dígitos de 0 a 9 (mais restrito)\n")
algo = input("Digite algo: ")
print(f"{algo} é decimal: {algo.isdecimal()}")

#############################################################################

print("\n'isalpha()' verifica se contém apenas letras\n")
algo = input("Digite algo: ")
print(f"{algo} é alfabético: {algo.isalpha()}")

print("\n'isalnum()' verifica se contém apenas letras e números\n")
algo = input("Digite algo: ")
print(f"{algo} é alfanumérico: {algo.isalnum()}")

print("\n'isspace()' verifica se contém apenas espaços\n")
algo = input("Digite algo: ")
print(f"{algo} contém apenas espaços: {algo.isspace()}")

#############################################################################

print("\n'isupper()' verifica se todas as letras são maiúsculas\n")
algo = input("Digite algo: ")
print(f"{algo} está em maiúsculas: {algo.isupper()}")

print("\n'islower()' verifica se todas as letras são minúsculas\n")
algo = input("Digite algo: ")
print(f"{algo} está em minúsculas: {algo.islower()}")

print("\n'istitle()' verifica se cada palavra começa com maiúscula\n")
algo = input("Digite algo: ")
print(f"{algo} está no formato de título: {algo.istitle()}")

#############################################################################

input("\nAperte qualquer coisa para fechar...")