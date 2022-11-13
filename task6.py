login = input("Введите логин: ")
urlogin = ["Kirill"]


def checker():
    check1 = True
    if login not in urlogin:
        check1 = False
    return check1


def validate():
    i = 0
    while i > 4:
        validator = ["#", "$", "%", "&"]
        if validator[i] in login:
            return
        else:
            check2 = False
        return check2
    i = i + 1


def register():
    if checker() == False and validate() == False:
        urlogin.append(login)
        print("Вы зарегистрировались, добро пожаловать")
    else:
        print("В вашем имени содержатся недопустимые символы или уже зарегистрированы")


register()