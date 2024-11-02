print('-' * 20)
salario = float(input("Quanto você ganha? R$"))

print(f"Se você supostamente tivesse um aumento de 15% você teria {(salario * 1.14):.2f}")

print('-' * 20)
produto = float(input("Digite o preço do produto: R$"))
print('-' * 20)
print(f"Este produto com um aumento de 10% fica {produto + (produto * (10/100))}")
print('-' * 20)
print(f"Com desconto de 10% fica {produto - (produto * (10/100))}")
print('-' * 20)