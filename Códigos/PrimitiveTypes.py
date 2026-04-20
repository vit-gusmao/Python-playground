print("'type' mostra a classe da variavel\n")
algo = input("Digite algo: ")
print(f"{algo} é da classe:{type(algo)}")
numero = int(input("Digite um número: "))
print(f"{numero} é da classe:{type(numero)}")

print("\n'isnumeric()' mostra se a variavel é númerica\n")
algo = input("Digite algo: ")
print(f"{algo} é númerico:{algo.isnumeric()}")

print("\n'isalpha()' mostra se a variavel é um alfabético\n")
algo = input("Digite algo: ")
print(f"{algo} é alfabético:{algo.isalpha()}")

print("\n'isalnum()' mostra se a variavel é alfanumérico\n")
algo = input("Digite algo: ")
print(f"{algo} é alfanumérico:{algo.isalnum()}")

print("\n'isupper()' mostra se a variavel há somente letras maiusculas\n")
algo = input("Digite algo: ")
print(f"{algo} há somente letras maiusculas:{algo.isupper()}")

print("\n'islower()' mostra se a variavel há somente letras minusculas\n")
algo = input("Digite algo: ")
print(f"{algo} há somente letras maiusculas:{algo.islower()}")

print("\n'istitle()' mostra se a variavel possui as Primeiras letra de cada palavra é maiúscula e o resto das letras são minúsculas\n")
algo = input("Digite algo: ")
print(f"{algo} as Primeiras letra de cada palavra é maiúscula e o resto das letras são minúsculas:{algo.istitle()}")

input("\nAperte qualquer coisa para fechar...")