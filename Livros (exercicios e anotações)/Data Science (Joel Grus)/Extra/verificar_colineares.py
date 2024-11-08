def verificadore_colineares(x: tuple[float,float], y: tuple[float,float]) -> bool:
    return True if x[0] / y[0] == x[1] / y[1] else False 

x = (1,3)
y = (2,2)

print(verificadore_colineares(x,y))