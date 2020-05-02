import unittest
import class_vector



class TestVectorClass(unittest.TestCase):

    def test_show_info(self):
        first_vector = (3, 5)
        second_vector = (2, 3)
        string = ("\nFirst vector: " + "(3, 5)" + "\t" + "Second vector: " + "(2, 3)")
        self.assertEqual(class_vector.show_info(first_vector,second_vector), string)

    def setUp(self):
        self.first_vector = class_vector.Vector(2, [1, 1])
        self.second_vector = class_vector.Vector(2, [2, 2])

    def test_add(self):
        self.assertEqual(self.first_vector.__add__(self.second_vector), class_vector.Vector(2, [3, 3]))

    def test_mul(self):
        self.assertEqual(self.first_vector.__mul__(self.second_vector), 4)

    def test_sub(self):
        self.assertEqual(self.second_vector.__sub__(self.first_vector), class_vector.Vector(2, [1, 1]))

    def test_str(self):
        self.assertEqual(self.first_vector.__str__(), "(1, 1)")
