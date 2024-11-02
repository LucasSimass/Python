import random
from math import sqrt , floor

num = int(input("Digite um número: "))

print('-' * 20)

raiz =  sqrt(num)

print(f"A raiz de {num} é {floor(raiz):.2f}")
print('-' * 20)

num_aleatorio = random.randint(1,10)

print(num_aleatorio)

print('-' * 20)