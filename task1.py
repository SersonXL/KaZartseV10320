class animal():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def print_full_info(self):
        print("Имя ", self.name)
        print("Цвет ", self.color)
        print("Возраст ", self.age)


class Cat(animal):
    def __init__(self, say):
        self.say = say
        super().__init__('Shade', 'black', '4')


class Dog(animal):
    def __init__(self, say):
        self.say = say
        super().__init__('Jormungand', 'brown', '2')


animal1 = Cat('meow')
animal2 = Dog('woof')
animal1.print_full_info()
print(animal1.say)
animal2.print_full_info()
print(animal2.say)
