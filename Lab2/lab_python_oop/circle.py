from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from math import pi


class Circle(Figure):
    figure_type = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, radius_param, color_param):
        self.radius = radius_param
        self.color = FigureColor()
        self.color.colour = color_param

    def square(self):
        return pi * self.radius * self.radius

    def __repr__(self):
        return '{} {} цвета с радиусом длины {}. Площадь равна {}.'.format(
            Circle.get_figure_type(),
            self.color.colour,
            self.radius,
            self.square()
        )
