from typing import List

Vector = List[int]

height_weight_age = [
    70,
    170,
    40
]

grades = [
    95,
    80,
    75,
    62,
]

# function that returns the sum of two vectors
def add_vectors(v_1: Vector, v_2: Vector) -> Vector:
    """Sum the corresponding elements"""
    # testing if the vectors are not empty
    assert v_1,"The vector cant be empty, if youre trying to sum them"
    assert v_2,"The vector cant be empty, if youre trying to sum them"

    # testing if the vectores has the same lenght
    assert len(v_1) == len(v_2), "The two vectors it has to be the same lenght"

    # return the sum of the two vectors
    return [v_1 + v_2 for v_1, v_2 in zip(v_1,v_2)] # sum two vectors

# function that returns the subtract of two vectors
def subtract_vectors(v_1: Vector, v_2: Vector) -> Vector:
    assert len(v_1) == len(v_2), "The two vectors it has to be the same lenght"
    return [v_1 - v_2 for v_1, v_2 in zip(v_1,v_2)] # subtract the two vectors # example: [1,2,3] - [1,2,3] = [0,0,0]

assert add_vectors(v_1=[1,2,3],v_2=[3,2,1]) == [4,4,4], "The function its now working"
assert subtract_vectors(v_1=[5,5,9],v_2=[1,2,3]) == [4,3,6], "the function its now working"



def sum_vectors(vectors: List[Vector]) -> Vector:

    assert vectors, "the vectors should not be empty"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "The vectors should have the same size if you wanna sum them"
    
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)] #

assert sum_vectors([[1,2], [1,2], [1,2]]) == [3,6], "the function itsnt working"

def scalar_multiply(scalar: float, vector: Vector) -> float:
    
    # vector * scalar = (x_1 * scalar , y_1 * scalar) 
    # vector_1 ·  vector_2 = (x_1 * x_2 + y_1 * y_2) 

    assert scalar, "scalar it empty"
    assert vector, "Vector its empty"

    return [element * scalar for element in vector]

assert scalar_multiply(scalar=2, vector=[10,2,3]) == [20,4,6],"the function its not working"
print(scalar_multiply(scalar=2, vector=[10,2,3]))

def mean_vector(vectors: List[Vector]) -> float:
    assert vectors, "Vectors its empty"
    n = len(vectors)
    return scalar_multiply(1/n, sum_vectors(vectors)) # example: v_1 = (1,2); v_2 = (4,3);  v_1 + v_2 = (1 + 4, 3 +2)   mean_vector =  (5/(1/n) + 5(1/n))
    
print(mean_vector([[10,5,5], [10,5,5], [10,5,5]]))


def dot_product(v_1: Vector, v_2: Vector) -> float:
    
    """
    v_1 · v_2 = (x_1 * y_1 + x_2 * y_2)
    """

    assert v_1, "v_1 its empty"
    assert v_2, "v_2 its empty"

    return sum(el_v1 * el_v2 for el_v1, el_v2 in zip(v_1, v_2))

print(dot_product([1,2],[1,2]))

def sum_of_squares(vector: Vector) -> float:
    """
        el_v1 * el_v1 + el_v2 * el_v2
    """
    return dot_product(vector,vector)

assert sum_of_squares([1,2,3]) == 14 # 1 * 1 + 2 * 2 + 3 * 3 = 14

import math

def magnitude(vector: Vector) -> float: # find the module
    """Return the magnitude (or the length)"""
    return math.sqrt(sum_of_squares(vector))

assert magnitude([3,4]) == 5, "the function or the value is not right" 

def squared_distance(vector1: Vector, vector2: Vector) -> float:
    """C"""
    return sum_of_squares(subtract_vectors(vector1, vector2))

assert squared_distance([7,5], [5,3]) == 8, "something went wrong"

def distance(v: Vector, w: Vector) -> float:
    """Computa a distancia entre v e w"""
    return math.sqrt(squared_distance(v, w))

# a function more clean
def distance(v: Vector, w: Vector) -> float: # 
    """Computa a distancia entre v e w"""
    return magnitude(subtract_vectors(v, w))

print(distance([10,24,32],[1,3,8]))


#--------Matrix------------

Matrix = List[List[float]]

A = [
    [1,2,3],     # A tem 2 linhas e 3 colunas
    [4,5,6], 
]

B = [
    [1,2],      # B tem 3 linhas e 2 colunas
    [3,4],
    [5,6],
]

from typing import Tuple

def shape(A: Matrix) -> tuple[int, int]:
    """Retorna (numero de linhas A e numeros de colunas de A)"""
    num_rows = len(A)
    num_col = len(A[0]) if A else 0
    return num_rows, num_col

assert shape(A=A) == (2,3) # 2 rows, 3 collumns


def get_row(A: Matrix, index: int) -> Vector:
    """Retorna a linha index de A (como um vetor)"""
    return A[index] # A[i] já está na linha i

def get_collumn(A: Matrix, index: int) -> Vector:
    """Retorna a coluna j de A (como um vetor)"""
    return [A_i[index] 
            for A_i in A]

print(get_collumn(A=A, index=1))

from typing import Callable

def make_matrix(num_cols: int,
                num_rows: int,
                entry_fn: Callable[[int,int], float])-> Matrix:
    """
    Retorna uma matrix num_rows x num_cols 
    cuja entrada (i, j) é entry_fn(i, j)
    """
    return [[entry_fn(j, i)
             for j in range(num_cols)
             ] for i in range(num_rows)] 


def identity_matrix(n: int) -> Matrix:
    """Retorna a Matrix de indentidade n x n"""
    return make_matrix(num_cols=n, num_rows=n, entry_fn= lambda i,j: 1 if i == j else 0)

print(identity_matrix(n=5,))

assert identity_matrix(n=5) == [[1, 0, 0, 0, 0], 
                                [0, 1, 0, 0, 0], 
                                [0, 0, 1, 0, 0], 
                                [0, 0, 0, 1, 0], 
                                [0, 0, 0, 0, 1]]

for indice, numero in enumerate([1,2,3,4,5,1,2,3]):
    print(indice, numero)