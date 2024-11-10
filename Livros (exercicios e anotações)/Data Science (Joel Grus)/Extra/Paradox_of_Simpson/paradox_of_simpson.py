from math import sqrt

xs = [-2,-1,0,1,2]
ys = [2,1,0,1,2]

def media(xs: list[float]) -> float:
    """Retorna a média"""
    return sum(xs) / len(xs)

def desvio(xs: list[float]) -> list[float]:
    return [x - media(xs) for x in xs]

# identifica a relação entre x e y
# se covariancia > 0, y tende a aumentar quando x aumenta
# se covariancia < 0, y tende a diminuir quando x aumenta
def covariancia(xs: list[float], ys: list[float]) -> float: 
    assert len(xs) == len(ys), "the lists it has to be the same lenght"
    return sum((x - media(xs)) * (y - media(ys)) for x,y in zip(xs,ys)) / (len(xs) - 1)

# se a correlação -1 indica uma forte relação linear e vice-versa, quanto mais distante de um desses numeros mais fraco relação linear é 
def correlacao(xs: list[float], ys: list[float]) -> float: 
    assert len(xs) == len(ys), "the lists it has to be the same lenght"

    x = sum((desvio(xs)[i] ** 2 for i,e in enumerate(xs)))
    y = sum((desvio(ys)[i] ** 2 for i,e in enumerate(ys))) 

    if x > 0 and y > 0:
        return sum(desvio(xs)[i] * desvio(ys)[i]  for i,e in enumerate(xs)) / sqrt(sum(desvio(xs)[i] ** 2 for i,e in enumerate(xs)) * sum(desvio(ys)[i] ** 2 for i,e in enumerate(ys)))
    return 0.0

xs = [1,2,3,4,5]
ys = [50,65,75,80,90]

print(sum((desvio(xs)[i] for i,e in enumerate(xs))))
print(sum((desvio(ys)[i] for i,e in enumerate(ys)))) 

if covariancia(xs,ys) > 0:
    print(f"y tende aumentar quando x aumenta já que covariancia é positiva {covariancia(xs,ys)}")
elif covariancia(xs,ys) == 0:
    print(f"x e y não possui conexão já que covariancia é {covariancia(xs,ys)}")
else:
    print(f"y tende diminuir quando x aumenta já que covariancia é negativa {covariancia(xs,ys)}")

# se correlação for proxima de 1 ou -1 indicia uma forte linearidade do grafico seja para cima(1) ou para baixo(-1)
print(f" {correlacao(xs,ys)}")