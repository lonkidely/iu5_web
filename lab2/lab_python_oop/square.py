from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    figure_type = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.figure_type

    def __init__(self, side_len_param, color_param):
        self.side = side_len_param
        super().__init__(self.side, self.side, color_param)

    def __repr__(self):
        return '{} {} цвета со стороной {}. Площадь равна {}.'.format(
            Square.get_figure_type(),
            self.color.colour,
            self.side,
            self.square()
        )
