import random
import linecache
import time


def merge(left, right, array):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if int(left[i]) < int(right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(array):
    n = len(array)
    if n < 2:
        return

    mid = n // 2
    left = []
    right = []

    for i in range(mid):
        number = array[i]
        left.append(number)

    for k in range(mid, n):
        number = array[k]
        right.append(number)

    merge_sort(left)
    merge_sort(right)

    merge(left, right, array)


def sorting(first_file_line, second_file_line, output_file_path, chunk_size, first_file_line_flag,
            second_file_line_flag, first_input, second_input, numbers_amount):
    while first_file_line < numbers_amount // 2 and second_file_line < numbers_amount // 2:
        f = open(output_file_path, "a")
        first_number = linecache.getline(first_input, first_file_line)
        second_number = linecache.getline(second_input, second_file_line)
        while first_file_line_flag <= chunk_size and second_file_line_flag <= chunk_size:

            if int(first_number) <= int(second_number):
                f.write(str(first_number))
                first_file_line += 1
                first_file_line_flag += 1
                first_number = linecache.getline(first_input, first_file_line)
            else:
                f.write(str(second_number))
                second_file_line += 1
                second_file_line_flag += 1
                second_number = linecache.getline(second_input, second_file_line)

        if first_file_line_flag > chunk_size:
            while second_file_line_flag <= chunk_size:
                second_number = linecache.getline(second_input, second_file_line)
                f.write(str(second_number))
                second_file_line += 1
                second_file_line_flag += 1
        else:
            while first_file_line_flag <= chunk_size:
                first_number = linecache.getline(first_input, first_file_line)
                f.write(str(first_number))
                first_file_line += 1
                first_file_line_flag += 1
        output_file_path = change_output(output_file_path)
        first_file_line_flag = 1
        second_file_line_flag = 1


def change_output(path):
    if path == "1_part.txt":
        return "2_part.txt"
    elif path == "2_part.txt":
        return "3_part.txt"
    elif path == "3_part.txt":
        return "4_part.txt"
    elif path == "4_part.txt":
        return "1_part.txt"


def change_input(path):
    if path == "1_part.txt":
        return "3_part.txt"
    elif path == "2_part.txt":
        return "4_part.txt"
    elif path == "3_part.txt":
        return "1_part.txt"
    elif path == "4_part.txt":
        return "2_part.txt"


def file_fragmentation(numbers_amount, memory_limit):
    file_number = 1
    line = 1
    number_array = []
    while line < numbers_amount:
        number_array.clear()
        for _ in range(0, memory_limit):
            number = linecache.getline("numbers.txt", line)
            number_array.append(number.replace("\n", ""))
            line += 1
        merge_sort(number_array)
        with open(str(file_number) + "_part.txt", "a") as file:
            for lines in number_array:
                file.write(str(lines) + "\n")
        if file_number == 1:
            file_number = 2
        else:
            file_number = 1


def check_amount(numbers_amount):
    if numbers_amount < 0:
        return numbers_amount*(-1)
    else:
        return numbers_amount


def create_file(numbers_amount, left_border, right_border):

    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(left_border, right_border)) for _ in range(numbers_amount))


def main():
    for i in range(1, 5):
        with open(str(i) + "_part.txt", "w"):
            pass

    with open("output.txt", "w"):
        pass

    output_file_path = "3_part.txt"
    numbers_amount = 50000
    numbers_amount = check_amount(numbers_amount);

    left_border = -10000
    right_border = 10000
    memory_limit = numbers_amount // 4
    start_time = time.time()
    create_file(numbers_amount, left_border, right_border)
    file_fragmentation(numbers_amount, memory_limit)

    first_file_line = 1
    second_file_line = 1

    first_input_file_path = "1_part.txt"
    second_input_file_path = "2_part.txt"

    while memory_limit <= numbers_amount:
        if memory_limit == numbers_amount // 2:
            sorting(1, 1, "output.txt", memory_limit, 1, 1, first_input_file_path, second_input_file_path,
                    numbers_amount)
            print("%s seconds" % (time.time() - start_time))
            exit(0)
        else:
            sorting(first_file_line, second_file_line, output_file_path, memory_limit, 1, 1, first_input_file_path,
                    second_input_file_path, numbers_amount)
        first_input_file_path = change_input(first_input_file_path)
        second_input_file_path = change_input(second_input_file_path)
        memory_limit *= 2


if __name__ == "__main__":
    main()