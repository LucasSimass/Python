lista = [1500,1200,1900,300]
def valor_total_info(valor): 
    if valor > 1200:
        imposto1 = valor *0.2        
    else:
        imposto1 = valor * 0.1            
    imposto2 = valor * 0.3
    imposto3 = valor * 0.2
    imposto_total = imposto1 + imposto2 + imposto3  
    return imposto_total

for valor in lista:
    imposto_total = valor_total_info(valor)
    print(f"R${valor} deve se pagar R${imposto_total} de imposto")

