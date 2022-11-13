def security():
    name = list(input("Введите ваш текст "))
    for i in range(len(name)):
        name[i] = "*"

    print(name)
