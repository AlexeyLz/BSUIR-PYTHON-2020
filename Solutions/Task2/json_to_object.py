import object_to_json
from object_to_json import Person


def from_json(json_string):
    python_object = {}
    index = 0
    while index < json_string.__len__():
        if (json_string[index] == "\"" and json_string[index - 1] == "{") or \
                (json_string[index] == "\"" and json_string[index - 2] == ","):
            attribute = json_string[index + 1:json_string.find("\"", index + 1)]
            opening_commas_index = json_string.find(":", index) + 2
            if json_string[opening_commas_index] == "{":
                closing_commas_index = json_string.find("}", opening_commas_index) + 1
            elif json_string[opening_commas_index] == "[":
                closing_commas_index = json_string.find("]", opening_commas_index) + 1
            else:
                closing_commas_index = json_string.find(", ", index)
            value = json_string[opening_commas_index:closing_commas_index]
            if is_number(value):
                value = int(value)
            elif value == "true":
                value = True
            elif value == "false":
                value = False
            elif value == "null":
                value = None
            elif value.find("{") > -1:
                value = from_json(value[value.find("{"):value.find("}") + 1])
            elif value.find("[") > -1:
                result = []
                value = value[1:-1]
                value = value.split(",")
                for item in value:
                    item = item.replace(" ", "")
                    if is_number(item):
                        result.append(int(item))
                value = result
            elif value.find("\"") > -1:
                value = value.replace("\"", "")

            python_object[attribute] = value
            index = closing_commas_index
        index += 1
        if index == 0:
            return python_object

    return python_object


def is_number(string):
    for char in string:
        if char < "0" or char > "9":
            return False
    return True


def main():
    person = Person()
    # print("Python: ", person.__dict__)
    print("JSON string:     ", object_to_json.to_json(person))
    print("Python's custom: ", from_json(object_to_json.to_json(person)))


if __name__ == "__main__":
    main()
