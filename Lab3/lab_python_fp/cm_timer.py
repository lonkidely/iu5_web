from time import time
from time import sleep
from contextlib import contextmanager
from lab_python_fp.print_task import print_task


class cm_timer_1:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time()
        print("time: {}".format(self.end_time - self.start_time))


@contextmanager
def cm_timer_2():
    start_time = time()
    yield
    end_time = time()
    print("time: {}".format(end_time - start_time))


@print_task
def task6():
    with cm_timer_1():
        sleep(1.0)
    with cm_timer_2():
        sleep(1.0)
