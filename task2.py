class MyException(Exception):
    pass


def check():
    name = input("Введите свой слово ")
    if name.isalpha() == False:
        raise MyException
    else:
        print("Ваше слово ", name)


check()
