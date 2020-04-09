import math

class N_Vector:

    def __init__(self, string):
        self._dimension = []
        self._size = 0
        if(type(string) == str):
            for item in string.split(' '):
                self._dimension.append(int(item))
                self._size = self._size + 1
        else:
            print('Неверный формат')

    def multiplication_by_constant(self, const):
        self._dimension = list(map(lambda x : x * const, self._dimension))
        return self._dimension

    def size(self):
        sum = 0
        for item in list(map(lambda x : x * x, self._dimension)):
            sum += item
        return math.sqrt(sum)

    def get_item(self, index):
        return self._dimension[index]

    def sum(self, vector2):
        return list(map(lambda x, y : x + y, self._dimension, vector2._dimension))

    def subtraction(self, vector2):
        return list(map(lambda x, y : x - y, self._dimension, vector2._dimension))

    def multiplication(self, vector2):
        return list(map(lambda x, y: x * y, self._dimension, vector2._dimension))

    def division(self, vector2):
        return list(map(lambda x, y: x / y, self._dimension, vector2._dimension))

    def scalar_product(self, vector2):
        sum = 0
        for item in list(map(lambda x, y: x * y, self._dimension, vector2._dimension)):
           sum += item
        return sum

    def equals(self, vector2):
        if self._dimension == vector2._dimension:
            return True
        return False
