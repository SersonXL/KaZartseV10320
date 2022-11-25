import re


class phone:
    def get_phone(self):
        urphone = "8(982)123-4546"
        rez = re.search(r"(?P<country>\+?\d)(?:\(?\-?)(?P<city>\d{3})(?:\)?\-?)(?P<station>\d)(?:\)?\-?)(?P<number>\d{2}\-?\d{2}\-?\d{2})", urphone)
        self.country = rez.group("country")
        self.city = rez.group("city")
        self.station = rez.group("station")
        self.number = rez.group("number")

    def print_number(self):
        print("country =", self.country, "city =", self.city, "station =", self.station, "number =", self.number)



tomsphone = phone()
tomsphone.get_phone()
tomsphone.print_number()


