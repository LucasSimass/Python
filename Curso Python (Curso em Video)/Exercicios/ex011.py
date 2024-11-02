print('-'*20)
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura

print('-'*20)
print(f"A área da parede({largura}x{altura}) é {area}m².")
print('-'*20)
print(f"Considerando que 1L de tinta cobre 2m², você precisaria de {area / 2}L de tinta.")
print('-'*20)