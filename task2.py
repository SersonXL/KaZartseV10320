from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, coefficient):
        self.coefficient = coefficient

    def __add__(self, other):
        return f'Общий расход ткани: {(self.coefficient / 6.5 + 0.5) + (2 * other.coefficient + 0.3)}'

    @abstractmethod
    def my_metod(self):
        pass


class Coat(Clothes):
    @property
    def expenses(self):
        return f'Расход ткани для пальто: {self.coefficient / 6.5 + 0.5}'

    def my_metod(self):
        print("ббб")

class Costume(Clothes):
    @property
    def expenses(self):
        return f'Расход ткани для костюма: {2 * self.coefficient + 0.3}'

    def my_metod(self):
        print("ббб")

coat1 = Coat(10)
costume = Costume(100)
print(coat1 + costume)
print(coat1.expenses)
print(costume.expenses)
coat1.my_metod()