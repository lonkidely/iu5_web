class FigureColor:

    def __init__(self):
        self.__color = None

    @property
    def colour(self):
        return self.__color

    @colour.setter
    def colour(self, color_param):
        self.__color = color_param
