# usaremos um conceito de aleatoriedade numeral, e quais numeros serão chamados 
from random import randint

def verifyingRandom(numbers_quantity):
    for i in range(max_numbers):
        the_chosen_number1 = randint(min_numbers,max_numbers) # chosee a number between 0 and 1000
        the_chosen_number2 = randint(min_numbers,max_numbers) # chosee a number between 0 and 1000
        numbers_quantity[the_chosen_number1 + the_chosen_number2] += 1 


max_numbers = 10000000 # minimum number possible to be chosen
min_numbers = 0 # maximum number possible to be chosen

numbers_quantity = {i:0 for i in range(max_numbers + max_numbers)} # output -> {1:0, 2:0, 3:0, 4:0...} | coment: we´re checking if the numbers was called in the random numbers, if it was we add 1+ into the value of the key, for example: random number is 7, so 7:1...

verifyingRandom(numbers_quantity)

for i in numbers_quantity:
    if numbers_quantity[i] > 6:
        print(f"{i}: {numbers_quantity[i]}")
