from lab_python_fp.print_task import print_task


class Unique(object):
    def __init__(self, items, **kwargs):
        self.used = set()
        self.data = items
        self.current_index = 0

        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        while True:
            if self.current_index == len(self.data):
                raise StopIteration
            current_item = self.data[self.current_index]
            self.current_index += 1

            if self.ignore_case and current_item.lower() not in self.used:
                self.used.add(current_item.lower())
                return current_item

            if not self.ignore_case and current_item not in self.used:
                self.used.add(current_item)
                return current_item

    def __iter__(self):
        return self


@print_task
def task3():
    data = [1, 1, 2, 2, 1, 2, 1, 2, 2, 1]
    for val in Unique(data):
        print(val, end=" ")
    print()

    data = ['a', 'A', 'b', 'B', 'ab', 'aB', 'Ab', 'AB']

    for val in Unique(data):
        print(val, end=" ")
    print()

    for val in Unique(data, ignore_case=True):
        print(val, end=" ")
    print()
