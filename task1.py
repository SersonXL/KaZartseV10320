class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname


    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def surname(self):
        return self.__surname

    @age.setter
    def age_changer(self, new_age):
        self.__age = new_age
        return self.__age


p = Person('Томас', 23, 'Паровозов')
print(p.name, p.age, p.surname)
p.age_changer = 25
print(p.age)
