import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math

import rectangle 
import circle 
import square 
import triangle 

import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res,100)

    def test_rectangle_mul2(self):
        res = rectangle.area(5,4)
        self.assertEqual(res,20)
    def test_rectangle_per(self):
        res = rectangle.perimeter(20,40)
        self.assertEqual(res,120)
        
class SquareTestCase(unittest.TestCase):
    def test_zero_square(self):
        res = square.area(0)
        self.assertEqual(res,0)
        
    def test_square_area(self):
        res = square.area(15)
        self.assertEqual(res,225)
        
    def test_square_perimeter(self):
        res = square.perimeter(20)
        self.assertEqual(res,80)

class TriangleTestCase(unittest.TestCase):
    def test_zero_triangle(self):
        res = triangle.area(10,0)
        self.assertEqual(res,0)
        
    def test_triangle_area(self):
        res = triangle.area(10,4)
        self.assertEqual(res,20)
        
    def test_triangle_perimeter(self):
        res = triangle.perimeter(10,11,12)
        self.assertEqual(res,33)
        
    def test_triangle_perimeter(self):
        res = triangle.perimeter(100,120,100)
        self.assertEqual(res,320)
        
class SircleTestCase(unittest.TestCase):
    def test_zero_sircle(self):
        res = circle.area(0)
        self.assertEqual(res,0)
        
    def test_area_sircle(self):
        res = circle.area(4)
        self.assertEqual(res,16*math.pi)

    def test_perimeter_sircle(self):
        res = circle.perimeter(10)
        self.assertEqual(res,20*math.pi)

if __name__ == '__main__':
    unittest.main()