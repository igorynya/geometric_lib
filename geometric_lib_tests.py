import unittest
import rectangle, circle, square, triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area_1(self):
       with self.assertRaises(ValueError) as e:
            rectangle.area(10, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_zero_area_2(self):
       with self.assertRaises(ValueError) as e:
            rectangle.area(0, 10)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
       
    def test_zero_area_3(self):
       with self.assertRaises(ValueError) as e:
            rectangle.area(0, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
       

    def test_negative_area_1(self):
        with self.assertRaises(ValueError) as e:
            rectangle.area(-10, 10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_negative_area_2(self):
        with self.assertRaises(ValueError) as e:
            rectangle.area(10, -10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_negative_area_3(self):
        with self.assertRaises(ValueError) as e:
            rectangle.area(-10, -10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_zero_perimeter_1(self):
       with self.assertRaises(ValueError) as e:
            rectangle.perimeter(10, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_zero_perimeter_2(self):
       with self.assertRaises(ValueError) as e:
            rectangle.perimeter(0, 10)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
       
    def test_zero_perimeter_3(self):
       with self.assertRaises(ValueError) as e:
            rectangle.perimeter(0, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])


    def test_negative_perimeter_1(self):
        with self.assertRaises(ValueError) as e:
            rectangle.perimeter(-10, 10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_negative_perimeter_2(self):
        with self.assertRaises(ValueError) as e:
            rectangle.perimeter(10, -10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_negative_perimeter_3(self):
        with self.assertRaises(ValueError) as e:
            rectangle.perimeter(-10, -10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])


    def test_type_argument_area_1(self):
        with self.assertRaises(TypeError) as e:
            rectangle.area(10, 'a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_type_argument_area_2(self):
        with self.assertRaises(TypeError) as e:
            rectangle.perimeter('abc', 'a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_type_argument_area_3(self):
        with self.assertRaises(TypeError) as e:
            rectangle.perimeter('abc', 100)
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    
    def test_type_argument_perimeter_1(self):
        with self.assertRaises(TypeError) as e:
            rectangle.perimeter(10, 'a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_type_argument_perimeter_2(self):
        with self.assertRaises(TypeError) as e:
            rectangle.perimeter('abc', 'a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_type_argument_perimeter_3(self):
        with self.assertRaises(TypeError) as e:
            rectangle.perimeter('abc', 100)
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])


    def test_rectangle_area_1(self):
       res = rectangle.area(10, 10)
       self.assertEqual(res, 100)

    def test_rectangle_area_2(self):
       res = rectangle.area(2, 3)
       self.assertEqual(res, 6)
    
    def test_rectangle_area_3(self):
       res = rectangle.area(3, 2)
       self.assertEqual(res, 6) 

    def test_rectangle_area_4(self):
       res = rectangle.area(239, 1)
       self.assertEqual(res, 239) 

    def test_rectangle_area_5(self):
       res = rectangle.area(119.5, 2)
       self.assertEqual(round(res, 0), 239) 


    def test_rectangle_perimeter_1(self):
       res = rectangle.perimeter(10, 10)
       self.assertEqual(res, 40)

    def test_rectangle_perimeter_2(self):
       res = rectangle.perimeter(2, 3)
       self.assertEqual(res, 10)
    
    def test_rectangle_perimeter_3(self):
       res = rectangle.perimeter(3, 2)
       self.assertEqual(res, 10) 

    def test_rectangle_perimeter_4(self):
       res = rectangle.perimeter(69.5, 50)
       self.assertEqual(res, 239) 


class CircleTestCase(unittest.TestCase):

    def test_zero_area_1(self):
       with self.assertRaises(ValueError) as e:
            circle.area(0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
       

    def test_negative_area_1(self):
        with self.assertRaises(ValueError) as e:
            circle.area(-10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_zero_perimeter_1(self):
       with self.assertRaises(ValueError) as e:
            circle.perimeter(0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])


    def test_negative_perimeter_1(self):
        with self.assertRaises(ValueError) as e:
            circle.perimeter(-10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_type_argument_area_1(self):
        with self.assertRaises(TypeError) as e:
            circle.area('a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])


    def test_type_argument_perimeter_1(self):
        with self.assertRaises(TypeError) as e:
            circle.perimeter('a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])


    def test_circle_area_1(self):
        res = circle.area(10)
        self.assertEqual(round(res, 7), 314.1592654)

    def test_circle_area_2(self):
        res = circle.area(1)
        self.assertEqual(round(res, 9), 3.141592654)

    def test_circle_perimeter_1(self):
        res = circle.perimeter(10)
        self.assertEqual(round(res, 7), 62.8318531)

    def test_circle_perimeter_2(self):
        res = circle.perimeter(1)
        self.assertEqual(round(res, 9), 6.283185307)


class SquareTestCase(unittest.TestCase):
    def test_zero_area_1(self):
       with self.assertRaises(ValueError) as e:
            square.area(0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
       

    def test_negative_area_1(self):
        with self.assertRaises(ValueError) as e:
            square.area(-10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_zero_perimeter_1(self):
       with self.assertRaises(ValueError) as e:
            square.perimeter(0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])


    def test_negative_perimeter_1(self):
        with self.assertRaises(ValueError) as e:
            square.perimeter(-10)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_type_argument_area_1(self):
        with self.assertRaises(TypeError) as e:
            square.area('a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])


    def test_type_argument_perimeter_1(self):
        with self.assertRaises(TypeError) as e:
            square.perimeter('a')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_square_area_1(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_circle_area_2(self):
        res = square.area(12)
        self.assertEqual(res, 144)

    def test_circle_perimeter_1(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_circle_perimeter_2(self):
        res = square.perimeter(239)
        self.assertEqual(res, 956)

    def test_circle_perimeter_3(self):
        res = square.perimeter(59.75)
        self.assertEqual(round(res, 0), 239)



class TriangleTestCase(unittest.TestCase):

    def test_zero_area_1(self):
       with self.assertRaises(ValueError) as e:
            triangle.area(0, 1)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_zero_area_2(self):
       with self.assertRaises(ValueError) as e:
            triangle.area(1, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_negative_area_1(self):
        with self.assertRaises(ValueError) as e:
            triangle.area(-2, 3)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    
    def test_negative_area_2(self):
        with self.assertRaises(ValueError) as e:
            triangle.area(3, -9)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_zero_perimeter_1(self):
       with self.assertRaises(ValueError) as e:
            triangle.perimeter(0, 3, 9)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_zero_perimeter_2(self):
       with self.assertRaises(ValueError) as e:
            triangle.perimeter(2, 0, 9)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_zero_perimeter_3(self):
       with self.assertRaises(ValueError) as e:
            triangle.perimeter(2, 3, 0)
       self.assertEqual("The function accepts only positive values as input", e.exception.args[0])


    def test_negative_perimeter_1(self):
        with self.assertRaises(ValueError) as e:
            triangle.perimeter(-2, 3, 9)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_negative_perimeter_2(self):
        with self.assertRaises(ValueError) as e:
            triangle.perimeter(2, -3, 9)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])

    def test_negative_perimeter_3(self):
        with self.assertRaises(ValueError) as e:
            triangle.perimeter(2, 3, -9)
        self.assertEqual("The function accepts only positive values as input", e.exception.args[0])
    

    def test_type_argument_area_1(self):
        with self.assertRaises(TypeError) as e:
            triangle.area("239", "top")
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])


    def test_type_argument_perimeter_1(self):
        with self.assertRaises(TypeError) as e:
            triangle.perimeter('2', '3', '9')
        self.assertEqual("The function accepts only float values as input", e.exception.args[0])

    def test_ineq_of_triangle_1(self):
        with self.assertRaises(ValueError) as e:
            triangle.perimeter(2, 3, 9)
        self.assertEqual("The triangle inequality is not satisfied", e.exception.args[0])
    
    def test_ineq_of_triangle_2(self):
        with self.assertRaises(ValueError) as e:
            triangle.perimeter(9, 2, 3)
        self.assertEqual("The triangle inequality is not satisfied", e.exception.args[0])

    def test_triangle_area_1(self):
        res = triangle.area(10, 2)
        self.assertEqual(res, 10)

    def test_triangle_area_2(self):
        res = triangle.area(239, 2)
        self.assertEqual(res, 239)

    def test_triangle_area_3(self):
        res = triangle.area(1, 1)
        self.assertEqual(res, 0.5)

    def test_triangle_perimeter_1(self):
        res = triangle.perimeter(10, 20, 25)
        self.assertEqual(res, 55)

    def test_triangle_perimeter_2(self):
        res = triangle.perimeter(1, 2, 2.5)
        self.assertEqual(round(res, 1), 5.5)

    def test_triangle_perimeter_3(self):
        res = triangle.perimeter(23.9, 23.9, 23.9)
        self.assertEqual(round(res, 1), 71.7)

    def test_triangle_perimeter_4(self):
        res = triangle.perimeter(79.66, 79.66, 79.66)
        self.assertEqual(round(res, 0), 239)
    


