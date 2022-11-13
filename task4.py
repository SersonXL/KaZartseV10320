
def get_password():
    password = input("Введите ваш пароль: ")
    hasher = hash(password)
    return hasher


print(get_password())
