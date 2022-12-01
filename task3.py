from abc import ABC, abstractmethod

class Stationery(ABC):

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        print("Рисуем")


class Pen(Stationery):

    def __init__(self, color):
        super().__init__(title = 'Ручка')
        self.color = "Синяя"

    def draw(self):
        print("Ручка пишет")


class Pencil(Stationery):

    def draw(self):
        print("Карандаш пишет")



class Handle(Stationery):

    def draw(self):
        print("Маркер пишет")



pen1 = Pen("Ручка")
pencil1 = Pencil("Карандаш")
handle1 = Handle("Маркер")


print(pen1.title, pen1.color), pen1.draw()
print(pencil1.title), pencil1.draw()
print(handle1.title), handle1.draw()