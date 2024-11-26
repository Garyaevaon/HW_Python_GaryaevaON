S = int(input("Введите размер одной стороны квадрата (только цифры): "))

import math

def square(S):
    return math.ceil (S*S)

result = square(S)
print(result)