import inspect
import gc


class Person(object):
    def __init__(self):
        self.name = "Alex"
        self.surname = "Brown"
        self.age = 45
        self.numbers = [80291234567, 80449876543]


def to_json(obj):
    if not isinstance(obj, (set, tuple, dict, list,)):
        attributes_dictionary = obj.__dict__
        attributes_list = list(attributes_dictionary)
        json_string = "{"
        for item in attributes_dictionary:
            if not inspect.ismethod(item):
                json_string += "\""
                json_string += str(item)
                json_string += "\": "
                attribute = getattr(obj, item)
                if isinstance(attribute, (set, tuple, dict, list,)):
                    json_string += "["
                    json_string += get_values(attribute)
                    if item != attributes_list[attributes_list.__len__() - 1]:
                        json_string += "], "
                    else:
                        json_string += "]}"
                elif isinstance(attribute, str):
                    json_string += "\""
                    if item != attributes_list[attributes_list.__len__() - 1]:
                        json_string += str(attribute)
                        json_string += "\", "
                    else:
                        json_string += str(attribute)
                        json_string += "\"}"
                else:
                    json_string += str(attribute)
                    if item != attributes_list[attributes_list.__len__() - 1]:
                        json_string += ", "
                    else:
                        json_string += "}"
    else:
        json_string = "["
        for object in obj:
            json_string += to_json(object)
            if object is not obj[obj.__len__() - 1]:
                json_string += ","
        json_string += "\n]"
    return json_string


def get_values(obj):
    obj = list(obj)
    values = ""
    for item in obj:
        values += str(item)
        values += ", "
    values = values[:values.__len__() - 2]
    return values


def objects_by_id(id_):
    for obj in gc.get_objects():
        if id(obj) == id_:
            return obj


def main():
    person = Person()
    print("JSON: ", to_json(person))


if __name__ == "__main__":
    main()
