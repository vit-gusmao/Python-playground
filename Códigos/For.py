#"for" é usado para repetir um número específico de vezes.

print('"for in range" repete uma quantidade definida de vezes.\n')

qtd_repeticoes = int(input("Digite um número para mostrar ele do começo até o final: "))
for numero in range(qtd_repeticoes + 1):  # o +1 mostra até o número final, pois o range é exclusivo no final.
    print(f"Repetição: {numero}")
print()

limite_superior = int(input("Digite um número para mostrar ele do 1 até o final: "))
for contador in range(limite_superior):
    print(f"Repetição: {contador + 1}")  # começa do 1, não do 0.

#############################################################################

print('\n"for" com início, fim e passo.\n')

inicio = 1
fim = 11
passo = 2

for valor_atual in range(inicio, fim, passo):
    print(f"Número: {valor_atual + 1}")

print("Fim do loop com passo.\n")

#############################################################################

print('"foreach" (for em listas) percorre elementos diretamente.\n')

lista_de_nomes = ["Ana", "Carlos", "João"]

for nome_aluno in lista_de_nomes:
    print(f"Nome: {nome_aluno}")

print("Fim do foreach.\n")

#############################################################################

print('"for" com índice usando enumerate.\n')

lista_de_frutas = ["Maçã", "Banana", "Uva"]

for indice_fruta, fruta_nome in enumerate(lista_de_frutas):
    print(f"Índice: {indice_fruta} - Fruta: {fruta_nome}")

print("Fim do for com índice.\n")

#############################################################################

print('"enumerate com start=" (índice começando de algum lugar)\n')

for posicao, fruta_enumerada in enumerate(lista_de_frutas, start=1):
    print(f"Posição: {posicao} - Fruta: {fruta_enumerada}")

print("Fim do enumerate com start.\n")

#############################################################################
# 🧠 NOVO CONCEITO 2: LISTA COMO MENU + INDEXAÇÃO
#############################################################################

print("Lista sendo usada como menu (simulando escolha do usuário)\n")

opcoes_pagamento = [
    "À vista dinheiro/cheque",
    "À vista no cartão",
    "Em até 2x no cartão",
    "3x ou mais no cartão"
]

for indice_opcao, descricao_opcao in enumerate(opcoes_pagamento, start=1):
    print(f"[{indice_opcao}] {descricao_opcao}")

simulacao_escolha_usuario = 2  # simulação de escolha do usuário

print(f"\nUsuário escolheu: {opcoes_pagamento[simulacao_escolha_usuario - 1]}")

print("Fim do exemplo de lista como menu.\n")

#############################################################################
# 🧠 NOVO CONCEITO 3: LAMBDA (FUNÇÃO CURTA)
#############################################################################

print('"lambda" (função curta sem nome)\n')

funcoes_calculo_preco = [
    lambda preco: preco * 0.9,
    lambda preco: preco * 0.95,
    lambda preco: preco,
    lambda preco: preco * 1.2
]

preco_base = 100
escolha_pagamento = 1

preco_final = funcoes_calculo_preco[escolha_pagamento - 1](preco_base)

print(f"Preço original: {preco_base}")
print(f"Preço final com lambda: {preco_final}")

print("Fim do lambda.\n")

#############################################################################
# 🧠 NOVO CONCEITO 4: FOR USANDO LISTA DE FUNÇÕES (IDEIA AVANÇADA)
#############################################################################

print('"lista de funções + escolha por índice"\n')

for indice_funcao in range(len(funcoes_calculo_preco)):
    resultado_calculo = funcoes_calculo_preco[indice_funcao](preco_base)
    print(f"Opção {indice_funcao + 1} gera: {resultado_calculo}")

print("Fim do exemplo avançado.\n")

#############################################################################

input("\nAperte qualquer coisa para fechar...")