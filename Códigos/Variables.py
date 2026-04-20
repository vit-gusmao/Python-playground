#variaveis em python não precisam ser tipificadas

nome = "vitor" #string: caracteres
idade = 18 #int: números inteiros
peso = 134.5 #float: números com .
mentira = False #boolean: true or false
cadeia = [nome, idade, peso, mentira]
print(cadeia)
print(f"Bom dia {nome}") # f"" faz {} poder puxar variaveis dentro do string

#inputs são sempre do tipo strings e precisam ser convertidos para sairem como outro tipo

n1 = int(input("Digite um número: ")) #int() convertendo o input para int
n2 = int(input("Digite outro: "))
print(f"A soma dos dois números é: {n1 + n2}") #caso não tivesse int(), iria juntar os dois números, não somar
nfloat = float(input("Digite outro: "))
print(nfloat) #números convertido como float aparece .0 do lado dele automaticamente
print(f"{nfloat:.2f}") # ":.xf" o x mostra quantidade de casas decimais no float dentro de {}

input("\nAperte qualquer coisa para fechar...")