from random import randint


def gen_random(num_count, min_value, max_value):
    return (randint(min_value, max_value) for i in range(num_count))


if __name__ == '__main__':
    for i in gen_random(10, 1, 5):
        print(i, end=" ")
    print()
