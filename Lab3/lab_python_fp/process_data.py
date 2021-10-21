import json
import sys
from lab_python_fp.field import field
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.print_result import print_result
from lab_python_fp.gen_random import gen_random
from lab_python_fp.print_task import print_task

path = "./data_light.json"

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


@print_task
def task7():
    with cm_timer_1():
        f4(f3(f2(f1(data))))
