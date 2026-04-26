from math import trunc, ceil, floor

def int_dec():
 while True:
    try:
        entry = (input("Digite um número: "))
        num = float(entry)
        return num
    except ValueError:
        print(f'"{entry}" não é um número.')


def decimal():
     while True:
        try:
            entry = (input("Digite um número decimal: "))
            num = float(entry)
            while num.is_integer():
                 print(f'"{trunc(num)}" não é um número decimal.')
                 num = float(input("Digite um número decimal: "))
            return num
        except ValueError:
            print(f'"{entry}" é um número decimal.')



###########################################################################################

print('"var.is_integer()" verifica se o float possui casa decimais ou não.\n')

num = int_dec()
if not num.is_integer():
    print(f'o número {num} possui casa decimais.')
else:
    print(f'o número {trunc(num)} não possui casa decimais.')

print()
###########################################################################################

print('''round(var) arredonda o float da seguinte forma:
Se for .0 até .4 → arredonda o float para baixo
Se for .5 até .9 → arredonda o float para cima\n''')

num = decimal()
print(f'o número {num} arredondado em round: {round(num)}\n')

###########################################################################################

print('''"math.ceil(var)" arredonda o float para cima.
"math.floor(var)" arredonda o float para baixo.\n''')

num = decimal()
print(f"{num} -> ceil: {ceil(num)} | floor: {floor(num)}\n")

###########################################################################################

print("'math.trunc(var)' remove a parte decimal do float.\n")
num = decimal()
print(f"{num} truncado fica {trunc(num)}\n")