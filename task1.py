class Batary():
    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def __str__(self):
        return '[' + ''.join(self.capacity) +']'

    def charge(self):
        if len(self.capacity) >= self.max_charge:
            print("Полностью заряжен")
        else:
            self.capacity.append('(')

    def discharge(self):
        try:
            self.capacity.pop(0)
        except IndexError:
            print("Полностью разряжен")

bat1 = Batary()
bat1.charge()
bat1.charge()
bat1.charge()
bat1.discharge()
bat1.charge()
bat1.charge()
bat1.discharge()
bat1.discharge()
print(bat1)
