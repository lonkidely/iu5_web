def print_task(task):
    def wrapper():
        print()
        print(task.__name__)
        return task()

    return wrapper
