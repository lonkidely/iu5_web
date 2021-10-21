def print_result(func):
    def wrapper(*args):
        result = func(*args)
        print(func.__name__)

        if type(result) == list:
            for val in result:
                print(val)
        elif type(result) == dict:
            for key, val in result.items():
                print("{} = {}".format(key, val))
        else:
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
