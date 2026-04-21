print("'Conversões numéricas' em Python\n")
print("Permite converter números para binário, octal e hexadecimal\n")

# ================= BINÁRIO =================
print('\nConversão para BINÁRIO "bin(var)"\n')
num = int(input("Digite um número inteiro: "))
print(f"Binário (com prefixo): {bin(num)}")
print(f"Binário (sem prefixo 0b): {bin(num)[2:]}")

# ================= OCTAL =================
print('\nConversão para OCTAL "oct(var)"\n')
num = int(input("Digite um número inteiro: "))
print(f"Octal (com prefixo): {oct(num)}")
print(f"Octal (sem prefixo 0o): {oct(num)[2:]}")

# ================= HEXADECIMAL =================
print('\nConversão para HEXADECIMAL "hex(var)"\n')
num = int(input("Digite um número inteiro: "))
print(f"Hexadecimal (com prefixo): {hex(num)}")
print(f"Hexadecimal (sem prefixo 0x): {hex(num)[2:]}")

# ================= FORMAT() =================
print('\nConversão usando format()\n')
num = int(input("Digite um número inteiro: "))
print(f"""Resultado:
Binário: {format(num, "b")}
Octal: {format(num, "o")}
Hexadecimal: {format(num, "x")}
""")

# ================= F-STRING =================
print('\nConversão usando f-string\n')
num = int(input("Digite um número inteiro: "))
print(f"""Resultado:
Binário: {num:b}
Octal: {num:o}
Hexadecimal: {num:x}
Hexadecimal MAIÚSCULO: {num:X}
""")

# ================= CONVERSÃO REVERSA =================
print('\nConversão reversa (outras bases → decimal)\n')

binario = input("Digite um número em binário: ")
print(f"Decimal: {int(binario, 2)}")

octal = input("Digite um número em octal: ")
print(f"Decimal: {int(octal, 8)}")

hexa = input("Digite um número em hexadecimal: ")
print(f"Decimal: {int(hexa, 16)}")

input("\nAperte qualquer coisa para fechar...")