import re


def find_email():
   result = re.findall(r'\w+@\w+.\w+',"Всем привет! Меня зовут Алексей. Мой email: alexVB@gmail.com. Привет, Алексей! Меня зовут Марина, моя почта: Marina@mail.ru'")
   print(result)


find_email()