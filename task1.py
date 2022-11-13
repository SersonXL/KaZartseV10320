import math


def engineer():
    sign = int(input("Выберите операцию: 1. квадратный корень, 2. возведение в степень "))
    if sign == 1:
        a = int(input("Введите число "))
        print(math.sqrt(a))
    if sign == 2:
        a = int(input("Введите число "))
        b = int(input("Введите степень "))
        print(math.pow(a, b))
    else:
        print("ошибка")


engineer()
