class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def view(self):
        print("Я - User. Могу просматривать содержимое")


class Moderator(User):

    def __init__(self, group_id):
        super().__init__("login123", "password123")
        self.group_id = group_id

    def view(self):
        print("Я - Moderator. Могу просматривать содержимое")

    def redact(self):
        print("Я - Moderator. Могу редактировать содержимое")


user1 = User
moder1 = Moderator(12345)
print(user1.view)
print(moder1.login, moder1.password, moder1.group_id)
moder1.view()
moder1.redact()
