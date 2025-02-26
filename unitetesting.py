import unittest
from user import User 
from userservice import UserService
from userUtil import UserUtil
from datetime import datetime

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(67886871, "John", "Doe", "john.doe@example.com", "Pass@123", datetime(2000, 5, 15))

    def test_get_details(self):
        self.assertEqual(self.user.get_details(), "ID: 67886871 Name: John Surname: Doe Email:john.doe@example.com")

    def test_get_age(self):
        expected_age = datetime.now().year - 2000
        if (datetime.today().month, datetime.today().day)< (5,15):
            expected_age -=1
        self.assertEqual(self.user.get_age(), expected_age)
        

class TestUserService(unittest.TestCase):
    def setUp(self):
        UserService.users = {}  
        self.user1 = User(1, "John", "Doe", "john.doe@example.com", "Pass@123", datetime(1998, 6, 10))
        self.user2 = User(2, "Jane", "Smith", "jane.smith@example.com", "Test@456", datetime(1995, 9, 22))
        
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)

    def test_add_user(self):
        self.assertIn(1, UserService.users)
        self.assertIn(2, UserService.users)

    def test_find_user(self):
        self.assertEqual(UserService.find_user(1), self.user1)
        self.assertIsNone(UserService.find_user(999))  

    def test_delete_user(self):
        UserService.delete_user(1)
        self.assertNotIn(1, UserService.users)

    def test_update_user(self):
        updated_user = User(1, "John", "Doe", "john.new@example.com", "NewPass@789", datetime(1998, 6, 10))
        UserService.update_user(1, updated_user)
        self.assertEqual(UserService.users[1].email, "john.new@example.com")

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 2)


class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(str(user_id).startswith(str(datetime.now().year)[-2:]))
        self.assertEqual(len(str(user_id)), 9)

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(len(password) >= 8)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()-_" for c in password))

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("Strong@123"))
        self.assertFalse(UserUtil.is_strong_password("weakpass"))

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@example.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("johndoe@example.com"))

if __name__ == "__main__":
    unittest.main()
