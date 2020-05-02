def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            print("[ Decorator works ]")
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def adding(first_number, second_number):
    return int(first_number) + int(second_number)


def main():
    counter = 0
    while counter < 3:
        first_number = counter
        second_number = counter
        counter += 1
        print(first_number, "+", second_number, "=", adding(first_number, second_number))

    counter = 0

    while counter < 5:
        first_number = counter
        second_number = counter
        counter += 1
        print(first_number, "+", second_number, "=", adding(first_number, second_number))


if __name__ == '__main__':
    main()
