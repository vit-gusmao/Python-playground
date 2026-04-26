#cada string é armazenada em um espaço do computador e cada espaço são colocado em um espaço.
#cada memória armazenada começa no 0, não no 1.

print("Pesquisa e contagem")

print('"len(string)" é usado para saber quantos espaços possui uma string.')
algo = input("Digite algo: ")
print(f' Você digitou "{algo}", possui {len(algo)} caracteres.\n')

print('".count(caractere)" conta quantas vezes um caractere aparece na string.')
algo = input("Digite algo: ")
caractere = input("Digite o caractere que deseja contar: ")
print(f' "{caractere}" aparece {algo.count(caractere)} vezes.\n')

print('".count(caractere, x, y)" conta o caractere entre os índices x e y.')
algo = input("Digite algo: ")
caractere = input("Digite o caractere: ")
x = int(input("Índice x: "))
y = int(input("Índice y: "))
print(f' "{caractere}" aparece {algo.count(caractere, x, y)} vezes entre {x} e {y}.\n')

print('".find(texto)" mostra o índice onde começa o texto (ou -1 se não encontrar).')
algo = input("Digite algo: ")
busca = input("Digite o que deseja encontrar: ")
print(f' "{busca}" começa no índice {algo.find(busca)}.\n')

print('"texto in string" verifica se existe dentro da string.')
algo = input("Digite algo: ")
busca = input("Digite o que deseja procurar: ")
print(f' Existe "{busca}" em "{algo}"? {busca in algo}\n')

print("\n'startswith()' verifica como a string começa\n")
algo = input("Digite algo: ")
inicio = input("Começa com: ")
print(f"{algo} começa com '{inicio}': {algo.startswith(inicio)}")

print("\n'endswith()' verifica como a string termina\n")
algo = input("Digite algo: ")
final = input("Termina com: ")
print(f"{algo} termina com '{final}': {algo.endswith(final)}")

input("\nAperte qualquer coisa para fechar...")