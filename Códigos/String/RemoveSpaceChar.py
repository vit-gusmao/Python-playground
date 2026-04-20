#toda memória é armazenada em um espaço do computador.
#cada memória armazenada começa no 0, não no 1.

print("Remoção de espaços e caracteres")

print('".strip()" remove espaços do início e do fim.')
algo = input("Digite algo com espaços: ")
print(f' Resultado: "{algo.strip()}"\n')

print('".strip(caractere)" remove caractere específico das pontas.')
algo = input("Digite algo: ")
caractere = input("Digite o caractere para remover: ")
print(f' Resultado: "{algo.strip(caractere)}"\n')

print('".lstrip()" remove espaços da esquerda.')
algo = input("Digite algo: ")
print(f' Resultado: "{algo.lstrip()}"\n')

print('".rstrip()" remove espaços da direita.')
algo = input("Digite algo: ")
print(f' Resultado: "{algo.rstrip()}"\n')

print('".lstrip(caractere)" remove caractere da esquerda.')
algo = input("Digite algo: ")
caractere = input("Digite o caractere: ")
print(f' Resultado: "{algo.lstrip(caractere)}"\n')

print('".rstrip(caractere)" remove caractere da direita.')
algo = input("Digite algo: ")
caractere = input("Digite o caractere: ")
print(f' Resultado: "{algo.rstrip(caractere)}"\n')

print('".split()" separa a string em grupos de espaço.') #grupo de espaço se inicia do 0 e para puxar sempre o ultimo espaço é -1
algo = input("Digite algo: ")
print(f' Resultado: {algo.split()}\n')

print('"separador.join(texto)" junta caracteres com um separador.')
algo = input("Digite algo: ")
separador = input("Digite o separador: ")
print(f' Resultado: "{separador.join(algo)}"\n')

input("\nAperte qualquer coisa para fechar...")