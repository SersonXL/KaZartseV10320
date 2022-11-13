def get_login():
    ulogin = input("Введите ваш логин: ")
    return ulogin


def get_password():
    password = input("Введите ваш пароль: ")
    hasher = hash(password)
    return hasher


print(get_login())
print(get_password())
