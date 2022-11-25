def validator():
    try:
        a = int(input("Введите число, которое будет возведенно в квадрат "))
        b = a * a
    except ValueError:
        print("Ошибка, введенено не число!")

    else:
        print(b)


validator()
