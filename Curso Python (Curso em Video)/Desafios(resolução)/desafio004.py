n = input("digite algo: ")
print(type(n))

if n.isnumeric():
    print(f"O valor '{n}' é um numero")

if n.isalpha():
    print(f"O valor '{n}' é um texto")

if n.isupper():
    print(f"O valor '{n}' está com todas as letras maiusculas")

if n.islower():
    print(f"O valor '{n}' está com todas as letras minusculas")

if n.isspace():
    print(f"O valor {n} possui apenas espaço")