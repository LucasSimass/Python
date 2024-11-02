import random

contagem = 0

ganhos = 0

perdas = 0

questoes = 5

while contagem <= 5: 
    n1 = random.randint(0,100)
    n2 = random.randint(1,100)

    Bigbrother = random.randint(1,2)

    questoes -= 1
    contagem += 1


    if questoes < 1:
        Bigbrother = 0
        print("O jogo acabou!")
        print("-" * 20)

    if Bigbrother == 1 and Bigbrother != 2:
        print(f"{n1} + {n2} = ?")
        resultado = n1 + n2
        resposta = int(input("Digite a resposta: "))
        print("-" * 20)
        if resposta == resultado:
            print(f"Você acertou, parabéns!!")
            ganhos += 1 
        else:
            print(f"A resposta era {resultado}, você perdeu!")
            perdas += 1
        print(f"Você tem mais {questoes} questões!")
        print("-" * 20)
    
    if Bigbrother == 2:
        print(f"{n1} - {n2} = ?")
        resultado = n1 - n2
        resposta = int(input("Digite a resposta: "))
        print("-" * 20)
        if resposta == resultado:
            print(f"Você acertou, parabéns!!")
            ganhos += 1  
        else:
            print(f"A resposta era {resultado}, você perdeu!")
            perdas += 1
        print(f"Você tem mais {questoes} questões!")
        print("-" * 20)


print(f"Você acertou {ganhos} vezes!")
if perdas > 0:
    print(f"Você errou {perdas} vezes!")
else:
    print("Você errou nenhuma vez!")
print("-" * 20)