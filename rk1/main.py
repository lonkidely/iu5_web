from functools import reduce


class Operator:
    def __init__(self, id, name, count_cycles, lang_id):
        self.id = id
        self.name = name
        # количество тактов процессора на выполнение
        self.count_cycles = count_cycles
        self.id_lang = lang_id


class ProgrammingLanguage:
    def __init__(self, id, title):
        self.id = id
        self.title = title


class OperatorOfProgrammingLanguages:
    def __init__(self, oper_id, lang_id):
        self.oper_id = oper_id
        self.lang_id = lang_id


languages = [
    ProgrammingLanguage(1, 'C - классика жанра'),
    ProgrammingLanguage(2, 'C++ - лучший язык в мире'),
    ProgrammingLanguage(3, 'C# - язык для студентов 2 курса ИУ5'),
    ProgrammingLanguage(4, 'Java - язык для души'),
    ProgrammingLanguage(5, 'Rust - глоток свежего воздуха'),
    ProgrammingLanguage(6, 'Swift - любителям яблок посвещается')
]

operators = [
    Operator(1, '!', 100, 1),
    Operator(2, '&&', 200, 2),
    Operator(3, '||', 200, 3),
    Operator(4, '<<', 50, 2),
    Operator(5, '+', 170, 5),
    Operator(6, '-', 170, 6),
    Operator(7, '*', 510, 4),
    Operator(8, '/', 315, 3),
    Operator(9, '&', 70, 1),
    Operator(10, '^', 90, 2),
    Operator(11, '|', 80, 1),
]

operators_of_languages = [
    OperatorOfProgrammingLanguages(1, 2),
    OperatorOfProgrammingLanguages(1, 6),
    OperatorOfProgrammingLanguages(1, 3),
    OperatorOfProgrammingLanguages(2, 2),
    OperatorOfProgrammingLanguages(2, 3),
    OperatorOfProgrammingLanguages(3, 4),
    OperatorOfProgrammingLanguages(3, 3),
    OperatorOfProgrammingLanguages(4, 1),
    OperatorOfProgrammingLanguages(4, 6),
    OperatorOfProgrammingLanguages(5, 2),
    OperatorOfProgrammingLanguages(5, 5),
    OperatorOfProgrammingLanguages(6, 4),
    OperatorOfProgrammingLanguages(6, 4),
    OperatorOfProgrammingLanguages(7, 2),
    OperatorOfProgrammingLanguages(7, 3),
    OperatorOfProgrammingLanguages(8, 6),
    OperatorOfProgrammingLanguages(8, 1),
    OperatorOfProgrammingLanguages(9, 4),
    OperatorOfProgrammingLanguages(9, 3),
    OperatorOfProgrammingLanguages(10, 2),
    OperatorOfProgrammingLanguages(10, 4),
    OperatorOfProgrammingLanguages(11, 5),
    OperatorOfProgrammingLanguages(11, 2)
]

one_to_many = [
    (o.name, o.count_cycles, l.title)
    for o in operators
    for l in languages
    if o.id_lang == l.id
]

many_to_many_temp = [
    (l.title, ol.lang_id, ol.oper_id)
    for l in languages
    for ol in operators_of_languages
    if ol.lang_id == l.id
]
many_to_many = [
    (o.name, o.count_cycles, title)
    for title, lang_id, oper_id in many_to_many_temp
    for o in operators
    if o.id == oper_id
]


def task1():
    print('Задание Е1')
    used = set()
    for name, count, title in sorted([(name, count, title) for name, count, title in one_to_many if 'язык' in title],
                                     key=lambda val: val[2]):
        if title not in used:
            used.add(title)
            print('{}, имеет следующие операторы:'.format(title))
        print(name)


def task2():
    print('\nЗадание Е2')
    result = sorted([
        (
            l.title,
            sum(cnt for tname, cnt, ttitle in one_to_many if l.title == ttitle),
            reduce(lambda acc, tmp: acc + 1, [name for name, tcnt, ttitle in one_to_many if l.title == ttitle], 0)
        ) for l in languages], key=lambda val: round(val[1] / val[2], 2))

    for items in result:
        print(items[0], round(items[1] / items[2], 2))


def task3():
    print('\nЗадание Е3')
    result = [(
        o.name,
        [title for tname, tcount, title in many_to_many if tname == o.name]
    ) for o in operators if len(o.name) == 2]
    for items in result:
        print('Оператор \"{}\" есть в следующих языках:'.format(items[0]))
        for lang in items[1]:
            print(lang)


def main():
    task1()
    task2()
    task3()


if __name__ == '__main__':
    main()
