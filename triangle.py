def area(a, h): 
    '''
    Возвращает площадь треугольника:
        Параметр: 
            a (int/double): основание треугольника
            h (int/double): высота треугольника

        Возвращаемое значение: 
            area_triangle (int/double): площадь треугоьника
    '''
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0 or h <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        return a * h / 2

def perimeter(a, b, c): 
    '''Принимает числа a, b ,c (стороны треугольника) и возвращает периметр этого треугольника'''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('The function accepts only float values as input')
    elif a <= 0 or b <= 0 or c <= 0:
        raise ValueError('The function accepts only positive values as input')
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError('The triangle inequality is not satisfied')
        else:
            return a + b + c
        
