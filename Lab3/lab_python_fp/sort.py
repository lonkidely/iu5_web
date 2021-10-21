from lab_python_fp.print_task import print_task


@print_task
def task4():
    data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

    result = sorted(data, key=abs, reverse=True)
    print(result)

    result_with_lambda = sorted(data, key=lambda val: abs(val), reverse=True)
    print(result_with_lambda)
