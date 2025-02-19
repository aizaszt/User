from datetime import datetime
class User:
    def __init__(self, user_id, name, surname, email, password, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.birthday = birthday

    def get_details(self):
        return f'ID: {self.user_id} Name: {self.name} Surname: {self.surname} Email:{self.email}'

    def get_age(self):
        today = datetime.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age
