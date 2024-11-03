#--------LEARNING ABOUT FUNCTIONS------------

# Create a function with only  a print(message), by default the message is "Default message"
def my_print(message = "Default message"):
    print(message)

my_print("Olá mundo!")
my_print()


# A function that create a full name based on the first and last name of the user 
def full_name(first = "[First name not found]", last = "[Last name not found]"):
    return first + " " + last
    
print(full_name(first="Lucas",last="Simas"))
print(full_name())

# you can add multilines if you use """ """
multi_line_strings = """you can have...
multiple lines...
of string"""

first_name = "Lucas"
last_name = "Simas"

the_full_name = f"{first_name} {last_name}"
print(the_full_name)


def sum_and_product(x,y):
    return (x + y), (x * y)

sp = sum_and_product(2,3) 
print(sp)
s, p = sum_and_product(5,10)
print(s,p)

#--------LEARNING ABOUT LIST------------

# a list with only integers
integer_list = [1,2,3]

# you can add any type of value in a list (most of languages is only possible if you declare that the list can receive any values)
heterogenous_list = ["String", 0.1, True, 1, [32,43]]

# Create a matriz with 3 collums and 3 rows 
easy_reader_list = [
    [4,2,1],
    [4,5,6],
    [1,9,2],
]

for i in [1,2,3,4,5]:
    print(i)


some = [1,3,4]
some2 = [5,7,9]

print(sum(some))
print (1 in [32,41])

some.extend(some2) # o some recebe todos as listas que se extenderão

print(some)

lista_add = [123,421,52] + [312,567,87]

print(lista_add)

verdadeiro, falso = [True, False] # o verdadeiro recebe o True e o falso recebe False

print(verdadeiro, falso)

#--------LEARNING ABOUT DICT AND TRY/EXCEPT------------

from collections import defaultdict, Counter

dict_list = defaultdict(list)
counter = Counter(
    "123"
)

try:
    print(0/0)
except ZeroDivisionError:
    print("cannot divide by zero")


my_tuple = (1,42)

try:
    my_tuple[1] = 14
except TypeError:
    print("cannot modify tuple")


nomes = {
    "Jhon": "Jhon",
    "Lucas": "Lucas",
    "Pedro": "Pedro"
}

nome_escolhido = "joao".capitalize() 

try:
    print(nomes[nome_escolhido])
except TypeError:
    print("Nome Não Encontrado")
except KeyError:
     print("Nome Não Encontrado")

nome_get = nomes.get("joao", 0) # caso não encotre a chave ele retornara 0
nome_get2 = nomes.get("mucas") # caso não encotre a chave ele retornara None

print(nome_get)

#--------LEARNING ABOUT SET------------
s = set() # we create a map that doesnt have keys, so we cant search for a value indivualy, but in the other hand it´s pretty fast and can help when we wanna find and manipulate a huge amount of data
s.add(1) # {1}
s.add(2) # {1,2}
s.add(4) # {1, 2, 4}

print(s)

words_list = ["aba", "Para", "Stop", "zoo"]

print("aba" in words_list) # wrong way (more slower)

words_set = set(words_list)

print("aba" in words_set) # right way (more faster)

words_list = list(words_list) # podemos converter novamente em uma lista

even_odds = "even" if 3 % 2  == 0 else "Odds" # criamos uma linha com condição 
 
print(even_odds)

for x in range(10):
    if x == 3:
        continue
    if x == 5:
       break 
    print(x)

x = None 

# O assert para o programa e as String da direita irão avisar o sinal de erro
assert x == None, "Forma não pythonica de escrever"
assert x is None, "X é igual a none (forma correta de escrever)"

print(all([1,True,1])) # if ALL of them it´s not false it will return True else return false
print(any([0,False,1])) # if ANY of them it´s true it will return True else return false

print("-" * 20)

print(all([]))
print(any([]))

x = [421,5,1,4,5,7,15,66,32,763]

y = sorted(x) # the sorted return the list organized by the lower value to the higher value 
x.sort() # the sort change directly the main list

print(x)

x = sorted([-4,1,3,-2], key=abs, reverse=True)

print(x)

def word_count(document):
    return Counter(
        document
    )


document = "You are my sunshine, my sweet heart , my baby, my manager, my prostitute, my pussy, maaaaa whatever"

print(word_count(document=document))

word_count_dict  = {}

for word in document:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else: 
        word_count_dict[word] = 1 


word_count_dict  = {}

for word in document:
    previous_count = word_count_dict.get(word, 0)
    word_count_dict[word] = previous_count + 1

print(word_count_dict)

wc = sorted(word_count_dict.items(), key=lambda word_count: word_count[1],reverse=True)

print(wc)

tweet = {
    "user": "Lucas Simas",
    "tweet": "What a good day to be alive",
    "location": "Brazil",
    "dataTime": "6:32"
}


tweet_keys = tweet.keys()
print(tweet_keys)
tweet_values = tweet.values()
print(tweet_values)
tweet_items = tweet.items()
print(tweet_items)

from collections import defaultdict # it´s like a dict but if we dont have the value or the key that we want he create one, very usefull

dd_list = defaultdict(list) # the type of the values that we gone convert or receive
dd_list[2].append(1) # the numbers we can append

dd_dict = defaultdict(dict) # the type of the values that we gone convert or receive
dd_dict["State"]["Rio de Janeiro"] = "Petropolis" # we create the keys and put a value with the '=' operator
print(dd_dict)

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1
print(dd_pair)

dobro = lambda x: x * 2

print(dobro(2))

c = Counter([1,3,5,1,5,6,23,5])

print(c)

even_numbers = [x for x in range(5) if x % 2 == 0 ] # in a range of 5 find the even numbers
print(even_numbers)

squares_by_x = [x * x for x in range(5)] # find the square of x 
print(squares_by_x)

even_squares = [x * x for x in range(5) if x in even_numbers]
print(even_squares)

square_dict = {x: x for x in range(5)}
print(square_dict)

square_set = {1,2,3}

zeros = [0 for _ in even_numbers] # each _ it will be equal to 0, so the output will be: [0,0,0] bc the even numbers has a lenght of 3

print(zeros)

pairs = [(x, y) 
for x in range(10)
for y in range(10)
]

print(pairs)

increasing_pairs = [
    (x,y) 
    for x in range(10)
    for y in range(x + 1,10)
]

print(increasing_pairs)


assert True == True, "Erro improvavel" # o assert para o codigo intantaneamente caso a condição for falsa ou gere um erro

# o try coleta a operação e caso ela possua um erro podemos tratar os dados sem que a execução do programa seja interrompida
try: 
    print(0/0)
except ZeroDivisionError:
    print("Você não pode dividir algo por 0")

print("O codigo acima msm tendo um erro, não finalizou a execução do codigo")

# search for the smallest item in the items
def smallest_item(items):
    assert items, "The List of items is empty" # we are checking if the list is empty, if it´s true we stop the execution of the program
    return min(items) # return the smallest number

list_words= ["opa","bom dia", "aaaaaaaaaaaaa", "ab"] # return the one that is most close to 'A'

list_numbers = [4,1,2,5,67,15,6,135,-1]

assert smallest_item(list_numbers) == -1, "The smallest number in the list is not -1"

#Create a class called Cachorro
class Cachorro:
    """
    Class: Cachorro (dog)

    atributes:
        name: the dog will receive a name
        years: the dog will receive there years
        race:  the dog will receive a race

    function Latir: it will print a ("Ruf")
    function aniversario: it will increase the years by +1 
    """

    def __init__(self, name = "[Name not Found]", years = "[Years not Found]", race= "[Race not Found]"):
        self.name = name
        self.years = years
        self.race = race
        print(f"his name is {self.name}") 
        print(f"his years is {self.years}")
        print(f"his race is {self.race}")
    

    def latir(self):
        print("Ruf")
    
    def aniversario(self):
        self.years = self.years + 1 
        print(f"Now he has {self.years}")


print("-" * 20)

dog1 = Cachorro(name="Raquina", years=3, race="Bulldog")

dog1.latir()
dog1.aniversario()
print(dog1.years)

print("-" * 20)

# Creates a class
class CountingClicker:
    def __init__(self, count=0):
        self.count = count

    def __addOne(self): # private Method
        return self.count + 1 
    
    def click(self, clicks=1):
        """every time you use the function click it will add one to count by default"""
        self.count += clicks

    def read(self): # read the count value 
        return self.count
    
    def reset(self):
        self.count = 0
        print("Count Reseted Successfuly")
    

print(CountingClicker(0).count)
print(CountingClicker(100).count)
print(CountingClicker(count=100).count)


clicker = CountingClicker()

assert clicker.read() == 0, "the Clicker Count it should be 0 by default"

clicker.click()
clicker.click()

assert clicker.read() == 2, "the CLICK its not working properly"

clicker.reset()

assert clicker.read() == 0, "The RESET its not working properly"



# we extend the class CountingClicker extending a class gives us all of the class and we can use and modify in the class that we have (everything we do in the class that we are receiving the extend, it will not modify the class that we are extending)
class NoResetCliker(CountingClicker): 
    def reset(self):
        pass

clicker2 = NoResetCliker()

assert clicker2.read() == 0, "The clicker2 by default should be 0"

clicker2.click()

assert clicker2.read() == 1, "The clicker method is not working"

clicker2.reset()

assert clicker2.read() == 1, "It shouldn be working the reset in that case"



# the generator every time reach the yield send the data to the for tool that we are using, the non-generators only send after the function finish all the calculation
def generate_range(n):
    i = 0
    while i < n:
        yield i 
        i += 1

for i in generate_range(10):
    print(f"i: {i}")




def infinite_and_beyond():
    """ Return 1,2,3... """
    n = 1
    while True:
        yield n
        n += 1
        if n == 100:
            break

for i in infinite_and_beyond():
    print(i)
    if i == 100:
        break

print("Oi")

# create a generator that we can only acess the values in a for tool, the generator only generate numbers, but dont armazene it 
even_below20 = (i for i in generate_range(20) if i % 2 == 0)

for i in even_below20:
    print(i)


data = infinite_and_beyond()

evens = [x for x in data if x % 2 == 0]

even_square = (x ** 2 for x in evens) 

even_square_ending_in_six = (x for x in even_square if x % 10 == 6)

names = ["Lucas", "Pedro", "Leonidas", "Jhon"]

# not Pythonic way
for name in range(len(names)):
    print(f"the index {name} is {names[name]}")

# Not Pythonic way
i = 0
for name in names:
    print(f"the index {i} is {names[i]}")
    i += 1

print("-" * 20)

# Pythonic way
for index ,name in enumerate(names): # enumete gives us the index and the value at the same time we just need to call eachother
    print(f"the index {index} is {name}")

#--------LEARNING ABOUT Random------------

import random

random.seed(10) # sempre obteremos os mesmos resultados (ajua na consistencia)

uniform_randoms = [random.random() for _ in range(5)]

print(uniform_randoms) # [0.5714025946899135, 0.4288890546751146, 0.5780913011344704, 0.20609823213950174, 0.81332125135732]

random.seed(10) # sempre caira no msm numero se colocaros o msm numero da ssed
print(random.random()) # 0.5714025946899135
random.seed(10)
print(random.random()) # 0.5714025946899135

print(random.randrange(1,10)) # 7
print(random.randrange(3,6)) # 4

up_to_ten = [i for i in range(1,11)] #[1,2,3,...10]

print(up_to_ten)
random.shuffle(up_to_ten) # shuffle it (change all the positions to a random position in the lenght) 
print(up_to_ten) # [5, 6, 9, 2, 3, 7, 8, 4, 1, 10]

my_best_friend = random.choice(["Lucas", "Pedro", "Leonidas", "Maria"])
print(my_best_friend) # Leonidas

lotterry_numbers = range(60)

winning_numbers = random.sample(lotterry_numbers, 6) 
print(winning_numbers) #  [4, 15, 47, 23, 2, 26]

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)

#--------LEARNING ABOUT RE------------

import re

re_examples = [               # All of them will return True 
    not re.match("a", "cat"), # it will return true bc "cat" doesnt start with "a"
    bool(re.search("a", "cat")), # it will retunr true bc "cat" contains "a"
    not re.search("c", "dog"), # it will return true bc it doesnt have a "c" in "dog" 
    3 == len(re.split("[ab]", "carbs")), # divide in "a" or "b" to ["c","r","s"]
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # it wil cjamge the numbers to "-"
 ]

print(re_examples)

assert all(re_examples), "At least one of the values is not true" # verifying if all the values is true, if dont it will stop runing the program

# re.match verifica se o INICIO corresponde ao dado inicial
# bool(re.search) verifica se a os dados corresponde ao dado prosposto

#--------LEARNING ABOUT Zip------------

list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]
print([pair for pair in zip(list1,list2)]) # [('a',1), ("b", 2), ("c", 3)]

pair = [('a', 1), ('b', 2), ('c', 3)]

letters, numbers = zip(*pair)
print(letters, numbers) # ('a', 'b', 'c') (1, 2, 3)

unziped = zip(*pair)
print(list(unziped)) # [('a', 'b', 'c'), (1, 2, 3)]

letters,numbers = zip(("a",1),("b",4),("c",5)) # we need to variables to get the value of tuple[x][0] and tuple[x][1]

print(letters, numbers) # ('a', 'b', 'c') (1, 4, 5)

def add(a,b): return a + b

print(add(1,3)) # 4

try:
    add([1,2])
except TypeError:
    print("add expects two inputs")

add(*[1,2]) #output: 3 ||| with the "*" we unpack the list and now the add will receive 1 and 2

print([1,2]) # [1,2]
print(*[1,2]) # 1 2

x,a = [*[1,2]]

print(x,a) # 1 2

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g 

def f1(x):
    return x + 1

g = doubler(f1)

assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

def f2(x,y):
    return x + y
g = doubler(f2)

try:
    g(1,2)
except TypeError:
    print("as defined, g only takes one argument")

#--------LEARNING ABOUT * and **------------

def magic(*args, **kwargs):
    print("Unnamed args: ", args)
    print("Keyword args: ", kwargs)

magic(1,2, key="word", key2="word2", key3= "word3") #Unnamed args:  (1, 2)
                                                    #Keyword args:  {'key': 'word', 'key2': 'word2', 'key3': 'word3'}   

def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1,2]
z_dict = {"z":3}

assert other_way_magic(*x_y_list, **z_dict) == 6, "1 + 2 + 3 should be equal to 6" # **z_dict == z=3

def double_correct(f):
    """funciona para qualquer entrada recebida por f"""
    def g(*args, **kwargs):
        """Todo argumento fornecido para g deve ser transmitido para f"""
        return 2 * f(*args, **kwargs)
    return g 

g = double_correct(f2)

print(g(*[1,2]))

assert g(1,2) == 6, "Doubler should work now"


def astericos(*args, **kwargs):
    print("Argumentos posicionais: ", args ) # argumentos que podem ser colocados em uma posição
    print("Argumentos nomeados: ", kwargs ) # argumentos que já possuem uma nomeação, exemplo: nome="lucas", idade=18

astericos(69,31,42,idade=18,nome="Pedro") # os argumnentos precisam estar dividos entre posicionais e nomeados

#--------LEARNING ABOUT ADDING------------

def add(a, b):
    return a + b

assert add(10,5) == 15, "+ is valid for numbers"
assert add([1,3,4], [32,41,2]) == [1,3,4,32,41,2], "+ is valid for lists"
assert add("Hello ", "World!") == "Hello World!", "+ is valid for strings"

try:
    add(10, "Five")
except TypeError:
    print("cannot add an int to a string" )


#--------LEARNING ABOUT DECLARE TYPE OF VALUES IN PARAMETERS AND FUNCTIONS RETURN------------

def add(a: int, b: int) -> int: # declaring that the 2 values should be integer and the return it has to be integer as well
    return a + b

try:
    add(a=1,b=2)
except TypeError:
    print("Use integer not String in that function")

print(add(a=10,b=5)) # this should be ok

print(add(a=10,b=5)) # this should NOT be ok

def doc_product(a: list, b: list) -> float: # that a GOOD way for documentation and readable code
    pass

def doc_product(a,b): # that NOT a good way for documentation and readable code
    pass

def lista(xs:list[int]) -> int: # when we declare what type of value we are working with he wil provide the tools for this type, in this example the function knows that the value is gone be a list so he provide the list tool like the clear() in this example
    xs.clear()

from typing import List

def total(xs: List[float]) -> float:
    return sum(xs)

print(total([1,2,3,4]))



from typing import Optional

x: int = 1 # declamos que o valor que x recebe sera inteiro

lista_inteiro: list[int] = [] # uma lista que ira receber numeros inteiros 

best_so_far: Optional[float] = None # recebera um possivel valor nulo

#--------LEARNING ABOUT Dict, Iterable, Tuple declares------------

from typing import Dict, Iterable, Tuple

counts: Dict[str, int] = {"data": 1, "science": 1}
if True:
    even: Iterable[int] = (x for x in range(10) if x % 2 == 0)

print(even)

triple: Tuple[int,float,int] = (10, 2.3, 5)


from typing import Callable

def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ",".join(n_copies)

print(twice(comma_repeater, "type hints")) # the comma_repeater receive two values the "type hints" and the value 2

Number = int
Numbers = List[int]

def total(xs: Numbers) -> Number:
    return sum(xs)