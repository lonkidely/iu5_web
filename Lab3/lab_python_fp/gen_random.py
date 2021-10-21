from random import randint
from lab_python_fp.print_task import print_task


def gen_random(num_count, min_value, max_value):
    return (randint(min_value, max_value) for i in range(num_count))


@print_task
def task2():
    for i in gen_random(10, 1, 5):
        print(i, end=" ")
    print()
