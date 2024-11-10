import enum
from random import choice, seed

# The Enum is a set typed of values enumerateds that let your code more descriptive and readable

class Kid(enum.Enum):
    Boy = 0
    Girl = 1
    
def random_kid() -> Kid:
    return choice([Kid.Boy, Kid.Girl])

both_girls = 0
older_girl = 0
either_girl = 0

seed(0)

for _ in range(10000):
    younger = random_kid()

    older = random_kid()
    if older == Kid.Girl:
        older_girl += 1
    if older == Kid.Girl and younger == Kid.Girl:
        both_girls += 1
    if older == Kid.Girl or younger == Kid.Girl:
        either_girl += 1 

print(f"P(both | older): {both_girls / older_girl}") # 0.5007089325501317 ~ 1/2
print(f"P(both | either): {both_girls / either_girl}") # 0.3311897106109325 ~ 1/3