class Cat:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def say_meow(self):
        print("мяу")

    def say_mya(self):
        print("мурлык")

    def jump(self):
        print("прыг")

    def print_full_info(self):
        print("кот по имени ",self.name)
        print("с покрасом: ",self.color)
        print("которому ",self.age," лет")


cat1 = Cat("Шейд", "черный", 5)

cat1.print_full_info()
cat1.say_meow()
cat1.say_mya()
cat1.jump()
