import math

def area(r):
    '''Принимает число r (радиус окружности) и возвращает площадь окружности'''
    if not isinstance(r, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif r <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return math.pi * r * r
    


def perimeter(r):
    '''
    Возвращает периметр окружности.

        Параметр:
            r (int/double): радиус окружности

        Возвращаемое значение:
            perimetr_circle (int/double): число - периметр окружности
    '''
    if not isinstance(r, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif r <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return 2 * math.pi * r
    
