num = int(input("Digite um número para ver sua tabuada: "))
contador = 1

print("-"*20)
while contador < 10:
    print(f"{num} x {contador} = {num * contador}")
    contador += 1
print("-"*20)