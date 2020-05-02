import unittest
import object_to_json


class Person(object):
    def __init__(self):
        self.name = "Andrew"
        self.surname = "Black"


class TestObjectJson(unittest.TestCase):

    def test_to_json(self):
        person = Person()
        self.assertEqual(object_to_json.to_json(person), "{\"name\": \"Andrew\", \"surname\": \"Black\"}")

    def test_get_object_by_id(self):
        obj = [1, 2, 3]
        self.assertEqual(object_to_json.objects_by_id(id(obj)), obj)

    def test_get_values(self):
        self.assertEqual(object_to_json.get_values([1, 2]), "1, 2", "Error here")




if __name__ == "__main__":
    unittest.main()
