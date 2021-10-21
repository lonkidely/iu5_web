import json
from field import field
from cm_timer import cm_timer_1
from print_result import print_result
from gen_random import gen_random

path = "../data_light.json"

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(set(val.lower() for val in field(arg, 'job-name')), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda val: str.startswith(val, "программист"), arg))


@print_result
def f3(arg):
    return list(map(lambda val: val + " с опытом Python", arg))


@print_result
def f4(arg):
    return [t[0] + t[1] for t in list(
        zip(arg, [(', зарплата ' + str(val) + ' руб.') for val in list(gen_random(len(arg), 100000, 200000))]))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
