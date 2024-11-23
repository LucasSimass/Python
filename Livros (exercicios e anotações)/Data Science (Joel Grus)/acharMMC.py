from collections import Counter

def acharMMC(x: int, y: int) -> None:
    xs = [x * i for i in range(1,101)]
    ys = [y * i for i in range(1,101)]

    for x,y in zip(xs,ys):
        print(x,y)
        if ys.count(x) == 1:
            return f"Encontrando o MMC: {x} == {ys[ys.index(x)]}"

print(acharMMC(8,12))