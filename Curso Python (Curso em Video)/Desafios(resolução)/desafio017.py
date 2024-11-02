print('-' * 20)
cateto1 = float(input("Informe o primeiro número do cateto (em metros): "))
cateto2 = float(input("Informe o segundo número do cateto (em metros): "))

hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2)) ** (1/2)
print('-' * 20)
print(f"A medida da hipotenusa é  de {hipotenusa}m")
print('-' * 20)