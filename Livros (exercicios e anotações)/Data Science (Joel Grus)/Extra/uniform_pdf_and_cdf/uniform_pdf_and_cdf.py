def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0

print(uniform_pdf(.2))

def uniform_cdf(x:float) -> float:
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

import math 

SQRT_TWO_PI = math.sqrt(2 * math.pi)    # return the sqrt of 2 * π

def normal(x: float, mu: float = 0, sing: float = 1) -> float:
    pass

print(math.pi)
print(math.exp(2)) # return e * 2
