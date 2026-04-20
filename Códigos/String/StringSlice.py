#toda memória é armazenada em um espaço do computador.
#cada memória armazenada começa no 0, não no 1.

print("Fatiamento de string\n")

print("""x = índice inicial (0)
y = índice final do antecessor (1)
z = índice pula espaços\n""")

print('"string[x:]" recebe o índice x até o final.')
algo = input("Digite algo: ")
x = int(input("Digite o índice x: "))
print(f' Resultado: "{algo[x:]}"\n')

print('"string[:y]" recebe do início até o antecessor do índice y.')
algo = input("Digite algo: ")
y = int(input("Digite o índice y: "))
print(f' Resultado: "{algo[:y]}"\n')

print('"string[::z]" recebe do início até o final pulando de z em z.')
algo = input("Digite algo: ")
z = int(input("Digite o índice z: "))
print(f' Resultado: "{algo[:y]}"\n')

print('"string[x:y]" recebe do índice x até o antecessor do índice y.')
algo = input("Digite algo: ")
x = int(input("Índice x: "))
y = int(input("Índice y: "))
print(f' Resultado: "{algo[x:y]}"\n')

print('"string[x:y:z]" recebe pulando de z em z.')
algo = input("Digite algo: ")
x = int(input("Índice x: "))
y = int(input("Índice y: "))
z = int(input("Índice z: "))
print(f' Resultado: "{algo[x:y:z]}"\n')

print('"string[x::z]" pega de x até o final pulando de z em z.')
algo = input("Digite algo: ")
x = int(input("Índice x: "))
z = int(input("Índice z: "))
print(f' Resultado: "{algo[x::z]}"')


print('"string[:y:z]" pulando de z em z.')
algo = input("Digite algo: ")
y = int(input("Índice y: "))
z = int(input("Índice z: "))
print(f' Resultado: "{algo[:y:z]}"')

input("\nAperte qualquer coisa para fechar...")