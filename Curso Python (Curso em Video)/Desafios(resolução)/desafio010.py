print("Quantos doláres você pode comprar com reais?")
print("-"*20)
real = float(input("Quantos reais você tem na carteira? "))
dolar = real / 5.29

print(f"Com R${real} daria pra comprar ${dolar:.2f}")