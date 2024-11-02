print("-" * 20)
carteira = float(input("Quando dinheiro você tem na carteira? R$"))

print("-" * 20)
print(f"Com R${carteira} você compraria US${(carteira / 5.37):.2f}")
print("-" * 20)
print(f"Com R${carteira} você compraria €{(carteira / 5.78):.2f}")
print("-" * 20)