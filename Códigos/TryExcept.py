# Try e Except são usados para evitar que o programa quebre quando ocorre um erro.
# Muito útil quando o usuário pode digitar algo inválido.

print("Tratamento de erros com Try e Except\n")

print('"try/except" evita que o programa pare quando ocorre erro.')
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número {numero}\n")
except:
    print("Erro! Você não digitou um número válido.\n")

#############################################################################

print('"ValueError" acontece quando o tipo de dado está errado (ex: letra no int).')
try:
    numero = int(input("Digite um número: "))
    print(f"Número convertido: {numero}\n")
except ValueError:
    print("Erro! Digite apenas números inteiros.\n")

#############################################################################

print('"ZeroDivisionError" acontece quando tenta dividir por zero.')
try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print(f"Resultado: {n1 / n2}\n")
except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.\n")

#############################################################################

print('"TypeError" acontece quando o tipo da variável não permite uma operação.')
try:
    texto = "abc"
    resultado = texto + 5  # não pode somar string com int
except TypeError:
    print("Erro! Não é possível somar string e inteiro.\n")

#############################################################################

print('"IndexError" acontece quando o índice não existe na lista.')
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro! Índice fora do alcance da lista.\n")

#############################################################################

print('"KeyError" acontece quando a chave não existe no dicionário.')
try:
    dicionario = {"nome": "João"}
    print(dicionario["idade"])
except KeyError:
    print("Erro! Chave não encontrada no dicionário.\n")

##############################################################################
print('"else" executa se NÃO der erro.')
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro ao converter.\n")
else:
    print(f"Conversão feita com sucesso: {numero}\n")

#############################################################################

print('"finally" sempre executa, com erro ou não.')
try:
    numero = int(input("Digite um número: "))
    print(numero)
except:
    print("Erro ao converter.")
finally:
    print("Fim da tentativa.\n")

#############################################################################

input("Aperte qualquer coisa para fechar...")