
class Vector(object):
    def __init__(self, size, *user_coordinates):
        self.size = int(size)
        self.coordinates = []
        for index in range(size):
            self.coordinates.append(int(user_coordinates[0][index]))

    def __add__(self, other):
        sum_coordinates = []
        for index in range(self.size):
            sum_coordinates.append(self.coordinates[index] + other.coordinates[index])
        return Vector(self.size, sum_coordinates)

    def __str__(self):
        vector_string = "("
        for index in range(self.size):
            vector_string += str(self.coordinates[index])
            if index != self.coordinates.__len__() - 1:
                vector_string += ", "
        vector_string += ")"
        return vector_string

    def __mul__(self, other):
        result_coordinates = []
        result = 0
        if isinstance(other, int):
            for index in range(self.size):
                result_coordinates.append(self.coordinates[index] * other)
            return Vector(self.size, result_coordinates)
        if isinstance(other, Vector):
            for index in range(self.size):
                result += self.coordinates[index] * other.coordinates[index]
            return result

    def __sub__(self, other):
        result_coordinates = []
        for index in range(self.size):
            result_coordinates.append(self.coordinates[index] - other.coordinates[index])
        return Vector(self.size, result_coordinates)

    def __eq__(self, other):
        for index in range(self.size):
            if self.coordinates[index] != other.coordinates[index]:
                return False
        return True

    def __len__(self):
        return self.size

    def __index__(self, other):
        return self.coordinates[other-1]


def input_coordinates(vector_size, vector_number):
    coordinates = []
    print("\nInput coordinates for " + str(vector_number) + " vector:\n")
    for i in range(int(vector_size)):
        coordinate = input(str(i + 1) + ": ")
        coordinates.append(coordinate)
    return coordinates


def show_info(first_vector, second_vector):
    string = ("\nFirst vector: " + str(first_vector) + "\t" + "Second vector: " + str(second_vector))
    return string


def main():
    while True:
        vector_size = int(input("Input vector's sizes: "))
        if vector_size <= 0:
            print("Repeat input [ size <= 0]")
        else:
            break

    first_vector = Vector(vector_size, input_coordinates(vector_size, 1))
    second_vector = Vector(vector_size, input_coordinates(vector_size, 2))
    while True:
        show_info(first_vector, second_vector)
        operation = input("\nChoose operation:\n" +
                          "1. Sum vectors\n" +
                          "2. Minus vectors\n" +
                          "3. Multiple const\n" +
                          "4. Multiple vectors\n" +
                          "5. Compare vectors\n" +
                          "6. Length of vectors\n" +
                          "7. By Index\n" +
                          "8. Exit\n")
        operation = int(operation)
        if operation == 1:
            print("\n", first_vector, " + ", second_vector, " = ", first_vector + second_vector)
        elif operation == 2:
            print("\n", first_vector, " - ", second_vector, " = ", first_vector - second_vector)
        elif operation == 3:
            constant = int(input("Input a constant: "))
            print("\n", first_vector, " * ", constant, " = ", str(first_vector * constant), "\t",
                  second_vector, " * ", constant, " = ", str(second_vector * constant))
        elif operation == 4:
            print("\n", first_vector, " * ", second_vector, " = ", first_vector * second_vector)
        elif operation == 5:
            if first_vector == second_vector:
                print("\n", first_vector, " == ", second_vector)
            else:
                print("\n", first_vector, " != ", second_vector)
        elif operation == 6:
            print("\nThe length of ", first_vector, " vector = ", first_vector.__len__(), "\n")
            print("\nThe length of ", second_vector, " vector = ", second_vector.__len__(), "\n")
        elif operation == 7:
            index = int(input("Input an index: "))
            print("\nThe coordinate in first vector", first_vector.__index__(index), "\n")
            print("\nThe coordinate in second vector", second_vector.__index__(index), "\n")
        elif operation == 8:
            quit()


if __name__ == "__main__":
    main()
