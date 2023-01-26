"""A Calculator"""


class Calculator():
    """Basic Calculator capable, of addition, subtraction, multiplication, division, as well as rounding to a specified decimal point."""

    def __init__(self, number_1 = 1, number_2 = 1, mode = 1, round_to = 1):
        """
        Attr:
        - n_1(int)         Number_1
        - n_2(int)         Number_2
        - mode(int):       Specifies operation to be carried out
        - round_to(int):   Decimal places to be rounded to
        - res(float):      Result
        """
        self.n_1 = number_1
        self.n_2 = number_2
        self.mode = mode
        self.round_to = round_to
        self.res = 0

    @property
    def n_1(self):
        return self.__n_1

    @n_1.setter
    def n_1(self, value):
        self.__n_1 = int(value) 

    @property
    def n_2(self):
        return self.__n_2

    @n_2.setter
    def n_2(self, value):
        self.__n_2 = int(value)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = int(value)

    @property
    def round_to(self):
        return self.__round_to

    @round_to.setter
    def round_to(self, value):
        self.__round_to = int(value)

    def addition(self):
        self.res = self.n_1 + self.n_2

    def subtraction(self):
        self.res = self.n_1 - self.n_2

    def multiplication(self):
        self.res = self.n_1 * self.n_2

    def division(self):
        self.res = self.n_1 / self.n_2

    def round(self):
        self.res = round(self.res, self.round_to)
