import math

def area(r):
    '''Принимает число r (радиус окружности) и возвращает площадь окружности'''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности.

        Параметр:
            r (int/double): радиус окружности

        Возвращаемое значение:
            perimetr_circle (int/double): число - периметр окружности
    '''
    return 2 * math.pi * r

