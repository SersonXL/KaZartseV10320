class Car:
    def __init__(self, color, mark, body, transmision, speed=0, ):
        self.color = color
        self.mark = mark
        self.body = body
        self.speed = speed
        self.transmission = transmision

    def start(self):
        print("Начало движения")
        self.speed = 30

    def stop(self):
        print("Вы приехали, конец движения")
        self.speed = 0

    def turn(self):
        select = input("Выберите в какую сторону повернуть : < - влево, > - вправо ")
        if select == "<":
            print("Машина повернула налево")
        elif select == ">":
            print("Машина повернула направо")
        else:
            print("Это куда?")

    def speed_up(self):
        self.speed = self.speed + 20
        print("Пятку в пол! Машина ускорилась, скорость = ", self.speed)

        if self.body == "Седан" and self.speed > 80:
            print("Скорость превышена! Разрешенная скорость 60 км/ч")
            self.speed = 60

        if self.body == "Грузовик" and self.speed > 60:
            print("Скорость превышена! Разрешенная скорость 60 км/ч")
            self.speed = 60

    def speed_down(self):
        print("Машина замедлилась, скорость ",self.speed)
        self.speed = self.speed - 10
        if self.speed < 0:
            self.speed = 0

    def beep(self):
        print("Бииииип")

    def show_full_info(self):
        print("Машина цвета ", self.color)
        print("Марка машины ", self.mark)
        print("Тип кузова ", self.body)
        print("Спидометр показывает ", self.speed)
        print("Тип коробки передач ", self.transmission)


bmw = Car("Нифертите", "BMW", "Седан", "auto")
bmw.show_full_info()
bmw.start()
bmw.turn()
bmw.speed_up()
bmw.speed_up()
bmw.speed_up()
bmw.speed_down()
bmw.speed_down()
bmw.speed_down()
bmw.speed_down()
bmw.stop()

man = Car("черный", "Man", "Грузовик", "auto")
man.show_full_info()
man.start()
man.turn()
man.speed_up()
man.speed_up()
man.speed_up()
man.speed_down()
man.speed_down()
man.speed_down()
man.stop()

