altura = float(input("Altura da parede em metros: "))
largura = float(input("Largura da parede em metros: "))

area_parede = altura * largura

# Supondo que 1L de tinta pode pintar 2m quadrados da parede
tinta_area_litros = area_parede / 2

print("-" *20)

print(f"A area da parede é de {area_parede} metros quadrados!")

print("-" *20)

print(f"Supondo que 1L de tinta pode pintar 2m quadrados da parede, seria necessario {tinta_area_litros}L de tinta!")
print("-" *20)