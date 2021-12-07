from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor


class Rectangle(Figure, FigureColor):
    figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, height_param, width_param, color_param):
        self.height = height_param
        self.width = width_param
        self.color = FigureColor()
        self.color.colour = color_param

    def square(self):
        return self.height * self.width

    def __repr__(self):
        return '{} {} цвета с шириной {} и высотой {}. Площадь равна {}.'.format(
            Rectangle.get_figure_type(),
            self.color.colour,
            self.width,
            self.height,
            self.square()
        )
