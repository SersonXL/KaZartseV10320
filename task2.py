class Father():

    def __init__(self, surname, name):
        self.name = surname
        self.color = name


class Child(Father):

    def __init__(self, patronim):
        super().__init__('Паравозов', 'Аркадий')
        self.patronim = patronim


person = Child("Томасович")
print(person.name, person.color, person.patronim)
