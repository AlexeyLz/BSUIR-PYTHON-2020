import unittest
import decorator


class DecoratorTest(unittest.TestCase):

    def test_decorator(self):
        self.assertEqual(decorator.adding(2, 2), 4)

    def test_adding(self):
        self.assertEqual(decorator.adding(268, -68), 200)


if __name__ == "__main__":
    unittest.main()