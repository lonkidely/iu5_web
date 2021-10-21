import sys
import math


def is_coef_correct(index, coef):
    try:
        num = float(coef)
    except ValueError:
        return False
    if num == 0.0 and index == 1:
        return False
    return True


def get_coef(index, message):
    try:
        coef = sys.argv[index]
    except IndexError:
        print(message)
        coef = input()
        while not (is_coef_correct(index, coef)):
            print("Введенный коэффициент некорректен, введите другой")
            coef = input()
    return float(coef)


def get_roots(a, b, c):
    roots = []

    d = b * b - 4.0 * a * c
    if d < 0.0:
        return
    if d == 0.0:
        root = -b / (2.0 * a)
        if root == 0.0:
            roots.append(0)
        elif root > 0.0:
            roots.append(math.sqrt(root))
            roots.append(-math.sqrt(root))
    else:
        sqrt_d = math.sqrt(d)
        first_root = (-b + sqrt_d) / (2.0 * a)
        second_root = (-b - sqrt_d) / (2.0 * a)
        if first_root == 0 or second_root == 0:
            roots.append(0)
        if first_root > 0.0:
            roots.append(math.sqrt(first_root))
            roots.append(-math.sqrt(first_root))
        if second_root > 0.0:
            roots.append(math.sqrt(second_root))
            roots.append(-math.sqrt(second_root))

    return roots


def main():
    a = get_coef(1, "Введите значение коэффициента A")
    b = get_coef(2, "Введите значение коэффициента B")
    c = get_coef(3, "Введите значение коэффициента C")

    roots = get_roots(a, b, c)
    cnt_roots = 0

    try:
        cnt_roots = len(roots)
    except TypeError:
        print("Корней нет!")
        return

    if cnt_roots == 0:
        print("Корней нет!")
    else:
        print("Корни данного уравнения:")
        for root in roots:
            print(root, end=" ")
        print()


if __name__ == '__main__':
    main()
