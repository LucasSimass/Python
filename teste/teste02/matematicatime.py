numeros = (1,2,3,4,5,8,2,4,1,5,6,7,3,2,9,10,15,1000)
contagem = 0

for item in numeros:
    contagem += item

media = contagem / len(numeros)

print(media)


nome = "João"
idade = 15
sexo = "M"

nome = {"nome":nome,"idade":idade,"sexo":sexo}

print(nome)
