
def area(a):
    '''
    Возвращает площадь квадрата.

        Параметр:
            a (int/double): сторона квадрата

        Возвращаемое значение:
            area_square (int/double): площадь квадрата
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return a * a


def perimeter(a):
    '''Принимает число a (сторона квадрата) и возвращает площадь квадрата'''
    if not isinstance(a, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return 4 * a
