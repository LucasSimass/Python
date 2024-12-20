from random import randint 
from collections import Counter

def portasEscolhas(usuario_decisao):
    portas = [0,0,0] # cria as portas 
    portas[randint(0,2)] += 1 # escolhe aleatoriamente uma porta e adiciona o premio

    porta_premiada = [index + 1 for index, value in enumerate(portas) if value == 1] # retorna a porta premiada, exemplo: porta 1, porta 2 ou porta 3

    print(porta_premiada)

    print("Um mago lhe diz que em uma das portas a um prêmio e nas outras a uma morte dolorosa, escolha sabiamente")
    print("Você só pode escolher a porta 1, 2 ou 3")

    usuario_porta = 3 - 1 # a porta que ele escolher não fara diferença por isso o usuario sempre escolhera a 2 porta

    print(f"Você escolheu a porta {usuario_porta + 1}")
    print("O mago lhe diz que ele retirara uma das portas...")

    print(portas)
    for index, value in enumerate(portas):
        if value != 1 and usuario_porta != index:
            print(f"A porta {index + 1} foi retirada")
            portas.pop(index)
            print(portas)
            print("O mago lhe diz se vc quer continuar na porta que vc deseja, ou quer mudar para a outra porta restante")
            # dentro dos parametros o jogador já decide se quer ou nao mudar a porta
            if usuario_decisao == "s":
                for index, value in enumerate(portas):
                    if portas[index] != portas[usuario_porta - 1]:
                        usuario_porta = index 
                if portas[usuario_porta] == 1: return "acertou"
                else: return "errou"
            elif usuario_decisao == "n":
                if portas[usuario_porta - 1] == 1: return "acertou"
                else: return "errou"
            break

trocou = [portasEscolhas("s") for i in range(1000)]
nao_trocou = [portasEscolhas("n") for i in range(1000)]

print(Counter(trocou))
print(Counter(nao_trocou))