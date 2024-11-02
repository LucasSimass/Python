from math import floor,ceil
print("-" * 20)
num = float(input("Digite um número não inteiro: "))

print("-" * 20)
print(f"{num} foi arredondado(para cima) para {ceil(num)}")
print(f"{num} foi arredondado(para baixo) para {floor(num)}")
print("-" * 20)