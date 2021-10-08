from itertools import chain


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        return (item[args[0]] for item in items if args[0] in item.keys() and item[args[0]] is not None)
    return [
        {key: val for key, val in item.items() if val is not None}
        for item in items if item.keys() & args and any(i is not None for i in item.values())
    ]
