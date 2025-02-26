from user import User
from  userUtil import UserUtil
from userservice import UserService
from datetime import datetime

if __name__=='__main__':
    name=input('Enter your name: ')
    surname=input('Enter your surname: ')
    p1 = User(
    UserUtil.generate_user_id(),
    name,
    surname,
    email=UserUtil.generate_email(name, surname, 'example.com'),
    password=UserUtil.generate_password(),
    birthday=datetime(2005, 10, 17),)
    
    
    p2 = User(
    UserUtil.generate_user_id(),
    'Meerim',
    'Askarbekova', 
    email=UserUtil.generate_email( 'Meerim', 'Askarbekova','example.com'),
    password=UserUtil.generate_password(),
    birthday=datetime(2005, 12, 8),)
    
    print(p1.get_details())
    print(p1.get_age())
    
    UserService.add_user(p1)
    print(p2.get_details())