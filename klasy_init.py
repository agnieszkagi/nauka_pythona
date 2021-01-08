import datetime

class User:
    """jest wywolywana przy kazdym stworzeniu obiektu
"""
    def __init__(self, full_name, birthday): #metoda inicjalizacja (konstruktor)
        self.name = full_name
        self.birthday = birthday #yyymmdd

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        """Zwraca wiek Użytkownika w latach."""
        today = datetime.date(2021, 1, 9)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

user = User("John Smith", "19931112")


print(user.name)
print(user.birthday)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())
