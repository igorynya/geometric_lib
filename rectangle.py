
def area(a, b): 
    '''Принимает числа a и b (стороны прямоугольника) и возвращает площадь прямоугольника'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0 or b <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return a * b

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника.

        Парметры:
            a (int/double): первая сторона прямоугольника
            b (int/double): вторая сторона прямоугольника

        Возвращаемое значение:
            perimetr_rectangle (int/double): число - периметр прямоугольника
    '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0 or b <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return 2 * (a + b)
