class Good:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calc(self):
        print("стоимость товара", self.price * self.weight)


apple = Good("apple", 100, 1.5)
apple.calc()
pear = Good('pear', 120, 0.8)
pear.calc()
