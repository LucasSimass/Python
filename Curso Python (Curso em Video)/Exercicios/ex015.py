print('-' * 20)
dias = int(input("Quanto dias o carro ficou alugado (digite apenas o número)? "))
km = float(input("Quantos km rodados (digite apenas o número)? "))

total = (dias * 60) + (km * 0.15 )

print('-' * 20)
print(f"O total a pagar é R${total:.2f}!")
print('-' * 20)


