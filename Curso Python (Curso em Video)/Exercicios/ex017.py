from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"A hipotenusa vai medir {hi:.2f}!")

print('-' * 20)

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

hi = hypot(co,ca)

print(f'A hipotenusa vai medir {hi:.2f}!')