goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': None, 'color': 'white', 'price': None},
    {'title': None, 'price': 1234}
]


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        return (item[args[0]] for item in items if args[0] in item.keys() and item[args[0]] is not None)
    return [
        {key: val for key, val in item.items() if val is not None}
        for item in items if item.keys() & args and any(i is not None for i in item.values())
    ]


if __name__ == '__main__':
    for i in field(goods, 'title'):
        print(i)

    for i in field(goods, 'title', 'price'):
        print(i)
