from lab_python_fp.field import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'color': None, 'price': 213},
    {'title': None, 'price': 1234}
]

def task1():
    for i in field(goods, 'title'):
        print(i)

    for i in field(goods, 'title', 'color'):
        print(i)


def main():
    task1()


if __name__ == '__main__':
    main()
