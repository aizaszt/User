import re 
import string
from datetime import datetime
import random
from user import User
from userservice import UserService
class UserUtil:


    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.today().year)[2:]
        random_digits = ''.join(random.choices(string.digits, k=7)
        return year_prefix + random_digits

   
    @staticmethod
    def generate_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(random.choices(characters, k=8))
            if UserUtil.is_strong_password(password):
                return password

    @staticmethod
    def is_strong_password(password):
        return (len(password) >= 8 and
                any(c.isupper() for c in password) and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password))


    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        pattern= r'^[a-z]+\.[a-z]+@[a-z]+\.[a-z]+$'
        return bool(re.match(pattern,email))
