from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle
import emoji


def main():
    rect = Rectangle(21, 21, "синего")
    circ = Circle(21.0, "зеленого")
    sq = Square(21, "красного")

    print(rect)
    print(circ)
    print(sq)

    print(emoji.emojize(':thumbs_up:'))


if __name__ == '__main__':
    main()
