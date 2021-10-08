from lab_python_fp.field import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'color': None, 'price': 213},
    {'title': None, 'price': 1234}
]


def main():
    for i in field(goods, 'title'):
        print(i)

    for i in field(goods, 'title', 'color'):
        print(i)


if __name__ == '__main__':
    main()
